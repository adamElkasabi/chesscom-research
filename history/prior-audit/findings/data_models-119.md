# data_models — findings 11801–11900

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-12075"></a>
## FND-12075: chesscom.user_properties.v1.UserSettingsProperty.notification_web_lesson_and_practice = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_lesson_and_practice = 10;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6398.

```text
 {
  int32 gameplay_challenge_max_rating = 9;
  }
  oneof _notification_web_lesson_and_practice {
  bool notification_web_lesson_and_practice = 10;
  }
  oneof _board_play_sounds {
  bool board_play_sounds = 11;
  }
  oneof _notification_email_new_content {
  bool notification_email_new_content = 12;
  }
  oneof _notification_email_new_social_trophy {
  bool notification_email_new_social_trophy = 13;
  }
  oneof _boa
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12076"></a>
## FND-12076: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_play_sounds

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_play_sounds {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6452.

```text
eof _notification_web_lesson_and_practice {
  bool notification_web_lesson_and_practice = 10;
  }
  oneof _board_play_sounds {
  bool board_play_sounds = 11;
  }
  oneof _notification_email_new_content {
  bool notification_email_new_content = 12;
  }
  oneof _notification_email_new_social_trophy {
  bool notification_email_new_social_trophy = 13;
  }
  oneof _board_move_method {
  string board_move_method = 14;
  }

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12077"></a>
## FND-12077: chesscom.user_properties.v1.UserSettingsProperty.board_play_sounds = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool board_play_sounds = 11;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6481.

```text
and_practice {
  bool notification_web_lesson_and_practice = 10;
  }
  oneof _board_play_sounds {
  bool board_play_sounds = 11;
  }
  oneof _notification_email_new_content {
  bool notification_email_new_content = 12;
  }
  oneof _notification_email_new_social_trophy {
  bool notification_email_new_social_trophy = 13;
  }
  oneof _board_move_method {
  string board_move_method = 14;
  }
  oneof _board_sound_theme {

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12078"></a>
## FND-12078: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_new_content

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_new_content {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6516.

```text
web_lesson_and_practice = 10;
  }
  oneof _board_play_sounds {
  bool board_play_sounds = 11;
  }
  oneof _notification_email_new_content {
  bool notification_email_new_content = 12;
  }
  oneof _notification_email_new_social_trophy {
  bool notification_email_new_social_trophy = 13;
  }
  oneof _board_move_method {
  string board_move_method = 14;
  }
  oneof _board_sound_theme {
  string board_sound_theme = 15;
  
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12079"></a>
## FND-12079: chesscom.user_properties.v1.UserSettingsProperty.notification_email_new_content = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_new_content = 12;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6558.

```text
_board_play_sounds {
  bool board_play_sounds = 11;
  }
  oneof _notification_email_new_content {
  bool notification_email_new_content = 12;
  }
  oneof _notification_email_new_social_trophy {
  bool notification_email_new_social_trophy = 13;
  }
  oneof _board_move_method {
  string board_move_method = 14;
  }
  oneof _board_sound_theme {
  string board_sound_theme = 15;
  }
  oneof _notification_email_news_and_ann
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12080"></a>
## FND-12080: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_new_social_trophy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_new_social_trophy {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6606.

```text
11;
  }
  oneof _notification_email_new_content {
  bool notification_email_new_content = 12;
  }
  oneof _notification_email_new_social_trophy {
  bool notification_email_new_social_trophy = 13;
  }
  oneof _board_move_method {
  string board_move_method = 14;
  }
  oneof _board_sound_theme {
  string board_sound_theme = 15;
  }
  oneof _notification_email_news_and_announcements {
  bool notification_email_news_and_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12081"></a>
## FND-12081: chesscom.user_properties.v1.UserSettingsProperty.notification_email_new_social_trophy = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_new_social_trophy = 13;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6654.

```text
{
  bool notification_email_new_content = 12;
  }
  oneof _notification_email_new_social_trophy {
  bool notification_email_new_social_trophy = 13;
  }
  oneof _board_move_method {
  string board_move_method = 14;
  }
  oneof _board_sound_theme {
  string board_sound_theme = 15;
  }
  oneof _notification_email_news_and_announcements {
  bool notification_email_news_and_announcements = 16;
  }
  oneof _notification_mo
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12082"></a>
## FND-12082: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_move_method

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_move_method {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6708.

```text
eof _notification_email_new_social_trophy {
  bool notification_email_new_social_trophy = 13;
  }
  oneof _board_move_method {
  string board_move_method = 14;
  }
  oneof _board_sound_theme {
  string board_sound_theme = 15;
  }
  oneof _notification_email_news_and_announcements {
  bool notification_email_news_and_announcements = 16;
  }
  oneof _notification_mobile_friend_activity_updates {
  bool notification_mob
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12083"></a>
## FND-12083: chesscom.user_properties.v1.UserSettingsProperty.board_move_method = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string board_move_method = 14;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6737.

```text
ocial_trophy {
  bool notification_email_new_social_trophy = 13;
  }
  oneof _board_move_method {
  string board_move_method = 14;
  }
  oneof _board_sound_theme {
  string board_sound_theme = 15;
  }
  oneof _notification_email_news_and_announcements {
  bool notification_email_news_and_announcements = 16;
  }
  oneof _notification_mobile_friend_activity_updates {
  bool notification_mobile_friend_activity_updates =
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12084"></a>
## FND-12084: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_sound_theme

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_sound_theme {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6774.

```text
ail_new_social_trophy = 13;
  }
  oneof _board_move_method {
  string board_move_method = 14;
  }
  oneof _board_sound_theme {
  string board_sound_theme = 15;
  }
  oneof _notification_email_news_and_announcements {
  bool notification_email_news_and_announcements = 16;
  }
  oneof _notification_mobile_friend_activity_updates {
  bool notification_mobile_friend_activity_updates = 17;
  }
  oneof _board_move_list_sty
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12085"></a>
## FND-12085: chesscom.user_properties.v1.UserSettingsProperty.board_sound_theme = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string board_sound_theme = 15;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6803.

```text
 }
  oneof _board_move_method {
  string board_move_method = 14;
  }
  oneof _board_sound_theme {
  string board_sound_theme = 15;
  }
  oneof _notification_email_news_and_announcements {
  bool notification_email_news_and_announcements = 16;
  }
  oneof _notification_mobile_friend_activity_updates {
  bool notification_mobile_friend_activity_updates = 17;
  }
  oneof _board_move_list_style {
  string board_move_list
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12086"></a>
## FND-12086: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_news_and_announcements

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_news_and_announcements {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6840.

```text
ing board_move_method = 14;
  }
  oneof _board_sound_theme {
  string board_sound_theme = 15;
  }
  oneof _notification_email_news_and_announcements {
  bool notification_email_news_and_announcements = 16;
  }
  oneof _notification_mobile_friend_activity_updates {
  bool notification_mobile_friend_activity_updates = 17;
  }
  oneof _board_move_list_style {
  string board_move_list_style = 18;
  }
  oneof _notificatio
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12087"></a>
## FND-12087: chesscom.user_properties.v1.UserSettingsProperty.notification_email_news_and_announcements = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_news_and_announcements = 16;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6893.

