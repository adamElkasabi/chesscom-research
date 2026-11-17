# data_models — findings 12201–12300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-12475"></a>
## FND-12475: oneof declaration: chesscom.user_properties.v1.WDLProperty._total_rated_games_chess_bullet

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_rated_games_chess_bullet {

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 4372.

```text
 39;
  }
  oneof _total_rated_games_chess_daily {
  int32 total_rated_games_chess_daily = 40;
  }
  oneof _total_rated_games_chess_bullet {
  int32 total_rated_games_chess_bullet = 41;
  }
  oneof _total_rated_games_chess_blitz {
  int32 total_rated_games_chess_blitz = 42;
  }
  oneof _total_rated_games_chess_rapid {
  int32 total_rated_games_chess_rapid = 43;
  }
  oneof _total_rated_games {
  int32 total_rated_game
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12476"></a>
## FND-12476: chesscom.user_properties.v1.WDLProperty.total_rated_games_chess_bullet = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_rated_games_chess_bullet = 41;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 4414.

```text
daily {
  int32 total_rated_games_chess_daily = 40;
  }
  oneof _total_rated_games_chess_bullet {
  int32 total_rated_games_chess_bullet = 41;
  }
  oneof _total_rated_games_chess_blitz {
  int32 total_rated_games_chess_blitz = 42;
  }
  oneof _total_rated_games_chess_rapid {
  int32 total_rated_games_chess_rapid = 43;
  }
  oneof _total_rated_games {
  int32 total_rated_games = 44;
  }
  oneof _total_unrated_games {
```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12477"></a>
## FND-12477: oneof declaration: chesscom.user_properties.v1.WDLProperty._total_rated_games_chess_blitz

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_rated_games_chess_blitz {

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 4463.

```text
0;
  }
  oneof _total_rated_games_chess_bullet {
  int32 total_rated_games_chess_bullet = 41;
  }
  oneof _total_rated_games_chess_blitz {
  int32 total_rated_games_chess_blitz = 42;
  }
  oneof _total_rated_games_chess_rapid {
  int32 total_rated_games_chess_rapid = 43;
  }
  oneof _total_rated_games {
  int32 total_rated_games = 44;
  }
  oneof _total_unrated_games {
  int32 total_unrated_games = 45;
  }
}

```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12478"></a>
## FND-12478: chesscom.user_properties.v1.WDLProperty.total_rated_games_chess_blitz = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_rated_games_chess_blitz = 42;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 4504.

```text
ullet {
  int32 total_rated_games_chess_bullet = 41;
  }
  oneof _total_rated_games_chess_blitz {
  int32 total_rated_games_chess_blitz = 42;
  }
  oneof _total_rated_games_chess_rapid {
  int32 total_rated_games_chess_rapid = 43;
  }
  oneof _total_rated_games {
  int32 total_rated_games = 44;
  }
  oneof _total_unrated_games {
  int32 total_unrated_games = 45;
  }
}

```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12479"></a>
## FND-12479: oneof declaration: chesscom.user_properties.v1.WDLProperty._total_rated_games_chess_rapid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_rated_games_chess_rapid {

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 4552.

```text
 41;
  }
  oneof _total_rated_games_chess_blitz {
  int32 total_rated_games_chess_blitz = 42;
  }
  oneof _total_rated_games_chess_rapid {
  int32 total_rated_games_chess_rapid = 43;
  }
  oneof _total_rated_games {
  int32 total_rated_games = 44;
  }
  oneof _total_unrated_games {
  int32 total_unrated_games = 45;
  }
}

```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12480"></a>
## FND-12480: chesscom.user_properties.v1.WDLProperty.total_rated_games_chess_rapid = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_rated_games_chess_rapid = 43;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 4593.

```text
_blitz {
  int32 total_rated_games_chess_blitz = 42;
  }
  oneof _total_rated_games_chess_rapid {
  int32 total_rated_games_chess_rapid = 43;
  }
  oneof _total_rated_games {
  int32 total_rated_games = 44;
  }
  oneof _total_unrated_games {
  int32 total_unrated_games = 45;
  }
}

```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12481"></a>
## FND-12481: oneof declaration: chesscom.user_properties.v1.WDLProperty._total_rated_games

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_rated_games {

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 4641.

```text
 42;
  }
  oneof _total_rated_games_chess_rapid {
  int32 total_rated_games_chess_rapid = 43;
  }
  oneof _total_rated_games {
  int32 total_rated_games = 44;
  }
  oneof _total_unrated_games {
  int32 total_unrated_games = 45;
  }
}

```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12482"></a>
## FND-12482: chesscom.user_properties.v1.WDLProperty.total_rated_games = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_rated_games = 44;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 4670.

```text
_games_chess_rapid {
  int32 total_rated_games_chess_rapid = 43;
  }
  oneof _total_rated_games {
  int32 total_rated_games = 44;
  }
  oneof _total_unrated_games {
  int32 total_unrated_games = 45;
  }
}

```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12483"></a>
## FND-12483: oneof declaration: chesscom.user_properties.v1.WDLProperty._total_unrated_games

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_unrated_games {

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 4706.

```text
ated_games_chess_rapid = 43;
  }
  oneof _total_rated_games {
  int32 total_rated_games = 44;
  }
  oneof _total_unrated_games {
  int32 total_unrated_games = 45;
  }
}

```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12484"></a>
## FND-12484: chesscom.user_properties.v1.WDLProperty.total_unrated_games = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_unrated_games = 45;

### Evidence

- **SRC-0645** `research/proto/chesscom/user_properties/v1/properties_wdl.proto` — [preserved redacted evidence](../evidence/text/ebb017cd5ceb10c56d033a28b093e6cab75dee5b52576c838c41b38fbb6446f3.proto)
  Character offset 4737.

```text
}
  oneof _total_rated_games {
  int32 total_rated_games = 44;
  }
  oneof _total_unrated_games {
  int32 total_unrated_games = 45;
  }
}

