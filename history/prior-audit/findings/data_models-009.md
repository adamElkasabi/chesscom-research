# data_models — findings 801–900

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-01075"></a>
## FND-01075: chesscom.chess.v1.PlayerMetadata.ratings = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Rating ratings = 2;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2418.

```text
.ChesscomPlayerMetadata chesscom_metadata = 3;
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

<a id="FND-01076"></a>
## FND-01076: message declaration: chesscom.chess.v1.Rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Rating {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2469.

```text
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

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01077"></a>
## FND-01077: oneof declaration: chesscom.chess.v1.Rating._rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2488.

```text
m.chess.v1.Color color = 1;
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

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01078"></a>
## FND-01078: chesscom.chess.v1.Rating.rating = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating = 1;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2506.

```text
olor = 1;
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

<a id="FND-01079"></a>
## FND-01079: message declaration: chesscom.chess.v1.ChesscomPlayerMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ChesscomPlayerMetadata {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2531.

```text
sscom.chess.v1.Rating ratings = 2;
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

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01080"></a>
## FND-01080: oneof declaration: chesscom.chess.v1.ChesscomPlayerMetadata._user_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_id {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2566.

```text
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

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01081"></a>
## FND-01081: chesscom.chess.v1.ChesscomPlayerMetadata.user_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_id = 1;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2585.

```text

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

<a id="FND-01082"></a>
## FND-01082: oneof declaration: chesscom.chess.v1.ChesscomPlayerMetadata._legacy_user_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _legacy_user_id {

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2611.

```text
 rating = 1;
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

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01083"></a>
## FND-01083: chesscom.chess.v1.ChesscomPlayerMetadata.legacy_user_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 legacy_user_id = 2;

### Evidence

- **SRC-0246** `research/proto/chesscom/chess/v1/game.proto` — [preserved redacted evidence](../evidence/text/cdcf7e4eaa09f01507e5baa4ee8a0a8eec77760cbd4dd6e77f2f155449569424.proto)
  Character offset 2637.

```text
e ChesscomPlayerMetadata {
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

<a id="FND-01084"></a>
## FND-01084: enum declaration: chesscom.chess.v1.GamePhase

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GamePhase {

### Evidence

- **SRC-0247** `research/proto/chesscom/chess/v1/game_phase.proto` — [preserved redacted evidence](../evidence/text/64dd5c13daa288783a5e0d4baa7cb6015ffe9b8ef3abfc53318035e6415d7d1e.proto)
  Character offset 93.

```text
// source: chesscom/chess/v1/game_phase.proto
// syntax: proto3

package chesscom.chess.v1;

enum GamePhase {
  GAME_PHASE_UNSPECIFIED = 0;
  GAME_PHASE_OPENING = 1;
  GAME_PHASE_MIDDLEGAME = 2;
  GAME_PHASE_ENDGAME = 3;
}

```

**Source references:** SRC-0247, SRC-1218  
**URL references:** None independently associated  
**Related findings:** FND-01085, FND-01086

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01085"></a>
## FND-01085: chesscom.chess.v1.GamePhase.GAME_PHASE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PHASE_UNSPECIFIED = 0;

### Evidence

- **SRC-0247** `research/proto/chesscom/chess/v1/game_phase.proto` — [preserved redacted evidence](../evidence/text/64dd5c13daa288783a5e0d4baa7cb6015ffe9b8ef3abfc53318035e6415d7d1e.proto)
  Character offset 112.

```text
hesscom/chess/v1/game_phase.proto
// syntax: proto3

package chesscom.chess.v1;

enum GamePhase {
  GAME_PHASE_UNSPECIFIED = 0;
  GAME_PHASE_OPENING = 1;
  GAME_PHASE_MIDDLEGAME = 2;
  GAME_PHASE_ENDGAME = 3;
}

```

**Source references:** SRC-0247, SRC-1218  
**URL references:** None independently associated  
**Related findings:** FND-01084, FND-01086

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01086"></a>
## FND-01086: chesscom.chess.v1.GamePhase.GAME_PHASE_OPENING = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PHASE_OPENING = 1;

### Evidence

- **SRC-0247** `research/proto/chesscom/chess/v1/game_phase.proto` — [preserved redacted evidence](../evidence/text/64dd5c13daa288783a5e0d4baa7cb6015ffe9b8ef3abfc53318035e6415d7d1e.proto)
  Character offset 142.

```text
oto
// syntax: proto3

package chesscom.chess.v1;

enum GamePhase {
  GAME_PHASE_UNSPECIFIED = 0;
  GAME_PHASE_OPENING = 1;
  GAME_PHASE_MIDDLEGAME = 2;
  GAME_PHASE_ENDGAME = 3;
}

```

**Source references:** SRC-0247, SRC-1218  
**URL references:** None independently associated  
**Related findings:** FND-01084, FND-01085

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01087"></a>
## FND-01087: chesscom.chess.v1.GamePhase.GAME_PHASE_MIDDLEGAME = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PHASE_MIDDLEGAME = 2;

### Evidence

- **SRC-0247** `research/proto/chesscom/chess/v1/game_phase.proto` — [preserved redacted evidence](../evidence/text/64dd5c13daa288783a5e0d4baa7cb6015ffe9b8ef3abfc53318035e6415d7d1e.proto)
  Character offset 168.

```text
kage chesscom.chess.v1;

enum GamePhase {
  GAME_PHASE_UNSPECIFIED = 0;
  GAME_PHASE_OPENING = 1;
  GAME_PHASE_MIDDLEGAME = 2;
  GAME_PHASE_ENDGAME = 3;
}

```

**Source references:** SRC-0247, SRC-1218  
**URL references:** None independently associated  
**Related findings:** FND-01084, FND-01085, FND-01086

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01088"></a>
## FND-01088: chesscom.chess.v1.GamePhase.GAME_PHASE_ENDGAME = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PHASE_ENDGAME = 3;

### Evidence

- **SRC-0247** `research/proto/chesscom/chess/v1/game_phase.proto` — [preserved redacted evidence](../evidence/text/64dd5c13daa288783a5e0d4baa7cb6015ffe9b8ef3abfc53318035e6415d7d1e.proto)
  Character offset 197.

```text
 GamePhase {
  GAME_PHASE_UNSPECIFIED = 0;
  GAME_PHASE_OPENING = 1;
  GAME_PHASE_MIDDLEGAME = 2;
  GAME_PHASE_ENDGAME = 3;
}

```

**Source references:** SRC-0247, SRC-1218  
**URL references:** None independently associated  
**Related findings:** FND-01084, FND-01085, FND-01086

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01089"></a>
## FND-01089: enum declaration: chesscom.chess.v1.PromotionPieceType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PromotionPieceType {

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 87.

```text
// source: chesscom/chess/v1/move.proto
// syntax: proto3

package chesscom.chess.v1;

enum PromotionPieceType {
  PROMOTION_PIECE_TYPE_UNSPECIFIED = 0;
  PROMOTION_PIECE_TYPE_KNIGHT = 1;
  PROMOTION_PIECE_TYPE_BISHOP = 2;
  PROMOTION_PIECE_TYPE_ROOK = 3;
  PROMOTION_PIECE_TYPE_QUEEN = 4;
}

