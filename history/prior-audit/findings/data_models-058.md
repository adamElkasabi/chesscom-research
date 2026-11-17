# data_models — findings 5701–5800

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-05975"></a>
## FND-05975: oneof declaration: chesscom.gameplay.v1.BattleRef._id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _id {

### Evidence

- **SRC-0472** `research/proto/chesscom/gameplay/v1/battle_ref.proto` — [preserved redacted evidence](../evidence/text/1095c2fbd6687265385775191e6542174762eba14488e75713fc5624935fa201.proto)
  Character offset 121.

```text
ameplay/v1/battle_ref.proto
// syntax: proto3

package chesscom.gameplay.v1;

message BattleRef {
  oneof _id {
  string id = 1;
  }
}

```

**Source references:** SRC-0472, SRC-1443  
**URL references:** None independently associated  
**Related findings:** FND-05974, FND-05976

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05976"></a>
## FND-05976: chesscom.gameplay.v1.BattleRef.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string id = 1;

### Evidence

- **SRC-0472** `research/proto/chesscom/gameplay/v1/battle_ref.proto` — [preserved redacted evidence](../evidence/text/1095c2fbd6687265385775191e6542174762eba14488e75713fc5624935fa201.proto)
  Character offset 135.

```text
tle_ref.proto
// syntax: proto3

package chesscom.gameplay.v1;

message BattleRef {
  oneof _id {
  string id = 1;
  }
}

```

**Source references:** SRC-0472, SRC-1443  
**URL references:** None independently associated  
**Related findings:** FND-05974, FND-05975

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05977"></a>
## FND-05977: enum declaration: chesscom.gameplay.v1.GameSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameSource {

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 97.

```text
// source: chesscom/gameplay/v1/game_ref.proto
// syntax: proto3

package chesscom.gameplay.v1;

enum GameSource {
  GAME_SOURCE_UNSPECIFIED = 0;
  GAME_SOURCE_RCN = 1;
  GAME_SOURCE_LC = 2;
}

message GameRef {
  oneof _id {
  string id = 1;
  }
  oneof _numeric_id {
  int64 numeric_id = 2;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass tim
```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05978, FND-05979

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05978"></a>
## FND-05978: chesscom.gameplay.v1.GameSource.GAME_SOURCE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_SOURCE_UNSPECIFIED = 0;

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 117.

```text
om/gameplay/v1/game_ref.proto
// syntax: proto3

package chesscom.gameplay.v1;

enum GameSource {
  GAME_SOURCE_UNSPECIFIED = 0;
  GAME_SOURCE_RCN = 1;
  GAME_SOURCE_LC = 2;
}

message GameRef {
  oneof _id {
  string id = 1;
  }
  oneof _numeric_id {
  int64 numeric_id = 2;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  on
```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05979

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05979"></a>
## FND-05979: chesscom.gameplay.v1.GameSource.GAME_SOURCE_RCN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_SOURCE_RCN = 1;

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 148.

```text
/ syntax: proto3

package chesscom.gameplay.v1;

enum GameSource {
  GAME_SOURCE_UNSPECIFIED = 0;
  GAME_SOURCE_RCN = 1;
  GAME_SOURCE_LC = 2;
}

message GameRef {
  oneof _id {
  string id = 1;
  }
  oneof _numeric_id {
  int64 numeric_id = 2;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gamep
```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05980"></a>
## FND-05980: chesscom.gameplay.v1.GameSource.GAME_SOURCE_LC = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_SOURCE_LC = 2;

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 171.