```

**Source references:** SRC-0645, SRC-1616  
**URL references:** None independently associated  
**Related findings:** FND-12347, FND-12348, FND-12349

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12485"></a>
## FND-12485: enum declaration: chesscom.user_properties.v1.WidgetsPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum WidgetsPropertyDefinition {

### Evidence

- **SRC-0646** `research/proto/chesscom/user_properties/v1/properties_widgets.proto` — [preserved redacted evidence](../evidence/text/df433be187454b21e61bff09f0e69d4539c8be15435a53280688986b5f5e5c87.proto)
  Character offset 121.

```text
ser_properties/v1/properties_widgets.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum WidgetsPropertyDefinition {
  WIDGETS_PROPERTY_UNSPECIFIED = 0;
  CURRENT_WIDGETS = 1;
  USED_WIDGETS = 2;
}

message WidgetsProperty {
  repeated string current_widgets = 1;
  repeated string used_widgets = 2;
}

```

**Source references:** SRC-0646, SRC-1617  
**URL references:** None independently associated  
**Related findings:** FND-12486, FND-12487

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12486"></a>
## FND-12486: chesscom.user_properties.v1.WidgetsPropertyDefinition.WIDGETS_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

WIDGETS_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0646** `research/proto/chesscom/user_properties/v1/properties_widgets.proto` — [preserved redacted evidence](../evidence/text/df433be187454b21e61bff09f0e69d4539c8be15435a53280688986b5f5e5c87.proto)
  Character offset 156.

```text
s.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum WidgetsPropertyDefinition {
  WIDGETS_PROPERTY_UNSPECIFIED = 0;
  CURRENT_WIDGETS = 1;
  USED_WIDGETS = 2;
}

message WidgetsProperty {
  repeated string current_widgets = 1;
  repeated string used_widgets = 2;
}

```

**Source references:** SRC-0646, SRC-1617  
**URL references:** None independently associated  
**Related findings:** FND-12485, FND-12487

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12487"></a>
## FND-12487: chesscom.user_properties.v1.WidgetsPropertyDefinition.CURRENT_WIDGETS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CURRENT_WIDGETS = 1;

### Evidence

- **SRC-0646** `research/proto/chesscom/user_properties/v1/properties_widgets.proto` — [preserved redacted evidence](../evidence/text/df433be187454b21e61bff09f0e69d4539c8be15435a53280688986b5f5e5c87.proto)
  Character offset 192.

```text
hesscom.user_properties.v1;

enum WidgetsPropertyDefinition {
  WIDGETS_PROPERTY_UNSPECIFIED = 0;
  CURRENT_WIDGETS = 1;
  USED_WIDGETS = 2;
}

message WidgetsProperty {
  repeated string current_widgets = 1;
  repeated string used_widgets = 2;
}

```

**Source references:** SRC-0646, SRC-1617  
**URL references:** None independently associated  
**Related findings:** FND-12485, FND-12486

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12488"></a>
## FND-12488: chesscom.user_properties.v1.WidgetsPropertyDefinition.USED_WIDGETS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USED_WIDGETS = 2;

### Evidence

- **SRC-0646** `research/proto/chesscom/user_properties/v1/properties_widgets.proto` — [preserved redacted evidence](../evidence/text/df433be187454b21e61bff09f0e69d4539c8be15435a53280688986b5f5e5c87.proto)
  Character offset 215.

```text
.v1;

enum WidgetsPropertyDefinition {
  WIDGETS_PROPERTY_UNSPECIFIED = 0;
  CURRENT_WIDGETS = 1;
  USED_WIDGETS = 2;
}

message WidgetsProperty {
  repeated string current_widgets = 1;
  repeated string used_widgets = 2;
}

```

**Source references:** SRC-0646, SRC-1617  
**URL references:** None independently associated  
**Related findings:** FND-12485, FND-12486, FND-12487

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12489"></a>
## FND-12489: message declaration: chesscom.user_properties.v1.WidgetsProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message WidgetsProperty {

### Evidence

- **SRC-0646** `research/proto/chesscom/user_properties/v1/properties_widgets.proto` — [preserved redacted evidence](../evidence/text/df433be187454b21e61bff09f0e69d4539c8be15435a53280688986b5f5e5c87.proto)
  Character offset 236.

```text
pertyDefinition {
  WIDGETS_PROPERTY_UNSPECIFIED = 0;
  CURRENT_WIDGETS = 1;
  USED_WIDGETS = 2;
}

message WidgetsProperty {
  repeated string current_widgets = 1;
  repeated string used_widgets = 2;
}

```

**Source references:** SRC-0646, SRC-1617  
**URL references:** None independently associated  
**Related findings:** FND-12485, FND-12486, FND-12487

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12490"></a>
## FND-12490: chesscom.user_properties.v1.WidgetsProperty.current_widgets = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string current_widgets = 1;

### Evidence

- **SRC-0646** `research/proto/chesscom/user_properties/v1/properties_widgets.proto` — [preserved redacted evidence](../evidence/text/df433be187454b21e61bff09f0e69d4539c8be15435a53280688986b5f5e5c87.proto)
  Character offset 264.

```text
PROPERTY_UNSPECIFIED = 0;
  CURRENT_WIDGETS = 1;
  USED_WIDGETS = 2;
}

message WidgetsProperty {
  repeated string current_widgets = 1;
  repeated string used_widgets = 2;
}

