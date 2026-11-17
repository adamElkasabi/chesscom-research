# data_models — findings 10701–10800

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-10975"></a>
## FND-10975: chesscom.user_properties.v1.RatingsProperty.rating_best_type = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string rating_best_type = 20;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 2066.

```text
pid_rd = 18;
  }
  oneof _rating_best {
  int32 rating_best = 19;
  }
  oneof _rating_best_type {
  string rating_best_type = 20;
  }
}

```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10976"></a>
## FND-10976: enum declaration: chesscom.user_properties.v1.RolesPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum RolesPropertyDefinition {

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 119.

```text
/user_properties/v1/properties_roles.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum RolesPropertyDefinition {
  ROLES_PROPERTY_UNSPECIFIED = 0;
  IS_STREAMER = 1;
  ROLES = 2;
  ROLES_TRUST_LEVEL = 3;
  IS_AFFILIATE_ENABLED = 4;
}

message RolesProperty {
  oneof _is_streamer {
  bool is_streamer = 1;
  }
  oneof _trust_level {
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool i
```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10977, FND-10978

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10977"></a>
## FND-10977: chesscom.user_properties.v1.RolesPropertyDefinition.ROLES_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ROLES_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 152.

```text
les.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum RolesPropertyDefinition {
  ROLES_PROPERTY_UNSPECIFIED = 0;
  IS_STREAMER = 1;
  ROLES = 2;
  ROLES_TRUST_LEVEL = 3;
  IS_AFFILIATE_ENABLED = 4;
}

message RolesProperty {
  oneof _is_streamer {
  bool is_streamer = 1;
  }
  oneof _trust_level {
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool is_affiliate_enabled = 4;
  }
  re
```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10976, FND-10978

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10978"></a>
## FND-10978: chesscom.user_properties.v1.RolesPropertyDefinition.IS_STREAMER = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_STREAMER = 1;

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 186.

```text
ge chesscom.user_properties.v1;

enum RolesPropertyDefinition {
  ROLES_PROPERTY_UNSPECIFIED = 0;
  IS_STREAMER = 1;
  ROLES = 2;
  ROLES_TRUST_LEVEL = 3;
  IS_AFFILIATE_ENABLED = 4;
}

message RolesProperty {
  oneof _is_streamer {
  bool is_streamer = 1;
  }
  oneof _trust_level {
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool is_affiliate_enabled = 4;
  }
  repeated string roles = 2;
}

```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10976, FND-10977

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10979"></a>
## FND-10979: chesscom.user_properties.v1.RolesPropertyDefinition.ROLES = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ROLES = 2;

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 205.

```text
operties.v1;

enum RolesPropertyDefinition {
  ROLES_PROPERTY_UNSPECIFIED = 0;
  IS_STREAMER = 1;
  ROLES = 2;
  ROLES_TRUST_LEVEL = 3;
  IS_AFFILIATE_ENABLED = 4;
}

message RolesProperty {
  oneof _is_streamer {
  bool is_streamer = 1;
  }
  oneof _trust_level {
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool is_affiliate_enabled = 4;
  }
  repeated string roles = 2;
}

```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10976, FND-10977, FND-10978

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10980"></a>
## FND-10980: chesscom.user_properties.v1.RolesPropertyDefinition.ROLES_TRUST_LEVEL = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ROLES_TRUST_LEVEL = 3;

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 218.

```text

enum RolesPropertyDefinition {
  ROLES_PROPERTY_UNSPECIFIED = 0;
  IS_STREAMER = 1;
  ROLES = 2;
  ROLES_TRUST_LEVEL = 3;
  IS_AFFILIATE_ENABLED = 4;
}

message RolesProperty {
  oneof _is_streamer {
  bool is_streamer = 1;
  }
  oneof _trust_level {
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool is_affiliate_enabled = 4;
  }
  repeated string roles = 2;
}

```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10976, FND-10977, FND-10978

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10981"></a>
## FND-10981: chesscom.user_properties.v1.RolesPropertyDefinition.IS_AFFILIATE_ENABLED = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_AFFILIATE_ENABLED = 4;

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 243.

```text
tion {
  ROLES_PROPERTY_UNSPECIFIED = 0;
  IS_STREAMER = 1;
  ROLES = 2;
  ROLES_TRUST_LEVEL = 3;
  IS_AFFILIATE_ENABLED = 4;
}

message RolesProperty {
  oneof _is_streamer {
  bool is_streamer = 1;
  }
  oneof _trust_level {
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool is_affiliate_enabled = 4;
  }
  repeated string roles = 2;
}

```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10976, FND-10977, FND-10978

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10982"></a>
## FND-10982: message declaration: chesscom.user_properties.v1.RolesProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RolesProperty {

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 272.

```text
CIFIED = 0;
  IS_STREAMER = 1;
  ROLES = 2;
  ROLES_TRUST_LEVEL = 3;
  IS_AFFILIATE_ENABLED = 4;
}

message RolesProperty {
  oneof _is_streamer {
  bool is_streamer = 1;
  }
  oneof _trust_level {
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool is_affiliate_enabled = 4;
  }
  repeated string roles = 2;
}

```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10976, FND-10977, FND-10978

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10983"></a>
## FND-10983: oneof declaration: chesscom.user_properties.v1.RolesProperty._is_streamer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_streamer {

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 298.

```text
= 1;
  ROLES = 2;
  ROLES_TRUST_LEVEL = 3;
  IS_AFFILIATE_ENABLED = 4;
}

message RolesProperty {
  oneof _is_streamer {
  bool is_streamer = 1;
  }
  oneof _trust_level {
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool is_affiliate_enabled = 4;
  }
  repeated string roles = 2;
}

```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10976, FND-10977, FND-10978

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10984"></a>
## FND-10984: chesscom.user_properties.v1.RolesProperty.is_streamer = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_streamer = 1;

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 321.