```text
ge chesscom.gameplay.v1;

enum GameSource {
  GAME_SOURCE_UNSPECIFIED = 0;
  GAME_SOURCE_RCN = 1;
  GAME_SOURCE_LC = 2;
}

message GameRef {
  oneof _id {
  string id = 1;
  }
  oneof _numeric_id {
  int64 numeric_id = 2;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource sourc
```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05981"></a>
## FND-05981: message declaration: chesscom.gameplay.v1.GameRef

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameRef {

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 194.

```text
;

enum GameSource {
  GAME_SOURCE_UNSPECIFIED = 0;
  GAME_SOURCE_RCN = 1;
  GAME_SOURCE_LC = 2;
}

message GameRef {
  oneof _id {
  string id = 1;
  }
  oneof _numeric_id {
  int64 numeric_id = 2;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_
```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05982"></a>
## FND-05982: oneof declaration: chesscom.gameplay.v1.GameRef._id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _id {

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 214.

```text

  GAME_SOURCE_UNSPECIFIED = 0;
  GAME_SOURCE_RCN = 1;
  GAME_SOURCE_LC = 2;
}

message GameRef {
  oneof _id {
  string id = 1;
  }
  oneof _numeric_id {
  int64 numeric_id = 2;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_private {
  bool is_
```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05983"></a>
## FND-05983: chesscom.gameplay.v1.GameRef.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string id = 1;

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 228.

```text
_UNSPECIFIED = 0;
  GAME_SOURCE_RCN = 1;
  GAME_SOURCE_LC = 2;
}

message GameRef {
  oneof _id {
  string id = 1;
  }
  oneof _numeric_id {
  int64 numeric_id = 2;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_private {
  bool is_private = 6;
 
```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05984"></a>
## FND-05984: oneof declaration: chesscom.gameplay.v1.GameRef._numeric_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _numeric_id {

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 249.

```text
AME_SOURCE_RCN = 1;
  GAME_SOURCE_LC = 2;
}

message GameRef {
  oneof _id {
  string id = 1;
  }
  oneof _numeric_id {
  int64 numeric_id = 2;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_private {
  bool is_private = 6;
  }
  oneof _legacy_id
```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05985"></a>
## FND-05985: chesscom.gameplay.v1.GameRef.numeric_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 numeric_id = 2;

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 271.

```text
GAME_SOURCE_LC = 2;
}

message GameRef {
  oneof _id {
  string id = 1;
  }
  oneof _numeric_id {
  int64 numeric_id = 2;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_private {
  bool is_private = 6;
  }
  oneof _legacy_id {
  int64 legacy_id =
```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05986"></a>
## FND-05986: oneof declaration: chesscom.gameplay.v1.GameRef._variant

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _variant {

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 299.

```text
ge GameRef {
  oneof _id {
  string id = 1;
  }
  oneof _numeric_id {
  int64 numeric_id = 2;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_private {
  bool is_private = 6;
  }
  oneof _legacy_id {
  int64 legacy_id = 7;
  }
}

```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05987"></a>
## FND-05987: chesscom.gameplay.v1.GameRef.variant = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Variant variant = 3;

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 318.

```text
f _id {
  string id = 1;
  }
  oneof _numeric_id {
  int64 numeric_id = 2;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_private {
  bool is_private = 6;
  }
  oneof _legacy_id {
  int64 legacy_id = 7;
  }
}

```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05988"></a>
## FND-05988: oneof declaration: chesscom.gameplay.v1.GameRef._timeclass

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _timeclass {

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 364.

```text
id {
  int64 numeric_id = 2;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_private {
  bool is_private = 6;
  }
  oneof _legacy_id {
  int64 legacy_id = 7;
  }
}

```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05989"></a>
## FND-05989: chesscom.gameplay.v1.GameRef.timeclass = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.TimeClass timeclass = 4;

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 385.

```text
id = 2;
  }
  oneof _variant {
  .chesscom.chess.v1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_private {
  bool is_private = 6;
  }
  oneof _legacy_id {
  int64 legacy_id = 7;
  }
}

```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05990"></a>
## FND-05990: oneof declaration: chesscom.gameplay.v1.GameRef._source

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _source {

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 435.

```text
1.Variant variant = 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_private {
  bool is_private = 6;
  }
  oneof _legacy_id {
  int64 legacy_id = 7;
  }
}

```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05991"></a>
## FND-05991: chesscom.gameplay.v1.GameRef.source = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.gameplay.v1.GameSource source = 5;

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 453.

```text
= 3;
  }
  oneof _timeclass {
  .chesscom.chess.v1.TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_private {
  bool is_private = 6;
  }
  oneof _legacy_id {
  int64 legacy_id = 7;
  }
}

```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05992"></a>
## FND-05992: oneof declaration: chesscom.gameplay.v1.GameRef._is_private

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_private {

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 504.

```text
TimeClass timeclass = 4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_private {
  bool is_private = 6;
  }
  oneof _legacy_id {
  int64 legacy_id = 7;
  }
}

```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05993"></a>
## FND-05993: chesscom.gameplay.v1.GameRef.is_private = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_private = 6;

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 526.

```text
4;
  }
  oneof _source {
  .chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_private {
  bool is_private = 6;
  }
  oneof _legacy_id {
  int64 legacy_id = 7;
  }
}

```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05994"></a>
## FND-05994: oneof declaration: chesscom.gameplay.v1.GameRef._legacy_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _legacy_id {

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 553.

```text
.chesscom.gameplay.v1.GameSource source = 5;
  }
  oneof _is_private {
  bool is_private = 6;
  }
  oneof _legacy_id {
  int64 legacy_id = 7;
  }
}

```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05995"></a>
## FND-05995: chesscom.gameplay.v1.GameRef.legacy_id = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 legacy_id = 7;

### Evidence

- **SRC-0473** `research/proto/chesscom/gameplay/v1/game_ref.proto` — [preserved redacted evidence](../evidence/text/b97c1ed98c23484ee2281ea0e4aee8b7a67f7ad80e5cded1f30b1a26ff731d67.proto)
  Character offset 574.

```text
.GameSource source = 5;
  }
  oneof _is_private {
  bool is_private = 6;
  }
  oneof _legacy_id {
  int64 legacy_id = 7;
  }
}

```

**Source references:** SRC-0473, SRC-1444  
**URL references:** None independently associated  
**Related findings:** FND-05977, FND-05978, FND-05979

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05996"></a>
## FND-05996: enum declaration: chesscom.i18n.v1.FailedSyncErrorCode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum FailedSyncErrorCode {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 92.

```text
// source: chesscom/i18n/v1/translation.proto
// syntax: proto3

package chesscom.i18n.v1;

enum FailedSyncErrorCode {
  FAILED_SYNC_ERROR_CODE_UNSPECIFIED = 0;
  FAILED_SYNC_ERROR_CODE_CROWDIN_API_ERROR = 1;
  FAILED_SYNC_ERROR_CODE_NETWORK_TIMEOUT = 2;
  FAILED_SYNC_ERROR_CODE_SYNC_ERROR = 3;
  FAILED_SYNC_ERROR_CODE_SOURCE_DIVERGENCE = 4;
}

enum SyncWarningKind {
  SYNC_WARNING_KIND_UNSPECIFIED = 0;
  SYN
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05997"></a>
## FND-05997: chesscom.i18n.v1.FailedSyncErrorCode.FAILED_SYNC_ERROR_CODE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FAILED_SYNC_ERROR_CODE_UNSPECIFIED = 0;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 121.

```text
18n/v1/translation.proto
// syntax: proto3

package chesscom.i18n.v1;

enum FailedSyncErrorCode {
  FAILED_SYNC_ERROR_CODE_UNSPECIFIED = 0;
  FAILED_SYNC_ERROR_CODE_CROWDIN_API_ERROR = 1;
  FAILED_SYNC_ERROR_CODE_NETWORK_TIMEOUT = 2;
  FAILED_SYNC_ERROR_CODE_SYNC_ERROR = 3;
  FAILED_SYNC_ERROR_CODE_SOURCE_DIVERGENCE = 4;
}

enum SyncWarningKind {
  SYNC_WARNING_KIND_UNSPECIFIED = 0;
  SYNC_WARNING_KIND_MISSING_IN_DB 
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05998"></a>
## FND-05998: chesscom.i18n.v1.FailedSyncErrorCode.FAILED_SYNC_ERROR_CODE_CROWDIN_API_ERROR = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FAILED_SYNC_ERROR_CODE_CROWDIN_API_ERROR = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 163.

```text


package chesscom.i18n.v1;

enum FailedSyncErrorCode {
  FAILED_SYNC_ERROR_CODE_UNSPECIFIED = 0;
  FAILED_SYNC_ERROR_CODE_CROWDIN_API_ERROR = 1;
  FAILED_SYNC_ERROR_CODE_NETWORK_TIMEOUT = 2;
  FAILED_SYNC_ERROR_CODE_SYNC_ERROR = 3;
  FAILED_SYNC_ERROR_CODE_SOURCE_DIVERGENCE = 4;
}

enum SyncWarningKind {
  SYNC_WARNING_KIND_UNSPECIFIED = 0;
  SYNC_WARNING_KIND_MISSING_IN_DB = 1;
  SYNC_WARNING_KIND_UNAPPROVED_IN_DB 
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05999"></a>
## FND-05999: chesscom.i18n.v1.FailedSyncErrorCode.FAILED_SYNC_ERROR_CODE_NETWORK_TIMEOUT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FAILED_SYNC_ERROR_CODE_NETWORK_TIMEOUT = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 211.

```text
rCode {
  FAILED_SYNC_ERROR_CODE_UNSPECIFIED = 0;
  FAILED_SYNC_ERROR_CODE_CROWDIN_API_ERROR = 1;
  FAILED_SYNC_ERROR_CODE_NETWORK_TIMEOUT = 2;
  FAILED_SYNC_ERROR_CODE_SYNC_ERROR = 3;
  FAILED_SYNC_ERROR_CODE_SOURCE_DIVERGENCE = 4;
}

enum SyncWarningKind {
  SYNC_WARNING_KIND_UNSPECIFIED = 0;
  SYNC_WARNING_KIND_MISSING_IN_DB = 1;
  SYNC_WARNING_KIND_UNAPPROVED_IN_DB = 2;
  SYNC_WARNING_KIND_MISSING_IN_VENDOR = 3;

```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06000"></a>
## FND-06000: chesscom.i18n.v1.FailedSyncErrorCode.FAILED_SYNC_ERROR_CODE_SYNC_ERROR = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FAILED_SYNC_ERROR_CODE_SYNC_ERROR = 3;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 257.

```text
 0;
  FAILED_SYNC_ERROR_CODE_CROWDIN_API_ERROR = 1;
  FAILED_SYNC_ERROR_CODE_NETWORK_TIMEOUT = 2;
  FAILED_SYNC_ERROR_CODE_SYNC_ERROR = 3;
  FAILED_SYNC_ERROR_CODE_SOURCE_DIVERGENCE = 4;
}

enum SyncWarningKind {
  SYNC_WARNING_KIND_UNSPECIFIED = 0;
  SYNC_WARNING_KIND_MISSING_IN_DB = 1;
  SYNC_WARNING_KIND_UNAPPROVED_IN_DB = 2;
  SYNC_WARNING_KIND_MISSING_IN_VENDOR = 3;
}

message TranslationResourceStats {
  option
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06001"></a>
## FND-06001: chesscom.i18n.v1.FailedSyncErrorCode.FAILED_SYNC_ERROR_CODE_SOURCE_DIVERGENCE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FAILED_SYNC_ERROR_CODE_SOURCE_DIVERGENCE = 4;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 298.

```text
ERROR = 1;
  FAILED_SYNC_ERROR_CODE_NETWORK_TIMEOUT = 2;
  FAILED_SYNC_ERROR_CODE_SYNC_ERROR = 3;
  FAILED_SYNC_ERROR_CODE_SOURCE_DIVERGENCE = 4;
}

enum SyncWarningKind {
  SYNC_WARNING_KIND_UNSPECIFIED = 0;
  SYNC_WARNING_KIND_MISSING_IN_DB = 1;
  SYNC_WARNING_KIND_UNAPPROVED_IN_DB = 2;
  SYNC_WARNING_KIND_MISSING_IN_VENDOR = 3;
}

message TranslationResourceStats {
  optional string resource_id = 1;
  optional str
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06002"></a>
## FND-06002: enum declaration: chesscom.i18n.v1.SyncWarningKind

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SyncWarningKind {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 347.

```text
UT = 2;
  FAILED_SYNC_ERROR_CODE_SYNC_ERROR = 3;
  FAILED_SYNC_ERROR_CODE_SOURCE_DIVERGENCE = 4;
}

enum SyncWarningKind {
  SYNC_WARNING_KIND_UNSPECIFIED = 0;
  SYNC_WARNING_KIND_MISSING_IN_DB = 1;
  SYNC_WARNING_KIND_UNAPPROVED_IN_DB = 2;
  SYNC_WARNING_KIND_MISSING_IN_VENDOR = 3;
}

message TranslationResourceStats {
  optional string resource_id = 1;
  optional string key = 2;
  repeated .chesscom.i18n.v1.Transla
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06003"></a>
## FND-06003: chesscom.i18n.v1.SyncWarningKind.SYNC_WARNING_KIND_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SYNC_WARNING_KIND_UNSPECIFIED = 0;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 372.

```text
OR_CODE_SYNC_ERROR = 3;
  FAILED_SYNC_ERROR_CODE_SOURCE_DIVERGENCE = 4;
}

enum SyncWarningKind {
  SYNC_WARNING_KIND_UNSPECIFIED = 0;
  SYNC_WARNING_KIND_MISSING_IN_DB = 1;
  SYNC_WARNING_KIND_UNAPPROVED_IN_DB = 2;
  SYNC_WARNING_KIND_MISSING_IN_VENDOR = 3;
}

message TranslationResourceStats {
  optional string resource_id = 1;
  optional string key = 2;
  repeated .chesscom.i18n.v1.TranslationResourceStats.Transla
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06004"></a>
## FND-06004: chesscom.i18n.v1.SyncWarningKind.SYNC_WARNING_KIND_MISSING_IN_DB = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SYNC_WARNING_KIND_MISSING_IN_DB = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 409.

```text
_ERROR_CODE_SOURCE_DIVERGENCE = 4;
}

enum SyncWarningKind {
  SYNC_WARNING_KIND_UNSPECIFIED = 0;
  SYNC_WARNING_KIND_MISSING_IN_DB = 1;
  SYNC_WARNING_KIND_UNAPPROVED_IN_DB = 2;
  SYNC_WARNING_KIND_MISSING_IN_VENDOR = 3;
}

message TranslationResourceStats {
  optional string resource_id = 1;
  optional string key = 2;
  repeated .chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry translation_entry
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06005"></a>
## FND-06005: chesscom.i18n.v1.SyncWarningKind.SYNC_WARNING_KIND_UNAPPROVED_IN_DB = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SYNC_WARNING_KIND_UNAPPROVED_IN_DB = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 448.

```text
num SyncWarningKind {
  SYNC_WARNING_KIND_UNSPECIFIED = 0;
  SYNC_WARNING_KIND_MISSING_IN_DB = 1;
  SYNC_WARNING_KIND_UNAPPROVED_IN_DB = 2;
  SYNC_WARNING_KIND_MISSING_IN_VENDOR = 3;
}

message TranslationResourceStats {
  optional string resource_id = 1;
  optional string key = 2;
  repeated .chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry translation_entry_rates = 3;
  optional double overall_c
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06006"></a>
## FND-06006: chesscom.i18n.v1.SyncWarningKind.SYNC_WARNING_KIND_MISSING_IN_VENDOR = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SYNC_WARNING_KIND_MISSING_IN_VENDOR = 3;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 490.

```text
UNSPECIFIED = 0;
  SYNC_WARNING_KIND_MISSING_IN_DB = 1;
  SYNC_WARNING_KIND_UNAPPROVED_IN_DB = 2;
  SYNC_WARNING_KIND_MISSING_IN_VENDOR = 3;
}

message TranslationResourceStats {
  optional string resource_id = 1;
  optional string key = 2;
  repeated .chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry translation_entry_rates = 3;
  optional double overall_completion_rate = 4;
  message TranslationE
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06007"></a>
## FND-06007: message declaration: chesscom.i18n.v1.TranslationResourceStats

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TranslationResourceStats {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 534.

```text
_IN_DB = 1;
  SYNC_WARNING_KIND_UNAPPROVED_IN_DB = 2;
  SYNC_WARNING_KIND_MISSING_IN_VENDOR = 3;
}

message TranslationResourceStats {
  optional string resource_id = 1;
  optional string key = 2;
  repeated .chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry translation_entry_rates = 3;
  optional double overall_completion_rate = 4;
  message TranslationEntryRatesEntry {
  optional string key = 1;

```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06008"></a>
## FND-06008: chesscom.i18n.v1.TranslationResourceStats.resource_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string resource_id = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 571.

```text
ROVED_IN_DB = 2;
  SYNC_WARNING_KIND_MISSING_IN_VENDOR = 3;
}

message TranslationResourceStats {
  optional string resource_id = 1;
  optional string key = 2;
  repeated .chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry translation_entry_rates = 3;
  optional double overall_completion_rate = 4;
  message TranslationEntryRatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

m
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06009"></a>
## FND-06009: chesscom.i18n.v1.TranslationResourceStats.key = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 606.

```text
D_MISSING_IN_VENDOR = 3;
}

message TranslationResourceStats {
  optional string resource_id = 1;
  optional string key = 2;
  repeated .chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry translation_entry_rates = 3;
  optional double overall_completion_rate = 4;
  message TranslationEntryRatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _proje
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06010"></a>
## FND-06010: chesscom.i18n.v1.TranslationResourceStats.translation_entry_rates = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry translation_entry_rates = 3;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 633.

```text

message TranslationResourceStats {
  optional string resource_id = 1;
  optional string key = 2;
  repeated .chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry translation_entry_rates = 3;
  optional double overall_completion_rate = 4;
  message TranslationEntryRatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06011"></a>
## FND-06011: chesscom.i18n.v1.TranslationResourceStats.overall_completion_rate = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double overall_completion_rate = 4;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 743.

```text
chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry translation_entry_rates = 3;
  optional double overall_completion_rate = 4;
  message TranslationEntryRatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06012"></a>
## FND-06012: message declaration: chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TranslationEntryRatesEntry {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 790.

```text
lationEntryRatesEntry translation_entry_rates = 3;
  optional double overall_completion_rate = 4;
  message TranslationEntryRatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata =
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06013"></a>
## FND-06013: chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 829.

```text
_rates = 3;
  optional double overall_completion_rate = 4;
  message TranslationEntryRatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06014"></a>
## FND-06014: chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double value = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 856.

```text
le overall_completion_rate = 4;
  message TranslationEntryRatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06015"></a>
## FND-06015: message declaration: chesscom.i18n.v1.Translation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Translation {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 890.

```text
message TranslationEntryRatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06016"></a>
## FND-06016: oneof declaration: chesscom.i18n.v1.Translation._project_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _project_id {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 914.

```text
RatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  repeated .chesscom.i18n.
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06017"></a>
## FND-06017: chesscom.i18n.v1.Translation.project_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string project_id = 4;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 936.

```text
l string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  repeated .chesscom.i18n.v1.Translation.Transla
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06018"></a>
## FND-06018: oneof declaration: chesscom.i18n.v1.Translation._resource_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _resource_id {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 965.

```text
double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  repeated .chesscom.i18n.v1.Translation.TranslationEntriesEntry translation_
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06019"></a>
## FND-06019: chesscom.i18n.v1.Translation.resource_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string resource_id = 5;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 988.

```text


message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  repeated .chesscom.i18n.v1.Translation.TranslationEntriesEntry translation_entries = 7;
  message 
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06020"></a>
## FND-06020: oneof declaration: chesscom.i18n.v1.Translation._translation_metadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _translation_metadata {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1018.

```text
f _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  repeated .chesscom.i18n.v1.Translation.TranslationEntriesEntry translation_entries = 7;
  message TranslationEntriesEntry {
  op
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06021"></a>
## FND-06021: chesscom.i18n.v1.Translation.translation_metadata = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1050.

```text
_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  repeated .chesscom.i18n.v1.Translation.TranslationEntriesEntry translation_entries = 7;
  message TranslationEntriesEntry {
  optional string key = 1;
  optiona
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06022"></a>
## FND-06022: chesscom.i18n.v1.Translation.string_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string string_id = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1120.

```text
eof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  repeated .chesscom.i18n.v1.Translation.TranslationEntriesEntry translation_entries = 7;
  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message FileTranslation {
  oneof _project_
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06023"></a>
## FND-06023: chesscom.i18n.v1.Translation.key = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 606.

```text
D_MISSING_IN_VENDOR = 3;
}

message TranslationResourceStats {
  optional string resource_id = 1;
  optional string key = 2;
  repeated .chesscom.i18n.v1.TranslationResourceStats.TranslationEntryRatesEntry translation_entry_rates = 3;
  optional double overall_completion_rate = 4;
  message TranslationEntryRatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _proje
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06024"></a>
## FND-06024: chesscom.i18n.v1.Translation.source = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string source = 3;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1180.

```text
etadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  repeated .chesscom.i18n.v1.Translation.TranslationEntriesEntry translation_entries = 7;
  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message FileTranslation {
  oneof _project_id {
  string project_id = 5;
  }
  oneof _resource_id {
  s
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06025"></a>
## FND-06025: chesscom.i18n.v1.Translation.translation_entries = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.i18n.v1.Translation.TranslationEntriesEntry translation_entries = 7;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1210.

```text
 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  repeated .chesscom.i18n.v1.Translation.TranslationEntriesEntry translation_entries = 7;
  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message FileTranslation {
  oneof _project_id {
  string project_id = 5;
  }
  oneof _resource_id {
  string resource_id = 6;
  }
  o
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06026"></a>
## FND-06026: message declaration: chesscom.i18n.v1.Translation.TranslationEntriesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TranslationEntriesEntry {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1300.

```text
ce = 3;
  repeated .chesscom.i18n.v1.Translation.TranslationEntriesEntry translation_entries = 7;
  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message FileTranslation {
  oneof _project_id {
  string project_id = 5;
  }
  oneof _resource_id {
  string resource_id = 6;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata 
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06027"></a>
## FND-06027: chesscom.i18n.v1.Translation.TranslationEntriesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 829.

```text
_rates = 3;
  optional double overall_completion_rate = 4;
  message TranslationEntryRatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06028"></a>
## FND-06028: chesscom.i18n.v1.Translation.TranslationEntriesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1363.

```text
riesEntry translation_entries = 7;
  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message FileTranslation {
  oneof _project_id {
  string project_id = 5;
  }
  oneof _resource_id {
  string resource_id = 6;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 7;
  }
  optional string file_id = 1;
  optional string file_
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06029"></a>
## FND-06029: message declaration: chesscom.i18n.v1.FileTranslation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FileTranslation {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1397.

```text

  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message FileTranslation {
  oneof _project_id {
  string project_id = 5;
  }
  oneof _resource_id {
  string resource_id = 6;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 7;
  }
  optional string file_id = 1;
  optional string file_name = 2;
  optional string file_p
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06030"></a>
## FND-06030: oneof declaration: chesscom.i18n.v1.FileTranslation._project_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _project_id {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 914.

```text
RatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  repeated .chesscom.i18n.
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06031"></a>
## FND-06031: chesscom.i18n.v1.FileTranslation.project_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string project_id = 5;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1447.

```text
ring key = 1;
  optional string value = 2;
  }
}

message FileTranslation {
  oneof _project_id {
  string project_id = 5;
  }
  oneof _resource_id {
  string resource_id = 6;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 7;
  }
  optional string file_id = 1;
  optional string file_name = 2;
  optional string file_path = 3;
  optional string file_format = 4;
  repe
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06032"></a>
## FND-06032: oneof declaration: chesscom.i18n.v1.FileTranslation._resource_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _resource_id {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 965.

```text
double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  repeated .chesscom.i18n.v1.Translation.TranslationEntriesEntry translation_
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06033"></a>
## FND-06033: chesscom.i18n.v1.FileTranslation.resource_id = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string resource_id = 6;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1499.

```text
ssage FileTranslation {
  oneof _project_id {
  string project_id = 5;
  }
  oneof _resource_id {
  string resource_id = 6;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 7;
  }
  optional string file_id = 1;
  optional string file_name = 2;
  optional string file_path = 3;
  optional string file_format = 4;
  repeated .chesscom.i18n.v1.FileTranslation.TranslationEn
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06034"></a>
## FND-06034: oneof declaration: chesscom.i18n.v1.FileTranslation._translation_metadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _translation_metadata {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1018.

```text
f _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  repeated .chesscom.i18n.v1.Translation.TranslationEntriesEntry translation_entries = 7;
  message TranslationEntriesEntry {
  op
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06035"></a>
## FND-06035: chesscom.i18n.v1.FileTranslation.translation_metadata = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.i18n.v1.TranslationMetadata translation_metadata = 7;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1561.

```text
_id = 5;
  }
  oneof _resource_id {
  string resource_id = 6;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 7;
  }
  optional string file_id = 1;
  optional string file_name = 2;
  optional string file_path = 3;
  optional string file_format = 4;
  repeated .chesscom.i18n.v1.FileTranslation.TranslationEntriesEntry translation_entries = 8;
  repeated string tags = 9
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06036"></a>
## FND-06036: chesscom.i18n.v1.FileTranslation.file_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string file_id = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1631.

```text
eof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 7;
  }
  optional string file_id = 1;
  optional string file_name = 2;
  optional string file_path = 3;
  optional string file_format = 4;
  repeated .chesscom.i18n.v1.FileTranslation.TranslationEntriesEntry translation_entries = 8;
  repeated string tags = 9;
  message TranslationEntriesEntry {
  optional string key = 1;
  opt
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06037"></a>
## FND-06037: chesscom.i18n.v1.FileTranslation.file_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string file_name = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1662.

```text
chesscom.i18n.v1.TranslationMetadata translation_metadata = 7;
  }
  optional string file_id = 1;
  optional string file_name = 2;
  optional string file_path = 3;
  optional string file_format = 4;
  repeated .chesscom.i18n.v1.FileTranslation.TranslationEntriesEntry translation_entries = 8;
  repeated string tags = 9;
  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}


```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06038"></a>
## FND-06038: chesscom.i18n.v1.FileTranslation.file_path = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string file_path = 3;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1695.

```text
ata translation_metadata = 7;
  }
  optional string file_id = 1;
  optional string file_name = 2;
  optional string file_path = 3;
  optional string file_format = 4;
  repeated .chesscom.i18n.v1.FileTranslation.TranslationEntriesEntry translation_entries = 8;
  repeated string tags = 9;
  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message TranslationMetadata {
  r
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06039"></a>
## FND-06039: chesscom.i18n.v1.FileTranslation.file_format = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string file_format = 4;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1728.

```text

  optional string file_id = 1;
  optional string file_name = 2;
  optional string file_path = 3;
  optional string file_format = 4;
  repeated .chesscom.i18n.v1.FileTranslation.TranslationEntriesEntry translation_entries = 8;
  repeated string tags = 9;
  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message TranslationMetadata {
  repeated .chesscom.i18n.v1.Transla
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06040"></a>
## FND-06040: chesscom.i18n.v1.FileTranslation.translation_entries = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.i18n.v1.FileTranslation.TranslationEntriesEntry translation_entries = 8;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1763.

```text
ptional string file_name = 2;
  optional string file_path = 3;
  optional string file_format = 4;
  repeated .chesscom.i18n.v1.FileTranslation.TranslationEntriesEntry translation_entries = 8;
  repeated string tags = 9;
  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message TranslationMetadata {
  repeated .chesscom.i18n.v1.TranslationMetadata.CompletionRateEntry co
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06041"></a>
## FND-06041: chesscom.i18n.v1.FileTranslation.tags = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string tags = 9;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1857.

```text
 4;
  repeated .chesscom.i18n.v1.FileTranslation.TranslationEntriesEntry translation_entries = 8;
  repeated string tags = 9;
  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message TranslationMetadata {
  repeated .chesscom.i18n.v1.TranslationMetadata.CompletionRateEntry completion_rate = 1;
  message CompletionRateEntry {
  optional string key = 1;
  optional doubl
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06042"></a>
## FND-06042: message declaration: chesscom.i18n.v1.FileTranslation.TranslationEntriesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TranslationEntriesEntry {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1300.

```text
ce = 3;
  repeated .chesscom.i18n.v1.Translation.TranslationEntriesEntry translation_entries = 7;
  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message FileTranslation {
  oneof _project_id {
  string project_id = 5;
  }
  oneof _resource_id {
  string resource_id = 6;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata 
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06043"></a>
## FND-06043: chesscom.i18n.v1.FileTranslation.TranslationEntriesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 829.

```text
_rates = 3;
  optional double overall_completion_rate = 4;
  message TranslationEntryRatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06044"></a>
## FND-06044: chesscom.i18n.v1.FileTranslation.TranslationEntriesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1363.

```text
riesEntry translation_entries = 7;
  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message FileTranslation {
  oneof _project_id {
  string project_id = 5;
  }
  oneof _resource_id {
  string resource_id = 6;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 7;
  }
  optional string file_id = 1;
  optional string file_
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06045"></a>
## FND-06045: message declaration: chesscom.i18n.v1.TranslationMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TranslationMetadata {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1982.

```text

  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message TranslationMetadata {
  repeated .chesscom.i18n.v1.TranslationMetadata.CompletionRateEntry completion_rate = 1;
  message CompletionRateEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message LanguageDefinition {
  oneof _dialect_of {
  string dialect_of = 14;
  }
  optional string id = 1
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06046"></a>
## FND-06046: chesscom.i18n.v1.TranslationMetadata.completion_rate = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.i18n.v1.TranslationMetadata.CompletionRateEntry completion_rate = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2014.

```text
ry {
  optional string key = 1;
  optional string value = 2;
  }
}

message TranslationMetadata {
  repeated .chesscom.i18n.v1.TranslationMetadata.CompletionRateEntry completion_rate = 1;
  message CompletionRateEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message LanguageDefinition {
  oneof _dialect_of {
  string dialect_of = 14;
  }
  optional string id = 1;
  optional string name = 2;
  
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06047"></a>
## FND-06047: message declaration: chesscom.i18n.v1.TranslationMetadata.CompletionRateEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CompletionRateEntry {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2104.

```text
adata {
  repeated .chesscom.i18n.v1.TranslationMetadata.CompletionRateEntry completion_rate = 1;
  message CompletionRateEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message LanguageDefinition {
  oneof _dialect_of {
  string dialect_of = 14;
  }
  optional string id = 1;
  optional string name = 2;
  optional string editor_code = 3;
  optional string two_letters_code = 4;
  optional string
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06048"></a>
## FND-06048: chesscom.i18n.v1.TranslationMetadata.CompletionRateEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 829.

```text
_rates = 3;
  optional double overall_completion_rate = 4;
  message TranslationEntryRatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06049"></a>
## FND-06049: chesscom.i18n.v1.TranslationMetadata.CompletionRateEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double value = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 856.

```text
le overall_completion_rate = 4;
  message TranslationEntryRatesEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message Translation {
  oneof _project_id {
  string project_id = 4;
  }
  oneof _resource_id {
  string resource_id = 5;
  }
  oneof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06050"></a>
## FND-06050: message declaration: chesscom.i18n.v1.LanguageDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LanguageDefinition {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2197.

```text
= 1;
  message CompletionRateEntry {
  optional string key = 1;
  optional double value = 2;
  }
}

message LanguageDefinition {
  oneof _dialect_of {
  string dialect_of = 14;
  }
  optional string id = 1;
  optional string name = 2;
  optional string editor_code = 3;
  optional string two_letters_code = 4;
  optional string three_letters_code = 5;
  optional string locale = 6;
  optional string android_code = 7;
  
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06051"></a>
## FND-06051: oneof declaration: chesscom.i18n.v1.LanguageDefinition._dialect_of

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _dialect_of {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2228.

```text
try {
  optional string key = 1;
  optional double value = 2;
  }
}

message LanguageDefinition {
  oneof _dialect_of {
  string dialect_of = 14;
  }
  optional string id = 1;
  optional string name = 2;
  optional string editor_code = 3;
  optional string two_letters_code = 4;
  optional string three_letters_code = 5;
  optional string locale = 6;
  optional string android_code = 7;
  optional string osx_code = 8;
 
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06052"></a>
## FND-06052: chesscom.i18n.v1.LanguageDefinition.dialect_of = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string dialect_of = 14;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2250.

```text
g key = 1;
  optional double value = 2;
  }
}

message LanguageDefinition {
  oneof _dialect_of {
  string dialect_of = 14;
  }
  optional string id = 1;
  optional string name = 2;
  optional string editor_code = 3;
  optional string two_letters_code = 4;
  optional string three_letters_code = 5;
  optional string locale = 6;
  optional string android_code = 7;
  optional string osx_code = 8;
  optional string osx_l
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06053"></a>
## FND-06053: chesscom.i18n.v1.LanguageDefinition.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2280.

```text
alue = 2;
  }
}

message LanguageDefinition {
  oneof _dialect_of {
  string dialect_of = 14;
  }
  optional string id = 1;
  optional string name = 2;
  optional string editor_code = 3;
  optional string two_letters_code = 4;
  optional string three_letters_code = 5;
  optional string locale = 6;
  optional string android_code = 7;
  optional string osx_code = 8;
  optional string osx_locale = 9;
  repeated string p
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06054"></a>
## FND-06054: chesscom.i18n.v1.LanguageDefinition.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2306.

```text
anguageDefinition {
  oneof _dialect_of {
  string dialect_of = 14;
  }
  optional string id = 1;
  optional string name = 2;
  optional string editor_code = 3;
  optional string two_letters_code = 4;
  optional string three_letters_code = 5;
  optional string locale = 6;
  optional string android_code = 7;
  optional string osx_code = 8;
  optional string osx_locale = 9;
  repeated string plural_category_names = 10;
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06055"></a>
## FND-06055: chesscom.i18n.v1.LanguageDefinition.editor_code = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string editor_code = 3;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2334.

```text
_dialect_of {
  string dialect_of = 14;
  }
  optional string id = 1;
  optional string name = 2;
  optional string editor_code = 3;
  optional string two_letters_code = 4;
  optional string three_letters_code = 5;
  optional string locale = 6;
  optional string android_code = 7;
  optional string osx_code = 8;
  optional string osx_locale = 9;
  repeated string plural_category_names = 10;
  optional string plural_ru
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06056"></a>
## FND-06056: chesscom.i18n.v1.LanguageDefinition.two_letters_code = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string two_letters_code = 4;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2369.

```text
 14;
  }
  optional string id = 1;
  optional string name = 2;
  optional string editor_code = 3;
  optional string two_letters_code = 4;
  optional string three_letters_code = 5;
  optional string locale = 6;
  optional string android_code = 7;
  optional string osx_code = 8;
  optional string osx_locale = 9;
  repeated string plural_category_names = 10;
  optional string plural_rules = 11;
  repeated string plural_
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06057"></a>
## FND-06057: chesscom.i18n.v1.LanguageDefinition.three_letters_code = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string three_letters_code = 5;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2409.

```text
ional string name = 2;
  optional string editor_code = 3;
  optional string two_letters_code = 4;
  optional string three_letters_code = 5;
  optional string locale = 6;
  optional string android_code = 7;
  optional string osx_code = 8;
  optional string osx_locale = 9;
  repeated string plural_category_names = 10;
  optional string plural_rules = 11;
  repeated string plural_examples = 12;
  optional string text_di
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06058"></a>
## FND-06058: chesscom.i18n.v1.LanguageDefinition.locale = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string locale = 6;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2451.

```text
ditor_code = 3;
  optional string two_letters_code = 4;
  optional string three_letters_code = 5;
  optional string locale = 6;
  optional string android_code = 7;
  optional string osx_code = 8;
  optional string osx_locale = 9;
  repeated string plural_category_names = 10;
  optional string plural_rules = 11;
  repeated string plural_examples = 12;
  optional string text_direction = 13;
}

message UpdateString {
  
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06059"></a>
## FND-06059: chesscom.i18n.v1.LanguageDefinition.android_code = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string android_code = 7;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2481.

```text
ing two_letters_code = 4;
  optional string three_letters_code = 5;
  optional string locale = 6;
  optional string android_code = 7;
  optional string osx_code = 8;
  optional string osx_locale = 9;
  repeated string plural_category_names = 10;
  optional string plural_rules = 11;
  repeated string plural_examples = 12;
  optional string text_direction = 13;
}

message UpdateString {
  optional string string_id = 1;
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06060"></a>
## FND-06060: chesscom.i18n.v1.LanguageDefinition.osx_code = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string osx_code = 8;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2517.

```text
 string three_letters_code = 5;
  optional string locale = 6;
  optional string android_code = 7;
  optional string osx_code = 8;
  optional string osx_locale = 9;
  repeated string plural_category_names = 10;
  optional string plural_rules = 11;
  repeated string plural_examples = 12;
  optional string text_direction = 13;
}

message UpdateString {
  optional string string_id = 1;
  optional string new_value = 2;
}

```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06061"></a>
## FND-06061: chesscom.i18n.v1.LanguageDefinition.osx_locale = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string osx_locale = 9;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2549.

```text
  optional string locale = 6;
  optional string android_code = 7;
  optional string osx_code = 8;
  optional string osx_locale = 9;
  repeated string plural_category_names = 10;
  optional string plural_rules = 11;
  repeated string plural_examples = 12;
  optional string text_direction = 13;
}

message UpdateString {
  optional string string_id = 1;
  optional string new_value = 2;
}

message UpdateFileData {
  opti
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06062"></a>
## FND-06062: chesscom.i18n.v1.LanguageDefinition.plural_category_names = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string plural_category_names = 10;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2583.

```text
tional string android_code = 7;
  optional string osx_code = 8;
  optional string osx_locale = 9;
  repeated string plural_category_names = 10;
  optional string plural_rules = 11;
  repeated string plural_examples = 12;
  optional string text_direction = 13;
}

message UpdateString {
  optional string string_id = 1;
  optional string new_value = 2;
}

message UpdateFileData {
  optional string file_id = 1;
  optiona
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06063"></a>
## FND-06063: chesscom.i18n.v1.LanguageDefinition.plural_rules = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string plural_rules = 11;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2629.

```text
ing osx_code = 8;
  optional string osx_locale = 9;
  repeated string plural_category_names = 10;
  optional string plural_rules = 11;
  repeated string plural_examples = 12;
  optional string text_direction = 13;
}

message UpdateString {
  optional string string_id = 1;
  optional string new_value = 2;
}

message UpdateFileData {
  optional string file_id = 1;
  optional string new_value = 2;
}

message SyncFailure
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06064"></a>
## FND-06064: chesscom.i18n.v1.LanguageDefinition.plural_examples = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string plural_examples = 12;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2666.

```text
sx_locale = 9;
  repeated string plural_category_names = 10;
  optional string plural_rules = 11;
  repeated string plural_examples = 12;
  optional string text_direction = 13;
}

message UpdateString {
  optional string string_id = 1;
  optional string new_value = 2;
}

message UpdateFileData {
  optional string file_id = 1;
  optional string new_value = 2;
}

message SyncFailure {
  optional string file_path = 1;
 
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06065"></a>
## FND-06065: chesscom.i18n.v1.LanguageDefinition.text_direction = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string text_direction = 13;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2706.

```text
category_names = 10;
  optional string plural_rules = 11;
  repeated string plural_examples = 12;
  optional string text_direction = 13;
}

message UpdateString {
  optional string string_id = 1;
  optional string new_value = 2;
}

message UpdateFileData {
  optional string file_id = 1;
  optional string new_value = 2;
}

message SyncFailure {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.FailedSyncEr
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06066"></a>
## FND-06066: message declaration: chesscom.i18n.v1.UpdateString

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UpdateString {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2746.

```text
lural_rules = 11;
  repeated string plural_examples = 12;
  optional string text_direction = 13;
}

message UpdateString {
  optional string string_id = 1;
  optional string new_value = 2;
}

message UpdateFileData {
  optional string file_id = 1;
  optional string new_value = 2;
}

message SyncFailure {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.FailedSyncErrorCode error_code = 2;
  optional strin
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06067"></a>
## FND-06067: chesscom.i18n.v1.UpdateString.string_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string string_id = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1120.

```text
eof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 6;
  }
  optional string string_id = 1;
  optional string key = 2;
  optional string source = 3;
  repeated .chesscom.i18n.v1.Translation.TranslationEntriesEntry translation_entries = 7;
  message TranslationEntriesEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message FileTranslation {
  oneof _project_
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06068"></a>
## FND-06068: chesscom.i18n.v1.UpdateString.new_value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string new_value = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2804.

```text
  optional string text_direction = 13;
}

message UpdateString {
  optional string string_id = 1;
  optional string new_value = 2;
}

message UpdateFileData {
  optional string file_id = 1;
  optional string new_value = 2;
}

message SyncFailure {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.FailedSyncErrorCode error_code = 2;
  optional string error_message = 3;
  repeated string keys = 4;
}

messag
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06069"></a>
## FND-06069: message declaration: chesscom.i18n.v1.UpdateFileData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UpdateFileData {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2838.

```text
 13;
}

message UpdateString {
  optional string string_id = 1;
  optional string new_value = 2;
}

message UpdateFileData {
  optional string file_id = 1;
  optional string new_value = 2;
}

message SyncFailure {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.FailedSyncErrorCode error_code = 2;
  optional string error_message = 3;
  repeated string keys = 4;
}

message SyncWarning {
  optional string 
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06070"></a>
## FND-06070: chesscom.i18n.v1.UpdateFileData.file_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string file_id = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 1631.

```text
eof _translation_metadata {
  .chesscom.i18n.v1.TranslationMetadata translation_metadata = 7;
  }
  optional string file_id = 1;
  optional string file_name = 2;
  optional string file_path = 3;
  optional string file_format = 4;
  repeated .chesscom.i18n.v1.FileTranslation.TranslationEntriesEntry translation_entries = 8;
  repeated string tags = 9;
  message TranslationEntriesEntry {
  optional string key = 1;
  opt
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06071"></a>
## FND-06071: chesscom.i18n.v1.UpdateFileData.new_value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string new_value = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2804.

```text
  optional string text_direction = 13;
}

message UpdateString {
  optional string string_id = 1;
  optional string new_value = 2;
}

message UpdateFileData {
  optional string file_id = 1;
  optional string new_value = 2;
}

message SyncFailure {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.FailedSyncErrorCode error_code = 2;
  optional string error_message = 3;
  repeated string keys = 4;
}

messag
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06072"></a>
## FND-06072: message declaration: chesscom.i18n.v1.SyncFailure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SyncFailure {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2930.

```text
= 2;
}

message UpdateFileData {
  optional string file_id = 1;
  optional string new_value = 2;
}

message SyncFailure {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.FailedSyncErrorCode error_code = 2;
  optional string error_message = 3;
  repeated string keys = 4;
}

message SyncWarning {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.SyncWarningKind kind = 2;
  optional string mess
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06073"></a>
## FND-06073: chesscom.i18n.v1.SyncFailure.file_path = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string file_path = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2954.

```text
leData {
  optional string file_id = 1;
  optional string new_value = 2;
}

message SyncFailure {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.FailedSyncErrorCode error_code = 2;
  optional string error_message = 3;
  repeated string keys = 4;
}

message SyncWarning {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.SyncWarningKind kind = 2;
  optional string message = 3;
  repeated stri
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06074"></a>
## FND-06074: chesscom.i18n.v1.SyncFailure.error_code = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.i18n.v1.FailedSyncErrorCode error_code = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2987.

```text
d = 1;
  optional string new_value = 2;
}

message SyncFailure {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.FailedSyncErrorCode error_code = 2;
  optional string error_message = 3;
  repeated string keys = 4;
}

message SyncWarning {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.SyncWarningKind kind = 2;
  optional string message = 3;
  repeated string keys = 4;
}

```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
