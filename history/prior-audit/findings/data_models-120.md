# data_models — findings 11901–12000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-12175"></a>
## FND-12175: chesscom.user_properties.v1.UserSettingsProperty.puzzles_show_details = 60

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string puzzles_show_details = 60;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10810.

```text
from {
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
  bool gameplay_friends_can_challenge_me_no_matter_w
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12176"></a>
## FND-12176: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_new_social_trophy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_new_social_trophy {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10850.

```text
t_requests_from = 59;
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
  bool gameplay_friends_can_challenge_me_no_matter_what = 63;
  }
  oneof _gameplay_live_see
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12177"></a>
## FND-12177: chesscom.user_properties.v1.UserSettingsProperty.notification_web_new_social_trophy = 61

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_new_social_trophy = 61;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10896.

```text
w_details {
  string puzzles_show_details = 60;
  }
  oneof _notification_web_new_social_trophy {
  bool notification_web_new_social_trophy = 61;
  }
  oneof _privacy_blog_privacy {
  string privacy_blog_privacy = 62;
  }
  oneof _gameplay_friends_can_challenge_me_no_matter_what {
  bool gameplay_friends_can_challenge_me_no_matter_what = 63;
  }
  oneof _gameplay_live_seek_filter_premium_only {
  bool gameplay_live_s
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12178"></a>
## FND-12178: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._privacy_blog_privacy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _privacy_blog_privacy {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10948.

```text
  oneof _notification_web_new_social_trophy {
  bool notification_web_new_social_trophy = 61;
  }
  oneof _privacy_blog_privacy {
  string privacy_blog_privacy = 62;
  }
  oneof _gameplay_friends_can_challenge_me_no_matter_what {
  bool gameplay_friends_can_challenge_me_no_matter_what = 63;
  }
  oneof _gameplay_live_seek_filter_premium_only {
  bool gameplay_live_seek_filter_premium_only = 64;
  }
  oneof _notificat
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12179"></a>
## FND-12179: chesscom.user_properties.v1.UserSettingsProperty.privacy_blog_privacy = 62

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string privacy_blog_privacy = 62;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 10980.

```text
cial_trophy {
  bool notification_web_new_social_trophy = 61;
  }
  oneof _privacy_blog_privacy {
  string privacy_blog_privacy = 62;
  }
  oneof _gameplay_friends_can_challenge_me_no_matter_what {
  bool gameplay_friends_can_challenge_me_no_matter_what = 63;
  }
  oneof _gameplay_live_seek_filter_premium_only {
  bool gameplay_live_seek_filter_premium_only = 64;
  }
  oneof _notification_email_game_event {
  bool no
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12180"></a>
## FND-12180: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_friends_can_challenge_me_no_matter_what

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_friends_can_challenge_me_no_matter_what {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11020.

```text
w_social_trophy = 61;
  }
  oneof _privacy_blog_privacy {
  string privacy_blog_privacy = 62;
  }
  oneof _gameplay_friends_can_challenge_me_no_matter_what {
  bool gameplay_friends_can_challenge_me_no_matter_what = 63;
  }
  oneof _gameplay_live_seek_filter_premium_only {
  bool gameplay_live_seek_filter_premium_only = 64;
  }
  oneof _notification_email_game_event {
  bool notification_email_game_event = 65;
  }
  
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12181"></a>
## FND-12181: chesscom.user_properties.v1.UserSettingsProperty.gameplay_friends_can_challenge_me_no_matter_what = 63

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_friends_can_challenge_me_no_matter_what = 63;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11080.

```text
string privacy_blog_privacy = 62;
  }
  oneof _gameplay_friends_can_challenge_me_no_matter_what {
  bool gameplay_friends_can_challenge_me_no_matter_what = 63;
  }
  oneof _gameplay_live_seek_filter_premium_only {
  bool gameplay_live_seek_filter_premium_only = 64;
  }
  oneof _notification_email_game_event {
  bool notification_email_game_event = 65;
  }
  oneof _gameplay_seek_game_type {
  string gameplay_seek_game
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12182"></a>
## FND-12182: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_seek_filter_premium_only

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_seek_filter_premium_only {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11146.

```text
n_challenge_me_no_matter_what {
  bool gameplay_friends_can_challenge_me_no_matter_what = 63;
  }
  oneof _gameplay_live_seek_filter_premium_only {
  bool gameplay_live_seek_filter_premium_only = 64;
  }
  oneof _notification_email_game_event {
  bool notification_email_game_event = 65;
  }
  oneof _gameplay_seek_game_type {
  string gameplay_seek_game_type = 66;
  }
  oneof _ui_enable_special_theme_forcing {
  bool 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12183"></a>
## FND-12183: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_seek_filter_premium_only = 64

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_live_seek_filter_premium_only = 64;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11196.

```text
iends_can_challenge_me_no_matter_what = 63;
  }
  oneof _gameplay_live_seek_filter_premium_only {
  bool gameplay_live_seek_filter_premium_only = 64;
  }
  oneof _notification_email_game_event {
  bool notification_email_game_event = 65;
  }
  oneof _gameplay_seek_game_type {
  string gameplay_seek_game_type = 66;
  }
  oneof _ui_enable_special_theme_forcing {
  bool ui_enable_special_theme_forcing = 67;
  }
  oneof 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12184"></a>
## FND-12184: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_game_event

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_game_event {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11252.

```text
_gameplay_live_seek_filter_premium_only {
  bool gameplay_live_seek_filter_premium_only = 64;
  }
  oneof _notification_email_game_event {
  bool notification_email_game_event = 65;
  }
  oneof _gameplay_seek_game_type {
  string gameplay_seek_game_type = 66;
  }
  oneof _ui_enable_special_theme_forcing {
  bool ui_enable_special_theme_forcing = 67;
  }
  oneof _gameplay_live_seek_base_time_chess {
  int32 gameplay_l
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12185"></a>
## FND-12185: chesscom.user_properties.v1.UserSettingsProperty.notification_email_game_event = 65

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_game_event = 65;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11293.

```text

  bool gameplay_live_seek_filter_premium_only = 64;
  }
  oneof _notification_email_game_event {
  bool notification_email_game_event = 65;
  }
  oneof _gameplay_seek_game_type {
  string gameplay_seek_game_type = 66;
  }
  oneof _ui_enable_special_theme_forcing {
  bool ui_enable_special_theme_forcing = 67;
  }
  oneof _gameplay_live_seek_base_time_chess {
  int32 gameplay_live_seek_base_time_chess = 68;
  }
  oneo
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12186"></a>
## FND-12186: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_seek_game_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_seek_game_type {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11340.

```text
= 64;
  }
  oneof _notification_email_game_event {
  bool notification_email_game_event = 65;
  }
  oneof _gameplay_seek_game_type {
  string gameplay_seek_game_type = 66;
  }
  oneof _ui_enable_special_theme_forcing {
  bool ui_enable_special_theme_forcing = 67;
  }
  oneof _gameplay_live_seek_base_time_chess {
  int32 gameplay_live_seek_base_time_chess = 68;
  }
  oneof _notification_mobile_new_user_comment {
  boo
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12187"></a>
## FND-12187: chesscom.user_properties.v1.UserSettingsProperty.gameplay_seek_game_type = 66

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string gameplay_seek_game_type = 66;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11375.

```text
il_game_event {
  bool notification_email_game_event = 65;
  }
  oneof _gameplay_seek_game_type {
  string gameplay_seek_game_type = 66;
  }
  oneof _ui_enable_special_theme_forcing {
  bool ui_enable_special_theme_forcing = 67;
  }
  oneof _gameplay_live_seek_base_time_chess {
  int32 gameplay_live_seek_base_time_chess = 68;
  }
  oneof _notification_mobile_new_user_comment {
  bool notification_mobile_new_user_comm
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12188"></a>
## FND-12188: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._ui_enable_special_theme_forcing

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ui_enable_special_theme_forcing {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11418.

```text
ame_event = 65;
  }
  oneof _gameplay_seek_game_type {
  string gameplay_seek_game_type = 66;
  }
  oneof _ui_enable_special_theme_forcing {
  bool ui_enable_special_theme_forcing = 67;
  }
  oneof _gameplay_live_seek_base_time_chess {
  int32 gameplay_live_seek_base_time_chess = 68;
  }
  oneof _notification_mobile_new_user_comment {
  bool notification_mobile_new_user_comment = 69;
  }
  oneof _notification_email_f
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12189"></a>
## FND-12189: chesscom.user_properties.v1.UserSettingsProperty.ui_enable_special_theme_forcing = 67

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool ui_enable_special_theme_forcing = 67;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11461.

```text
game_type {
  string gameplay_seek_game_type = 66;
  }
  oneof _ui_enable_special_theme_forcing {
  bool ui_enable_special_theme_forcing = 67;
  }
  oneof _gameplay_live_seek_base_time_chess {
  int32 gameplay_live_seek_base_time_chess = 68;
  }
  oneof _notification_mobile_new_user_comment {
  bool notification_mobile_new_user_comment = 69;
  }
  oneof _notification_email_friend_activity_updates {
  bool notificatio
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12190"></a>
## FND-12190: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_seek_base_time_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_seek_base_time_chess {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11510.

```text
;
  }
  oneof _ui_enable_special_theme_forcing {
  bool ui_enable_special_theme_forcing = 67;
  }
  oneof _gameplay_live_seek_base_time_chess {
  int32 gameplay_live_seek_base_time_chess = 68;
  }
  oneof _notification_mobile_new_user_comment {
  bool notification_mobile_new_user_comment = 69;
  }
  oneof _notification_email_friend_activity_updates {
  bool notification_email_friend_activity_updates = 70;
  }
  oneof
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12191"></a>
## FND-12191: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_seek_base_time_chess = 68

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 gameplay_live_seek_base_time_chess = 68;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11556.

