# data_models — findings 701–800

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-00975"></a>
## FND-00975: chesscom.chess.v1.ArrowMarking.color = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.MarkingColor color = 2;

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 331.

```text
ARKING_COLOR_ORANGE = 4;
}

message ArrowMarking {
  optional .chesscom.chess.v1.Arrow arrow = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message SquareMarking {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message BoardMarkings {
  repeated .chesscom.chess.v1.ArrowMarking arrows = 1;
  repeated .chesscom.chess.v1.SquareMarking squares = 2;
```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00968, FND-00969

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00976"></a>
## FND-00976: message declaration: chesscom.chess.v1.SquareMarking

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SquareMarking {

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 386.

```text
tional .chesscom.chess.v1.Arrow arrow = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message SquareMarking {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message BoardMarkings {
  repeated .chesscom.chess.v1.ArrowMarking arrows = 1;
  repeated .chesscom.chess.v1.SquareMarking squares = 2;
}

```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00968, FND-00969

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00977"></a>
## FND-00977: chesscom.chess.v1.SquareMarking.square = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square square = 1;

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 412.

```text
Arrow arrow = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message SquareMarking {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message BoardMarkings {
  repeated .chesscom.chess.v1.ArrowMarking arrows = 1;
  repeated .chesscom.chess.v1.SquareMarking squares = 2;
}

```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00968, FND-00969

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00978"></a>
## FND-00978: chesscom.chess.v1.SquareMarking.color = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.MarkingColor color = 2;

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 331.

```text
ARKING_COLOR_ORANGE = 4;
}

message ArrowMarking {
  optional .chesscom.chess.v1.Arrow arrow = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message SquareMarking {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message BoardMarkings {
  repeated .chesscom.chess.v1.ArrowMarking arrows = 1;
  repeated .chesscom.chess.v1.SquareMarking squares = 2;
```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00968, FND-00969

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00979"></a>
## FND-00979: message declaration: chesscom.chess.v1.BoardMarkings

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BoardMarkings {

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 516.

```text
onal .chesscom.chess.v1.Square square = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message BoardMarkings {
  repeated .chesscom.chess.v1.ArrowMarking arrows = 1;
  repeated .chesscom.chess.v1.SquareMarking squares = 2;
}

```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00968, FND-00969

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00980"></a>
## FND-00980: chesscom.chess.v1.BoardMarkings.arrows = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.ArrowMarking arrows = 1;

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 542.

```text
uare square = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message BoardMarkings {
  repeated .chesscom.chess.v1.ArrowMarking arrows = 1;
  repeated .chesscom.chess.v1.SquareMarking squares = 2;
}

```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00968, FND-00969

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00981"></a>
## FND-00981: chesscom.chess.v1.BoardMarkings.squares = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.SquareMarking squares = 2;

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 597.

```text
olor color = 2;
}

message BoardMarkings {
  repeated .chesscom.chess.v1.ArrowMarking arrows = 1;
  repeated .chesscom.chess.v1.SquareMarking squares = 2;
}

```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00968, FND-00969

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00982"></a>
## FND-00982: enum declaration: chesscom.chess.v1.ChesscomGameSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ChesscomGameSource {

### Evidence

- **SRC-0242** `research/proto/chesscom/chess/v1/chesscom_game_source.proto` — [preserved redacted evidence](../evidence/text/9c615e9e5f93b8946ab479a5449e8a5ceb69e1032e8446264cf55e5fb6e6c2c1.proto)
  Character offset 103.

```text
source: chesscom/chess/v1/chesscom_game_source.proto
// syntax: proto3

package chesscom.chess.v1;

enum ChesscomGameSource {
  CHESSCOM_GAME_SOURCE_UNSPECIFIED = 0;
  CHESSCOM_GAME_SOURCE_DAILY = 1;
  CHESSCOM_GAME_SOURCE_LIVE = 2;
  CHESSCOM_GAME_SOURCE_MASTER = 3;
  CHESSCOM_GAME_SOURCE_PGN = 4;
  CHESSCOM_GAME_SOURCE_VS_COMPUTER = 5;
  CHESSCOM_GAME_SOURCE_VS_COACH = 6;
}

```

**Source references:** SRC-0242, SRC-1213  
**URL references:** None independently associated  
**Related findings:** FND-00983, FND-00984

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00983"></a>
## FND-00983: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESSCOM_GAME_SOURCE_UNSPECIFIED = 0;

### Evidence

- **SRC-0242** `research/proto/chesscom/chess/v1/chesscom_game_source.proto` — [preserved redacted evidence](../evidence/text/9c615e9e5f93b8946ab479a5449e8a5ceb69e1032e8446264cf55e5fb6e6c2c1.proto)
  Character offset 131.

```text
esscom_game_source.proto
// syntax: proto3

package chesscom.chess.v1;

enum ChesscomGameSource {
  CHESSCOM_GAME_SOURCE_UNSPECIFIED = 0;
  CHESSCOM_GAME_SOURCE_DAILY = 1;
  CHESSCOM_GAME_SOURCE_LIVE = 2;
  CHESSCOM_GAME_SOURCE_MASTER = 3;
  CHESSCOM_GAME_SOURCE_PGN = 4;
  CHESSCOM_GAME_SOURCE_VS_COMPUTER = 5;
  CHESSCOM_GAME_SOURCE_VS_COACH = 6;
}

```

**Source references:** SRC-0242, SRC-1213  
**URL references:** None independently associated  
**Related findings:** FND-00982, FND-00984

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00984"></a>
## FND-00984: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_DAILY = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESSCOM_GAME_SOURCE_DAILY = 1;

### Evidence

- **SRC-0242** `research/proto/chesscom/chess/v1/chesscom_game_source.proto` — [preserved redacted evidence](../evidence/text/9c615e9e5f93b8946ab479a5449e8a5ceb69e1032e8446264cf55e5fb6e6c2c1.proto)
  Character offset 171.

```text
o3

package chesscom.chess.v1;

enum ChesscomGameSource {
  CHESSCOM_GAME_SOURCE_UNSPECIFIED = 0;
  CHESSCOM_GAME_SOURCE_DAILY = 1;
  CHESSCOM_GAME_SOURCE_LIVE = 2;
  CHESSCOM_GAME_SOURCE_MASTER = 3;
  CHESSCOM_GAME_SOURCE_PGN = 4;
  CHESSCOM_GAME_SOURCE_VS_COMPUTER = 5;
  CHESSCOM_GAME_SOURCE_VS_COACH = 6;
}

```

**Source references:** SRC-0242, SRC-1213  
**URL references:** None independently associated  
**Related findings:** FND-00982, FND-00983

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00985"></a>
## FND-00985: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_LIVE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESSCOM_GAME_SOURCE_LIVE = 2;

### Evidence

- **SRC-0242** `research/proto/chesscom/chess/v1/chesscom_game_source.proto` — [preserved redacted evidence](../evidence/text/9c615e9e5f93b8946ab479a5449e8a5ceb69e1032e8446264cf55e5fb6e6c2c1.proto)
  Character offset 205.

```text
um ChesscomGameSource {
  CHESSCOM_GAME_SOURCE_UNSPECIFIED = 0;
  CHESSCOM_GAME_SOURCE_DAILY = 1;
  CHESSCOM_GAME_SOURCE_LIVE = 2;
  CHESSCOM_GAME_SOURCE_MASTER = 3;
  CHESSCOM_GAME_SOURCE_PGN = 4;
  CHESSCOM_GAME_SOURCE_VS_COMPUTER = 5;
  CHESSCOM_GAME_SOURCE_VS_COACH = 6;
}

```

**Source references:** SRC-0242, SRC-1213  
**URL references:** None independently associated  
**Related findings:** FND-00982, FND-00983, FND-00984

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00986"></a>
## FND-00986: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_MASTER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESSCOM_GAME_SOURCE_MASTER = 3;

### Evidence

- **SRC-0242** `research/proto/chesscom/chess/v1/chesscom_game_source.proto` — [preserved redacted evidence](../evidence/text/9c615e9e5f93b8946ab479a5449e8a5ceb69e1032e8446264cf55e5fb6e6c2c1.proto)
  Character offset 238.

```text
M_GAME_SOURCE_UNSPECIFIED = 0;
  CHESSCOM_GAME_SOURCE_DAILY = 1;
  CHESSCOM_GAME_SOURCE_LIVE = 2;
  CHESSCOM_GAME_SOURCE_MASTER = 3;
  CHESSCOM_GAME_SOURCE_PGN = 4;
  CHESSCOM_GAME_SOURCE_VS_COMPUTER = 5;
  CHESSCOM_GAME_SOURCE_VS_COACH = 6;
}

```

**Source references:** SRC-0242, SRC-1213  
**URL references:** None independently associated  
**Related findings:** FND-00982, FND-00983, FND-00984

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00987"></a>
## FND-00987: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_PGN = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESSCOM_GAME_SOURCE_PGN = 4;

### Evidence

- **SRC-0242** `research/proto/chesscom/chess/v1/chesscom_game_source.proto` — [preserved redacted evidence](../evidence/text/9c615e9e5f93b8946ab479a5449e8a5ceb69e1032e8446264cf55e5fb6e6c2c1.proto)
  Character offset 273.

```text
ESSCOM_GAME_SOURCE_DAILY = 1;
  CHESSCOM_GAME_SOURCE_LIVE = 2;
  CHESSCOM_GAME_SOURCE_MASTER = 3;
  CHESSCOM_GAME_SOURCE_PGN = 4;
  CHESSCOM_GAME_SOURCE_VS_COMPUTER = 5;
  CHESSCOM_GAME_SOURCE_VS_COACH = 6;
}

```

**Source references:** SRC-0242, SRC-1213  
**URL references:** None independently associated  
**Related findings:** FND-00982, FND-00983, FND-00984

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00988"></a>
## FND-00988: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_VS_COMPUTER = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESSCOM_GAME_SOURCE_VS_COMPUTER = 5;

### Evidence

- **SRC-0242** `research/proto/chesscom/chess/v1/chesscom_game_source.proto` — [preserved redacted evidence](../evidence/text/9c615e9e5f93b8946ab479a5449e8a5ceb69e1032e8446264cf55e5fb6e6c2c1.proto)
  Character offset 305.

```text
CHESSCOM_GAME_SOURCE_LIVE = 2;
  CHESSCOM_GAME_SOURCE_MASTER = 3;
  CHESSCOM_GAME_SOURCE_PGN = 4;
  CHESSCOM_GAME_SOURCE_VS_COMPUTER = 5;
  CHESSCOM_GAME_SOURCE_VS_COACH = 6;
}

```

**Source references:** SRC-0242, SRC-1213  
**URL references:** None independently associated  
**Related findings:** FND-00982, FND-00983, FND-00984

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00989"></a>
## FND-00989: chesscom.chess.v1.ChesscomGameSource.CHESSCOM_GAME_SOURCE_VS_COACH = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESSCOM_GAME_SOURCE_VS_COACH = 6;

### Evidence

- **SRC-0242** `research/proto/chesscom/chess/v1/chesscom_game_source.proto` — [preserved redacted evidence](../evidence/text/9c615e9e5f93b8946ab479a5449e8a5ceb69e1032e8446264cf55e5fb6e6c2c1.proto)
  Character offset 345.

```text
M_GAME_SOURCE_MASTER = 3;
  CHESSCOM_GAME_SOURCE_PGN = 4;
  CHESSCOM_GAME_SOURCE_VS_COMPUTER = 5;
  CHESSCOM_GAME_SOURCE_VS_COACH = 6;
}

```

**Source references:** SRC-0242, SRC-1213  
**URL references:** None independently associated  
**Related findings:** FND-00982, FND-00983, FND-00984

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00990"></a>
## FND-00990: enum declaration: chesscom.chess.v1.Color

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Color {

### Evidence

- **SRC-0243** `research/proto/chesscom/chess/v1/color.proto` — [preserved redacted evidence](../evidence/text/8c010e011b29ce3b89f14be2c10705f32d6ede2db1c8089115ea113fbcbf6bc2.proto)
  Character offset 88.

```text
// source: chesscom/chess/v1/color.proto
// syntax: proto3

package chesscom.chess.v1;

enum Color {
  COLOR_UNSPECIFIED = 0;
  COLOR_WHITE = 1;
  COLOR_BLACK = 2;
}

```

**Source references:** SRC-0243, SRC-1214  
**URL references:** None independently associated  
**Related findings:** FND-00991, FND-00992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00991"></a>
## FND-00991: chesscom.chess.v1.Color.COLOR_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COLOR_UNSPECIFIED = 0;

### Evidence

- **SRC-0243** `research/proto/chesscom/chess/v1/color.proto` — [preserved redacted evidence](../evidence/text/8c010e011b29ce3b89f14be2c10705f32d6ede2db1c8089115ea113fbcbf6bc2.proto)
  Character offset 103.

```text
source: chesscom/chess/v1/color.proto
// syntax: proto3

package chesscom.chess.v1;

enum Color {
  COLOR_UNSPECIFIED = 0;
  COLOR_WHITE = 1;
  COLOR_BLACK = 2;
}

```

**Source references:** SRC-0243, SRC-1214  
**URL references:** None independently associated  
**Related findings:** FND-00990, FND-00992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00992"></a>
## FND-00992: chesscom.chess.v1.Color.COLOR_WHITE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COLOR_WHITE = 1;

### Evidence

- **SRC-0243** `research/proto/chesscom/chess/v1/color.proto` — [preserved redacted evidence](../evidence/text/8c010e011b29ce3b89f14be2c10705f32d6ede2db1c8089115ea113fbcbf6bc2.proto)
  Character offset 128.

```text
/color.proto
// syntax: proto3

package chesscom.chess.v1;

enum Color {
  COLOR_UNSPECIFIED = 0;
  COLOR_WHITE = 1;
  COLOR_BLACK = 2;
}

```

**Source references:** SRC-0243, SRC-1214  
**URL references:** None independently associated  
**Related findings:** FND-00990, FND-00991

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00993"></a>
## FND-00993: chesscom.chess.v1.Color.COLOR_BLACK = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COLOR_BLACK = 2;

### Evidence

- **SRC-0243** `research/proto/chesscom/chess/v1/color.proto` — [preserved redacted evidence](../evidence/text/8c010e011b29ce3b89f14be2c10705f32d6ede2db1c8089115ea113fbcbf6bc2.proto)
  Character offset 147.

```text
tax: proto3

package chesscom.chess.v1;

enum Color {
  COLOR_UNSPECIFIED = 0;
  COLOR_WHITE = 1;
  COLOR_BLACK = 2;
}

```

**Source references:** SRC-0243, SRC-1214  
**URL references:** None independently associated  
**Related findings:** FND-00990, FND-00991, FND-00992

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00994"></a>
## FND-00994: message declaration: chesscom.chess.v1.EcoFamily

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EcoFamily {

### Evidence

- **SRC-0244** `research/proto/chesscom/chess/v1/eco.proto` — [preserved redacted evidence](../evidence/text/1bca77717c8c695f8b0f904c4afd4b8dbd34cc13e1f452ca26c99897f0e99f43.proto)
  Character offset 86.

```text
// source: chesscom/chess/v1/eco.proto
// syntax: proto3

package chesscom.chess.v1;

message EcoFamily {
  optional uint32 eco_family_id = 1;
  optional string name = 2;
}

```

**Source references:** SRC-0244, SRC-1215  
**URL references:** None independently associated  
**Related findings:** FND-00995, FND-00996

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00995"></a>
## FND-00995: chesscom.chess.v1.EcoFamily.eco_family_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 eco_family_id = 1;

### Evidence

- **SRC-0244** `research/proto/chesscom/chess/v1/eco.proto` — [preserved redacted evidence](../evidence/text/1bca77717c8c695f8b0f904c4afd4b8dbd34cc13e1f452ca26c99897f0e99f43.proto)
  Character offset 108.

```text
e: chesscom/chess/v1/eco.proto
// syntax: proto3

package chesscom.chess.v1;

message EcoFamily {
  optional uint32 eco_family_id = 1;
  optional string name = 2;
}

```

**Source references:** SRC-0244, SRC-1215  
**URL references:** None independently associated  
**Related findings:** FND-00994, FND-00996

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00996"></a>
## FND-00996: chesscom.chess.v1.EcoFamily.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0244** `research/proto/chesscom/chess/v1/eco.proto` — [preserved redacted evidence](../evidence/text/1bca77717c8c695f8b0f904c4afd4b8dbd34cc13e1f452ca26c99897f0e99f43.proto)
  Character offset 145.

```text
tax: proto3

package chesscom.chess.v1;

message EcoFamily {
  optional uint32 eco_family_id = 1;
  optional string name = 2;
}

```

**Source references:** SRC-0244, SRC-1215  
**URL references:** None independently associated  
**Related findings:** FND-00994, FND-00995

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00997"></a>
## FND-00997: enum declaration: chesscom.chess.v1.File

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum File {

### Evidence

- **SRC-0245** `research/proto/chesscom/chess/v1/file.proto` — [preserved redacted evidence](../evidence/text/7fd9803c0ee5746c4f39c77345e18561dfe4aae010630c8b46f0449cd0c62747.proto)
  Character offset 87.

```text
// source: chesscom/chess/v1/file.proto
// syntax: proto3

package chesscom.chess.v1;

enum File {
  FILE_UNSPECIFIED = 0;
  FILE_A = 1;
  FILE_B = 2;
  FILE_C = 3;
  FILE_D = 4;
  FILE_E = 5;
  FILE_F = 6;
  FILE_G = 7;
  FILE_H = 8;
}

```

**Source references:** SRC-0245, SRC-1216  
**URL references:** None independently associated  
**Related findings:** FND-00998, FND-00999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00998"></a>
## FND-00998: chesscom.chess.v1.File.FILE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FILE_UNSPECIFIED = 0;

### Evidence

- **SRC-0245** `research/proto/chesscom/chess/v1/file.proto` — [preserved redacted evidence](../evidence/text/7fd9803c0ee5746c4f39c77345e18561dfe4aae010630c8b46f0449cd0c62747.proto)
  Character offset 101.

```text
/ source: chesscom/chess/v1/file.proto
// syntax: proto3

package chesscom.chess.v1;

enum File {
  FILE_UNSPECIFIED = 0;
  FILE_A = 1;
  FILE_B = 2;
  FILE_C = 3;
  FILE_D = 4;
  FILE_E = 5;
  FILE_F = 6;
  FILE_G = 7;
  FILE_H = 8;
}

```

**Source references:** SRC-0245, SRC-1216  
**URL references:** None independently associated  
**Related findings:** FND-00997, FND-00999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00999"></a>
## FND-00999: chesscom.chess.v1.File.FILE_A = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FILE_A = 1;

### Evidence

- **SRC-0245** `research/proto/chesscom/chess/v1/file.proto` — [preserved redacted evidence](../evidence/text/7fd9803c0ee5746c4f39c77345e18561dfe4aae010630c8b46f0449cd0c62747.proto)
  Character offset 125.

```text
/v1/file.proto
// syntax: proto3

package chesscom.chess.v1;

enum File {
  FILE_UNSPECIFIED = 0;
  FILE_A = 1;
  FILE_B = 2;
  FILE_C = 3;
  FILE_D = 4;
  FILE_E = 5;
  FILE_F = 6;
  FILE_G = 7;
  FILE_H = 8;
}

```

**Source references:** SRC-0245, SRC-1216  
**URL references:** None independently associated  
**Related findings:** FND-00997, FND-00998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01000"></a>
## FND-01000: chesscom.chess.v1.File.FILE_B = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FILE_B = 2;

### Evidence

- **SRC-0245** `research/proto/chesscom/chess/v1/file.proto` — [preserved redacted evidence](../evidence/text/7fd9803c0ee5746c4f39c77345e18561dfe4aae010630c8b46f0449cd0c62747.proto)
  Character offset 139.

```text

// syntax: proto3

package chesscom.chess.v1;

enum File {
  FILE_UNSPECIFIED = 0;
  FILE_A = 1;
  FILE_B = 2;
  FILE_C = 3;
  FILE_D = 4;
  FILE_E = 5;
  FILE_F = 6;
  FILE_G = 7;
  FILE_H = 8;
}

```

**Source references:** SRC-0245, SRC-1216  
**URL references:** None independently associated  
**Related findings:** FND-00997, FND-00998, FND-00999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01001"></a>
## FND-01001: chesscom.chess.v1.File.FILE_C = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FILE_C = 3;

### Evidence

- **SRC-0245** `research/proto/chesscom/chess/v1/file.proto` — [preserved redacted evidence](../evidence/text/7fd9803c0ee5746c4f39c77345e18561dfe4aae010630c8b46f0449cd0c62747.proto)
  Character offset 153.

```text
oto3

package chesscom.chess.v1;

enum File {
  FILE_UNSPECIFIED = 0;
  FILE_A = 1;
  FILE_B = 2;
  FILE_C = 3;
  FILE_D = 4;
  FILE_E = 5;
  FILE_F = 6;
  FILE_G = 7;
  FILE_H = 8;
}

```

**Source references:** SRC-0245, SRC-1216  
**URL references:** None independently associated  
**Related findings:** FND-00997, FND-00998, FND-00999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01002"></a>
## FND-01002: chesscom.chess.v1.File.FILE_D = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FILE_D = 4;

### Evidence

- **SRC-0245** `research/proto/chesscom/chess/v1/file.proto` — [preserved redacted evidence](../evidence/text/7fd9803c0ee5746c4f39c77345e18561dfe4aae010630c8b46f0449cd0c62747.proto)
  Character offset 167.

```text
chesscom.chess.v1;

enum File {
  FILE_UNSPECIFIED = 0;
  FILE_A = 1;
  FILE_B = 2;
  FILE_C = 3;
  FILE_D = 4;
  FILE_E = 5;
  FILE_F = 6;
  FILE_G = 7;
  FILE_H = 8;
}

```

**Source references:** SRC-0245, SRC-1216  
**URL references:** None independently associated  
**Related findings:** FND-00997, FND-00998, FND-00999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01003"></a>
## FND-01003: chesscom.chess.v1.File.FILE_E = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FILE_E = 5;

### Evidence

- **SRC-0245** `research/proto/chesscom/chess/v1/file.proto` — [preserved redacted evidence](../evidence/text/7fd9803c0ee5746c4f39c77345e18561dfe4aae010630c8b46f0449cd0c62747.proto)
  Character offset 181.

```text
.v1;

enum File {
  FILE_UNSPECIFIED = 0;
  FILE_A = 1;
  FILE_B = 2;
  FILE_C = 3;
  FILE_D = 4;
  FILE_E = 5;
  FILE_F = 6;
  FILE_G = 7;
  FILE_H = 8;
}

```

**Source references:** SRC-0245, SRC-1216  
**URL references:** None independently associated  
**Related findings:** FND-00997, FND-00998, FND-00999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01004"></a>
## FND-01004: chesscom.chess.v1.File.FILE_F = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FILE_F = 6;

### Evidence

- **SRC-0245** `research/proto/chesscom/chess/v1/file.proto` — [preserved redacted evidence](../evidence/text/7fd9803c0ee5746c4f39c77345e18561dfe4aae010630c8b46f0449cd0c62747.proto)
  Character offset 195.

```text
e {
  FILE_UNSPECIFIED = 0;
  FILE_A = 1;
  FILE_B = 2;
  FILE_C = 3;
  FILE_D = 4;
  FILE_E = 5;
  FILE_F = 6;
  FILE_G = 7;
  FILE_H = 8;
}

```

**Source references:** SRC-0245, SRC-1216  
**URL references:** None independently associated  
**Related findings:** FND-00997, FND-00998, FND-00999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01005"></a>
## FND-01005: chesscom.chess.v1.File.FILE_G = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FILE_G = 7;

### Evidence

- **SRC-0245** `research/proto/chesscom/chess/v1/file.proto` — [preserved redacted evidence](../evidence/text/7fd9803c0ee5746c4f39c77345e18561dfe4aae010630c8b46f0449cd0c62747.proto)
  Character offset 209.

```text
PECIFIED = 0;
  FILE_A = 1;
  FILE_B = 2;
  FILE_C = 3;
  FILE_D = 4;
  FILE_E = 5;
  FILE_F = 6;
  FILE_G = 7;
  FILE_H = 8;
}

```

**Source references:** SRC-0245, SRC-1216  
**URL references:** None independently associated  
**Related findings:** FND-00997, FND-00998, FND-00999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01006"></a>
## FND-01006: chesscom.chess.v1.File.FILE_H = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FILE_H = 8;

### Evidence

- **SRC-0245** `research/proto/chesscom/chess/v1/file.proto` — [preserved redacted evidence](../evidence/text/7fd9803c0ee5746c4f39c77345e18561dfe4aae010630c8b46f0449cd0c62747.proto)
  Character offset 223.

```text
  FILE_A = 1;
  FILE_B = 2;
  FILE_C = 3;
  FILE_D = 4;
  FILE_E = 5;
  FILE_F = 6;
  FILE_G = 7;
  FILE_H = 8;
}

```

**Source references:** SRC-0245, SRC-1216  
**URL references:** None independently associated  
**Related findings:** FND-00997, FND-00998, FND-00999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01007"></a>
## FND-01007: message declaration: chesscom.chess.v1.GameResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameResult {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 87.

```text
// source: chesscom/chess/v1/game.proto
// syntax: proto3

package chesscom.chess.v1;

message GameResult {
  optional .chesscom.chess.v1.Result result = 1;
  optional .chesscom.chess.v1.ResultType result_type = 2;
}

message Game {
  optional .chesscom.chess.v1.Position starting_position = 1;
  repeated .chesscom.chess.v1.GameMove moves = 2;
  optional .chesscom.chess.v1.GameMetadata metadata = 3;
}

me
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01008"></a>
## FND-01008: chesscom.chess.v1.GameResult.result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Result result = 1;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 110.

```text
 chesscom/chess/v1/game.proto
// syntax: proto3

package chesscom.chess.v1;

message GameResult {
  optional .chesscom.chess.v1.Result result = 1;
  optional .chesscom.chess.v1.ResultType result_type = 2;
}

message Game {
  optional .chesscom.chess.v1.Position starting_position = 1;
  repeated .chesscom.chess.v1.GameMove moves = 2;
  optional .chesscom.chess.v1.GameMetadata metadata = 3;
}

message GameMove {
  oneo
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01009"></a>
## FND-01009: chesscom.chess.v1.GameResult.result_type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.ResultType result_type = 2;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 159.

```text
package chesscom.chess.v1;

message GameResult {
  optional .chesscom.chess.v1.Result result = 1;
  optional .chesscom.chess.v1.ResultType result_type = 2;
}

message Game {
  optional .chesscom.chess.v1.Position starting_position = 1;
  repeated .chesscom.chess.v1.GameMove moves = 2;
  optional .chesscom.chess.v1.GameMetadata metadata = 3;
}

message GameMove {
  oneof _metadata {
  .chesscom.chess.v1.GameMoveMetada
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01010"></a>
## FND-01010: message declaration: chesscom.chess.v1.Game

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Game {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 218.

```text
 .chesscom.chess.v1.Result result = 1;
  optional .chesscom.chess.v1.ResultType result_type = 2;
}

message Game {
  optional .chesscom.chess.v1.Position starting_position = 1;
  repeated .chesscom.chess.v1.GameMove moves = 2;
  optional .chesscom.chess.v1.GameMetadata metadata = 3;
}

message GameMove {
  oneof _metadata {
  .chesscom.chess.v1.GameMoveMetadata metadata = 2;
  }
  optional .chesscom.chess.v1.Move mov
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01011"></a>
## FND-01011: chesscom.chess.v1.Game.starting_position = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Position starting_position = 1;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 235.

```text
v1.Result result = 1;
  optional .chesscom.chess.v1.ResultType result_type = 2;
}

message Game {
  optional .chesscom.chess.v1.Position starting_position = 1;
  repeated .chesscom.chess.v1.GameMove moves = 2;
  optional .chesscom.chess.v1.GameMetadata metadata = 3;
}

message GameMove {
  oneof _metadata {
  .chesscom.chess.v1.GameMoveMetadata metadata = 2;
  }
  optional .chesscom.chess.v1.Move move = 1;
  repeated
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01012"></a>
## FND-01012: chesscom.chess.v1.Game.moves = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.GameMove moves = 2;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 297.

```text
 result_type = 2;
}

message Game {
  optional .chesscom.chess.v1.Position starting_position = 1;
  repeated .chesscom.chess.v1.GameMove moves = 2;
  optional .chesscom.chess.v1.GameMetadata metadata = 3;
}

message GameMove {
  oneof _metadata {
  .chesscom.chess.v1.GameMoveMetadata metadata = 2;
  }
  optional .chesscom.chess.v1.Move move = 1;
  repeated .chesscom.chess.v1.MoveVariation variations = 3;
}

message G
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01013"></a>
## FND-01013: chesscom.chess.v1.Game.metadata = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.GameMetadata metadata = 3;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 347.

```text
esscom.chess.v1.Position starting_position = 1;
  repeated .chesscom.chess.v1.GameMove moves = 2;
  optional .chesscom.chess.v1.GameMetadata metadata = 3;
}

message GameMove {
  oneof _metadata {
  .chesscom.chess.v1.GameMoveMetadata metadata = 2;
  }
  optional .chesscom.chess.v1.Move move = 1;
  repeated .chesscom.chess.v1.MoveVariation variations = 3;
}

message GameMoveMetadata {
  oneof _score {
  .chesscom.che
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01014"></a>
## FND-01014: message declaration: chesscom.chess.v1.GameMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameMove {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 405.

```text
 .chesscom.chess.v1.GameMove moves = 2;
  optional .chesscom.chess.v1.GameMetadata metadata = 3;
}

message GameMove {
  oneof _metadata {
  .chesscom.chess.v1.GameMoveMetadata metadata = 2;
  }
  optional .chesscom.chess.v1.Move move = 1;
  repeated .chesscom.chess.v1.MoveVariation variations = 3;
}

message GameMoveMetadata {
  oneof _score {
  .chesscom.chess.v1.Score score = 1;
  }
  oneof _time_remaining_ms {
  
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01015"></a>
## FND-01015: oneof declaration: chesscom.chess.v1.GameMove._metadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _metadata {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 426.

```text
ameMove moves = 2;
  optional .chesscom.chess.v1.GameMetadata metadata = 3;
}

message GameMove {
  oneof _metadata {
  .chesscom.chess.v1.GameMoveMetadata metadata = 2;
  }
  optional .chesscom.chess.v1.Move move = 1;
  repeated .chesscom.chess.v1.MoveVariation variations = 3;
}

message GameMoveMetadata {
  oneof _score {
  .chesscom.chess.v1.Score score = 1;
  }
  oneof _time_remaining_ms {
  uint32 time_remaining
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01016"></a>
## FND-01016: chesscom.chess.v1.GameMove.metadata = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.GameMoveMetadata metadata = 2;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 446.

```text
 optional .chesscom.chess.v1.GameMetadata metadata = 3;
}

message GameMove {
  oneof _metadata {
  .chesscom.chess.v1.GameMoveMetadata metadata = 2;
  }
  optional .chesscom.chess.v1.Move move = 1;
  repeated .chesscom.chess.v1.MoveVariation variations = 3;
}

message GameMoveMetadata {
  oneof _score {
  .chesscom.chess.v1.Score score = 1;
  }
  oneof _time_remaining_ms {
  uint32 time_remaining_ms = 2;
  }
  oneof
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01017"></a>
## FND-01017: chesscom.chess.v1.GameMove.move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move move = 1;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 502.

```text
}

message GameMove {
  oneof _metadata {
  .chesscom.chess.v1.GameMoveMetadata metadata = 2;
  }
  optional .chesscom.chess.v1.Move move = 1;
  repeated .chesscom.chess.v1.MoveVariation variations = 3;
}

message GameMoveMetadata {
  oneof _score {
  .chesscom.chess.v1.Score score = 1;
  }
  oneof _time_remaining_ms {
  uint32 time_remaining_ms = 2;
  }
  oneof _comment_before {
  string comment_before = 3;
  }
  re
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01018"></a>
## FND-01018: chesscom.chess.v1.GameMove.variations = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.MoveVariation variations = 3;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 547.

```text
chesscom.chess.v1.GameMoveMetadata metadata = 2;
  }
  optional .chesscom.chess.v1.Move move = 1;
  repeated .chesscom.chess.v1.MoveVariation variations = 3;
}

message GameMoveMetadata {
  oneof _score {
  .chesscom.chess.v1.Score score = 1;
  }
  oneof _time_remaining_ms {
  uint32 time_remaining_ms = 2;
  }
  oneof _comment_before {
  string comment_before = 3;
  }
  repeated string comments_after = 4;
  repeated 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01019"></a>
## FND-01019: message declaration: chesscom.chess.v1.GameMoveMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameMoveMetadata {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 608.

```text
al .chesscom.chess.v1.Move move = 1;
  repeated .chesscom.chess.v1.MoveVariation variations = 3;
}

message GameMoveMetadata {
  oneof _score {
  .chesscom.chess.v1.Score score = 1;
  }
  oneof _time_remaining_ms {
  uint32 time_remaining_ms = 2;
  }
  oneof _comment_before {
  string comment_before = 3;
  }
  repeated string comments_after = 4;
  repeated uint32 nags = 5;
}

message MoveVariation {
  repeated .chess
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01020"></a>
## FND-01020: oneof declaration: chesscom.chess.v1.GameMoveMetadata._score

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _score {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 637.

```text
ve = 1;
  repeated .chesscom.chess.v1.MoveVariation variations = 3;
}

message GameMoveMetadata {
  oneof _score {
  .chesscom.chess.v1.Score score = 1;
  }
  oneof _time_remaining_ms {
  uint32 time_remaining_ms = 2;
  }
  oneof _comment_before {
  string comment_before = 3;
  }
  repeated string comments_after = 4;
  repeated uint32 nags = 5;
}

message MoveVariation {
  repeated .chesscom.chess.v1.GameMove moves =
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01021"></a>
## FND-01021: chesscom.chess.v1.GameMoveMetadata.score = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Score score = 1;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 654.

```text
d .chesscom.chess.v1.MoveVariation variations = 3;
}

message GameMoveMetadata {
  oneof _score {
  .chesscom.chess.v1.Score score = 1;
  }
  oneof _time_remaining_ms {
  uint32 time_remaining_ms = 2;
  }
  oneof _comment_before {
  string comment_before = 3;
  }
  repeated string comments_after = 4;
  repeated uint32 nags = 5;
}

message MoveVariation {
  repeated .chesscom.chess.v1.GameMove moves = 1;
}

message Ru
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01022"></a>
## FND-01022: oneof declaration: chesscom.chess.v1.GameMoveMetadata._time_remaining_ms

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_remaining_ms {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 696.

```text
ons = 3;
}

message GameMoveMetadata {
  oneof _score {
  .chesscom.chess.v1.Score score = 1;
  }
  oneof _time_remaining_ms {
  uint32 time_remaining_ms = 2;
  }
  oneof _comment_before {
  string comment_before = 3;
  }
  repeated string comments_after = 4;
  repeated uint32 nags = 5;
}

message MoveVariation {
  repeated .chesscom.chess.v1.GameMove moves = 1;
}

message Rules {
  oneof _is_chess960 {
  bool is_che
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01023"></a>
## FND-01023: chesscom.chess.v1.GameMoveMetadata.time_remaining_ms = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 time_remaining_ms = 2;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 725.

```text
etadata {
  oneof _score {
  .chesscom.chess.v1.Score score = 1;
  }
  oneof _time_remaining_ms {
  uint32 time_remaining_ms = 2;
  }
  oneof _comment_before {
  string comment_before = 3;
  }
  repeated string comments_after = 4;
  repeated uint32 nags = 5;
}

message MoveVariation {
  repeated .chesscom.chess.v1.GameMove moves = 1;
}

message Rules {
  oneof _is_chess960 {
  bool is_chess960 = 1;
  }
}

message Gam
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01024"></a>
## FND-01024: oneof declaration: chesscom.chess.v1.GameMoveMetadata._comment_before

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _comment_before {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 761.

```text
om.chess.v1.Score score = 1;
  }
  oneof _time_remaining_ms {
  uint32 time_remaining_ms = 2;
  }
  oneof _comment_before {
  string comment_before = 3;
  }
  repeated string comments_after = 4;
  repeated uint32 nags = 5;
}

message MoveVariation {
  repeated .chesscom.chess.v1.GameMove moves = 1;
}

message Rules {
  oneof _is_chess960 {
  bool is_chess960 = 1;
  }
}

message GameMetadata {
  oneof _time_control {

```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01025"></a>
## FND-01025: chesscom.chess.v1.GameMoveMetadata.comment_before = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string comment_before = 3;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 787.

```text
1;
  }
  oneof _time_remaining_ms {
  uint32 time_remaining_ms = 2;
  }
  oneof _comment_before {
  string comment_before = 3;
  }
  repeated string comments_after = 4;
  repeated uint32 nags = 5;
}

message MoveVariation {
  repeated .chesscom.chess.v1.GameMove moves = 1;
}

message Rules {
  oneof _is_chess960 {
  bool is_chess960 = 1;
  }
}

message GameMetadata {
  oneof _time_control {
  .chesscom.chess.v1.TimeC
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01026"></a>
## FND-01026: chesscom.chess.v1.GameMoveMetadata.comments_after = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string comments_after = 4;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 820.

```text
 {
  uint32 time_remaining_ms = 2;
  }
  oneof _comment_before {
  string comment_before = 3;
  }
  repeated string comments_after = 4;
  repeated uint32 nags = 5;
}

message MoveVariation {
  repeated .chesscom.chess.v1.GameMove moves = 1;
}

message Rules {
  oneof _is_chess960 {
  bool is_chess960 = 1;
  }
}

message GameMetadata {
  oneof _time_control {
  .chesscom.chess.v1.TimeControl time_control = 2;
  }
  on
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01027"></a>
## FND-01027: chesscom.chess.v1.GameMoveMetadata.nags = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 nags = 5;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 858.

```text

  oneof _comment_before {
  string comment_before = 3;
  }
  repeated string comments_after = 4;
  repeated uint32 nags = 5;
}

message MoveVariation {
  repeated .chesscom.chess.v1.GameMove moves = 1;
}

message Rules {
  oneof _is_chess960 {
  bool is_chess960 = 1;
  }
}

message GameMetadata {
  oneof _time_control {
  .chesscom.chess.v1.TimeControl time_control = 2;
  }
  oneof _timestamps {
  .chesscom.chess.v1
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01028"></a>
## FND-01028: message declaration: chesscom.chess.v1.MoveVariation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MoveVariation {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 887.

```text
string comment_before = 3;
  }
  repeated string comments_after = 4;
  repeated uint32 nags = 5;
}

message MoveVariation {
  repeated .chesscom.chess.v1.GameMove moves = 1;
}

message Rules {
  oneof _is_chess960 {
  bool is_chess960 = 1;
  }
}

message GameMetadata {
  oneof _time_control {
  .chesscom.chess.v1.TimeControl time_control = 2;
  }
  oneof _timestamps {
  .chesscom.chess.v1.Timestamps timestamps = 3;
 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01029"></a>
## FND-01029: chesscom.chess.v1.MoveVariation.moves = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.GameMove moves = 1;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 913.

```text

  }
  repeated string comments_after = 4;
  repeated uint32 nags = 5;
}

message MoveVariation {
  repeated .chesscom.chess.v1.GameMove moves = 1;
}

message Rules {
  oneof _is_chess960 {
  bool is_chess960 = 1;
  }
}

message GameMetadata {
  oneof _time_control {
  .chesscom.chess.v1.TimeControl time_control = 2;
  }
  oneof _timestamps {
  .chesscom.chess.v1.Timestamps timestamps = 3;
  }
  oneof _result {
  .ch
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01030"></a>
## FND-01030: message declaration: chesscom.chess.v1.Rules

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Rules {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 964.

```text
ed uint32 nags = 5;
}

message MoveVariation {
  repeated .chesscom.chess.v1.GameMove moves = 1;
}

message Rules {
  oneof _is_chess960 {
  bool is_chess960 = 1;
  }
}

message GameMetadata {
  oneof _time_control {
  .chesscom.chess.v1.TimeControl time_control = 2;
  }
  oneof _timestamps {
  .chesscom.chess.v1.Timestamps timestamps = 3;
  }
  oneof _result {
  .chesscom.chess.v1.GameResult result = 4;
  }
  oneof 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01031"></a>
## FND-01031: oneof declaration: chesscom.chess.v1.Rules._is_chess960

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_chess960 {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 982.

```text
;
}

message MoveVariation {
  repeated .chesscom.chess.v1.GameMove moves = 1;
}

message Rules {
  oneof _is_chess960 {
  bool is_chess960 = 1;
  }
}

message GameMetadata {
  oneof _time_control {
  .chesscom.chess.v1.TimeControl time_control = 2;
  }
  oneof _timestamps {
  .chesscom.chess.v1.Timestamps timestamps = 3;
  }
  oneof _result {
  .chesscom.chess.v1.GameResult result = 4;
  }
  oneof _rules {
  .chessc
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01032"></a>
## FND-01032: chesscom.chess.v1.Rules.is_chess960 = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_chess960 = 1;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1005.

```text
ion {
  repeated .chesscom.chess.v1.GameMove moves = 1;
}

message Rules {
  oneof _is_chess960 {
  bool is_chess960 = 1;
  }
}

message GameMetadata {
  oneof _time_control {
  .chesscom.chess.v1.TimeControl time_control = 2;
  }
  oneof _timestamps {
  .chesscom.chess.v1.Timestamps timestamps = 3;
  }
  oneof _result {
  .chesscom.chess.v1.GameResult result = 4;
  }
  oneof _rules {
  .chesscom.chess.v1.Rules rules
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01033"></a>
## FND-01033: message declaration: chesscom.chess.v1.GameMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameMetadata {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1034.

```text
ess.v1.GameMove moves = 1;
}

message Rules {
  oneof _is_chess960 {
  bool is_chess960 = 1;
  }
}

message GameMetadata {
  oneof _time_control {
  .chesscom.chess.v1.TimeControl time_control = 2;
  }
  oneof _timestamps {
  .chesscom.chess.v1.Timestamps timestamps = 3;
  }
  oneof _result {
  .chesscom.chess.v1.GameResult result = 4;
  }
  oneof _rules {
  .chesscom.chess.v1.Rules rules = 5;
  }
  oneof _chesscom_m
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01034"></a>
## FND-01034: oneof declaration: chesscom.chess.v1.GameMetadata._time_control

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_control {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1059.

```text
;
}

message Rules {
  oneof _is_chess960 {
  bool is_chess960 = 1;
  }
}

message GameMetadata {
  oneof _time_control {
  .chesscom.chess.v1.TimeControl time_control = 2;
  }
  oneof _timestamps {
  .chesscom.chess.v1.Timestamps timestamps = 3;
  }
  oneof _result {
  .chesscom.chess.v1.GameResult result = 4;
  }
  oneof _rules {
  .chesscom.chess.v1.Rules rules = 5;
  }
  oneof _chesscom_metadata {
  .chesscom.che
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01035"></a>
## FND-01035: chesscom.chess.v1.GameMetadata.time_control = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.TimeControl time_control = 2;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1083.

```text
neof _is_chess960 {
  bool is_chess960 = 1;
  }
}

message GameMetadata {
  oneof _time_control {
  .chesscom.chess.v1.TimeControl time_control = 2;
  }
  oneof _timestamps {
  .chesscom.chess.v1.Timestamps timestamps = 3;
  }
  oneof _result {
  .chesscom.chess.v1.GameResult result = 4;
  }
  oneof _rules {
  .chesscom.chess.v1.Rules rules = 5;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomGameMetada
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01036"></a>
## FND-01036: oneof declaration: chesscom.chess.v1.GameMetadata._timestamps

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _timestamps {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1138.

```text
age GameMetadata {
  oneof _time_control {
  .chesscom.chess.v1.TimeControl time_control = 2;
  }
  oneof _timestamps {
  .chesscom.chess.v1.Timestamps timestamps = 3;
  }
  oneof _result {
  .chesscom.chess.v1.GameResult result = 4;
  }
  oneof _rules {
  .chesscom.chess.v1.Rules rules = 5;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomGameMetadata chesscom_metadata = 6;
  }
  oneof _link {
  string 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01037"></a>
## FND-01037: chesscom.chess.v1.GameMetadata.timestamps = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Timestamps timestamps = 3;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1160.

```text
neof _time_control {
  .chesscom.chess.v1.TimeControl time_control = 2;
  }
  oneof _timestamps {
  .chesscom.chess.v1.Timestamps timestamps = 3;
  }
  oneof _result {
  .chesscom.chess.v1.GameResult result = 4;
  }
  oneof _rules {
  .chesscom.chess.v1.Rules rules = 5;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomGameMetadata chesscom_metadata = 6;
  }
  oneof _link {
  string link = 8;
  }
  oneof 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01038"></a>
## FND-01038: oneof declaration: chesscom.chess.v1.GameMetadata._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1212.

```text
l time_control = 2;
  }
  oneof _timestamps {
  .chesscom.chess.v1.Timestamps timestamps = 3;
  }
  oneof _result {
  .chesscom.chess.v1.GameResult result = 4;
  }
  oneof _rules {
  .chesscom.chess.v1.Rules rules = 5;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomGameMetadata chesscom_metadata = 6;
  }
  oneof _link {
  string link = 8;
  }
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_cl
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01039"></a>
## FND-01039: chesscom.chess.v1.GameMetadata.result = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.GameResult result = 4;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1230.

```text
;
  }
  oneof _timestamps {
  .chesscom.chess.v1.Timestamps timestamps = 3;
  }
  oneof _result {
  .chesscom.chess.v1.GameResult result = 4;
  }
  oneof _rules {
  .chesscom.chess.v1.Rules rules = 5;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomGameMetadata chesscom_metadata = 6;
  }
  oneof _link {
  string link = 8;
  }
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 9;
  }
  one
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01040"></a>
## FND-01040: oneof declaration: chesscom.chess.v1.GameMetadata._rules

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rules {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1278.

```text
.Timestamps timestamps = 3;
  }
  oneof _result {
  .chesscom.chess.v1.GameResult result = 4;
  }
  oneof _rules {
  .chesscom.chess.v1.Rules rules = 5;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomGameMetadata chesscom_metadata = 6;
  }
  oneof _link {
  string link = 8;
  }
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 9;
  }
  oneof _is_rated {
  bool is_rated = 10;
  }
  repea
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01041"></a>
## FND-01041: chesscom.chess.v1.GameMetadata.rules = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Rules rules = 5;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1295.

```text
tamps = 3;
  }
  oneof _result {
  .chesscom.chess.v1.GameResult result = 4;
  }
  oneof _rules {
  .chesscom.chess.v1.Rules rules = 5;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomGameMetadata chesscom_metadata = 6;
  }
  oneof _link {
  string link = 8;
  }
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 9;
  }
  oneof _is_rated {
  bool is_rated = 10;
  }
  repeated .chesscom.che
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01042"></a>
## FND-01042: oneof declaration: chesscom.chess.v1.GameMetadata._chesscom_metadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _chesscom_metadata {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1337.

```text
om.chess.v1.GameResult result = 4;
  }
  oneof _rules {
  .chesscom.chess.v1.Rules rules = 5;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomGameMetadata chesscom_metadata = 6;
  }
  oneof _link {
  string link = 8;
  }
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 9;
  }
  oneof _is_rated {
  bool is_rated = 10;
  }
  repeated .chesscom.chess.v1.PlayerMetadata players = 1;
  repeat
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01043"></a>
## FND-01043: chesscom.chess.v1.GameMetadata.chesscom_metadata = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.ChesscomGameMetadata chesscom_metadata = 6;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1366.

```text
 = 4;
  }
  oneof _rules {
  .chesscom.chess.v1.Rules rules = 5;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomGameMetadata chesscom_metadata = 6;
  }
  oneof _link {
  string link = 8;
  }
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 9;
  }
  oneof _is_rated {
  bool is_rated = 10;
  }
  repeated .chesscom.chess.v1.PlayerMetadata players = 1;
  repeated .chesscom.chess.v1.GameMet
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01044"></a>
## FND-01044: oneof declaration: chesscom.chess.v1.GameMetadata._link

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _link {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1435.

```text
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomGameMetadata chesscom_metadata = 6;
  }
  oneof _link {
  string link = 8;
  }
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 9;
  }
  oneof _is_rated {
  bool is_rated = 10;
  }
  repeated .chesscom.chess.v1.PlayerMetadata players = 1;
  repeated .chesscom.chess.v1.GameMetadata.PgnHeadersEntry pgn_headers = 7;
  message PgnHeadersEntry {
  
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01045"></a>
## FND-01045: chesscom.chess.v1.GameMetadata.link = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string link = 8;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1451.

```text
m_metadata {
  .chesscom.chess.v1.ChesscomGameMetadata chesscom_metadata = 6;
  }
  oneof _link {
  string link = 8;
  }
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 9;
  }
  oneof _is_rated {
  bool is_rated = 10;
  }
  repeated .chesscom.chess.v1.PlayerMetadata players = 1;
  repeated .chesscom.chess.v1.GameMetadata.PgnHeadersEntry pgn_headers = 7;
  message PgnHeadersEntry {
  optional string 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01046"></a>
## FND-01046: oneof declaration: chesscom.chess.v1.GameMetadata._time_class

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_class {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1474.

```text
m.chess.v1.ChesscomGameMetadata chesscom_metadata = 6;
  }
  oneof _link {
  string link = 8;
  }
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 9;
  }
  oneof _is_rated {
  bool is_rated = 10;
  }
  repeated .chesscom.chess.v1.PlayerMetadata players = 1;
  repeated .chesscom.chess.v1.GameMetadata.PgnHeadersEntry pgn_headers = 7;
  message PgnHeadersEntry {
  optional string key = 1;
  optional str
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01047"></a>
## FND-01047: chesscom.chess.v1.GameMetadata.time_class = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.TimeClass time_class = 9;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1496.

```text
eMetadata chesscom_metadata = 6;
  }
  oneof _link {
  string link = 8;
  }
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 9;
  }
  oneof _is_rated {
  bool is_rated = 10;
  }
  repeated .chesscom.chess.v1.PlayerMetadata players = 1;
  repeated .chesscom.chess.v1.GameMetadata.PgnHeadersEntry pgn_headers = 7;
  message PgnHeadersEntry {
  optional string key = 1;
  optional string value = 2;
  }
}


```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01048"></a>
## FND-01048: oneof declaration: chesscom.chess.v1.GameMetadata._is_rated

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_rated {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1547.

```text
{
  string link = 8;
  }
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 9;
  }
  oneof _is_rated {
  bool is_rated = 10;
  }
  repeated .chesscom.chess.v1.PlayerMetadata players = 1;
  repeated .chesscom.chess.v1.GameMetadata.PgnHeadersEntry pgn_headers = 7;
  message PgnHeadersEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message Timestamps {
  oneof _started_at {
  int64 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01049"></a>
## FND-01049: chesscom.chess.v1.GameMetadata.is_rated = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_rated = 10;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1567.

```text

  }
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 9;
  }
  oneof _is_rated {
  bool is_rated = 10;
  }
  repeated .chesscom.chess.v1.PlayerMetadata players = 1;
  repeated .chesscom.chess.v1.GameMetadata.PgnHeadersEntry pgn_headers = 7;
  message PgnHeadersEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message Timestamps {
  oneof _started_at {
  int64 started_at = 1;
  }

```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01050"></a>
## FND-01050: chesscom.chess.v1.GameMetadata.players = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.PlayerMetadata players = 1;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1593.

```text

  .chesscom.chess.v1.TimeClass time_class = 9;
  }
  oneof _is_rated {
  bool is_rated = 10;
  }
  repeated .chesscom.chess.v1.PlayerMetadata players = 1;
  repeated .chesscom.chess.v1.GameMetadata.PgnHeadersEntry pgn_headers = 7;
  message PgnHeadersEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message Timestamps {
  oneof _started_at {
  int64 started_at = 1;
  }
  oneof _finished_at {
  i
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01051"></a>
## FND-01051: chesscom.chess.v1.GameMetadata.pgn_headers = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.GameMetadata.PgnHeadersEntry pgn_headers = 7;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1651.

```text
f _is_rated {
  bool is_rated = 10;
  }
  repeated .chesscom.chess.v1.PlayerMetadata players = 1;
  repeated .chesscom.chess.v1.GameMetadata.PgnHeadersEntry pgn_headers = 7;
  message PgnHeadersEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message Timestamps {
  oneof _started_at {
  int64 started_at = 1;
  }
  oneof _finished_at {
  int64 finished_at = 2;
  }
}

message ChesscomGameMetadata 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01052"></a>
## FND-01052: message declaration: chesscom.chess.v1.GameMetadata.PgnHeadersEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PgnHeadersEntry {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1727.

```text
Metadata players = 1;
  repeated .chesscom.chess.v1.GameMetadata.PgnHeadersEntry pgn_headers = 7;
  message PgnHeadersEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message Timestamps {
  oneof _started_at {
  int64 started_at = 1;
  }
  oneof _finished_at {
  int64 finished_at = 2;
  }
}

message ChesscomGameMetadata {
  oneof _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  i
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01053"></a>
## FND-01053: chesscom.chess.v1.GameMetadata.PgnHeadersEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1755.

```text
ated .chesscom.chess.v1.GameMetadata.PgnHeadersEntry pgn_headers = 7;
  message PgnHeadersEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message Timestamps {
  oneof _started_at {
  int64 started_at = 1;
  }
  oneof _finished_at {
  int64 finished_at = 2;
  }
}

message ChesscomGameMetadata {
  oneof _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01054"></a>
## FND-01054: chesscom.chess.v1.GameMetadata.PgnHeadersEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1782.

```text
eMetadata.PgnHeadersEntry pgn_headers = 7;
  message PgnHeadersEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message Timestamps {
  oneof _started_at {
  int64 started_at = 1;
  }
  oneof _finished_at {
  int64 finished_at = 2;
  }
}

message ChesscomGameMetadata {
  oneof _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01055"></a>
## FND-01055: message declaration: chesscom.chess.v1.Timestamps

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Timestamps {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1816.

```text
ers = 7;
  message PgnHeadersEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message Timestamps {
  oneof _started_at {
  int64 started_at = 1;
  }
  oneof _finished_at {
  int64 finished_at = 2;
  }
}

message ChesscomGameMetadata {
  oneof _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_sour
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01056"></a>
## FND-01056: oneof declaration: chesscom.chess.v1.Timestamps._started_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _started_at {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1839.

```text
eadersEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message Timestamps {
  oneof _started_at {
  int64 started_at = 1;
  }
  oneof _finished_at {
  int64 finished_at = 2;
  }
}

message ChesscomGameMetadata {
  oneof _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01057"></a>
## FND-01057: chesscom.chess.v1.Timestamps.started_at = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 started_at = 1;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1861.

```text
al string key = 1;
  optional string value = 2;
  }
}

message Timestamps {
  oneof _started_at {
  int64 started_at = 1;
  }
  oneof _finished_at {
  int64 finished_at = 2;
  }
}

message ChesscomGameMetadata {
  oneof _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.v1.ChesscomGameSource 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01058"></a>
## FND-01058: oneof declaration: chesscom.chess.v1.Timestamps._finished_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _finished_at {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1889.

```text
l string value = 2;
  }
}

message Timestamps {
  oneof _started_at {
  int64 started_at = 1;
  }
  oneof _finished_at {
  int64 finished_at = 2;
  }
}

message ChesscomGameMetadata {
  oneof _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

mess
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01059"></a>
## FND-01059: chesscom.chess.v1.Timestamps.finished_at = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 finished_at = 2;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1912.

```text

}

message Timestamps {
  oneof _started_at {
  int64 started_at = 1;
  }
  oneof _finished_at {
  int64 finished_at = 2;
  }
}

message ChesscomGameMetadata {
  oneof _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

message PlayerMetadata {
  
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01060"></a>
## FND-01060: message declaration: chesscom.chess.v1.ChesscomGameMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ChesscomGameMetadata {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1942.

```text
of _started_at {
  int64 started_at = 1;
  }
  oneof _finished_at {
  int64 finished_at = 2;
  }
}

message ChesscomGameMetadata {
  oneof _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

message PlayerMetadata {
  oneof _name {
  string name = 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01061"></a>
## FND-01061: oneof declaration: chesscom.chess.v1.ChesscomGameMetadata._game_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_id {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1975.

```text
at = 1;
  }
  oneof _finished_at {
  int64 finished_at = 2;
  }
}

message ChesscomGameMetadata {
  oneof _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

message PlayerMetadata {
  oneof _name {
  string name = 4;
  }
  oneof _chesscom_metadata
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01062"></a>
## FND-01062: chesscom.chess.v1.ChesscomGameMetadata.game_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string game_id = 1;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1994.

```text
 _finished_at {
  int64 finished_at = 2;
  }
}

message ChesscomGameMetadata {
  oneof _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

message PlayerMetadata {
  oneof _name {
  string name = 4;
  }
  oneof _chesscom_metadata {
  .chesscom.ches
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01063"></a>
## FND-01063: oneof declaration: chesscom.chess.v1.ChesscomGameMetadata._legacy_game_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _legacy_game_id {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2020.

```text
nished_at = 2;
  }
}

message ChesscomGameMetadata {
  oneof _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

message PlayerMetadata {
  oneof _name {
  string name = 4;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomPlayerMetadat
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01064"></a>
## FND-01064: chesscom.chess.v1.ChesscomGameMetadata.legacy_game_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 legacy_game_id = 2;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2046.

```text
age ChesscomGameMetadata {
  oneof _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

message PlayerMetadata {
  oneof _name {
  string name = 4;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomPlayerMetadata chesscom_metadata = 3;
 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01065"></a>
## FND-01065: oneof declaration: chesscom.chess.v1.ChesscomGameMetadata._eco_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _eco_id {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2078.

```text
of _game_id {
  string game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

message PlayerMetadata {
  oneof _name {
  string name = 4;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomPlayerMetadata chesscom_metadata = 3;
  }
  optional .chesscom.chess.v1
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01066"></a>
## FND-01066: chesscom.chess.v1.ChesscomGameMetadata.eco_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 eco_id = 3;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2096.

```text
ring game_id = 1;
  }
  oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

message PlayerMetadata {
  oneof _name {
  string name = 4;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomPlayerMetadata chesscom_metadata = 3;
  }
  optional .chesscom.chess.v1.Color color = 1;

```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01067"></a>
## FND-01067: oneof declaration: chesscom.chess.v1.ChesscomGameMetadata._game_source

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_source {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2120.

```text
oneof _legacy_game_id {
  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

message PlayerMetadata {
  oneof _name {
  string name = 4;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomPlayerMetadata chesscom_metadata = 3;
  }
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.che
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01068"></a>
## FND-01068: chesscom.chess.v1.ChesscomGameMetadata.game_source = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.ChesscomGameSource game_source = 4;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2143.

```text

  int64 legacy_game_id = 2;
  }
  oneof _eco_id {
  int64 eco_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

message PlayerMetadata {
  oneof _name {
  string name = 4;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomPlayerMetadata chesscom_metadata = 3;
  }
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.chess.v1.Rating ratings = 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01069"></a>
## FND-01069: message declaration: chesscom.chess.v1.PlayerMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayerMetadata {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2205.

```text
_id = 3;
  }
  oneof _game_source {
  .chesscom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

message PlayerMetadata {
  oneof _name {
  string name = 4;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomPlayerMetadata chesscom_metadata = 3;
  }
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.chess.v1.Rating ratings = 2;
}

message Rating {
  oneof _rating {
  int32 rating = 1;
 
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01070"></a>
## FND-01070: oneof declaration: chesscom.chess.v1.PlayerMetadata._name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _name {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2232.

```text
source {
  .chesscom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

message PlayerMetadata {
  oneof _name {
  string name = 4;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomPlayerMetadata chesscom_metadata = 3;
  }
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.chess.v1.Rating ratings = 2;
}

message Rating {
  oneof _rating {
  int32 rating = 1;
  }
}

message ChesscomPlaye
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01071"></a>
## FND-01071: chesscom.chess.v1.PlayerMetadata.name = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string name = 4;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2248.

```text
scom.chess.v1.ChesscomGameSource game_source = 4;
  }
}

message PlayerMetadata {
  oneof _name {
  string name = 4;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomPlayerMetadata chesscom_metadata = 3;
  }
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.chess.v1.Rating ratings = 2;
}

message Rating {
  oneof _rating {
  int32 rating = 1;
  }
}

message ChesscomPlayerMetadata {
  on
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01072"></a>
## FND-01072: oneof declaration: chesscom.chess.v1.PlayerMetadata._chesscom_metadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _chesscom_metadata {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 1337.

```text
om.chess.v1.GameResult result = 4;
  }
  oneof _rules {
  .chesscom.chess.v1.Rules rules = 5;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomGameMetadata chesscom_metadata = 6;
  }
  oneof _link {
  string link = 8;
  }
  oneof _time_class {
  .chesscom.chess.v1.TimeClass time_class = 9;
  }
  oneof _is_rated {
  bool is_rated = 10;
  }
  repeated .chesscom.chess.v1.PlayerMetadata players = 1;
  repeat
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01073"></a>
## FND-01073: chesscom.chess.v1.PlayerMetadata.chesscom_metadata = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.ChesscomPlayerMetadata chesscom_metadata = 3;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2300.

```text
}
}

message PlayerMetadata {
  oneof _name {
  string name = 4;
  }
  oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomPlayerMetadata chesscom_metadata = 3;
  }
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.chess.v1.Rating ratings = 2;
}

message Rating {
  oneof _rating {
  int32 rating = 1;
  }
}

message ChesscomPlayerMetadata {
  oneof _user_id {
  string user_id = 1;
  }
  oneof _le
```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01074"></a>
## FND-01074: chesscom.chess.v1.PlayerMetadata.color = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Color color = 1;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2371.

```text
oneof _chesscom_metadata {
  .chesscom.chess.v1.ChesscomPlayerMetadata chesscom_metadata = 3;
  }
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.chess.v1.Rating ratings = 2;
}

message Rating {
  oneof _rating {
  int32 rating = 1;
  }
}

message ChesscomPlayerMetadata {
  oneof _user_id {
  string user_id = 1;
  }
  oneof _legacy_user_id {
  int64 legacy_user_id = 2;
  }
}

```

**Source references:** SRC-0246, SRC-1217  
**URL references:** None independently associated  
**Related findings:** FND-01007, FND-01008, FND-01009

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
