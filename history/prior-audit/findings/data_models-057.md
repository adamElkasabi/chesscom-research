# data_models — findings 5601–5700

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-05875"></a>
## FND-05875: chesscom.game_storage.v2.GameResult.GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 437.

```text
DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 1
```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05876"></a>
## FND-05876: chesscom.game_storage.v2.GameResult.GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 486.

```text
TITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05877"></a>
## FND-05877: chesscom.game_storage.v2.GameResult.GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 546.

```text
LT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05878"></a>
## FND-05878: chesscom.game_storage.v2.GameResult.GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 587.

```text
AME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05879"></a>
## FND-05879: chesscom.game_storage.v2.GameResult.GAME_RESULT_ABORTED = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_ABORTED = 12;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 641.

```text
9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05880"></a>
## FND-05880: chesscom.game_storage.v2.GameResult.GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 669.

```text
MOVE_RULE = 10;
  GAME_RESULT_WIN_LOSE_BY_BUGHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05881"></a>
## FND-05881: chesscom.game_storage.v2.GameResult.GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 713.

```text
GHOUSE_PARTNER_LOSE = 11;
  GAME_RESULT_ABORTED = 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05882"></a>
## FND-05882: chesscom.game_storage.v2.GameResult.GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;

### Evidence

- **SRC-0459** `research/proto/chesscom/game_storage/v2/game_result.proto` — [preserved redacted evidence](../evidence/text/e7b2b2ec8221364c45b5f4537af1b6ffd2a9354f2fd66d9fcdf03336de293a0d.proto)
  Character offset 762.

```text
 12;
  GAME_RESULT_WIN_LOSE_BY_THREE_CHECK = 13;
  GAME_RESULT_WIN_LOSE_BY_KING_OF_THE_HILL = 14;
  GAME_RESULT_WIN_LOSE_BY_DOUBLE_FORFEIT = 15;
}

```

**Source references:** SRC-0459, SRC-1430  
**URL references:** None independently associated  
**Related findings:** FND-05866, FND-05867, FND-05868

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05883"></a>
## FND-05883: enum declaration: chesscom.game_storage.v2.GameServer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameServer {

### Evidence

- **SRC-0460** `research/proto/chesscom/game_storage/v2/game_server.proto` — [preserved redacted evidence](../evidence/text/76607d61cf4c05ae8c7e676f83334d63fbef02f0418320dd3885ad9e820a65e1.proto)
  Character offset 108.

```text
e: chesscom/game_storage/v2/game_server.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum GameServer {
  GAME_SERVER_UNSPECIFIED = 0;
  GAME_SERVER_RCN = 1;
  GAME_SERVER_LIVE_CHESS = 2;
  GAME_SERVER_WEB = 3;
}

```

**Source references:** SRC-0460, SRC-1431  
**URL references:** None independently associated  
**Related findings:** FND-05884, FND-05885

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05884"></a>
## FND-05884: chesscom.game_storage.v2.GameServer.GAME_SERVER_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_SERVER_UNSPECIFIED = 0;

### Evidence

- **SRC-0460** `research/proto/chesscom/game_storage/v2/game_server.proto` — [preserved redacted evidence](../evidence/text/76607d61cf4c05ae8c7e676f83334d63fbef02f0418320dd3885ad9e820a65e1.proto)
  Character offset 128.

```text
rage/v2/game_server.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum GameServer {
  GAME_SERVER_UNSPECIFIED = 0;
  GAME_SERVER_RCN = 1;
  GAME_SERVER_LIVE_CHESS = 2;
  GAME_SERVER_WEB = 3;
}

```

**Source references:** SRC-0460, SRC-1431  
**URL references:** None independently associated  
**Related findings:** FND-05883, FND-05885

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05885"></a>
## FND-05885: chesscom.game_storage.v2.GameServer.GAME_SERVER_RCN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_SERVER_RCN = 1;

### Evidence

- **SRC-0460** `research/proto/chesscom/game_storage/v2/game_server.proto` — [preserved redacted evidence](../evidence/text/76607d61cf4c05ae8c7e676f83334d63fbef02f0418320dd3885ad9e820a65e1.proto)
  Character offset 159.

```text
ntax: proto3

package chesscom.game_storage.v2;

enum GameServer {
  GAME_SERVER_UNSPECIFIED = 0;
  GAME_SERVER_RCN = 1;
  GAME_SERVER_LIVE_CHESS = 2;
  GAME_SERVER_WEB = 3;
}

```

**Source references:** SRC-0460, SRC-1431  
**URL references:** None independently associated  
**Related findings:** FND-05883, FND-05884

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05886"></a>
## FND-05886: chesscom.game_storage.v2.GameServer.GAME_SERVER_LIVE_CHESS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_SERVER_LIVE_CHESS = 2;

### Evidence

- **SRC-0460** `research/proto/chesscom/game_storage/v2/game_server.proto` — [preserved redacted evidence](../evidence/text/76607d61cf4c05ae8c7e676f83334d63fbef02f0418320dd3885ad9e820a65e1.proto)
  Character offset 182.

```text
hesscom.game_storage.v2;

enum GameServer {
  GAME_SERVER_UNSPECIFIED = 0;
  GAME_SERVER_RCN = 1;
  GAME_SERVER_LIVE_CHESS = 2;
  GAME_SERVER_WEB = 3;
}

```

**Source references:** SRC-0460, SRC-1431  
**URL references:** None independently associated  
**Related findings:** FND-05883, FND-05884, FND-05885

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05887"></a>
## FND-05887: chesscom.game_storage.v2.GameServer.GAME_SERVER_WEB = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_SERVER_WEB = 3;

### Evidence

- **SRC-0460** `research/proto/chesscom/game_storage/v2/game_server.proto` — [preserved redacted evidence](../evidence/text/76607d61cf4c05ae8c7e676f83334d63fbef02f0418320dd3885ad9e820a65e1.proto)
  Character offset 212.

```text
 GameServer {
  GAME_SERVER_UNSPECIFIED = 0;
  GAME_SERVER_RCN = 1;
  GAME_SERVER_LIVE_CHESS = 2;
  GAME_SERVER_WEB = 3;
}

```

**Source references:** SRC-0460, SRC-1431  
**URL references:** None independently associated  
**Related findings:** FND-05883, FND-05884, FND-05885

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05888"></a>
## FND-05888: message declaration: chesscom.game_storage.v2.OpeningData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message OpeningData {

### Evidence

- **SRC-0461** `research/proto/chesscom/game_storage/v2/opening_data.proto` — [preserved redacted evidence](../evidence/text/a39948ef35974490fffdd3096f41b30325934392311087d393a5d4d600ea80a0.proto)
  Character offset 109.

```text
: chesscom/game_storage/v2/opening_data.proto
// syntax: proto3

package chesscom.game_storage.v2;

message OpeningData {
  oneof _last_book_eco_id {
  uint32 last_book_eco_id = 1;
  }
  oneof _last_book_ply {
  uint32 last_book_ply = 2;
  }
  oneof _last_notable_eco_id {
  uint32 last_notable_eco_id = 3;
  }
  oneof _last_notable_ply {
  uint32 last_notable_ply = 4;
  }
  optional uint32 eco_family_id = 5;
  optiona
```

**Source references:** SRC-0461, SRC-1432  
**URL references:** None independently associated  
**Related findings:** FND-05889, FND-05890

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05889"></a>
## FND-05889: oneof declaration: chesscom.game_storage.v2.OpeningData._last_book_eco_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_book_eco_id {

### Evidence

- **SRC-0461** `research/proto/chesscom/game_storage/v2/opening_data.proto` — [preserved redacted evidence](../evidence/text/a39948ef35974490fffdd3096f41b30325934392311087d393a5d4d600ea80a0.proto)
  Character offset 133.