message CastlingDetails {
  optional .chesscom.chess.v1.Square king_from = 1;
  optional .chesscom.chess.v1.Square
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01090, FND-01091

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01090"></a>
## FND-01090: chesscom.chess.v1.PromotionPieceType.PROMOTION_PIECE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROMOTION_PIECE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 115.

```text
scom/chess/v1/move.proto
// syntax: proto3

package chesscom.chess.v1;

enum PromotionPieceType {
  PROMOTION_PIECE_TYPE_UNSPECIFIED = 0;
  PROMOTION_PIECE_TYPE_KNIGHT = 1;
  PROMOTION_PIECE_TYPE_BISHOP = 2;
  PROMOTION_PIECE_TYPE_ROOK = 3;
  PROMOTION_PIECE_TYPE_QUEEN = 4;
}

message CastlingDetails {
  optional .chesscom.chess.v1.Square king_from = 1;
  optional .chesscom.chess.v1.Square king_to = 2;
  optional .ch
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01091

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01091"></a>
## FND-01091: chesscom.chess.v1.PromotionPieceType.PROMOTION_PIECE_TYPE_KNIGHT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROMOTION_PIECE_TYPE_KNIGHT = 1;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 155.

```text
o3

package chesscom.chess.v1;

enum PromotionPieceType {
  PROMOTION_PIECE_TYPE_UNSPECIFIED = 0;
  PROMOTION_PIECE_TYPE_KNIGHT = 1;
  PROMOTION_PIECE_TYPE_BISHOP = 2;
  PROMOTION_PIECE_TYPE_ROOK = 3;
  PROMOTION_PIECE_TYPE_QUEEN = 4;
}

message CastlingDetails {
  optional .chesscom.chess.v1.Square king_from = 1;
  optional .chesscom.chess.v1.Square king_to = 2;
  optional .chesscom.chess.v1.Square rook_from = 3;
  
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01092"></a>
## FND-01092: chesscom.chess.v1.PromotionPieceType.PROMOTION_PIECE_TYPE_BISHOP = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROMOTION_PIECE_TYPE_BISHOP = 2;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 190.

```text
m PromotionPieceType {
  PROMOTION_PIECE_TYPE_UNSPECIFIED = 0;
  PROMOTION_PIECE_TYPE_KNIGHT = 1;
  PROMOTION_PIECE_TYPE_BISHOP = 2;
  PROMOTION_PIECE_TYPE_ROOK = 3;
  PROMOTION_PIECE_TYPE_QUEEN = 4;
}

message CastlingDetails {
  optional .chesscom.chess.v1.Square king_from = 1;
  optional .chesscom.chess.v1.Square king_to = 2;
  optional .chesscom.chess.v1.Square rook_from = 3;
  optional .chesscom.chess.v1.Square 
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01093"></a>
## FND-01093: chesscom.chess.v1.PromotionPieceType.PROMOTION_PIECE_TYPE_ROOK = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROMOTION_PIECE_TYPE_ROOK = 3;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 225.

```text
PIECE_TYPE_UNSPECIFIED = 0;
  PROMOTION_PIECE_TYPE_KNIGHT = 1;
  PROMOTION_PIECE_TYPE_BISHOP = 2;
  PROMOTION_PIECE_TYPE_ROOK = 3;
  PROMOTION_PIECE_TYPE_QUEEN = 4;
}

message CastlingDetails {
  optional .chesscom.chess.v1.Square king_from = 1;
  optional .chesscom.chess.v1.Square king_to = 2;
  optional .chesscom.chess.v1.Square rook_from = 3;
  optional .chesscom.chess.v1.Square rook_to = 4;
}

message Move {
  on
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01094"></a>
## FND-01094: chesscom.chess.v1.PromotionPieceType.PROMOTION_PIECE_TYPE_QUEEN = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PROMOTION_PIECE_TYPE_QUEEN = 4;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 258.

```text
MOTION_PIECE_TYPE_KNIGHT = 1;
  PROMOTION_PIECE_TYPE_BISHOP = 2;
  PROMOTION_PIECE_TYPE_ROOK = 3;
  PROMOTION_PIECE_TYPE_QUEEN = 4;
}

message CastlingDetails {
  optional .chesscom.chess.v1.Square king_from = 1;
  optional .chesscom.chess.v1.Square king_to = 2;
  optional .chesscom.chess.v1.Square rook_from = 3;
  optional .chesscom.chess.v1.Square rook_to = 4;
}

message Move {
  oneof _promotion_piece_type {
  .ch
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01095"></a>
## FND-01095: message declaration: chesscom.chess.v1.CastlingDetails

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CastlingDetails {

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 293.

```text
MOTION_PIECE_TYPE_BISHOP = 2;
  PROMOTION_PIECE_TYPE_ROOK = 3;
  PROMOTION_PIECE_TYPE_QUEEN = 4;
}

message CastlingDetails {
  optional .chesscom.chess.v1.Square king_from = 1;
  optional .chesscom.chess.v1.Square king_to = 2;
  optional .chesscom.chess.v1.Square rook_from = 3;
  optional .chesscom.chess.v1.Square rook_to = 4;
}

message Move {
  oneof _promotion_piece_type {
  .chesscom.chess.v1.PromotionPieceType 
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01096"></a>
## FND-01096: chesscom.chess.v1.CastlingDetails.king_from = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square king_from = 1;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 321.

```text
;
  PROMOTION_PIECE_TYPE_ROOK = 3;
  PROMOTION_PIECE_TYPE_QUEEN = 4;
}

message CastlingDetails {
  optional .chesscom.chess.v1.Square king_from = 1;
  optional .chesscom.chess.v1.Square king_to = 2;
  optional .chesscom.chess.v1.Square rook_from = 3;
  optional .chesscom.chess.v1.Square rook_to = 4;
}

message Move {
  oneof _promotion_piece_type {
  .chesscom.chess.v1.PromotionPieceType promotion_piece_type = 3;
  
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01097"></a>
## FND-01097: chesscom.chess.v1.CastlingDetails.king_to = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square king_to = 2;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 373.

```text
_TYPE_QUEEN = 4;
}

message CastlingDetails {
  optional .chesscom.chess.v1.Square king_from = 1;
  optional .chesscom.chess.v1.Square king_to = 2;
  optional .chesscom.chess.v1.Square rook_from = 3;
  optional .chesscom.chess.v1.Square rook_to = 4;
}

message Move {
  oneof _promotion_piece_type {
  .chesscom.chess.v1.PromotionPieceType promotion_piece_type = 3;
  }
  oneof _time_taken_ms {
  uint32 time_taken_ms = 
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01098"></a>
## FND-01098: chesscom.chess.v1.CastlingDetails.rook_from = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square rook_from = 3;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 423.

```text
tional .chesscom.chess.v1.Square king_from = 1;
  optional .chesscom.chess.v1.Square king_to = 2;
  optional .chesscom.chess.v1.Square rook_from = 3;
  optional .chesscom.chess.v1.Square rook_to = 4;
}

message Move {
  oneof _promotion_piece_type {
  .chesscom.chess.v1.PromotionPieceType promotion_piece_type = 3;
  }
  oneof _time_taken_ms {
  uint32 time_taken_ms = 4;
  }
  oneof _castling_details {
  .chesscom.che
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01099"></a>
## FND-01099: chesscom.chess.v1.CastlingDetails.rook_to = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square rook_to = 4;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 475.

```text
tional .chesscom.chess.v1.Square king_to = 2;
  optional .chesscom.chess.v1.Square rook_from = 3;
  optional .chesscom.chess.v1.Square rook_to = 4;
}

message Move {
  oneof _promotion_piece_type {
  .chesscom.chess.v1.PromotionPieceType promotion_piece_type = 3;
  }
  oneof _time_taken_ms {
  uint32 time_taken_ms = 4;
  }
  oneof _castling_details {
  .chesscom.chess.v1.CastlingDetails castling_details = 5;
  }
  on
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01100"></a>
## FND-01100: message declaration: chesscom.chess.v1.Move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Move {

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 526.

```text
ional .chesscom.chess.v1.Square rook_from = 3;
  optional .chesscom.chess.v1.Square rook_to = 4;
}

message Move {
  oneof _promotion_piece_type {
  .chesscom.chess.v1.PromotionPieceType promotion_piece_type = 3;
  }
  oneof _time_taken_ms {
  uint32 time_taken_ms = 4;
  }
  oneof _castling_details {
  .chesscom.chess.v1.CastlingDetails castling_details = 5;
  }
  oneof _remaining_clock_ms {
  uint32 remaining_clock_
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01101"></a>
## FND-01101: oneof declaration: chesscom.chess.v1.Move._promotion_piece_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _promotion_piece_type {

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 543.

```text
hess.v1.Square rook_from = 3;
  optional .chesscom.chess.v1.Square rook_to = 4;
}

message Move {
  oneof _promotion_piece_type {
  .chesscom.chess.v1.PromotionPieceType promotion_piece_type = 3;
  }
  oneof _time_taken_ms {
  uint32 time_taken_ms = 4;
  }
  oneof _castling_details {
  .chesscom.chess.v1.CastlingDetails castling_details = 5;
  }
  oneof _remaining_clock_ms {
  uint32 remaining_clock_ms = 6;
  }
  one
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01102"></a>
## FND-01102: chesscom.chess.v1.Move.promotion_piece_type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.PromotionPieceType promotion_piece_type = 3;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 575.

```text
optional .chesscom.chess.v1.Square rook_to = 4;
}

message Move {
  oneof _promotion_piece_type {
  .chesscom.chess.v1.PromotionPieceType promotion_piece_type = 3;
  }
  oneof _time_taken_ms {
  uint32 time_taken_ms = 4;
  }
  oneof _castling_details {
  .chesscom.chess.v1.CastlingDetails castling_details = 5;
  }
  oneof _remaining_clock_ms {
  uint32 remaining_clock_ms = 6;
  }
  oneof _drop_piece_type {
  .chessco
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01103"></a>
## FND-01103: oneof declaration: chesscom.chess.v1.Move._time_taken_ms

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_taken_ms {

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 645.

```text
eof _promotion_piece_type {
  .chesscom.chess.v1.PromotionPieceType promotion_piece_type = 3;
  }
  oneof _time_taken_ms {
  uint32 time_taken_ms = 4;
  }
  oneof _castling_details {
  .chesscom.chess.v1.CastlingDetails castling_details = 5;
  }
  oneof _remaining_clock_ms {
  uint32 remaining_clock_ms = 6;
  }
  oneof _drop_piece_type {
  .chesscom.chess.v1.PieceType drop_piece_type = 7;
  }
  oneof _time_taken_dura
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01104"></a>
## FND-01104: chesscom.chess.v1.Move.time_taken_ms = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 time_taken_ms = 4;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 670.

```text
 {
  .chesscom.chess.v1.PromotionPieceType promotion_piece_type = 3;
  }
  oneof _time_taken_ms {
  uint32 time_taken_ms = 4;
  }
  oneof _castling_details {
  .chesscom.chess.v1.CastlingDetails castling_details = 5;
  }
  oneof _remaining_clock_ms {
  uint32 remaining_clock_ms = 6;
  }
  oneof _drop_piece_type {
  .chesscom.chess.v1.PieceType drop_piece_type = 7;
  }
  oneof _time_taken_duration {
  .google.protobuf
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01105"></a>
## FND-01105: oneof declaration: chesscom.chess.v1.Move._castling_details

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _castling_details {

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 702.

```text
nPieceType promotion_piece_type = 3;
  }
  oneof _time_taken_ms {
  uint32 time_taken_ms = 4;
  }
  oneof _castling_details {
  .chesscom.chess.v1.CastlingDetails castling_details = 5;
  }
  oneof _remaining_clock_ms {
  uint32 remaining_clock_ms = 6;
  }
  oneof _drop_piece_type {
  .chesscom.chess.v1.PieceType drop_piece_type = 7;
  }
  oneof _time_taken_duration {
  .google.protobuf.Duration time_taken_duration = 
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01106"></a>
## FND-01106: chesscom.chess.v1.Move.castling_details = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.CastlingDetails castling_details = 5;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 730.

```text
ype = 3;
  }
  oneof _time_taken_ms {
  uint32 time_taken_ms = 4;
  }
  oneof _castling_details {
  .chesscom.chess.v1.CastlingDetails castling_details = 5;
  }
  oneof _remaining_clock_ms {
  uint32 remaining_clock_ms = 6;
  }
  oneof _drop_piece_type {
  .chesscom.chess.v1.PieceType drop_piece_type = 7;
  }
  oneof _time_taken_duration {
  .google.protobuf.Duration time_taken_duration = 8;
  }
  optional .chesscom.
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01107"></a>
## FND-01107: oneof declaration: chesscom.chess.v1.Move._remaining_clock_ms

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _remaining_clock_ms {

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 793.

```text
4;
  }
  oneof _castling_details {
  .chesscom.chess.v1.CastlingDetails castling_details = 5;
  }
  oneof _remaining_clock_ms {
  uint32 remaining_clock_ms = 6;
  }
  oneof _drop_piece_type {
  .chesscom.chess.v1.PieceType drop_piece_type = 7;
  }
  oneof _time_taken_duration {
  .google.protobuf.Duration time_taken_duration = 8;
  }
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square 
```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01108"></a>
## FND-01108: chesscom.chess.v1.Move.remaining_clock_ms = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 remaining_clock_ms = 6;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 823.

```text
ls {
  .chesscom.chess.v1.CastlingDetails castling_details = 5;
  }
  oneof _remaining_clock_ms {
  uint32 remaining_clock_ms = 6;
  }
  oneof _drop_piece_type {
  .chesscom.chess.v1.PieceType drop_piece_type = 7;
  }
  oneof _time_taken_duration {
  .google.protobuf.Duration time_taken_duration = 8;
  }
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
}

```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01109"></a>
## FND-01109: oneof declaration: chesscom.chess.v1.Move._drop_piece_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _drop_piece_type {

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 860.

```text
ails castling_details = 5;
  }
  oneof _remaining_clock_ms {
  uint32 remaining_clock_ms = 6;
  }
  oneof _drop_piece_type {
  .chesscom.chess.v1.PieceType drop_piece_type = 7;
  }
  oneof _time_taken_duration {
  .google.protobuf.Duration time_taken_duration = 8;
  }
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
}