```text
ES_TRUST_LEVEL = 3;
  IS_AFFILIATE_ENABLED = 4;
}

message RolesProperty {
  oneof _is_streamer {
  bool is_streamer = 1;
  }
  oneof _trust_level {
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool is_affiliate_enabled = 4;
  }
  repeated string roles = 2;
}

```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10976, FND-10977, FND-10978

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10985"></a>
## FND-10985: oneof declaration: chesscom.user_properties.v1.RolesProperty._trust_level

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _trust_level {

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 349.

```text
ILIATE_ENABLED = 4;
}

message RolesProperty {
  oneof _is_streamer {
  bool is_streamer = 1;
  }
  oneof _trust_level {
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool is_affiliate_enabled = 4;
  }
  repeated string roles = 2;
}

```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10976, FND-10977, FND-10978

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10986"></a>
## FND-10986: chesscom.user_properties.v1.RolesProperty.trust_level = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 trust_level = 3;

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 372.

```text
message RolesProperty {
  oneof _is_streamer {
  bool is_streamer = 1;
  }
  oneof _trust_level {
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool is_affiliate_enabled = 4;
  }
  repeated string roles = 2;
}

```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10976, FND-10977, FND-10978

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10987"></a>
## FND-10987: oneof declaration: chesscom.user_properties.v1.RolesProperty._is_affiliate_enabled

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_affiliate_enabled {

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 401.

```text
of _is_streamer {
  bool is_streamer = 1;
  }
  oneof _trust_level {
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool is_affiliate_enabled = 4;
  }
  repeated string roles = 2;
}

```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10976, FND-10977, FND-10978

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10988"></a>
## FND-10988: chesscom.user_properties.v1.RolesProperty.is_affiliate_enabled = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_affiliate_enabled = 4;

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 433.

```text
amer = 1;
  }
  oneof _trust_level {
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool is_affiliate_enabled = 4;
  }
  repeated string roles = 2;
}

```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10976, FND-10977, FND-10978

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10989"></a>
## FND-10989: chesscom.user_properties.v1.RolesProperty.roles = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string roles = 2;

### Evidence

- **SRC-0626** `research/proto/chesscom/user_properties/v1/properties_roles.proto` — [preserved redacted evidence](../evidence/text/72953c3a9a79677f858694b6e0c8e741fc33275cc7ecec4171ac5df41f196f48.proto)
  Character offset 470.

```text
  int32 trust_level = 3;
  }
  oneof _is_affiliate_enabled {
  bool is_affiliate_enabled = 4;
  }
  repeated string roles = 2;
}

```

**Source references:** SRC-0626, SRC-1597  
**URL references:** None independently associated  
**Related findings:** FND-10976, FND-10977, FND-10978

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10990"></a>
## FND-10990: enum declaration: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SettingsDailyChessPropertyDefinition {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 134.

```text
s/v1/properties_settings_daily_chess.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum SettingsDailyChessPropertyDefinition {
  DAILY_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  MAX_GAME_COUNT = 1;
  MIN_OPPONENT_RATING = 2;
  MAX_OPPONENT_RATING = 3;
  MIN_DAYS_PER_MOVE = 4;
  MAX_DAYS_PER_MOVE = 5;
  IS_FRIEND_EXEMPT = 6;
  IS_TOUCH_MOVE = 7;
  IS_NOT_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAM
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10991"></a>
## FND-10991: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.DAILY_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DAILY_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 180.

```text
syntax: proto3

package chesscom.user_properties.v1;

enum SettingsDailyChessPropertyDefinition {
  DAILY_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  MAX_GAME_COUNT = 1;
  MIN_OPPONENT_RATING = 2;
  MAX_OPPONENT_RATING = 3;
  MIN_DAYS_PER_MOVE = 4;
  MAX_DAYS_PER_MOVE = 5;
  IS_FRIEND_EXEMPT = 6;
  IS_TOUCH_MOVE = 7;
  IS_NOT_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10992"></a>
## FND-10992: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.MAX_GAME_COUNT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MAX_GAME_COUNT = 1;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 229.

```text
v1;

enum SettingsDailyChessPropertyDefinition {
  DAILY_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  MAX_GAME_COUNT = 1;
  MIN_OPPONENT_RATING = 2;
  MAX_OPPONENT_RATING = 3;
  MIN_DAYS_PER_MOVE = 4;
  MAX_DAYS_PER_MOVE = 5;
  IS_FRIEND_EXEMPT = 6;
  IS_TOUCH_MOVE = 7;
  IS_NOT_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10993"></a>
## FND-10993: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.MIN_OPPONENT_RATING = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MIN_OPPONENT_RATING = 2;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 251.

```text
yChessPropertyDefinition {
  DAILY_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  MAX_GAME_COUNT = 1;
  MIN_OPPONENT_RATING = 2;
  MAX_OPPONENT_RATING = 3;
  MIN_DAYS_PER_MOVE = 4;
  MAX_DAYS_PER_MOVE = 5;
  IS_FRIEND_EXEMPT = 6;
  IS_TOUCH_MOVE = 7;
  IS_NOT_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DAT
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10994"></a>
## FND-10994: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.MAX_OPPONENT_RATING = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MAX_OPPONENT_RATING = 3;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 278.

```text
  DAILY_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  MAX_GAME_COUNT = 1;
  MIN_OPPONENT_RATING = 2;
  MAX_OPPONENT_RATING = 3;
  MIN_DAYS_PER_MOVE = 4;
  MAX_DAYS_PER_MOVE = 5;
  IS_FRIEND_EXEMPT = 6;
  IS_TOUCH_MOVE = 7;
  IS_NOT_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTO
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10995"></a>
## FND-10995: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.MIN_DAYS_PER_MOVE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MIN_DAYS_PER_MOVE = 4;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 305.

```text
ERTY_UNSPECIFIED = 0;
  MAX_GAME_COUNT = 1;
  MIN_OPPONENT_RATING = 2;
  MAX_OPPONENT_RATING = 3;
  MIN_DAYS_PER_MOVE = 4;
  MAX_DAYS_PER_MOVE = 5;
  IS_FRIEND_EXEMPT = 6;
  IS_TOUCH_MOVE = 7;
  IS_NOT_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10996"></a>
## FND-10996: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.MAX_DAYS_PER_MOVE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MAX_DAYS_PER_MOVE = 5;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 330.

```text
AX_GAME_COUNT = 1;
  MIN_OPPONENT_RATING = 2;
  MAX_OPPONENT_RATING = 3;
  MIN_DAYS_PER_MOVE = 4;
  MAX_DAYS_PER_MOVE = 5;
  IS_FRIEND_EXEMPT = 6;
  IS_TOUCH_MOVE = 7;
  IS_NOT_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10997"></a>
## FND-10997: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.IS_FRIEND_EXEMPT = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_FRIEND_EXEMPT = 6;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 355.

```text
OPPONENT_RATING = 2;
  MAX_OPPONENT_RATING = 3;
  MIN_DAYS_PER_MOVE = 4;
  MAX_DAYS_PER_MOVE = 5;
  IS_FRIEND_EXEMPT = 6;
  IS_TOUCH_MOVE = 7;
  IS_NOT_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES =
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10998"></a>
## FND-10998: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.IS_TOUCH_MOVE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_TOUCH_MOVE = 7;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 379.

```text
AX_OPPONENT_RATING = 3;
  MIN_DAYS_PER_MOVE = 4;
  MAX_DAYS_PER_MOVE = 5;
  IS_FRIEND_EXEMPT = 6;
  IS_TOUCH_MOVE = 7;
  IS_NOT_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10999"></a>
## FND-10999: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.IS_NOT_AVAILABLE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_NOT_AVAILABLE = 8;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 400.

```text
3;
  MIN_DAYS_PER_MOVE = 4;
  MAX_DAYS_PER_MOVE = 5;
  IS_FRIEND_EXEMPT = 6;
  IS_TOUCH_MOVE = 7;
  IS_NOT_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 2
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11000"></a>
## FND-11000: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.GAME_PIECE_STYLE_ID = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PIECE_STYLE_ID = 9;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 424.

```text
 4;
  MAX_DAYS_PER_MOVE = 5;
  IS_FRIEND_EXEMPT = 6;
  IS_TOUCH_MOVE = 7;
  IS_NOT_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOV
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11001"></a>
## FND-11001: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.GAME_BOARD_COLOR_ID = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_BOARD_COLOR_ID = 10;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 451.

```text
;
  IS_FRIEND_EXEMPT = 6;
  IS_TOUCH_MOVE = 7;
  IS_NOT_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11002"></a>
## FND-11002: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.GAME_BOARD_SIZE_ID = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_BOARD_SIZE_ID = 11;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 479.

```text
IS_TOUCH_MOVE = 7;
  IS_NOT_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

m
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11003"></a>
## FND-11003: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.POST_MOVE_ACTION = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

POST_MOVE_ACTION = 12;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 506.

```text
_AVAILABLE = 8;
  GAME_PIECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessPr
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11004"></a>
## FND-11004: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.VACATION_TIME = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VACATION_TIME = 13;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 531.

```text
ECE_STYLE_ID = 9;
  GAME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_gam
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11005"></a>
## FND-11005: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.VACATION_LEAVE_DATE = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VACATION_LEAVE_DATE = 14;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 553.

```text
ME_BOARD_COLOR_ID = 10;
  GAME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11006"></a>
## FND-11006: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.IS_WHITE_ON_BOTTOM = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IS_WHITE_ON_BOTTOM = 15;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 581.

```text
ME_BOARD_SIZE_ID = 11;
  POST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11007"></a>
## FND-11007: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.SHOW_COORDINATES = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHOW_COORDINATES = 16;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 608.

```text
ST_MOVE_ACTION = 12;
  VACATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  in
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11008"></a>
## FND-11008: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.AUTO_WIN_ON_TIME = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

AUTO_WIN_ON_TIME = 17;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 633.

```text
CATION_TIME = 13;
  VACATION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  int32 min_opponent_rating =
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11009"></a>
## FND-11009: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.HIGHLIGHT_MOVES = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HIGHLIGHT_MOVES = 18;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 658.

```text
ION_LEAVE_DATE = 14;
  IS_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  int32 min_opponent_rating = 2;
  }
  oneof _max_oppo
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11010"></a>
## FND-11010: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.SOUNDS_ENABLED = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SOUNDS_ENABLED = 19;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 682.

```text
S_WHITE_ON_BOTTOM = 15;
  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  int32 min_opponent_rating = 2;
  }
  oneof _max_opponent_rating {
  int32 ma
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11011"></a>
## FND-11011: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.DEFAULT_TAB = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DEFAULT_TAB = 20;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 705.

```text

  SHOW_COORDINATES = 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  int32 min_opponent_rating = 2;
  }
  oneof _max_opponent_rating {
  int32 max_opponent_rating = 3;

```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11012"></a>
## FND-11012: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.SHARED_SOUND_ON_MOVE = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_SOUND_ON_MOVE = 21;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 725.

```text
= 16;
  AUTO_WIN_ON_TIME = 17;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  int32 min_opponent_rating = 2;
  }
  oneof _max_opponent_rating {
  int32 max_opponent_rating = 3;
  }
  oneof _min_day
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11013"></a>
## FND-11013: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.SHOW_LEGAL_MOVES = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHOW_LEGAL_MOVES = 22;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 754.

```text
;
  HIGHLIGHT_MOVES = 18;
  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  int32 min_opponent_rating = 2;
  }
  oneof _max_opponent_rating {
  int32 max_opponent_rating = 3;
  }
  oneof _min_days_per_move {
  int32 min_days
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11014"></a>
## FND-11014: chesscom.user_properties.v1.SettingsDailyChessPropertyDefinition.SOUNDS_ID = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SOUNDS_ID = 23;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 779.

```text

  SOUNDS_ENABLED = 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  int32 min_opponent_rating = 2;
  }
  oneof _max_opponent_rating {
  int32 max_opponent_rating = 3;
  }
  oneof _min_days_per_move {
  int32 min_days_per_move = 4;
  }
  oneo
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11015"></a>
## FND-11015: message declaration: chesscom.user_properties.v1.SettingsDailyChessProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SettingsDailyChessProperty {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 798.

```text
 19;
  DEFAULT_TAB = 20;
  SHARED_SOUND_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  int32 min_opponent_rating = 2;
  }
  oneof _max_opponent_rating {
  int32 max_opponent_rating = 3;
  }
  oneof _min_days_per_move {
  int32 min_days_per_move = 4;
  }
  oneof _max_days_per_mov
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11016"></a>
## FND-11016: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._max_game_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_game_count {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 837.

```text
_ON_MOVE = 21;
  SHOW_LEGAL_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  int32 min_opponent_rating = 2;
  }
  oneof _max_opponent_rating {
  int32 max_opponent_rating = 3;
  }
  oneof _min_days_per_move {
  int32 min_days_per_move = 4;
  }
  oneof _max_days_per_move {
  int32 max_days_per_move = 5;
  }