```text
v2/opening_data.proto
// syntax: proto3

package chesscom.game_storage.v2;

message OpeningData {
  oneof _last_book_eco_id {
  uint32 last_book_eco_id = 1;
  }
  oneof _last_book_ply {
  uint32 last_book_ply = 2;
  }
  oneof _last_notable_eco_id {
  uint32 last_notable_eco_id = 3;
  }
  oneof _last_notable_ply {
  uint32 last_notable_ply = 4;
  }
  optional uint32 eco_family_id = 5;
  optional string eco_code = 6;
}
```

**Source references:** SRC-0461, SRC-1432  
**URL references:** None independently associated  
**Related findings:** FND-05888, FND-05890

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05890"></a>
## FND-05890: chesscom.game_storage.v2.OpeningData.last_book_eco_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 last_book_eco_id = 1;

### Evidence

- **SRC-0461** `research/proto/chesscom/game_storage/v2/opening_data.proto` — [preserved redacted evidence](../evidence/text/a39948ef35974490fffdd3096f41b30325934392311087d393a5d4d600ea80a0.proto)
  Character offset 161.

```text
tax: proto3

package chesscom.game_storage.v2;

message OpeningData {
  oneof _last_book_eco_id {
  uint32 last_book_eco_id = 1;
  }
  oneof _last_book_ply {
  uint32 last_book_ply = 2;
  }
  oneof _last_notable_eco_id {
  uint32 last_notable_eco_id = 3;
  }
  oneof _last_notable_ply {
  uint32 last_notable_ply = 4;
  }
  optional uint32 eco_family_id = 5;
  optional string eco_code = 6;
}

```

