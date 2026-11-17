# data_models — findings 10801–10900

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-11075"></a>
## FND-11075: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.SEEK_BASE_TIME = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEEK_BASE_TIME = 12;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 500.

```text
W_CHAT_REQUEST_FROM = 8;
  AUTO_TOP = 9;
  FOCUS_MODE_ENABLED = 10;
  ALLOW_CHALLENGES_FROM = 11;
  SEEK_BASE_TIME = 12;
  SEEK_MIN_RATING = 13;
  SEEK_MAX_RATING = 14;
  CHALLENGE_POPUP_ALERT = 15;
  FRIEND_POPUP_ALERT = 16;
  EVENT_ANNOUNCEMENT = 17;
  CHALLENGE_MIN_RATING = 18;
  CHALLENGE_MAX_RATING = 19;
  SEEK_BASE_TIME_VARIANTS = 20;
  SEEK_INCREMENT_VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11076"></a>
## FND-11076: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.SEEK_MIN_RATING = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEEK_MIN_RATING = 13;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 523.

```text
;
  AUTO_TOP = 9;
  FOCUS_MODE_ENABLED = 10;
  ALLOW_CHALLENGES_FROM = 11;
  SEEK_BASE_TIME = 12;
  SEEK_MIN_RATING = 13;
  SEEK_MAX_RATING = 14;
  CHALLENGE_POPUP_ALERT = 15;
  FRIEND_POPUP_ALERT = 16;
  EVENT_ANNOUNCEMENT = 17;
  CHALLENGE_MIN_RATING = 18;
  CHALLENGE_MAX_RATING = 19;
  SEEK_BASE_TIME_VARIANTS = 20;
  SEEK_INCREMENT_VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GA
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11077"></a>
## FND-11077: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.SEEK_MAX_RATING = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEEK_MAX_RATING = 14;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 547.

```text
S_MODE_ENABLED = 10;
  ALLOW_CHALLENGES_FROM = 11;
  SEEK_BASE_TIME = 12;
  SEEK_MIN_RATING = 13;
  SEEK_MAX_RATING = 14;
  CHALLENGE_POPUP_ALERT = 15;
  FRIEND_POPUP_ALERT = 16;
  EVENT_ANNOUNCEMENT = 17;
  CHALLENGE_MIN_RATING = 18;
  CHALLENGE_MAX_RATING = 19;
  SEEK_BASE_TIME_VARIANTS = 20;
  SEEK_INCREMENT_VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11078"></a>
## FND-11078: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.CHALLENGE_POPUP_ALERT = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHALLENGE_POPUP_ALERT = 15;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 571.

```text
LLOW_CHALLENGES_FROM = 11;
  SEEK_BASE_TIME = 12;
  SEEK_MIN_RATING = 13;
  SEEK_MAX_RATING = 14;
  CHALLENGE_POPUP_ALERT = 15;
  FRIEND_POPUP_ALERT = 16;
  EVENT_ANNOUNCEMENT = 17;
  CHALLENGE_MIN_RATING = 18;
  CHALLENGE_MAX_RATING = 19;
  SEEK_BASE_TIME_VARIANTS = 20;
  SEEK_INCREMENT_VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message SettingsLiveChessProper
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11079"></a>
## FND-11079: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.FRIEND_POPUP_ALERT = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FRIEND_POPUP_ALERT = 16;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 601.