```text
 {
  bool ui_enable_special_theme_forcing = 67;
  }
  oneof _gameplay_live_seek_base_time_chess {
  int32 gameplay_live_seek_base_time_chess = 68;
  }
  oneof _notification_mobile_new_user_comment {
  bool notification_mobile_new_user_comment = 69;
  }
  oneof _notification_email_friend_activity_updates {
  bool notification_email_friend_activity_updates = 70;
  }
  oneof _gameplay_live_seek_increment_variants {
  in
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12192"></a>
## FND-12192: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_new_user_comment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_new_user_comment {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11609.

```text
 oneof _gameplay_live_seek_base_time_chess {
  int32 gameplay_live_seek_base_time_chess = 68;
  }
  oneof _notification_mobile_new_user_comment {
  bool notification_mobile_new_user_comment = 69;
  }
  oneof _notification_email_friend_activity_updates {
  bool notification_email_friend_activity_updates = 70;
  }
  oneof _gameplay_live_seek_increment_variants {
  int32 gameplay_live_seek_increment_variants = 71;
  }
 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12193"></a>
## FND-12193: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_new_user_comment = 69

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_new_user_comment = 69;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11657.

```text
nt32 gameplay_live_seek_base_time_chess = 68;
  }
  oneof _notification_mobile_new_user_comment {
  bool notification_mobile_new_user_comment = 69;
  }
  oneof _notification_email_friend_activity_updates {
  bool notification_email_friend_activity_updates = 70;
  }
  oneof _gameplay_live_seek_increment_variants {
  int32 gameplay_live_seek_increment_variants = 71;
  }
  oneof _gameplay_auto_analysis {
  bool gameplay
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12194"></a>
## FND-12194: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_friend_activity_updates

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_friend_activity_updates {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11711.

```text
eof _notification_mobile_new_user_comment {
  bool notification_mobile_new_user_comment = 69;
  }
  oneof _notification_email_friend_activity_updates {
  bool notification_email_friend_activity_updates = 70;
  }
  oneof _gameplay_live_seek_increment_variants {
  int32 gameplay_live_seek_increment_variants = 71;
  }
  oneof _gameplay_auto_analysis {
  bool gameplay_auto_analysis = 72;
  }
  oneof _privacy_allow_club_i
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12195"></a>
## FND-12195: chesscom.user_properties.v1.UserSettingsProperty.notification_email_friend_activity_updates = 70

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_friend_activity_updates = 70;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11765.