**Source references:** SRC-0461, SRC-1432  
**URL references:** None independently associated  
**Related findings:** FND-05888, FND-05889

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05891"></a>
## FND-05891: oneof declaration: chesscom.game_storage.v2.OpeningData._last_book_ply

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_book_ply {

### Evidence

- **SRC-0461** `research/proto/chesscom/game_storage/v2/opening_data.proto` — [preserved redacted evidence](../evidence/text/a39948ef35974490fffdd3096f41b30325934392311087d393a5d4d600ea80a0.proto)
  Character offset 196.

```text
storage.v2;

message OpeningData {
  oneof _last_book_eco_id {
  uint32 last_book_eco_id = 1;
  }
  oneof _last_book_ply {
  uint32 last_book_ply = 2;
  }
  oneof _last_notable_eco_id {
  uint32 last_notable_eco_id = 3;
  }
  oneof _last_notable_ply {
  uint32 last_notable_ply = 4;
  }
  optional uint32 eco_family_id = 5;
  optional string eco_code = 6;
}

```

**Source references:** SRC-0461, SRC-1432  
**URL references:** None independently associated  
**Related findings:** FND-05888, FND-05889, FND-05890

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05892"></a>
## FND-05892: chesscom.game_storage.v2.OpeningData.last_book_ply = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 last_book_ply = 2;

### Evidence

- **SRC-0461** `research/proto/chesscom/game_storage/v2/opening_data.proto` — [preserved redacted evidence](../evidence/text/a39948ef35974490fffdd3096f41b30325934392311087d393a5d4d600ea80a0.proto)
  Character offset 221.

```text
ingData {
  oneof _last_book_eco_id {
  uint32 last_book_eco_id = 1;
  }
  oneof _last_book_ply {
  uint32 last_book_ply = 2;
  }
  oneof _last_notable_eco_id {
  uint32 last_notable_eco_id = 3;
  }
  oneof _last_notable_ply {
  uint32 last_notable_ply = 4;
  }
  optional uint32 eco_family_id = 5;
  optional string eco_code = 6;
}

```

**Source references:** SRC-0461, SRC-1432  
**URL references:** None independently associated  
**Related findings:** FND-05888, FND-05889, FND-05890

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05893"></a>
## FND-05893: oneof declaration: chesscom.game_storage.v2.OpeningData._last_notable_eco_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_notable_eco_id {

### Evidence

- **SRC-0461** `research/proto/chesscom/game_storage/v2/opening_data.proto` — [preserved redacted evidence](../evidence/text/a39948ef35974490fffdd3096f41b30325934392311087d393a5d4d600ea80a0.proto)
  Character offset 253.

```text
_id {
  uint32 last_book_eco_id = 1;
  }
  oneof _last_book_ply {
  uint32 last_book_ply = 2;
  }
  oneof _last_notable_eco_id {
  uint32 last_notable_eco_id = 3;
  }
  oneof _last_notable_ply {
  uint32 last_notable_ply = 4;
  }
  optional uint32 eco_family_id = 5;
  optional string eco_code = 6;
}

```

**Source references:** SRC-0461, SRC-1432  
**URL references:** None independently associated  
**Related findings:** FND-05888, FND-05889, FND-05890

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05894"></a>
## FND-05894: chesscom.game_storage.v2.OpeningData.last_notable_eco_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 last_notable_eco_id = 3;

### Evidence

- **SRC-0461** `research/proto/chesscom/game_storage/v2/opening_data.proto` — [preserved redacted evidence](../evidence/text/a39948ef35974490fffdd3096f41b30325934392311087d393a5d4d600ea80a0.proto)
  Character offset 284.

```text
 = 1;
  }
  oneof _last_book_ply {
  uint32 last_book_ply = 2;
  }
  oneof _last_notable_eco_id {
  uint32 last_notable_eco_id = 3;
  }
  oneof _last_notable_ply {
  uint32 last_notable_ply = 4;
  }
  optional uint32 eco_family_id = 5;
  optional string eco_code = 6;
}

```

**Source references:** SRC-0461, SRC-1432  
**URL references:** None independently associated  
**Related findings:** FND-05888, FND-05889, FND-05890

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05895"></a>
## FND-05895: oneof declaration: chesscom.game_storage.v2.OpeningData._last_notable_ply

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_notable_ply {

### Evidence

- **SRC-0461** `research/proto/chesscom/game_storage/v2/opening_data.proto` — [preserved redacted evidence](../evidence/text/a39948ef35974490fffdd3096f41b30325934392311087d393a5d4d600ea80a0.proto)
  Character offset 322.

```text
int32 last_book_ply = 2;
  }
  oneof _last_notable_eco_id {
  uint32 last_notable_eco_id = 3;
  }
  oneof _last_notable_ply {
  uint32 last_notable_ply = 4;
  }
  optional uint32 eco_family_id = 5;
  optional string eco_code = 6;
}

```

**Source references:** SRC-0461, SRC-1432  
**URL references:** None independently associated  
**Related findings:** FND-05888, FND-05889, FND-05890

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05896"></a>
## FND-05896: chesscom.game_storage.v2.OpeningData.last_notable_ply = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 last_notable_ply = 4;

### Evidence

- **SRC-0461** `research/proto/chesscom/game_storage/v2/opening_data.proto` — [preserved redacted evidence](../evidence/text/a39948ef35974490fffdd3096f41b30325934392311087d393a5d4d600ea80a0.proto)
  Character offset 350.

```text

  oneof _last_notable_eco_id {
  uint32 last_notable_eco_id = 3;
  }
  oneof _last_notable_ply {
  uint32 last_notable_ply = 4;
  }
  optional uint32 eco_family_id = 5;
  optional string eco_code = 6;
}

```

**Source references:** SRC-0461, SRC-1432  
**URL references:** None independently associated  
**Related findings:** FND-05888, FND-05889, FND-05890

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05897"></a>
## FND-05897: chesscom.game_storage.v2.OpeningData.eco_family_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 eco_family_id = 5;

### Evidence

- **SRC-0461** `research/proto/chesscom/game_storage/v2/opening_data.proto` — [preserved redacted evidence](../evidence/text/a39948ef35974490fffdd3096f41b30325934392311087d393a5d4d600ea80a0.proto)
  Character offset 385.

```text
int32 last_notable_eco_id = 3;
  }
  oneof _last_notable_ply {
  uint32 last_notable_ply = 4;
  }
  optional uint32 eco_family_id = 5;
  optional string eco_code = 6;
}

```

**Source references:** SRC-0461, SRC-1432  
**URL references:** None independently associated  
**Related findings:** FND-05888, FND-05889, FND-05890

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05898"></a>
## FND-05898: chesscom.game_storage.v2.OpeningData.eco_code = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string eco_code = 6;

### Evidence

- **SRC-0461** `research/proto/chesscom/game_storage/v2/opening_data.proto` — [preserved redacted evidence](../evidence/text/a39948ef35974490fffdd3096f41b30325934392311087d393a5d4d600ea80a0.proto)
  Character offset 422.

```text
oneof _last_notable_ply {
  uint32 last_notable_ply = 4;
  }
  optional uint32 eco_family_id = 5;
  optional string eco_code = 6;
}

```

**Source references:** SRC-0461, SRC-1432  
**URL references:** None independently associated  
**Related findings:** FND-05888, FND-05889, FND-05890

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05899"></a>
## FND-05899: enum declaration: chesscom.game_storage.v2.PlayerBadSportBehavior

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayerBadSportBehavior {

### Evidence

- **SRC-0462** `research/proto/chesscom/game_storage/v2/player_bad_sport_behavior.proto` — [preserved redacted evidence](../evidence/text/dfe3f86da8323ef168305386610db54aaee3340a128514aae71cbf7b68122bf5.proto)
  Character offset 122.

```text
me_storage/v2/player_bad_sport_behavior.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIO
```

**Source references:** SRC-0462, SRC-1433  
**URL references:** None independently associated  
**Related findings:** FND-05900, FND-05901

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05900"></a>
## FND-05900: chesscom.game_storage.v2.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;

### Evidence

- **SRC-0462** `research/proto/chesscom/game_storage/v2/player_bad_sport_behavior.proto` — [preserved redacted evidence](../evidence/text/dfe3f86da8323ef168305386610db54aaee3340a128514aae71cbf7b68122bf5.proto)
  Character offset 154.

```text
ehavior.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_
```

**Source references:** SRC-0462, SRC-1433  
**URL references:** None independently associated  
**Related findings:** FND-05899, FND-05901

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05901"></a>
## FND-05901: chesscom.game_storage.v2.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;

### Evidence

- **SRC-0462** `research/proto/chesscom/game_storage/v2/player_bad_sport_behavior.proto` — [preserved redacted evidence](../evidence/text/dfe3f86da8323ef168305386610db54aaee3340a128514aae71cbf7b68122bf5.proto)
  Character offset 199.

```text
scom.game_storage.v2;

enum PlayerBadSportBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED 
```

**Source references:** SRC-0462, SRC-1433  
**URL references:** None independently associated  
**Related findings:** FND-05899, FND-05900

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05902"></a>
## FND-05902: chesscom.game_storage.v2.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;

### Evidence

- **SRC-0462** `research/proto/chesscom/game_storage/v2/player_bad_sport_behavior.proto` — [preserved redacted evidence](../evidence/text/dfe3f86da8323ef168305386610db54aaee3340a128514aae71cbf7b68122bf5.proto)
  Character offset 237.

```text
portBehavior {
  PLAYER_BAD_SPORT_BEHAVIOR_UNSPECIFIED = 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

```

**Source references:** SRC-0462, SRC-1433  
**URL references:** None independently associated  
**Related findings:** FND-05899, FND-05900, FND-05901

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05903"></a>
## FND-05903: chesscom.game_storage.v2.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;

### Evidence

- **SRC-0462** `research/proto/chesscom/game_storage/v2/player_bad_sport_behavior.proto` — [preserved redacted evidence](../evidence/text/dfe3f86da8323ef168305386610db54aaee3340a128514aae71cbf7b68122bf5.proto)
  Character offset 292.

```text
= 0;
  PLAYER_BAD_SPORT_BEHAVIOR_NONE = 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

```

**Source references:** SRC-0462, SRC-1433  
**URL references:** None independently associated  
**Related findings:** FND-05899, FND-05900, FND-05901

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05904"></a>
## FND-05904: chesscom.game_storage.v2.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;

### Evidence

- **SRC-0462** `research/proto/chesscom/game_storage/v2/player_bad_sport_behavior.proto` — [preserved redacted evidence](../evidence/text/dfe3f86da8323ef168305386610db54aaee3340a128514aae71cbf7b68122bf5.proto)
  Character offset 331.

```text
 1;
  PLAYER_BAD_SPORT_BEHAVIOR_FIRST_MOVE_NOT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

```

**Source references:** SRC-0462, SRC-1433  
**URL references:** None independently associated  
**Related findings:** FND-05899, FND-05900, FND-05901

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05905"></a>
## FND-05905: chesscom.game_storage.v2.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;

### Evidence

- **SRC-0462** `research/proto/chesscom/game_storage/v2/player_bad_sport_behavior.proto` — [preserved redacted evidence](../evidence/text/dfe3f86da8323ef168305386610db54aaee3340a128514aae71cbf7b68122bf5.proto)
  Character offset 375.

```text
OT_PLAYED = 2;
  PLAYER_BAD_SPORT_BEHAVIOR_ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

```

**Source references:** SRC-0462, SRC-1433  
**URL references:** None independently associated  
**Related findings:** FND-05899, FND-05900, FND-05901

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05906"></a>
## FND-05906: chesscom.game_storage.v2.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;

### Evidence

- **SRC-0462** `research/proto/chesscom/game_storage/v2/player_bad_sport_behavior.proto` — [preserved redacted evidence](../evidence/text/dfe3f86da8323ef168305386610db54aaee3340a128514aae71cbf7b68122bf5.proto)
  Character offset 418.

```text
ABORT = 3;
  PLAYER_BAD_SPORT_BEHAVIOR_DISCONNECT = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

```

**Source references:** SRC-0462, SRC-1433  
**URL references:** None independently associated  
**Related findings:** FND-05899, FND-05900, FND-05901

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05907"></a>
## FND-05907: chesscom.game_storage.v2.PlayerBadSportBehavior.PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;

### Evidence

- **SRC-0462** `research/proto/chesscom/game_storage/v2/player_bad_sport_behavior.proto` — [preserved redacted evidence](../evidence/text/dfe3f86da8323ef168305386610db54aaee3340a128514aae71cbf7b68122bf5.proto)
  Character offset 467.

```text
 = 4;
  PLAYER_BAD_SPORT_BEHAVIOR_RAGE_QUIT = 5;
  PLAYER_BAD_SPORT_BEHAVIOR_MOVE_NOT_PLAYED = 6;
  PLAYER_BAD_SPORT_BEHAVIOR_BOTH_PLAYERS_DISCONNECTED = 7;
}

```

**Source references:** SRC-0462, SRC-1433  
**URL references:** None independently associated  
**Related findings:** FND-05899, FND-05900, FND-05901

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05908"></a>
## FND-05908: enum declaration: chesscom.game_storage.v2.PlayerProvider

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayerProvider {

### Evidence

- **SRC-0463** `research/proto/chesscom/game_storage/v2/player_provider.proto` — [preserved redacted evidence](../evidence/text/0f0a7a0ef5402a4a38f73e4d15c3ebc92faf4b1b56fa22bf59f119d2aaa42714.proto)
  Character offset 112.

```text
hesscom/game_storage/v2/player_provider.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

```

**Source references:** SRC-0463, SRC-1434  
**URL references:** None independently associated  
**Related findings:** FND-05909, FND-05910

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05909"></a>
## FND-05909: chesscom.game_storage.v2.PlayerProvider.PLAYER_PROVIDER_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_UNSPECIFIED = 0;

### Evidence

- **SRC-0463** `research/proto/chesscom/game_storage/v2/player_provider.proto` — [preserved redacted evidence](../evidence/text/0f0a7a0ef5402a4a38f73e4d15c3ebc92faf4b1b56fa22bf59f119d2aaa42714.proto)
  Character offset 136.

```text
player_provider.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

```

**Source references:** SRC-0463, SRC-1434  
**URL references:** None independently associated  
**Related findings:** FND-05908, FND-05910

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05910"></a>
## FND-05910: chesscom.game_storage.v2.PlayerProvider.PLAYER_PROVIDER_CHESS_COM = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_CHESS_COM = 1;

### Evidence

- **SRC-0463** `research/proto/chesscom/game_storage/v2/player_provider.proto` — [preserved redacted evidence](../evidence/text/0f0a7a0ef5402a4a38f73e4d15c3ebc92faf4b1b56fa22bf59f119d2aaa42714.proto)
  Character offset 171.

```text
oto3

package chesscom.game_storage.v2;

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

```

**Source references:** SRC-0463, SRC-1434  
**URL references:** None independently associated  
**Related findings:** FND-05908, FND-05909

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05911"></a>
## FND-05911: chesscom.game_storage.v2.PlayerProvider.PLAYER_PROVIDER_CHESS_KID = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_CHESS_KID = 2;

### Evidence

- **SRC-0463** `research/proto/chesscom/game_storage/v2/player_provider.proto` — [preserved redacted evidence](../evidence/text/0f0a7a0ef5402a4a38f73e4d15c3ebc92faf4b1b56fa22bf59f119d2aaa42714.proto)
  Character offset 204.

```text
ge.v2;

enum PlayerProvider {
  PLAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

```

**Source references:** SRC-0463, SRC-1434  
**URL references:** None independently associated  
**Related findings:** FND-05908, FND-05909, FND-05910

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05912"></a>
## FND-05912: chesscom.game_storage.v2.PlayerProvider.PLAYER_PROVIDER_FIDE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_FIDE = 3;

### Evidence

- **SRC-0463** `research/proto/chesscom/game_storage/v2/player_provider.proto` — [preserved redacted evidence](../evidence/text/0f0a7a0ef5402a4a38f73e4d15c3ebc92faf4b1b56fa22bf59f119d2aaa42714.proto)
  Character offset 237.

```text
LAYER_PROVIDER_UNSPECIFIED = 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

```

**Source references:** SRC-0463, SRC-1434  
**URL references:** None independently associated  
**Related findings:** FND-05908, FND-05909, FND-05910

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05913"></a>
## FND-05913: chesscom.game_storage.v2.PlayerProvider.PLAYER_PROVIDER_LICHESS_ORG = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_LICHESS_ORG = 4;

### Evidence

- **SRC-0463** `research/proto/chesscom/game_storage/v2/player_provider.proto` — [preserved redacted evidence](../evidence/text/0f0a7a0ef5402a4a38f73e4d15c3ebc92faf4b1b56fa22bf59f119d2aaa42714.proto)
  Character offset 265.

```text
 0;
  PLAYER_PROVIDER_CHESS_COM = 1;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

```

**Source references:** SRC-0463, SRC-1434  
**URL references:** None independently associated  
**Related findings:** FND-05908, FND-05909, FND-05910

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05914"></a>
## FND-05914: chesscom.game_storage.v2.PlayerProvider.PLAYER_PROVIDER_CHESSBASE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_CHESSBASE = 5;

### Evidence

- **SRC-0463** `research/proto/chesscom/game_storage/v2/player_provider.proto` — [preserved redacted evidence](../evidence/text/0f0a7a0ef5402a4a38f73e4d15c3ebc92faf4b1b56fa22bf59f119d2aaa42714.proto)
  Character offset 300.

```text
;
  PLAYER_PROVIDER_CHESS_KID = 2;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

```

**Source references:** SRC-0463, SRC-1434  
**URL references:** None independently associated  
**Related findings:** FND-05908, FND-05909, FND-05910

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05915"></a>
## FND-05915: chesscom.game_storage.v2.PlayerProvider.PLAYER_PROVIDER_CHESS_COM_MASTER = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_PROVIDER_CHESS_COM_MASTER = 6;

### Evidence

- **SRC-0463** `research/proto/chesscom/game_storage/v2/player_provider.proto` — [preserved redacted evidence](../evidence/text/0f0a7a0ef5402a4a38f73e4d15c3ebc92faf4b1b56fa22bf59f119d2aaa42714.proto)
  Character offset 333.

```text
;
  PLAYER_PROVIDER_FIDE = 3;
  PLAYER_PROVIDER_LICHESS_ORG = 4;
  PLAYER_PROVIDER_CHESSBASE = 5;
  PLAYER_PROVIDER_CHESS_COM_MASTER = 6;
}

```

**Source references:** SRC-0463, SRC-1434  
**URL references:** None independently associated  
**Related findings:** FND-05908, FND-05909, FND-05910

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05916"></a>
## FND-05916: enum declaration: chesscom.game_storage.v2.PlayerResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayerResult {

### Evidence

- **SRC-0464** `research/proto/chesscom/game_storage/v2/player_result.proto` — [preserved redacted evidence](../evidence/text/c55ebe6899e840934fd9473a6477144bbf32a212bffe3f047a3cd2f4c92a3092.proto)
  Character offset 110.

```text
 chesscom/game_storage/v2/player_result.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

```

**Source references:** SRC-0464, SRC-1435  
**URL references:** None independently associated  
**Related findings:** FND-05917, FND-05918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05917"></a>
## FND-05917: chesscom.game_storage.v2.PlayerResult.PLAYER_RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0464** `research/proto/chesscom/game_storage/v2/player_result.proto` — [preserved redacted evidence](../evidence/text/c55ebe6899e840934fd9473a6477144bbf32a212bffe3f047a3cd2f4c92a3092.proto)
  Character offset 132.

```text
/v2/player_result.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

```

**Source references:** SRC-0464, SRC-1435  
**URL references:** None independently associated  
**Related findings:** FND-05916, FND-05918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05918"></a>
## FND-05918: chesscom.game_storage.v2.PlayerResult.PLAYER_RESULT_WIN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_RESULT_WIN = 1;

### Evidence

- **SRC-0464** `research/proto/chesscom/game_storage/v2/player_result.proto` — [preserved redacted evidence](../evidence/text/c55ebe6899e840934fd9473a6477144bbf32a212bffe3f047a3cd2f4c92a3092.proto)
  Character offset 165.

```text
: proto3

package chesscom.game_storage.v2;

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

```

**Source references:** SRC-0464, SRC-1435  
**URL references:** None independently associated  
**Related findings:** FND-05916, FND-05917

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05919"></a>
## FND-05919: chesscom.game_storage.v2.PlayerResult.PLAYER_RESULT_DRAW = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_RESULT_DRAW = 2;

### Evidence

- **SRC-0464** `research/proto/chesscom/game_storage/v2/player_result.proto` — [preserved redacted evidence](../evidence/text/c55ebe6899e840934fd9473a6477144bbf32a212bffe3f047a3cd2f4c92a3092.proto)
  Character offset 190.

```text
m.game_storage.v2;

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

```

**Source references:** SRC-0464, SRC-1435  
**URL references:** None independently associated  
**Related findings:** FND-05916, FND-05917, FND-05918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05920"></a>
## FND-05920: chesscom.game_storage.v2.PlayerResult.PLAYER_RESULT_LOSE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_RESULT_LOSE = 3;

### Evidence

- **SRC-0464** `research/proto/chesscom/game_storage/v2/player_result.proto` — [preserved redacted evidence](../evidence/text/c55ebe6899e840934fd9473a6477144bbf32a212bffe3f047a3cd2f4c92a3092.proto)
  Character offset 216.

```text
layerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

```

**Source references:** SRC-0464, SRC-1435  
**URL references:** None independently associated  
**Related findings:** FND-05916, FND-05917, FND-05918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05921"></a>
## FND-05921: chesscom.game_storage.v2.PlayerResult.PLAYER_RESULT_ABORT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_RESULT_ABORT = 4;

### Evidence

- **SRC-0464** `research/proto/chesscom/game_storage/v2/player_result.proto` — [preserved redacted evidence](../evidence/text/c55ebe6899e840934fd9473a6477144bbf32a212bffe3f047a3cd2f4c92a3092.proto)
  Character offset 242.

```text
ULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

```

**Source references:** SRC-0464, SRC-1435  
**URL references:** None independently associated  
**Related findings:** FND-05916, FND-05917, FND-05918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05922"></a>
## FND-05922: chesscom.game_storage.v2.PlayerResult.PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;

### Evidence

- **SRC-0464** `research/proto/chesscom/game_storage/v2/player_result.proto` — [preserved redacted evidence](../evidence/text/c55ebe6899e840934fd9473a6477144bbf32a212bffe3f047a3cd2f4c92a3092.proto)
  Character offset 269.

```text
ER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

```

**Source references:** SRC-0464, SRC-1435  
**URL references:** None independently associated  
**Related findings:** FND-05916, FND-05917, FND-05918

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05923"></a>
## FND-05923: enum declaration: chesscom.game_storage.v2.PlayerTitle

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayerTitle {

### Evidence

- **SRC-0465** `research/proto/chesscom/game_storage/v2/player_title.proto` — [preserved redacted evidence](../evidence/text/67ae51f0ff7cd45fbe865383ae5daedd13b7b51596bc4e848288c0b4b442aca2.proto)
  Character offset 109.

```text
: chesscom/game_storage/v2/player_title.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

```

**Source references:** SRC-0465, SRC-1436  
**URL references:** None independently associated  
**Related findings:** FND-05924, FND-05925

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05924"></a>
## FND-05924: chesscom.game_storage.v2.PlayerTitle.PLAYER_TITLE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_UNSPECIFIED = 0;

### Evidence

- **SRC-0465** `research/proto/chesscom/game_storage/v2/player_title.proto` — [preserved redacted evidence](../evidence/text/67ae51f0ff7cd45fbe865383ae5daedd13b7b51596bc4e848288c0b4b442aca2.proto)
  Character offset 130.

```text
ge/v2/player_title.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

```

**Source references:** SRC-0465, SRC-1436  
**URL references:** None independently associated  
**Related findings:** FND-05923, FND-05925

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05925"></a>
## FND-05925: chesscom.game_storage.v2.PlayerTitle.PLAYER_TITLE_WGM = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_WGM = 1;

### Evidence

- **SRC-0465** `research/proto/chesscom/game_storage/v2/player_title.proto` — [preserved redacted evidence](../evidence/text/67ae51f0ff7cd45fbe865383ae5daedd13b7b51596bc4e848288c0b4b442aca2.proto)
  Character offset 162.

```text
ax: proto3

package chesscom.game_storage.v2;

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

```

**Source references:** SRC-0465, SRC-1436  
**URL references:** None independently associated  
**Related findings:** FND-05923, FND-05924

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05926"></a>
## FND-05926: chesscom.game_storage.v2.PlayerTitle.PLAYER_TITLE_GM = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_GM = 2;

### Evidence

- **SRC-0465** `research/proto/chesscom/game_storage/v2/player_title.proto` — [preserved redacted evidence](../evidence/text/67ae51f0ff7cd45fbe865383ae5daedd13b7b51596bc4e848288c0b4b442aca2.proto)
  Character offset 186.

```text
scom.game_storage.v2;

enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

```

**Source references:** SRC-0465, SRC-1436  
**URL references:** None independently associated  
**Related findings:** FND-05923, FND-05924, FND-05925

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05927"></a>
## FND-05927: chesscom.game_storage.v2.PlayerTitle.PLAYER_TITLE_WIM = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_WIM = 3;

### Evidence

- **SRC-0465** `research/proto/chesscom/game_storage/v2/player_title.proto` — [preserved redacted evidence](../evidence/text/67ae51f0ff7cd45fbe865383ae5daedd13b7b51596bc4e848288c0b4b442aca2.proto)
  Character offset 209.

```text
enum PlayerTitle {
  PLAYER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

```

**Source references:** SRC-0465, SRC-1436  
**URL references:** None independently associated  
**Related findings:** FND-05923, FND-05924, FND-05925

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05928"></a>
## FND-05928: chesscom.game_storage.v2.PlayerTitle.PLAYER_TITLE_IM = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_IM = 4;

### Evidence

- **SRC-0465** `research/proto/chesscom/game_storage/v2/player_title.proto` — [preserved redacted evidence](../evidence/text/67ae51f0ff7cd45fbe865383ae5daedd13b7b51596bc4e848288c0b4b442aca2.proto)
  Character offset 233.

```text
YER_TITLE_UNSPECIFIED = 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

```

**Source references:** SRC-0465, SRC-1436  
**URL references:** None independently associated  
**Related findings:** FND-05923, FND-05924, FND-05925

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05929"></a>
## FND-05929: chesscom.game_storage.v2.PlayerTitle.PLAYER_TITLE_WFM = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_WFM = 5;

### Evidence

- **SRC-0465** `research/proto/chesscom/game_storage/v2/player_title.proto` — [preserved redacted evidence](../evidence/text/67ae51f0ff7cd45fbe865383ae5daedd13b7b51596bc4e848288c0b4b442aca2.proto)
  Character offset 256.

```text
 0;
  PLAYER_TITLE_WGM = 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

```

**Source references:** SRC-0465, SRC-1436  
**URL references:** None independently associated  
**Related findings:** FND-05923, FND-05924, FND-05925

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05930"></a>
## FND-05930: chesscom.game_storage.v2.PlayerTitle.PLAYER_TITLE_FM = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_FM = 6;

### Evidence

- **SRC-0465** `research/proto/chesscom/game_storage/v2/player_title.proto` — [preserved redacted evidence](../evidence/text/67ae51f0ff7cd45fbe865383ae5daedd13b7b51596bc4e848288c0b4b442aca2.proto)
  Character offset 280.

```text
 1;
  PLAYER_TITLE_GM = 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

```

**Source references:** SRC-0465, SRC-1436  
**URL references:** None independently associated  
**Related findings:** FND-05923, FND-05924, FND-05925

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05931"></a>
## FND-05931: chesscom.game_storage.v2.PlayerTitle.PLAYER_TITLE_WNM = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_WNM = 7;

### Evidence

- **SRC-0465** `research/proto/chesscom/game_storage/v2/player_title.proto` — [preserved redacted evidence](../evidence/text/67ae51f0ff7cd45fbe865383ae5daedd13b7b51596bc4e848288c0b4b442aca2.proto)
  Character offset 303.

```text
 2;
  PLAYER_TITLE_WIM = 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

```

**Source references:** SRC-0465, SRC-1436  
**URL references:** None independently associated  
**Related findings:** FND-05923, FND-05924, FND-05925

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05932"></a>
## FND-05932: chesscom.game_storage.v2.PlayerTitle.PLAYER_TITLE_NM = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_NM = 8;

### Evidence

- **SRC-0465** `research/proto/chesscom/game_storage/v2/player_title.proto` — [preserved redacted evidence](../evidence/text/67ae51f0ff7cd45fbe865383ae5daedd13b7b51596bc4e848288c0b4b442aca2.proto)
  Character offset 327.

```text
 3;
  PLAYER_TITLE_IM = 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

```

**Source references:** SRC-0465, SRC-1436  
**URL references:** None independently associated  
**Related findings:** FND-05923, FND-05924, FND-05925

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05933"></a>
## FND-05933: chesscom.game_storage.v2.PlayerTitle.PLAYER_TITLE_M = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_M = 9;

### Evidence

- **SRC-0465** `research/proto/chesscom/game_storage/v2/player_title.proto` — [preserved redacted evidence](../evidence/text/67ae51f0ff7cd45fbe865383ae5daedd13b7b51596bc4e848288c0b4b442aca2.proto)
  Character offset 350.

```text
 4;
  PLAYER_TITLE_WFM = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

```

**Source references:** SRC-0465, SRC-1436  
**URL references:** None independently associated  
**Related findings:** FND-05923, FND-05924, FND-05925

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05934"></a>
## FND-05934: chesscom.game_storage.v2.PlayerTitle.PLAYER_TITLE_CM = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_CM = 10;

### Evidence

- **SRC-0465** `research/proto/chesscom/game_storage/v2/player_title.proto` — [preserved redacted evidence](../evidence/text/67ae51f0ff7cd45fbe865383ae5daedd13b7b51596bc4e848288c0b4b442aca2.proto)
  Character offset 372.

```text
 = 5;
  PLAYER_TITLE_FM = 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

```

**Source references:** SRC-0465, SRC-1436  
**URL references:** None independently associated  
**Related findings:** FND-05923, FND-05924, FND-05925

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05935"></a>
## FND-05935: chesscom.game_storage.v2.PlayerTitle.PLAYER_TITLE_WCM = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TITLE_WCM = 11;

### Evidence

- **SRC-0465** `research/proto/chesscom/game_storage/v2/player_title.proto` — [preserved redacted evidence](../evidence/text/67ae51f0ff7cd45fbe865383ae5daedd13b7b51596bc4e848288c0b4b442aca2.proto)
  Character offset 396.

```text
= 6;
  PLAYER_TITLE_WNM = 7;
  PLAYER_TITLE_NM = 8;
  PLAYER_TITLE_M = 9;
  PLAYER_TITLE_CM = 10;
  PLAYER_TITLE_WCM = 11;
}

```

**Source references:** SRC-0465, SRC-1436  
**URL references:** None independently associated  
**Related findings:** FND-05923, FND-05924, FND-05925

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05936"></a>
## FND-05936: enum declaration: chesscom.game_storage.v2.PlayerType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayerType {

### Evidence

- **SRC-0466** `research/proto/chesscom/game_storage/v2/player_type.proto` — [preserved redacted evidence](../evidence/text/82c99084b8b880fb8770dad932e4da43ce87e80e8983228fe521c21c12a665ac.proto)
  Character offset 108.

```text
e: chesscom/game_storage/v2/player_type.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

```

**Source references:** SRC-0466, SRC-1437  
**URL references:** None independently associated  
**Related findings:** FND-05937, FND-05938

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05937"></a>
## FND-05937: chesscom.game_storage.v2.PlayerType.PLAYER_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0466** `research/proto/chesscom/game_storage/v2/player_type.proto` — [preserved redacted evidence](../evidence/text/82c99084b8b880fb8770dad932e4da43ce87e80e8983228fe521c21c12a665ac.proto)
  Character offset 128.

```text
rage/v2/player_type.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

```

**Source references:** SRC-0466, SRC-1437  
**URL references:** None independently associated  
**Related findings:** FND-05936, FND-05938

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05938"></a>
## FND-05938: chesscom.game_storage.v2.PlayerType.PLAYER_TYPE_HUMAN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TYPE_HUMAN = 1;

### Evidence

- **SRC-0466** `research/proto/chesscom/game_storage/v2/player_type.proto` — [preserved redacted evidence](../evidence/text/82c99084b8b880fb8770dad932e4da43ce87e80e8983228fe521c21c12a665ac.proto)
  Character offset 159.

```text
ntax: proto3

package chesscom.game_storage.v2;

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

```

**Source references:** SRC-0466, SRC-1437  
**URL references:** None independently associated  
**Related findings:** FND-05936, FND-05937

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05939"></a>
## FND-05939: chesscom.game_storage.v2.PlayerType.PLAYER_TYPE_COMPUTER = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TYPE_COMPUTER = 2;

### Evidence

- **SRC-0466** `research/proto/chesscom/game_storage/v2/player_type.proto` — [preserved redacted evidence](../evidence/text/82c99084b8b880fb8770dad932e4da43ce87e80e8983228fe521c21c12a665ac.proto)
  Character offset 184.

```text
sscom.game_storage.v2;

enum PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

```

**Source references:** SRC-0466, SRC-1437  
**URL references:** None independently associated  
**Related findings:** FND-05936, FND-05937, FND-05938

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05940"></a>
## FND-05940: chesscom.game_storage.v2.PlayerType.PLAYER_TYPE_CYBORG = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_TYPE_CYBORG = 3;

### Evidence

- **SRC-0466** `research/proto/chesscom/game_storage/v2/player_type.proto` — [preserved redacted evidence](../evidence/text/82c99084b8b880fb8770dad932e4da43ce87e80e8983228fe521c21c12a665ac.proto)
  Character offset 212.

```text
 PlayerType {
  PLAYER_TYPE_UNSPECIFIED = 0;
  PLAYER_TYPE_HUMAN = 1;
  PLAYER_TYPE_COMPUTER = 2;
  PLAYER_TYPE_CYBORG = 3;
}

```

**Source references:** SRC-0466, SRC-1437  
**URL references:** None independently associated  
**Related findings:** FND-05936, FND-05937, FND-05938

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05941"></a>
## FND-05941: enum declaration: chesscom.game_storage.v2.RatingClass

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum RatingClass {

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 109.

```text
: chesscom/game_storage/v2/rating_class.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960
```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05942"></a>
## FND-05942: chesscom.game_storage.v2.RatingClass.RATING_CLASS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_UNSPECIFIED = 0;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 130.

```text
ge/v2/rating_class.proto
// syntax: proto3

package chesscom.game_storage.v2;

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_
```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05943"></a>
## FND-05943: chesscom.game_storage.v2.RatingClass.RATING_CLASS_UNRATED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_UNRATED = 1;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 162.

```text
ax: proto3

package chesscom.game_storage.v2;

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  
```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05944"></a>
## FND-05944: chesscom.game_storage.v2.RatingClass.RATING_CLASS_CHESS_COM_CHESS_BULLET = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 190.

```text
.game_storage.v2;

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGO
```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05945"></a>
## FND-05945: chesscom.game_storage.v2.RatingClass.RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 233.

```text
ING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THRE
```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05946"></a>
## FND-05946: chesscom.game_storage.v2.RatingClass.RATING_CLASS_CHESS_COM_CHESS_RAPID = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 275.

```text
UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZ
```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05947"></a>
## FND-05947: chesscom.game_storage.v2.RatingClass.RATING_CLASS_CHESS_COM_CHESS_DAILY = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 317.

```text
S_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STA
```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05948"></a>
## FND-05948: chesscom.game_storage.v2.RatingClass.RATING_CLASS_CHESS_COM_CHESS960 = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS960 = 6;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 359.

```text
SS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPI
```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05949"></a>
## FND-05949: chesscom.game_storage.v2.RatingClass.RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 398.

```text
CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ
```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05950"></a>
## FND-05950: chesscom.game_storage.v2.RatingClass.RATING_CLASS_CHESS_COM_BUGHOUSE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_BUGHOUSE = 8;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 443.

```text
SS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CH
```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05951"></a>
## FND-05951: chesscom.game_storage.v2.RatingClass.RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 482.

```text
CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05952"></a>
## FND-05952: chesscom.game_storage.v2.RatingClass.RATING_CLASS_CHESS_COM_THREECHECK = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_THREECHECK = 10;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 526.

```text
960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05953"></a>
## FND-05953: chesscom.game_storage.v2.RatingClass.RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 568.

```text
GHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05954"></a>
## FND-05954: chesscom.game_storage.v2.RatingClass.RATING_CLASS_FIDE_CHESS_STANDARD = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_FIDE_CHESS_STANDARD = 12;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 610.

```text
FTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05955"></a>
## FND-05955: chesscom.game_storage.v2.RatingClass.RATING_CLASS_FIDE_CHESS_RAPID = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_FIDE_CHESS_RAPID = 13;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 651.

```text
REECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05956"></a>
## FND-05956: chesscom.game_storage.v2.RatingClass.RATING_CLASS_FIDE_CHESS_BLITZ = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_FIDE_CHESS_BLITZ = 14;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 689.

```text
M_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05957"></a>
## FND-05957: chesscom.game_storage.v2.RatingClass.RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;

### Evidence

- **SRC-0467** `research/proto/chesscom/game_storage/v2/rating_class.proto` — [preserved redacted evidence](../evidence/text/a544855b62dc688542d379bdc07132e6c2101bbdf8a8bf6ba06d8e2c758ea6eb.proto)
  Character offset 727.

```text
_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

```

**Source references:** SRC-0467, SRC-1438  
**URL references:** None independently associated  
**Related findings:** FND-05941, FND-05942, FND-05943

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05958"></a>
## FND-05958: message declaration: chesscom.game_storage.v2.SpecialGameEvent

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SpecialGameEvent {

### Evidence

- **SRC-0468** `research/proto/chesscom/game_storage/v2/special_game_event.proto` — [preserved redacted evidence](../evidence/text/b1cdd4a47b0856289d47a54dd44240fd0d56e7f967251f06dd9b59f6e4bb8ddb.proto)
  Character offset 115.

```text
scom/game_storage/v2/special_game_event.proto
// syntax: proto3

package chesscom.game_storage.v2;

message SpecialGameEvent {
  optional bool is_featured = 1;
  optional bool is_pcl = 2;
}

```

**Source references:** SRC-0468, SRC-1439  
**URL references:** None independently associated  
**Related findings:** FND-05959, FND-05960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05959"></a>
## FND-05959: chesscom.game_storage.v2.SpecialGameEvent.is_featured = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_featured = 1;

### Evidence

- **SRC-0468** `research/proto/chesscom/game_storage/v2/special_game_event.proto` — [preserved redacted evidence](../evidence/text/b1cdd4a47b0856289d47a54dd44240fd0d56e7f967251f06dd9b59f6e4bb8ddb.proto)
  Character offset 144.

```text
game_event.proto
// syntax: proto3

package chesscom.game_storage.v2;

message SpecialGameEvent {
  optional bool is_featured = 1;
  optional bool is_pcl = 2;
}

```

**Source references:** SRC-0468, SRC-1439  
**URL references:** None independently associated  
**Related findings:** FND-05958, FND-05960

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05960"></a>
## FND-05960: chesscom.game_storage.v2.SpecialGameEvent.is_pcl = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_pcl = 2;

### Evidence

- **SRC-0468** `research/proto/chesscom/game_storage/v2/special_game_event.proto` — [preserved redacted evidence](../evidence/text/b1cdd4a47b0856289d47a54dd44240fd0d56e7f967251f06dd9b59f6e4bb8ddb.proto)
  Character offset 177.

```text
3

package chesscom.game_storage.v2;

message SpecialGameEvent {
  optional bool is_featured = 1;
  optional bool is_pcl = 2;
}

```

**Source references:** SRC-0468, SRC-1439  
**URL references:** None independently associated  
**Related findings:** FND-05958, FND-05959

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05961"></a>
## FND-05961: message declaration: chesscom.game_storage.v2.TournamentData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TournamentData {

### Evidence

- **SRC-0469** `research/proto/chesscom/game_storage/v2/tournament_data.proto` — [preserved redacted evidence](../evidence/text/d4309b87fa4d1e784aed7d7a2d3147fe6536900d5e17814d53b827d9f1fdf1a2.proto)
  Character offset 112.

```text
hesscom/game_storage/v2/tournament_data.proto
// syntax: proto3

package chesscom.game_storage.v2;

message TournamentData {
  optional .chesscom.tdtools.v1.ChessComTournamentIdentifier chess_com_tournament_identifier = 1;
  optional uint32 round = 2;
}

```

**Source references:** SRC-0469, SRC-1440  
**URL references:** None independently associated  
**Related findings:** FND-05962, FND-05963

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05962"></a>
## FND-05962: chesscom.game_storage.v2.TournamentData.chess_com_tournament_identifier = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.tdtools.v1.ChessComTournamentIdentifier chess_com_tournament_identifier = 1;

### Evidence

- **SRC-0469** `research/proto/chesscom/game_storage/v2/tournament_data.proto` — [preserved redacted evidence](../evidence/text/d4309b87fa4d1e784aed7d7a2d3147fe6536900d5e17814d53b827d9f1fdf1a2.proto)
  Character offset 139.

```text
rnament_data.proto
// syntax: proto3

package chesscom.game_storage.v2;

message TournamentData {
  optional .chesscom.tdtools.v1.ChessComTournamentIdentifier chess_com_tournament_identifier = 1;
  optional uint32 round = 2;
}

```

**Source references:** SRC-0469, SRC-1440  
**URL references:** None independently associated  
**Related findings:** FND-05961, FND-05963

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05963"></a>
## FND-05963: chesscom.game_storage.v2.TournamentData.round = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 round = 2;

### Evidence

- **SRC-0469** `research/proto/chesscom/game_storage/v2/tournament_data.proto` — [preserved redacted evidence](../evidence/text/d4309b87fa4d1e784aed7d7a2d3147fe6536900d5e17814d53b827d9f1fdf1a2.proto)
  Character offset 237.

```text
  optional .chesscom.tdtools.v1.ChessComTournamentIdentifier chess_com_tournament_identifier = 1;
  optional uint32 round = 2;
}

```

**Source references:** SRC-0469, SRC-1440  
**URL references:** None independently associated  
**Related findings:** FND-05961, FND-05962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05964"></a>
## FND-05964: message declaration: chesscom.game_storage.v2.VsCoachGameData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message VsCoachGameData {

### Evidence

- **SRC-0470** `research/proto/chesscom/game_storage/v2/vs_coach_game_data.proto` — [preserved redacted evidence](../evidence/text/9302c3f5a949c3116aadd074efd08446d1b1836b3e0fe3da41928288f7760cf9.proto)
  Character offset 115.

```text
scom/game_storage/v2/vs_coach_game_data.proto
// syntax: proto3

package chesscom.game_storage.v2;

message VsCoachGameData {
  optional string coach_id = 1;
}

```

**Source references:** SRC-0470, SRC-1441  
**URL references:** None independently associated  
**Related findings:** FND-05965

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05965"></a>
## FND-05965: chesscom.game_storage.v2.VsCoachGameData.coach_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coach_id = 1;

### Evidence

- **SRC-0470** `research/proto/chesscom/game_storage/v2/vs_coach_game_data.proto` — [preserved redacted evidence](../evidence/text/9302c3f5a949c3116aadd074efd08446d1b1836b3e0fe3da41928288f7760cf9.proto)
  Character offset 143.

```text
h_game_data.proto
// syntax: proto3

package chesscom.game_storage.v2;

message VsCoachGameData {
  optional string coach_id = 1;
}

```

**Source references:** SRC-0470, SRC-1441  
**URL references:** None independently associated  
**Related findings:** FND-05964

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05966"></a>
## FND-05966: message declaration: chesscom.game_storage.v2.VsComputerGameData

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message VsComputerGameData {

### Evidence

- **SRC-0471** `research/proto/chesscom/game_storage/v2/vs_computer_game_data.proto` — [preserved redacted evidence](../evidence/text/37801a1fcf13e43bbb9228eec5dfc270789819d1a1dec851ce209fcd7cb22b3f.proto)
  Character offset 118.

```text
m/game_storage/v2/vs_computer_game_data.proto
// syntax: proto3

package chesscom.game_storage.v2;

message VsComputerGameData {
  oneof _crowns_earned {
  uint32 crowns_earned = 2;
  }
  oneof _event_config_key {
  string event_config_key = 5;
  }
  repeated .chesscom.computer.v2.AssistedGameFeature assisted_game_features = 1;
  optional string bot_personality_id = 3;
  optional .chesscom.computer.v2.GameMode game_m
```

**Source references:** SRC-0471, SRC-1442  
**URL references:** None independently associated  
**Related findings:** FND-05967, FND-05968

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05967"></a>
## FND-05967: oneof declaration: chesscom.game_storage.v2.VsComputerGameData._crowns_earned

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _crowns_earned {

### Evidence

- **SRC-0471** `research/proto/chesscom/game_storage/v2/vs_computer_game_data.proto` — [preserved redacted evidence](../evidence/text/37801a1fcf13e43bbb9228eec5dfc270789819d1a1dec851ce209fcd7cb22b3f.proto)
  Character offset 149.

```text
ame_data.proto
// syntax: proto3

package chesscom.game_storage.v2;

message VsComputerGameData {
  oneof _crowns_earned {
  uint32 crowns_earned = 2;
  }
  oneof _event_config_key {
  string event_config_key = 5;
  }
  repeated .chesscom.computer.v2.AssistedGameFeature assisted_game_features = 1;
  optional string bot_personality_id = 3;
  optional .chesscom.computer.v2.GameMode game_mode = 4;
}

```

**Source references:** SRC-0471, SRC-1442  
**URL references:** None independently associated  
**Related findings:** FND-05966, FND-05968

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05968"></a>
## FND-05968: chesscom.game_storage.v2.VsComputerGameData.crowns_earned = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 crowns_earned = 2;

### Evidence

- **SRC-0471** `research/proto/chesscom/game_storage/v2/vs_computer_game_data.proto` — [preserved redacted evidence](../evidence/text/37801a1fcf13e43bbb9228eec5dfc270789819d1a1dec851ce209fcd7cb22b3f.proto)
  Character offset 174.

```text
 proto3

package chesscom.game_storage.v2;

message VsComputerGameData {
  oneof _crowns_earned {
  uint32 crowns_earned = 2;
  }
  oneof _event_config_key {
  string event_config_key = 5;
  }
  repeated .chesscom.computer.v2.AssistedGameFeature assisted_game_features = 1;
  optional string bot_personality_id = 3;
  optional .chesscom.computer.v2.GameMode game_mode = 4;
}

```

**Source references:** SRC-0471, SRC-1442  
**URL references:** None independently associated  
**Related findings:** FND-05966, FND-05967

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05969"></a>
## FND-05969: oneof declaration: chesscom.game_storage.v2.VsComputerGameData._event_config_key

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _event_config_key {

### Evidence

- **SRC-0471** `research/proto/chesscom/game_storage/v2/vs_computer_game_data.proto` — [preserved redacted evidence](../evidence/text/37801a1fcf13e43bbb9228eec5dfc270789819d1a1dec851ce209fcd7cb22b3f.proto)
  Character offset 206.

```text
torage.v2;

message VsComputerGameData {
  oneof _crowns_earned {
  uint32 crowns_earned = 2;
  }
  oneof _event_config_key {
  string event_config_key = 5;
  }
  repeated .chesscom.computer.v2.AssistedGameFeature assisted_game_features = 1;
  optional string bot_personality_id = 3;
  optional .chesscom.computer.v2.GameMode game_mode = 4;
}

```

**Source references:** SRC-0471, SRC-1442  
**URL references:** None independently associated  
**Related findings:** FND-05966, FND-05967, FND-05968

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05970"></a>
## FND-05970: chesscom.game_storage.v2.VsComputerGameData.event_config_key = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string event_config_key = 5;

### Evidence

- **SRC-0471** `research/proto/chesscom/game_storage/v2/vs_computer_game_data.proto` — [preserved redacted evidence](../evidence/text/37801a1fcf13e43bbb9228eec5dfc270789819d1a1dec851ce209fcd7cb22b3f.proto)
  Character offset 234.

```text
erGameData {
  oneof _crowns_earned {
  uint32 crowns_earned = 2;
  }
  oneof _event_config_key {
  string event_config_key = 5;
  }
  repeated .chesscom.computer.v2.AssistedGameFeature assisted_game_features = 1;
  optional string bot_personality_id = 3;
  optional .chesscom.computer.v2.GameMode game_mode = 4;
}

```

**Source references:** SRC-0471, SRC-1442  
**URL references:** None independently associated  
**Related findings:** FND-05966, FND-05967, FND-05968

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05971"></a>
## FND-05971: chesscom.game_storage.v2.VsComputerGameData.assisted_game_features = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.computer.v2.AssistedGameFeature assisted_game_features = 1;

### Evidence

- **SRC-0471** `research/proto/chesscom/game_storage/v2/vs_computer_game_data.proto` — [preserved redacted evidence](../evidence/text/37801a1fcf13e43bbb9228eec5dfc270789819d1a1dec851ce209fcd7cb22b3f.proto)
  Character offset 269.

```text
 {
  uint32 crowns_earned = 2;
  }
  oneof _event_config_key {
  string event_config_key = 5;
  }
  repeated .chesscom.computer.v2.AssistedGameFeature assisted_game_features = 1;
  optional string bot_personality_id = 3;
  optional .chesscom.computer.v2.GameMode game_mode = 4;
}

```

**Source references:** SRC-0471, SRC-1442  
**URL references:** None independently associated  
**Related findings:** FND-05966, FND-05967, FND-05968

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05972"></a>
## FND-05972: chesscom.game_storage.v2.VsComputerGameData.bot_personality_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string bot_personality_id = 3;

### Evidence

- **SRC-0471** `research/proto/chesscom/game_storage/v2/vs_computer_game_data.proto` — [preserved redacted evidence](../evidence/text/37801a1fcf13e43bbb9228eec5dfc270789819d1a1dec851ce209fcd7cb22b3f.proto)
  Character offset 350.

```text
fig_key = 5;
  }
  repeated .chesscom.computer.v2.AssistedGameFeature assisted_game_features = 1;
  optional string bot_personality_id = 3;
  optional .chesscom.computer.v2.GameMode game_mode = 4;
}

```

**Source references:** SRC-0471, SRC-1442  
**URL references:** None independently associated  
**Related findings:** FND-05966, FND-05967, FND-05968

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05973"></a>
## FND-05973: chesscom.game_storage.v2.VsComputerGameData.game_mode = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.computer.v2.GameMode game_mode = 4;

### Evidence

- **SRC-0471** `research/proto/chesscom/game_storage/v2/vs_computer_game_data.proto` — [preserved redacted evidence](../evidence/text/37801a1fcf13e43bbb9228eec5dfc270789819d1a1dec851ce209fcd7cb22b3f.proto)
  Character offset 392.

```text
uter.v2.AssistedGameFeature assisted_game_features = 1;
  optional string bot_personality_id = 3;
  optional .chesscom.computer.v2.GameMode game_mode = 4;
}

```

**Source references:** SRC-0471, SRC-1442  
**URL references:** None independently associated  
**Related findings:** FND-05966, FND-05967, FND-05968

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05974"></a>
## FND-05974: message declaration: chesscom.gameplay.v1.BattleRef

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BattleRef {

### Evidence

- **SRC-0472** `research/proto/chesscom/gameplay/v1/battle_ref.proto` — [preserved redacted evidence](../evidence/text/1095c2fbd6687265385775191e6542174762eba14488e75713fc5624935fa201.proto)
  Character offset 99.

```text
// source: chesscom/gameplay/v1/battle_ref.proto
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
**Related findings:** FND-05975, FND-05976

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