```

**Source references:** SRC-0646, SRC-1617  
**URL references:** None independently associated  
**Related findings:** FND-12485, FND-12486, FND-12487

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12491"></a>
## FND-12491: chesscom.user_properties.v1.WidgetsProperty.used_widgets = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string used_widgets = 2;

### Evidence

- **SRC-0646** `research/proto/chesscom/user_properties/v1/properties_widgets.proto` — [preserved redacted evidence](../evidence/text/df433be187454b21e61bff09f0e69d4539c8be15435a53280688986b5f5e5c87.proto)
  Character offset 303.

```text
GETS = 1;
  USED_WIDGETS = 2;
}

message WidgetsProperty {
  repeated string current_widgets = 1;
  repeated string used_widgets = 2;
}

```

**Source references:** SRC-0646, SRC-1617  
**URL references:** None independently associated  
**Related findings:** FND-12485, FND-12486, FND-12487

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12492"></a>
## FND-12492: message declaration: chesscom.user_relationships.v2.ListableUserRelationship

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListableUserRelationship {

### Evidence

- **SRC-0647** `research/proto/chesscom/user_relationships/v2/list_user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/3625d965c1861d7b76ee7b2a00db7f6eabe22af311d284e164e3613e53732c4c.proto)
  Character offset 138.

```text
/v2/list_user_relationships_model.proto
// syntax: proto3

package chesscom.user_relationships.v2;

message ListableUserRelationship {
  optional string user_uuid = 1;
  optional .google.protobuf.Timestamp created_at = 2;
  optional .chesscom.user_relationships.v2.UserRelationshipType user_relationship = 3;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 4;
}

```

**Source references:** SRC-0647, SRC-1618  
**URL references:** None independently associated  
**Related findings:** FND-12493, FND-12494

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12493"></a>
## FND-12493: chesscom.user_relationships.v2.ListableUserRelationship.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0647** `research/proto/chesscom/user_relationships/v2/list_user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/3625d965c1861d7b76ee7b2a00db7f6eabe22af311d284e164e3613e53732c4c.proto)
  Character offset 175.

```text
to
// syntax: proto3

package chesscom.user_relationships.v2;

message ListableUserRelationship {
  optional string user_uuid = 1;
  optional .google.protobuf.Timestamp created_at = 2;
  optional .chesscom.user_relationships.v2.UserRelationshipType user_relationship = 3;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 4;
}

```

**Source references:** SRC-0647, SRC-1618  
**URL references:** None independently associated  
**Related findings:** FND-12492, FND-12494

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12494"></a>
## FND-12494: chesscom.user_relationships.v2.ListableUserRelationship.created_at = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp created_at = 2;

### Evidence

- **SRC-0647** `research/proto/chesscom/user_relationships/v2/list_user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/3625d965c1861d7b76ee7b2a00db7f6eabe22af311d284e164e3613e53732c4c.proto)
  Character offset 208.

```text
sscom.user_relationships.v2;

message ListableUserRelationship {
  optional string user_uuid = 1;
  optional .google.protobuf.Timestamp created_at = 2;
  optional .chesscom.user_relationships.v2.UserRelationshipType user_relationship = 3;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 4;
}

```

**Source references:** SRC-0647, SRC-1618  
**URL references:** None independently associated  
**Related findings:** FND-12492, FND-12493

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12495"></a>
## FND-12495: chesscom.user_relationships.v2.ListableUserRelationship.user_relationship = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_relationships.v2.UserRelationshipType user_relationship = 3;

### Evidence

- **SRC-0647** `research/proto/chesscom/user_relationships/v2/list_user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/3625d965c1861d7b76ee7b2a00db7f6eabe22af311d284e164e3613e53732c4c.proto)
  Character offset 262.

```text
tionship {
  optional string user_uuid = 1;
  optional .google.protobuf.Timestamp created_at = 2;
  optional .chesscom.user_relationships.v2.UserRelationshipType user_relationship = 3;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 4;
}

```

**Source references:** SRC-0647, SRC-1618  
**URL references:** None independently associated  
**Related findings:** FND-12492, FND-12493, FND-12494

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12496"></a>
## FND-12496: chesscom.user_relationships.v2.ListableUserRelationship.direction = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 4;

### Evidence

- **SRC-0647** `research/proto/chesscom/user_relationships/v2/list_user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/3625d965c1861d7b76ee7b2a00db7f6eabe22af311d284e164e3613e53732c4c.proto)
  Character offset 349.

```text
ed_at = 2;
  optional .chesscom.user_relationships.v2.UserRelationshipType user_relationship = 3;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 4;
}

```

**Source references:** SRC-0647, SRC-1618  
**URL references:** None independently associated  
**Related findings:** FND-12492, FND-12493, FND-12494

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12497"></a>
## FND-12497: enum declaration: chesscom.user_relationships.v2.UserRelationshipDirection

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum UserRelationshipDirection {

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 133.

```text
ships/v2/user_relationships_model.proto
// syntax: proto3

package chesscom.user_relationships.v2;

enum UserRelationshipDirection {
  USER_RELATIONSHIP_DIRECTION_UNSPECIFIED = 0;
  USER_RELATIONSHIP_DIRECTION_INCOMING = 1;
  USER_RELATIONSHIP_DIRECTION_OUTGOING = 2;
  USER_RELATIONSHIP_DIRECTION_MUTUAL = 3;
}