```text
theme {
  string board_sound_theme = 15;
  }
  oneof _notification_email_news_and_announcements {
  bool notification_email_news_and_announcements = 16;
  }
  oneof _notification_mobile_friend_activity_updates {
  bool notification_mobile_friend_activity_updates = 17;
  }
  oneof _board_move_list_style {
  string board_move_list_style = 18;
  }
  oneof _notification_mobile_recommended_match {
  bool notification_mobi
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12088"></a>
## FND-12088: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_friend_activity_updates

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_friend_activity_updates {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 6952.

```text
ication_email_news_and_announcements {
  bool notification_email_news_and_announcements = 16;
  }
  oneof _notification_mobile_friend_activity_updates {
  bool notification_mobile_friend_activity_updates = 17;
  }
  oneof _board_move_list_style {
  string board_move_list_style = 18;
  }
  oneof _notification_mobile_recommended_match {
  bool notification_mobile_recommended_match = 19;
  }
  oneof _notification_email_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12089"></a>
## FND-12089: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_friend_activity_updates = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_friend_activity_updates = 17;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7007.

```text
ion_email_news_and_announcements = 16;
  }
  oneof _notification_mobile_friend_activity_updates {
  bool notification_mobile_friend_activity_updates = 17;
  }
  oneof _board_move_list_style {
  string board_move_list_style = 18;
  }
  oneof _notification_mobile_recommended_match {
  bool notification_mobile_recommended_match = 19;
  }
  oneof _notification_email_new_comment {
  bool notification_email_new_comment = 2
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12090"></a>
## FND-12090: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_move_list_style

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_move_list_style {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7068.

```text
ion_mobile_friend_activity_updates {
  bool notification_mobile_friend_activity_updates = 17;
  }
  oneof _board_move_list_style {
  string board_move_list_style = 18;
  }
  oneof _notification_mobile_recommended_match {
  bool notification_mobile_recommended_match = 19;
  }
  oneof _notification_email_new_comment {
  bool notification_email_new_comment = 20;
  }
  oneof _gameplay_daily_confirm_move {
  bool gameplay
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12091"></a>
## FND-12091: chesscom.user_properties.v1.UserSettingsProperty.board_move_list_style = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string board_move_list_style = 18;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7101.

```text
s {
  bool notification_mobile_friend_activity_updates = 17;
  }
  oneof _board_move_list_style {
  string board_move_list_style = 18;
  }
  oneof _notification_mobile_recommended_match {
  bool notification_mobile_recommended_match = 19;
  }
  oneof _notification_email_new_comment {
  bool notification_email_new_comment = 20;
  }
  oneof _gameplay_daily_confirm_move {
  bool gameplay_daily_confirm_move = 21;
  }
  o
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12092"></a>
## FND-12092: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_recommended_match

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_recommended_match {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7142.

```text
ivity_updates = 17;
  }
  oneof _board_move_list_style {
  string board_move_list_style = 18;
  }
  oneof _notification_mobile_recommended_match {
  bool notification_mobile_recommended_match = 19;
  }
  oneof _notification_email_new_comment {
  bool notification_email_new_comment = 20;
  }
  oneof _gameplay_daily_confirm_move {
  bool gameplay_daily_confirm_move = 21;
  }
  oneof _gameplay_seek_min_rating {
  int32 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12093"></a>
## FND-12093: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_recommended_match = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_recommended_match = 19;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7191.

```text
style {
  string board_move_list_style = 18;
  }
  oneof _notification_mobile_recommended_match {
  bool notification_mobile_recommended_match = 19;
  }
  oneof _notification_email_new_comment {
  bool notification_email_new_comment = 20;
  }
  oneof _gameplay_daily_confirm_move {
  bool gameplay_daily_confirm_move = 21;
  }
  oneof _gameplay_seek_min_rating {
  int32 gameplay_seek_min_rating = 22;
  }
  oneof _notif
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12094"></a>
## FND-12094: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_new_comment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_new_comment {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7246.

```text
f _notification_mobile_recommended_match {
  bool notification_mobile_recommended_match = 19;
  }
  oneof _notification_email_new_comment {
  bool notification_email_new_comment = 20;
  }
  oneof _gameplay_daily_confirm_move {
  bool gameplay_daily_confirm_move = 21;
  }
  oneof _gameplay_seek_min_rating {
  int32 gameplay_seek_min_rating = 22;
  }
  oneof _notification_web_new_user_comment {
  bool notification_web_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12095"></a>
## FND-12095: chesscom.user_properties.v1.UserSettingsProperty.notification_email_new_comment = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_new_comment = 20;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7288.

```text

  bool notification_mobile_recommended_match = 19;
  }
  oneof _notification_email_new_comment {
  bool notification_email_new_comment = 20;
  }
  oneof _gameplay_daily_confirm_move {
  bool gameplay_daily_confirm_move = 21;
  }
  oneof _gameplay_seek_min_rating {
  int32 gameplay_seek_min_rating = 22;
  }
  oneof _notification_web_new_user_comment {
  bool notification_web_new_user_comment = 23;
  }
  oneof _board_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12096"></a>
## FND-12096: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_daily_confirm_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_daily_confirm_move {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7336.

```text
19;
  }
  oneof _notification_email_new_comment {
  bool notification_email_new_comment = 20;
  }
  oneof _gameplay_daily_confirm_move {
  bool gameplay_daily_confirm_move = 21;
  }
  oneof _gameplay_seek_min_rating {
  int32 gameplay_seek_min_rating = 22;
  }
  oneof _notification_web_new_user_comment {
  bool notification_web_new_user_comment = 23;
  }
  oneof _board_show_legal_moves {
  bool board_show_legal_moves
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12097"></a>
## FND-12097: chesscom.user_properties.v1.UserSettingsProperty.gameplay_daily_confirm_move = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_daily_confirm_move = 21;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7375.

```text
_comment {
  bool notification_email_new_comment = 20;
  }
  oneof _gameplay_daily_confirm_move {
  bool gameplay_daily_confirm_move = 21;
  }
  oneof _gameplay_seek_min_rating {
  int32 gameplay_seek_min_rating = 22;
  }
  oneof _notification_web_new_user_comment {
  bool notification_web_new_user_comment = 23;
  }
  oneof _board_show_legal_moves {
  bool board_show_legal_moves = 24;
  }
  oneof _gameplay_show_times
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12098"></a>
## FND-12098: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_seek_min_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_seek_min_rating {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7420.

```text
ent = 20;
  }
  oneof _gameplay_daily_confirm_move {
  bool gameplay_daily_confirm_move = 21;
  }
  oneof _gameplay_seek_min_rating {
  int32 gameplay_seek_min_rating = 22;
  }
  oneof _notification_web_new_user_comment {
  bool notification_web_new_user_comment = 23;
  }
  oneof _board_show_legal_moves {
  bool board_show_legal_moves = 24;
  }
  oneof _gameplay_show_timestamps {
  bool gameplay_show_timestamps = 25;
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12099"></a>
## FND-12099: chesscom.user_properties.v1.UserSettingsProperty.gameplay_seek_min_rating = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 gameplay_seek_min_rating = 22;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7456.

```text
y_confirm_move {
  bool gameplay_daily_confirm_move = 21;
  }
  oneof _gameplay_seek_min_rating {
  int32 gameplay_seek_min_rating = 22;
  }
  oneof _notification_web_new_user_comment {
  bool notification_web_new_user_comment = 23;
  }
  oneof _board_show_legal_moves {
  bool board_show_legal_moves = 24;
  }
  oneof _gameplay_show_timestamps {
  bool gameplay_show_timestamps = 25;
  }
  oneof _notification_web_game_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12100"></a>
## FND-12100: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_new_user_comment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_new_user_comment {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7499.

```text
irm_move = 21;
  }
  oneof _gameplay_seek_min_rating {
  int32 gameplay_seek_min_rating = 22;
  }
  oneof _notification_web_new_user_comment {
  bool notification_web_new_user_comment = 23;
  }
  oneof _board_show_legal_moves {
  bool board_show_legal_moves = 24;
  }
  oneof _gameplay_show_timestamps {
  bool gameplay_show_timestamps = 25;
  }
  oneof _notification_web_game_event {
  bool notification_web_game_event 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12101"></a>
## FND-12101: chesscom.user_properties.v1.UserSettingsProperty.notification_web_new_user_comment = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_new_user_comment = 23;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7544.

```text
_rating {
  int32 gameplay_seek_min_rating = 22;
  }
  oneof _notification_web_new_user_comment {
  bool notification_web_new_user_comment = 23;
  }
  oneof _board_show_legal_moves {
  bool board_show_legal_moves = 24;
  }
  oneof _gameplay_show_timestamps {
  bool gameplay_show_timestamps = 25;
  }
  oneof _notification_web_game_event {
  bool notification_web_game_event = 26;
  }
  oneof _privacy_friends_list_priva
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12102"></a>
## FND-12102: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_show_legal_moves

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_show_legal_moves {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7595.

```text
}
  oneof _notification_web_new_user_comment {
  bool notification_web_new_user_comment = 23;
  }
  oneof _board_show_legal_moves {
  bool board_show_legal_moves = 24;
  }
  oneof _gameplay_show_timestamps {
  bool gameplay_show_timestamps = 25;
  }
  oneof _notification_web_game_event {
  bool notification_web_game_event = 26;
  }
  oneof _privacy_friends_list_privacy {
  string privacy_friends_list_privacy = 27;
  
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12103"></a>
## FND-12103: chesscom.user_properties.v1.UserSettingsProperty.board_show_legal_moves = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool board_show_legal_moves = 24;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7629.

```text
er_comment {
  bool notification_web_new_user_comment = 23;
  }
  oneof _board_show_legal_moves {
  bool board_show_legal_moves = 24;
  }
  oneof _gameplay_show_timestamps {
  bool gameplay_show_timestamps = 25;
  }
  oneof _notification_web_game_event {
  bool notification_web_game_event = 26;
  }
  oneof _privacy_friends_list_privacy {
  string privacy_friends_list_privacy = 27;
  }
  oneof _notification_web_vote_c
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12104"></a>
## FND-12104: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_show_timestamps

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_show_timestamps {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7669.

```text
_user_comment = 23;
  }
  oneof _board_show_legal_moves {
  bool board_show_legal_moves = 24;
  }
  oneof _gameplay_show_timestamps {
  bool gameplay_show_timestamps = 25;
  }
  oneof _notification_web_game_event {
  bool notification_web_game_event = 26;
  }
  oneof _privacy_friends_list_privacy {
  string privacy_friends_list_privacy = 27;
  }
  oneof _notification_web_vote_chess {
  bool notification_web_vote_ches
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12105"></a>
## FND-12105: chesscom.user_properties.v1.UserSettingsProperty.gameplay_show_timestamps = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_show_timestamps = 25;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7705.

```text
rd_show_legal_moves {
  bool board_show_legal_moves = 24;
  }
  oneof _gameplay_show_timestamps {
  bool gameplay_show_timestamps = 25;
  }
  oneof _notification_web_game_event {
  bool notification_web_game_event = 26;
  }
  oneof _privacy_friends_list_privacy {
  string privacy_friends_list_privacy = 27;
  }
  oneof _notification_web_vote_chess {
  bool notification_web_vote_chess = 28;
  }
  oneof _board_coordinat
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12106"></a>
## FND-12106: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_game_event

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_game_event {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7747.

```text
gal_moves = 24;
  }
  oneof _gameplay_show_timestamps {
  bool gameplay_show_timestamps = 25;
  }
  oneof _notification_web_game_event {
  bool notification_web_game_event = 26;
  }
  oneof _privacy_friends_list_privacy {
  string privacy_friends_list_privacy = 27;
  }
  oneof _notification_web_vote_chess {
  bool notification_web_vote_chess = 28;
  }
  oneof _board_coordinates {
  string board_coordinates = 29;
  }

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12107"></a>
## FND-12107: chesscom.user_properties.v1.UserSettingsProperty.notification_web_game_event = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_game_event = 26;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7786.

```text
how_timestamps {
  bool gameplay_show_timestamps = 25;
  }
  oneof _notification_web_game_event {
  bool notification_web_game_event = 26;
  }
  oneof _privacy_friends_list_privacy {
  string privacy_friends_list_privacy = 27;
  }
  oneof _notification_web_vote_chess {
  bool notification_web_vote_chess = 28;
  }
  oneof _board_coordinates {
  string board_coordinates = 29;
  }
  oneof _gameplay_live_play_multiple_ga
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12108"></a>
## FND-12108: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._privacy_friends_list_privacy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _privacy_friends_list_privacy {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7831.

```text
mps = 25;
  }
  oneof _notification_web_game_event {
  bool notification_web_game_event = 26;
  }
  oneof _privacy_friends_list_privacy {
  string privacy_friends_list_privacy = 27;
  }
  oneof _notification_web_vote_chess {
  bool notification_web_vote_chess = 28;
  }
  oneof _board_coordinates {
  string board_coordinates = 29;
  }
  oneof _gameplay_live_play_multiple_games {
  bool gameplay_live_play_multiple_game
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12109"></a>
## FND-12109: chesscom.user_properties.v1.UserSettingsProperty.privacy_friends_list_privacy = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string privacy_friends_list_privacy = 27;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7871.

```text
game_event {
  bool notification_web_game_event = 26;
  }
  oneof _privacy_friends_list_privacy {
  string privacy_friends_list_privacy = 27;
  }
  oneof _notification_web_vote_chess {
  bool notification_web_vote_chess = 28;
  }
  oneof _board_coordinates {
  string board_coordinates = 29;
  }
  oneof _gameplay_live_play_multiple_games {
  bool gameplay_live_play_multiple_games = 30;
  }
  oneof _notification_email_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12110"></a>
## FND-12110: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_vote_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_vote_chess {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7919.

```text
= 26;
  }
  oneof _privacy_friends_list_privacy {
  string privacy_friends_list_privacy = 27;
  }
  oneof _notification_web_vote_chess {
  bool notification_web_vote_chess = 28;
  }
  oneof _board_coordinates {
  string board_coordinates = 29;
  }
  oneof _gameplay_live_play_multiple_games {
  bool gameplay_live_play_multiple_games = 30;
  }
  oneof _notification_email_chess_tv {
  bool notification_email_chess_tv = 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12111"></a>
## FND-12111: chesscom.user_properties.v1.UserSettingsProperty.notification_web_vote_chess = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_vote_chess = 28;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 7958.

```text
_privacy {
  string privacy_friends_list_privacy = 27;
  }
  oneof _notification_web_vote_chess {
  bool notification_web_vote_chess = 28;
  }
  oneof _board_coordinates {
  string board_coordinates = 29;
  }
  oneof _gameplay_live_play_multiple_games {
  bool gameplay_live_play_multiple_games = 30;
  }
  oneof _notification_email_chess_tv {
  bool notification_email_chess_tv = 31;
  }
  oneof _gameplay_live_auto_pro
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12112"></a>
## FND-12112: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_coordinates

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_coordinates {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8003.

```text
acy = 27;
  }
  oneof _notification_web_vote_chess {
  bool notification_web_vote_chess = 28;
  }
  oneof _board_coordinates {
  string board_coordinates = 29;
  }
  oneof _gameplay_live_play_multiple_games {
  bool gameplay_live_play_multiple_games = 30;
  }
  oneof _notification_email_chess_tv {
  bool notification_email_chess_tv = 31;
  }
  oneof _gameplay_live_auto_promote_queen {
  bool gameplay_live_auto_promot
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12113"></a>
## FND-12113: chesscom.user_properties.v1.UserSettingsProperty.board_coordinates = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string board_coordinates = 29;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8032.

```text
cation_web_vote_chess {
  bool notification_web_vote_chess = 28;
  }
  oneof _board_coordinates {
  string board_coordinates = 29;
  }
  oneof _gameplay_live_play_multiple_games {
  bool gameplay_live_play_multiple_games = 30;
  }
  oneof _notification_email_chess_tv {
  bool notification_email_chess_tv = 31;
  }
  oneof _gameplay_live_auto_promote_queen {
  bool gameplay_live_auto_promote_queen = 32;
  }
  oneof _no
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12114"></a>
## FND-12114: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_play_multiple_games

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_play_multiple_games {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8069.

```text
cation_web_vote_chess = 28;
  }
  oneof _board_coordinates {
  string board_coordinates = 29;
  }
  oneof _gameplay_live_play_multiple_games {
  bool gameplay_live_play_multiple_games = 30;
  }
  oneof _notification_email_chess_tv {
  bool notification_email_chess_tv = 31;
  }
  oneof _gameplay_live_auto_promote_queen {
  bool gameplay_live_auto_promote_queen = 32;
  }
  oneof _notification_mobile_new_comment {
  boo
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12115"></a>
## FND-12115: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_play_multiple_games = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_live_play_multiple_games = 30;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8114.

```text
d_coordinates {
  string board_coordinates = 29;
  }
  oneof _gameplay_live_play_multiple_games {
  bool gameplay_live_play_multiple_games = 30;
  }
  oneof _notification_email_chess_tv {
  bool notification_email_chess_tv = 31;
  }
  oneof _gameplay_live_auto_promote_queen {
  bool gameplay_live_auto_promote_queen = 32;
  }
  oneof _notification_mobile_new_comment {
  bool notification_mobile_new_comment = 33;
  }
 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12116"></a>
## FND-12116: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_chess_tv

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_chess_tv {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8165.

```text
}
  oneof _gameplay_live_play_multiple_games {
  bool gameplay_live_play_multiple_games = 30;
  }
  oneof _notification_email_chess_tv {
  bool notification_email_chess_tv = 31;
  }
  oneof _gameplay_live_auto_promote_queen {
  bool gameplay_live_auto_promote_queen = 32;
  }
  oneof _notification_mobile_new_comment {
  bool notification_mobile_new_comment = 33;
  }
  oneof _gameplay_daily_max_days_per_move {
  int32 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12117"></a>
## FND-12117: chesscom.user_properties.v1.UserSettingsProperty.notification_email_chess_tv = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_chess_tv = 31;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8204.

```text
games {
  bool gameplay_live_play_multiple_games = 30;
  }
  oneof _notification_email_chess_tv {
  bool notification_email_chess_tv = 31;
  }
  oneof _gameplay_live_auto_promote_queen {
  bool gameplay_live_auto_promote_queen = 32;
  }
  oneof _notification_mobile_new_comment {
  bool notification_mobile_new_comment = 33;
  }
  oneof _gameplay_daily_max_days_per_move {
  int32 gameplay_daily_max_days_per_move = 34;

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12118"></a>
## FND-12118: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_auto_promote_queen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_auto_promote_queen {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8249.

```text
mes = 30;
  }
  oneof _notification_email_chess_tv {
  bool notification_email_chess_tv = 31;
  }
  oneof _gameplay_live_auto_promote_queen {
  bool gameplay_live_auto_promote_queen = 32;
  }
  oneof _notification_mobile_new_comment {
  bool notification_mobile_new_comment = 33;
  }
  oneof _gameplay_daily_max_days_per_move {
  int32 gameplay_daily_max_days_per_move = 34;
  }
  oneof _gameplay_confirm_resign {
  bool
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12119"></a>
## FND-12119: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_auto_promote_queen = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_live_auto_promote_queen = 32;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8293.

```text
ess_tv {
  bool notification_email_chess_tv = 31;
  }
  oneof _gameplay_live_auto_promote_queen {
  bool gameplay_live_auto_promote_queen = 32;
  }
  oneof _notification_mobile_new_comment {
  bool notification_mobile_new_comment = 33;
  }
  oneof _gameplay_daily_max_days_per_move {
  int32 gameplay_daily_max_days_per_move = 34;
  }
  oneof _gameplay_confirm_resign {
  bool gameplay_confirm_resign = 35;
  }
  oneof _
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12120"></a>
## FND-12120: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_new_comment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_new_comment {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8343.

```text
  }
  oneof _gameplay_live_auto_promote_queen {
  bool gameplay_live_auto_promote_queen = 32;
  }
  oneof _notification_mobile_new_comment {
  bool notification_mobile_new_comment = 33;
  }
  oneof _gameplay_daily_max_days_per_move {
  int32 gameplay_daily_max_days_per_move = 34;
  }
  oneof _gameplay_confirm_resign {
  bool gameplay_confirm_resign = 35;
  }
  oneof _gameplay_live_seek_base_time_variants {
  int32 ga
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12121"></a>
## FND-12121: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_new_comment = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_new_comment = 33;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8386.

```text
en {
  bool gameplay_live_auto_promote_queen = 32;
  }
  oneof _notification_mobile_new_comment {
  bool notification_mobile_new_comment = 33;
  }
  oneof _gameplay_daily_max_days_per_move {
  int32 gameplay_daily_max_days_per_move = 34;
  }
  oneof _gameplay_confirm_resign {
  bool gameplay_confirm_resign = 35;
  }
  oneof _gameplay_live_seek_base_time_variants {
  int32 gameplay_live_seek_base_time_variants = 36;
 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12122"></a>
## FND-12122: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_daily_max_days_per_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_daily_max_days_per_move {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8435.

```text
;
  }
  oneof _notification_mobile_new_comment {
  bool notification_mobile_new_comment = 33;
  }
  oneof _gameplay_daily_max_days_per_move {
  int32 gameplay_daily_max_days_per_move = 34;
  }
  oneof _gameplay_confirm_resign {
  bool gameplay_confirm_resign = 35;
  }
  oneof _gameplay_live_seek_base_time_variants {
  int32 gameplay_live_seek_base_time_variants = 36;
  }
  oneof _notification_email_lesson_quota {
  b
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12123"></a>
## FND-12123: chesscom.user_properties.v1.UserSettingsProperty.gameplay_daily_max_days_per_move = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 gameplay_daily_max_days_per_move = 34;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8479.

```text
nt {
  bool notification_mobile_new_comment = 33;
  }
  oneof _gameplay_daily_max_days_per_move {
  int32 gameplay_daily_max_days_per_move = 34;
  }
  oneof _gameplay_confirm_resign {
  bool gameplay_confirm_resign = 35;
  }
  oneof _gameplay_live_seek_base_time_variants {
  int32 gameplay_live_seek_base_time_variants = 36;
  }
  oneof _notification_email_lesson_quota {
  bool notification_email_lesson_quota = 37;
  
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12124"></a>
## FND-12124: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_confirm_resign

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_confirm_resign {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8530.

```text
 }
  oneof _gameplay_daily_max_days_per_move {
  int32 gameplay_daily_max_days_per_move = 34;
  }
  oneof _gameplay_confirm_resign {
  bool gameplay_confirm_resign = 35;
  }
  oneof _gameplay_live_seek_base_time_variants {
  int32 gameplay_live_seek_base_time_variants = 36;
  }
  oneof _notification_email_lesson_quota {
  bool notification_email_lesson_quota = 37;
  }
  oneof _notification_email_lesson_and_practice {
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12125"></a>
## FND-12125: chesscom.user_properties.v1.UserSettingsProperty.gameplay_confirm_resign = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_confirm_resign = 35;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8565.

```text
_per_move {
  int32 gameplay_daily_max_days_per_move = 34;
  }
  oneof _gameplay_confirm_resign {
  bool gameplay_confirm_resign = 35;
  }
  oneof _gameplay_live_seek_base_time_variants {
  int32 gameplay_live_seek_base_time_variants = 36;
  }
  oneof _notification_email_lesson_quota {
  bool notification_email_lesson_quota = 37;
  }
  oneof _notification_email_lesson_and_practice {
  bool notification_email_lesson_a
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12126"></a>
## FND-12126: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_seek_base_time_variants

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_seek_base_time_variants {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8606.

```text
ys_per_move = 34;
  }
  oneof _gameplay_confirm_resign {
  bool gameplay_confirm_resign = 35;
  }
  oneof _gameplay_live_seek_base_time_variants {
  int32 gameplay_live_seek_base_time_variants = 36;
  }
  oneof _notification_email_lesson_quota {
  bool notification_email_lesson_quota = 37;
  }
  oneof _notification_email_lesson_and_practice {
  bool notification_email_lesson_and_practice = 38;
  }
  oneof _gameplay_l
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12127"></a>
## FND-12127: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_seek_base_time_variants = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 gameplay_live_seek_base_time_variants = 36;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8655.