```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01110"></a>
## FND-01110: chesscom.chess.v1.Move.drop_piece_type = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.PieceType drop_piece_type = 7;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 887.

```text
  }
  oneof _remaining_clock_ms {
  uint32 remaining_clock_ms = 6;
  }
  oneof _drop_piece_type {
  .chesscom.chess.v1.PieceType drop_piece_type = 7;
  }
  oneof _time_taken_duration {
  .google.protobuf.Duration time_taken_duration = 8;
  }
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
}

```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01111"></a>
## FND-01111: oneof declaration: chesscom.chess.v1.Move._time_taken_duration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_taken_duration {

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 943.

```text
ck_ms = 6;
  }
  oneof _drop_piece_type {
  .chesscom.chess.v1.PieceType drop_piece_type = 7;
  }
  oneof _time_taken_duration {
  .google.protobuf.Duration time_taken_duration = 8;
  }
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
}

```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01112"></a>
## FND-01112: chesscom.chess.v1.Move.time_taken_duration = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Duration time_taken_duration = 8;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 974.

```text
ece_type {
  .chesscom.chess.v1.PieceType drop_piece_type = 7;
  }
  oneof _time_taken_duration {
  .google.protobuf.Duration time_taken_duration = 8;
  }
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
}

```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01113"></a>
## FND-01113: chesscom.chess.v1.Move.from = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square from = 1;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 1031.

```text
 = 7;
  }
  oneof _time_taken_duration {
  .google.protobuf.Duration time_taken_duration = 8;
  }
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
}

```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01114"></a>
## FND-01114: chesscom.chess.v1.Move.to = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square to = 2;

### Evidence

- **SRC-0248** `research/proto/chesscom/chess/v1/move.proto` — [preserved redacted evidence](../evidence/text/2f6e5361f8e49dcfbf02831df79b0a3246b429da1e5f60b1679547a8c72f3097.proto)
  Character offset 1078.

```text
gle.protobuf.Duration time_taken_duration = 8;
  }
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
}

```

**Source references:** SRC-0248, SRC-1219  
**URL references:** None independently associated  
**Related findings:** FND-01089, FND-01090, FND-01091

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01115"></a>
## FND-01115: enum declaration: chesscom.chess.v1.MoveNotation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MoveNotation {

### Evidence

- **SRC-0249** `research/proto/chesscom/chess/v1/notation.proto` — [preserved redacted evidence](../evidence/text/aad69ed445aa8a84ad7edab96969044758768f5e7d40d7ab175e7344368ff18a.proto)
  Character offset 91.

```text
// source: chesscom/chess/v1/notation.proto
// syntax: proto3

package chesscom.chess.v1;

enum MoveNotation {
  MOVE_NOTATION_UNSPECIFIED = 0;
  MOVE_NOTATION_TCN = 1;
  MOVE_NOTATION_SAN = 2;
  MOVE_NOTATION_UCI_LAN = 3;
}

```

**Source references:** SRC-0249, SRC-1220  
**URL references:** None independently associated  
**Related findings:** FND-01116, FND-01117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01116"></a>
## FND-01116: chesscom.chess.v1.MoveNotation.MOVE_NOTATION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_NOTATION_UNSPECIFIED = 0;

### Evidence

- **SRC-0249** `research/proto/chesscom/chess/v1/notation.proto` — [preserved redacted evidence](../evidence/text/aad69ed445aa8a84ad7edab96969044758768f5e7d40d7ab175e7344368ff18a.proto)
  Character offset 113.

```text
esscom/chess/v1/notation.proto
// syntax: proto3