```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11017"></a>
## FND-11017: chesscom.user_properties.v1.SettingsDailyChessProperty.max_game_count = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max_game_count = 1;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 863.

```text
L_MOVES = 22;
  SOUNDS_ID = 23;
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  int32 min_opponent_rating = 2;
  }
  oneof _max_opponent_rating {
  int32 max_opponent_rating = 3;
  }
  oneof _min_days_per_move {
  int32 min_days_per_move = 4;
  }
  oneof _max_days_per_move {
  int32 max_days_per_move = 5;
  }
  oneof _is_friend_exempt 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11018"></a>
## FND-11018: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._min_opponent_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _min_opponent_rating {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 895.

```text
}

message SettingsDailyChessProperty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  int32 min_opponent_rating = 2;
  }
  oneof _max_opponent_rating {
  int32 max_opponent_rating = 3;
  }
  oneof _min_days_per_move {
  int32 min_days_per_move = 4;
  }
  oneof _max_days_per_move {
  int32 max_days_per_move = 5;
  }
  oneof _is_friend_exempt {
  bool is_friend_exempt = 6;
 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11019"></a>
## FND-11019: chesscom.user_properties.v1.SettingsDailyChessProperty.min_opponent_rating = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 min_opponent_rating = 2;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 926.

```text
operty {
  oneof _max_game_count {
  int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  int32 min_opponent_rating = 2;
  }
  oneof _max_opponent_rating {
  int32 max_opponent_rating = 3;
  }
  oneof _min_days_per_move {
  int32 min_days_per_move = 4;
  }
  oneof _max_days_per_move {
  int32 max_days_per_move = 5;
  }
  oneof _is_friend_exempt {
  bool is_friend_exempt = 6;
  }
  oneof _is_touch_move {
  b
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11020"></a>
## FND-11020: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._max_opponent_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_opponent_rating {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 963.

```text
int32 max_game_count = 1;
  }
  oneof _min_opponent_rating {
  int32 min_opponent_rating = 2;
  }
  oneof _max_opponent_rating {
  int32 max_opponent_rating = 3;
  }
  oneof _min_days_per_move {
  int32 min_days_per_move = 4;
  }
  oneof _max_days_per_move {
  int32 max_days_per_move = 5;
  }
  oneof _is_friend_exempt {
  bool is_friend_exempt = 6;
  }
  oneof _is_touch_move {
  bool is_touch_move = 7;
  }
  oneof _i
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11021"></a>
## FND-11021: chesscom.user_properties.v1.SettingsDailyChessProperty.max_opponent_rating = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max_opponent_rating = 3;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 994.

```text
 oneof _min_opponent_rating {
  int32 min_opponent_rating = 2;
  }
  oneof _max_opponent_rating {
  int32 max_opponent_rating = 3;
  }
  oneof _min_days_per_move {
  int32 min_days_per_move = 4;
  }
  oneof _max_days_per_move {
  int32 max_days_per_move = 5;
  }
  oneof _is_friend_exempt {
  bool is_friend_exempt = 6;
  }
  oneof _is_touch_move {
  bool is_touch_move = 7;
  }
  oneof _is_not_available {
  bool is_not
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11022"></a>
## FND-11022: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._min_days_per_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _min_days_per_move {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1031.

```text
 min_opponent_rating = 2;
  }
  oneof _max_opponent_rating {
  int32 max_opponent_rating = 3;
  }
  oneof _min_days_per_move {
  int32 min_days_per_move = 4;
  }
  oneof _max_days_per_move {
  int32 max_days_per_move = 5;
  }
  oneof _is_friend_exempt {
  bool is_friend_exempt = 6;
  }
  oneof _is_touch_move {
  bool is_touch_move = 7;
  }
  oneof _is_not_available {
  bool is_not_available = 8;
  }
  oneof _game_pie
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11023"></a>
## FND-11023: chesscom.user_properties.v1.SettingsDailyChessProperty.min_days_per_move = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 min_days_per_move = 4;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1060.

```text

  oneof _max_opponent_rating {
  int32 max_opponent_rating = 3;
  }
  oneof _min_days_per_move {
  int32 min_days_per_move = 4;
  }
  oneof _max_days_per_move {
  int32 max_days_per_move = 5;
  }
  oneof _is_friend_exempt {
  bool is_friend_exempt = 6;
  }
  oneof _is_touch_move {
  bool is_touch_move = 7;
  }
  oneof _is_not_available {
  bool is_not_available = 8;
  }
  oneof _game_piece_style_id {
  int32 game_pi
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11024"></a>
## FND-11024: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._max_days_per_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_days_per_move {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1095.

```text
nt32 max_opponent_rating = 3;
  }
  oneof _min_days_per_move {
  int32 min_days_per_move = 4;
  }
  oneof _max_days_per_move {
  int32 max_days_per_move = 5;
  }
  oneof _is_friend_exempt {
  bool is_friend_exempt = 6;
  }
  oneof _is_touch_move {
  bool is_touch_move = 7;
  }
  oneof _is_not_available {
  bool is_not_available = 8;
  }
  oneof _game_piece_style_id {
  int32 game_piece_style_id = 9;
  }
  oneof _game
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11025"></a>
## FND-11025: chesscom.user_properties.v1.SettingsDailyChessProperty.max_days_per_move = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max_days_per_move = 5;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1124.

```text

  }
  oneof _min_days_per_move {
  int32 min_days_per_move = 4;
  }
  oneof _max_days_per_move {
  int32 max_days_per_move = 5;
  }
  oneof _is_friend_exempt {
  bool is_friend_exempt = 6;
  }
  oneof _is_touch_move {
  bool is_touch_move = 7;
  }
  oneof _is_not_available {
  bool is_not_available = 8;
  }
  oneof _game_piece_style_id {
  int32 game_piece_style_id = 9;
  }
  oneof _game_board_color_id {
  int32 gam
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11026"></a>
## FND-11026: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._is_friend_exempt

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_friend_exempt {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1159.

```text
 int32 min_days_per_move = 4;
  }
  oneof _max_days_per_move {
  int32 max_days_per_move = 5;
  }
  oneof _is_friend_exempt {
  bool is_friend_exempt = 6;
  }
  oneof _is_touch_move {
  bool is_touch_move = 7;
  }
  oneof _is_not_available {
  bool is_not_available = 8;
  }
  oneof _game_piece_style_id {
  int32 game_piece_style_id = 9;
  }
  oneof _game_board_color_id {
  int32 game_board_color_id = 10;
  }
  oneof 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11027"></a>
## FND-11027: chesscom.user_properties.v1.SettingsDailyChessProperty.is_friend_exempt = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_friend_exempt = 6;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1187.

```text
;
  }
  oneof _max_days_per_move {
  int32 max_days_per_move = 5;
  }
  oneof _is_friend_exempt {
  bool is_friend_exempt = 6;
  }
  oneof _is_touch_move {
  bool is_touch_move = 7;
  }
  oneof _is_not_available {
  bool is_not_available = 8;
  }
  oneof _game_piece_style_id {
  int32 game_piece_style_id = 9;
  }
  oneof _game_board_color_id {
  int32 game_board_color_id = 10;
  }
  oneof _game_board_size_id {
  int3
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11028"></a>
## FND-11028: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._is_touch_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_touch_move {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1220.

```text
{
  int32 max_days_per_move = 5;
  }
  oneof _is_friend_exempt {
  bool is_friend_exempt = 6;
  }
  oneof _is_touch_move {
  bool is_touch_move = 7;
  }
  oneof _is_not_available {
  bool is_not_available = 8;
  }
  oneof _game_piece_style_id {
  int32 game_piece_style_id = 9;
  }
  oneof _game_board_color_id {
  int32 game_board_color_id = 10;
  }
  oneof _game_board_size_id {
  int32 game_board_size_id = 11;
  }
  
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11029"></a>
## FND-11029: chesscom.user_properties.v1.SettingsDailyChessProperty.is_touch_move = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_touch_move = 7;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1245.

```text
ve = 5;
  }
  oneof _is_friend_exempt {
  bool is_friend_exempt = 6;
  }
  oneof _is_touch_move {
  bool is_touch_move = 7;
  }
  oneof _is_not_available {
  bool is_not_available = 8;
  }
  oneof _game_piece_style_id {
  int32 game_piece_style_id = 9;
  }
  oneof _game_board_color_id {
  int32 game_board_color_id = 10;
  }
  oneof _game_board_size_id {
  int32 game_board_size_id = 11;
  }
  oneof _post_move_action {
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11030"></a>
## FND-11030: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._is_not_available

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_not_available {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1275.

```text
_exempt {
  bool is_friend_exempt = 6;
  }
  oneof _is_touch_move {
  bool is_touch_move = 7;
  }
  oneof _is_not_available {
  bool is_not_available = 8;
  }
  oneof _game_piece_style_id {
  int32 game_piece_style_id = 9;
  }
  oneof _game_board_color_id {
  int32 game_board_color_id = 10;
  }
  oneof _game_board_size_id {
  int32 game_board_size_id = 11;
  }
  oneof _post_move_action {
  string post_move_action = 1
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11031"></a>
## FND-11031: chesscom.user_properties.v1.SettingsDailyChessProperty.is_not_available = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_not_available = 8;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1303.

```text
xempt = 6;
  }
  oneof _is_touch_move {
  bool is_touch_move = 7;
  }
  oneof _is_not_available {
  bool is_not_available = 8;
  }
  oneof _game_piece_style_id {
  int32 game_piece_style_id = 9;
  }
  oneof _game_board_color_id {
  int32 game_board_color_id = 10;
  }
  oneof _game_board_size_id {
  int32 game_board_size_id = 11;
  }
  oneof _post_move_action {
  string post_move_action = 12;
  }
  oneof _vacation_tim
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11032"></a>
## FND-11032: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._game_piece_style_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_piece_style_id {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1336.

```text
move {
  bool is_touch_move = 7;
  }
  oneof _is_not_available {
  bool is_not_available = 8;
  }
  oneof _game_piece_style_id {
  int32 game_piece_style_id = 9;
  }
  oneof _game_board_color_id {
  int32 game_board_color_id = 10;
  }
  oneof _game_board_size_id {
  int32 game_board_size_id = 11;
  }
  oneof _post_move_action {
  string post_move_action = 12;
  }
  oneof _vacation_time {
  int32 vacation_time = 13;
 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11033"></a>
## FND-11033: chesscom.user_properties.v1.SettingsDailyChessProperty.game_piece_style_id = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 game_piece_style_id = 9;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1367.

```text
;
  }
  oneof _is_not_available {
  bool is_not_available = 8;
  }
  oneof _game_piece_style_id {
  int32 game_piece_style_id = 9;
  }
  oneof _game_board_color_id {
  int32 game_board_color_id = 10;
  }
  oneof _game_board_size_id {
  int32 game_board_size_id = 11;
  }
  oneof _post_move_action {
  string post_move_action = 12;
  }
  oneof _vacation_time {
  int32 vacation_time = 13;
  }
  oneof _vacation_leave_date
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11034"></a>
## FND-11034: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._game_board_color_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_board_color_id {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1404.

```text
ool is_not_available = 8;
  }
  oneof _game_piece_style_id {
  int32 game_piece_style_id = 9;
  }
  oneof _game_board_color_id {
  int32 game_board_color_id = 10;
  }
  oneof _game_board_size_id {
  int32 game_board_size_id = 11;
  }
  oneof _post_move_action {
  string post_move_action = 12;
  }
  oneof _vacation_time {
  int32 vacation_time = 13;
  }
  oneof _vacation_leave_date {
  .google.protobuf.Timestamp vacat
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11035"></a>
## FND-11035: chesscom.user_properties.v1.SettingsDailyChessProperty.game_board_color_id = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 game_board_color_id = 10;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1435.

```text
 oneof _game_piece_style_id {
  int32 game_piece_style_id = 9;
  }
  oneof _game_board_color_id {
  int32 game_board_color_id = 10;
  }
  oneof _game_board_size_id {
  int32 game_board_size_id = 11;
  }
  oneof _post_move_action {
  string post_move_action = 12;
  }
  oneof _vacation_time {
  int32 vacation_time = 13;
  }
  oneof _vacation_leave_date {
  .google.protobuf.Timestamp vacation_leave_date = 14;
  }
  oneo
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11036"></a>
## FND-11036: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._game_board_size_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_board_size_id {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1473.

```text
game_piece_style_id = 9;
  }
  oneof _game_board_color_id {
  int32 game_board_color_id = 10;
  }
  oneof _game_board_size_id {
  int32 game_board_size_id = 11;
  }
  oneof _post_move_action {
  string post_move_action = 12;
  }
  oneof _vacation_time {
  int32 vacation_time = 13;
  }
  oneof _vacation_leave_date {
  .google.protobuf.Timestamp vacation_leave_date = 14;
  }
  oneof _is_white_on_bottom {
  bool is_whit
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11037"></a>
## FND-11037: chesscom.user_properties.v1.SettingsDailyChessProperty.game_board_size_id = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 game_board_size_id = 11;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1503.

```text
 oneof _game_board_color_id {
  int32 game_board_color_id = 10;
  }
  oneof _game_board_size_id {
  int32 game_board_size_id = 11;
  }
  oneof _post_move_action {
  string post_move_action = 12;
  }
  oneof _vacation_time {
  int32 vacation_time = 13;
  }
  oneof _vacation_leave_date {
  .google.protobuf.Timestamp vacation_leave_date = 14;
  }
  oneof _is_white_on_bottom {
  bool is_white_on_bottom = 15;
  }
  oneof 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11038"></a>
## FND-11038: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._post_move_action

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _post_move_action {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1540.

```text
 game_board_color_id = 10;
  }
  oneof _game_board_size_id {
  int32 game_board_size_id = 11;
  }
  oneof _post_move_action {
  string post_move_action = 12;
  }
  oneof _vacation_time {
  int32 vacation_time = 13;
  }
  oneof _vacation_leave_date {
  .google.protobuf.Timestamp vacation_leave_date = 14;
  }
  oneof _is_white_on_bottom {
  bool is_white_on_bottom = 15;
  }
  oneof _show_coordinates {
  int32 show_coor
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11039"></a>
## FND-11039: chesscom.user_properties.v1.SettingsDailyChessProperty.post_move_action = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string post_move_action = 12;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1568.

```text
 }
  oneof _game_board_size_id {
  int32 game_board_size_id = 11;
  }
  oneof _post_move_action {
  string post_move_action = 12;
  }
  oneof _vacation_time {
  int32 vacation_time = 13;
  }
  oneof _vacation_leave_date {
  .google.protobuf.Timestamp vacation_leave_date = 14;
  }
  oneof _is_white_on_bottom {
  bool is_white_on_bottom = 15;
  }
  oneof _show_coordinates {
  int32 show_coordinates = 16;
  }
  oneof _a
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11040"></a>
## FND-11040: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._vacation_time

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _vacation_time {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1604.

```text
nt32 game_board_size_id = 11;
  }
  oneof _post_move_action {
  string post_move_action = 12;
  }
  oneof _vacation_time {
  int32 vacation_time = 13;
  }
  oneof _vacation_leave_date {
  .google.protobuf.Timestamp vacation_leave_date = 14;
  }
  oneof _is_white_on_bottom {
  bool is_white_on_bottom = 15;
  }
  oneof _show_coordinates {
  int32 show_coordinates = 16;
  }
  oneof _auto_win_on_time {
  bool auto_win_on
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11041"></a>
## FND-11041: chesscom.user_properties.v1.SettingsDailyChessProperty.vacation_time = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 vacation_time = 13;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1629.

```text
 11;
  }
  oneof _post_move_action {
  string post_move_action = 12;
  }
  oneof _vacation_time {
  int32 vacation_time = 13;
  }
  oneof _vacation_leave_date {
  .google.protobuf.Timestamp vacation_leave_date = 14;
  }
  oneof _is_white_on_bottom {
  bool is_white_on_bottom = 15;
  }
  oneof _show_coordinates {
  int32 show_coordinates = 16;
  }
  oneof _auto_win_on_time {
  bool auto_win_on_time = 17;
  }
  oneof _
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11042"></a>
## FND-11042: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._vacation_leave_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _vacation_leave_date {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1661.

```text
on {
  string post_move_action = 12;
  }
  oneof _vacation_time {
  int32 vacation_time = 13;
  }
  oneof _vacation_leave_date {
  .google.protobuf.Timestamp vacation_leave_date = 14;
  }
  oneof _is_white_on_bottom {
  bool is_white_on_bottom = 15;
  }
  oneof _show_coordinates {
  int32 show_coordinates = 16;
  }
  oneof _auto_win_on_time {
  bool auto_win_on_time = 17;
  }
  oneof _highlight_moves {
  bool highlig
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11043"></a>
## FND-11043: chesscom.user_properties.v1.SettingsDailyChessProperty.vacation_leave_date = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp vacation_leave_date = 14;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1692.

```text
= 12;
  }
  oneof _vacation_time {
  int32 vacation_time = 13;
  }
  oneof _vacation_leave_date {
  .google.protobuf.Timestamp vacation_leave_date = 14;
  }
  oneof _is_white_on_bottom {
  bool is_white_on_bottom = 15;
  }
  oneof _show_coordinates {
  int32 show_coordinates = 16;
  }
  oneof _auto_win_on_time {
  bool auto_win_on_time = 17;
  }
  oneof _highlight_moves {
  bool highlight_moves = 18;
  }
  oneof _sou
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11044"></a>
## FND-11044: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._is_white_on_bottom

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_white_on_bottom {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1751.

```text
13;
  }
  oneof _vacation_leave_date {
  .google.protobuf.Timestamp vacation_leave_date = 14;
  }
  oneof _is_white_on_bottom {
  bool is_white_on_bottom = 15;
  }
  oneof _show_coordinates {
  int32 show_coordinates = 16;
  }
  oneof _auto_win_on_time {
  bool auto_win_on_time = 17;
  }
  oneof _highlight_moves {
  bool highlight_moves = 18;
  }
  oneof _sounds_enabled {
  bool sounds_enabled = 19;
  }
  oneof _defa
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11045"></a>
## FND-11045: chesscom.user_properties.v1.SettingsDailyChessProperty.is_white_on_bottom = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_white_on_bottom = 15;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1781.

```text
e_date {
  .google.protobuf.Timestamp vacation_leave_date = 14;
  }
  oneof _is_white_on_bottom {
  bool is_white_on_bottom = 15;
  }
  oneof _show_coordinates {
  int32 show_coordinates = 16;
  }
  oneof _auto_win_on_time {
  bool auto_win_on_time = 17;
  }
  oneof _highlight_moves {
  bool highlight_moves = 18;
  }
  oneof _sounds_enabled {
  bool sounds_enabled = 19;
  }
  oneof _default_tab {
  int32 default_tab 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11046"></a>
## FND-11046: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._show_coordinates

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _show_coordinates {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1817.

```text
p vacation_leave_date = 14;
  }
  oneof _is_white_on_bottom {
  bool is_white_on_bottom = 15;
  }
  oneof _show_coordinates {
  int32 show_coordinates = 16;
  }
  oneof _auto_win_on_time {
  bool auto_win_on_time = 17;
  }
  oneof _highlight_moves {
  bool highlight_moves = 18;
  }
  oneof _sounds_enabled {
  bool sounds_enabled = 19;
  }
  oneof _default_tab {
  int32 default_tab = 20;
  }
  oneof _shared_sound_on_m
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11047"></a>
## FND-11047: chesscom.user_properties.v1.SettingsDailyChessProperty.show_coordinates = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 show_coordinates = 16;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1845.

```text
  }
  oneof _is_white_on_bottom {
  bool is_white_on_bottom = 15;
  }
  oneof _show_coordinates {
  int32 show_coordinates = 16;
  }
  oneof _auto_win_on_time {
  bool auto_win_on_time = 17;
  }
  oneof _highlight_moves {
  bool highlight_moves = 18;
  }
  oneof _sounds_enabled {
  bool sounds_enabled = 19;
  }
  oneof _default_tab {
  int32 default_tab = 20;
  }
  oneof _shared_sound_on_move {
  bool shared_sound_on
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11048"></a>
## FND-11048: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._auto_win_on_time

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _auto_win_on_time {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1880.

```text
 bool is_white_on_bottom = 15;
  }
  oneof _show_coordinates {
  int32 show_coordinates = 16;
  }
  oneof _auto_win_on_time {
  bool auto_win_on_time = 17;
  }
  oneof _highlight_moves {
  bool highlight_moves = 18;
  }
  oneof _sounds_enabled {
  bool sounds_enabled = 19;
  }
  oneof _default_tab {
  int32 default_tab = 20;
  }
  oneof _shared_sound_on_move {
  bool shared_sound_on_move = 21;
  }
  oneof _show_legal
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11049"></a>
## FND-11049: chesscom.user_properties.v1.SettingsDailyChessProperty.auto_win_on_time = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool auto_win_on_time = 17;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1908.

```text
5;
  }
  oneof _show_coordinates {
  int32 show_coordinates = 16;
  }
  oneof _auto_win_on_time {
  bool auto_win_on_time = 17;
  }
  oneof _highlight_moves {
  bool highlight_moves = 18;
  }
  oneof _sounds_enabled {
  bool sounds_enabled = 19;
  }
  oneof _default_tab {
  int32 default_tab = 20;
  }
  oneof _shared_sound_on_move {
  bool shared_sound_on_move = 21;
  }
  oneof _show_legal_moves {
  bool show_legal_m
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11050"></a>
## FND-11050: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._highlight_moves

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _highlight_moves {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1942.

```text

  int32 show_coordinates = 16;
  }
  oneof _auto_win_on_time {
  bool auto_win_on_time = 17;
  }
  oneof _highlight_moves {
  bool highlight_moves = 18;
  }
  oneof _sounds_enabled {
  bool sounds_enabled = 19;
  }
  oneof _default_tab {
  int32 default_tab = 20;
  }
  oneof _shared_sound_on_move {
  bool shared_sound_on_move = 21;
  }
  oneof _show_legal_moves {
  bool show_legal_moves = 22;
  }
  oneof _sounds_id 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11051"></a>
## FND-11051: chesscom.user_properties.v1.SettingsDailyChessProperty.highlight_moves = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool highlight_moves = 18;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 1969.

```text
 16;
  }
  oneof _auto_win_on_time {
  bool auto_win_on_time = 17;
  }
  oneof _highlight_moves {
  bool highlight_moves = 18;
  }
  oneof _sounds_enabled {
  bool sounds_enabled = 19;
  }
  oneof _default_tab {
  int32 default_tab = 20;
  }
  oneof _shared_sound_on_move {
  bool shared_sound_on_move = 21;
  }
  oneof _show_legal_moves {
  bool show_legal_moves = 22;
  }
  oneof _sounds_id {
  int32 sounds_id = 23;
 
```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11052"></a>
## FND-11052: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._sounds_enabled

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _sounds_enabled {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 2002.

```text
e {
  bool auto_win_on_time = 17;
  }
  oneof _highlight_moves {
  bool highlight_moves = 18;
  }
  oneof _sounds_enabled {
  bool sounds_enabled = 19;
  }
  oneof _default_tab {
  int32 default_tab = 20;
  }
  oneof _shared_sound_on_move {
  bool shared_sound_on_move = 21;
  }
  oneof _show_legal_moves {
  bool show_legal_moves = 22;
  }
  oneof _sounds_id {
  int32 sounds_id = 23;
  }
}

```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11053"></a>
## FND-11053: chesscom.user_properties.v1.SettingsDailyChessProperty.sounds_enabled = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool sounds_enabled = 19;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 2028.

```text
e = 17;
  }
  oneof _highlight_moves {
  bool highlight_moves = 18;
  }
  oneof _sounds_enabled {
  bool sounds_enabled = 19;
  }
  oneof _default_tab {
  int32 default_tab = 20;
  }
  oneof _shared_sound_on_move {
  bool shared_sound_on_move = 21;
  }
  oneof _show_legal_moves {
  bool show_legal_moves = 22;
  }
  oneof _sounds_id {
  int32 sounds_id = 23;
  }
}

```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11054"></a>
## FND-11054: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._default_tab

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _default_tab {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 2060.

```text
oves {
  bool highlight_moves = 18;
  }
  oneof _sounds_enabled {
  bool sounds_enabled = 19;
  }
  oneof _default_tab {
  int32 default_tab = 20;
  }
  oneof _shared_sound_on_move {
  bool shared_sound_on_move = 21;
  }
  oneof _show_legal_moves {
  bool show_legal_moves = 22;
  }
  oneof _sounds_id {
  int32 sounds_id = 23;
  }
}

```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11055"></a>
## FND-11055: chesscom.user_properties.v1.SettingsDailyChessProperty.default_tab = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 default_tab = 20;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 2083.

```text
_moves = 18;
  }
  oneof _sounds_enabled {
  bool sounds_enabled = 19;
  }
  oneof _default_tab {
  int32 default_tab = 20;
  }
  oneof _shared_sound_on_move {
  bool shared_sound_on_move = 21;
  }
  oneof _show_legal_moves {
  bool show_legal_moves = 22;
  }
  oneof _sounds_id {
  int32 sounds_id = 23;
  }
}

```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11056"></a>
## FND-11056: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._shared_sound_on_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _shared_sound_on_move {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 2113.

```text
ds_enabled {
  bool sounds_enabled = 19;
  }
  oneof _default_tab {
  int32 default_tab = 20;
  }
  oneof _shared_sound_on_move {
  bool shared_sound_on_move = 21;
  }
  oneof _show_legal_moves {
  bool show_legal_moves = 22;
  }
  oneof _sounds_id {
  int32 sounds_id = 23;
  }
}

```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11057"></a>
## FND-11057: chesscom.user_properties.v1.SettingsDailyChessProperty.shared_sound_on_move = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool shared_sound_on_move = 21;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 2145.

```text
ed = 19;
  }
  oneof _default_tab {
  int32 default_tab = 20;
  }
  oneof _shared_sound_on_move {
  bool shared_sound_on_move = 21;
  }
  oneof _show_legal_moves {
  bool show_legal_moves = 22;
  }
  oneof _sounds_id {
  int32 sounds_id = 23;
  }
}