```text
EEK_BASE_TIME = 12;
  SEEK_MIN_RATING = 13;
  SEEK_MAX_RATING = 14;
  CHALLENGE_POPUP_ALERT = 15;
  FRIEND_POPUP_ALERT = 16;
  EVENT_ANNOUNCEMENT = 17;
  CHALLENGE_MIN_RATING = 18;
  CHALLENGE_MAX_RATING = 19;
  SEEK_BASE_TIME_VARIANTS = 20;
  SEEK_INCREMENT_VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message SettingsLiveChessProperty {
  oneof _auto_queen {
  b
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11080"></a>
## FND-11080: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.EVENT_ANNOUNCEMENT = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_ANNOUNCEMENT = 17;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 628.

```text
MIN_RATING = 13;
  SEEK_MAX_RATING = 14;
  CHALLENGE_POPUP_ALERT = 15;
  FRIEND_POPUP_ALERT = 16;
  EVENT_ANNOUNCEMENT = 17;
  CHALLENGE_MIN_RATING = 18;
  CHALLENGE_MAX_RATING = 19;
  SEEK_BASE_TIME_VARIANTS = 20;
  SEEK_INCREMENT_VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message SettingsLiveChessProperty {
  oneof _auto_queen {
  bool auto_queen = 1;
  }
  o
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11081"></a>
## FND-11081: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.CHALLENGE_MIN_RATING = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHALLENGE_MIN_RATING = 18;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 655.

```text
_RATING = 14;
  CHALLENGE_POPUP_ALERT = 15;
  FRIEND_POPUP_ALERT = 16;
  EVENT_ANNOUNCEMENT = 17;
  CHALLENGE_MIN_RATING = 18;
  CHALLENGE_MAX_RATING = 19;
  SEEK_BASE_TIME_VARIANTS = 20;
  SEEK_INCREMENT_VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message SettingsLiveChessProperty {
  oneof _auto_queen {
  bool auto_queen = 1;
  }
  oneof _play_multiple_games {
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11082"></a>
## FND-11082: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.CHALLENGE_MAX_RATING = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHALLENGE_MAX_RATING = 19;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 684.

```text
UP_ALERT = 15;
  FRIEND_POPUP_ALERT = 16;
  EVENT_ANNOUNCEMENT = 17;
  CHALLENGE_MIN_RATING = 18;
  CHALLENGE_MAX_RATING = 19;
  SEEK_BASE_TIME_VARIANTS = 20;
  SEEK_INCREMENT_VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message SettingsLiveChessProperty {
  oneof _auto_queen {
  bool auto_queen = 1;
  }
  oneof _play_multiple_games {
  bool play_multiple_games =
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11083"></a>
## FND-11083: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.SEEK_BASE_TIME_VARIANTS = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEEK_BASE_TIME_VARIANTS = 20;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 713.

```text
_ALERT = 16;
  EVENT_ANNOUNCEMENT = 17;
  CHALLENGE_MIN_RATING = 18;
  CHALLENGE_MAX_RATING = 19;
  SEEK_BASE_TIME_VARIANTS = 20;
  SEEK_INCREMENT_VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message SettingsLiveChessProperty {
  oneof _auto_queen {
  bool auto_queen = 1;
  }
  oneof _play_multiple_games {
  bool play_multiple_games = 2;
  }
  oneof _seek_increme
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11084"></a>
## FND-11084: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.SEEK_INCREMENT_VARIANTS = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEEK_INCREMENT_VARIANTS = 21;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 745.

```text
T = 17;
  CHALLENGE_MIN_RATING = 18;
  CHALLENGE_MAX_RATING = 19;
  SEEK_BASE_TIME_VARIANTS = 20;
  SEEK_INCREMENT_VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message SettingsLiveChessProperty {
  oneof _auto_queen {
  bool auto_queen = 1;
  }
  oneof _play_multiple_games {
  bool play_multiple_games = 2;
  }
  oneof _seek_increment {
  int32 seek_increment = 3;
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11085"></a>
## FND-11085: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.SEEK_BASE_TIME_CHESS = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEEK_BASE_TIME_CHESS = 22;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 777.

```text
 18;
  CHALLENGE_MAX_RATING = 19;
  SEEK_BASE_TIME_VARIANTS = 20;
  SEEK_INCREMENT_VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message SettingsLiveChessProperty {
  oneof _auto_queen {
  bool auto_queen = 1;
  }
  oneof _play_multiple_games {
  bool play_multiple_games = 2;
  }
  oneof _seek_increment {
  int32 seek_increment = 3;
  }
  oneof _seek_rated {
  boo
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11086"></a>
## FND-11086: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.SEEK_INCREMENT_CHESS = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEEK_INCREMENT_CHESS = 23;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 806.

```text
 19;
  SEEK_BASE_TIME_VARIANTS = 20;
  SEEK_INCREMENT_VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message SettingsLiveChessProperty {
  oneof _auto_queen {
  bool auto_queen = 1;
  }
  oneof _play_multiple_games {
  bool play_multiple_games = 2;
  }
  oneof _seek_increment {
  int32 seek_increment = 3;
  }
  oneof _seek_rated {
  bool seek_rated = 4;
  }
  oneof
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11087"></a>
## FND-11087: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.ALLOW_GAME_CHAT = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ALLOW_GAME_CHAT = 24;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 835.

```text
S = 20;
  SEEK_INCREMENT_VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message SettingsLiveChessProperty {
  oneof _auto_queen {
  bool auto_queen = 1;
  }
  oneof _play_multiple_games {
  bool play_multiple_games = 2;
  }
  oneof _seek_increment {
  int32 seek_increment = 3;
  }
  oneof _seek_rated {
  bool seek_rated = 4;
  }
  oneof _seek_filter_premium_only {

```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11088"></a>
## FND-11088: message declaration: chesscom.user_properties.v1.SettingsLiveChessProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SettingsLiveChessProperty {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 860.

```text
VARIANTS = 21;
  SEEK_BASE_TIME_CHESS = 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message SettingsLiveChessProperty {
  oneof _auto_queen {
  bool auto_queen = 1;
  }
  oneof _play_multiple_games {
  bool play_multiple_games = 2;
  }
  oneof _seek_increment {
  int32 seek_increment = 3;
  }
  oneof _seek_rated {
  bool seek_rated = 4;
  }
  oneof _seek_filter_premium_only {
  bool seek_filter_premiu
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11089"></a>
## FND-11089: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._auto_queen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _auto_queen {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 898.

```text
= 22;
  SEEK_INCREMENT_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message SettingsLiveChessProperty {
  oneof _auto_queen {
  bool auto_queen = 1;
  }
  oneof _play_multiple_games {
  bool play_multiple_games = 2;
  }
  oneof _seek_increment {
  int32 seek_increment = 3;
  }
  oneof _seek_rated {
  bool seek_rated = 4;
  }
  oneof _seek_filter_premium_only {
  bool seek_filter_premium_only = 5;
  }
  oneof _premove_enabl
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11090"></a>
## FND-11090: chesscom.user_properties.v1.SettingsLiveChessProperty.auto_queen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool auto_queen = 1;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 920.

```text
_CHESS = 23;
  ALLOW_GAME_CHAT = 24;
}

message SettingsLiveChessProperty {
  oneof _auto_queen {
  bool auto_queen = 1;
  }
  oneof _play_multiple_games {
  bool play_multiple_games = 2;
  }
  oneof _seek_increment {
  int32 seek_increment = 3;
  }
  oneof _seek_rated {
  bool seek_rated = 4;
  }
  oneof _seek_filter_premium_only {
  bool seek_filter_premium_only = 5;
  }
  oneof _premove_enabled {
  bool premove_en
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11091"></a>
## FND-11091: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._play_multiple_games

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _play_multiple_games {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 947.

```text
HAT = 24;
}

message SettingsLiveChessProperty {
  oneof _auto_queen {
  bool auto_queen = 1;
  }
  oneof _play_multiple_games {
  bool play_multiple_games = 2;
  }
  oneof _seek_increment {
  int32 seek_increment = 3;
  }
  oneof _seek_rated {
  bool seek_rated = 4;
  }
  oneof _seek_filter_premium_only {
  bool seek_filter_premium_only = 5;
  }
  oneof _premove_enabled {
  bool premove_enabled = 6;
  }
  oneof _see
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11092"></a>
## FND-11092: chesscom.user_properties.v1.SettingsLiveChessProperty.play_multiple_games = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool play_multiple_games = 2;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 978.

```text
veChessProperty {
  oneof _auto_queen {
  bool auto_queen = 1;
  }
  oneof _play_multiple_games {
  bool play_multiple_games = 2;
  }
  oneof _seek_increment {
  int32 seek_increment = 3;
  }
  oneof _seek_rated {
  bool seek_rated = 4;
  }
  oneof _seek_filter_premium_only {
  bool seek_filter_premium_only = 5;
  }
  oneof _premove_enabled {
  bool premove_enabled = 6;
  }
  oneof _seek_filter_rated_only {
  bool se
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11093"></a>
## FND-11093: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._seek_increment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _seek_increment {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1014.

```text
n {
  bool auto_queen = 1;
  }
  oneof _play_multiple_games {
  bool play_multiple_games = 2;
  }
  oneof _seek_increment {
  int32 seek_increment = 3;
  }
  oneof _seek_rated {
  bool seek_rated = 4;
  }
  oneof _seek_filter_premium_only {
  bool seek_filter_premium_only = 5;
  }
  oneof _premove_enabled {
  bool premove_enabled = 6;
  }
  oneof _seek_filter_rated_only {
  bool seek_filter_rated_only = 7;
  }
  oneo
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11094"></a>
## FND-11094: chesscom.user_properties.v1.SettingsLiveChessProperty.seek_increment = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 seek_increment = 3;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1040.

```text

  }
  oneof _play_multiple_games {
  bool play_multiple_games = 2;
  }
  oneof _seek_increment {
  int32 seek_increment = 3;
  }
  oneof _seek_rated {
  bool seek_rated = 4;
  }
  oneof _seek_filter_premium_only {
  bool seek_filter_premium_only = 5;
  }
  oneof _premove_enabled {
  bool premove_enabled = 6;
  }
  oneof _seek_filter_rated_only {
  bool seek_filter_rated_only = 7;
  }
  oneof _allow_chat_request_from
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11095"></a>
## FND-11095: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._seek_rated

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _seek_rated {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1072.

```text
s {
  bool play_multiple_games = 2;
  }
  oneof _seek_increment {
  int32 seek_increment = 3;
  }
  oneof _seek_rated {
  bool seek_rated = 4;
  }
  oneof _seek_filter_premium_only {
  bool seek_filter_premium_only = 5;
  }
  oneof _premove_enabled {
  bool premove_enabled = 6;
  }
  oneof _seek_filter_rated_only {
  bool seek_filter_rated_only = 7;
  }
  oneof _allow_chat_request_from {
  int32 allow_chat_request_fr
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11096"></a>
## FND-11096: chesscom.user_properties.v1.SettingsLiveChessProperty.seek_rated = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool seek_rated = 4;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1094.

```text
le_games = 2;
  }
  oneof _seek_increment {
  int32 seek_increment = 3;
  }
  oneof _seek_rated {
  bool seek_rated = 4;
  }
  oneof _seek_filter_premium_only {
  bool seek_filter_premium_only = 5;
  }
  oneof _premove_enabled {
  bool premove_enabled = 6;
  }
  oneof _seek_filter_rated_only {
  bool seek_filter_rated_only = 7;
  }
  oneof _allow_chat_request_from {
  int32 allow_chat_request_from = 8;
  }
  oneof _a
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11097"></a>
## FND-11097: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._seek_filter_premium_only

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _seek_filter_premium_only {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1121.

```text
seek_increment {
  int32 seek_increment = 3;
  }
  oneof _seek_rated {
  bool seek_rated = 4;
  }
  oneof _seek_filter_premium_only {
  bool seek_filter_premium_only = 5;
  }
  oneof _premove_enabled {
  bool premove_enabled = 6;
  }
  oneof _seek_filter_rated_only {
  bool seek_filter_rated_only = 7;
  }
  oneof _allow_chat_request_from {
  int32 allow_chat_request_from = 8;
  }
  oneof _auto_top {
  bool auto_top =
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11098"></a>
## FND-11098: chesscom.user_properties.v1.SettingsLiveChessProperty.seek_filter_premium_only = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool seek_filter_premium_only = 5;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1157.

```text
ent = 3;
  }
  oneof _seek_rated {
  bool seek_rated = 4;
  }
  oneof _seek_filter_premium_only {
  bool seek_filter_premium_only = 5;
  }
  oneof _premove_enabled {
  bool premove_enabled = 6;
  }
  oneof _seek_filter_rated_only {
  bool seek_filter_rated_only = 7;
  }
  oneof _allow_chat_request_from {
  int32 allow_chat_request_from = 8;
  }
  oneof _auto_top {
  bool auto_top = 9;
  }
  oneof _focus_mode_enabled 
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11099"></a>
## FND-11099: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._premove_enabled

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _premove_enabled {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1198.

```text
 seek_rated = 4;
  }
  oneof _seek_filter_premium_only {
  bool seek_filter_premium_only = 5;
  }
  oneof _premove_enabled {
  bool premove_enabled = 6;
  }
  oneof _seek_filter_rated_only {
  bool seek_filter_rated_only = 7;
  }
  oneof _allow_chat_request_from {
  int32 allow_chat_request_from = 8;
  }
  oneof _auto_top {
  bool auto_top = 9;
  }
  oneof _focus_mode_enabled {
  bool focus_mode_enabled = 10;
  }
  o
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11100"></a>
## FND-11100: chesscom.user_properties.v1.SettingsLiveChessProperty.premove_enabled = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool premove_enabled = 6;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1225.

```text
f _seek_filter_premium_only {
  bool seek_filter_premium_only = 5;
  }
  oneof _premove_enabled {
  bool premove_enabled = 6;
  }
  oneof _seek_filter_rated_only {
  bool seek_filter_rated_only = 7;
  }
  oneof _allow_chat_request_from {
  int32 allow_chat_request_from = 8;
  }
  oneof _auto_top {
  bool auto_top = 9;
  }
  oneof _focus_mode_enabled {
  bool focus_mode_enabled = 10;
  }
  oneof _allow_challenges_from
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11101"></a>
## FND-11101: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._seek_filter_rated_only

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _seek_filter_rated_only {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1257.

```text
bool seek_filter_premium_only = 5;
  }
  oneof _premove_enabled {
  bool premove_enabled = 6;
  }
  oneof _seek_filter_rated_only {
  bool seek_filter_rated_only = 7;
  }
  oneof _allow_chat_request_from {
  int32 allow_chat_request_from = 8;
  }
  oneof _auto_top {
  bool auto_top = 9;
  }
  oneof _focus_mode_enabled {
  bool focus_mode_enabled = 10;
  }
  oneof _allow_challenges_from {
  int32 allow_challenges_from
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11102"></a>
## FND-11102: chesscom.user_properties.v1.SettingsLiveChessProperty.seek_filter_rated_only = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool seek_filter_rated_only = 7;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1291.

```text

  }
  oneof _premove_enabled {
  bool premove_enabled = 6;
  }
  oneof _seek_filter_rated_only {
  bool seek_filter_rated_only = 7;
  }
  oneof _allow_chat_request_from {
  int32 allow_chat_request_from = 8;
  }
  oneof _auto_top {
  bool auto_top = 9;
  }
  oneof _focus_mode_enabled {
  bool focus_mode_enabled = 10;
  }
  oneof _allow_challenges_from {
  int32 allow_challenges_from = 11;
  }
  oneof _seek_base_time
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11103"></a>
## FND-11103: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._allow_chat_request_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _allow_chat_request_from {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1330.

```text
premove_enabled = 6;
  }
  oneof _seek_filter_rated_only {
  bool seek_filter_rated_only = 7;
  }
  oneof _allow_chat_request_from {
  int32 allow_chat_request_from = 8;
  }
  oneof _auto_top {
  bool auto_top = 9;
  }
  oneof _focus_mode_enabled {
  bool focus_mode_enabled = 10;
  }
  oneof _allow_challenges_from {
  int32 allow_challenges_from = 11;
  }
  oneof _seek_base_time {
  int32 seek_base_time = 12;
  }
  o
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11104"></a>
## FND-11104: chesscom.user_properties.v1.SettingsLiveChessProperty.allow_chat_request_from = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 allow_chat_request_from = 8;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1365.

```text
eek_filter_rated_only {
  bool seek_filter_rated_only = 7;
  }
  oneof _allow_chat_request_from {
  int32 allow_chat_request_from = 8;
  }
  oneof _auto_top {
  bool auto_top = 9;
  }
  oneof _focus_mode_enabled {
  bool focus_mode_enabled = 10;
  }
  oneof _allow_challenges_from {
  int32 allow_challenges_from = 11;
  }
  oneof _seek_base_time {
  int32 seek_base_time = 12;
  }
  oneof _seek_min_rating {
  int32 see
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11105"></a>
## FND-11105: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._auto_top

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _auto_top {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1406.

```text
r_rated_only = 7;
  }
  oneof _allow_chat_request_from {
  int32 allow_chat_request_from = 8;
  }
  oneof _auto_top {
  bool auto_top = 9;
  }
  oneof _focus_mode_enabled {
  bool focus_mode_enabled = 10;
  }
  oneof _allow_challenges_from {
  int32 allow_challenges_from = 11;
  }
  oneof _seek_base_time {
  int32 seek_base_time = 12;
  }
  oneof _seek_min_rating {
  int32 seek_min_rating = 13;
  }
  oneof _seek_max_
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11106"></a>
## FND-11106: chesscom.user_properties.v1.SettingsLiveChessProperty.auto_top = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool auto_top = 9;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1426.

```text
}
  oneof _allow_chat_request_from {
  int32 allow_chat_request_from = 8;
  }
  oneof _auto_top {
  bool auto_top = 9;
  }
  oneof _focus_mode_enabled {
  bool focus_mode_enabled = 10;
  }
  oneof _allow_challenges_from {
  int32 allow_challenges_from = 11;
  }
  oneof _seek_base_time {
  int32 seek_base_time = 12;
  }
  oneof _seek_min_rating {
  int32 seek_min_rating = 13;
  }
  oneof _seek_max_rating {
  int32 see
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11107"></a>
## FND-11107: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._focus_mode_enabled

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _focus_mode_enabled {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1451.

```text
uest_from {
  int32 allow_chat_request_from = 8;
  }
  oneof _auto_top {
  bool auto_top = 9;
  }
  oneof _focus_mode_enabled {
  bool focus_mode_enabled = 10;
  }
  oneof _allow_challenges_from {
  int32 allow_challenges_from = 11;
  }
  oneof _seek_base_time {
  int32 seek_base_time = 12;
  }
  oneof _seek_min_rating {
  int32 seek_min_rating = 13;
  }
  oneof _seek_max_rating {
  int32 seek_max_rating = 14;
  }
  
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11108"></a>
## FND-11108: chesscom.user_properties.v1.SettingsLiveChessProperty.focus_mode_enabled = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool focus_mode_enabled = 10;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1481.

```text
_request_from = 8;
  }
  oneof _auto_top {
  bool auto_top = 9;
  }
  oneof _focus_mode_enabled {
  bool focus_mode_enabled = 10;
  }
  oneof _allow_challenges_from {
  int32 allow_challenges_from = 11;
  }
  oneof _seek_base_time {
  int32 seek_base_time = 12;
  }
  oneof _seek_min_rating {
  int32 seek_min_rating = 13;
  }
  oneof _seek_max_rating {
  int32 seek_max_rating = 14;
  }
  oneof _challenge_popup_alert {
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11109"></a>
## FND-11109: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._allow_challenges_from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _allow_challenges_from {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1517.

```text
_top {
  bool auto_top = 9;
  }
  oneof _focus_mode_enabled {
  bool focus_mode_enabled = 10;
  }
  oneof _allow_challenges_from {
  int32 allow_challenges_from = 11;
  }
  oneof _seek_base_time {
  int32 seek_base_time = 12;
  }
  oneof _seek_min_rating {
  int32 seek_min_rating = 13;
  }
  oneof _seek_max_rating {
  int32 seek_max_rating = 14;
  }
  oneof _challenge_popup_alert {
  int32 challenge_popup_alert = 15;
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11110"></a>
## FND-11110: chesscom.user_properties.v1.SettingsLiveChessProperty.allow_challenges_from = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 allow_challenges_from = 11;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1550.

```text
 oneof _focus_mode_enabled {
  bool focus_mode_enabled = 10;
  }
  oneof _allow_challenges_from {
  int32 allow_challenges_from = 11;
  }
  oneof _seek_base_time {
  int32 seek_base_time = 12;
  }
  oneof _seek_min_rating {
  int32 seek_min_rating = 13;
  }
  oneof _seek_max_rating {
  int32 seek_max_rating = 14;
  }
  oneof _challenge_popup_alert {
  int32 challenge_popup_alert = 15;
  }
  oneof _friend_popup_alert 
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11111"></a>
## FND-11111: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._seek_base_time

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _seek_base_time {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1590.

```text
s_mode_enabled = 10;
  }
  oneof _allow_challenges_from {
  int32 allow_challenges_from = 11;
  }
  oneof _seek_base_time {
  int32 seek_base_time = 12;
  }
  oneof _seek_min_rating {
  int32 seek_min_rating = 13;
  }
  oneof _seek_max_rating {
  int32 seek_max_rating = 14;
  }
  oneof _challenge_popup_alert {
  int32 challenge_popup_alert = 15;
  }
  oneof _friend_popup_alert {
  int32 friend_popup_alert = 16;
  }
 
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11112"></a>
## FND-11112: chesscom.user_properties.v1.SettingsLiveChessProperty.seek_base_time = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 seek_base_time = 12;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1616.

```text
 oneof _allow_challenges_from {
  int32 allow_challenges_from = 11;
  }
  oneof _seek_base_time {
  int32 seek_base_time = 12;
  }
  oneof _seek_min_rating {
  int32 seek_min_rating = 13;
  }
  oneof _seek_max_rating {
  int32 seek_max_rating = 14;
  }
  oneof _challenge_popup_alert {
  int32 challenge_popup_alert = 15;
  }
  oneof _friend_popup_alert {
  int32 friend_popup_alert = 16;
  }
  oneof _event_announcement
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11113"></a>
## FND-11113: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._seek_min_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _seek_min_rating {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1649.

```text
 int32 allow_challenges_from = 11;
  }
  oneof _seek_base_time {
  int32 seek_base_time = 12;
  }
  oneof _seek_min_rating {
  int32 seek_min_rating = 13;
  }
  oneof _seek_max_rating {
  int32 seek_max_rating = 14;
  }
  oneof _challenge_popup_alert {
  int32 challenge_popup_alert = 15;
  }
  oneof _friend_popup_alert {
  int32 friend_popup_alert = 16;
  }
  oneof _event_announcement {
  int32 event_announcement = 1
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11114"></a>
## FND-11114: chesscom.user_properties.v1.SettingsLiveChessProperty.seek_min_rating = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 seek_min_rating = 13;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1676.

```text
m = 11;
  }
  oneof _seek_base_time {
  int32 seek_base_time = 12;
  }
  oneof _seek_min_rating {
  int32 seek_min_rating = 13;
  }
  oneof _seek_max_rating {
  int32 seek_max_rating = 14;
  }
  oneof _challenge_popup_alert {
  int32 challenge_popup_alert = 15;
  }
  oneof _friend_popup_alert {
  int32 friend_popup_alert = 16;
  }
  oneof _event_announcement {
  int32 event_announcement = 17;
  }
  oneof _challenge_m
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11115"></a>
## FND-11115: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._seek_max_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _seek_max_rating {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1710.

```text
e {
  int32 seek_base_time = 12;
  }
  oneof _seek_min_rating {
  int32 seek_min_rating = 13;
  }
  oneof _seek_max_rating {
  int32 seek_max_rating = 14;
  }
  oneof _challenge_popup_alert {
  int32 challenge_popup_alert = 15;
  }
  oneof _friend_popup_alert {
  int32 friend_popup_alert = 16;
  }
  oneof _event_announcement {
  int32 event_announcement = 17;
  }
  oneof _challenge_min_rating {
  int32 challenge_min_
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11116"></a>
## FND-11116: chesscom.user_properties.v1.SettingsLiveChessProperty.seek_max_rating = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 seek_max_rating = 14;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1737.

```text
= 12;
  }
  oneof _seek_min_rating {
  int32 seek_min_rating = 13;
  }
  oneof _seek_max_rating {
  int32 seek_max_rating = 14;
  }
  oneof _challenge_popup_alert {
  int32 challenge_popup_alert = 15;
  }
  oneof _friend_popup_alert {
  int32 friend_popup_alert = 16;
  }
  oneof _event_announcement {
  int32 event_announcement = 17;
  }
  oneof _challenge_min_rating {
  int32 challenge_min_rating = 18;
  }
  oneof _c
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11117"></a>
## FND-11117: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._challenge_popup_alert

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _challenge_popup_alert {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1771.

```text
 {
  int32 seek_min_rating = 13;
  }
  oneof _seek_max_rating {
  int32 seek_max_rating = 14;
  }
  oneof _challenge_popup_alert {
  int32 challenge_popup_alert = 15;
  }
  oneof _friend_popup_alert {
  int32 friend_popup_alert = 16;
  }
  oneof _event_announcement {
  int32 event_announcement = 17;
  }
  oneof _challenge_min_rating {
  int32 challenge_min_rating = 18;
  }
  oneof _challenge_max_rating {
  int32 chal
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11118"></a>
## FND-11118: chesscom.user_properties.v1.SettingsLiveChessProperty.challenge_popup_alert = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 challenge_popup_alert = 15;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1804.

```text
  }
  oneof _seek_max_rating {
  int32 seek_max_rating = 14;
  }
  oneof _challenge_popup_alert {
  int32 challenge_popup_alert = 15;
  }
  oneof _friend_popup_alert {
  int32 friend_popup_alert = 16;
  }
  oneof _event_announcement {
  int32 event_announcement = 17;
  }
  oneof _challenge_min_rating {
  int32 challenge_min_rating = 18;
  }
  oneof _challenge_max_rating {
  int32 challenge_max_rating = 19;
  }
  oneo
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11119"></a>
## FND-11119: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._friend_popup_alert

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _friend_popup_alert {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1844.

```text
eek_max_rating = 14;
  }
  oneof _challenge_popup_alert {
  int32 challenge_popup_alert = 15;
  }
  oneof _friend_popup_alert {
  int32 friend_popup_alert = 16;
  }
  oneof _event_announcement {
  int32 event_announcement = 17;
  }
  oneof _challenge_min_rating {
  int32 challenge_min_rating = 18;
  }
  oneof _challenge_max_rating {
  int32 challenge_max_rating = 19;
  }
  oneof _seek_base_time_variants {
  int32 see
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11120"></a>
## FND-11120: chesscom.user_properties.v1.SettingsLiveChessProperty.friend_popup_alert = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 friend_popup_alert = 16;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1874.

```text
of _challenge_popup_alert {
  int32 challenge_popup_alert = 15;
  }
  oneof _friend_popup_alert {
  int32 friend_popup_alert = 16;
  }
  oneof _event_announcement {
  int32 event_announcement = 17;
  }
  oneof _challenge_min_rating {
  int32 challenge_min_rating = 18;
  }
  oneof _challenge_max_rating {
  int32 challenge_max_rating = 19;
  }
  oneof _seek_base_time_variants {
  int32 seek_base_time_variants = 20;
  }
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11121"></a>
## FND-11121: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._event_announcement

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _event_announcement {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1911.

```text
hallenge_popup_alert = 15;
  }
  oneof _friend_popup_alert {
  int32 friend_popup_alert = 16;
  }
  oneof _event_announcement {
  int32 event_announcement = 17;
  }
  oneof _challenge_min_rating {
  int32 challenge_min_rating = 18;
  }
  oneof _challenge_max_rating {
  int32 challenge_max_rating = 19;
  }
  oneof _seek_base_time_variants {
  int32 seek_base_time_variants = 20;
  }
  oneof _seek_increment_variants {
 
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11122"></a>
## FND-11122: chesscom.user_properties.v1.SettingsLiveChessProperty.event_announcement = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 event_announcement = 17;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1941.

```text

  oneof _friend_popup_alert {
  int32 friend_popup_alert = 16;
  }
  oneof _event_announcement {
  int32 event_announcement = 17;
  }
  oneof _challenge_min_rating {
  int32 challenge_min_rating = 18;
  }
  oneof _challenge_max_rating {
  int32 challenge_max_rating = 19;
  }
  oneof _seek_base_time_variants {
  int32 seek_base_time_variants = 20;
  }
  oneof _seek_increment_variants {
  int32 seek_increment_variants
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11123"></a>
## FND-11123: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._challenge_min_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _challenge_min_rating {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 1978.

```text
2 friend_popup_alert = 16;
  }
  oneof _event_announcement {
  int32 event_announcement = 17;
  }
  oneof _challenge_min_rating {
  int32 challenge_min_rating = 18;
  }
  oneof _challenge_max_rating {
  int32 challenge_max_rating = 19;
  }
  oneof _seek_base_time_variants {
  int32 seek_base_time_variants = 20;
  }
  oneof _seek_increment_variants {
  int32 seek_increment_variants = 21;
  }
  oneof _seek_base_time_ch
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11124"></a>
## FND-11124: chesscom.user_properties.v1.SettingsLiveChessProperty.challenge_min_rating = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 challenge_min_rating = 18;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 2010.

```text
 oneof _event_announcement {
  int32 event_announcement = 17;
  }
  oneof _challenge_min_rating {
  int32 challenge_min_rating = 18;
  }
  oneof _challenge_max_rating {
  int32 challenge_max_rating = 19;
  }
  oneof _seek_base_time_variants {
  int32 seek_base_time_variants = 20;
  }
  oneof _seek_increment_variants {
  int32 seek_increment_variants = 21;
  }
  oneof _seek_base_time_chess {
  int32 seek_base_time_che
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11125"></a>
## FND-11125: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._challenge_max_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _challenge_max_rating {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 2049.

```text
ent_announcement = 17;
  }
  oneof _challenge_min_rating {
  int32 challenge_min_rating = 18;
  }
  oneof _challenge_max_rating {
  int32 challenge_max_rating = 19;
  }
  oneof _seek_base_time_variants {
  int32 seek_base_time_variants = 20;
  }
  oneof _seek_increment_variants {
  int32 seek_increment_variants = 21;
  }
  oneof _seek_base_time_chess {
  int32 seek_base_time_chess = 22;
  }
  oneof _seek_increment_ch
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11126"></a>
## FND-11126: chesscom.user_properties.v1.SettingsLiveChessProperty.challenge_max_rating = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 challenge_max_rating = 19;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 2081.

```text
of _challenge_min_rating {
  int32 challenge_min_rating = 18;
  }
  oneof _challenge_max_rating {
  int32 challenge_max_rating = 19;
  }
  oneof _seek_base_time_variants {
  int32 seek_base_time_variants = 20;
  }
  oneof _seek_increment_variants {
  int32 seek_increment_variants = 21;
  }
  oneof _seek_base_time_chess {
  int32 seek_base_time_chess = 22;
  }
  oneof _seek_increment_chess {
  int32 seek_increment_che
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11127"></a>
## FND-11127: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._seek_base_time_variants

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _seek_base_time_variants {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 2120.

```text
lenge_min_rating = 18;
  }
  oneof _challenge_max_rating {
  int32 challenge_max_rating = 19;
  }
  oneof _seek_base_time_variants {
  int32 seek_base_time_variants = 20;
  }
  oneof _seek_increment_variants {
  int32 seek_increment_variants = 21;
  }
  oneof _seek_base_time_chess {
  int32 seek_base_time_chess = 22;
  }
  oneof _seek_increment_chess {
  int32 seek_increment_chess = 23;
  }
  oneof _allow_game_chat {
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11128"></a>
## FND-11128: chesscom.user_properties.v1.SettingsLiveChessProperty.seek_base_time_variants = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 seek_base_time_variants = 20;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 2155.

```text
_challenge_max_rating {
  int32 challenge_max_rating = 19;
  }
  oneof _seek_base_time_variants {
  int32 seek_base_time_variants = 20;
  }
  oneof _seek_increment_variants {
  int32 seek_increment_variants = 21;
  }
  oneof _seek_base_time_chess {
  int32 seek_base_time_chess = 22;
  }
  oneof _seek_increment_chess {
  int32 seek_increment_chess = 23;
  }
  oneof _allow_game_chat {
  int32 allow_game_chat = 24;
  }

```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11129"></a>
## FND-11129: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._seek_increment_variants

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _seek_increment_variants {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 2197.

```text
max_rating = 19;
  }
  oneof _seek_base_time_variants {
  int32 seek_base_time_variants = 20;
  }
  oneof _seek_increment_variants {
  int32 seek_increment_variants = 21;
  }
  oneof _seek_base_time_chess {
  int32 seek_base_time_chess = 22;
  }
  oneof _seek_increment_chess {
  int32 seek_increment_chess = 23;
  }
  oneof _allow_game_chat {
  int32 allow_game_chat = 24;
  }
}

```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11130"></a>
## FND-11130: chesscom.user_properties.v1.SettingsLiveChessProperty.seek_increment_variants = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 seek_increment_variants = 21;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 2232.

```text
base_time_variants {
  int32 seek_base_time_variants = 20;
  }
  oneof _seek_increment_variants {
  int32 seek_increment_variants = 21;
  }
  oneof _seek_base_time_chess {
  int32 seek_base_time_chess = 22;
  }
  oneof _seek_increment_chess {
  int32 seek_increment_chess = 23;
  }
  oneof _allow_game_chat {
  int32 allow_game_chat = 24;
  }
}

```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11131"></a>
## FND-11131: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._seek_base_time_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _seek_base_time_chess {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 2274.

```text
e_variants = 20;
  }
  oneof _seek_increment_variants {
  int32 seek_increment_variants = 21;
  }
  oneof _seek_base_time_chess {
  int32 seek_base_time_chess = 22;
  }
  oneof _seek_increment_chess {
  int32 seek_increment_chess = 23;
  }
  oneof _allow_game_chat {
  int32 allow_game_chat = 24;
  }
}

```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11132"></a>
## FND-11132: chesscom.user_properties.v1.SettingsLiveChessProperty.seek_base_time_chess = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 seek_base_time_chess = 22;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 2306.

```text
ek_increment_variants {
  int32 seek_increment_variants = 21;
  }
  oneof _seek_base_time_chess {
  int32 seek_base_time_chess = 22;
  }
  oneof _seek_increment_chess {
  int32 seek_increment_chess = 23;
  }
  oneof _allow_game_chat {
  int32 allow_game_chat = 24;
  }
}

```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11133"></a>
## FND-11133: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._seek_increment_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _seek_increment_chess {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 2345.

```text
crement_variants = 21;
  }
  oneof _seek_base_time_chess {
  int32 seek_base_time_chess = 22;
  }
  oneof _seek_increment_chess {
  int32 seek_increment_chess = 23;
  }
  oneof _allow_game_chat {
  int32 allow_game_chat = 24;
  }
}

```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11134"></a>
## FND-11134: chesscom.user_properties.v1.SettingsLiveChessProperty.seek_increment_chess = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 seek_increment_chess = 23;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 2377.

```text
of _seek_base_time_chess {
  int32 seek_base_time_chess = 22;
  }
  oneof _seek_increment_chess {
  int32 seek_increment_chess = 23;
  }
  oneof _allow_game_chat {
  int32 allow_game_chat = 24;
  }
}

```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11135"></a>
## FND-11135: oneof declaration: chesscom.user_properties.v1.SettingsLiveChessProperty._allow_game_chat

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _allow_game_chat {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 2416.

```text
_base_time_chess = 22;
  }
  oneof _seek_increment_chess {
  int32 seek_increment_chess = 23;
  }
  oneof _allow_game_chat {
  int32 allow_game_chat = 24;
  }
}

```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11136"></a>
## FND-11136: chesscom.user_properties.v1.SettingsLiveChessProperty.allow_game_chat = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 allow_game_chat = 24;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 2443.

```text
  oneof _seek_increment_chess {
  int32 seek_increment_chess = 23;
  }
  oneof _allow_game_chat {
  int32 allow_game_chat = 24;
  }
}

```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11137"></a>
## FND-11137: enum declaration: chesscom.user_properties.v1.SkillsPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SkillsPropertyDefinition {

### Evidence

- **SRC-0629** `research/proto/chesscom/user_properties/v1/properties_skills.proto` — [preserved redacted evidence](../evidence/text/f52240cb37433d05089da30b8b3b69106c34fedb91580ba2e0cf3faf0119e3da.proto)
  Character offset 120.

```text
user_properties/v1/properties_skills.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum SkillsPropertyDefinition {
  SKILLS_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  SKILLS_PROPERTY_DEFINITION_UNLOCKED_SKILLS = 1;
  SKILLS_PROPERTY_DEFINITION_MASTERED_SKILLS = 2;
}

message SkillsProperty {
  repeated string unlocked_skills = 1;
  repeated string mastered_skills = 2;
}

```

**Source references:** SRC-0629, SRC-1600  
**URL references:** None independently associated  
**Related findings:** FND-11138, FND-11139

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11138"></a>
## FND-11138: chesscom.user_properties.v1.SkillsPropertyDefinition.SKILLS_PROPERTY_DEFINITION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILLS_PROPERTY_DEFINITION_UNSPECIFIED = 0;

### Evidence

- **SRC-0629** `research/proto/chesscom/user_properties/v1/properties_skills.proto` — [preserved redacted evidence](../evidence/text/f52240cb37433d05089da30b8b3b69106c34fedb91580ba2e0cf3faf0119e3da.proto)
  Character offset 154.

```text
ls.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum SkillsPropertyDefinition {
  SKILLS_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  SKILLS_PROPERTY_DEFINITION_UNLOCKED_SKILLS = 1;
  SKILLS_PROPERTY_DEFINITION_MASTERED_SKILLS = 2;
}

message SkillsProperty {
  repeated string unlocked_skills = 1;
  repeated string mastered_skills = 2;
}

```

**Source references:** SRC-0629, SRC-1600  
**URL references:** None independently associated  
**Related findings:** FND-11137, FND-11139

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11139"></a>
## FND-11139: chesscom.user_properties.v1.SkillsPropertyDefinition.SKILLS_PROPERTY_DEFINITION_UNLOCKED_SKILLS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILLS_PROPERTY_DEFINITION_UNLOCKED_SKILLS = 1;

### Evidence

- **SRC-0629** `research/proto/chesscom/user_properties/v1/properties_skills.proto` — [preserved redacted evidence](../evidence/text/f52240cb37433d05089da30b8b3b69106c34fedb91580ba2e0cf3faf0119e3da.proto)
  Character offset 200.

```text
ser_properties.v1;

enum SkillsPropertyDefinition {
  SKILLS_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  SKILLS_PROPERTY_DEFINITION_UNLOCKED_SKILLS = 1;
  SKILLS_PROPERTY_DEFINITION_MASTERED_SKILLS = 2;
}

message SkillsProperty {
  repeated string unlocked_skills = 1;
  repeated string mastered_skills = 2;
}

```

**Source references:** SRC-0629, SRC-1600  
**URL references:** None independently associated  
**Related findings:** FND-11137, FND-11138

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11140"></a>
## FND-11140: chesscom.user_properties.v1.SkillsPropertyDefinition.SKILLS_PROPERTY_DEFINITION_MASTERED_SKILLS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILLS_PROPERTY_DEFINITION_MASTERED_SKILLS = 2;

### Evidence

- **SRC-0629** `research/proto/chesscom/user_properties/v1/properties_skills.proto` — [preserved redacted evidence](../evidence/text/f52240cb37433d05089da30b8b3b69106c34fedb91580ba2e0cf3faf0119e3da.proto)
  Character offset 250.

```text
{
  SKILLS_PROPERTY_DEFINITION_UNSPECIFIED = 0;
  SKILLS_PROPERTY_DEFINITION_UNLOCKED_SKILLS = 1;
  SKILLS_PROPERTY_DEFINITION_MASTERED_SKILLS = 2;
}

message SkillsProperty {
  repeated string unlocked_skills = 1;
  repeated string mastered_skills = 2;
}

```

**Source references:** SRC-0629, SRC-1600  
**URL references:** None independently associated  
**Related findings:** FND-11137, FND-11138, FND-11139

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11141"></a>
## FND-11141: message declaration: chesscom.user_properties.v1.SkillsProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillsProperty {

### Evidence

- **SRC-0629** `research/proto/chesscom/user_properties/v1/properties_skills.proto` — [preserved redacted evidence](../evidence/text/f52240cb37433d05089da30b8b3b69106c34fedb91580ba2e0cf3faf0119e3da.proto)
  Character offset 301.

```text
KILLS_PROPERTY_DEFINITION_UNLOCKED_SKILLS = 1;
  SKILLS_PROPERTY_DEFINITION_MASTERED_SKILLS = 2;
}

message SkillsProperty {
  repeated string unlocked_skills = 1;
  repeated string mastered_skills = 2;
}

```

**Source references:** SRC-0629, SRC-1600  
**URL references:** None independently associated  
**Related findings:** FND-11137, FND-11138, FND-11139

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11142"></a>
## FND-11142: chesscom.user_properties.v1.SkillsProperty.unlocked_skills = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string unlocked_skills = 1;

### Evidence

- **SRC-0629** `research/proto/chesscom/user_properties/v1/properties_skills.proto` — [preserved redacted evidence](../evidence/text/f52240cb37433d05089da30b8b3b69106c34fedb91580ba2e0cf3faf0119e3da.proto)
  Character offset 328.

```text
NLOCKED_SKILLS = 1;
  SKILLS_PROPERTY_DEFINITION_MASTERED_SKILLS = 2;
}

message SkillsProperty {
  repeated string unlocked_skills = 1;
  repeated string mastered_skills = 2;
}

```

**Source references:** SRC-0629, SRC-1600  
**URL references:** None independently associated  
**Related findings:** FND-11137, FND-11138, FND-11139

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11143"></a>
## FND-11143: chesscom.user_properties.v1.SkillsProperty.mastered_skills = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string mastered_skills = 2;

### Evidence

- **SRC-0629** `research/proto/chesscom/user_properties/v1/properties_skills.proto` — [preserved redacted evidence](../evidence/text/f52240cb37433d05089da30b8b3b69106c34fedb91580ba2e0cf3faf0119e3da.proto)
  Character offset 367.

```text
EFINITION_MASTERED_SKILLS = 2;
}

message SkillsProperty {
  repeated string unlocked_skills = 1;
  repeated string mastered_skills = 2;
}

```

**Source references:** SRC-0629, SRC-1600  
**URL references:** None independently associated  
**Related findings:** FND-11137, FND-11138, FND-11139

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11144"></a>
## FND-11144: enum declaration: chesscom.user_properties.v1.StatsDailyPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum StatsDailyPropertyDefinition {

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 125.

```text
properties/v1/properties_stats_daily.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum StatsDailyPropertyDefinition {
  STATS_DAILY_PROPERTY_UNSPECIFIED = 0;
  STATS_DAILY_TOTAL_GAME_COUNT = 1;
  STATS_DAILY_TOURNAMENT_COUNT = 2;
  STATS_DAILY_TOURNAMENT_GAME_WIN_COUNT = 3;
  STATS_DAILY_TOURNAMENT_GAME_LOSS_COUNT = 4;
  STATS_DAILY_TOURNAMENT_GAME_DRAW_COUNT = 5;
  STATS_DAILY_TOURNAMENT_1ST_PLACE 
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11145"></a>
## FND-11145: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 163.

```text
roto
// syntax: proto3

package chesscom.user_properties.v1;

enum StatsDailyPropertyDefinition {
  STATS_DAILY_PROPERTY_UNSPECIFIED = 0;
  STATS_DAILY_TOTAL_GAME_COUNT = 1;
  STATS_DAILY_TOURNAMENT_COUNT = 2;
  STATS_DAILY_TOURNAMENT_GAME_WIN_COUNT = 3;
  STATS_DAILY_TOURNAMENT_GAME_LOSS_COUNT = 4;
  STATS_DAILY_TOURNAMENT_GAME_DRAW_COUNT = 5;
  STATS_DAILY_TOURNAMENT_1ST_PLACE = 6;
  STATS_DAILY_TOURNAMENT_2ND_PLAC
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11146"></a>
## FND-11146: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOTAL_GAME_COUNT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOTAL_GAME_COUNT = 1;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 203.

```text
.user_properties.v1;

enum StatsDailyPropertyDefinition {
  STATS_DAILY_PROPERTY_UNSPECIFIED = 0;
  STATS_DAILY_TOTAL_GAME_COUNT = 1;
  STATS_DAILY_TOURNAMENT_COUNT = 2;
  STATS_DAILY_TOURNAMENT_GAME_WIN_COUNT = 3;
  STATS_DAILY_TOURNAMENT_GAME_LOSS_COUNT = 4;
  STATS_DAILY_TOURNAMENT_GAME_DRAW_COUNT = 5;
  STATS_DAILY_TOURNAMENT_1ST_PLACE = 6;
  STATS_DAILY_TOURNAMENT_2ND_PLACE = 7;
  STATS_DAILY_TOURNAMENT_3RD_PLAC
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11147"></a>
## FND-11147: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_COUNT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_COUNT = 2;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 239.

```text
yPropertyDefinition {
  STATS_DAILY_PROPERTY_UNSPECIFIED = 0;
  STATS_DAILY_TOTAL_GAME_COUNT = 1;
  STATS_DAILY_TOURNAMENT_COUNT = 2;
  STATS_DAILY_TOURNAMENT_GAME_WIN_COUNT = 3;
  STATS_DAILY_TOURNAMENT_GAME_LOSS_COUNT = 4;
  STATS_DAILY_TOURNAMENT_GAME_DRAW_COUNT = 5;
  STATS_DAILY_TOURNAMENT_1ST_PLACE = 6;
  STATS_DAILY_TOURNAMENT_2ND_PLACE = 7;
  STATS_DAILY_TOURNAMENT_3RD_PLACE = 8;
  STATS_DAILY_TOURNAMENT_HOST
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11148"></a>
## FND-11148: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_GAME_WIN_COUNT = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_GAME_WIN_COUNT = 3;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 275.

```text
PROPERTY_UNSPECIFIED = 0;
  STATS_DAILY_TOTAL_GAME_COUNT = 1;
  STATS_DAILY_TOURNAMENT_COUNT = 2;
  STATS_DAILY_TOURNAMENT_GAME_WIN_COUNT = 3;
  STATS_DAILY_TOURNAMENT_GAME_LOSS_COUNT = 4;
  STATS_DAILY_TOURNAMENT_GAME_DRAW_COUNT = 5;
  STATS_DAILY_TOURNAMENT_1ST_PLACE = 6;
  STATS_DAILY_TOURNAMENT_2ND_PLACE = 7;
  STATS_DAILY_TOURNAMENT_3RD_PLACE = 8;
  STATS_DAILY_TOURNAMENT_HOST_COUNT = 9;
  STATS_DAILY_TOURNAMENT
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11149"></a>
## FND-11149: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_GAME_LOSS_COUNT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_GAME_LOSS_COUNT = 4;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 320.

```text
_GAME_COUNT = 1;
  STATS_DAILY_TOURNAMENT_COUNT = 2;
  STATS_DAILY_TOURNAMENT_GAME_WIN_COUNT = 3;
  STATS_DAILY_TOURNAMENT_GAME_LOSS_COUNT = 4;
  STATS_DAILY_TOURNAMENT_GAME_DRAW_COUNT = 5;
  STATS_DAILY_TOURNAMENT_1ST_PLACE = 6;
  STATS_DAILY_TOURNAMENT_2ND_PLACE = 7;
  STATS_DAILY_TOURNAMENT_3RD_PLACE = 8;
  STATS_DAILY_TOURNAMENT_HOST_COUNT = 9;
  STATS_DAILY_TOURNAMENT_HOST_USER_COUNT = 10;
  STATS_DAILY_TOURNAME
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11150"></a>
## FND-11150: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_GAME_DRAW_COUNT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_GAME_DRAW_COUNT = 5;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 366.

```text
T = 2;
  STATS_DAILY_TOURNAMENT_GAME_WIN_COUNT = 3;
  STATS_DAILY_TOURNAMENT_GAME_LOSS_COUNT = 4;
  STATS_DAILY_TOURNAMENT_GAME_DRAW_COUNT = 5;
  STATS_DAILY_TOURNAMENT_1ST_PLACE = 6;
  STATS_DAILY_TOURNAMENT_2ND_PLACE = 7;
  STATS_DAILY_TOURNAMENT_3RD_PLACE = 8;
  STATS_DAILY_TOURNAMENT_HOST_COUNT = 9;
  STATS_DAILY_TOURNAMENT_HOST_USER_COUNT = 10;
  STATS_DAILY_TOURNAMENT_WITHDRAW_COUNT = 11;
  STATS_DAILY_TOURNAME
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11151"></a>
## FND-11151: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_1ST_PLACE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_1ST_PLACE = 6;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 412.

```text
 = 3;
  STATS_DAILY_TOURNAMENT_GAME_LOSS_COUNT = 4;
  STATS_DAILY_TOURNAMENT_GAME_DRAW_COUNT = 5;
  STATS_DAILY_TOURNAMENT_1ST_PLACE = 6;
  STATS_DAILY_TOURNAMENT_2ND_PLACE = 7;
  STATS_DAILY_TOURNAMENT_3RD_PLACE = 8;
  STATS_DAILY_TOURNAMENT_HOST_COUNT = 9;
  STATS_DAILY_TOURNAMENT_HOST_USER_COUNT = 10;
  STATS_DAILY_TOURNAMENT_WITHDRAW_COUNT = 11;
  STATS_DAILY_TOURNAMENT_IN_PROGRESS_COUNT = 12;
  STATS_DAILY_TOURN
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11152"></a>
## FND-11152: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_2ND_PLACE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_2ND_PLACE = 7;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 452.

```text
_COUNT = 4;
  STATS_DAILY_TOURNAMENT_GAME_DRAW_COUNT = 5;
  STATS_DAILY_TOURNAMENT_1ST_PLACE = 6;
  STATS_DAILY_TOURNAMENT_2ND_PLACE = 7;
  STATS_DAILY_TOURNAMENT_3RD_PLACE = 8;
  STATS_DAILY_TOURNAMENT_HOST_COUNT = 9;
  STATS_DAILY_TOURNAMENT_HOST_USER_COUNT = 10;
  STATS_DAILY_TOURNAMENT_WITHDRAW_COUNT = 11;
  STATS_DAILY_TOURNAMENT_IN_PROGRESS_COUNT = 12;
  STATS_DAILY_TOURNAMENT_CANCEL_COUNT = 13;
  STATS_DAILY_T
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11153"></a>
## FND-11153: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_3RD_PLACE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_3RD_PLACE = 8;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 492.

```text
E_DRAW_COUNT = 5;
  STATS_DAILY_TOURNAMENT_1ST_PLACE = 6;
  STATS_DAILY_TOURNAMENT_2ND_PLACE = 7;
  STATS_DAILY_TOURNAMENT_3RD_PLACE = 8;
  STATS_DAILY_TOURNAMENT_HOST_COUNT = 9;
  STATS_DAILY_TOURNAMENT_HOST_USER_COUNT = 10;
  STATS_DAILY_TOURNAMENT_WITHDRAW_COUNT = 11;
  STATS_DAILY_TOURNAMENT_IN_PROGRESS_COUNT = 12;
  STATS_DAILY_TOURNAMENT_CANCEL_COUNT = 13;
  STATS_DAILY_TOURNAMENT_POINTS = 14;
  STATS_DAILY_TOU
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11154"></a>
## FND-11154: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_HOST_COUNT = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_HOST_COUNT = 9;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 532.

```text
NT_1ST_PLACE = 6;
  STATS_DAILY_TOURNAMENT_2ND_PLACE = 7;
  STATS_DAILY_TOURNAMENT_3RD_PLACE = 8;
  STATS_DAILY_TOURNAMENT_HOST_COUNT = 9;
  STATS_DAILY_TOURNAMENT_HOST_USER_COUNT = 10;
  STATS_DAILY_TOURNAMENT_WITHDRAW_COUNT = 11;
  STATS_DAILY_TOURNAMENT_IN_PROGRESS_COUNT = 12;
  STATS_DAILY_TOURNAMENT_CANCEL_COUNT = 13;
  STATS_DAILY_TOURNAMENT_POINTS = 14;
  STATS_DAILY_TOURNAMENT_COUNT_TOTAL = 15;
  STATS_DAILY_
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11155"></a>
## FND-11155: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_HOST_USER_COUNT = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_HOST_USER_COUNT = 10;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 573.

```text
T_2ND_PLACE = 7;
  STATS_DAILY_TOURNAMENT_3RD_PLACE = 8;
  STATS_DAILY_TOURNAMENT_HOST_COUNT = 9;
  STATS_DAILY_TOURNAMENT_HOST_USER_COUNT = 10;
  STATS_DAILY_TOURNAMENT_WITHDRAW_COUNT = 11;
  STATS_DAILY_TOURNAMENT_IN_PROGRESS_COUNT = 12;
  STATS_DAILY_TOURNAMENT_CANCEL_COUNT = 13;
  STATS_DAILY_TOURNAMENT_POINTS = 14;
  STATS_DAILY_TOURNAMENT_COUNT_TOTAL = 15;
  STATS_DAILY_TOURNAMENT_POINTS_TOTAL = 16;
  STATS_DAI
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11156"></a>
## FND-11156: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_WITHDRAW_COUNT = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_WITHDRAW_COUNT = 11;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 620.

```text
LACE = 8;
  STATS_DAILY_TOURNAMENT_HOST_COUNT = 9;
  STATS_DAILY_TOURNAMENT_HOST_USER_COUNT = 10;
  STATS_DAILY_TOURNAMENT_WITHDRAW_COUNT = 11;
  STATS_DAILY_TOURNAMENT_IN_PROGRESS_COUNT = 12;
  STATS_DAILY_TOURNAMENT_CANCEL_COUNT = 13;
  STATS_DAILY_TOURNAMENT_POINTS = 14;
  STATS_DAILY_TOURNAMENT_COUNT_TOTAL = 15;
  STATS_DAILY_TOURNAMENT_POINTS_TOTAL = 16;
  STATS_DAILY_TOURNAMENT_COUNT_PREVIOUS = 17;
  STATS_DAIL
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11157"></a>
## FND-11157: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_IN_PROGRESS_COUNT = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_IN_PROGRESS_COUNT = 12;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 666.

```text
= 9;
  STATS_DAILY_TOURNAMENT_HOST_USER_COUNT = 10;
  STATS_DAILY_TOURNAMENT_WITHDRAW_COUNT = 11;
  STATS_DAILY_TOURNAMENT_IN_PROGRESS_COUNT = 12;
  STATS_DAILY_TOURNAMENT_CANCEL_COUNT = 13;
  STATS_DAILY_TOURNAMENT_POINTS = 14;
  STATS_DAILY_TOURNAMENT_COUNT_TOTAL = 15;
  STATS_DAILY_TOURNAMENT_POINTS_TOTAL = 16;
  STATS_DAILY_TOURNAMENT_COUNT_PREVIOUS = 17;
  STATS_DAILY_TOURNAMENT_POINTS_PREVIOUS = 18;
  STATS_DAI
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11158"></a>
## FND-11158: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_CANCEL_COUNT = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_CANCEL_COUNT = 13;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 715.

```text
0;
  STATS_DAILY_TOURNAMENT_WITHDRAW_COUNT = 11;
  STATS_DAILY_TOURNAMENT_IN_PROGRESS_COUNT = 12;
  STATS_DAILY_TOURNAMENT_CANCEL_COUNT = 13;
  STATS_DAILY_TOURNAMENT_POINTS = 14;
  STATS_DAILY_TOURNAMENT_COUNT_TOTAL = 15;
  STATS_DAILY_TOURNAMENT_POINTS_TOTAL = 16;
  STATS_DAILY_TOURNAMENT_COUNT_PREVIOUS = 17;
  STATS_DAILY_TOURNAMENT_POINTS_PREVIOUS = 18;
  STATS_DAILY_UNRATED_GAME_COUNT = 19;
  STATS_DAILY_IN_PROG
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11159"></a>
## FND-11159: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_POINTS = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_POINTS = 14;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 759.

```text
 11;
  STATS_DAILY_TOURNAMENT_IN_PROGRESS_COUNT = 12;
  STATS_DAILY_TOURNAMENT_CANCEL_COUNT = 13;
  STATS_DAILY_TOURNAMENT_POINTS = 14;
  STATS_DAILY_TOURNAMENT_COUNT_TOTAL = 15;
  STATS_DAILY_TOURNAMENT_POINTS_TOTAL = 16;
  STATS_DAILY_TOURNAMENT_COUNT_PREVIOUS = 17;
  STATS_DAILY_TOURNAMENT_POINTS_PREVIOUS = 18;
  STATS_DAILY_UNRATED_GAME_COUNT = 19;
  STATS_DAILY_IN_PROGRESS_COUNT = 20;
  STATS_DAILY_TIMEOUT_COUNT
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11160"></a>
## FND-11160: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_COUNT_TOTAL = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_COUNT_TOTAL = 15;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 797.

```text
ESS_COUNT = 12;
  STATS_DAILY_TOURNAMENT_CANCEL_COUNT = 13;
  STATS_DAILY_TOURNAMENT_POINTS = 14;
  STATS_DAILY_TOURNAMENT_COUNT_TOTAL = 15;
  STATS_DAILY_TOURNAMENT_POINTS_TOTAL = 16;
  STATS_DAILY_TOURNAMENT_COUNT_PREVIOUS = 17;
  STATS_DAILY_TOURNAMENT_POINTS_PREVIOUS = 18;
  STATS_DAILY_UNRATED_GAME_COUNT = 19;
  STATS_DAILY_IN_PROGRESS_COUNT = 20;
  STATS_DAILY_TIMEOUT_COUNT = 21;
  STATS_DAILY_MOVES_PER_GAME = 
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11161"></a>
## FND-11161: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_POINTS_TOTAL = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_POINTS_TOTAL = 16;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 840.

```text
NCEL_COUNT = 13;
  STATS_DAILY_TOURNAMENT_POINTS = 14;
  STATS_DAILY_TOURNAMENT_COUNT_TOTAL = 15;
  STATS_DAILY_TOURNAMENT_POINTS_TOTAL = 16;
  STATS_DAILY_TOURNAMENT_COUNT_PREVIOUS = 17;
  STATS_DAILY_TOURNAMENT_POINTS_PREVIOUS = 18;
  STATS_DAILY_UNRATED_GAME_COUNT = 19;
  STATS_DAILY_IN_PROGRESS_COUNT = 20;
  STATS_DAILY_TIMEOUT_COUNT = 21;
  STATS_DAILY_MOVES_PER_GAME = 22;
  STATS_DAILY_TOTAL_MOVE_TIME = 23;
  S
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11162"></a>
## FND-11162: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_COUNT_PREVIOUS = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_COUNT_PREVIOUS = 17;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 884.

```text
INTS = 14;
  STATS_DAILY_TOURNAMENT_COUNT_TOTAL = 15;
  STATS_DAILY_TOURNAMENT_POINTS_TOTAL = 16;
  STATS_DAILY_TOURNAMENT_COUNT_PREVIOUS = 17;
  STATS_DAILY_TOURNAMENT_POINTS_PREVIOUS = 18;
  STATS_DAILY_UNRATED_GAME_COUNT = 19;
  STATS_DAILY_IN_PROGRESS_COUNT = 20;
  STATS_DAILY_TIMEOUT_COUNT = 21;
  STATS_DAILY_MOVES_PER_GAME = 22;
  STATS_DAILY_TOTAL_MOVE_TIME = 23;
  STATS_DAILY_TOTAL_MOVE_COUNT = 24;
  STATS_DA
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11163"></a>
## FND-11163: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOURNAMENT_POINTS_PREVIOUS = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOURNAMENT_POINTS_PREVIOUS = 18;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 930.

```text
L = 15;
  STATS_DAILY_TOURNAMENT_POINTS_TOTAL = 16;
  STATS_DAILY_TOURNAMENT_COUNT_PREVIOUS = 17;
  STATS_DAILY_TOURNAMENT_POINTS_PREVIOUS = 18;
  STATS_DAILY_UNRATED_GAME_COUNT = 19;
  STATS_DAILY_IN_PROGRESS_COUNT = 20;
  STATS_DAILY_TIMEOUT_COUNT = 21;
  STATS_DAILY_MOVES_PER_GAME = 22;
  STATS_DAILY_TOTAL_MOVE_TIME = 23;
  STATS_DAILY_TOTAL_MOVE_COUNT = 24;
  STATS_DAILY_LAST_GAME_DATE = 25;
  STATS_DAILY_CURRENT
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11164"></a>
## FND-11164: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_UNRATED_GAME_COUNT = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_UNRATED_GAME_COUNT = 19;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 977.

```text
 16;
  STATS_DAILY_TOURNAMENT_COUNT_PREVIOUS = 17;
  STATS_DAILY_TOURNAMENT_POINTS_PREVIOUS = 18;
  STATS_DAILY_UNRATED_GAME_COUNT = 19;
  STATS_DAILY_IN_PROGRESS_COUNT = 20;
  STATS_DAILY_TIMEOUT_COUNT = 21;
  STATS_DAILY_MOVES_PER_GAME = 22;
  STATS_DAILY_TOTAL_MOVE_TIME = 23;
  STATS_DAILY_TOTAL_MOVE_COUNT = 24;
  STATS_DAILY_LAST_GAME_DATE = 25;
  STATS_DAILY_CURRENT_STREAK = 26;
  STATS_DAILY_MAX_WIN_STREAK = 27
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11165"></a>
## FND-11165: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_IN_PROGRESS_COUNT = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_IN_PROGRESS_COUNT = 20;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 1016.

```text
VIOUS = 17;
  STATS_DAILY_TOURNAMENT_POINTS_PREVIOUS = 18;
  STATS_DAILY_UNRATED_GAME_COUNT = 19;
  STATS_DAILY_IN_PROGRESS_COUNT = 20;
  STATS_DAILY_TIMEOUT_COUNT = 21;
  STATS_DAILY_MOVES_PER_GAME = 22;
  STATS_DAILY_TOTAL_MOVE_TIME = 23;
  STATS_DAILY_TOTAL_MOVE_COUNT = 24;
  STATS_DAILY_LAST_GAME_DATE = 25;
  STATS_DAILY_CURRENT_STREAK = 26;
  STATS_DAILY_MAX_WIN_STREAK = 27;
  STATS_DAILY_MAX_LOSS_STREAK = 28;
 
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11166"></a>
## FND-11166: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TIMEOUT_COUNT = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TIMEOUT_COUNT = 21;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 1054.

```text
OINTS_PREVIOUS = 18;
  STATS_DAILY_UNRATED_GAME_COUNT = 19;
  STATS_DAILY_IN_PROGRESS_COUNT = 20;
  STATS_DAILY_TIMEOUT_COUNT = 21;
  STATS_DAILY_MOVES_PER_GAME = 22;
  STATS_DAILY_TOTAL_MOVE_TIME = 23;
  STATS_DAILY_TOTAL_MOVE_COUNT = 24;
  STATS_DAILY_LAST_GAME_DATE = 25;
  STATS_DAILY_CURRENT_STREAK = 26;
  STATS_DAILY_MAX_WIN_STREAK = 27;
  STATS_DAILY_MAX_LOSS_STREAK = 28;
  STATS_DAILY_RATING = 29;
  STATS_DAIL
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11167"></a>
## FND-11167: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_MOVES_PER_GAME = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_MOVES_PER_GAME = 22;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 1088.

```text
_UNRATED_GAME_COUNT = 19;
  STATS_DAILY_IN_PROGRESS_COUNT = 20;
  STATS_DAILY_TIMEOUT_COUNT = 21;
  STATS_DAILY_MOVES_PER_GAME = 22;
  STATS_DAILY_TOTAL_MOVE_TIME = 23;
  STATS_DAILY_TOTAL_MOVE_COUNT = 24;
  STATS_DAILY_LAST_GAME_DATE = 25;
  STATS_DAILY_CURRENT_STREAK = 26;
  STATS_DAILY_MAX_WIN_STREAK = 27;
  STATS_DAILY_MAX_LOSS_STREAK = 28;
  STATS_DAILY_RATING = 29;
  STATS_DAILY_RD = 30;
  STATS_DAILY_IS_ACTIVE
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11168"></a>
## FND-11168: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOTAL_MOVE_TIME = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOTAL_MOVE_TIME = 23;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 1123.

```text
AILY_IN_PROGRESS_COUNT = 20;
  STATS_DAILY_TIMEOUT_COUNT = 21;
  STATS_DAILY_MOVES_PER_GAME = 22;
  STATS_DAILY_TOTAL_MOVE_TIME = 23;
  STATS_DAILY_TOTAL_MOVE_COUNT = 24;
  STATS_DAILY_LAST_GAME_DATE = 25;
  STATS_DAILY_CURRENT_STREAK = 26;
  STATS_DAILY_MAX_WIN_STREAK = 27;
  STATS_DAILY_MAX_LOSS_STREAK = 28;
  STATS_DAILY_RATING = 29;
  STATS_DAILY_RD = 30;
  STATS_DAILY_IS_ACTIVE = 31;
  STATS_DAILY_TIMEOUT_PERCEN
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11169"></a>
## FND-11169: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_TOTAL_MOVE_COUNT = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_TOTAL_MOVE_COUNT = 24;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 1159.

```text
_DAILY_TIMEOUT_COUNT = 21;
  STATS_DAILY_MOVES_PER_GAME = 22;
  STATS_DAILY_TOTAL_MOVE_TIME = 23;
  STATS_DAILY_TOTAL_MOVE_COUNT = 24;
  STATS_DAILY_LAST_GAME_DATE = 25;
  STATS_DAILY_CURRENT_STREAK = 26;
  STATS_DAILY_MAX_WIN_STREAK = 27;
  STATS_DAILY_MAX_LOSS_STREAK = 28;
  STATS_DAILY_RATING = 29;
  STATS_DAILY_RD = 30;
  STATS_DAILY_IS_ACTIVE = 31;
  STATS_DAILY_TIMEOUT_PERCENT = 32;
  STATS_DAILY_AVG_TIME_PER_M
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11170"></a>
## FND-11170: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_LAST_GAME_DATE = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_LAST_GAME_DATE = 25;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 1196.

```text
ILY_MOVES_PER_GAME = 22;
  STATS_DAILY_TOTAL_MOVE_TIME = 23;
  STATS_DAILY_TOTAL_MOVE_COUNT = 24;
  STATS_DAILY_LAST_GAME_DATE = 25;
  STATS_DAILY_CURRENT_STREAK = 26;
  STATS_DAILY_MAX_WIN_STREAK = 27;
  STATS_DAILY_MAX_LOSS_STREAK = 28;
  STATS_DAILY_RATING = 29;
  STATS_DAILY_RD = 30;
  STATS_DAILY_IS_ACTIVE = 31;
  STATS_DAILY_TIMEOUT_PERCENT = 32;
  STATS_DAILY_AVG_TIME_PER_MOVE = 33;
  STATS_DAILY_IS_UNRATED = 
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11171"></a>
## FND-11171: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_CURRENT_STREAK = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_CURRENT_STREAK = 26;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 1231.

```text
ILY_TOTAL_MOVE_TIME = 23;
  STATS_DAILY_TOTAL_MOVE_COUNT = 24;
  STATS_DAILY_LAST_GAME_DATE = 25;
  STATS_DAILY_CURRENT_STREAK = 26;
  STATS_DAILY_MAX_WIN_STREAK = 27;
  STATS_DAILY_MAX_LOSS_STREAK = 28;
  STATS_DAILY_RATING = 29;
  STATS_DAILY_RD = 30;
  STATS_DAILY_IS_ACTIVE = 31;
  STATS_DAILY_TIMEOUT_PERCENT = 32;
  STATS_DAILY_AVG_TIME_PER_MOVE = 33;
  STATS_DAILY_IS_UNRATED = 34;
  STATS_DAILY_HIGHEST_RATING = 
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11172"></a>
## FND-11172: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_MAX_WIN_STREAK = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_MAX_WIN_STREAK = 27;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 1266.

```text
AILY_TOTAL_MOVE_COUNT = 24;
  STATS_DAILY_LAST_GAME_DATE = 25;
  STATS_DAILY_CURRENT_STREAK = 26;
  STATS_DAILY_MAX_WIN_STREAK = 27;
  STATS_DAILY_MAX_LOSS_STREAK = 28;
  STATS_DAILY_RATING = 29;
  STATS_DAILY_RD = 30;
  STATS_DAILY_IS_ACTIVE = 31;
  STATS_DAILY_TIMEOUT_PERCENT = 32;
  STATS_DAILY_AVG_TIME_PER_MOVE = 33;
  STATS_DAILY_IS_UNRATED = 34;
  STATS_DAILY_HIGHEST_RATING = 35;
  STATS_DAILY_HIGHEST_RATING_DA
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11173"></a>
## FND-11173: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_MAX_LOSS_STREAK = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_MAX_LOSS_STREAK = 28;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 1301.

```text
_DAILY_LAST_GAME_DATE = 25;
  STATS_DAILY_CURRENT_STREAK = 26;
  STATS_DAILY_MAX_WIN_STREAK = 27;
  STATS_DAILY_MAX_LOSS_STREAK = 28;
  STATS_DAILY_RATING = 29;
  STATS_DAILY_RD = 30;
  STATS_DAILY_IS_ACTIVE = 31;
  STATS_DAILY_TIMEOUT_PERCENT = 32;
  STATS_DAILY_AVG_TIME_PER_MOVE = 33;
  STATS_DAILY_IS_UNRATED = 34;
  STATS_DAILY_HIGHEST_RATING = 35;
  STATS_DAILY_HIGHEST_RATING_DATE = 36;
  STATS_DAILY_AVG_OPPONENT
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11174"></a>
## FND-11174: chesscom.user_properties.v1.StatsDailyPropertyDefinition.STATS_DAILY_RATING = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATS_DAILY_RATING = 29;

### Evidence

- **SRC-0630** `research/proto/chesscom/user_properties/v1/properties_stats_daily.proto` — [preserved redacted evidence](../evidence/text/bf96ae6e1e8fe77e52c24bdd08785e2eaa3d1bbffdc6d6457f7b3a6bb49a9953.proto)
  Character offset 1337.

```text
DAILY_CURRENT_STREAK = 26;
  STATS_DAILY_MAX_WIN_STREAK = 27;
  STATS_DAILY_MAX_LOSS_STREAK = 28;
  STATS_DAILY_RATING = 29;
  STATS_DAILY_RD = 30;
  STATS_DAILY_IS_ACTIVE = 31;
  STATS_DAILY_TIMEOUT_PERCENT = 32;
  STATS_DAILY_AVG_TIME_PER_MOVE = 33;
  STATS_DAILY_IS_UNRATED = 34;
  STATS_DAILY_HIGHEST_RATING = 35;
  STATS_DAILY_HIGHEST_RATING_DATE = 36;
  STATS_DAILY_AVG_OPPONENT_RATING = 37;
  STATS_DAILY_BEST_WIN
```

**Source references:** SRC-0630, SRC-1601  
**URL references:** None independently associated  
**Related findings:** FND-11144, FND-11145, FND-11146

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