```text
esign {
  bool gameplay_confirm_resign = 35;
  }
  oneof _gameplay_live_seek_base_time_variants {
  int32 gameplay_live_seek_base_time_variants = 36;
  }
  oneof _notification_email_lesson_quota {
  bool notification_email_lesson_quota = 37;
  }
  oneof _notification_email_lesson_and_practice {
  bool notification_email_lesson_and_practice = 38;
  }
  oneof _gameplay_live_challenge_alerts {
  string gameplay_live_cha
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12128"></a>
## FND-12128: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_lesson_quota

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_lesson_quota {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8711.

```text
 _gameplay_live_seek_base_time_variants {
  int32 gameplay_live_seek_base_time_variants = 36;
  }
  oneof _notification_email_lesson_quota {
  bool notification_email_lesson_quota = 37;
  }
  oneof _notification_email_lesson_and_practice {
  bool notification_email_lesson_and_practice = 38;
  }
  oneof _gameplay_live_challenge_alerts {
  string gameplay_live_challenge_alerts = 39;
  }
  oneof _board_white_always_on_b
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12129"></a>
## FND-12129: chesscom.user_properties.v1.UserSettingsProperty.notification_email_lesson_quota = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_lesson_quota = 37;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8754.

```text
 int32 gameplay_live_seek_base_time_variants = 36;
  }
  oneof _notification_email_lesson_quota {
  bool notification_email_lesson_quota = 37;
  }
  oneof _notification_email_lesson_and_practice {
  bool notification_email_lesson_and_practice = 38;
  }
  oneof _gameplay_live_challenge_alerts {
  string gameplay_live_challenge_alerts = 39;
  }
  oneof _board_white_always_on_bottom {
  bool board_white_always_on_bottom
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12130"></a>
## FND-12130: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_lesson_and_practice

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_lesson_and_practice {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8803.

```text
;
  }
  oneof _notification_email_lesson_quota {
  bool notification_email_lesson_quota = 37;
  }
  oneof _notification_email_lesson_and_practice {
  bool notification_email_lesson_and_practice = 38;
  }
  oneof _gameplay_live_challenge_alerts {
  string gameplay_live_challenge_alerts = 39;
  }
  oneof _board_white_always_on_bottom {
  bool board_white_always_on_bottom = 40;
  }
  oneof _notification_web_new_comment 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12131"></a>