```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11058"></a>
## FND-11058: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._show_legal_moves

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _show_legal_moves {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 2183.

```text
int32 default_tab = 20;
  }
  oneof _shared_sound_on_move {
  bool shared_sound_on_move = 21;
  }
  oneof _show_legal_moves {
  bool show_legal_moves = 22;
  }
  oneof _sounds_id {
  int32 sounds_id = 23;
  }
}

```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11059"></a>
## FND-11059: chesscom.user_properties.v1.SettingsDailyChessProperty.show_legal_moves = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool show_legal_moves = 22;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 2211.

```text
  oneof _shared_sound_on_move {
  bool shared_sound_on_move = 21;
  }
  oneof _show_legal_moves {
  bool show_legal_moves = 22;
  }
  oneof _sounds_id {
  int32 sounds_id = 23;
  }
}

```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11060"></a>
## FND-11060: oneof declaration: chesscom.user_properties.v1.SettingsDailyChessProperty._sounds_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _sounds_id {

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 2245.

```text
bool shared_sound_on_move = 21;
  }
  oneof _show_legal_moves {
  bool show_legal_moves = 22;
  }
  oneof _sounds_id {
  int32 sounds_id = 23;
  }
}

```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11061"></a>
## FND-11061: chesscom.user_properties.v1.SettingsDailyChessProperty.sounds_id = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 sounds_id = 23;

### Evidence

- **SRC-0627** `research/proto/chesscom/user_properties/v1/properties_settings_daily_chess.proto` — [preserved redacted evidence](../evidence/text/21f01e88ea7cbba76eb7af66103ac91267d9050bfb85a225e27a9c678222940c.proto)
  Character offset 2266.

```text
move = 21;
  }
  oneof _show_legal_moves {
  bool show_legal_moves = 22;
  }
  oneof _sounds_id {
  int32 sounds_id = 23;
  }
}