```text
ification_mobile_new_user_comment = 69;
  }
  oneof _notification_email_friend_activity_updates {
  bool notification_email_friend_activity_updates = 70;
  }
  oneof _gameplay_live_seek_increment_variants {
  int32 gameplay_live_seek_increment_variants = 71;
  }
  oneof _gameplay_auto_analysis {
  bool gameplay_auto_analysis = 72;
  }
  oneof _privacy_allow_club_invitations {
  bool privacy_allow_club_invitations = 7
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12196"></a>
## FND-12196: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_seek_increment_variants

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_seek_increment_variants {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11825.

```text
ation_email_friend_activity_updates {
  bool notification_email_friend_activity_updates = 70;
  }
  oneof _gameplay_live_seek_increment_variants {
  int32 gameplay_live_seek_increment_variants = 71;
  }
  oneof _gameplay_auto_analysis {
  bool gameplay_auto_analysis = 72;
  }
  oneof _privacy_allow_club_invitations {
  bool privacy_allow_club_invitations = 73;
  }
  oneof _gameplay_live_low_time_warning {
  bool game
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12197"></a>
## FND-12197: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_seek_increment_variants = 71

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 gameplay_live_seek_increment_variants = 71;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11874.

```text
fication_email_friend_activity_updates = 70;
  }
  oneof _gameplay_live_seek_increment_variants {
  int32 gameplay_live_seek_increment_variants = 71;
  }
  oneof _gameplay_auto_analysis {
  bool gameplay_auto_analysis = 72;
  }
  oneof _privacy_allow_club_invitations {
  bool privacy_allow_club_invitations = 73;
  }
  oneof _gameplay_live_low_time_warning {
  bool gameplay_live_low_time_warning = 74;
  }
  oneof _not
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12198"></a>
## FND-12198: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_auto_analysis

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_auto_analysis {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11930.

```text
 _gameplay_live_seek_increment_variants {
  int32 gameplay_live_seek_increment_variants = 71;
  }
  oneof _gameplay_auto_analysis {
  bool gameplay_auto_analysis = 72;
  }
  oneof _privacy_allow_club_invitations {
  bool privacy_allow_club_invitations = 73;
  }
  oneof _gameplay_live_low_time_warning {
  bool gameplay_live_low_time_warning = 74;
  }
  oneof _notification_web_lesson_quota {
  bool notification_web_les
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12199"></a>
## FND-12199: chesscom.user_properties.v1.UserSettingsProperty.gameplay_auto_analysis = 72

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_auto_analysis = 72;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 11964.

```text
iants {
  int32 gameplay_live_seek_increment_variants = 71;
  }
  oneof _gameplay_auto_analysis {
  bool gameplay_auto_analysis = 72;
  }
  oneof _privacy_allow_club_invitations {
  bool privacy_allow_club_invitations = 73;
  }
  oneof _gameplay_live_low_time_warning {
  bool gameplay_live_low_time_warning = 74;
  }
  oneof _notification_web_lesson_quota {
  bool notification_web_lesson_quota = 75;
  }
  oneof _gamep
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12200"></a>
## FND-12200: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._privacy_allow_club_invitations

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _privacy_allow_club_invitations {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12004.

```text
ment_variants = 71;
  }
  oneof _gameplay_auto_analysis {
  bool gameplay_auto_analysis = 72;
  }
  oneof _privacy_allow_club_invitations {
  bool privacy_allow_club_invitations = 73;
  }
  oneof _gameplay_live_low_time_warning {
  bool gameplay_live_low_time_warning = 74;
  }
  oneof _notification_web_lesson_quota {
  bool notification_web_lesson_quota = 75;
  }
  oneof _gameplay_daily_min_days_per_move {
  int32 ga
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12201"></a>
## FND-12201: chesscom.user_properties.v1.UserSettingsProperty.privacy_allow_club_invitations = 73

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool privacy_allow_club_invitations = 73;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12046.

```text
auto_analysis {
  bool gameplay_auto_analysis = 72;
  }
  oneof _privacy_allow_club_invitations {
  bool privacy_allow_club_invitations = 73;
  }
  oneof _gameplay_live_low_time_warning {
  bool gameplay_live_low_time_warning = 74;
  }
  oneof _notification_web_lesson_quota {
  bool notification_web_lesson_quota = 75;
  }
  oneof _gameplay_daily_min_days_per_move {
  int32 gameplay_daily_min_days_per_move = 76;
  }
 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12202"></a>
## FND-12202: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_low_time_warning

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_low_time_warning {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12094.

```text
72;
  }
  oneof _privacy_allow_club_invitations {
  bool privacy_allow_club_invitations = 73;
  }
  oneof _gameplay_live_low_time_warning {
  bool gameplay_live_low_time_warning = 74;
  }
  oneof _notification_web_lesson_quota {
  bool notification_web_lesson_quota = 75;
  }
  oneof _gameplay_daily_min_days_per_move {
  int32 gameplay_daily_min_days_per_move = 76;
  }
  oneof _gameplay_focus_mode {
  bool gameplay_fo
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12203"></a>
## FND-12203: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_low_time_warning = 74

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_live_low_time_warning = 74;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12136.

```text
tions {
  bool privacy_allow_club_invitations = 73;
  }
  oneof _gameplay_live_low_time_warning {
  bool gameplay_live_low_time_warning = 74;
  }
  oneof _notification_web_lesson_quota {
  bool notification_web_lesson_quota = 75;
  }
  oneof _gameplay_daily_min_days_per_move {
  int32 gameplay_daily_min_days_per_move = 76;
  }
  oneof _gameplay_focus_mode {
  bool gameplay_focus_mode = 77;
  }
  oneof _gameplay_live_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12204"></a>
## FND-12204: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_lesson_quota

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_lesson_quota {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12184.

```text
73;
  }
  oneof _gameplay_live_low_time_warning {
  bool gameplay_live_low_time_warning = 74;
  }
  oneof _notification_web_lesson_quota {
  bool notification_web_lesson_quota = 75;
  }
  oneof _gameplay_daily_min_days_per_move {
  int32 gameplay_daily_min_days_per_move = 76;
  }
  oneof _gameplay_focus_mode {
  bool gameplay_focus_mode = 77;
  }
  oneof _gameplay_live_seek_is_rated {
  bool gameplay_live_seek_is_rat
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12205"></a>
## FND-12205: chesscom.user_properties.v1.UserSettingsProperty.notification_web_lesson_quota = 75

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_lesson_quota = 75;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12225.

```text
arning {
  bool gameplay_live_low_time_warning = 74;
  }
  oneof _notification_web_lesson_quota {
  bool notification_web_lesson_quota = 75;
  }
  oneof _gameplay_daily_min_days_per_move {
  int32 gameplay_daily_min_days_per_move = 76;
  }
  oneof _gameplay_focus_mode {
  bool gameplay_focus_mode = 77;
  }
  oneof _gameplay_live_seek_is_rated {
  bool gameplay_live_seek_is_rated = 78;
  }
  oneof _gameplay_live_frien
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12206"></a>
## FND-12206: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_daily_min_days_per_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_daily_min_days_per_move {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12272.

```text
= 74;
  }
  oneof _notification_web_lesson_quota {
  bool notification_web_lesson_quota = 75;
  }
  oneof _gameplay_daily_min_days_per_move {
  int32 gameplay_daily_min_days_per_move = 76;
  }
  oneof _gameplay_focus_mode {
  bool gameplay_focus_mode = 77;
  }
  oneof _gameplay_live_seek_is_rated {
  bool gameplay_live_seek_is_rated = 78;
  }
  oneof _gameplay_live_friends_alerts {
  string gameplay_live_friends_aler
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12207"></a>
## FND-12207: chesscom.user_properties.v1.UserSettingsProperty.gameplay_daily_min_days_per_move = 76

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 gameplay_daily_min_days_per_move = 76;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12316.

```text
uota {
  bool notification_web_lesson_quota = 75;
  }
  oneof _gameplay_daily_min_days_per_move {
  int32 gameplay_daily_min_days_per_move = 76;
  }
  oneof _gameplay_focus_mode {
  bool gameplay_focus_mode = 77;
  }
  oneof _gameplay_live_seek_is_rated {
  bool gameplay_live_seek_is_rated = 78;
  }
  oneof _gameplay_live_friends_alerts {
  string gameplay_live_friends_alerts = 79;
  }
  oneof _privacy_safe_mode {
  
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12208"></a>
## FND-12208: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_focus_mode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_focus_mode {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12367.

```text
 }
  oneof _gameplay_daily_min_days_per_move {
  int32 gameplay_daily_min_days_per_move = 76;
  }
  oneof _gameplay_focus_mode {
  bool gameplay_focus_mode = 77;
  }
  oneof _gameplay_live_seek_is_rated {
  bool gameplay_live_seek_is_rated = 78;
  }
  oneof _gameplay_live_friends_alerts {
  string gameplay_live_friends_alerts = 79;
  }
  oneof _privacy_safe_mode {
  bool privacy_safe_mode = 80;
  }
  oneof _board_sho
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12209"></a>
## FND-12209: chesscom.user_properties.v1.UserSettingsProperty.gameplay_focus_mode = 77

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_focus_mode = 77;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12398.

```text
days_per_move {
  int32 gameplay_daily_min_days_per_move = 76;
  }
  oneof _gameplay_focus_mode {
  bool gameplay_focus_mode = 77;
  }
  oneof _gameplay_live_seek_is_rated {
  bool gameplay_live_seek_is_rated = 78;
  }
  oneof _gameplay_live_friends_alerts {
  string gameplay_live_friends_alerts = 79;
  }
  oneof _privacy_safe_mode {
  bool privacy_safe_mode = 80;
  }
  oneof _board_show_animations {
  bool board_sho
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12210"></a>
## FND-12210: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_seek_is_rated

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_seek_is_rated {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12435.

```text
y_min_days_per_move = 76;
  }
  oneof _gameplay_focus_mode {
  bool gameplay_focus_mode = 77;
  }
  oneof _gameplay_live_seek_is_rated {
  bool gameplay_live_seek_is_rated = 78;
  }
  oneof _gameplay_live_friends_alerts {
  string gameplay_live_friends_alerts = 79;
  }
  oneof _privacy_safe_mode {
  bool privacy_safe_mode = 80;
  }
  oneof _board_show_animations {
  bool board_show_animations = 81;
  }
  oneof _ui_mo
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12211"></a>
## FND-12211: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_seek_is_rated = 78

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_live_seek_is_rated = 78;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12474.