package chesscom.chess.v1;

enum MoveNotation {
  MOVE_NOTATION_UNSPECIFIED = 0;
  MOVE_NOTATION_TCN = 1;
  MOVE_NOTATION_SAN = 2;
  MOVE_NOTATION_UCI_LAN = 3;
}

```

**Source references:** SRC-0249, SRC-1220  
**URL references:** None independently associated  
**Related findings:** FND-01115, FND-01117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01117"></a>
## FND-01117: chesscom.chess.v1.MoveNotation.MOVE_NOTATION_TCN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_NOTATION_TCN = 1;

### Evidence

- **SRC-0249** `research/proto/chesscom/chess/v1/notation.proto` — [preserved redacted evidence](../evidence/text/aad69ed445aa8a84ad7edab96969044758768f5e7d40d7ab175e7344368ff18a.proto)
  Character offset 146.

```text
 syntax: proto3

package chesscom.chess.v1;

enum MoveNotation {
  MOVE_NOTATION_UNSPECIFIED = 0;
  MOVE_NOTATION_TCN = 1;
  MOVE_NOTATION_SAN = 2;
  MOVE_NOTATION_UCI_LAN = 3;
}

```

**Source references:** SRC-0249, SRC-1220  
**URL references:** None independently associated  
**Related findings:** FND-01115, FND-01116

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01118"></a>
## FND-01118: chesscom.chess.v1.MoveNotation.MOVE_NOTATION_SAN = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_NOTATION_SAN = 2;

### Evidence

- **SRC-0249** `research/proto/chesscom/chess/v1/notation.proto` — [preserved redacted evidence](../evidence/text/aad69ed445aa8a84ad7edab96969044758768f5e7d40d7ab175e7344368ff18a.proto)
  Character offset 171.

```text
chesscom.chess.v1;

enum MoveNotation {
  MOVE_NOTATION_UNSPECIFIED = 0;
  MOVE_NOTATION_TCN = 1;
  MOVE_NOTATION_SAN = 2;
  MOVE_NOTATION_UCI_LAN = 3;
}

```

**Source references:** SRC-0249, SRC-1220  
**URL references:** None independently associated  
**Related findings:** FND-01115, FND-01116, FND-01117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01119"></a>
## FND-01119: chesscom.chess.v1.MoveNotation.MOVE_NOTATION_UCI_LAN = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_NOTATION_UCI_LAN = 3;

### Evidence

- **SRC-0249** `research/proto/chesscom/chess/v1/notation.proto` — [preserved redacted evidence](../evidence/text/aad69ed445aa8a84ad7edab96969044758768f5e7d40d7ab175e7344368ff18a.proto)
  Character offset 196.

```text
MoveNotation {
  MOVE_NOTATION_UNSPECIFIED = 0;
  MOVE_NOTATION_TCN = 1;
  MOVE_NOTATION_SAN = 2;
  MOVE_NOTATION_UCI_LAN = 3;
}

```

**Source references:** SRC-0249, SRC-1220  
**URL references:** None independently associated  
**Related findings:** FND-01115, FND-01116, FND-01117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01120"></a>
## FND-01120: enum declaration: chesscom.chess.v1.PieceType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PieceType {

### Evidence

- **SRC-0250** `research/proto/chesscom/chess/v1/piece.proto` — [preserved redacted evidence](../evidence/text/02f803bb0704af5b014e65daa91f867bef528e1ac97ef7486d25fb10f0ed9d6e.proto)
  Character offset 88.

```text
// source: chesscom/chess/v1/piece.proto
// syntax: proto3

package chesscom.chess.v1;

enum PieceType {
  PIECE_TYPE_UNSPECIFIED = 0;
  PIECE_TYPE_PAWN = 1;
  PIECE_TYPE_KNIGHT = 2;
  PIECE_TYPE_BISHOP = 3;
  PIECE_TYPE_ROOK = 4;
  PIECE_TYPE_QUEEN = 5;
  PIECE_TYPE_KING = 6;
}

message Piece {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.PieceType type = 2;
}

```

**Source references:** SRC-0250, SRC-1221  
**URL references:** None independently associated  
**Related findings:** FND-01121, FND-01122

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01121"></a>
## FND-01121: chesscom.chess.v1.PieceType.PIECE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PIECE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0250** `research/proto/chesscom/chess/v1/piece.proto` — [preserved redacted evidence](../evidence/text/02f803bb0704af5b014e65daa91f867bef528e1ac97ef7486d25fb10f0ed9d6e.proto)
  Character offset 107.

```text
ce: chesscom/chess/v1/piece.proto
// syntax: proto3

package chesscom.chess.v1;

enum PieceType {
  PIECE_TYPE_UNSPECIFIED = 0;
  PIECE_TYPE_PAWN = 1;
  PIECE_TYPE_KNIGHT = 2;
  PIECE_TYPE_BISHOP = 3;
  PIECE_TYPE_ROOK = 4;
  PIECE_TYPE_QUEEN = 5;
  PIECE_TYPE_KING = 6;
}

message Piece {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.PieceType type = 2;
}

```

**Source references:** SRC-0250, SRC-1221  
**URL references:** None independently associated  
**Related findings:** FND-01120, FND-01122

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01122"></a>
## FND-01122: chesscom.chess.v1.PieceType.PIECE_TYPE_PAWN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PIECE_TYPE_PAWN = 1;

### Evidence

- **SRC-0250** `research/proto/chesscom/chess/v1/piece.proto` — [preserved redacted evidence](../evidence/text/02f803bb0704af5b014e65daa91f867bef528e1ac97ef7486d25fb10f0ed9d6e.proto)
  Character offset 137.

```text
oto
// syntax: proto3

package chesscom.chess.v1;

enum PieceType {
  PIECE_TYPE_UNSPECIFIED = 0;
  PIECE_TYPE_PAWN = 1;
  PIECE_TYPE_KNIGHT = 2;
  PIECE_TYPE_BISHOP = 3;
  PIECE_TYPE_ROOK = 4;
  PIECE_TYPE_QUEEN = 5;
  PIECE_TYPE_KING = 6;
}

message Piece {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.PieceType type = 2;
}

```

**Source references:** SRC-0250, SRC-1221  
**URL references:** None independently associated  
**Related findings:** FND-01120, FND-01121

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01123"></a>
## FND-01123: chesscom.chess.v1.PieceType.PIECE_TYPE_KNIGHT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PIECE_TYPE_KNIGHT = 2;

### Evidence

- **SRC-0250** `research/proto/chesscom/chess/v1/piece.proto` — [preserved redacted evidence](../evidence/text/02f803bb0704af5b014e65daa91f867bef528e1ac97ef7486d25fb10f0ed9d6e.proto)
  Character offset 160.

```text
package chesscom.chess.v1;

enum PieceType {
  PIECE_TYPE_UNSPECIFIED = 0;
  PIECE_TYPE_PAWN = 1;
  PIECE_TYPE_KNIGHT = 2;
  PIECE_TYPE_BISHOP = 3;
  PIECE_TYPE_ROOK = 4;
  PIECE_TYPE_QUEEN = 5;
  PIECE_TYPE_KING = 6;
}

message Piece {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.PieceType type = 2;
}

```

**Source references:** SRC-0250, SRC-1221  
**URL references:** None independently associated  
**Related findings:** FND-01120, FND-01121, FND-01122

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01124"></a>
## FND-01124: chesscom.chess.v1.PieceType.PIECE_TYPE_BISHOP = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PIECE_TYPE_BISHOP = 3;

### Evidence

- **SRC-0250** `research/proto/chesscom/chess/v1/piece.proto` — [preserved redacted evidence](../evidence/text/02f803bb0704af5b014e65daa91f867bef528e1ac97ef7486d25fb10f0ed9d6e.proto)
  Character offset 185.

```text
;

enum PieceType {
  PIECE_TYPE_UNSPECIFIED = 0;
  PIECE_TYPE_PAWN = 1;
  PIECE_TYPE_KNIGHT = 2;
  PIECE_TYPE_BISHOP = 3;
  PIECE_TYPE_ROOK = 4;
  PIECE_TYPE_QUEEN = 5;
  PIECE_TYPE_KING = 6;
}