```

**Source references:** SRC-0627, SRC-1598  
**URL references:** None independently associated  
**Related findings:** FND-10990, FND-10991, FND-10992

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-11062"></a>
## FND-11062: enum declaration: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SettingsLiveChessPropertyDefinition {

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 133.

```text
es/v1/properties_settings_live_chess.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum SettingsLiveChessPropertyDefinition {
  LIVE_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  AUTO_QUEEN = 1;
  PLAY_MULTIPLE_GAMES = 2;
  SEEK_INCREMENT = 3;
  SEEK_RATED = 4;
  SEEK_FILTER_PREMIUM_ONLY = 5;
  PREMOVE_ENABLED = 6;
  SEEK_FILTER_RATED_ONLY = 7;
  ALLOW_CHAT_REQUEST_FROM = 8;
  AUTO_TOP = 9;
  FOCUS_MODE
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11063"></a>
## FND-11063: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.LIVE_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LIVE_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 178.

```text
 syntax: proto3

package chesscom.user_properties.v1;

enum SettingsLiveChessPropertyDefinition {
  LIVE_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  AUTO_QUEEN = 1;
  PLAY_MULTIPLE_GAMES = 2;
  SEEK_INCREMENT = 3;
  SEEK_RATED = 4;
  SEEK_FILTER_PREMIUM_ONLY = 5;
  PREMOVE_ENABLED = 6;
  SEEK_FILTER_RATED_ONLY = 7;
  ALLOW_CHAT_REQUEST_FROM = 8;
  AUTO_TOP = 9;
  FOCUS_MODE_ENABLED = 10;
  ALLOW_CHALLENGES_FROM = 11;

```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11064"></a>
## FND-11064: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.AUTO_QUEEN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

AUTO_QUEEN = 1;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 226.

```text
s.v1;

enum SettingsLiveChessPropertyDefinition {
  LIVE_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  AUTO_QUEEN = 1;
  PLAY_MULTIPLE_GAMES = 2;
  SEEK_INCREMENT = 3;
  SEEK_RATED = 4;
  SEEK_FILTER_PREMIUM_ONLY = 5;
  PREMOVE_ENABLED = 6;
  SEEK_FILTER_RATED_ONLY = 7;
  ALLOW_CHAT_REQUEST_FROM = 8;
  AUTO_TOP = 9;
  FOCUS_MODE_ENABLED = 10;
  ALLOW_CHALLENGES_FROM = 11;
  SEEK_BASE_TIME = 12;
  SEEK_MIN_RATING = 13;
 
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11065"></a>
## FND-11065: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.PLAY_MULTIPLE_GAMES = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAY_MULTIPLE_GAMES = 2;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 244.

```text
gsLiveChessPropertyDefinition {
  LIVE_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  AUTO_QUEEN = 1;
  PLAY_MULTIPLE_GAMES = 2;
  SEEK_INCREMENT = 3;
  SEEK_RATED = 4;
  SEEK_FILTER_PREMIUM_ONLY = 5;
  PREMOVE_ENABLED = 6;
  SEEK_FILTER_RATED_ONLY = 7;
  ALLOW_CHAT_REQUEST_FROM = 8;
  AUTO_TOP = 9;
  FOCUS_MODE_ENABLED = 10;
  ALLOW_CHALLENGES_FROM = 11;
  SEEK_BASE_TIME = 12;
  SEEK_MIN_RATING = 13;
  SEEK_MAX_RATING =
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11066"></a>
## FND-11066: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.SEEK_INCREMENT = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEEK_INCREMENT = 3;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 271.

```text
on {
  LIVE_CHESS_SETTINGS_PROPERTY_UNSPECIFIED = 0;
  AUTO_QUEEN = 1;
  PLAY_MULTIPLE_GAMES = 2;
  SEEK_INCREMENT = 3;
  SEEK_RATED = 4;
  SEEK_FILTER_PREMIUM_ONLY = 5;
  PREMOVE_ENABLED = 6;
  SEEK_FILTER_RATED_ONLY = 7;
  ALLOW_CHAT_REQUEST_FROM = 8;
  AUTO_TOP = 9;
  FOCUS_MODE_ENABLED = 10;
  ALLOW_CHALLENGES_FROM = 11;
  SEEK_BASE_TIME = 12;
  SEEK_MIN_RATING = 13;
  SEEK_MAX_RATING = 14;
  CHALLENGE_POPUP_ALER
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11067"></a>
## FND-11067: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.SEEK_RATED = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEEK_RATED = 4;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 293.

```text
INGS_PROPERTY_UNSPECIFIED = 0;
  AUTO_QUEEN = 1;
  PLAY_MULTIPLE_GAMES = 2;
  SEEK_INCREMENT = 3;
  SEEK_RATED = 4;
  SEEK_FILTER_PREMIUM_ONLY = 5;
  PREMOVE_ENABLED = 6;
  SEEK_FILTER_RATED_ONLY = 7;
  ALLOW_CHAT_REQUEST_FROM = 8;
  AUTO_TOP = 9;
  FOCUS_MODE_ENABLED = 10;
  ALLOW_CHALLENGES_FROM = 11;
  SEEK_BASE_TIME = 12;
  SEEK_MIN_RATING = 13;
  SEEK_MAX_RATING = 14;
  CHALLENGE_POPUP_ALERT = 15;
  FRIEND_POPUP
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11068"></a>
## FND-11068: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.SEEK_FILTER_PREMIUM_ONLY = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEEK_FILTER_PREMIUM_ONLY = 5;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 311.

```text
ECIFIED = 0;
  AUTO_QUEEN = 1;
  PLAY_MULTIPLE_GAMES = 2;
  SEEK_INCREMENT = 3;
  SEEK_RATED = 4;
  SEEK_FILTER_PREMIUM_ONLY = 5;
  PREMOVE_ENABLED = 6;
  SEEK_FILTER_RATED_ONLY = 7;
  ALLOW_CHAT_REQUEST_FROM = 8;
  AUTO_TOP = 9;
  FOCUS_MODE_ENABLED = 10;
  ALLOW_CHALLENGES_FROM = 11;
  SEEK_BASE_TIME = 12;
  SEEK_MIN_RATING = 13;
  SEEK_MAX_RATING = 14;
  CHALLENGE_POPUP_ALERT = 15;
  FRIEND_POPUP_ALERT = 16;
  EVE
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11069"></a>
## FND-11069: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.PREMOVE_ENABLED = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMOVE_ENABLED = 6;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 343.

```text
 PLAY_MULTIPLE_GAMES = 2;
  SEEK_INCREMENT = 3;
  SEEK_RATED = 4;
  SEEK_FILTER_PREMIUM_ONLY = 5;
  PREMOVE_ENABLED = 6;
  SEEK_FILTER_RATED_ONLY = 7;
  ALLOW_CHAT_REQUEST_FROM = 8;
  AUTO_TOP = 9;
  FOCUS_MODE_ENABLED = 10;
  ALLOW_CHALLENGES_FROM = 11;
  SEEK_BASE_TIME = 12;
  SEEK_MIN_RATING = 13;
  SEEK_MAX_RATING = 14;
  CHALLENGE_POPUP_ALERT = 15;
  FRIEND_POPUP_ALERT = 16;
  EVENT_ANNOUNCEMENT = 17;
  CHALLENG
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11070"></a>
## FND-11070: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.SEEK_FILTER_RATED_ONLY = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEEK_FILTER_RATED_ONLY = 7;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 366.

```text
2;
  SEEK_INCREMENT = 3;
  SEEK_RATED = 4;
  SEEK_FILTER_PREMIUM_ONLY = 5;
  PREMOVE_ENABLED = 6;
  SEEK_FILTER_RATED_ONLY = 7;
  ALLOW_CHAT_REQUEST_FROM = 8;
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
  CH
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11071"></a>
## FND-11071: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.ALLOW_CHAT_REQUEST_FROM = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ALLOW_CHAT_REQUEST_FROM = 8;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 396.

```text
K_RATED = 4;
  SEEK_FILTER_PREMIUM_ONLY = 5;
  PREMOVE_ENABLED = 6;
  SEEK_FILTER_RATED_ONLY = 7;
  ALLOW_CHAT_REQUEST_FROM = 8;
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
  SEE
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11072"></a>
## FND-11072: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.AUTO_TOP = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

AUTO_TOP = 9;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 427.

```text
IUM_ONLY = 5;
  PREMOVE_ENABLED = 6;
  SEEK_FILTER_RATED_ONLY = 7;
  ALLOW_CHAT_REQUEST_FROM = 8;
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
  SE
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11073"></a>
## FND-11073: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.FOCUS_MODE_ENABLED = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FOCUS_MODE_ENABLED = 10;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 443.

```text
PREMOVE_ENABLED = 6;
  SEEK_FILTER_RATED_ONLY = 7;
  ALLOW_CHAT_REQUEST_FROM = 8;
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
  SEEK_INCREMENT_VAR
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-11074"></a>
## FND-11074: chesscom.user_properties.v1.SettingsLiveChessPropertyDefinition.ALLOW_CHALLENGES_FROM = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ALLOW_CHALLENGES_FROM = 11;

### Evidence

- **SRC-0628** `research/proto/chesscom/user_properties/v1/properties_settings_live_chess.proto` — [preserved redacted evidence](../evidence/text/072d2c8cbfcec2fd0a95dab7adf91a132e263422ef64f2604caf9b427f40f459.proto)
  Character offset 470.

```text
_FILTER_RATED_ONLY = 7;
  ALLOW_CHAT_REQUEST_FROM = 8;
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
  SEEK_BASE_TIM
```

**Source references:** SRC-0628, SRC-1599  
**URL references:** None independently associated  
**Related findings:** FND-11062, FND-11063, FND-11064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