```text
gameplay_focus_mode {
  bool gameplay_focus_mode = 77;
  }
  oneof _gameplay_live_seek_is_rated {
  bool gameplay_live_seek_is_rated = 78;
  }
  oneof _gameplay_live_friends_alerts {
  string gameplay_live_friends_alerts = 79;
  }
  oneof _privacy_safe_mode {
  bool privacy_safe_mode = 80;
  }
  oneof _board_show_animations {
  bool board_show_animations = 81;
  }
  oneof _ui_mode {
  string ui_mode = 82;
  }
  oneof
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12212"></a>
## FND-12212: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_friends_alerts

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_friends_alerts {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12519.

```text
ode = 77;
  }
  oneof _gameplay_live_seek_is_rated {
  bool gameplay_live_seek_is_rated = 78;
  }
  oneof _gameplay_live_friends_alerts {
  string gameplay_live_friends_alerts = 79;
  }
  oneof _privacy_safe_mode {
  bool privacy_safe_mode = 80;
  }
  oneof _board_show_animations {
  bool board_show_animations = 81;
  }
  oneof _ui_mode {
  string ui_mode = 82;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_table
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12213"></a>
## FND-12213: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_friends_alerts = 79

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string gameplay_live_friends_alerts = 79;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12559.

```text
k_is_rated {
  bool gameplay_live_seek_is_rated = 78;
  }
  oneof _gameplay_live_friends_alerts {
  string gameplay_live_friends_alerts = 79;
  }
  oneof _privacy_safe_mode {
  bool privacy_safe_mode = 80;
  }
  oneof _board_show_animations {
  bool board_show_animations = 81;
  }
  oneof _ui_mode {
  string ui_mode = 82;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame {
  bool gameplay_analys
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12214"></a>
## FND-12214: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._privacy_safe_mode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _privacy_safe_mode {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12607.

```text
= 78;
  }
  oneof _gameplay_live_friends_alerts {
  string gameplay_live_friends_alerts = 79;
  }
  oneof _privacy_safe_mode {
  bool privacy_safe_mode = 80;
  }
  oneof _board_show_animations {
  bool board_show_animations = 81;
  }
  oneof _ui_mode {
  string ui_mode = 82;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame {
  bool gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame = 83
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12215"></a>
## FND-12215: chesscom.user_properties.v1.UserSettingsProperty.privacy_safe_mode = 80

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool privacy_safe_mode = 80;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12636.

```text
ive_friends_alerts {
  string gameplay_live_friends_alerts = 79;
  }
  oneof _privacy_safe_mode {
  bool privacy_safe_mode = 80;
  }
  oneof _board_show_animations {
  bool board_show_animations = 81;
  }
  oneof _ui_mode {
  string ui_mode = 82;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame {
  bool gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame = 83;
  }
  oneof _notification_m
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12216"></a>
## FND-12216: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_show_animations

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_show_animations {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12671.

```text
lay_live_friends_alerts = 79;
  }
  oneof _privacy_safe_mode {
  bool privacy_safe_mode = 80;
  }
  oneof _board_show_animations {
  bool board_show_animations = 81;
  }
  oneof _ui_mode {
  string ui_mode = 82;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame {
  bool gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame = 83;
  }
  oneof _notification_mobile_hero_playing {
  bool notific
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12217"></a>
## FND-12217: chesscom.user_properties.v1.UserSettingsProperty.board_show_animations = 81

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool board_show_animations = 81;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12704.

```text

  oneof _privacy_safe_mode {
  bool privacy_safe_mode = 80;
  }
  oneof _board_show_animations {
  bool board_show_animations = 81;
  }
  oneof _ui_mode {
  string ui_mode = 82;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame {
  bool gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame = 83;
  }
  oneof _notification_mobile_hero_playing {
  bool notification_mobile_hero_playing = 84;
 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12218"></a>
## FND-12218: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._ui_mode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ui_mode {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12743.

```text
ivacy_safe_mode = 80;
  }
  oneof _board_show_animations {
  bool board_show_animations = 81;
  }
  oneof _ui_mode {
  string ui_mode = 82;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame {
  bool gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame = 83;
  }
  oneof _notification_mobile_hero_playing {
  bool notification_mobile_hero_playing = 84;
  }
  oneof _notification_mobile_puzzle_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12219"></a>
## FND-12219: chesscom.user_properties.v1.UserSettingsProperty.ui_mode = 82

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string ui_mode = 82;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12762.

```text
0;
  }
  oneof _board_show_animations {
  bool board_show_animations = 81;
  }
  oneof _ui_mode {
  string ui_mode = 82;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame {
  bool gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame = 83;
  }
  oneof _notification_mobile_hero_playing {
  bool notification_mobile_hero_playing = 84;
  }
  oneof _notification_mobile_puzzle_reminder {
  bool n
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12220"></a>
## FND-12220: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12789.

```text
animations {
  bool board_show_animations = 81;
  }
  oneof _ui_mode {
  string ui_mode = 82;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame {
  bool gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame = 83;
  }
  oneof _notification_mobile_hero_playing {
  bool notification_mobile_hero_playing = 84;
  }
  oneof _notification_mobile_puzzle_reminder {
  bool notification_mobile_puzzle_r
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12221"></a>
## FND-12221: chesscom.user_properties.v1.UserSettingsProperty.gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame = 83

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame = 83;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12859.

```text

  string ui_mode = 82;
  }
  oneof _gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame {
  bool gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame = 83;
  }
  oneof _notification_mobile_hero_playing {
  bool notification_mobile_hero_playing = 84;
  }
  oneof _notification_mobile_puzzle_reminder {
  bool notification_mobile_puzzle_reminder = 85;
  }
  oneof _notification_web_friend_activity_updates {

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12222"></a>
## FND-12222: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_hero_playing

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_hero_playing {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12935.

```text
ablebase_in_endgame {
  bool gameplay_analysis_evaluation_bar_mode_tablebase_in_endgame = 83;
  }
  oneof _notification_mobile_hero_playing {
  bool notification_mobile_hero_playing = 84;
  }
  oneof _notification_mobile_puzzle_reminder {
  bool notification_mobile_puzzle_reminder = 85;
  }
  oneof _notification_web_friend_activity_updates {
  bool notification_web_friend_activity_updates = 86;
  }
  oneof _gameplay_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12223"></a>
## FND-12223: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_hero_playing = 84

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_hero_playing = 84;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 12979.

```text
is_evaluation_bar_mode_tablebase_in_endgame = 83;
  }
  oneof _notification_mobile_hero_playing {
  bool notification_mobile_hero_playing = 84;
  }
  oneof _notification_mobile_puzzle_reminder {
  bool notification_mobile_puzzle_reminder = 85;
  }
  oneof _notification_web_friend_activity_updates {
  bool notification_web_friend_activity_updates = 86;
  }
  oneof _gameplay_live_engine_evaluation {
  bool gameplay_liv
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12224"></a>
## FND-12224: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_puzzle_reminder

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_puzzle_reminder {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13029.

```text
  }
  oneof _notification_mobile_hero_playing {
  bool notification_mobile_hero_playing = 84;
  }
  oneof _notification_mobile_puzzle_reminder {
  bool notification_mobile_puzzle_reminder = 85;
  }
  oneof _notification_web_friend_activity_updates {
  bool notification_web_friend_activity_updates = 86;
  }
  oneof _gameplay_live_engine_evaluation {
  bool gameplay_live_engine_evaluation = 87;
  }
  oneof _notificatio
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12225"></a>
## FND-12225: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_puzzle_reminder = 85

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_puzzle_reminder = 85;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13076.

```text

  bool notification_mobile_hero_playing = 84;
  }
  oneof _notification_mobile_puzzle_reminder {
  bool notification_mobile_puzzle_reminder = 85;
  }
  oneof _notification_web_friend_activity_updates {
  bool notification_web_friend_activity_updates = 86;
  }
  oneof _gameplay_live_engine_evaluation {
  bool gameplay_live_engine_evaluation = 87;
  }
  oneof _notification_email_new_user_comment {
  bool notification_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12226"></a>
## FND-12226: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_friend_activity_updates

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_friend_activity_updates {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13129.

```text
oneof _notification_mobile_puzzle_reminder {
  bool notification_mobile_puzzle_reminder = 85;
  }
  oneof _notification_web_friend_activity_updates {
  bool notification_web_friend_activity_updates = 86;
  }
  oneof _gameplay_live_engine_evaluation {
  bool gameplay_live_engine_evaluation = 87;
  }
  oneof _notification_email_new_user_comment {
  bool notification_email_new_user_comment = 88;
  }
  oneof _gameplay_al
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12227"></a>
## FND-12227: chesscom.user_properties.v1.UserSettingsProperty.notification_web_friend_activity_updates = 86

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_friend_activity_updates = 86;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13181.

```text
notification_mobile_puzzle_reminder = 85;
  }
  oneof _notification_web_friend_activity_updates {
  bool notification_web_friend_activity_updates = 86;
  }
  oneof _gameplay_live_engine_evaluation {
  bool gameplay_live_engine_evaluation = 87;
  }
  oneof _notification_email_new_user_comment {
  bool notification_email_new_user_comment = 88;
  }
  oneof _gameplay_allow_game_chat_with {
  string gameplay_allow_game_ch
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12228"></a>
## FND-12228: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_engine_evaluation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_engine_evaluation {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13239.

```text
ification_web_friend_activity_updates {
  bool notification_web_friend_activity_updates = 86;
  }
  oneof _gameplay_live_engine_evaluation {
  bool gameplay_live_engine_evaluation = 87;
  }
  oneof _notification_email_new_user_comment {
  bool notification_email_new_user_comment = 88;
  }
  oneof _gameplay_allow_game_chat_with {
  string gameplay_allow_game_chat_with = 89;
  }
  oneof _notification_email_new_friend_r
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12229"></a>
## FND-12229: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_engine_evaluation = 87

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_live_engine_evaluation = 87;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13282.

```text
ool notification_web_friend_activity_updates = 86;
  }
  oneof _gameplay_live_engine_evaluation {
  bool gameplay_live_engine_evaluation = 87;
  }
  oneof _notification_email_new_user_comment {
  bool notification_email_new_user_comment = 88;
  }
  oneof _gameplay_allow_game_chat_with {
  string gameplay_allow_game_chat_with = 89;
  }
  oneof _notification_email_new_friend_request {
  bool notification_email_new_frie
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12230"></a>
## FND-12230: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_new_user_comment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_new_user_comment {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13331.

```text
;
  }
  oneof _gameplay_live_engine_evaluation {
  bool gameplay_live_engine_evaluation = 87;
  }
  oneof _notification_email_new_user_comment {
  bool notification_email_new_user_comment = 88;
  }
  oneof _gameplay_allow_game_chat_with {
  string gameplay_allow_game_chat_with = 89;
  }
  oneof _notification_email_new_friend_request {
  bool notification_email_new_friend_request = 90;
  }
  oneof _notification_email_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12231"></a>
## FND-12231: chesscom.user_properties.v1.UserSettingsProperty.notification_email_new_user_comment = 88

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_new_user_comment = 88;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13378.

```text
{
  bool gameplay_live_engine_evaluation = 87;
  }
  oneof _notification_email_new_user_comment {
  bool notification_email_new_user_comment = 88;
  }
  oneof _gameplay_allow_game_chat_with {
  string gameplay_allow_game_chat_with = 89;
  }
  oneof _notification_email_new_friend_request {
  bool notification_email_new_friend_request = 90;
  }
  oneof _notification_email_new_message {
  bool notification_email_new_mes
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12232"></a>
## FND-12232: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_allow_game_chat_with

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_allow_game_chat_with {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13431.

```text
oneof _notification_email_new_user_comment {
  bool notification_email_new_user_comment = 88;
  }
  oneof _gameplay_allow_game_chat_with {
  string gameplay_allow_game_chat_with = 89;
  }
  oneof _notification_email_new_friend_request {
  bool notification_email_new_friend_request = 90;
  }
  oneof _notification_email_new_message {
  bool notification_email_new_message = 91;
  }
  oneof _gameplay_live_auto_watch_top_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12233"></a>
## FND-12233: chesscom.user_properties.v1.UserSettingsProperty.gameplay_allow_game_chat_with = 89

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string gameplay_allow_game_chat_with = 89;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13472.

```text
t {
  bool notification_email_new_user_comment = 88;
  }
  oneof _gameplay_allow_game_chat_with {
  string gameplay_allow_game_chat_with = 89;
  }
  oneof _notification_email_new_friend_request {
  bool notification_email_new_friend_request = 90;
  }
  oneof _notification_email_new_message {
  bool notification_email_new_message = 91;
  }
  oneof _gameplay_live_auto_watch_top_game {
  bool gameplay_live_auto_watch_to
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12234"></a>
## FND-12234: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_new_friend_request

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_new_friend_request {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13521.

```text
88;
  }
  oneof _gameplay_allow_game_chat_with {
  string gameplay_allow_game_chat_with = 89;
  }
  oneof _notification_email_new_friend_request {
  bool notification_email_new_friend_request = 90;
  }
  oneof _notification_email_new_message {
  bool notification_email_new_message = 91;
  }
  oneof _gameplay_live_auto_watch_top_game {
  bool gameplay_live_auto_watch_top_game = 92;
  }
  oneof _board_pieces_style {
  
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12235"></a>
## FND-12235: chesscom.user_properties.v1.UserSettingsProperty.notification_email_new_friend_request = 90

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_new_friend_request = 90;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13570.

```text
  string gameplay_allow_game_chat_with = 89;
  }
  oneof _notification_email_new_friend_request {
  bool notification_email_new_friend_request = 90;
  }
  oneof _notification_email_new_message {
  bool notification_email_new_message = 91;
  }
  oneof _gameplay_live_auto_watch_top_game {
  bool gameplay_live_auto_watch_top_game = 92;
  }
  oneof _board_pieces_style {
  string board_pieces_style = 93;
  }
  oneof _game
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12236"></a>
## FND-12236: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_new_message

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_new_message {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13625.

```text
f _notification_email_new_friend_request {
  bool notification_email_new_friend_request = 90;
  }
  oneof _notification_email_new_message {
  bool notification_email_new_message = 91;
  }
  oneof _gameplay_live_auto_watch_top_game {
  bool gameplay_live_auto_watch_top_game = 92;
  }
  oneof _board_pieces_style {
  string board_pieces_style = 93;
  }
  oneof _gameplay_live_seek_increment_chess {
  int32 gameplay_live_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12237"></a>
## FND-12237: chesscom.user_properties.v1.UserSettingsProperty.notification_email_new_message = 91

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_new_message = 91;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13667.

```text

  bool notification_email_new_friend_request = 90;
  }
  oneof _notification_email_new_message {
  bool notification_email_new_message = 91;
  }
  oneof _gameplay_live_auto_watch_top_game {
  bool gameplay_live_auto_watch_top_game = 92;
  }
  oneof _board_pieces_style {
  string board_pieces_style = 93;
  }
  oneof _gameplay_live_seek_increment_chess {
  int32 gameplay_live_seek_increment_chess = 94;
  }
  oneof _no
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12238"></a>
## FND-12238: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_auto_watch_top_game

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_auto_watch_top_game {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13715.

```text
90;
  }
  oneof _notification_email_new_message {
  bool notification_email_new_message = 91;
  }
  oneof _gameplay_live_auto_watch_top_game {
  bool gameplay_live_auto_watch_top_game = 92;
  }
  oneof _board_pieces_style {
  string board_pieces_style = 93;
  }
  oneof _gameplay_live_seek_increment_chess {
  int32 gameplay_live_seek_increment_chess = 94;
  }
  oneof _notification_mobile_new_friend_request {
  bool no
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12239"></a>
## FND-12239: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_auto_watch_top_game = 92

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_live_auto_watch_top_game = 92;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13760.

```text
ge {
  bool notification_email_new_message = 91;
  }
  oneof _gameplay_live_auto_watch_top_game {
  bool gameplay_live_auto_watch_top_game = 92;
  }
  oneof _board_pieces_style {
  string board_pieces_style = 93;
  }
  oneof _gameplay_live_seek_increment_chess {
  int32 gameplay_live_seek_increment_chess = 94;
  }
  oneof _notification_mobile_new_friend_request {
  bool notification_mobile_new_friend_request = 95;
  
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12240"></a>
## FND-12240: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._board_pieces_style

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_pieces_style {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13811.

```text
}
  oneof _gameplay_live_auto_watch_top_game {
  bool gameplay_live_auto_watch_top_game = 92;
  }
  oneof _board_pieces_style {
  string board_pieces_style = 93;
  }
  oneof _gameplay_live_seek_increment_chess {
  int32 gameplay_live_seek_increment_chess = 94;
  }
  oneof _notification_mobile_new_friend_request {
  bool notification_mobile_new_friend_request = 95;
  }
  oneof _gameplay_daily_after_moving {
  string g
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12241"></a>
## FND-12241: chesscom.user_properties.v1.UserSettingsProperty.board_pieces_style = 93

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string board_pieces_style = 93;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13841.

```text
watch_top_game {
  bool gameplay_live_auto_watch_top_game = 92;
  }
  oneof _board_pieces_style {
  string board_pieces_style = 93;
  }
  oneof _gameplay_live_seek_increment_chess {
  int32 gameplay_live_seek_increment_chess = 94;
  }
  oneof _notification_mobile_new_friend_request {
  bool notification_mobile_new_friend_request = 95;
  }
  oneof _gameplay_daily_after_moving {
  string gameplay_daily_after_moving = 9
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12242"></a>
## FND-12242: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_seek_increment_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_seek_increment_chess {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13879.

```text
auto_watch_top_game = 92;
  }
  oneof _board_pieces_style {
  string board_pieces_style = 93;
  }
  oneof _gameplay_live_seek_increment_chess {
  int32 gameplay_live_seek_increment_chess = 94;
  }
  oneof _notification_mobile_new_friend_request {
  bool notification_mobile_new_friend_request = 95;
  }
  oneof _gameplay_daily_after_moving {
  string gameplay_daily_after_moving = 96;
  }
  oneof _gameplay_live_allow_ch
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12243"></a>
## FND-12243: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_seek_increment_chess = 94

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 gameplay_live_seek_increment_chess = 94;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13925.

```text
ieces_style {
  string board_pieces_style = 93;
  }
  oneof _gameplay_live_seek_increment_chess {
  int32 gameplay_live_seek_increment_chess = 94;
  }
  oneof _notification_mobile_new_friend_request {
  bool notification_mobile_new_friend_request = 95;
  }
  oneof _gameplay_daily_after_moving {
  string gameplay_daily_after_moving = 96;
  }
  oneof _gameplay_live_allow_chat_requests_from {
  string gameplay_live_allo
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12244"></a>
## FND-12244: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_new_friend_request

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_new_friend_request {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 13978.

```text
 oneof _gameplay_live_seek_increment_chess {
  int32 gameplay_live_seek_increment_chess = 94;
  }
  oneof _notification_mobile_new_friend_request {
  bool notification_mobile_new_friend_request = 95;
  }
  oneof _gameplay_daily_after_moving {
  string gameplay_daily_after_moving = 96;
  }
  oneof _gameplay_live_allow_chat_requests_from {
  string gameplay_live_allow_chat_requests_from = 97;
  }
  oneof _notification_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12245"></a>
## FND-12245: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_new_friend_request = 95

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_new_friend_request = 95;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14028.

```text
32 gameplay_live_seek_increment_chess = 94;
  }
  oneof _notification_mobile_new_friend_request {
  bool notification_mobile_new_friend_request = 95;
  }
  oneof _gameplay_daily_after_moving {
  string gameplay_daily_after_moving = 96;
  }
  oneof _gameplay_live_allow_chat_requests_from {
  string gameplay_live_allow_chat_requests_from = 97;
  }
  oneof _notification_email_my_turn_to_move {
  bool notification_email_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12246"></a>
## FND-12246: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_daily_after_moving

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_daily_after_moving {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14084.

```text
_notification_mobile_new_friend_request {
  bool notification_mobile_new_friend_request = 95;
  }
  oneof _gameplay_daily_after_moving {
  string gameplay_daily_after_moving = 96;
  }
  oneof _gameplay_live_allow_chat_requests_from {
  string gameplay_live_allow_chat_requests_from = 97;
  }
  oneof _notification_email_my_turn_to_move {
  bool notification_email_my_turn_to_move = 98;
  }
  oneof _notification_mobile_n
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12247"></a>
## FND-12247: chesscom.user_properties.v1.UserSettingsProperty.gameplay_daily_after_moving = 96

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string gameplay_daily_after_moving = 96;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14123.

```text
 {
  bool notification_mobile_new_friend_request = 95;
  }
  oneof _gameplay_daily_after_moving {
  string gameplay_daily_after_moving = 96;
  }
  oneof _gameplay_live_allow_chat_requests_from {
  string gameplay_live_allow_chat_requests_from = 97;
  }
  oneof _notification_email_my_turn_to_move {
  bool notification_email_my_turn_to_move = 98;
  }
  oneof _notification_mobile_new_social_trophy {
  bool notification_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12248"></a>
## FND-12248: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_allow_chat_requests_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_allow_chat_requests_from {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14170.

```text
t = 95;
  }
  oneof _gameplay_daily_after_moving {
  string gameplay_daily_after_moving = 96;
  }
  oneof _gameplay_live_allow_chat_requests_from {
  string gameplay_live_allow_chat_requests_from = 97;
  }
  oneof _notification_email_my_turn_to_move {
  bool notification_email_my_turn_to_move = 98;
  }
  oneof _notification_mobile_new_social_trophy {
  bool notification_mobile_new_social_trophy = 99;
  }
  oneof _gam
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12249"></a>
## FND-12249: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_allow_chat_requests_from = 97

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string gameplay_live_allow_chat_requests_from = 97;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14220.

```text

  string gameplay_daily_after_moving = 96;
  }
  oneof _gameplay_live_allow_chat_requests_from {
  string gameplay_live_allow_chat_requests_from = 97;
  }
  oneof _notification_email_my_turn_to_move {
  bool notification_email_my_turn_to_move = 98;
  }
  oneof _notification_mobile_new_social_trophy {
  bool notification_mobile_new_social_trophy = 99;
  }
  oneof _gameplay_daily_max_game_count {
  int32 gameplay_dail
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12250"></a>
## FND-12250: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_my_turn_to_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_my_turn_to_move {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14278.

```text
ameplay_live_allow_chat_requests_from {
  string gameplay_live_allow_chat_requests_from = 97;
  }
  oneof _notification_email_my_turn_to_move {
  bool notification_email_my_turn_to_move = 98;
  }
  oneof _notification_mobile_new_social_trophy {
  bool notification_mobile_new_social_trophy = 99;
  }
  oneof _gameplay_daily_max_game_count {
  int32 gameplay_daily_max_game_count = 100;
  }
  oneof _puzzles_show_timer {

```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12251"></a>
## FND-12251: chesscom.user_properties.v1.UserSettingsProperty.notification_email_my_turn_to_move = 98

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_my_turn_to_move = 98;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14324.

```text
ng gameplay_live_allow_chat_requests_from = 97;
  }
  oneof _notification_email_my_turn_to_move {
  bool notification_email_my_turn_to_move = 98;
  }
  oneof _notification_mobile_new_social_trophy {
  bool notification_mobile_new_social_trophy = 99;
  }
  oneof _gameplay_daily_max_game_count {
  int32 gameplay_daily_max_game_count = 100;
  }
  oneof _puzzles_show_timer {
  bool puzzles_show_timer = 101;
  }
  oneof _
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12252"></a>
## FND-12252: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_mobile_new_social_trophy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_mobile_new_social_trophy {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14376.

```text
  oneof _notification_email_my_turn_to_move {
  bool notification_email_my_turn_to_move = 98;
  }
  oneof _notification_mobile_new_social_trophy {
  bool notification_mobile_new_social_trophy = 99;
  }
  oneof _gameplay_daily_max_game_count {
  int32 gameplay_daily_max_game_count = 100;
  }
  oneof _puzzles_show_timer {
  bool puzzles_show_timer = 101;
  }
  oneof _privacy_notes_privacy {
  string privacy_notes_priva
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12253"></a>
## FND-12253: chesscom.user_properties.v1.UserSettingsProperty.notification_mobile_new_social_trophy = 99

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_mobile_new_social_trophy = 99;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14425.

```text
ool notification_email_my_turn_to_move = 98;
  }
  oneof _notification_mobile_new_social_trophy {
  bool notification_mobile_new_social_trophy = 99;
  }
  oneof _gameplay_daily_max_game_count {
  int32 gameplay_daily_max_game_count = 100;
  }
  oneof _puzzles_show_timer {
  bool puzzles_show_timer = 101;
  }
  oneof _privacy_notes_privacy {
  string privacy_notes_privacy = 102;
  }
  oneof _learn_coach {
  string lea
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12254"></a>
## FND-12254: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_daily_max_game_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_daily_max_game_count {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14480.

```text
f _notification_mobile_new_social_trophy {
  bool notification_mobile_new_social_trophy = 99;
  }
  oneof _gameplay_daily_max_game_count {
  int32 gameplay_daily_max_game_count = 100;
  }
  oneof _puzzles_show_timer {
  bool puzzles_show_timer = 101;
  }
  oneof _privacy_notes_privacy {
  string privacy_notes_privacy = 102;
  }
  oneof _learn_coach {
  string learn_coach = 103;
  }
  oneof _gameplay_live_right_button
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12255"></a>
## FND-12255: chesscom.user_properties.v1.UserSettingsProperty.gameplay_daily_max_game_count = 100

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 gameplay_daily_max_game_count = 100;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14521.

```text
{
  bool notification_mobile_new_social_trophy = 99;
  }
  oneof _gameplay_daily_max_game_count {
  int32 gameplay_daily_max_game_count = 100;
  }
  oneof _puzzles_show_timer {
  bool puzzles_show_timer = 101;
  }
  oneof _privacy_notes_privacy {
  string privacy_notes_privacy = 102;
  }
  oneof _learn_coach {
  string learn_coach = 103;
  }
  oneof _gameplay_live_right_button_arrows {
  bool gameplay_live_right_butt
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12256"></a>
## FND-12256: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._puzzles_show_timer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzles_show_timer {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14570.

```text
99;
  }
  oneof _gameplay_daily_max_game_count {
  int32 gameplay_daily_max_game_count = 100;
  }
  oneof _puzzles_show_timer {
  bool puzzles_show_timer = 101;
  }
  oneof _privacy_notes_privacy {
  string privacy_notes_privacy = 102;
  }
  oneof _learn_coach {
  string learn_coach = 103;
  }
  oneof _gameplay_live_right_button_arrows {
  bool gameplay_live_right_button_arrows = 104;
  }
  oneof _privacy_allow_tourn
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12257"></a>
## FND-12257: chesscom.user_properties.v1.UserSettingsProperty.puzzles_show_timer = 101

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool puzzles_show_timer = 101;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14600.

```text
y_max_game_count {
  int32 gameplay_daily_max_game_count = 100;
  }
  oneof _puzzles_show_timer {
  bool puzzles_show_timer = 101;
  }
  oneof _privacy_notes_privacy {
  string privacy_notes_privacy = 102;
  }
  oneof _learn_coach {
  string learn_coach = 103;
  }
  oneof _gameplay_live_right_button_arrows {
  bool gameplay_live_right_button_arrows = 104;
  }
  oneof _privacy_allow_tournament_invitations {
  bool pri
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12258"></a>
## FND-12258: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._privacy_notes_privacy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _privacy_notes_privacy {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14637.

```text
aily_max_game_count = 100;
  }
  oneof _puzzles_show_timer {
  bool puzzles_show_timer = 101;
  }
  oneof _privacy_notes_privacy {
  string privacy_notes_privacy = 102;
  }
  oneof _learn_coach {
  string learn_coach = 103;
  }
  oneof _gameplay_live_right_button_arrows {
  bool gameplay_live_right_button_arrows = 104;
  }
  oneof _privacy_allow_tournament_invitations {
  bool privacy_allow_tournament_invitations = 1
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12259"></a>
## FND-12259: chesscom.user_properties.v1.UserSettingsProperty.privacy_notes_privacy = 102

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string privacy_notes_privacy = 102;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14670.

```text
oneof _puzzles_show_timer {
  bool puzzles_show_timer = 101;
  }
  oneof _privacy_notes_privacy {
  string privacy_notes_privacy = 102;
  }
  oneof _learn_coach {
  string learn_coach = 103;
  }
  oneof _gameplay_live_right_button_arrows {
  bool gameplay_live_right_button_arrows = 104;
  }
  oneof _privacy_allow_tournament_invitations {
  bool privacy_allow_tournament_invitations = 105;
  }
  oneof _notification_web
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12260"></a>
## FND-12260: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._learn_coach

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _learn_coach {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14712.

```text
_show_timer = 101;
  }
  oneof _privacy_notes_privacy {
  string privacy_notes_privacy = 102;
  }
  oneof _learn_coach {
  string learn_coach = 103;
  }
  oneof _gameplay_live_right_button_arrows {
  bool gameplay_live_right_button_arrows = 104;
  }
  oneof _privacy_allow_tournament_invitations {
  bool privacy_allow_tournament_invitations = 105;
  }
  oneof _notification_web_new_friend_request {
  bool notification_
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12261"></a>
## FND-12261: chesscom.user_properties.v1.UserSettingsProperty.learn_coach = 103

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string learn_coach = 103;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14735.

```text
  oneof _privacy_notes_privacy {
  string privacy_notes_privacy = 102;
  }
  oneof _learn_coach {
  string learn_coach = 103;
  }
  oneof _gameplay_live_right_button_arrows {
  bool gameplay_live_right_button_arrows = 104;
  }
  oneof _privacy_allow_tournament_invitations {
  bool privacy_allow_tournament_invitations = 105;
  }
  oneof _notification_web_new_friend_request {
  bool notification_web_new_friend_request 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12262"></a>
## FND-12262: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_right_button_arrows

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_right_button_arrows {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14767.

```text

  string privacy_notes_privacy = 102;
  }
  oneof _learn_coach {
  string learn_coach = 103;
  }
  oneof _gameplay_live_right_button_arrows {
  bool gameplay_live_right_button_arrows = 104;
  }
  oneof _privacy_allow_tournament_invitations {
  bool privacy_allow_tournament_invitations = 105;
  }
  oneof _notification_web_new_friend_request {
  bool notification_web_new_friend_request = 106;
  }
  oneof _gameplay_liv
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12263"></a>
## FND-12263: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_right_button_arrows = 104

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool gameplay_live_right_button_arrows = 104;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14812.

```text
oneof _learn_coach {
  string learn_coach = 103;
  }
  oneof _gameplay_live_right_button_arrows {
  bool gameplay_live_right_button_arrows = 104;
  }
  oneof _privacy_allow_tournament_invitations {
  bool privacy_allow_tournament_invitations = 105;
  }
  oneof _notification_web_new_friend_request {
  bool notification_web_new_friend_request = 106;
  }
  oneof _gameplay_live_event_announcements {
  string gameplay_liv
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12264"></a>
## FND-12264: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._privacy_allow_tournament_invitations

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _privacy_allow_tournament_invitations {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14864.

```text

  oneof _gameplay_live_right_button_arrows {
  bool gameplay_live_right_button_arrows = 104;
  }
  oneof _privacy_allow_tournament_invitations {
  bool privacy_allow_tournament_invitations = 105;
  }
  oneof _notification_web_new_friend_request {
  bool notification_web_new_friend_request = 106;
  }
  oneof _gameplay_live_event_announcements {
  string gameplay_live_event_announcements = 107;
  }
  oneof _notificati
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12265"></a>
## FND-12265: chesscom.user_properties.v1.UserSettingsProperty.privacy_allow_tournament_invitations = 105

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool privacy_allow_tournament_invitations = 105;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14912.

```text
bool gameplay_live_right_button_arrows = 104;
  }
  oneof _privacy_allow_tournament_invitations {
  bool privacy_allow_tournament_invitations = 105;
  }
  oneof _notification_web_new_friend_request {
  bool notification_web_new_friend_request = 106;
  }
  oneof _gameplay_live_event_announcements {
  string gameplay_live_event_announcements = 107;
  }
  oneof _notification_email_puzzle_reminder {
  bool notification_e
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12266"></a>
## FND-12266: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_web_new_friend_request

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_web_new_friend_request {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 14967.

```text
of _privacy_allow_tournament_invitations {
  bool privacy_allow_tournament_invitations = 105;
  }
  oneof _notification_web_new_friend_request {
  bool notification_web_new_friend_request = 106;
  }
  oneof _gameplay_live_event_announcements {
  string gameplay_live_event_announcements = 107;
  }
  oneof _notification_email_puzzle_reminder {
  bool notification_email_puzzle_reminder = 108;
  }
  oneof _notification_e
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12267"></a>
## FND-12267: chesscom.user_properties.v1.UserSettingsProperty.notification_web_new_friend_request = 106

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_web_new_friend_request = 106;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15014.

```text
ol privacy_allow_tournament_invitations = 105;
  }
  oneof _notification_web_new_friend_request {
  bool notification_web_new_friend_request = 106;
  }
  oneof _gameplay_live_event_announcements {
  string gameplay_live_event_announcements = 107;
  }
  oneof _notification_email_puzzle_reminder {
  bool notification_email_puzzle_reminder = 108;
  }
  oneof _notification_email_vote_chess {
  bool notification_email_vot
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12268"></a>
## FND-12268: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._gameplay_live_event_announcements

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _gameplay_live_event_announcements {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15068.

```text
neof _notification_web_new_friend_request {
  bool notification_web_new_friend_request = 106;
  }
  oneof _gameplay_live_event_announcements {
  string gameplay_live_event_announcements = 107;
  }
  oneof _notification_email_puzzle_reminder {
  bool notification_email_puzzle_reminder = 108;
  }
  oneof _notification_email_vote_chess {
  bool notification_email_vote_chess = 109;
  }
  oneof _notification_auto_track_co
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12269"></a>
## FND-12269: chesscom.user_properties.v1.UserSettingsProperty.gameplay_live_event_announcements = 107

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string gameplay_live_event_announcements = 107;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15113.

```text
 bool notification_web_new_friend_request = 106;
  }
  oneof _gameplay_live_event_announcements {
  string gameplay_live_event_announcements = 107;
  }
  oneof _notification_email_puzzle_reminder {
  bool notification_email_puzzle_reminder = 108;
  }
  oneof _notification_email_vote_chess {
  bool notification_email_vote_chess = 109;
  }
  oneof _notification_auto_track_content {
  bool notification_auto_track_conten
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12270"></a>
## FND-12270: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_puzzle_reminder

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_puzzle_reminder {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15167.

```text
 oneof _gameplay_live_event_announcements {
  string gameplay_live_event_announcements = 107;
  }
  oneof _notification_email_puzzle_reminder {
  bool notification_email_puzzle_reminder = 108;
  }
  oneof _notification_email_vote_chess {
  bool notification_email_vote_chess = 109;
  }
  oneof _notification_auto_track_content {
  bool notification_auto_track_content = 110;
  }
  oneof _gameplay_live_seek_filter_hide_v
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12271"></a>
## FND-12271: chesscom.user_properties.v1.UserSettingsProperty.notification_email_puzzle_reminder = 108

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_puzzle_reminder = 108;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15213.

```text
string gameplay_live_event_announcements = 107;
  }
  oneof _notification_email_puzzle_reminder {
  bool notification_email_puzzle_reminder = 108;
  }
  oneof _notification_email_vote_chess {
  bool notification_email_vote_chess = 109;
  }
  oneof _notification_auto_track_content {
  bool notification_auto_track_content = 110;
  }
  oneof _gameplay_live_seek_filter_hide_variants {
  bool gameplay_live_seek_filter_hid
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12272"></a>
## FND-12272: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_email_vote_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_email_vote_chess {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15266.

```text
 oneof _notification_email_puzzle_reminder {
  bool notification_email_puzzle_reminder = 108;
  }
  oneof _notification_email_vote_chess {
  bool notification_email_vote_chess = 109;
  }
  oneof _notification_auto_track_content {
  bool notification_auto_track_content = 110;
  }
  oneof _gameplay_live_seek_filter_hide_variants {
  bool gameplay_live_seek_filter_hide_variants = 111;
  }
  oneof _privacy_messages_priva
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12273"></a>
## FND-12273: chesscom.user_properties.v1.UserSettingsProperty.notification_email_vote_chess = 109

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool notification_email_vote_chess = 109;

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15307.

```text
r {
  bool notification_email_puzzle_reminder = 108;
  }
  oneof _notification_email_vote_chess {
  bool notification_email_vote_chess = 109;
  }
  oneof _notification_auto_track_content {
  bool notification_auto_track_content = 110;
  }
  oneof _gameplay_live_seek_filter_hide_variants {
  bool gameplay_live_seek_filter_hide_variants = 111;
  }
  oneof _privacy_messages_privacy {
  string privacy_messages_privacy = 
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12274"></a>
## FND-12274: oneof declaration: chesscom.user_properties.v1.UserSettingsProperty._notification_auto_track_content

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _notification_auto_track_content {

### Evidence

- **SRC-0643** `research/proto/chesscom/user_properties/v1/properties_user_settings.proto` — [preserved redacted evidence](../evidence/text/b1314dca288bc04aae5f5f326ae9414c8b19a3a313edabd475475b6d3e6c097c.proto)
  Character offset 15355.

```text
108;
  }
  oneof _notification_email_vote_chess {
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
  oneof _gameplay_live_seek_filter_rate
```

**Source references:** SRC-0643, SRC-1614  
**URL references:** None independently associated  
**Related findings:** FND-11919, FND-11920, FND-11921

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