message Piece {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.PieceType type = 2;
}

```

**Source references:** SRC-0250, SRC-1221  
**URL references:** None independently associated  
**Related findings:** FND-01120, FND-01121, FND-01122

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01125"></a>
## FND-01125: chesscom.chess.v1.PieceType.PIECE_TYPE_ROOK = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PIECE_TYPE_ROOK = 4;

### Evidence

- **SRC-0250** `research/proto/chesscom/chess/v1/piece.proto` — [preserved redacted evidence](../evidence/text/02f803bb0704af5b014e65daa91f867bef528e1ac97ef7486d25fb10f0ed9d6e.proto)
  Character offset 210.

```text
CE_TYPE_UNSPECIFIED = 0;
  PIECE_TYPE_PAWN = 1;
  PIECE_TYPE_KNIGHT = 2;
  PIECE_TYPE_BISHOP = 3;
  PIECE_TYPE_ROOK = 4;
  PIECE_TYPE_QUEEN = 5;
  PIECE_TYPE_KING = 6;
}

message Piece {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.PieceType type = 2;
}

```

**Source references:** SRC-0250, SRC-1221  
**URL references:** None independently associated  
**Related findings:** FND-01120, FND-01121, FND-01122

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01126"></a>
## FND-01126: chesscom.chess.v1.PieceType.PIECE_TYPE_QUEEN = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PIECE_TYPE_QUEEN = 5;

### Evidence

- **SRC-0250** `research/proto/chesscom/chess/v1/piece.proto` — [preserved redacted evidence](../evidence/text/02f803bb0704af5b014e65daa91f867bef528e1ac97ef7486d25fb10f0ed9d6e.proto)
  Character offset 233.

```text
;
  PIECE_TYPE_PAWN = 1;
  PIECE_TYPE_KNIGHT = 2;
  PIECE_TYPE_BISHOP = 3;
  PIECE_TYPE_ROOK = 4;
  PIECE_TYPE_QUEEN = 5;
  PIECE_TYPE_KING = 6;
}

message Piece {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.PieceType type = 2;
}

```

**Source references:** SRC-0250, SRC-1221  
**URL references:** None independently associated  
**Related findings:** FND-01120, FND-01121, FND-01122

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01127"></a>
## FND-01127: chesscom.chess.v1.PieceType.PIECE_TYPE_KING = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PIECE_TYPE_KING = 6;

### Evidence

- **SRC-0250** `research/proto/chesscom/chess/v1/piece.proto` — [preserved redacted evidence](../evidence/text/02f803bb0704af5b014e65daa91f867bef528e1ac97ef7486d25fb10f0ed9d6e.proto)
  Character offset 257.

```text

  PIECE_TYPE_KNIGHT = 2;
  PIECE_TYPE_BISHOP = 3;
  PIECE_TYPE_ROOK = 4;
  PIECE_TYPE_QUEEN = 5;
  PIECE_TYPE_KING = 6;
}

message Piece {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.PieceType type = 2;
}

```

**Source references:** SRC-0250, SRC-1221  
**URL references:** None independently associated  
**Related findings:** FND-01120, FND-01121, FND-01122

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01128"></a>
## FND-01128: message declaration: chesscom.chess.v1.Piece

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Piece {

### Evidence

- **SRC-0250** `research/proto/chesscom/chess/v1/piece.proto` — [preserved redacted evidence](../evidence/text/02f803bb0704af5b014e65daa91f867bef528e1ac97ef7486d25fb10f0ed9d6e.proto)
  Character offset 281.

```text
;
  PIECE_TYPE_BISHOP = 3;
  PIECE_TYPE_ROOK = 4;
  PIECE_TYPE_QUEEN = 5;
  PIECE_TYPE_KING = 6;
}

message Piece {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.PieceType type = 2;
}

```

**Source references:** SRC-0250, SRC-1221  
**URL references:** None independently associated  
**Related findings:** FND-01120, FND-01121, FND-01122

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01129"></a>
## FND-01129: chesscom.chess.v1.Piece.color = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Color color = 1;

### Evidence

- **SRC-0250** `research/proto/chesscom/chess/v1/piece.proto` — [preserved redacted evidence](../evidence/text/02f803bb0704af5b014e65daa91f867bef528e1ac97ef7486d25fb10f0ed9d6e.proto)
  Character offset 299.

```text
HOP = 3;
  PIECE_TYPE_ROOK = 4;
  PIECE_TYPE_QUEEN = 5;
  PIECE_TYPE_KING = 6;
}

message Piece {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.PieceType type = 2;
}

```

**Source references:** SRC-0250, SRC-1221  
**URL references:** None independently associated  
**Related findings:** FND-01120, FND-01121, FND-01122

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01130"></a>
## FND-01130: chesscom.chess.v1.Piece.type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.PieceType type = 2;

### Evidence

- **SRC-0250** `research/proto/chesscom/chess/v1/piece.proto` — [preserved redacted evidence](../evidence/text/02f803bb0704af5b014e65daa91f867bef528e1ac97ef7486d25fb10f0ed9d6e.proto)
  Character offset 346.

```text
EEN = 5;
  PIECE_TYPE_KING = 6;
}

message Piece {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.PieceType type = 2;
}

```

**Source references:** SRC-0250, SRC-1221  
**URL references:** None independently associated  
**Related findings:** FND-01120, FND-01121, FND-01122

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01131"></a>
## FND-01131: message declaration: chesscom.chess.v1.Position

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Position {

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 91.

```text
// source: chesscom/chess/v1/position.proto
// syntax: proto3

package chesscom.chess.v1;

