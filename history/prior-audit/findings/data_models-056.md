# data_models — findings 5501–5600

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-05775"></a>
## FND-05775: chesscom.game_storage.v1.VariantGame.end_fen4 = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string end_fen4 = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6412.

```text
optional string second_game_key = 3;
}

message VariantGame {
  optional string initial_fen4 = 1;
  optional string end_fen4 = 2;
  optional uint32 ply_count = 3;
  optional string pgn4 = 4;
  optional string board_dimension = 5;
  optional .chesscom.game_storage.v1.VariantGame.VariantType type = 6;
  optional string rating_type = 7;
  optional .chesscom.game_storage.v1.Player player_1 = 8;
  optional .chesscom.game_
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05776"></a>
## FND-05776: chesscom.game_storage.v1.VariantGame.ply_count = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 ply_count = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 5993.

```text
e_storage.v1.MasterChessGameData master_chess_game_data = 8;
  }
  optional string final_fen = 2;
  optional uint32 ply_count = 3;
  optional string move_text = 4;
  repeated uint32 move_timestamps = 5;
  optional .chesscom.game_storage.v1.Player white_player = 6;
  optional .chesscom.game_storage.v1.Player black_player = 7;
}

message BughouseGame {
  optional .chesscom.game_storage.v1.ChessGame first_board = 1;
  o
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05777"></a>
## FND-05777: chesscom.game_storage.v1.VariantGame.pgn4 = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string pgn4 = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6477.

```text
ptional string initial_fen4 = 1;
  optional string end_fen4 = 2;
  optional uint32 ply_count = 3;
  optional string pgn4 = 4;
  optional string board_dimension = 5;
  optional .chesscom.game_storage.v1.VariantGame.VariantType type = 6;
  optional string rating_type = 7;
  optional .chesscom.game_storage.v1.Player player_1 = 8;
  optional .chesscom.game_storage.v1.Player player_2 = 9;
  optional .chesscom.game_storage
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05778"></a>
## FND-05778: chesscom.game_storage.v1.VariantGame.board_dimension = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string board_dimension = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6505.

```text
= 1;
  optional string end_fen4 = 2;
  optional uint32 ply_count = 3;
  optional string pgn4 = 4;
  optional string board_dimension = 5;
  optional .chesscom.game_storage.v1.VariantGame.VariantType type = 6;
  optional string rating_type = 7;
  optional .chesscom.game_storage.v1.Player player_1 = 8;
  optional .chesscom.game_storage.v1.Player player_2 = 9;
  optional .chesscom.game_storage.v1.Player player_3 = 10;
  
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05779"></a>
## FND-05779: chesscom.game_storage.v1.VariantGame.type = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.VariantGame.VariantType type = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6544.

```text
optional uint32 ply_count = 3;
  optional string pgn4 = 4;
  optional string board_dimension = 5;
  optional .chesscom.game_storage.v1.VariantGame.VariantType type = 6;
  optional string rating_type = 7;
  optional .chesscom.game_storage.v1.Player player_1 = 8;
  optional .chesscom.game_storage.v1.Player player_2 = 9;
  optional .chesscom.game_storage.v1.Player player_3 = 10;
  optional .chesscom.game_storage.v1.Play
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05780"></a>
## FND-05780: chesscom.game_storage.v1.VariantGame.rating_type = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string rating_type = 7;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6615.

```text
tring board_dimension = 5;
  optional .chesscom.game_storage.v1.VariantGame.VariantType type = 6;
  optional string rating_type = 7;
  optional .chesscom.game_storage.v1.Player player_1 = 8;
  optional .chesscom.game_storage.v1.Player player_2 = 9;
  optional .chesscom.game_storage.v1.Player player_3 = 10;
  optional .chesscom.game_storage.v1.Player player_4 = 11;
  enum VariantType {
    VARIANT_TYPE_UNSPECIFIED = 0
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05781"></a>
## FND-05781: chesscom.game_storage.v1.VariantGame.player_1 = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.Player player_1 = 8;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6650.

```text
al .chesscom.game_storage.v1.VariantGame.VariantType type = 6;
  optional string rating_type = 7;
  optional .chesscom.game_storage.v1.Player player_1 = 8;
  optional .chesscom.game_storage.v1.Player player_2 = 9;
  optional .chesscom.game_storage.v1.Player player_3 = 10;
  optional .chesscom.game_storage.v1.Player player_4 = 11;
  enum VariantType {
    VARIANT_TYPE_UNSPECIFIED = 0;
    VARIANT_TYPE_FREE_FOR_ALL = 1
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05782"></a>
## FND-05782: chesscom.game_storage.v1.VariantGame.player_2 = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.Player player_2 = 9;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6708.

```text
= 6;
  optional string rating_type = 7;
  optional .chesscom.game_storage.v1.Player player_1 = 8;
  optional .chesscom.game_storage.v1.Player player_2 = 9;
  optional .chesscom.game_storage.v1.Player player_3 = 10;
  optional .chesscom.game_storage.v1.Player player_4 = 11;
  enum VariantType {
    VARIANT_TYPE_UNSPECIFIED = 0;
    VARIANT_TYPE_FREE_FOR_ALL = 1;
    VARIANT_TYPE_TEAMS = 2;
    VARIANT_TYPE_SOLO = 3;
 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05783"></a>
## FND-05783: chesscom.game_storage.v1.VariantGame.player_3 = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.Player player_3 = 10;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6766.

```text
om.game_storage.v1.Player player_1 = 8;
  optional .chesscom.game_storage.v1.Player player_2 = 9;
  optional .chesscom.game_storage.v1.Player player_3 = 10;
  optional .chesscom.game_storage.v1.Player player_4 = 11;
  enum VariantType {
    VARIANT_TYPE_UNSPECIFIED = 0;
    VARIANT_TYPE_FREE_FOR_ALL = 1;
    VARIANT_TYPE_TEAMS = 2;
    VARIANT_TYPE_SOLO = 3;
  }
}

message PerPlayerTimeControl {
  optional string pla
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05784"></a>
## FND-05784: chesscom.game_storage.v1.VariantGame.player_4 = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.Player player_4 = 11;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6825.

```text
m.game_storage.v1.Player player_2 = 9;
  optional .chesscom.game_storage.v1.Player player_3 = 10;
  optional .chesscom.game_storage.v1.Player player_4 = 11;
  enum VariantType {
    VARIANT_TYPE_UNSPECIFIED = 0;
    VARIANT_TYPE_FREE_FOR_ALL = 1;
    VARIANT_TYPE_TEAMS = 2;
    VARIANT_TYPE_SOLO = 3;
  }
}

message PerPlayerTimeControl {
  optional string player_id = 1;
  optional string time_control = 2;
}

message 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05785"></a>
## FND-05785: enum declaration: chesscom.game_storage.v1.VariantGame.VariantType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum VariantType {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6884.

```text
.game_storage.v1.Player player_3 = 10;
  optional .chesscom.game_storage.v1.Player player_4 = 11;
  enum VariantType {
    VARIANT_TYPE_UNSPECIFIED = 0;
    VARIANT_TYPE_FREE_FOR_ALL = 1;
    VARIANT_TYPE_TEAMS = 2;
    VARIANT_TYPE_SOLO = 3;
  }
}

message PerPlayerTimeControl {
  optional string player_id = 1;
  optional string time_control = 2;
}

message Player {
  oneof _client {
  string client = 13;
  }
  oneo
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05786"></a>
## FND-05786: chesscom.game_storage.v1.VariantGame.VariantType.VARIANT_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6907.

```text
 player_3 = 10;
  optional .chesscom.game_storage.v1.Player player_4 = 11;
  enum VariantType {
    VARIANT_TYPE_UNSPECIFIED = 0;
    VARIANT_TYPE_FREE_FOR_ALL = 1;
    VARIANT_TYPE_TEAMS = 2;
    VARIANT_TYPE_SOLO = 3;
  }
}

message PerPlayerTimeControl {
  optional string player_id = 1;
  optional string time_control = 2;
}

message Player {
  oneof _client {
  string client = 13;
  }
  oneof _points {
  uint32 po
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05787"></a>
## FND-05787: chesscom.game_storage.v1.VariantGame.VariantType.VARIANT_TYPE_FREE_FOR_ALL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_TYPE_FREE_FOR_ALL = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6941.

```text
om.game_storage.v1.Player player_4 = 11;
  enum VariantType {
    VARIANT_TYPE_UNSPECIFIED = 0;
    VARIANT_TYPE_FREE_FOR_ALL = 1;
    VARIANT_TYPE_TEAMS = 2;
    VARIANT_TYPE_SOLO = 3;
  }
}

message PerPlayerTimeControl {
  optional string player_id = 1;
  optional string time_control = 2;
}

message Player {
  oneof _client {
  string client = 13;
  }
  oneof _points {
  uint32 points = 14;
  }
  oneof _initial_ra
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05788"></a>
## FND-05788: chesscom.game_storage.v1.VariantGame.VariantType.VARIANT_TYPE_TEAMS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_TYPE_TEAMS = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 6976.

```text
= 11;
  enum VariantType {
    VARIANT_TYPE_UNSPECIFIED = 0;
    VARIANT_TYPE_FREE_FOR_ALL = 1;
    VARIANT_TYPE_TEAMS = 2;
    VARIANT_TYPE_SOLO = 3;
  }
}

message PerPlayerTimeControl {
  optional string player_id = 1;
  optional string time_control = 2;
}

message Player {
  oneof _client {
  string client = 13;
  }
  oneof _points {
  uint32 points = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05789"></a>
## FND-05789: chesscom.game_storage.v1.VariantGame.VariantType.VARIANT_TYPE_SOLO = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_TYPE_SOLO = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7004.

```text
   VARIANT_TYPE_UNSPECIFIED = 0;
    VARIANT_TYPE_FREE_FOR_ALL = 1;
    VARIANT_TYPE_TEAMS = 2;
    VARIANT_TYPE_SOLO = 3;
  }
}

message PerPlayerTimeControl {
  optional string player_id = 1;
  optional string time_control = 2;
}

message Player {
  oneof _client {
  string client = 13;
  }
  oneof _points {
  uint32 points = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05790"></a>
## FND-05790: message declaration: chesscom.game_storage.v1.PerPlayerTimeControl

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PerPlayerTimeControl {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7034.

```text
0;
    VARIANT_TYPE_FREE_FOR_ALL = 1;
    VARIANT_TYPE_TEAMS = 2;
    VARIANT_TYPE_SOLO = 3;
  }
}

message PerPlayerTimeControl {
  optional string player_id = 1;
  optional string time_control = 2;
}

message Player {
  oneof _client {
  string client = 13;
  }
  oneof _points {
  uint32 points = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05791"></a>
## FND-05791: chesscom.game_storage.v1.PerPlayerTimeControl.player_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string player_id = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7067.

```text
= 1;
    VARIANT_TYPE_TEAMS = 2;
    VARIANT_TYPE_SOLO = 3;
  }
}

message PerPlayerTimeControl {
  optional string player_id = 1;
  optional string time_control = 2;
}

message Player {
  oneof _client {
  string client = 13;
  }
  oneof _points {
  uint32 points = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05792"></a>
## FND-05792: chesscom.game_storage.v1.PerPlayerTimeControl.time_control = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string time_control = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7100.

```text
    VARIANT_TYPE_SOLO = 3;
  }
}

message PerPlayerTimeControl {
  optional string player_id = 1;
  optional string time_control = 2;
}

message Player {
  oneof _client {
  string client = 13;
  }
  oneof _points {
  uint32 points = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05793"></a>
## FND-05793: message declaration: chesscom.game_storage.v1.Player

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Player {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7137.

```text
sage PerPlayerTimeControl {
  optional string player_id = 1;
  optional string time_control = 2;
}

message Player {
  oneof _client {
  string client = 13;
  }
  oneof _points {
  uint32 points = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  on
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05794"></a>
## FND-05794: oneof declaration: chesscom.game_storage.v1.Player._client

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _client {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7156.

```text
ontrol {
  optional string player_id = 1;
  optional string time_control = 2;
}

message Player {
  oneof _client {
  string client = 13;
  }
  oneof _points {
  uint32 points = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_lo
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05795"></a>
## FND-05795: chesscom.game_storage.v1.Player.client = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string client = 13;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7174.

```text
l string player_id = 1;
  optional string time_control = 2;
}

message Player {
  oneof _client {
  string client = 13;
  }
  oneof _points {
  uint32 points = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05796"></a>
## FND-05796: oneof declaration: chesscom.game_storage.v1.Player._points

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _points {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7200.

```text
optional string time_control = 2;
}

message Player {
  oneof _client {
  string client = 13;
  }
  oneof _points {
  uint32 points = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05797"></a>
## FND-05797: chesscom.game_storage.v1.Player.points = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 points = 14;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7218.

```text
me_control = 2;
}

message Player {
  oneof _client {
  string client = 13;
  }
  oneof _points {
  uint32 points = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
  oneof _bad_spor
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05798"></a>
## FND-05798: oneof declaration: chesscom.game_storage.v1.Player._initial_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _initial_rating {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7244.

```text
 Player {
  oneof _client {
  string client = 13;
  }
  oneof _points {
  uint32 points = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
  oneof _bad_sport_behavior {
  .chesscom.g
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05799"></a>
## FND-05799: chesscom.game_storage.v1.Player.initial_rating = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 initial_rating = 15;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7270.

```text
{
  string client = 13;
  }
  oneof _points {
  uint32 points = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v1.PlayerBadSp
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05800"></a>
## FND-05800: oneof declaration: chesscom.game_storage.v1.Player._rating_diff

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_diff {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7304.

```text
f _points {
  uint32 points = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v1.PlayerBadSportBehavior bad_sport_behavior = 2
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05801"></a>
## FND-05801: chesscom.game_storage.v1.Player.rating_diff = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

float rating_diff = 16;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7327.

```text
ints = 14;
  }
  oneof _initial_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v1.PlayerBadSportBehavior bad_sport_behavior = 20;
  }
  optional strin
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05802"></a>
## FND-05802: oneof declaration: chesscom.game_storage.v1.Player._fide_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fide_id {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7357.

```text
l_rating {
  uint32 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v1.PlayerBadSportBehavior bad_sport_behavior = 20;
  }
  optional string id = 1;
  optional .chesscom
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05803"></a>
## FND-05803: chesscom.game_storage.v1.Player.fide_id = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint64 fide_id = 17;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7376.

```text
 initial_rating = 15;
  }
  oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v1.PlayerBadSportBehavior bad_sport_behavior = 20;
  }
  optional string id = 1;
  optional .chesscom.game_storage.v1.Pl
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05804"></a>
## FND-05804: oneof declaration: chesscom.game_storage.v1.Player._min_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _min_rating {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7403.

```text
 oneof _rating_diff {
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v1.PlayerBadSportBehavior bad_sport_behavior = 20;
  }
  optional string id = 1;
  optional .chesscom.game_storage.v1.PlayerType type = 2;
  option
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05805"></a>
## FND-05805: chesscom.game_storage.v1.Player.min_rating = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 min_rating = 18;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7425.

```text
  float rating_diff = 16;
  }
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v1.PlayerBadSportBehavior bad_sport_behavior = 20;
  }
  optional string id = 1;
  optional .chesscom.game_storage.v1.PlayerType type = 2;
  optional .chesscom.game_stor
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05806"></a>
## FND-05806: oneof declaration: chesscom.game_storage.v1.Player._dw_incident_logged

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _dw_incident_logged {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7455.

```text
  oneof _fide_id {
  uint64 fide_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v1.PlayerBadSportBehavior bad_sport_behavior = 20;
  }
  optional string id = 1;
  optional .chesscom.game_storage.v1.PlayerType type = 2;
  optional .chesscom.game_storage.v1.PlayerProvider provider
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05807"></a>
## FND-05807: chesscom.game_storage.v1.Player.dw_incident_logged = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 dw_incident_logged = 19;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7485.

```text
de_id = 17;
  }
  oneof _min_rating {
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v1.PlayerBadSportBehavior bad_sport_behavior = 20;
  }
  optional string id = 1;
  optional .chesscom.game_storage.v1.PlayerType type = 2;
  optional .chesscom.game_storage.v1.PlayerProvider provider = 3;
  optional string key = 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05808"></a>
## FND-05808: oneof declaration: chesscom.game_storage.v1.Player._bad_sport_behavior

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _bad_sport_behavior {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7523.

```text
  uint32 min_rating = 18;
  }
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v1.PlayerBadSportBehavior bad_sport_behavior = 20;
  }
  optional string id = 1;
  optional .chesscom.game_storage.v1.PlayerType type = 2;
  optional .chesscom.game_storage.v1.PlayerProvider provider = 3;
  optional string key = 4;
  optional string display_handle = 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05809"></a>
## FND-05809: chesscom.game_storage.v1.Player.bad_sport_behavior = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_storage.v1.PlayerBadSportBehavior bad_sport_behavior = 20;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7553.

```text
  oneof _dw_incident_logged {
  uint32 dw_incident_logged = 19;
  }
  oneof _bad_sport_behavior {
  .chesscom.game_storage.v1.PlayerBadSportBehavior bad_sport_behavior = 20;
  }
  optional string id = 1;
  optional .chesscom.game_storage.v1.PlayerType type = 2;
  optional .chesscom.game_storage.v1.PlayerProvider provider = 3;
  optional string key = 4;
  optional string display_handle = 5;
  optional string display_n
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05810"></a>
## FND-05810: chesscom.game_storage.v1.Player.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7633.

```text
_sport_behavior {
  .chesscom.game_storage.v1.PlayerBadSportBehavior bad_sport_behavior = 20;
  }
  optional string id = 1;
  optional .chesscom.game_storage.v1.PlayerType type = 2;
  optional .chesscom.game_storage.v1.PlayerProvider provider = 3;
  optional string key = 4;
  optional string display_handle = 5;
  optional string display_name = 6;
  optional .chesscom.game_storage.v1.PlayerTitle title = 7;
  optional 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05811"></a>
## FND-05811: chesscom.game_storage.v1.Player.type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.PlayerType type = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7659.

```text
com.game_storage.v1.PlayerBadSportBehavior bad_sport_behavior = 20;
  }
  optional string id = 1;
  optional .chesscom.game_storage.v1.PlayerType type = 2;
  optional .chesscom.game_storage.v1.PlayerProvider provider = 3;
  optional string key = 4;
  optional string display_handle = 5;
  optional string display_name = 6;
  optional .chesscom.game_storage.v1.PlayerTitle title = 7;
  optional string country = 8;
  opti
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05812"></a>
## FND-05812: chesscom.game_storage.v1.Player.provider = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.PlayerProvider provider = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7717.

```text
ior = 20;
  }
  optional string id = 1;
  optional .chesscom.game_storage.v1.PlayerType type = 2;
  optional .chesscom.game_storage.v1.PlayerProvider provider = 3;
  optional string key = 4;
  optional string display_handle = 5;
  optional string display_name = 6;
  optional .chesscom.game_storage.v1.PlayerTitle title = 7;
  optional string country = 8;
  optional uint32 final_rating = 9;
  optional .chesscom.game_st
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05813"></a>
## FND-05813: chesscom.game_storage.v1.Player.key = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7783.

```text
storage.v1.PlayerType type = 2;
  optional .chesscom.game_storage.v1.PlayerProvider provider = 3;
  optional string key = 4;
  optional string display_handle = 5;
  optional string display_name = 6;
  optional .chesscom.game_storage.v1.PlayerTitle title = 7;
  optional string country = 8;
  optional uint32 final_rating = 9;
  optional .chesscom.game_storage.v1.PlayerResult result = 10;
  optional uint32 place = 11;
}
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05814"></a>
## FND-05814: chesscom.game_storage.v1.Player.display_handle = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string display_handle = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7810.

```text
= 2;
  optional .chesscom.game_storage.v1.PlayerProvider provider = 3;
  optional string key = 4;
  optional string display_handle = 5;
  optional string display_name = 6;
  optional .chesscom.game_storage.v1.PlayerTitle title = 7;
  optional string country = 8;
  optional uint32 final_rating = 9;
  optional .chesscom.game_storage.v1.PlayerResult result = 10;
  optional uint32 place = 11;
}

message MasterChessGameDa
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05815"></a>
## FND-05815: chesscom.game_storage.v1.Player.display_name = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string display_name = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7848.

```text
.v1.PlayerProvider provider = 3;
  optional string key = 4;
  optional string display_handle = 5;
  optional string display_name = 6;
  optional .chesscom.game_storage.v1.PlayerTitle title = 7;
  optional string country = 8;
  optional uint32 final_rating = 9;
  optional .chesscom.game_storage.v1.PlayerResult result = 10;
  optional uint32 place = 11;
}

message MasterChessGameData {
  oneof _final_fen3 {
  string fi
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05816"></a>
## FND-05816: chesscom.game_storage.v1.Player.title = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.PlayerTitle title = 7;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7884.

```text
ptional string key = 4;
  optional string display_handle = 5;
  optional string display_name = 6;
  optional .chesscom.game_storage.v1.PlayerTitle title = 7;
  optional string country = 8;
  optional uint32 final_rating = 9;
  optional .chesscom.game_storage.v1.PlayerResult result = 10;
  optional uint32 place = 11;
}

message MasterChessGameData {
  oneof _final_fen3 {
  string final_fen3 = 7;
  }
  oneof _final_fen
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05817"></a>
## FND-05817: chesscom.game_storage.v1.Player.country = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string country = 8;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7944.

```text
;
  optional string display_name = 6;
  optional .chesscom.game_storage.v1.PlayerTitle title = 7;
  optional string country = 8;
  optional uint32 final_rating = 9;
  optional .chesscom.game_storage.v1.PlayerResult result = 10;
  optional uint32 place = 11;
}

message MasterChessGameData {
  oneof _final_fen3 {
  string final_fen3 = 7;
  }
  oneof _final_fen6 {
  string final_fen6 = 8;
  }
  optional string pgn = 1;

```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05818"></a>
## FND-05818: chesscom.game_storage.v1.Player.final_rating = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 final_rating = 9;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 7975.

```text
e = 6;
  optional .chesscom.game_storage.v1.PlayerTitle title = 7;
  optional string country = 8;
  optional uint32 final_rating = 9;
  optional .chesscom.game_storage.v1.PlayerResult result = 10;
  optional uint32 place = 11;
}

message MasterChessGameData {
  oneof _final_fen3 {
  string final_fen3 = 7;
  }
  oneof _final_fen6 {
  string final_fen6 = 8;
  }
  optional string pgn = 1;
  optional string event = 2;
  
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05819"></a>
## FND-05819: chesscom.game_storage.v1.Player.result = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.PlayerResult result = 10;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8011.

```text
rage.v1.PlayerTitle title = 7;
  optional string country = 8;
  optional uint32 final_rating = 9;
  optional .chesscom.game_storage.v1.PlayerResult result = 10;
  optional uint32 place = 11;
}

message MasterChessGameData {
  oneof _final_fen3 {
  string final_fen3 = 7;
  }
  oneof _final_fen6 {
  string final_fen6 = 8;
  }
  optional string pgn = 1;
  optional string event = 2;
  optional string site = 3;
  optional
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05820"></a>
## FND-05820: chesscom.game_storage.v1.Player.place = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 place = 11;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8074.

```text
 optional uint32 final_rating = 9;
  optional .chesscom.game_storage.v1.PlayerResult result = 10;
  optional uint32 place = 11;
}

message MasterChessGameData {
  oneof _final_fen3 {
  string final_fen3 = 7;
  }
  oneof _final_fen6 {
  string final_fen6 = 8;
  }
  optional string pgn = 1;
  optional string event = 2;
  optional string site = 3;
  optional string date = 4;
  optional string round = 5;
  optional strin
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05821"></a>
## FND-05821: message declaration: chesscom.game_storage.v1.MasterChessGameData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MasterChessGameData {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8105.

```text
 9;
  optional .chesscom.game_storage.v1.PlayerResult result = 10;
  optional uint32 place = 11;
}

message MasterChessGameData {
  oneof _final_fen3 {
  string final_fen3 = 7;
  }
  oneof _final_fen6 {
  string final_fen6 = 8;
  }
  optional string pgn = 1;
  optional string event = 2;
  optional string site = 3;
  optional string date = 4;
  optional string round = 5;
  optional string move_text = 6;
  optional str
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05822"></a>
## FND-05822: oneof declaration: chesscom.game_storage.v1.MasterChessGameData._final_fen3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _final_fen3 {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8137.

```text
orage.v1.PlayerResult result = 10;
  optional uint32 place = 11;
}

message MasterChessGameData {
  oneof _final_fen3 {
  string final_fen3 = 7;
  }
  oneof _final_fen6 {
  string final_fen6 = 8;
  }
  optional string pgn = 1;
  optional string event = 2;
  optional string site = 3;
  optional string date = 4;
  optional string round = 5;
  optional string move_text = 6;
  optional string time_control = 9;
}

message
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05823"></a>
## FND-05823: chesscom.game_storage.v1.MasterChessGameData.final_fen3 = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string final_fen3 = 7;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8159.

```text
result = 10;
  optional uint32 place = 11;
}

message MasterChessGameData {
  oneof _final_fen3 {
  string final_fen3 = 7;
  }
  oneof _final_fen6 {
  string final_fen6 = 8;
  }
  optional string pgn = 1;
  optional string event = 2;
  optional string site = 3;
  optional string date = 4;
  optional string round = 5;
  optional string move_text = 6;
  optional string time_control = 9;
}

message PlayModeGrouping {
  
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05824"></a>
## FND-05824: oneof declaration: chesscom.game_storage.v1.MasterChessGameData._final_fen6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _final_fen6 {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8188.

```text
2 place = 11;
}

message MasterChessGameData {
  oneof _final_fen3 {
  string final_fen3 = 7;
  }
  oneof _final_fen6 {
  string final_fen6 = 8;
  }
  optional string pgn = 1;
  optional string event = 2;
  optional string site = 3;
  optional string date = 4;
  optional string round = 5;
  optional string move_text = 6;
  optional string time_control = 9;
}

message PlayModeGrouping {
  repeated .chesscom.game_stora
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05825"></a>
## FND-05825: chesscom.game_storage.v1.MasterChessGameData.final_fen6 = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string final_fen6 = 8;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8210.

```text
ge MasterChessGameData {
  oneof _final_fen3 {
  string final_fen3 = 7;
  }
  oneof _final_fen6 {
  string final_fen6 = 8;
  }
  optional string pgn = 1;
  optional string event = 2;
  optional string site = 3;
  optional string date = 4;
  optional string round = 5;
  optional string move_text = 6;
  optional string time_control = 9;
}

message PlayModeGrouping {
  repeated .chesscom.game_storage.v1.Variant variants
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05826"></a>
## FND-05826: chesscom.game_storage.v1.MasterChessGameData.pgn = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string pgn = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8239.

```text
eof _final_fen3 {
  string final_fen3 = 7;
  }
  oneof _final_fen6 {
  string final_fen6 = 8;
  }
  optional string pgn = 1;
  optional string event = 2;
  optional string site = 3;
  optional string date = 4;
  optional string round = 5;
  optional string move_text = 6;
  optional string time_control = 9;
}

message PlayModeGrouping {
  repeated .chesscom.game_storage.v1.Variant variants = 1;
  repeated .chesscom.ga
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05827"></a>
## FND-05827: chesscom.game_storage.v1.MasterChessGameData.event = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string event = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8266.

```text
final_fen3 = 7;
  }
  oneof _final_fen6 {
  string final_fen6 = 8;
  }
  optional string pgn = 1;
  optional string event = 2;
  optional string site = 3;
  optional string date = 4;
  optional string round = 5;
  optional string move_text = 6;
  optional string time_control = 9;
}

message PlayModeGrouping {
  repeated .chesscom.game_storage.v1.Variant variants = 1;
  repeated .chesscom.game_storage.v1.TimeClass tim
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05828"></a>
## FND-05828: chesscom.game_storage.v1.MasterChessGameData.site = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string site = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8295.

```text
final_fen6 {
  string final_fen6 = 8;
  }
  optional string pgn = 1;
  optional string event = 2;
  optional string site = 3;
  optional string date = 4;
  optional string round = 5;
  optional string move_text = 6;
  optional string time_control = 9;
}

message PlayModeGrouping {
  repeated .chesscom.game_storage.v1.Variant variants = 1;
  repeated .chesscom.game_storage.v1.TimeClass time_classes = 2;
}

message Pla
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05829"></a>
## FND-05829: chesscom.game_storage.v1.MasterChessGameData.date = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string date = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8323.

```text
fen6 = 8;
  }
  optional string pgn = 1;
  optional string event = 2;
  optional string site = 3;
  optional string date = 4;
  optional string round = 5;
  optional string move_text = 6;
  optional string time_control = 9;
}

message PlayModeGrouping {
  repeated .chesscom.game_storage.v1.Variant variants = 1;
  repeated .chesscom.game_storage.v1.TimeClass time_classes = 2;
}

message PlayModeGroupingOptions {
}

me
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05830"></a>
## FND-05830: chesscom.game_storage.v1.MasterChessGameData.round = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string round = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8351.

```text
ing pgn = 1;
  optional string event = 2;
  optional string site = 3;
  optional string date = 4;
  optional string round = 5;
  optional string move_text = 6;
  optional string time_control = 9;
}

message PlayModeGrouping {
  repeated .chesscom.game_storage.v1.Variant variants = 1;
  repeated .chesscom.game_storage.v1.TimeClass time_classes = 2;
}

message PlayModeGroupingOptions {
}

message VsCoachGameData {
  op
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05831"></a>
## FND-05831: chesscom.game_storage.v1.MasterChessGameData.move_text = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string move_text = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8380.

```text
g event = 2;
  optional string site = 3;
  optional string date = 4;
  optional string round = 5;
  optional string move_text = 6;
  optional string time_control = 9;
}

message PlayModeGrouping {
  repeated .chesscom.game_storage.v1.Variant variants = 1;
  repeated .chesscom.game_storage.v1.TimeClass time_classes = 2;
}

message PlayModeGroupingOptions {
}

message VsCoachGameData {
  optional string coach_id = 1;
}
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05832"></a>
## FND-05832: chesscom.game_storage.v1.MasterChessGameData.time_control = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string time_control = 9;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8413.

```text
te = 3;
  optional string date = 4;
  optional string round = 5;
  optional string move_text = 6;
  optional string time_control = 9;
}

message PlayModeGrouping {
  repeated .chesscom.game_storage.v1.Variant variants = 1;
  repeated .chesscom.game_storage.v1.TimeClass time_classes = 2;
}

message PlayModeGroupingOptions {
}

message VsCoachGameData {
  optional string coach_id = 1;
}

```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05833"></a>
## FND-05833: message declaration: chesscom.game_storage.v1.PlayModeGrouping

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayModeGrouping {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8450.

```text
 optional string round = 5;
  optional string move_text = 6;
  optional string time_control = 9;
}

message PlayModeGrouping {
  repeated .chesscom.game_storage.v1.Variant variants = 1;
  repeated .chesscom.game_storage.v1.TimeClass time_classes = 2;
}

message PlayModeGroupingOptions {
}

message VsCoachGameData {
  optional string coach_id = 1;
}

```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05834"></a>
## FND-05834: chesscom.game_storage.v1.PlayModeGrouping.variants = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_storage.v1.Variant variants = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8479.

```text
 optional string move_text = 6;
  optional string time_control = 9;
}

message PlayModeGrouping {
  repeated .chesscom.game_storage.v1.Variant variants = 1;
  repeated .chesscom.game_storage.v1.TimeClass time_classes = 2;
}

message PlayModeGroupingOptions {
}

message VsCoachGameData {
  optional string coach_id = 1;
}

```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05835"></a>
## FND-05835: chesscom.game_storage.v1.PlayModeGrouping.time_classes = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.game_storage.v1.TimeClass time_classes = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8538.

```text
rol = 9;
}

message PlayModeGrouping {
  repeated .chesscom.game_storage.v1.Variant variants = 1;
  repeated .chesscom.game_storage.v1.TimeClass time_classes = 2;
}

message PlayModeGroupingOptions {
}

message VsCoachGameData {
  optional string coach_id = 1;
}

```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05836"></a>
## FND-05836: message declaration: chesscom.game_storage.v1.PlayModeGroupingOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayModeGroupingOptions {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8604.

```text
torage.v1.Variant variants = 1;
  repeated .chesscom.game_storage.v1.TimeClass time_classes = 2;
}

message PlayModeGroupingOptions {
}

message VsCoachGameData {
  optional string coach_id = 1;
}

```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05837"></a>
## FND-05837: message declaration: chesscom.game_storage.v1.VsCoachGameData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message VsCoachGameData {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8641.

```text
eated .chesscom.game_storage.v1.TimeClass time_classes = 2;
}

message PlayModeGroupingOptions {
}

message VsCoachGameData {
  optional string coach_id = 1;
}

```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05838"></a>
## FND-05838: chesscom.game_storage.v1.VsCoachGameData.coach_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coach_id = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 8669.

```text
.v1.TimeClass time_classes = 2;
}

message PlayModeGroupingOptions {
}

message VsCoachGameData {
  optional string coach_id = 1;
}

```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05839"></a>
## FND-05839: enum declaration: chesscom.game_storage.v2.GameOrigin

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameOrigin {

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 108.

```text
e: chesscom/game_storage/v2/game_origin.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIG
```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05840, FND-05841

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05840"></a>
## FND-05840: chesscom.game_storage.v2.GameOrigin.GAME_ORIGIN_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_UNSPECIFIED = 0;

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 128.

```text
rage/v2/game_origin.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH
```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05839, FND-05841

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05841"></a>
## FND-05841: chesscom.game_storage.v2.GameOrigin.GAME_ORIGIN_DIRECT_CHALLENGE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_DIRECT_CHALLENGE = 1;

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 159.

```text
ntax: proto3

package chesscom.game_storage.v2;

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 1
```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05839, FND-05840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05842"></a>
## FND-05842: chesscom.game_storage.v2.GameOrigin.GAME_ORIGIN_SEEK = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_SEEK = 2;

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 195.

```text
storage.v2;

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05839, FND-05840, FND-05841

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05843"></a>
## FND-05843: chesscom.game_storage.v2.GameOrigin.GAME_ORIGIN_POOL_SEEK = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_POOL_SEEK = 3;

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 219.

```text
igin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05839, FND-05840, FND-05841

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05844"></a>
## FND-05844: chesscom.game_storage.v2.GameOrigin.GAME_ORIGIN_START_GAME = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_START_GAME = 4;

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 248.

```text
IED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05839, FND-05840, FND-05841

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05845"></a>
## FND-05845: chesscom.game_storage.v2.GameOrigin.GAME_ORIGIN_MATCH = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_MATCH = 5;

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 278.

```text
CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05839, FND-05840, FND-05841

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05846"></a>
## FND-05846: chesscom.game_storage.v2.GameOrigin.GAME_ORIGIN_ARENA = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_ARENA = 6;

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 303.

```text
GIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05839, FND-05840, FND-05841

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05847"></a>
## FND-05847: chesscom.game_storage.v2.GameOrigin.GAME_ORIGIN_TOURNAMENT = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_TOURNAMENT = 7;

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 328.

```text
IN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05839, FND-05840, FND-05841

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05848"></a>
## FND-05848: chesscom.game_storage.v2.GameOrigin.GAME_ORIGIN_TEAM_MATCH = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_TEAM_MATCH = 8;

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 358.

```text
N_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05839, FND-05840, FND-05841

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05849"></a>
## FND-05849: chesscom.game_storage.v2.GameOrigin.GAME_ORIGIN_COMPETITION = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_COMPETITION = 9;

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 388.

```text
N_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05839, FND-05840, FND-05841

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05850"></a>
## FND-05850: chesscom.game_storage.v2.GameOrigin.GAME_ORIGIN_RECOMMENDED_MATCH = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_RECOMMENDED_MATCH = 10;

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 419.

```text
A = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05839, FND-05840, FND-05841

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05851"></a>
## FND-05851: chesscom.game_storage.v2.GameOrigin.GAME_ORIGIN_LEAGUE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_LEAGUE = 11;

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 457.

```text
 GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05839, FND-05840, FND-05841

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05852"></a>
## FND-05852: chesscom.game_storage.v2.GameOrigin.GAME_ORIGIN_SIMUL = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_SIMUL = 12;

### Evidence

- **SRC-0456** `research/proto/chesscom/game_storage/v2/game_origin.proto` — [preserved redacted evidence](../evidence/text/579e5a2ae07b8f1c85192a21d4752ada5e0393fd390b64c4a3163352ff0f3790.proto)
  Character offset 484.

```text
;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

```

**Source references:** SRC-0456, SRC-1427  
**URL references:** None independently associated  
**Related findings:** FND-05839, FND-05840, FND-05841

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05853"></a>
## FND-05853: enum declaration: chesscom.game_storage.v2.GamePrivacy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GamePrivacy {

### Evidence

- **SRC-0457** `research/proto/chesscom/game_storage/v2/game_privacy.proto` — [preserved redacted evidence](../evidence/text/5c7dacd0c77c72f1857de27f952a93409a8fce8b05ddfce7f1c997c99d6462ee.proto)
  Character offset 109.

```text
: chesscom/game_storage/v2/game_privacy.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

```

**Source references:** SRC-0457, SRC-1428  
**URL references:** None independently associated  
**Related findings:** FND-05854, FND-05855

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05854"></a>
## FND-05854: chesscom.game_storage.v2.GamePrivacy.GAME_PRIVACY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PRIVACY_UNSPECIFIED = 0;

### Evidence

- **SRC-0457** `research/proto/chesscom/game_storage/v2/game_privacy.proto` — [preserved redacted evidence](../evidence/text/5c7dacd0c77c72f1857de27f952a93409a8fce8b05ddfce7f1c997c99d6462ee.proto)
  Character offset 130.

```text
ge/v2/game_privacy.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

```

**Source references:** SRC-0457, SRC-1428  
**URL references:** None independently associated  
**Related findings:** FND-05853, FND-05855

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05855"></a>
## FND-05855: chesscom.game_storage.v2.GamePrivacy.GAME_PRIVACY_PUBLIC = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PRIVACY_PUBLIC = 1;

### Evidence

- **SRC-0457** `research/proto/chesscom/game_storage/v2/game_privacy.proto` — [preserved redacted evidence](../evidence/text/5c7dacd0c77c72f1857de27f952a93409a8fce8b05ddfce7f1c997c99d6462ee.proto)
  Character offset 162.

```text
ax: proto3

package chesscom.game_storage.v2;

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

```

**Source references:** SRC-0457, SRC-1428  
**URL references:** None independently associated  
**Related findings:** FND-05853, FND-05854

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05856"></a>
## FND-05856: chesscom.game_storage.v2.GamePrivacy.GAME_PRIVACY_PRIVATE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PRIVACY_PRIVATE = 2;

### Evidence

- **SRC-0457** `research/proto/chesscom/game_storage/v2/game_privacy.proto` — [preserved redacted evidence](../evidence/text/5c7dacd0c77c72f1857de27f952a93409a8fce8b05ddfce7f1c997c99d6462ee.proto)
  Character offset 189.

```text
m.game_storage.v2;

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

```

**Source references:** SRC-0457, SRC-1428  
**URL references:** None independently associated  
**Related findings:** FND-05853, FND-05854, FND-05855

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05857"></a>
## FND-05857: enum declaration: chesscom.game_storage.v2.GameProvider

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameProvider {

### Evidence

- **SRC-0458** `research/proto/chesscom/game_storage/v2/game_provider.proto` — [preserved redacted evidence](../evidence/text/5c64825b392eaf5cc544525d13827fd17f62d27b40dd69695c1ffa9b0d45d5f7.proto)
  Character offset 110.

```text
 chesscom/game_storage/v2/game_provider.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum GameProvider {
  GAME_PROVIDER_UNSPECIFIED = 0;
  GAME_PROVIDER_CHESS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

```

**Source references:** SRC-0458, SRC-1429  
**URL references:** None independently associated  
**Related findings:** FND-05858, FND-05859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05858"></a>
## FND-05858: chesscom.game_storage.v2.GameProvider.GAME_PROVIDER_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_UNSPECIFIED = 0;

### Evidence

- **SRC-0458** `research/proto/chesscom/game_storage/v2/game_provider.proto` — [preserved redacted evidence](../evidence/text/5c64825b392eaf5cc544525d13827fd17f62d27b40dd69695c1ffa9b0d45d5f7.proto)
  Character offset 132.

```text
/v2/game_provider.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum GameProvider {
  GAME_PROVIDER_UNSPECIFIED = 0;
  GAME_PROVIDER_CHESS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

```

**Source references:** SRC-0458, SRC-1429  
**URL references:** None independently associated  
**Related findings:** FND-05857, FND-05859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05859"></a>
## FND-05859: chesscom.game_storage.v2.GameProvider.GAME_PROVIDER_CHESS_COM = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_CHESS_COM = 1;

### Evidence

- **SRC-0458** `research/proto/chesscom/game_storage/v2/game_provider.proto` — [preserved redacted evidence](../evidence/text/5c64825b392eaf5cc544525d13827fd17f62d27b40dd69695c1ffa9b0d45d5f7.proto)
  Character offset 165.

```text
: proto3

package chesscom.game_storage.v2;

enum GameProvider {
  GAME_PROVIDER_UNSPECIFIED = 0;
  GAME_PROVIDER_CHESS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

```

**Source references:** SRC-0458, SRC-1429  
**URL references:** None independently associated  
**Related findings:** FND-05857, FND-05858

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05860"></a>
## FND-05860: chesscom.game_storage.v2.GameProvider.GAME_PROVIDER_CHESS_KID = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_CHESS_KID = 2;

### Evidence

- **SRC-0458** `research/proto/chesscom/game_storage/v2/game_provider.proto` — [preserved redacted evidence](../evidence/text/5c64825b392eaf5cc544525d13827fd17f62d27b40dd69695c1ffa9b0d45d5f7.proto)
  Character offset 196.

```text
_storage.v2;

enum GameProvider {
  GAME_PROVIDER_UNSPECIFIED = 0;
  GAME_PROVIDER_CHESS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

```

**Source references:** SRC-0458, SRC-1429  
**URL references:** None independently associated  
**Related findings:** FND-05857, FND-05858, FND-05859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05861"></a>
## FND-05861: chesscom.game_storage.v2.GameProvider.GAME_PROVIDER_FIDE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_FIDE = 3;

### Evidence

- **SRC-0458** `research/proto/chesscom/game_storage/v2/game_provider.proto` — [preserved redacted evidence](../evidence/text/5c64825b392eaf5cc544525d13827fd17f62d27b40dd69695c1ffa9b0d45d5f7.proto)
  Character offset 227.

```text
 {
  GAME_PROVIDER_UNSPECIFIED = 0;
  GAME_PROVIDER_CHESS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

```

**Source references:** SRC-0458, SRC-1429  
**URL references:** None independently associated  
**Related findings:** FND-05857, FND-05858, FND-05859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05862"></a>
## FND-05862: chesscom.game_storage.v2.GameProvider.GAME_PROVIDER_LICHESS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_LICHESS = 4;

### Evidence

- **SRC-0458** `research/proto/chesscom/game_storage/v2/game_provider.proto` — [preserved redacted evidence](../evidence/text/5c64825b392eaf5cc544525d13827fd17f62d27b40dd69695c1ffa9b0d45d5f7.proto)
  Character offset 253.

```text
FIED = 0;
  GAME_PROVIDER_CHESS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

```

**Source references:** SRC-0458, SRC-1429  
**URL references:** None independently associated  
**Related findings:** FND-05857, FND-05858, FND-05859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05863"></a>
## FND-05863: chesscom.game_storage.v2.GameProvider.GAME_PROVIDER_CHESSBASE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_CHESSBASE = 5;

### Evidence

- **SRC-0458** `research/proto/chesscom/game_storage/v2/game_provider.proto` — [preserved redacted evidence](../evidence/text/5c64825b392eaf5cc544525d13827fd17f62d27b40dd69695c1ffa9b0d45d5f7.proto)
  Character offset 282.

```text
SS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

```

**Source references:** SRC-0458, SRC-1429  
**URL references:** None independently associated  
**Related findings:** FND-05857, FND-05858, FND-05859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05864"></a>
## FND-05864: chesscom.game_storage.v2.GameProvider.GAME_PROVIDER_OFFLINE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_OFFLINE = 6;

### Evidence

- **SRC-0458** `research/proto/chesscom/game_storage/v2/game_provider.proto` — [preserved redacted evidence](../evidence/text/5c64825b392eaf5cc544525d13827fd17f62d27b40dd69695c1ffa9b0d45d5f7.proto)
  Character offset 313.

```text
SS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

```

**Source references:** SRC-0458, SRC-1429  
**URL references:** None independently associated  
**Related findings:** FND-05857, FND-05858, FND-05859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05865"></a>
## FND-05865: chesscom.game_storage.v2.GameProvider.GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;

### Evidence

- **SRC-0458** `research/proto/chesscom/game_storage/v2/game_provider.proto` — [preserved redacted evidence](../evidence/text/5c64825b392eaf5cc544525d13827fd17f62d27b40dd69695c1ffa9b0d45d5f7.proto)
  Character offset 342.

```text
IDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

```

**Source references:** SRC-0458, SRC-1429  
**URL references:** None independently associated  
**Related findings:** FND-05857, FND-05858, FND-05859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05866"></a>
## FND-05866: enum declaration: chesscom.game_storage.v2.GameResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameResult {

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 108.

```text
e: chesscom/game_storage/v2/game_result.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMAT
```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05867"></a>
## FND-05867: chesscom.game_storage.v2.GameResult.GAME_RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 128.

```text
rage/v2/game_result.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT
```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05868"></a>
## FND-05868: chesscom.game_storage.v2.GameResult.GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 159.

```text
ntax: proto3

package chesscom.game_storage.v2;

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL 
```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05869"></a>
## FND-05869: chesscom.game_storage.v2.GameResult.GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 198.

```text
rage.v2;

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_I
```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05870"></a>
## FND-05870: chesscom.game_storage.v2.GameResult.GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 239.

```text
_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_D
```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05871"></a>
## FND-05871: chesscom.game_storage.v2.GameResult.GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 282.

```text
_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN
```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05872"></a>
## FND-05872: chesscom.game_storage.v2.GameResult.GAME_RESULT_DRAW_BY_AGREEMENT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_DRAW_BY_AGREEMENT = 5;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 325.

```text
CKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME
```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05873"></a>
## FND-05873: chesscom.game_storage.v2.GameResult.GAME_RESULT_DRAW_BY_REPETITION = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_DRAW_BY_REPETITION = 6;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 362.

```text
_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_W
```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05874"></a>
## FND-05874: chesscom.game_storage.v2.GameResult.GAME_RESULT_DRAW_BY_STALEMATE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_DRAW_BY_STALEMATE = 7;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 400.

```text
SE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RE
```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