## FND-12131: chesscom.user_properties.v1.UserSettingsProperty.notification_email_lesson_and_practice = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_lesson_and_practice = 38;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8853.

```text
 bool notification_email_lesson_quota = 37;
  }
  oneof _notification_email_lesson_and_practice {
  bool notification_email_lesson_and_practice = 38;
  }
  oneof _gameplay_live_challenge_alerts {
  string gameplay_live_challenge_alerts = 39;
  }
  oneof _board_white_always_on_bottom {
  bool board_white_always_on_bottom = 40;
  }
  oneof _notification_web_new_comment {
  bool notification_web_new_comment = 41;
  }
  
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12132"></a>
## FND-12132: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_challenge_alerts

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_challenge_alerts {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8909.

```text
_notification_email_lesson_and_practice {
  bool notification_email_lesson_and_practice = 38;
  }
  oneof _gameplay_live_challenge_alerts {
  string gameplay_live_challenge_alerts = 39;
  }
  oneof _board_white_always_on_bottom {
  bool board_white_always_on_bottom = 40;
  }
  oneof _notification_web_new_comment {
  bool notification_web_new_comment = 41;
  }
  oneof _privacy_insights_privacy {
  string privacy_insig
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12133"></a>
## FND-12133: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_challenge_alerts = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string gameplay_live_challenge_alerts = 39;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 8951.

```text
  bool notification_email_lesson_and_practice = 38;
  }
  oneof _gameplay_live_challenge_alerts {
  string gameplay_live_challenge_alerts = 39;
  }
  oneof _board_white_always_on_bottom {
  bool board_white_always_on_bottom = 40;
  }
  oneof _notification_web_new_comment {
  bool notification_web_new_comment = 41;
  }
  oneof _privacy_insights_privacy {
  string privacy_insights_privacy = 42;
  }
  oneof _notificatio
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12134"></a>
## FND-12134: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_white_always_on_bottom

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_white_always_on_bottom {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9001.

```text
;
  }
  oneof _gameplay_live_challenge_alerts {
  string gameplay_live_challenge_alerts = 39;
  }
  oneof _board_white_always_on_bottom {
  bool board_white_always_on_bottom = 40;
  }
  oneof _notification_web_new_comment {
  bool notification_web_new_comment = 41;
  }
  oneof _privacy_insights_privacy {
  string privacy_insights_privacy = 42;
  }
  oneof _notification_web_new_content {
  bool notification_web_new_co
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12135"></a>
## FND-12135: chesscom.user_properties.v1.UserSettingsProperty.board_white_always_on_bottom = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool board_white_always_on_bottom = 40;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9041.

```text
lerts {
  string gameplay_live_challenge_alerts = 39;
  }
  oneof _board_white_always_on_bottom {
  bool board_white_always_on_bottom = 40;
  }
  oneof _notification_web_new_comment {
  bool notification_web_new_comment = 41;
  }
  oneof _privacy_insights_privacy {
  string privacy_insights_privacy = 42;
  }
  oneof _notification_web_new_content {
  bool notification_web_new_content = 43;
  }
  oneof _privacy_allow_f
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12136"></a>
## FND-12136: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_new_comment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_new_comment {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9087.

```text
s = 39;
  }
  oneof _board_white_always_on_bottom {
  bool board_white_always_on_bottom = 40;
  }
  oneof _notification_web_new_comment {
  bool notification_web_new_comment = 41;
  }
  oneof _privacy_insights_privacy {
  string privacy_insights_privacy = 42;
  }
  oneof _notification_web_new_content {
  bool notification_web_new_content = 43;
  }
  oneof _privacy_allow_friend_requests {
  bool privacy_allow_friend_r
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12137"></a>
## FND-12137: chesscom.user_properties.v1.UserSettingsProperty.notification_web_new_comment = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_new_comment = 41;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9127.

```text
on_bottom {
  bool board_white_always_on_bottom = 40;
  }
  oneof _notification_web_new_comment {
  bool notification_web_new_comment = 41;
  }
  oneof _privacy_insights_privacy {
  string privacy_insights_privacy = 42;
  }
  oneof _notification_web_new_content {
  bool notification_web_new_content = 43;
  }
  oneof _privacy_allow_friend_requests {
  bool privacy_allow_friend_requests = 44;
  }
  oneof _notification_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12138"></a>
## FND-12138: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._privacy_insights_privacy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _privacy_insights_privacy {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9173.

```text
m = 40;
  }
  oneof _notification_web_new_comment {
  bool notification_web_new_comment = 41;
  }
  oneof _privacy_insights_privacy {
  string privacy_insights_privacy = 42;
  }
  oneof _notification_web_new_content {
  bool notification_web_new_content = 43;
  }
  oneof _privacy_allow_friend_requests {
  bool privacy_allow_friend_requests = 44;
  }
  oneof _notification_mobile_lesson_quota {
  bool notification_mobi
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12139"></a>
## FND-12139: chesscom.user_properties.v1.UserSettingsProperty.privacy_insights_privacy = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string privacy_insights_privacy = 42;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9209.

```text
b_new_comment {
  bool notification_web_new_comment = 41;
  }
  oneof _privacy_insights_privacy {
  string privacy_insights_privacy = 42;
  }
  oneof _notification_web_new_content {
  bool notification_web_new_content = 43;
  }
  oneof _privacy_allow_friend_requests {
  bool privacy_allow_friend_requests = 44;
  }
  oneof _notification_mobile_lesson_quota {
  bool notification_mobile_lesson_quota = 45;
  }
  oneof _g
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12140"></a>
## FND-12140: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_new_content

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_new_content {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9253.

```text
comment = 41;
  }
  oneof _privacy_insights_privacy {
  string privacy_insights_privacy = 42;
  }
  oneof _notification_web_new_content {
  bool notification_web_new_content = 43;
  }
  oneof _privacy_allow_friend_requests {
  bool privacy_allow_friend_requests = 44;
  }
  oneof _notification_mobile_lesson_quota {
  bool notification_mobile_lesson_quota = 45;
  }
  oneof _gameplay_live_premoves {
  bool gameplay_live
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12141"></a>
## FND-12141: chesscom.user_properties.v1.UserSettingsProperty.notification_web_new_content = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_new_content = 43;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9293.

```text
hts_privacy {
  string privacy_insights_privacy = 42;
  }
  oneof _notification_web_new_content {
  bool notification_web_new_content = 43;
  }
  oneof _privacy_allow_friend_requests {
  bool privacy_allow_friend_requests = 44;
  }
  oneof _notification_mobile_lesson_quota {
  bool notification_mobile_lesson_quota = 45;
  }
  oneof _gameplay_live_premoves {
  bool gameplay_live_premoves = 46;
  }
  oneof _notificatio
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12142"></a>
## FND-12142: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._privacy_allow_friend_requests

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _privacy_allow_friend_requests {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9339.

```text
y = 42;
  }
  oneof _notification_web_new_content {
  bool notification_web_new_content = 43;
  }
  oneof _privacy_allow_friend_requests {
  bool privacy_allow_friend_requests = 44;
  }
  oneof _notification_mobile_lesson_quota {
  bool notification_mobile_lesson_quota = 45;
  }
  oneof _gameplay_live_premoves {
  bool gameplay_live_premoves = 46;
  }
  oneof _notification_mobile_new_message {
  bool notification_mob
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12143"></a>
## FND-12143: chesscom.user_properties.v1.UserSettingsProperty.privacy_allow_friend_requests = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool privacy_allow_friend_requests = 44;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9380.

```text
_content {
  bool notification_web_new_content = 43;
  }
  oneof _privacy_allow_friend_requests {
  bool privacy_allow_friend_requests = 44;
  }
  oneof _notification_mobile_lesson_quota {
  bool notification_mobile_lesson_quota = 45;
  }
  oneof _gameplay_live_premoves {
  bool gameplay_live_premoves = 46;
  }
  oneof _notification_mobile_new_message {
  bool notification_mobile_new_message = 47;
  }
  oneof _notifi
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12144"></a>
## FND-12144: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_lesson_quota

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_lesson_quota {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9427.

```text
= 43;
  }
  oneof _privacy_allow_friend_requests {
  bool privacy_allow_friend_requests = 44;
  }
  oneof _notification_mobile_lesson_quota {
  bool notification_mobile_lesson_quota = 45;
  }
  oneof _gameplay_live_premoves {
  bool gameplay_live_premoves = 46;
  }
  oneof _notification_mobile_new_message {
  bool notification_mobile_new_message = 47;
  }
  oneof _notification_web_news_and_announcements {
  bool noti
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12145"></a>
## FND-12145: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_lesson_quota = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_lesson_quota = 45;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9471.

```text
ests {
  bool privacy_allow_friend_requests = 44;
  }
  oneof _notification_mobile_lesson_quota {
  bool notification_mobile_lesson_quota = 45;
  }
  oneof _gameplay_live_premoves {
  bool gameplay_live_premoves = 46;
  }
  oneof _notification_mobile_new_message {
  bool notification_mobile_new_message = 47;
  }
  oneof _notification_web_news_and_announcements {
  bool notification_web_news_and_announcements = 48;
  
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12146"></a>
## FND-12146: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_premoves

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_premoves {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9521.

```text
  }
  oneof _notification_mobile_lesson_quota {
  bool notification_mobile_lesson_quota = 45;
  }
  oneof _gameplay_live_premoves {
  bool gameplay_live_premoves = 46;
  }
  oneof _notification_mobile_new_message {
  bool notification_mobile_new_message = 47;
  }
  oneof _notification_web_news_and_announcements {
  bool notification_web_news_and_announcements = 48;
  }
  oneof _notification_email_hero_playing {
  boo
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12147"></a>
## FND-12147: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_premoves = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_live_premoves = 46;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9555.

```text
esson_quota {
  bool notification_mobile_lesson_quota = 45;
  }
  oneof _gameplay_live_premoves {
  bool gameplay_live_premoves = 46;
  }
  oneof _notification_mobile_new_message {
  bool notification_mobile_new_message = 47;
  }
  oneof _notification_web_news_and_announcements {
  bool notification_web_news_and_announcements = 48;
  }
  oneof _notification_email_hero_playing {
  bool notification_email_hero_playing 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12148"></a>
## FND-12148: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_new_message

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_new_message {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9595.

```text
_lesson_quota = 45;
  }
  oneof _gameplay_live_premoves {
  bool gameplay_live_premoves = 46;
  }
  oneof _notification_mobile_new_message {
  bool notification_mobile_new_message = 47;
  }
  oneof _notification_web_news_and_announcements {
  bool notification_web_news_and_announcements = 48;
  }
  oneof _notification_email_hero_playing {
  bool notification_email_hero_playing = 49;
  }
  oneof _gameplay_live_evaluat
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12149"></a>
## FND-12149: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_new_message = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_new_message = 47;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9638.