message Position {
  oneof _en_passant_square {
  .chesscom.chess.v1.Square en_passant_square = 4;
  }
  oneof _in_check {
  bool in_check = 7;
  }
  repeated .chesscom.chess.v1.Placement pieces = 1;
  optional .chesscom.chess.v1.Color active_color = 2;
  repeated .chesscom.chess.v1.CastlingRight castling_rights = 3;
 
```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01132, FND-01133

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01132"></a>
## FND-01132: oneof declaration: chesscom.chess.v1.Position._en_passant_square

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _en_passant_square {

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 112.

```text
hesscom/chess/v1/position.proto
// syntax: proto3

package chesscom.chess.v1;

message Position {
  oneof _en_passant_square {
  .chesscom.chess.v1.Square en_passant_square = 4;
  }
  oneof _in_check {
  bool in_check = 7;
  }
  repeated .chesscom.chess.v1.Placement pieces = 1;
  optional .chesscom.chess.v1.Color active_color = 2;
  repeated .chesscom.chess.v1.CastlingRight castling_rights = 3;
  optional uint32 half
```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01133

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01133"></a>
## FND-01133: chesscom.chess.v1.Position.en_passant_square = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Square en_passant_square = 4;

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 141.

```text
to
// syntax: proto3

package chesscom.chess.v1;

message Position {
  oneof _en_passant_square {
  .chesscom.chess.v1.Square en_passant_square = 4;
  }
  oneof _in_check {
  bool in_check = 7;
  }
  repeated .chesscom.chess.v1.Placement pieces = 1;
  optional .chesscom.chess.v1.Color active_color = 2;
  repeated .chesscom.chess.v1.CastlingRight castling_rights = 3;
  optional uint32 halfmove_clock = 5;
  optional ui
```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01134"></a>
## FND-01134: oneof declaration: chesscom.chess.v1.Position._in_check

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _in_check {

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 196.

```text
ge Position {
  oneof _en_passant_square {
  .chesscom.chess.v1.Square en_passant_square = 4;
  }
  oneof _in_check {
  bool in_check = 7;
  }
  repeated .chesscom.chess.v1.Placement pieces = 1;
  optional .chesscom.chess.v1.Color active_color = 2;
  repeated .chesscom.chess.v1.CastlingRight castling_rights = 3;
  optional uint32 halfmove_clock = 5;
  optional uint32 fullmove_number = 6;
}

message Placement {
  opti
```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132, FND-01133

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01135"></a>
## FND-01135: chesscom.chess.v1.Position.in_check = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool in_check = 7;

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 216.

```text
f _en_passant_square {
  .chesscom.chess.v1.Square en_passant_square = 4;
  }
  oneof _in_check {
  bool in_check = 7;
  }
  repeated .chesscom.chess.v1.Placement pieces = 1;
  optional .chesscom.chess.v1.Color active_color = 2;
  repeated .chesscom.chess.v1.CastlingRight castling_rights = 3;
  optional uint32 halfmove_clock = 5;
  optional uint32 fullmove_number = 6;
}

message Placement {
  optional .chesscom.chess
```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132, FND-01133

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01136"></a>
## FND-01136: chesscom.chess.v1.Position.pieces = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Placement pieces = 1;

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 241.

```text
.chesscom.chess.v1.Square en_passant_square = 4;
  }
  oneof _in_check {
  bool in_check = 7;
  }
  repeated .chesscom.chess.v1.Placement pieces = 1;
  optional .chesscom.chess.v1.Color active_color = 2;
  repeated .chesscom.chess.v1.CastlingRight castling_rights = 3;
  optional uint32 halfmove_clock = 5;
  optional uint32 fullmove_number = 6;
}

message Placement {
  optional .chesscom.chess.v1.Piece piece = 1;
  op
```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132, FND-01133

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01137"></a>
## FND-01137: chesscom.chess.v1.Position.active_color = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Color active_color = 2;

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 293.

```text

  oneof _in_check {
  bool in_check = 7;
  }
  repeated .chesscom.chess.v1.Placement pieces = 1;
  optional .chesscom.chess.v1.Color active_color = 2;
  repeated .chesscom.chess.v1.CastlingRight castling_rights = 3;
  optional uint32 halfmove_clock = 5;
  optional uint32 fullmove_number = 6;
}

message Placement {
  optional .chesscom.chess.v1.Piece piece = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

mess
```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132, FND-01133

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01138"></a>
## FND-01138: chesscom.chess.v1.Position.castling_rights = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.CastlingRight castling_rights = 3;

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 347.

```text
ed .chesscom.chess.v1.Placement pieces = 1;
  optional .chesscom.chess.v1.Color active_color = 2;
  repeated .chesscom.chess.v1.CastlingRight castling_rights = 3;
  optional uint32 halfmove_clock = 5;
  optional uint32 fullmove_number = 6;
}

message Placement {
  optional .chesscom.chess.v1.Piece piece = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message CastlingRight {
  optional .chesscom.chess.v1.Colo
```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132, FND-01133

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01139"></a>
## FND-01139: chesscom.chess.v1.Position.halfmove_clock = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 halfmove_clock = 5;

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 412.

```text
chess.v1.Color active_color = 2;
  repeated .chesscom.chess.v1.CastlingRight castling_rights = 3;
  optional uint32 halfmove_clock = 5;
  optional uint32 fullmove_number = 6;
}

message Placement {
  optional .chesscom.chess.v1.Piece piece = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message CastlingRight {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.File rook_file = 2;
}

```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132, FND-01133

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01140"></a>
## FND-01140: chesscom.chess.v1.Position.fullmove_number = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 fullmove_number = 6;

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 450.

```text
eated .chesscom.chess.v1.CastlingRight castling_rights = 3;
  optional uint32 halfmove_clock = 5;
  optional uint32 fullmove_number = 6;
}

message Placement {
  optional .chesscom.chess.v1.Piece piece = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message CastlingRight {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.File rook_file = 2;
}

```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132, FND-01133

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01141"></a>
## FND-01141: message declaration: chesscom.chess.v1.Placement

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Placement {

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 490.

```text
astling_rights = 3;
  optional uint32 halfmove_clock = 5;
  optional uint32 fullmove_number = 6;
}

message Placement {
  optional .chesscom.chess.v1.Piece piece = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message CastlingRight {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.File rook_file = 2;
}

```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132, FND-01133

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01142"></a>
## FND-01142: chesscom.chess.v1.Placement.piece = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Piece piece = 1;

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 512.

```text
optional uint32 halfmove_clock = 5;
  optional uint32 fullmove_number = 6;
}

message Placement {
  optional .chesscom.chess.v1.Piece piece = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message CastlingRight {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.File rook_file = 2;
}

```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132, FND-01133

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01143"></a>
## FND-01143: chesscom.chess.v1.Placement.square = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square square = 2;

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 559.

```text
uint32 fullmove_number = 6;
}

message Placement {
  optional .chesscom.chess.v1.Piece piece = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message CastlingRight {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.File rook_file = 2;
}

```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132, FND-01133

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01144"></a>
## FND-01144: message declaration: chesscom.chess.v1.CastlingRight

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CastlingRight {

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 609.

```text

  optional .chesscom.chess.v1.Piece piece = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message CastlingRight {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.File rook_file = 2;
}

```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132, FND-01133

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01145"></a>
## FND-01145: chesscom.chess.v1.CastlingRight.color = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Color color = 1;

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 635.

```text
s.v1.Piece piece = 1;
  optional .chesscom.chess.v1.Square square = 2;
}

message CastlingRight {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.File rook_file = 2;
}

```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132, FND-01133

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01146"></a>
## FND-01146: chesscom.chess.v1.CastlingRight.rook_file = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.File rook_file = 2;

### Evidence

- **SRC-0251** `research/proto/chesscom/chess/v1/position.proto` — [preserved redacted evidence](../evidence/text/f46049186883c802b979cbd5422164a7743e8c9bfc3d7dcea12f9306867d73ee.proto)
  Character offset 682.

```text
s.v1.Square square = 2;
}

message CastlingRight {
  optional .chesscom.chess.v1.Color color = 1;
  optional .chesscom.chess.v1.File rook_file = 2;
}

```

**Source references:** SRC-0251, SRC-1222  
**URL references:** None independently associated  
**Related findings:** FND-01131, FND-01132, FND-01133

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01147"></a>
## FND-01147: enum declaration: chesscom.chess.v1.Result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Result {

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 89.

```text
// source: chesscom/chess/v1/result.proto
// syntax: proto3

package chesscom.chess.v1;

enum Result {
  RESULT_UNSPECIFIED = 0;
  RESULT_WHITE_WIN = 1;
  RESULT_BLACK_WIN = 2;
  RESULT_DRAW = 3;
  RESULT_ABORT = 4;
}

enum ResultType {
  RESULT_TYPE_UNSPECIFIED = 0;
  RESULT_TYPE_CHECKMATE = 1;
  RESULT_TYPE_STALEMATE = 2;
  RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TY
```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01148"></a>
## FND-01148: chesscom.chess.v1.Result.RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 105.

```text
urce: chesscom/chess/v1/result.proto
// syntax: proto3

package chesscom.chess.v1;

enum Result {
  RESULT_UNSPECIFIED = 0;
  RESULT_WHITE_WIN = 1;
  RESULT_BLACK_WIN = 2;
  RESULT_DRAW = 3;
  RESULT_ABORT = 4;
}

enum ResultType {
  RESULT_TYPE_UNSPECIFIED = 0;
  RESULT_TYPE_CHECKMATE = 1;
  RESULT_TYPE_STALEMATE = 2;
  RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 
```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01149"></a>
## FND-01149: chesscom.chess.v1.Result.RESULT_WHITE_WIN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_WHITE_WIN = 1;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 131.

```text
sult.proto
// syntax: proto3

package chesscom.chess.v1;

enum Result {
  RESULT_UNSPECIFIED = 0;
  RESULT_WHITE_WIN = 1;
  RESULT_BLACK_WIN = 2;
  RESULT_DRAW = 3;
  RESULT_ABORT = 4;
}

enum ResultType {
  RESULT_TYPE_UNSPECIFIED = 0;
  RESULT_TYPE_CHECKMATE = 1;
  RESULT_TYPE_STALEMATE = 2;
  RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT =
```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01150"></a>
## FND-01150: chesscom.chess.v1.Result.RESULT_BLACK_WIN = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_BLACK_WIN = 2;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 155.

```text
oto3

package chesscom.chess.v1;

enum Result {
  RESULT_UNSPECIFIED = 0;
  RESULT_WHITE_WIN = 1;
  RESULT_BLACK_WIN = 2;
  RESULT_DRAW = 3;
  RESULT_ABORT = 4;
}

enum ResultType {
  RESULT_TYPE_UNSPECIFIED = 0;
  RESULT_TYPE_CHECKMATE = 1;
  RESULT_TYPE_STALEMATE = 2;
  RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT = 6;
  RESULT_TYPE_TIMEOU
```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01151"></a>
## FND-01151: chesscom.chess.v1.Result.RESULT_DRAW = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_DRAW = 3;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 179.

```text
hess.v1;

enum Result {
  RESULT_UNSPECIFIED = 0;
  RESULT_WHITE_WIN = 1;
  RESULT_BLACK_WIN = 2;
  RESULT_DRAW = 3;
  RESULT_ABORT = 4;
}

enum ResultType {
  RESULT_TYPE_UNSPECIFIED = 0;
  RESULT_TYPE_CHECKMATE = 1;
  RESULT_TYPE_STALEMATE = 2;
  RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT = 6;
  RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERI
```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01152"></a>
## FND-01152: chesscom.chess.v1.Result.RESULT_ABORT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_ABORT = 4;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 198.

```text
lt {
  RESULT_UNSPECIFIED = 0;
  RESULT_WHITE_WIN = 1;
  RESULT_BLACK_WIN = 2;
  RESULT_DRAW = 3;
  RESULT_ABORT = 4;
}

enum ResultType {
  RESULT_TYPE_UNSPECIFIED = 0;
  RESULT_TYPE_CHECKMATE = 1;
  RESULT_TYPE_STALEMATE = 2;
  RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT = 6;
  RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7;
  RESULT_TY
```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01153"></a>
## FND-01153: enum declaration: chesscom.chess.v1.ResultType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ResultType {

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 219.

```text
FIED = 0;
  RESULT_WHITE_WIN = 1;
  RESULT_BLACK_WIN = 2;
  RESULT_DRAW = 3;
  RESULT_ABORT = 4;
}

enum ResultType {
  RESULT_TYPE_UNSPECIFIED = 0;
  RESULT_TYPE_CHECKMATE = 1;
  RESULT_TYPE_STALEMATE = 2;
  RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT = 6;
  RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7;
  RESULT_TYPE_ABANDONMENT = 8;
 
```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01154"></a>
## FND-01154: chesscom.chess.v1.ResultType.RESULT_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 239.

```text
HITE_WIN = 1;
  RESULT_BLACK_WIN = 2;
  RESULT_DRAW = 3;
  RESULT_ABORT = 4;
}

enum ResultType {
  RESULT_TYPE_UNSPECIFIED = 0;
  RESULT_TYPE_CHECKMATE = 1;
  RESULT_TYPE_STALEMATE = 2;
  RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT = 6;
  RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7;
  RESULT_TYPE_ABANDONMENT = 8;
  RESULT_TYPE_50_MOVE
```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01155"></a>
## FND-01155: chesscom.chess.v1.ResultType.RESULT_TYPE_CHECKMATE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_CHECKMATE = 1;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 270.

```text
N = 2;
  RESULT_DRAW = 3;
  RESULT_ABORT = 4;
}

enum ResultType {
  RESULT_TYPE_UNSPECIFIED = 0;
  RESULT_TYPE_CHECKMATE = 1;
  RESULT_TYPE_STALEMATE = 2;
  RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT = 6;
  RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7;
  RESULT_TYPE_ABANDONMENT = 8;
  RESULT_TYPE_50_MOVE_RULE = 9;
  RESULT_TYPE_THREEF
```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01156"></a>
## FND-01156: chesscom.chess.v1.ResultType.RESULT_TYPE_STALEMATE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_STALEMATE = 2;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 299.

```text
ESULT_ABORT = 4;
}

enum ResultType {
  RESULT_TYPE_UNSPECIFIED = 0;
  RESULT_TYPE_CHECKMATE = 1;
  RESULT_TYPE_STALEMATE = 2;
  RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT = 6;
  RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7;
  RESULT_TYPE_ABANDONMENT = 8;
  RESULT_TYPE_50_MOVE_RULE = 9;
  RESULT_TYPE_THREEFOLD = 10;
  RESULT_TYPE_BUGHO
```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01157"></a>
## FND-01157: chesscom.chess.v1.ResultType.RESULT_TYPE_INSUFFICIENT_MATERIAL = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 328.

```text
ltType {
  RESULT_TYPE_UNSPECIFIED = 0;
  RESULT_TYPE_CHECKMATE = 1;
  RESULT_TYPE_STALEMATE = 2;
  RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT = 6;
  RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7;
  RESULT_TYPE_ABANDONMENT = 8;
  RESULT_TYPE_50_MOVE_RULE = 9;
  RESULT_TYPE_THREEFOLD = 10;
  RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11;
  RESU
```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01158"></a>
## FND-01158: chesscom.chess.v1.ResultType.RESULT_TYPE_RESIGNATION = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_RESIGNATION = 4;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 369.

```text
 RESULT_TYPE_CHECKMATE = 1;
  RESULT_TYPE_STALEMATE = 2;
  RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT = 6;
  RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7;
  RESULT_TYPE_ABANDONMENT = 8;
  RESULT_TYPE_50_MOVE_RULE = 9;
  RESULT_TYPE_THREEFOLD = 10;
  RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11;
  RESULT_TYPE_THREE_CHECK = 12;
  RESULT_TYPE_K
```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01159"></a>
## FND-01159: chesscom.chess.v1.ResultType.RESULT_TYPE_DRAW_OFFER = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_DRAW_OFFER = 5;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 400.

```text
ESULT_TYPE_STALEMATE = 2;
  RESULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT = 6;
  RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7;
  RESULT_TYPE_ABANDONMENT = 8;
  RESULT_TYPE_50_MOVE_RULE = 9;
  RESULT_TYPE_THREEFOLD = 10;
  RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11;
  RESULT_TYPE_THREE_CHECK = 12;
  RESULT_TYPE_KING_OF_THE_HILL = 13;
  RESULT_
```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01160"></a>
## FND-01160: chesscom.chess.v1.ResultType.RESULT_TYPE_TIMEOUT = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_TIMEOUT = 6;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 430.

```text
SULT_TYPE_INSUFFICIENT_MATERIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT = 6;
  RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7;
  RESULT_TYPE_ABANDONMENT = 8;
  RESULT_TYPE_50_MOVE_RULE = 9;
  RESULT_TYPE_THREEFOLD = 10;
  RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11;
  RESULT_TYPE_THREE_CHECK = 12;
  RESULT_TYPE_KING_OF_THE_HILL = 13;
  RESULT_TYPE_DOUBLE_FORFEIT = 14;
}

```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01161"></a>
## FND-01161: chesscom.chess.v1.ResultType.RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 457.

```text
RIAL = 3;
  RESULT_TYPE_RESIGNATION = 4;
  RESULT_TYPE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT = 6;
  RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7;
  RESULT_TYPE_ABANDONMENT = 8;
  RESULT_TYPE_50_MOVE_RULE = 9;
  RESULT_TYPE_THREEFOLD = 10;
  RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11;
  RESULT_TYPE_THREE_CHECK = 12;
  RESULT_TYPE_KING_OF_THE_HILL = 13;
  RESULT_TYPE_DOUBLE_FORFEIT = 14;
}

```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01162"></a>
## FND-01162: chesscom.chess.v1.ResultType.RESULT_TYPE_ABANDONMENT = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_ABANDONMENT = 8;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 509.

```text
PE_DRAW_OFFER = 5;
  RESULT_TYPE_TIMEOUT = 6;
  RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7;
  RESULT_TYPE_ABANDONMENT = 8;
  RESULT_TYPE_50_MOVE_RULE = 9;
  RESULT_TYPE_THREEFOLD = 10;
  RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11;
  RESULT_TYPE_THREE_CHECK = 12;
  RESULT_TYPE_KING_OF_THE_HILL = 13;
  RESULT_TYPE_DOUBLE_FORFEIT = 14;
}

```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01163"></a>
## FND-01163: chesscom.chess.v1.ResultType.RESULT_TYPE_50_MOVE_RULE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_50_MOVE_RULE = 9;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 540.

```text
E_TIMEOUT = 6;
  RESULT_TYPE_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 7;
  RESULT_TYPE_ABANDONMENT = 8;
  RESULT_TYPE_50_MOVE_RULE = 9;
  RESULT_TYPE_THREEFOLD = 10;
  RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11;
  RESULT_TYPE_THREE_CHECK = 12;
  RESULT_TYPE_KING_OF_THE_HILL = 13;
  RESULT_TYPE_DOUBLE_FORFEIT = 14;
}

```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01164"></a>
## FND-01164: chesscom.chess.v1.ResultType.RESULT_TYPE_THREEFOLD = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_THREEFOLD = 10;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 572.

```text
EOUT_VS_INSUFFICIENT_MATERIAL = 7;
  RESULT_TYPE_ABANDONMENT = 8;
  RESULT_TYPE_50_MOVE_RULE = 9;
  RESULT_TYPE_THREEFOLD = 10;
  RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11;
  RESULT_TYPE_THREE_CHECK = 12;
  RESULT_TYPE_KING_OF_THE_HILL = 13;
  RESULT_TYPE_DOUBLE_FORFEIT = 14;
}

```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01165"></a>
## FND-01165: chesscom.chess.v1.ResultType.RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 602.

```text
= 7;
  RESULT_TYPE_ABANDONMENT = 8;
  RESULT_TYPE_50_MOVE_RULE = 9;
  RESULT_TYPE_THREEFOLD = 10;
  RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11;
  RESULT_TYPE_THREE_CHECK = 12;
  RESULT_TYPE_KING_OF_THE_HILL = 13;
  RESULT_TYPE_DOUBLE_FORFEIT = 14;
}

```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01166"></a>
## FND-01166: chesscom.chess.v1.ResultType.RESULT_TYPE_THREE_CHECK = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_THREE_CHECK = 12;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 644.

```text
LT_TYPE_50_MOVE_RULE = 9;
  RESULT_TYPE_THREEFOLD = 10;
  RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11;
  RESULT_TYPE_THREE_CHECK = 12;
  RESULT_TYPE_KING_OF_THE_HILL = 13;
  RESULT_TYPE_DOUBLE_FORFEIT = 14;
}

```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01167"></a>
## FND-01167: chesscom.chess.v1.ResultType.RESULT_TYPE_KING_OF_THE_HILL = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_KING_OF_THE_HILL = 13;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 676.

```text
LT_TYPE_THREEFOLD = 10;
  RESULT_TYPE_BUGHOUSE_PARTNER_LOSE = 11;
  RESULT_TYPE_THREE_CHECK = 12;
  RESULT_TYPE_KING_OF_THE_HILL = 13;
  RESULT_TYPE_DOUBLE_FORFEIT = 14;
}

```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01168"></a>
## FND-01168: chesscom.chess.v1.ResultType.RESULT_TYPE_DOUBLE_FORFEIT = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RESULT_TYPE_DOUBLE_FORFEIT = 14;

### Evidence

- **SRC-0252** `research/proto/chesscom/chess/v1/result.proto` — [preserved redacted evidence](../evidence/text/db49f78d8191e7a329e9db3576afd02eaf2e1b315ffdd9d51c0a6559e825d4f8.proto)
  Character offset 713.

```text
_BUGHOUSE_PARTNER_LOSE = 11;
  RESULT_TYPE_THREE_CHECK = 12;
  RESULT_TYPE_KING_OF_THE_HILL = 13;
  RESULT_TYPE_DOUBLE_FORFEIT = 14;
}