enum UserRelationshipType {
  USER_RELATIONSHIP_TYPE_UNSPECIFIED = 0;
  USER_RELATIONSHIP_TYPE_FRIENDSHIP =
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12498, FND-12499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12498"></a>
## FND-12498: chesscom.user_relationships.v2.UserRelationshipDirection.USER_RELATIONSHIP_DIRECTION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_RELATIONSHIP_DIRECTION_UNSPECIFIED = 0;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 168.

```text
roto
// syntax: proto3

package chesscom.user_relationships.v2;

enum UserRelationshipDirection {
  USER_RELATIONSHIP_DIRECTION_UNSPECIFIED = 0;
  USER_RELATIONSHIP_DIRECTION_INCOMING = 1;
  USER_RELATIONSHIP_DIRECTION_OUTGOING = 2;
  USER_RELATIONSHIP_DIRECTION_MUTUAL = 3;
}

enum UserRelationshipType {
  USER_RELATIONSHIP_TYPE_UNSPECIFIED = 0;
  USER_RELATIONSHIP_TYPE_FRIENDSHIP = 1;
  USER_RELATIONSHIP_TYPE_BLOCK 
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12499"></a>
## FND-12499: chesscom.user_relationships.v2.UserRelationshipDirection.USER_RELATIONSHIP_DIRECTION_INCOMING = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_RELATIONSHIP_DIRECTION_INCOMING = 1;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 215.

```text
elationships.v2;

enum UserRelationshipDirection {
  USER_RELATIONSHIP_DIRECTION_UNSPECIFIED = 0;
  USER_RELATIONSHIP_DIRECTION_INCOMING = 1;
  USER_RELATIONSHIP_DIRECTION_OUTGOING = 2;
  USER_RELATIONSHIP_DIRECTION_MUTUAL = 3;
}

enum UserRelationshipType {
  USER_RELATIONSHIP_TYPE_UNSPECIFIED = 0;
  USER_RELATIONSHIP_TYPE_FRIENDSHIP = 1;
  USER_RELATIONSHIP_TYPE_BLOCK = 2;
  USER_RELATIONSHIP_TYPE_FRIEND_REQUEST = 
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12500"></a>
## FND-12500: chesscom.user_relationships.v2.UserRelationshipDirection.USER_RELATIONSHIP_DIRECTION_OUTGOING = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_RELATIONSHIP_DIRECTION_OUTGOING = 2;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 259.

```text
tion {
  USER_RELATIONSHIP_DIRECTION_UNSPECIFIED = 0;
  USER_RELATIONSHIP_DIRECTION_INCOMING = 1;
  USER_RELATIONSHIP_DIRECTION_OUTGOING = 2;
  USER_RELATIONSHIP_DIRECTION_MUTUAL = 3;
}

enum UserRelationshipType {
  USER_RELATIONSHIP_TYPE_UNSPECIFIED = 0;
  USER_RELATIONSHIP_TYPE_FRIENDSHIP = 1;
  USER_RELATIONSHIP_TYPE_BLOCK = 2;
  USER_RELATIONSHIP_TYPE_FRIEND_REQUEST = 3;
}

message UserRelationship {
  optional 
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12501"></a>
## FND-12501: chesscom.user_relationships.v2.UserRelationshipDirection.USER_RELATIONSHIP_DIRECTION_MUTUAL = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_RELATIONSHIP_DIRECTION_MUTUAL = 3;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 303.

```text
FIED = 0;
  USER_RELATIONSHIP_DIRECTION_INCOMING = 1;
  USER_RELATIONSHIP_DIRECTION_OUTGOING = 2;
  USER_RELATIONSHIP_DIRECTION_MUTUAL = 3;
}

enum UserRelationshipType {
  USER_RELATIONSHIP_TYPE_UNSPECIFIED = 0;
  USER_RELATIONSHIP_TYPE_FRIENDSHIP = 1;
  USER_RELATIONSHIP_TYPE_BLOCK = 2;
  USER_RELATIONSHIP_TYPE_FRIEND_REQUEST = 3;
}

message UserRelationship {
  optional .chesscom.user_relationships.v2.UserRelation
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12502"></a>
## FND-12502: enum declaration: chesscom.user_relationships.v2.UserRelationshipType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum UserRelationshipType {

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 346.

```text
OMING = 1;
  USER_RELATIONSHIP_DIRECTION_OUTGOING = 2;
  USER_RELATIONSHIP_DIRECTION_MUTUAL = 3;
}

enum UserRelationshipType {
  USER_RELATIONSHIP_TYPE_UNSPECIFIED = 0;
  USER_RELATIONSHIP_TYPE_FRIENDSHIP = 1;
  USER_RELATIONSHIP_TYPE_BLOCK = 2;
  USER_RELATIONSHIP_TYPE_FRIEND_REQUEST = 3;
}

message UserRelationship {
  optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;
  optional .chesscom.use
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12503"></a>
## FND-12503: chesscom.user_relationships.v2.UserRelationshipType.USER_RELATIONSHIP_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_RELATIONSHIP_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 376.

```text
_DIRECTION_OUTGOING = 2;
  USER_RELATIONSHIP_DIRECTION_MUTUAL = 3;
}

enum UserRelationshipType {
  USER_RELATIONSHIP_TYPE_UNSPECIFIED = 0;
  USER_RELATIONSHIP_TYPE_FRIENDSHIP = 1;
  USER_RELATIONSHIP_TYPE_BLOCK = 2;
  USER_RELATIONSHIP_TYPE_FRIEND_REQUEST = 3;
}

message UserRelationship {
  optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;
  optional .chesscom.user_relationships.v2.UserRelatio
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12504"></a>
## FND-12504: chesscom.user_relationships.v2.UserRelationshipType.USER_RELATIONSHIP_TYPE_FRIENDSHIP = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_RELATIONSHIP_TYPE_FRIENDSHIP = 1;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 418.

```text
IP_DIRECTION_MUTUAL = 3;
}

enum UserRelationshipType {
  USER_RELATIONSHIP_TYPE_UNSPECIFIED = 0;
  USER_RELATIONSHIP_TYPE_FRIENDSHIP = 1;
  USER_RELATIONSHIP_TYPE_BLOCK = 2;
  USER_RELATIONSHIP_TYPE_FRIEND_REQUEST = 3;
}

message UserRelationship {
  optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
  optional .
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12505"></a>
## FND-12505: chesscom.user_relationships.v2.UserRelationshipType.USER_RELATIONSHIP_TYPE_BLOCK = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_RELATIONSHIP_TYPE_BLOCK = 2;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 459.

```text
tionshipType {
  USER_RELATIONSHIP_TYPE_UNSPECIFIED = 0;
  USER_RELATIONSHIP_TYPE_FRIENDSHIP = 1;
  USER_RELATIONSHIP_TYPE_BLOCK = 2;
  USER_RELATIONSHIP_TYPE_FRIEND_REQUEST = 3;
}

message UserRelationship {
  optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
  optional .google.protobuf.Timestamp created_at = 3;
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12506"></a>
## FND-12506: chesscom.user_relationships.v2.UserRelationshipType.USER_RELATIONSHIP_TYPE_FRIEND_REQUEST = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_RELATIONSHIP_TYPE_FRIEND_REQUEST = 3;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 495.

```text
YPE_UNSPECIFIED = 0;
  USER_RELATIONSHIP_TYPE_FRIENDSHIP = 1;
  USER_RELATIONSHIP_TYPE_BLOCK = 2;
  USER_RELATIONSHIP_TYPE_FRIEND_REQUEST = 3;
}

message UserRelationship {
  optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
  optional .google.protobuf.Timestamp created_at = 3;
}

message UserRelationshipRequestC
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12507"></a>
## FND-12507: message declaration: chesscom.user_relationships.v2.UserRelationship

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserRelationship {

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 541.

```text
FRIENDSHIP = 1;
  USER_RELATIONSHIP_TYPE_BLOCK = 2;
  USER_RELATIONSHIP_TYPE_FRIEND_REQUEST = 3;
}

message UserRelationship {
  optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
  optional .google.protobuf.Timestamp created_at = 3;
}

message UserRelationshipRequestCriteria {
  optional .chesscom.user_relationsh
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12508"></a>
## FND-12508: chesscom.user_relationships.v2.UserRelationship.type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 570.

```text
ONSHIP_TYPE_BLOCK = 2;
  USER_RELATIONSHIP_TYPE_FRIEND_REQUEST = 3;
}

message UserRelationship {
  optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
  optional .google.protobuf.Timestamp created_at = 3;
}

message UserRelationshipRequestCriteria {
  optional .chesscom.user_relationships.v2.UserRelationshipType r
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12509"></a>
## FND-12509: chesscom.user_relationships.v2.UserRelationship.direction = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 644.

```text
sage UserRelationship {
  optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
  optional .google.protobuf.Timestamp created_at = 3;
}

message UserRelationshipRequestCriteria {
  optional .chesscom.user_relationships.v2.UserRelationshipType relationship_type = 1;
  optional .chesscom.user_relationships.v2.UserRelat
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12510"></a>
## FND-12510: chesscom.user_relationships.v2.UserRelationship.created_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp created_at = 3;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 728.

```text
ype type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
  optional .google.protobuf.Timestamp created_at = 3;
}

message UserRelationshipRequestCriteria {
  optional .chesscom.user_relationships.v2.UserRelationshipType relationship_type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
}

message UserRelationshipInteraction {
  oneof _cr
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12511"></a>
## FND-12511: message declaration: chesscom.user_relationships.v2.UserRelationshipRequestCriteria

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserRelationshipRequestCriteria {

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 783.

```text
2.UserRelationshipDirection direction = 2;
  optional .google.protobuf.Timestamp created_at = 3;
}

message UserRelationshipRequestCriteria {
  optional .chesscom.user_relationships.v2.UserRelationshipType relationship_type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
}

message UserRelationshipInteraction {
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 3;
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12512"></a>
## FND-12512: chesscom.user_relationships.v2.UserRelationshipRequestCriteria.relationship_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_relationships.v2.UserRelationshipType relationship_type = 1;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 827.

```text
 optional .google.protobuf.Timestamp created_at = 3;
}

message UserRelationshipRequestCriteria {
  optional .chesscom.user_relationships.v2.UserRelationshipType relationship_type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
}

message UserRelationshipInteraction {
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 3;
  }
  optional .chesscom.user_relationships
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12513"></a>
## FND-12513: chesscom.user_relationships.v2.UserRelationshipRequestCriteria.direction = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 644.

```text
sage UserRelationship {
  optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
  optional .google.protobuf.Timestamp created_at = 3;
}

message UserRelationshipRequestCriteria {
  optional .chesscom.user_relationships.v2.UserRelationshipType relationship_type = 1;
  optional .chesscom.user_relationships.v2.UserRelat
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12514"></a>
## FND-12514: message declaration: chesscom.user_relationships.v2.UserRelationshipInteraction

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserRelationshipInteraction {

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 999.

```text
ip_type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
}

message UserRelationshipInteraction {
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 3;
  }
  optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
}

```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12515"></a>
## FND-12515: oneof declaration: chesscom.user_relationships.v2.UserRelationshipInteraction._created_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _created_at {

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 1039.

```text
elationships.v2.UserRelationshipDirection direction = 2;
}

message UserRelationshipInteraction {
  oneof _created_at {
  .google.protobuf.Timestamp created_at = 3;
  }
  optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
}

```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12516"></a>
## FND-12516: chesscom.user_relationships.v2.UserRelationshipInteraction.created_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp created_at = 3;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 737.

```text
= 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
  optional .google.protobuf.Timestamp created_at = 3;
}

message UserRelationshipRequestCriteria {
  optional .chesscom.user_relationships.v2.UserRelationshipType relationship_type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
}

message UserRelationshipInteraction {
  oneof _created_at 
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12517"></a>
## FND-12517: chesscom.user_relationships.v2.UserRelationshipInteraction.type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 570.

```text
ONSHIP_TYPE_BLOCK = 2;
  USER_RELATIONSHIP_TYPE_FRIEND_REQUEST = 3;
}

message UserRelationship {
  optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
  optional .google.protobuf.Timestamp created_at = 3;
}

message UserRelationshipRequestCriteria {
  optional .chesscom.user_relationships.v2.UserRelationshipType r
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12518"></a>
## FND-12518: chesscom.user_relationships.v2.UserRelationshipInteraction.direction = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;

### Evidence

- **SRC-0648** `research/proto/chesscom/user_relationships/v2/user_relationships_model.proto` — [preserved redacted evidence](../evidence/text/993098f54e065c9fc7db020c09527aff354c962416f9016b6d4624f7a0429b36.proto)
  Character offset 644.

```text
sage UserRelationship {
  optional .chesscom.user_relationships.v2.UserRelationshipType type = 1;
  optional .chesscom.user_relationships.v2.UserRelationshipDirection direction = 2;
  optional .google.protobuf.Timestamp created_at = 3;
}

message UserRelationshipRequestCriteria {
  optional .chesscom.user_relationships.v2.UserRelationshipType relationship_type = 1;
  optional .chesscom.user_relationships.v2.UserRelat
```

**Source references:** SRC-0648, SRC-1619  
**URL references:** None independently associated  
**Related findings:** FND-12497, FND-12498, FND-12499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12519"></a>
## FND-12519: enum declaration: chesscom.user_targeting.v1.BinaryOperator

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum BinaryOperator {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 115.

```text
scom/user_targeting/v1/user_targeting.proto
// syntax: proto3

package chesscom.user_targeting.v1;

enum BinaryOperator {
  BINARY_OPERATOR_UNSPECIFIED = 0;
  GREATER = 1;
  GREATER_OR_EQUAL = 2;
  LESSER = 3;
  LESSER_OR_EQUAL = 4;
  EQUALS = 5;
  NOT_EQUALS = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 1
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12520"></a>
## FND-12520: chesscom.user_targeting.v1.BinaryOperator.BINARY_OPERATOR_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BINARY_OPERATOR_UNSPECIFIED = 0;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 139.

```text
ser_targeting.proto
// syntax: proto3

package chesscom.user_targeting.v1;

enum BinaryOperator {
  BINARY_OPERATOR_UNSPECIFIED = 0;
  GREATER = 1;
  GREATER_OR_EQUAL = 2;
  LESSER = 3;
  LESSER_OR_EQUAL = 4;
  EQUALS = 5;
  NOT_EQUALS = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12521"></a>
## FND-12521: chesscom.user_targeting.v1.BinaryOperator.GREATER = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GREATER = 1;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 174.

```text
o3

package chesscom.user_targeting.v1;

enum BinaryOperator {
  BINARY_OPERATOR_UNSPECIFIED = 0;
  GREATER = 1;
  GREATER_OR_EQUAL = 2;
  LESSER = 3;
  LESSER_OR_EQUAL = 4;
  EQUALS = 5;
  NOT_EQUALS = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12522"></a>
## FND-12522: chesscom.user_targeting.v1.BinaryOperator.GREATER_OR_EQUAL = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GREATER_OR_EQUAL = 2;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 189.

```text
sscom.user_targeting.v1;

enum BinaryOperator {
  BINARY_OPERATOR_UNSPECIFIED = 0;
  GREATER = 1;
  GREATER_OR_EQUAL = 2;
  LESSER = 3;
  LESSER_OR_EQUAL = 4;
  EQUALS = 5;
  NOT_EQUALS = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12523"></a>
## FND-12523: chesscom.user_targeting.v1.BinaryOperator.LESSER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LESSER = 3;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 213.

```text


enum BinaryOperator {
  BINARY_OPERATOR_UNSPECIFIED = 0;
  GREATER = 1;
  GREATER_OR_EQUAL = 2;
  LESSER = 3;
  LESSER_OR_EQUAL = 4;
  EQUALS = 5;
  NOT_EQUALS = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12524"></a>
## FND-12524: chesscom.user_targeting.v1.BinaryOperator.LESSER_OR_EQUAL = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LESSER_OR_EQUAL = 4;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 227.

```text
perator {
  BINARY_OPERATOR_UNSPECIFIED = 0;
  GREATER = 1;
  GREATER_OR_EQUAL = 2;
  LESSER = 3;
  LESSER_OR_EQUAL = 4;
  EQUALS = 5;
  NOT_EQUALS = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPE
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12525"></a>
## FND-12525: chesscom.user_targeting.v1.BinaryOperator.EQUALS = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EQUALS = 5;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 250.

```text
ATOR_UNSPECIFIED = 0;
  GREATER = 1;
  GREATER_OR_EQUAL = 2;
  LESSER = 3;
  LESSER_OR_EQUAL = 4;
  EQUALS = 5;
  NOT_EQUALS = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12526"></a>
## FND-12526: chesscom.user_targeting.v1.BinaryOperator.NOT_EQUALS = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOT_EQUALS = 6;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 264.

```text
ED = 0;
  GREATER = 1;
  GREATER_OR_EQUAL = 2;
  LESSER = 3;
  LESSER_OR_EQUAL = 4;
  EQUALS = 5;
  NOT_EQUALS = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  O
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12527"></a>
## FND-12527: chesscom.user_targeting.v1.BinaryOperator.CONTAINS = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CONTAINS = 7;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 282.

```text
= 1;
  GREATER_OR_EQUAL = 2;
  LESSER = 3;
  LESSER_OR_EQUAL = 4;
  EQUALS = 5;
  NOT_EQUALS = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum Dat
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12528"></a>
## FND-12528: chesscom.user_targeting.v1.BinaryOperator.DOES_NOT_CONTAIN = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DOES_NOT_CONTAIN = 8;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 298.

```text
R_EQUAL = 2;
  LESSER = 3;
  LESSER_OR_EQUAL = 4;
  EQUALS = 5;
  NOT_EQUALS = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12529"></a>
## FND-12529: chesscom.user_targeting.v1.BinaryOperator.WITHIN = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

WITHIN = 9;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 322.

```text
3;
  LESSER_OR_EQUAL = 4;
  EQUALS = 5;
  NOT_EQUALS = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECI
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12530"></a>
## FND-12530: chesscom.user_targeting.v1.BinaryOperator.STARTS_WITH = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STARTS_WITH = 10;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 336.

```text
_EQUAL = 4;
  EQUALS = 5;
  NOT_EQUALS = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EV
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12531"></a>
## FND-12531: chesscom.user_targeting.v1.BinaryOperator.ENDS_WITH = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENDS_WITH = 11;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 356.

```text
 = 5;
  NOT_EQUALS = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYP
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12532"></a>
## FND-12532: chesscom.user_targeting.v1.BinaryOperator.MATCHES = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MATCHES = 12;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 374.

```text
 = 6;
  CONTAINS = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVE
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12533"></a>
## FND-12533: chesscom.user_targeting.v1.BinaryOperator.NOT_WITHIN = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOT_WITHIN = 13;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 390.

```text
 = 7;
  DOES_NOT_CONTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12534"></a>
## FND-12534: chesscom.user_targeting.v1.BinaryOperator.ANY_OF = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANY_OF = 14;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 409.

```text
NTAIN = 8;
  WITHIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12535"></a>
## FND-12535: chesscom.user_targeting.v1.BinaryOperator.NONE_OF = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NONE_OF = 15;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 424.

```text
THIN = 9;
  STARTS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

e
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12536"></a>
## FND-12536: chesscom.user_targeting.v1.BinaryOperator.EXISTS = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EXISTS = 16;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 440.

```text
TS_WITH = 10;
  ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
 
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12537"></a>
## FND-12537: chesscom.user_targeting.v1.BinaryOperator.NOT_EXISTS = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOT_EXISTS = 17;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 455.

```text
 ENDS_WITH = 11;
  MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSP
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12538"></a>
## FND-12538: chesscom.user_targeting.v1.BinaryOperator.BETWEEN = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BETWEEN = 18;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 474.

```text
MATCHES = 12;
  NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILL
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12539"></a>
## FND-12539: chesscom.user_targeting.v1.BinaryOperator.NOT_BETWEEN = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NOT_BETWEEN = 19;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 490.

```text
NOT_WITHIN = 13;
  ANY_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12540"></a>
## FND-12540: enum declaration: chesscom.user_targeting.v1.LogicalOperator

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum LogicalOperator {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 511.

```text
Y_OF = 14;
  NONE_OF = 15;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTE
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12541"></a>
## FND-12541: chesscom.user_targeting.v1.LogicalOperator.LOGICAL_OPERATOR_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOGICAL_OPERATOR_UNSPECIFIED = 0;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 536.

```text
;
  EXISTS = 16;
  NOT_EXISTS = 17;
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAY
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12542"></a>
## FND-12542: chesscom.user_targeting.v1.LogicalOperator.AND = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

AND = 1;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 572.

```text
  BETWEEN = 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12543"></a>
## FND-12543: chesscom.user_targeting.v1.LogicalOperator.OR = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

OR = 2;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 583.

```text
 18;
  NOT_BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeD
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12544"></a>
## FND-12544: enum declaration: chesscom.user_targeting.v1.DataSourceType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum DataSourceType {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 594.

```text
BETWEEN = 19;
}

enum LogicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12545"></a>
## FND-12545: chesscom.user_targeting.v1.DataSourceType.DATA_SOURCE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DATA_SOURCE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 618.

```text
gicalOperator {
  LOGICAL_OPERATOR_UNSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECI
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12546"></a>
## FND-12546: chesscom.user_targeting.v1.DataSourceType.EVENT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT = 1;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 654.

```text
NSPECIFIED = 0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12547"></a>
## FND-12547: chesscom.user_targeting.v1.DataSourceType.EVENT_TYPE_TRACK = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_TRACK = 2;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 667.

```text
0;
  AND = 1;
  OR = 2;
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrd
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12548"></a>
## FND-12548: chesscom.user_targeting.v1.DataSourceType.EVENT_TYPE_TYPED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

EVENT_TYPE_TYPED = 3;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 691.

```text
}

enum DataSourceType {
  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPEC
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12549"></a>
## FND-12549: chesscom.user_targeting.v1.DataSourceType.TEMPORARY_USER_DATA = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TEMPORARY_USER_DATA = 4;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 715.

```text

  DATA_SOURCE_TYPE_UNSPECIFIED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12550"></a>
## FND-12550: enum declaration: chesscom.user_targeting.v1.TimeUnit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TimeUnit {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 743.

```text
IED = 0;
  EVENT = 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC =
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12551"></a>
## FND-12551: chesscom.user_targeting.v1.TimeUnit.TIME_UNIT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_UNIT_UNSPECIFIED = 0;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 761.

```text
 1;
  EVENT_TYPE_TRACK = 2;
  EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Rul
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12552"></a>
## FND-12552: chesscom.user_targeting.v1.TimeUnit.MILLISECONDS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MILLISECONDS = 1;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 790.

```text
 EVENT_TYPE_TYPED = 3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_opera
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12553"></a>
## FND-12553: chesscom.user_targeting.v1.TimeUnit.SECONDS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SECONDS = 2;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 810.

```text
3;
  TEMPORARY_USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.us
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12554"></a>
## FND-12554: chesscom.user_targeting.v1.TimeUnit.MINUTES = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MINUTES = 3;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 825.

```text
USER_DATA = 4;
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12555"></a>
## FND-12555: chesscom.user_targeting.v1.TimeUnit.HOURS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

HOURS = 4;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 840.

```text
}

enum TimeUnit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperato
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12556"></a>
## FND-12556: chesscom.user_targeting.v1.TimeUnit.DAYS = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DAYS = 5;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 853.

```text
nit {
  TIME_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_ope
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12557"></a>
## FND-12557: chesscom.user_targeting.v1.TimeUnit.MONTHS = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MONTHS = 6;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 865.

```text
_UNIT_UNSPECIFIED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
 
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12558"></a>
## FND-12558: chesscom.user_targeting.v1.TimeUnit.YEARS = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

YEARS = 7;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 879.

```text
IED = 0;
  MILLISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional 
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12559"></a>
## FND-12559: enum declaration: chesscom.user_targeting.v1.TimeDirection

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TimeDirection {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 893.

```text
LISECONDS = 1;
  SECONDS = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12560"></a>
## FND-12560: chesscom.user_targeting.v1.TimeDirection.TIME_DIRECTION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_DIRECTION_UNSPECIFIED = 0;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 916.

```text
S = 2;
  MINUTES = 3;
  HOURS = 4;
  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string nam
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12561"></a>
## FND-12561: chesscom.user_targeting.v1.TimeDirection.LAST = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LAST = 1;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 950.

```text

  DAYS = 5;
  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12562"></a>
## FND-12562: chesscom.user_targeting.v1.TimeDirection.NEXT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NEXT = 2;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 962.

```text

  MONTHS = 6;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12563"></a>
## FND-12563: enum declaration: chesscom.user_targeting.v1.SortOrder

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SortOrder {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 975.

```text
;
  YEARS = 7;
}

enum TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated .chesscom.us
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12564"></a>
## FND-12564: chesscom.user_targeting.v1.SortOrder.SORT_ORDER_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_ORDER_UNSPECIFIED = 0;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 994.

```text
num TimeDirection {
  TIME_DIRECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated .chesscom.user_targeting.v1.Cri
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12565"></a>
## FND-12565: chesscom.user_targeting.v1.SortOrder.SORT_ORDER_ASC = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_ORDER_ASC = 1;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1024.

```text
ECTION_UNSPECIFIED = 0;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 4;
  repeate
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12566"></a>
## FND-12566: chesscom.user_targeting.v1.SortOrder.SORT_ORDER_DESC = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SORT_ORDER_DESC = 2;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1046.

```text
;
  LAST = 1;
  NEXT = 2;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 4;
  repeated .chesscom.user_targe
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12567"></a>
## FND-12567: message declaration: chesscom.user_targeting.v1.Ruleset

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Ruleset {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1070.

```text
;
}

enum SortOrder {
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 4;
  repeated .chesscom.user_targeting.v1.NestedCriteria c
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12568"></a>
## FND-12568: oneof declaration: chesscom.user_targeting.v1.Ruleset._logical_operator

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _logical_operator {

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1090.

```text
{
  SORT_ORDER_UNSPECIFIED = 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 4;
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 6;

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-12569"></a>
## FND-12569: chesscom.user_targeting.v1.Ruleset.logical_operator = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1118.

```text
 0;
  SORT_ORDER_ASC = 1;
  SORT_ORDER_DESC = 2;
}

message Ruleset {
  oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 4;
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 6;
}

message Criterion {
  one
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12570"></a>
## FND-12570: chesscom.user_targeting.v1.Ruleset.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1190.

```text
oneof _logical_operator {
  .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 4;
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 6;
}

message Criterion {
  oneof _value {
  string value = 3;
  }
  oneof _modifier {
  .chesscom.user
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12571"></a>
## FND-12571: chesscom.user_targeting.v1.Ruleset.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1217.

```text
 .chesscom.user_targeting.v1.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 4;
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 6;
}

message Criterion {
  oneof _value {
  string value = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.BinaryOperato
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12572"></a>
## FND-12572: chesscom.user_targeting.v1.Ruleset.enabled = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enabled = 3;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1245.

```text
.LogicalOperator logical_operator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 4;
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 6;
}

message Criterion {
  oneof _value {
  string value = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.BinaryOperatorModifier modifier = 4;
  }

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12573"></a>
## FND-12573: chesscom.user_targeting.v1.Ruleset.criteria = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_targeting.v1.Criterion criteria = 4;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1274.

```text
ator = 5;
  }
  optional string key = 1;
  optional string name = 2;
  optional bool enabled = 3;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 4;
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 6;
}

message Criterion {
  oneof _value {
  string value = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.BinaryOperatorModifier modifier = 4;
  }
  oneof _second_value {
  str
```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-12574"></a>
## FND-12574: chesscom.user_targeting.v1.Ruleset.criteria_groups = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 6;

### Evidence

- **SRC-0649** `research/proto/chesscom/user_targeting/v1/user_targeting.proto` — [preserved redacted evidence](../evidence/text/4eccac93f2cec2ffa2fa285a27ac7ca8fd809c2d7b7768265a868d4382d6737c.proto)
  Character offset 1337.

```text
 = 2;
  optional bool enabled = 3;
  repeated .chesscom.user_targeting.v1.Criterion criteria = 4;
  repeated .chesscom.user_targeting.v1.NestedCriteria criteria_groups = 6;
}

message Criterion {
  oneof _value {
  string value = 3;
  }
  oneof _modifier {
  .chesscom.user_targeting.v1.BinaryOperatorModifier modifier = 4;
  }
  oneof _second_value {
  string second_value = 6;
  }
  optional string user_property = 1;

```

**Source references:** SRC-0649, SRC-1620  
**URL references:** None independently associated  
**Related findings:** FND-12519, FND-12520, FND-12521

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