```text
ive_premoves {
  bool gameplay_live_premoves = 46;
  }
  oneof _notification_mobile_new_message {
  bool notification_mobile_new_message = 47;
  }
  oneof _notification_web_news_and_announcements {
  bool notification_web_news_and_announcements = 48;
  }
  oneof _notification_email_hero_playing {
  bool notification_email_hero_playing = 49;
  }
  oneof _gameplay_live_evaluation_bar {
  bool gameplay_live_evaluation_b
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12150"></a>
## FND-12150: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_news_and_announcements

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_news_and_announcements {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9687.

```text
;
  }
  oneof _notification_mobile_new_message {
  bool notification_mobile_new_message = 47;
  }
  oneof _notification_web_news_and_announcements {
  bool notification_web_news_and_announcements = 48;
  }
  oneof _notification_email_hero_playing {
  bool notification_email_hero_playing = 49;
  }
  oneof _gameplay_live_evaluation_bar {
  bool gameplay_live_evaluation_bar = 50;
  }
  oneof _notification_mobile_vote_ch
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12151"></a>
## FND-12151: chesscom.user_properties.v1.UserSettingsProperty.notification_web_news_and_announcements = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_news_and_announcements = 48;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9738.

```text
bool notification_mobile_new_message = 47;
  }
  oneof _notification_web_news_and_announcements {
  bool notification_web_news_and_announcements = 48;
  }
  oneof _notification_email_hero_playing {
  bool notification_email_hero_playing = 49;
  }
  oneof _gameplay_live_evaluation_bar {
  bool gameplay_live_evaluation_bar = 50;
  }
  oneof _notification_mobile_vote_chess {
  bool notification_mobile_vote_chess = 51;
 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12152"></a>
## FND-12152: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_hero_playing

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_hero_playing {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9795.

```text
otification_web_news_and_announcements {
  bool notification_web_news_and_announcements = 48;
  }
  oneof _notification_email_hero_playing {
  bool notification_email_hero_playing = 49;
  }
  oneof _gameplay_live_evaluation_bar {
  bool gameplay_live_evaluation_bar = 50;
  }
  oneof _notification_mobile_vote_chess {
  bool notification_mobile_vote_chess = 51;
  }
  oneof _notification_web_new_message {
  bool notific
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12153"></a>
## FND-12153: chesscom.user_properties.v1.UserSettingsProperty.notification_email_hero_playing = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_hero_playing = 49;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9838.

```text
bool notification_web_news_and_announcements = 48;
  }
  oneof _notification_email_hero_playing {
  bool notification_email_hero_playing = 49;
  }
  oneof _gameplay_live_evaluation_bar {
  bool gameplay_live_evaluation_bar = 50;
  }
  oneof _notification_mobile_vote_chess {
  bool notification_mobile_vote_chess = 51;
  }
  oneof _notification_web_new_message {
  bool notification_web_new_message = 52;
  }
  oneof _bo
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12154"></a>
## FND-12154: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_evaluation_bar

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_evaluation_bar {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9887.

```text
;
  }
  oneof _notification_email_hero_playing {
  bool notification_email_hero_playing = 49;
  }
  oneof _gameplay_live_evaluation_bar {
  bool gameplay_live_evaluation_bar = 50;
  }
  oneof _notification_mobile_vote_chess {
  bool notification_mobile_vote_chess = 51;
  }
  oneof _notification_web_new_message {
  bool notification_web_new_message = 52;
  }
  oneof _board_highlight_moves {
  bool board_highlight_move
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12155"></a>
## FND-12155: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_evaluation_bar = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_live_evaluation_bar = 50;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9927.

```text
laying {
  bool notification_email_hero_playing = 49;
  }
  oneof _gameplay_live_evaluation_bar {
  bool gameplay_live_evaluation_bar = 50;
  }
  oneof _notification_mobile_vote_chess {
  bool notification_mobile_vote_chess = 51;
  }
  oneof _notification_web_new_message {
  bool notification_web_new_message = 52;
  }
  oneof _board_highlight_moves {
  bool board_highlight_moves = 53;
  }
  oneof _gameplay_seek_max_r
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12156"></a>
## FND-12156: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_vote_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_vote_chess {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 9973.

```text
g = 49;
  }
  oneof _gameplay_live_evaluation_bar {
  bool gameplay_live_evaluation_bar = 50;
  }
  oneof _notification_mobile_vote_chess {
  bool notification_mobile_vote_chess = 51;
  }
  oneof _notification_web_new_message {
  bool notification_web_new_message = 52;
  }
  oneof _board_highlight_moves {
  bool board_highlight_moves = 53;
  }
  oneof _gameplay_seek_max_rating {
  int32 gameplay_seek_max_rating = 54;
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12157"></a>
## FND-12157: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_vote_chess = 51

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_vote_chess = 51;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10015.

```text
ion_bar {
  bool gameplay_live_evaluation_bar = 50;
  }
  oneof _notification_mobile_vote_chess {
  bool notification_mobile_vote_chess = 51;
  }
  oneof _notification_web_new_message {
  bool notification_web_new_message = 52;
  }
  oneof _board_highlight_moves {
  bool board_highlight_moves = 53;
  }
  oneof _gameplay_seek_max_rating {
  int32 gameplay_seek_max_rating = 54;
  }
  oneof _gameplay_analysis_evaluation
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12158"></a>
## FND-12158: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_new_message

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_new_message {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10063.

```text
50;
  }
  oneof _notification_mobile_vote_chess {
  bool notification_mobile_vote_chess = 51;
  }
  oneof _notification_web_new_message {
  bool notification_web_new_message = 52;
  }
  oneof _board_highlight_moves {
  bool board_highlight_moves = 53;
  }
  oneof _gameplay_seek_max_rating {
  int32 gameplay_seek_max_rating = 54;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_wdl_for_openings {
  bool gameplay_ana
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12159"></a>
## FND-12159: chesscom.user_properties.v1.UserSettingsProperty.notification_web_new_message = 52

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_new_message = 52;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10103.

```text
e_chess {
  bool notification_mobile_vote_chess = 51;
  }
  oneof _notification_web_new_message {
  bool notification_web_new_message = 52;
  }
  oneof _board_highlight_moves {
  bool board_highlight_moves = 53;
  }
  oneof _gameplay_seek_max_rating {
  int32 gameplay_seek_max_rating = 54;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_wdl_for_openings {
  bool gameplay_analysis_evaluation_bar_mode_wdl_for_openin
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12160"></a>
## FND-12160: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_highlight_moves

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_highlight_moves {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10149.

```text
s = 51;
  }
  oneof _notification_web_new_message {
  bool notification_web_new_message = 52;
  }
  oneof _board_highlight_moves {
  bool board_highlight_moves = 53;
  }
  oneof _gameplay_seek_max_rating {
  int32 gameplay_seek_max_rating = 54;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_wdl_for_openings {
  bool gameplay_analysis_evaluation_bar_mode_wdl_for_openings = 55;
  }
  oneof _board_board_style {
  st
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12161"></a>
## FND-12161: chesscom.user_properties.v1.UserSettingsProperty.board_highlight_moves = 53

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool board_highlight_moves = 53;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10182.

```text
_web_new_message {
  bool notification_web_new_message = 52;
  }
  oneof _board_highlight_moves {
  bool board_highlight_moves = 53;
  }
  oneof _gameplay_seek_max_rating {
  int32 gameplay_seek_max_rating = 54;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_wdl_for_openings {
  bool gameplay_analysis_evaluation_bar_mode_wdl_for_openings = 55;
  }
  oneof _board_board_style {
  string board_board_style = 56;
  }

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12162"></a>
## FND-12162: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_seek_max_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_seek_max_rating {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10221.

```text
web_new_message = 52;
  }
  oneof _board_highlight_moves {
  bool board_highlight_moves = 53;
  }
  oneof _gameplay_seek_max_rating {
  int32 gameplay_seek_max_rating = 54;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_wdl_for_openings {
  bool gameplay_analysis_evaluation_bar_mode_wdl_for_openings = 55;
  }
  oneof _board_board_style {
  string board_board_style = 56;
  }
  oneof _gameplay_allow_challenges_from
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12163"></a>
## FND-12163: chesscom.user_properties.v1.UserSettingsProperty.gameplay_seek_max_rating = 54

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 gameplay_seek_max_rating = 54;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10257.

```text
oard_highlight_moves {
  bool board_highlight_moves = 53;
  }
  oneof _gameplay_seek_max_rating {
  int32 gameplay_seek_max_rating = 54;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_wdl_for_openings {
  bool gameplay_analysis_evaluation_bar_mode_wdl_for_openings = 55;
  }
  oneof _board_board_style {
  string board_board_style = 56;
  }
  oneof _gameplay_allow_challenges_from {
  string gameplay_allow_challenge
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12164"></a>
## FND-12164: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_analysis_evaluation_bar_mode_wdl_for_openings

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_analysis_evaluation_bar_mode_wdl_for_openings {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10300.

```text
ht_moves = 53;
  }
  oneof _gameplay_seek_max_rating {
  int32 gameplay_seek_max_rating = 54;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_wdl_for_openings {
  bool gameplay_analysis_evaluation_bar_mode_wdl_for_openings = 55;
  }
  oneof _board_board_style {
  string board_board_style = 56;
  }
  oneof _gameplay_allow_challenges_from {
  string gameplay_allow_challenges_from = 57;
  }
  oneof _gameplay_play_str
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12165"></a>
## FND-12165: chesscom.user_properties.v1.UserSettingsProperty.gameplay_analysis_evaluation_bar_mode_wdl_for_openings = 55

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_analysis_evaluation_bar_mode_wdl_for_openings = 55;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10366.

```text
eplay_seek_max_rating = 54;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_wdl_for_openings {
  bool gameplay_analysis_evaluation_bar_mode_wdl_for_openings = 55;
  }
  oneof _board_board_style {
  string board_board_style = 56;
  }
  oneof _gameplay_allow_challenges_from {
  string gameplay_allow_challenges_from = 57;
  }
  oneof _gameplay_play_streaks {
  bool gameplay_play_streaks = 58;
  }
  oneof _privacy_all
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12166"></a>
## FND-12166: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_board_style

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_board_style {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10438.

```text
r_mode_wdl_for_openings {
  bool gameplay_analysis_evaluation_bar_mode_wdl_for_openings = 55;
  }
  oneof _board_board_style {
  string board_board_style = 56;
  }
  oneof _gameplay_allow_challenges_from {
  string gameplay_allow_challenges_from = 57;
  }
  oneof _gameplay_play_streaks {
  bool gameplay_play_streaks = 58;
  }
  oneof _privacy_allow_global_chat_requests_from {
  string privacy_allow_global_chat_reques
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12167"></a>
## FND-12167: chesscom.user_properties.v1.UserSettingsProperty.board_board_style = 56

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string board_board_style = 56;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10467.

```text
ool gameplay_analysis_evaluation_bar_mode_wdl_for_openings = 55;
  }
  oneof _board_board_style {
  string board_board_style = 56;
  }
  oneof _gameplay_allow_challenges_from {
  string gameplay_allow_challenges_from = 57;
  }
  oneof _gameplay_play_streaks {
  bool gameplay_play_streaks = 58;
  }
  oneof _privacy_allow_global_chat_requests_from {
  string privacy_allow_global_chat_requests_from = 59;
  }
  oneof _pu
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12168"></a>
## FND-12168: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_allow_challenges_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_allow_challenges_from {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10504.

```text
mode_wdl_for_openings = 55;
  }
  oneof _board_board_style {
  string board_board_style = 56;
  }
  oneof _gameplay_allow_challenges_from {
  string gameplay_allow_challenges_from = 57;
  }
  oneof _gameplay_play_streaks {
  bool gameplay_play_streaks = 58;
  }
  oneof _privacy_allow_global_chat_requests_from {
  string privacy_allow_global_chat_requests_from = 59;
  }
  oneof _puzzles_show_details {
  string puzzles
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12169"></a>
## FND-12169: chesscom.user_properties.v1.UserSettingsProperty.gameplay_allow_challenges_from = 57

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string gameplay_allow_challenges_from = 57;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10546.

```text
oard_board_style {
  string board_board_style = 56;
  }
  oneof _gameplay_allow_challenges_from {
  string gameplay_allow_challenges_from = 57;
  }
  oneof _gameplay_play_streaks {
  bool gameplay_play_streaks = 58;
  }
  oneof _privacy_allow_global_chat_requests_from {
  string privacy_allow_global_chat_requests_from = 59;
  }
  oneof _puzzles_show_details {
  string puzzles_show_details = 60;
  }
  oneof _notificat
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12170"></a>
## FND-12170: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_play_streaks

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_play_streaks {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10596.

```text
;
  }
  oneof _gameplay_allow_challenges_from {
  string gameplay_allow_challenges_from = 57;
  }
  oneof _gameplay_play_streaks {
  bool gameplay_play_streaks = 58;
  }
  oneof _privacy_allow_global_chat_requests_from {
  string privacy_allow_global_chat_requests_from = 59;
  }
  oneof _puzzles_show_details {
  string puzzles_show_details = 60;
  }
  oneof _notification_web_new_social_trophy {
  bool notification_we
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12171"></a>
## FND-12171: chesscom.user_properties.v1.UserSettingsProperty.gameplay_play_streaks = 58

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_play_streaks = 58;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10629.

```text
llenges_from {
  string gameplay_allow_challenges_from = 57;
  }
  oneof _gameplay_play_streaks {
  bool gameplay_play_streaks = 58;
  }
  oneof _privacy_allow_global_chat_requests_from {
  string privacy_allow_global_chat_requests_from = 59;
  }
  oneof _puzzles_show_details {
  string puzzles_show_details = 60;
  }
  oneof _notification_web_new_social_trophy {
  bool notification_web_new_social_trophy = 61;
  }
  o
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12172"></a>
## FND-12172: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._privacy_allow_global_chat_requests_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _privacy_allow_global_chat_requests_from {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10668.

```text
challenges_from = 57;
  }
  oneof _gameplay_play_streaks {
  bool gameplay_play_streaks = 58;
  }
  oneof _privacy_allow_global_chat_requests_from {
  string privacy_allow_global_chat_requests_from = 59;
  }
  oneof _puzzles_show_details {
  string puzzles_show_details = 60;
  }
  oneof _notification_web_new_social_trophy {
  bool notification_web_new_social_trophy = 61;
  }
  oneof _privacy_blog_privacy {
  string p
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12173"></a>
## FND-12173: chesscom.user_properties.v1.UserSettingsProperty.privacy_allow_global_chat_requests_from = 59

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string privacy_allow_global_chat_requests_from = 59;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10719.

```text
reaks {
  bool gameplay_play_streaks = 58;
  }
  oneof _privacy_allow_global_chat_requests_from {
  string privacy_allow_global_chat_requests_from = 59;
  }
  oneof _puzzles_show_details {
  string puzzles_show_details = 60;
  }
  oneof _notification_web_new_social_trophy {
  bool notification_web_new_social_trophy = 61;
  }
  oneof _privacy_blog_privacy {
  string privacy_blog_privacy = 62;
  }
  oneof _gameplay_fri
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12174"></a>
## FND-12174: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._puzzles_show_details

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzles_show_details {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10778.

```text
vacy_allow_global_chat_requests_from {
  string privacy_allow_global_chat_requests_from = 59;
  }
  oneof _puzzles_show_details {
  string puzzles_show_details = 60;
  }
  oneof _notification_web_new_social_trophy {
  bool notification_web_new_social_trophy = 61;
  }
  oneof _privacy_blog_privacy {
  string privacy_blog_privacy = 62;
  }
  oneof _gameplay_friends_can_challenge_me_no_matter_what {
  bool gameplay_frie
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