```

**Source references:** SRC-0252, SRC-1223  
**URL references:** None independently associated  
**Related findings:** FND-01147, FND-01148, FND-01149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01169"></a>
## FND-01169: message declaration: chesscom.chess.v1.Score

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Score {

### Evidence

- **SRC-0253** `research/proto/chesscom/chess/v1/score.proto` — [preserved redacted evidence](../evidence/text/b95817c41c774121208debc9d25f7c2f532521519cc2704f33ec79c84010efae.proto)
  Character offset 88.

```text
// source: chesscom/chess/v1/score.proto
// syntax: proto3

package chesscom.chess.v1;

message Score {
  oneof score {
  sint32 score_centipawns_white = 1;
  int32 mate_in_white = 2;
  int32 mate_in_black = 3;
  .chesscom.chess.v1.Stalemate stalemate = 4;
  }
}

message Stalemate {
}

```

**Source references:** SRC-0253, SRC-1224  
**URL references:** None independently associated  
**Related findings:** FND-01170, FND-01171

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01170"></a>
## FND-01170: oneof declaration: chesscom.chess.v1.Score.score

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof score {

### Evidence

- **SRC-0253** `research/proto/chesscom/chess/v1/score.proto` — [preserved redacted evidence](../evidence/text/b95817c41c774121208debc9d25f7c2f532521519cc2704f33ec79c84010efae.proto)
  Character offset 106.

```text
rce: chesscom/chess/v1/score.proto
// syntax: proto3

package chesscom.chess.v1;

message Score {
  oneof score {
  sint32 score_centipawns_white = 1;
  int32 mate_in_white = 2;
  int32 mate_in_black = 3;
  .chesscom.chess.v1.Stalemate stalemate = 4;
  }
}

message Stalemate {
}

```

**Source references:** SRC-0253, SRC-1224  
**URL references:** None independently associated  
**Related findings:** FND-01169, FND-01171

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01171"></a>
## FND-01171: chesscom.chess.v1.Score.score_centipawns_white = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

sint32 score_centipawns_white = 1;

### Evidence

- **SRC-0253** `research/proto/chesscom/chess/v1/score.proto` — [preserved redacted evidence](../evidence/text/b95817c41c774121208debc9d25f7c2f532521519cc2704f33ec79c84010efae.proto)
  Character offset 122.

```text
ess/v1/score.proto
// syntax: proto3

package chesscom.chess.v1;

message Score {
  oneof score {
  sint32 score_centipawns_white = 1;
  int32 mate_in_white = 2;
  int32 mate_in_black = 3;
  .chesscom.chess.v1.Stalemate stalemate = 4;
  }
}

message Stalemate {
}

```

**Source references:** SRC-0253, SRC-1224  
**URL references:** None independently associated  
**Related findings:** FND-01169, FND-01170

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01172"></a>
## FND-01172: chesscom.chess.v1.Score.mate_in_white = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 mate_in_white = 2;

### Evidence

- **SRC-0253** `research/proto/chesscom/chess/v1/score.proto` — [preserved redacted evidence](../evidence/text/b95817c41c774121208debc9d25f7c2f532521519cc2704f33ec79c84010efae.proto)
  Character offset 159.

```text

package chesscom.chess.v1;

message Score {
  oneof score {
  sint32 score_centipawns_white = 1;
  int32 mate_in_white = 2;
  int32 mate_in_black = 3;
  .chesscom.chess.v1.Stalemate stalemate = 4;
  }
}

message Stalemate {
}

```

**Source references:** SRC-0253, SRC-1224  
**URL references:** None independently associated  
**Related findings:** FND-01169, FND-01170, FND-01171

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01173"></a>
## FND-01173: chesscom.chess.v1.Score.mate_in_black = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 mate_in_black = 3;

### Evidence

- **SRC-0253** `research/proto/chesscom/chess/v1/score.proto` — [preserved redacted evidence](../evidence/text/b95817c41c774121208debc9d25f7c2f532521519cc2704f33ec79c84010efae.proto)
  Character offset 186.

```text


message Score {
  oneof score {
  sint32 score_centipawns_white = 1;
  int32 mate_in_white = 2;
  int32 mate_in_black = 3;
  .chesscom.chess.v1.Stalemate stalemate = 4;
  }
}

message Stalemate {
}

```

**Source references:** SRC-0253, SRC-1224  
**URL references:** None independently associated  
**Related findings:** FND-01169, FND-01170, FND-01171

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01174"></a>
## FND-01174: chesscom.chess.v1.Score.stalemate = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Stalemate stalemate = 4;

### Evidence

- **SRC-0253** `research/proto/chesscom/chess/v1/score.proto` — [preserved redacted evidence](../evidence/text/b95817c41c774121208debc9d25f7c2f532521519cc2704f33ec79c84010efae.proto)
  Character offset 213.

```text
core {
  sint32 score_centipawns_white = 1;
  int32 mate_in_white = 2;
  int32 mate_in_black = 3;
  .chesscom.chess.v1.Stalemate stalemate = 4;
  }
}

message Stalemate {
}

```

**Source references:** SRC-0253, SRC-1224  
**URL references:** None independently associated  
**Related findings:** FND-01169, FND-01170, FND-01171

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
