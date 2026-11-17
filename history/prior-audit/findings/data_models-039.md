# data_models — findings 3801–3900

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-04075"></a>
## FND-04075: chesscom.explanation_engine.v1.MoveClassificationVersion.MOVE_CLASSIFICATION_VERSION_V2 = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_VERSION_V2 = 1;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 699.

```text
N_TRICKY = 20;
}

enum MoveClassificationVersion {
  MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_VERSION_V2 = 1;
  MOVE_CLASSIFICATION_VERSION_V3 = 2;
}

message EvalClassification {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional .chesscom.engine.v1.Evaluation evaluation = 2;
}

```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04076"></a>
## FND-04076: chesscom.explanation_engine.v1.MoveClassificationVersion.MOVE_CLASSIFICATION_VERSION_V3 = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_VERSION_V3 = 2;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 737.

```text
ionVersion {
  MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_VERSION_V2 = 1;
  MOVE_CLASSIFICATION_VERSION_V3 = 2;
}

message EvalClassification {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional .chesscom.engine.v1.Evaluation evaluation = 2;
}

```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04077"></a>
## FND-04077: message declaration: chesscom.explanation_engine.v1.EvalClassification

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EvalClassification {

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 776.

```text
ION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_VERSION_V2 = 1;
  MOVE_CLASSIFICATION_VERSION_V3 = 2;
}

message EvalClassification {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional .chesscom.engine.v1.Evaluation evaluation = 2;
}

```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04078"></a>
## FND-04078: chesscom.explanation_engine.v1.EvalClassification.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 807.

```text
SSIFICATION_VERSION_V2 = 1;
  MOVE_CLASSIFICATION_VERSION_V3 = 2;
}

message EvalClassification {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional .chesscom.engine.v1.Evaluation evaluation = 2;
}

```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04079"></a>
## FND-04079: chesscom.explanation_engine.v1.EvalClassification.evaluation = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.engine.v1.Evaluation evaluation = 2;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 894.

```text
fication {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional .chesscom.engine.v1.Evaluation evaluation = 2;
}

```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04080"></a>
## FND-04080: message declaration: chesscom.explanation_engine.v1.PieceMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PieceMove {

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 121.

```text
xplanation_engine/v1/move_details.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message PieceMove {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.chess.v1.Piece piece = 3;
}

message NormalMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_p
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04081, FND-04082

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04081"></a>
## FND-04081: chesscom.explanation_engine.v1.PieceMove.from = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square from = 1;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 143.

```text
ove_details.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message PieceMove {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.chess.v1.Piece piece = 3;
}

message NormalMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
}

message C
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04082"></a>
## FND-04082: chesscom.explanation_engine.v1.PieceMove.to = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square to = 2;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 190.

```text
esscom.explanation_engine.v1;

message PieceMove {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.chess.v1.Piece piece = 3;
}

message NormalMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
}

message CastlingMove {
  optional .chesscom.explanation_
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04083"></a>
## FND-04083: chesscom.explanation_engine.v1.PieceMove.piece = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Piece piece = 3;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 235.

```text
ove {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.chess.v1.Piece piece = 3;
}

message NormalMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
}

message CastlingMove {
  optional .chesscom.explanation_engine.v1.PieceMove king_move = 1;
  optional
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04084"></a>
## FND-04084: message declaration: chesscom.explanation_engine.v1.NormalMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NormalMove {

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 283.

```text
= 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.chess.v1.Piece piece = 3;
}

message NormalMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
}

message CastlingMove {
  optional .chesscom.explanation_engine.v1.PieceMove king_move = 1;
  optional .chesscom.explanation_engine.v1.PieceMove rook_
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04085"></a>
## FND-04085: oneof declaration: chesscom.explanation_engine.v1.NormalMove._captured_piece

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _captured_piece {

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 306.

```text
om.chess.v1.Square to = 2;
  optional .chesscom.chess.v1.Piece piece = 3;
}

message NormalMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
}

message CastlingMove {
  optional .chesscom.explanation_engine.v1.PieceMove king_move = 1;
  optional .chesscom.explanation_engine.v1.PieceMove rook_move = 2;
}

message Pr
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04086"></a>
## FND-04086: chesscom.explanation_engine.v1.NormalMove.captured_piece = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Piece captured_piece = 2;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 332.

```text

  optional .chesscom.chess.v1.Piece piece = 3;
}

message NormalMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
}

message CastlingMove {
  optional .chesscom.explanation_engine.v1.PieceMove king_move = 1;
  optional .chesscom.explanation_engine.v1.PieceMove rook_move = 2;
}

message PromotionMove {
  oneof _cap
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04087"></a>
## FND-04087: chesscom.explanation_engine.v1.NormalMove.moved_piece = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 383.

```text
message NormalMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
}

message CastlingMove {
  optional .chesscom.explanation_engine.v1.PieceMove king_move = 1;
  optional .chesscom.explanation_engine.v1.PieceMove rook_move = 2;
}

message PromotionMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_p
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04088"></a>
## FND-04088: message declaration: chesscom.explanation_engine.v1.CastlingMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CastlingMove {

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 454.

```text
ce captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
}

message CastlingMove {
  optional .chesscom.explanation_engine.v1.PieceMove king_move = 1;
  optional .chesscom.explanation_engine.v1.PieceMove rook_move = 2;
}

message PromotionMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove move
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04089"></a>
## FND-04089: chesscom.explanation_engine.v1.CastlingMove.king_move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.PieceMove king_move = 1;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 479.

```text
}
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
}

message CastlingMove {
  optional .chesscom.explanation_engine.v1.PieceMove king_move = 1;
  optional .chesscom.explanation_engine.v1.PieceMove rook_move = 2;
}

message PromotionMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
  optional .
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04090"></a>
## FND-04090: chesscom.explanation_engine.v1.CastlingMove.rook_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.PieceMove rook_move = 2;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 547.

```text
 1;
}

message CastlingMove {
  optional .chesscom.explanation_engine.v1.PieceMove king_move = 1;
  optional .chesscom.explanation_engine.v1.PieceMove rook_move = 2;
}

message PromotionMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
  optional .chesscom.chess.v1.PromotionPieceType promoted_piece_type = 3;
}

mes
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04091"></a>
## FND-04091: message declaration: chesscom.explanation_engine.v1.PromotionMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PromotionMove {

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 616.

```text
.v1.PieceMove king_move = 1;
  optional .chesscom.explanation_engine.v1.PieceMove rook_move = 2;
}

message PromotionMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
  optional .chesscom.chess.v1.PromotionPieceType promoted_piece_type = 3;
}

message EnpassantMove {
  optional .chesscom.explanation_engine.v1.Piece
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04092"></a>
## FND-04092: oneof declaration: chesscom.explanation_engine.v1.PromotionMove._captured_piece

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _captured_piece {

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 306.

```text
om.chess.v1.Square to = 2;
  optional .chesscom.chess.v1.Piece piece = 3;
}

message NormalMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
}

message CastlingMove {
  optional .chesscom.explanation_engine.v1.PieceMove king_move = 1;
  optional .chesscom.explanation_engine.v1.PieceMove rook_move = 2;
}

message Pr
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04093"></a>
## FND-04093: chesscom.explanation_engine.v1.PromotionMove.captured_piece = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Piece captured_piece = 2;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 332.

```text

  optional .chesscom.chess.v1.Piece piece = 3;
}

message NormalMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
}

message CastlingMove {
  optional .chesscom.explanation_engine.v1.PieceMove king_move = 1;
  optional .chesscom.explanation_engine.v1.PieceMove rook_move = 2;
}

message PromotionMove {
  oneof _cap
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04094"></a>
## FND-04094: chesscom.explanation_engine.v1.PromotionMove.moved_piece = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 383.

```text
message NormalMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
}

message CastlingMove {
  optional .chesscom.explanation_engine.v1.PieceMove king_move = 1;
  optional .chesscom.explanation_engine.v1.PieceMove rook_move = 2;
}

message PromotionMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_p
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04095"></a>
## FND-04095: chesscom.explanation_engine.v1.PromotionMove.promoted_piece_type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.PromotionPieceType promoted_piece_type = 3;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 789.

```text
ece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
  optional .chesscom.chess.v1.PromotionPieceType promoted_piece_type = 3;
}

message EnpassantMove {
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
  optional .chesscom.chess.v1.Square capture_square = 2;
}

message NullMove {
}

message MoveDetails {
  oneof kind {
  .chesscom.explanation_engine.v
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04096"></a>
## FND-04096: message declaration: chesscom.explanation_engine.v1.EnpassantMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EnpassantMove {

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 864.

```text
eMove moved_piece = 1;
  optional .chesscom.chess.v1.PromotionPieceType promoted_piece_type = 3;
}

message EnpassantMove {
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
  optional .chesscom.chess.v1.Square capture_square = 2;
}

message NullMove {
}

message MoveDetails {
  oneof kind {
  .chesscom.explanation_engine.v1.NormalMove regular_move = 4;
  .chesscom.explanation_engine.v1.CastlingMo
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04097"></a>
## FND-04097: chesscom.explanation_engine.v1.EnpassantMove.moved_piece = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 383.

```text
message NormalMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_piece = 2;
  }
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
}

message CastlingMove {
  optional .chesscom.explanation_engine.v1.PieceMove king_move = 1;
  optional .chesscom.explanation_engine.v1.PieceMove rook_move = 2;
}

message PromotionMove {
  oneof _captured_piece {
  .chesscom.chess.v1.Piece captured_p
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04098"></a>
## FND-04098: chesscom.explanation_engine.v1.EnpassantMove.capture_square = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square capture_square = 2;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 960.

```text

}

message EnpassantMove {
  optional .chesscom.explanation_engine.v1.PieceMove moved_piece = 1;
  optional .chesscom.chess.v1.Square capture_square = 2;
}

message NullMove {
}

message MoveDetails {
  oneof kind {
  .chesscom.explanation_engine.v1.NormalMove regular_move = 4;
  .chesscom.explanation_engine.v1.CastlingMove castling_move = 5;
  .chesscom.explanation_engine.v1.PromotionMove promotion_move = 6;
  .che
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04099"></a>
## FND-04099: message declaration: chesscom.explanation_engine.v1.NullMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NullMove {

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1018.

```text
on_engine.v1.PieceMove moved_piece = 1;
  optional .chesscom.chess.v1.Square capture_square = 2;
}

message NullMove {
}

message MoveDetails {
  oneof kind {
  .chesscom.explanation_engine.v1.NormalMove regular_move = 4;
  .chesscom.explanation_engine.v1.CastlingMove castling_move = 5;
  .chesscom.explanation_engine.v1.PromotionMove promotion_move = 6;
  .chesscom.explanation_engine.v1.EnpassantMove en_passant_move 
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04100"></a>
## FND-04100: message declaration: chesscom.explanation_engine.v1.MoveDetails

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MoveDetails {

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1040.

```text
 moved_piece = 1;
  optional .chesscom.chess.v1.Square capture_square = 2;
}

message NullMove {
}

message MoveDetails {
  oneof kind {
  .chesscom.explanation_engine.v1.NormalMove regular_move = 4;
  .chesscom.explanation_engine.v1.CastlingMove castling_move = 5;
  .chesscom.explanation_engine.v1.PromotionMove promotion_move = 6;
  .chesscom.explanation_engine.v1.EnpassantMove en_passant_move = 7;
  .chesscom.expla
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04101"></a>
## FND-04101: oneof declaration: chesscom.explanation_engine.v1.MoveDetails.kind

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof kind {

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1064.

```text
onal .chesscom.chess.v1.Square capture_square = 2;
}

message NullMove {
}

message MoveDetails {
  oneof kind {
  .chesscom.explanation_engine.v1.NormalMove regular_move = 4;
  .chesscom.explanation_engine.v1.CastlingMove castling_move = 5;
  .chesscom.explanation_engine.v1.PromotionMove promotion_move = 6;
  .chesscom.explanation_engine.v1.EnpassantMove en_passant_move = 7;
  .chesscom.explanation_engine.v1.NullMov
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04102"></a>
## FND-04102: chesscom.explanation_engine.v1.MoveDetails.regular_move = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.NormalMove regular_move = 4;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1079.

```text
chess.v1.Square capture_square = 2;
}

message NullMove {
}

message MoveDetails {
  oneof kind {
  .chesscom.explanation_engine.v1.NormalMove regular_move = 4;
  .chesscom.explanation_engine.v1.CastlingMove castling_move = 5;
  .chesscom.explanation_engine.v1.PromotionMove promotion_move = 6;
  .chesscom.explanation_engine.v1.EnpassantMove en_passant_move = 7;
  .chesscom.explanation_engine.v1.NullMove null_move = 8
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04103"></a>
## FND-04103: chesscom.explanation_engine.v1.MoveDetails.castling_move = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.CastlingMove castling_move = 5;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1142.

```text
ssage MoveDetails {
  oneof kind {
  .chesscom.explanation_engine.v1.NormalMove regular_move = 4;
  .chesscom.explanation_engine.v1.CastlingMove castling_move = 5;
  .chesscom.explanation_engine.v1.PromotionMove promotion_move = 6;
  .chesscom.explanation_engine.v1.EnpassantMove en_passant_move = 7;
  .chesscom.explanation_engine.v1.NullMove null_move = 8;
  }
  oneof _game_result {
  .chesscom.chess.v1.GameResult ga
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04104"></a>
## FND-04104: chesscom.explanation_engine.v1.MoveDetails.promotion_move = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PromotionMove promotion_move = 6;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1208.

```text
v1.NormalMove regular_move = 4;
  .chesscom.explanation_engine.v1.CastlingMove castling_move = 5;
  .chesscom.explanation_engine.v1.PromotionMove promotion_move = 6;
  .chesscom.explanation_engine.v1.EnpassantMove en_passant_move = 7;
  .chesscom.explanation_engine.v1.NullMove null_move = 8;
  }
  oneof _game_result {
  .chesscom.chess.v1.GameResult game_result = 11;
  }
  optional string move_string = 1;
  optional 
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04105"></a>
## FND-04105: chesscom.explanation_engine.v1.MoveDetails.en_passant_move = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.EnpassantMove en_passant_move = 7;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1276.

```text
stlingMove castling_move = 5;
  .chesscom.explanation_engine.v1.PromotionMove promotion_move = 6;
  .chesscom.explanation_engine.v1.EnpassantMove en_passant_move = 7;
  .chesscom.explanation_engine.v1.NullMove null_move = 8;
  }
  oneof _game_result {
  .chesscom.chess.v1.GameResult game_result = 11;
  }
  optional string move_string = 1;
  optional .chesscom.chess.v1.Move move = 2;
  optional int32 time_taken_ms = 3
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04106"></a>
## FND-04106: chesscom.explanation_engine.v1.MoveDetails.null_move = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.NullMove null_move = 8;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1345.

```text
tionMove promotion_move = 6;
  .chesscom.explanation_engine.v1.EnpassantMove en_passant_move = 7;
  .chesscom.explanation_engine.v1.NullMove null_move = 8;
  }
  oneof _game_result {
  .chesscom.chess.v1.GameResult game_result = 11;
  }
  optional string move_string = 1;
  optional .chesscom.chess.v1.Move move = 2;
  optional int32 time_taken_ms = 3;
  optional .chesscom.chess.v1.Color moved_color = 9;
  optional int
```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04107"></a>
## FND-04107: oneof declaration: chesscom.explanation_engine.v1.MoveDetails._game_result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_result {

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1407.

```text
.EnpassantMove en_passant_move = 7;
  .chesscom.explanation_engine.v1.NullMove null_move = 8;
  }
  oneof _game_result {
  .chesscom.chess.v1.GameResult game_result = 11;
  }
  optional string move_string = 1;
  optional .chesscom.chess.v1.Move move = 2;
  optional int32 time_taken_ms = 3;
  optional .chesscom.chess.v1.Color moved_color = 9;
  optional int32 full_move_number = 10;
}

```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04108"></a>
## FND-04108: chesscom.explanation_engine.v1.MoveDetails.game_result = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.GameResult game_result = 11;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1430.

```text
nt_move = 7;
  .chesscom.explanation_engine.v1.NullMove null_move = 8;
  }
  oneof _game_result {
  .chesscom.chess.v1.GameResult game_result = 11;
  }
  optional string move_string = 1;
  optional .chesscom.chess.v1.Move move = 2;
  optional int32 time_taken_ms = 3;
  optional .chesscom.chess.v1.Color moved_color = 9;
  optional int32 full_move_number = 10;
}

```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04109"></a>
## FND-04109: chesscom.explanation_engine.v1.MoveDetails.move_string = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string move_string = 1;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1484.

```text
e null_move = 8;
  }
  oneof _game_result {
  .chesscom.chess.v1.GameResult game_result = 11;
  }
  optional string move_string = 1;
  optional .chesscom.chess.v1.Move move = 2;
  optional int32 time_taken_ms = 3;
  optional .chesscom.chess.v1.Color moved_color = 9;
  optional int32 full_move_number = 10;
}

```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04110"></a>
## FND-04110: chesscom.explanation_engine.v1.MoveDetails.move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move move = 2;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1519.

```text
result {
  .chesscom.chess.v1.GameResult game_result = 11;
  }
  optional string move_string = 1;
  optional .chesscom.chess.v1.Move move = 2;
  optional int32 time_taken_ms = 3;
  optional .chesscom.chess.v1.Color moved_color = 9;
  optional int32 full_move_number = 10;
}

```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04111"></a>
## FND-04111: chesscom.explanation_engine.v1.MoveDetails.time_taken_ms = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 time_taken_ms = 3;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1564.

```text
_result = 11;
  }
  optional string move_string = 1;
  optional .chesscom.chess.v1.Move move = 2;
  optional int32 time_taken_ms = 3;
  optional .chesscom.chess.v1.Color moved_color = 9;
  optional int32 full_move_number = 10;
}

```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04112"></a>
## FND-04112: chesscom.explanation_engine.v1.MoveDetails.moved_color = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Color moved_color = 9;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1600.

```text
move_string = 1;
  optional .chesscom.chess.v1.Move move = 2;
  optional int32 time_taken_ms = 3;
  optional .chesscom.chess.v1.Color moved_color = 9;
  optional int32 full_move_number = 10;
}

```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04113"></a>
## FND-04113: chesscom.explanation_engine.v1.MoveDetails.full_move_number = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 full_move_number = 10;

### Evidence

- **SRC-0415** `research/proto/chesscom/explanation_engine/v1/move_details.proto` — [preserved redacted evidence](../evidence/text/287d2de96a2d810d3d1513ba0964e3ae0f4c9bac5fae7905bdbacb5ea47038fa.proto)
  Character offset 1653.

```text
ove = 2;
  optional int32 time_taken_ms = 3;
  optional .chesscom.chess.v1.Color moved_color = 9;
  optional int32 full_move_number = 10;
}

```

**Source references:** SRC-0415, SRC-1386  
**URL references:** None independently associated  
**Related findings:** FND-04080, FND-04081, FND-04082

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04114"></a>
## FND-04114: message declaration: chesscom.explanation_engine.v1.MoveList

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MoveList {

### Evidence

- **SRC-0416** `research/proto/chesscom/explanation_engine/v1/move_list.proto` — [preserved redacted evidence](../evidence/text/7429be937fbb1b84c33ee6e92001b996747b134108a16675a5f1e52983fda733.proto)
  Character offset 118.

```text
m/explanation_engine/v1/move_list.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message MoveList {
  repeated .chesscom.chess.v1.Move moves = 1;
}

message UciMoveList {
  repeated string moves = 1;
}

```

**Source references:** SRC-0416, SRC-1387  
**URL references:** None independently associated  
**Related findings:** FND-04115, FND-04116

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04115"></a>
## FND-04115: chesscom.explanation_engine.v1.MoveList.moves = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Move moves = 1;

### Evidence

- **SRC-0416** `research/proto/chesscom/explanation_engine/v1/move_list.proto` — [preserved redacted evidence](../evidence/text/7429be937fbb1b84c33ee6e92001b996747b134108a16675a5f1e52983fda733.proto)
  Character offset 139.

```text
v1/move_list.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message MoveList {
  repeated .chesscom.chess.v1.Move moves = 1;
}

message UciMoveList {
  repeated string moves = 1;
}

```

**Source references:** SRC-0416, SRC-1387  
**URL references:** None independently associated  
**Related findings:** FND-04114, FND-04116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04116"></a>
## FND-04116: message declaration: chesscom.explanation_engine.v1.UciMoveList

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UciMoveList {

### Evidence

- **SRC-0416** `research/proto/chesscom/explanation_engine/v1/move_list.proto` — [preserved redacted evidence](../evidence/text/7429be937fbb1b84c33ee6e92001b996747b134108a16675a5f1e52983fda733.proto)
  Character offset 186.

```text
hesscom.explanation_engine.v1;

message MoveList {
  repeated .chesscom.chess.v1.Move moves = 1;
}

message UciMoveList {
  repeated string moves = 1;
}

```

**Source references:** SRC-0416, SRC-1387  
**URL references:** None independently associated  
**Related findings:** FND-04114, FND-04115

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04117"></a>
## FND-04117: chesscom.explanation_engine.v1.UciMoveList.moves = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string moves = 1;

### Evidence

- **SRC-0416** `research/proto/chesscom/explanation_engine/v1/move_list.proto` — [preserved redacted evidence](../evidence/text/7429be937fbb1b84c33ee6e92001b996747b134108a16675a5f1e52983fda733.proto)
  Character offset 210.

```text
ne.v1;

message MoveList {
  repeated .chesscom.chess.v1.Move moves = 1;
}

message UciMoveList {
  repeated string moves = 1;
}

```

**Source references:** SRC-0416, SRC-1387  
**URL references:** None independently associated  
**Related findings:** FND-04114, FND-04115, FND-04116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04118"></a>
## FND-04118: message declaration: chesscom.explanation_engine.v1.NewGame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NewGame {

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 117.

```text
om/explanation_engine/v1/new_game.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message NewGame {
  oneof from {
  .chesscom.chess.v1.Game game = 1;
  .chesscom.explanation_engine.v1.GameInitialPosition initial_position = 2;
  .chesscom.explanation_engine.v1.TcnGame tcn_game = 4;
  .chesscom.explanation_engine.v1.PositionWithMoves position_with_moves = 5;
  .chesscom.explanation_engine.v1.PgnGame 
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04119, FND-04120

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04119"></a>
## FND-04119: oneof declaration: chesscom.explanation_engine.v1.NewGame.from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof from {

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 137.

```text
e/v1/new_game.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message NewGame {
  oneof from {
  .chesscom.chess.v1.Game game = 1;
  .chesscom.explanation_engine.v1.GameInitialPosition initial_position = 2;
  .chesscom.explanation_engine.v1.TcnGame tcn_game = 4;
  .chesscom.explanation_engine.v1.PositionWithMoves position_with_moves = 5;
  .chesscom.explanation_engine.v1.PgnGame pgn_game = 6;
  }
  
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04120

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04120"></a>
## FND-04120: chesscom.explanation_engine.v1.NewGame.game = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Game game = 1;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 152.

```text
roto
// syntax: proto3

package chesscom.explanation_engine.v1;

message NewGame {
  oneof from {
  .chesscom.chess.v1.Game game = 1;
  .chesscom.explanation_engine.v1.GameInitialPosition initial_position = 2;
  .chesscom.explanation_engine.v1.TcnGame tcn_game = 4;
  .chesscom.explanation_engine.v1.PositionWithMoves position_with_moves = 5;
  .chesscom.explanation_engine.v1.PgnGame pgn_game = 6;
  }
  optional .chess
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04121"></a>
## FND-04121: chesscom.explanation_engine.v1.NewGame.initial_position = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.GameInitialPosition initial_position = 2;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 188.

```text
scom.explanation_engine.v1;

message NewGame {
  oneof from {
  .chesscom.chess.v1.Game game = 1;
  .chesscom.explanation_engine.v1.GameInitialPosition initial_position = 2;
  .chesscom.explanation_engine.v1.TcnGame tcn_game = 4;
  .chesscom.explanation_engine.v1.PositionWithMoves position_with_moves = 5;
  .chesscom.explanation_engine.v1.PgnGame pgn_game = 6;
  }
  optional .chesscom.explanation_engine.v1.GameSettin
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04122"></a>
## FND-04122: chesscom.explanation_engine.v1.NewGame.tcn_game = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.TcnGame tcn_game = 4;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 264.

```text
ess.v1.Game game = 1;
  .chesscom.explanation_engine.v1.GameInitialPosition initial_position = 2;
  .chesscom.explanation_engine.v1.TcnGame tcn_game = 4;
  .chesscom.explanation_engine.v1.PositionWithMoves position_with_moves = 5;
  .chesscom.explanation_engine.v1.PgnGame pgn_game = 6;
  }
  optional .chesscom.explanation_engine.v1.GameSettings settings = 3;
}

message PositionWithMoves {
  oneof move_list {
  .chess
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04123"></a>
## FND-04123: chesscom.explanation_engine.v1.NewGame.position_with_moves = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PositionWithMoves position_with_moves = 5;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 320.

```text
GameInitialPosition initial_position = 2;
  .chesscom.explanation_engine.v1.TcnGame tcn_game = 4;
  .chesscom.explanation_engine.v1.PositionWithMoves position_with_moves = 5;
  .chesscom.explanation_engine.v1.PgnGame pgn_game = 6;
  }
  optional .chesscom.explanation_engine.v1.GameSettings settings = 3;
}

message PositionWithMoves {
  oneof move_list {
  .chesscom.explanation_engine.v1.UciMoveList uci_moves = 2;
  .
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04124"></a>
## FND-04124: chesscom.explanation_engine.v1.NewGame.pgn_game = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PgnGame pgn_game = 6;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 397.

```text
cnGame tcn_game = 4;
  .chesscom.explanation_engine.v1.PositionWithMoves position_with_moves = 5;
  .chesscom.explanation_engine.v1.PgnGame pgn_game = 6;
  }
  optional .chesscom.explanation_engine.v1.GameSettings settings = 3;
}

message PositionWithMoves {
  oneof move_list {
  .chesscom.explanation_engine.v1.UciMoveList uci_moves = 2;
  .chesscom.explanation_engine.v1.MoveList moves = 3;
  }
  optional .chesscom.e
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04125"></a>
## FND-04125: chesscom.explanation_engine.v1.NewGame.settings = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GameSettings settings = 3;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 457.

```text
ionWithMoves position_with_moves = 5;
  .chesscom.explanation_engine.v1.PgnGame pgn_game = 6;
  }
  optional .chesscom.explanation_engine.v1.GameSettings settings = 3;
}

message PositionWithMoves {
  oneof move_list {
  .chesscom.explanation_engine.v1.UciMoveList uci_moves = 2;
  .chesscom.explanation_engine.v1.MoveList moves = 3;
  }
  optional .chesscom.explanation_engine.v1.GameInitialPosition initial_position = 
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04126"></a>
## FND-04126: message declaration: chesscom.explanation_engine.v1.PositionWithMoves

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PositionWithMoves {

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 528.

```text
.PgnGame pgn_game = 6;
  }
  optional .chesscom.explanation_engine.v1.GameSettings settings = 3;
}

message PositionWithMoves {
  oneof move_list {
  .chesscom.explanation_engine.v1.UciMoveList uci_moves = 2;
  .chesscom.explanation_engine.v1.MoveList moves = 3;
  }
  optional .chesscom.explanation_engine.v1.GameInitialPosition initial_position = 1;
}

message GameInitialPosition {
  oneof initial_position {
  .chess
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04127"></a>
## FND-04127: oneof declaration: chesscom.explanation_engine.v1.PositionWithMoves.move_list

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof move_list {

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 558.

```text
ptional .chesscom.explanation_engine.v1.GameSettings settings = 3;
}

message PositionWithMoves {
  oneof move_list {
  .chesscom.explanation_engine.v1.UciMoveList uci_moves = 2;
  .chesscom.explanation_engine.v1.MoveList moves = 3;
  }
  optional .chesscom.explanation_engine.v1.GameInitialPosition initial_position = 1;
}

message GameInitialPosition {
  oneof initial_position {
  .chesscom.chess.v1.Position position
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04128"></a>
## FND-04128: chesscom.explanation_engine.v1.PositionWithMoves.uci_moves = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.UciMoveList uci_moves = 2;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 578.

```text
planation_engine.v1.GameSettings settings = 3;
}

message PositionWithMoves {
  oneof move_list {
  .chesscom.explanation_engine.v1.UciMoveList uci_moves = 2;
  .chesscom.explanation_engine.v1.MoveList moves = 3;
  }
  optional .chesscom.explanation_engine.v1.GameInitialPosition initial_position = 1;
}

message GameInitialPosition {
  oneof initial_position {
  .chesscom.chess.v1.Position position = 2;
  bytes compre
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04129"></a>
## FND-04129: chesscom.explanation_engine.v1.PositionWithMoves.moves = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.MoveList moves = 3;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 639.

```text
itionWithMoves {
  oneof move_list {
  .chesscom.explanation_engine.v1.UciMoveList uci_moves = 2;
  .chesscom.explanation_engine.v1.MoveList moves = 3;
  }
  optional .chesscom.explanation_engine.v1.GameInitialPosition initial_position = 1;
}

message GameInitialPosition {
  oneof initial_position {
  .chesscom.chess.v1.Position position = 2;
  bytes compressed_position = 3;
  string fen = 4;
  }
  optional .chesscom
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04130"></a>
## FND-04130: chesscom.explanation_engine.v1.PositionWithMoves.initial_position = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GameInitialPosition initial_position = 1;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 697.

```text
on_engine.v1.UciMoveList uci_moves = 2;
  .chesscom.explanation_engine.v1.MoveList moves = 3;
  }
  optional .chesscom.explanation_engine.v1.GameInitialPosition initial_position = 1;
}

message GameInitialPosition {
  oneof initial_position {
  .chesscom.chess.v1.Position position = 2;
  bytes compressed_position = 3;
  string fen = 4;
  }
  optional .chesscom.chess.v1.GameMetadata metadata = 1;
}

message PgnGame {

```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04131"></a>
## FND-04131: message declaration: chesscom.explanation_engine.v1.GameInitialPosition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameInitialPosition {

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 783.

```text
es = 3;
  }
  optional .chesscom.explanation_engine.v1.GameInitialPosition initial_position = 1;
}

message GameInitialPosition {
  oneof initial_position {
  .chesscom.chess.v1.Position position = 2;
  bytes compressed_position = 3;
  string fen = 4;
  }
  optional .chesscom.chess.v1.GameMetadata metadata = 1;
}

message PgnGame {
  optional string pgn = 1;
  optional bool take_first_game_only = 2;
  optional string
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04132"></a>
## FND-04132: oneof declaration: chesscom.explanation_engine.v1.GameInitialPosition.initial_position

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof initial_position {

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 815.

```text
.explanation_engine.v1.GameInitialPosition initial_position = 1;
}

message GameInitialPosition {
  oneof initial_position {
  .chesscom.chess.v1.Position position = 2;
  bytes compressed_position = 3;
  string fen = 4;
  }
  optional .chesscom.chess.v1.GameMetadata metadata = 1;
}

message PgnGame {
  optional string pgn = 1;
  optional bool take_first_game_only = 2;
  optional string artifact_id = 3;
  optional .ch
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04133"></a>
## FND-04133: chesscom.explanation_engine.v1.GameInitialPosition.position = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Position position = 2;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 842.

```text
InitialPosition initial_position = 1;
}

message GameInitialPosition {
  oneof initial_position {
  .chesscom.chess.v1.Position position = 2;
  bytes compressed_position = 3;
  string fen = 4;
  }
  optional .chesscom.chess.v1.GameMetadata metadata = 1;
}

message PgnGame {
  optional string pgn = 1;
  optional bool take_first_game_only = 2;
  optional string artifact_id = 3;
  optional .chesscom.chess.v1.GameMetadat
```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04134"></a>
## FND-04134: chesscom.explanation_engine.v1.GameInitialPosition.compressed_position = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bytes compressed_position = 3;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 886.

```text
sage GameInitialPosition {
  oneof initial_position {
  .chesscom.chess.v1.Position position = 2;
  bytes compressed_position = 3;
  string fen = 4;
  }
  optional .chesscom.chess.v1.GameMetadata metadata = 1;
}

message PgnGame {
  optional string pgn = 1;
  optional bool take_first_game_only = 2;
  optional string artifact_id = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04135"></a>
## FND-04135: chesscom.explanation_engine.v1.GameInitialPosition.fen = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string fen = 4;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 919.

```text
f initial_position {
  .chesscom.chess.v1.Position position = 2;
  bytes compressed_position = 3;
  string fen = 4;
  }
  optional .chesscom.chess.v1.GameMetadata metadata = 1;
}

message PgnGame {
  optional string pgn = 1;
  optional bool take_first_game_only = 2;
  optional string artifact_id = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04136"></a>
## FND-04136: chesscom.explanation_engine.v1.GameInitialPosition.metadata = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.GameMetadata metadata = 1;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 941.

```text
 .chesscom.chess.v1.Position position = 2;
  bytes compressed_position = 3;
  string fen = 4;
  }
  optional .chesscom.chess.v1.GameMetadata metadata = 1;
}

message PgnGame {
  optional string pgn = 1;
  optional bool take_first_game_only = 2;
  optional string artifact_id = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04137"></a>
## FND-04137: message declaration: chesscom.explanation_engine.v1.PgnGame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PgnGame {

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 999.

```text
sed_position = 3;
  string fen = 4;
  }
  optional .chesscom.chess.v1.GameMetadata metadata = 1;
}

message PgnGame {
  optional string pgn = 1;
  optional bool take_first_game_only = 2;
  optional string artifact_id = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04138"></a>
## FND-04138: chesscom.explanation_engine.v1.PgnGame.pgn = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string pgn = 1;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 1019.

```text
string fen = 4;
  }
  optional .chesscom.chess.v1.GameMetadata metadata = 1;
}

message PgnGame {
  optional string pgn = 1;
  optional bool take_first_game_only = 2;
  optional string artifact_id = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04139"></a>
## FND-04139: chesscom.explanation_engine.v1.PgnGame.take_first_game_only = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool take_first_game_only = 2;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 1046.

```text
nal .chesscom.chess.v1.GameMetadata metadata = 1;
}

message PgnGame {
  optional string pgn = 1;
  optional bool take_first_game_only = 2;
  optional string artifact_id = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04140"></a>
## FND-04140: chesscom.explanation_engine.v1.PgnGame.artifact_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string artifact_id = 3;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 1088.

```text
ta = 1;
}

message PgnGame {
  optional string pgn = 1;
  optional bool take_first_game_only = 2;
  optional string artifact_id = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04141"></a>
## FND-04141: chesscom.explanation_engine.v1.PgnGame.metadata = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.GameMetadata metadata = 4;

### Evidence

- **SRC-0417** `research/proto/chesscom/explanation_engine/v1/new_game.proto` — [preserved redacted evidence](../evidence/text/ce3e392e6fce6a8435b8610626b043010093583ee567a5d6c276f144bf8ad3d3.proto)
  Character offset 1123.

```text
onal string pgn = 1;
  optional bool take_first_game_only = 2;
  optional string artifact_id = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0417, SRC-1388  
**URL references:** None independently associated  
**Related findings:** FND-04118, FND-04119, FND-04120

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04142"></a>
## FND-04142: enum declaration: chesscom.explanation_engine.v1.FenNotation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum FenNotation {

### Evidence

- **SRC-0418** `research/proto/chesscom/explanation_engine/v1/notation.proto` — [preserved redacted evidence](../evidence/text/dcf6e38f0428b25ec6fe76d5534b007d74550700f0a7a562311a069d9ab4d295.proto)
  Character offset 117.

```text
om/explanation_engine/v1/notation.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum FenNotation {
  FEN_NOTATION_UNSPECIFIED = 0;
  FEN_NOTATION_INFERRED = 1;
  FEN_NOTATION_STANDARD = 2;
  FEN_NOTATION_SHREDDER = 3;
}

```

**Source references:** SRC-0418, SRC-1389  
**URL references:** None independently associated  
**Related findings:** FND-04143, FND-04144

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04143"></a>
## FND-04143: chesscom.explanation_engine.v1.FenNotation.FEN_NOTATION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEN_NOTATION_UNSPECIFIED = 0;

### Evidence

- **SRC-0418** `research/proto/chesscom/explanation_engine/v1/notation.proto` — [preserved redacted evidence](../evidence/text/dcf6e38f0428b25ec6fe76d5534b007d74550700f0a7a562311a069d9ab4d295.proto)
  Character offset 138.

```text
/v1/notation.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum FenNotation {
  FEN_NOTATION_UNSPECIFIED = 0;
  FEN_NOTATION_INFERRED = 1;
  FEN_NOTATION_STANDARD = 2;
  FEN_NOTATION_SHREDDER = 3;
}

```

**Source references:** SRC-0418, SRC-1389  
**URL references:** None independently associated  
**Related findings:** FND-04142, FND-04144

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04144"></a>
## FND-04144: chesscom.explanation_engine.v1.FenNotation.FEN_NOTATION_INFERRED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEN_NOTATION_INFERRED = 1;

### Evidence

- **SRC-0418** `research/proto/chesscom/explanation_engine/v1/notation.proto` — [preserved redacted evidence](../evidence/text/dcf6e38f0428b25ec6fe76d5534b007d74550700f0a7a562311a069d9ab4d295.proto)
  Character offset 170.

```text
oto3

package chesscom.explanation_engine.v1;

enum FenNotation {
  FEN_NOTATION_UNSPECIFIED = 0;
  FEN_NOTATION_INFERRED = 1;
  FEN_NOTATION_STANDARD = 2;
  FEN_NOTATION_SHREDDER = 3;
}

```

**Source references:** SRC-0418, SRC-1389  
**URL references:** None independently associated  
**Related findings:** FND-04142, FND-04143

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04145"></a>
## FND-04145: chesscom.explanation_engine.v1.FenNotation.FEN_NOTATION_STANDARD = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEN_NOTATION_STANDARD = 2;

### Evidence

- **SRC-0418** `research/proto/chesscom/explanation_engine/v1/notation.proto` — [preserved redacted evidence](../evidence/text/dcf6e38f0428b25ec6fe76d5534b007d74550700f0a7a562311a069d9ab4d295.proto)
  Character offset 199.

```text
ation_engine.v1;

enum FenNotation {
  FEN_NOTATION_UNSPECIFIED = 0;
  FEN_NOTATION_INFERRED = 1;
  FEN_NOTATION_STANDARD = 2;
  FEN_NOTATION_SHREDDER = 3;
}

```

**Source references:** SRC-0418, SRC-1389  
**URL references:** None independently associated  
**Related findings:** FND-04142, FND-04143, FND-04144

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04146"></a>
## FND-04146: chesscom.explanation_engine.v1.FenNotation.FEN_NOTATION_SHREDDER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

FEN_NOTATION_SHREDDER = 3;

### Evidence

- **SRC-0418** `research/proto/chesscom/explanation_engine/v1/notation.proto` — [preserved redacted evidence](../evidence/text/dcf6e38f0428b25ec6fe76d5534b007d74550700f0a7a562311a069d9ab4d295.proto)
  Character offset 228.

```text
ation {
  FEN_NOTATION_UNSPECIFIED = 0;
  FEN_NOTATION_INFERRED = 1;
  FEN_NOTATION_STANDARD = 2;
  FEN_NOTATION_SHREDDER = 3;
}

```

**Source references:** SRC-0418, SRC-1389  
**URL references:** None independently associated  
**Related findings:** FND-04142, FND-04143, FND-04144

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04147"></a>
## FND-04147: message declaration: chesscom.explanation_engine.v1.Opening

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Opening {

### Evidence

- **SRC-0419** `research/proto/chesscom/explanation_engine/v1/opening.proto` — [preserved redacted evidence](../evidence/text/859a88415f8cf198928bffe84b7eb4a0ffcc92b46009c4ae4bcc9bafa6d79f44.proto)
  Character offset 116.

```text
com/explanation_engine/v1/opening.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message Opening {
  oneof _opening_name {
  string opening_name = 1;
  }
  oneof _tcn_moves {
  string tcn_moves = 2;
  }
  oneof _eco_code {
  string eco_code = 3;
  }
  oneof _url {
  string url = 4;
  }
}

```

**Source references:** SRC-0419, SRC-1390  
**URL references:** None independently associated  
**Related findings:** FND-04148, FND-04149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04148"></a>
## FND-04148: oneof declaration: chesscom.explanation_engine.v1.Opening._opening_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening_name {

### Evidence

- **SRC-0419** `research/proto/chesscom/explanation_engine/v1/opening.proto` — [preserved redacted evidence](../evidence/text/859a88415f8cf198928bffe84b7eb4a0ffcc92b46009c4ae4bcc9bafa6d79f44.proto)
  Character offset 136.

```text
ne/v1/opening.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message Opening {
  oneof _opening_name {
  string opening_name = 1;
  }
  oneof _tcn_moves {
  string tcn_moves = 2;
  }
  oneof _eco_code {
  string eco_code = 3;
  }
  oneof _url {
  string url = 4;
  }
}

```

**Source references:** SRC-0419, SRC-1390  
**URL references:** None independently associated  
**Related findings:** FND-04147, FND-04149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04149"></a>
## FND-04149: chesscom.explanation_engine.v1.Opening.opening_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opening_name = 1;

### Evidence

- **SRC-0419** `research/proto/chesscom/explanation_engine/v1/opening.proto` — [preserved redacted evidence](../evidence/text/859a88415f8cf198928bffe84b7eb4a0ffcc92b46009c4ae4bcc9bafa6d79f44.proto)
  Character offset 160.

```text
yntax: proto3

package chesscom.explanation_engine.v1;

message Opening {
  oneof _opening_name {
  string opening_name = 1;
  }
  oneof _tcn_moves {
  string tcn_moves = 2;
  }
  oneof _eco_code {
  string eco_code = 3;
  }
  oneof _url {
  string url = 4;
  }
}

```

**Source references:** SRC-0419, SRC-1390  
**URL references:** None independently associated  
**Related findings:** FND-04147, FND-04148

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04150"></a>
## FND-04150: oneof declaration: chesscom.explanation_engine.v1.Opening._tcn_moves

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tcn_moves {

### Evidence

- **SRC-0419** `research/proto/chesscom/explanation_engine/v1/opening.proto` — [preserved redacted evidence](../evidence/text/859a88415f8cf198928bffe84b7eb4a0ffcc92b46009c4ae4bcc9bafa6d79f44.proto)
  Character offset 191.

```text
.explanation_engine.v1;

message Opening {
  oneof _opening_name {
  string opening_name = 1;
  }
  oneof _tcn_moves {
  string tcn_moves = 2;
  }
  oneof _eco_code {
  string eco_code = 3;
  }
  oneof _url {
  string url = 4;
  }
}

```

**Source references:** SRC-0419, SRC-1390  
**URL references:** None independently associated  
**Related findings:** FND-04147, FND-04148, FND-04149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04151"></a>
## FND-04151: chesscom.explanation_engine.v1.Opening.tcn_moves = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string tcn_moves = 2;

### Evidence

- **SRC-0419** `research/proto/chesscom/explanation_engine/v1/opening.proto` — [preserved redacted evidence](../evidence/text/859a88415f8cf198928bffe84b7eb4a0ffcc92b46009c4ae4bcc9bafa6d79f44.proto)
  Character offset 212.

```text
1;

message Opening {
  oneof _opening_name {
  string opening_name = 1;
  }
  oneof _tcn_moves {
  string tcn_moves = 2;
  }
  oneof _eco_code {
  string eco_code = 3;
  }
  oneof _url {
  string url = 4;
  }
}

```

**Source references:** SRC-0419, SRC-1390  
**URL references:** None independently associated  
**Related findings:** FND-04147, FND-04148, FND-04149

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04152"></a>
## FND-04152: oneof declaration: chesscom.explanation_engine.v1.Opening._eco_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _eco_code {

### Evidence

- **SRC-0419** `research/proto/chesscom/explanation_engine/v1/opening.proto` — [preserved redacted evidence](../evidence/text/859a88415f8cf198928bffe84b7eb4a0ffcc92b46009c4ae4bcc9bafa6d79f44.proto)
  Character offset 240.

```text
f _opening_name {
  string opening_name = 1;
  }
  oneof _tcn_moves {
  string tcn_moves = 2;
  }
  oneof _eco_code {
  string eco_code = 3;
  }
  oneof _url {
  string url = 4;
  }
}

```

**Source references:** SRC-0419, SRC-1390  
**URL references:** None independently associated  
**Related findings:** FND-04147, FND-04148, FND-04149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04153"></a>
## FND-04153: chesscom.explanation_engine.v1.Opening.eco_code = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string eco_code = 3;

### Evidence

- **SRC-0419** `research/proto/chesscom/explanation_engine/v1/opening.proto` — [preserved redacted evidence](../evidence/text/859a88415f8cf198928bffe84b7eb4a0ffcc92b46009c4ae4bcc9bafa6d79f44.proto)
  Character offset 260.

```text
string opening_name = 1;
  }
  oneof _tcn_moves {
  string tcn_moves = 2;
  }
  oneof _eco_code {
  string eco_code = 3;
  }
  oneof _url {
  string url = 4;
  }
}

```

**Source references:** SRC-0419, SRC-1390  
**URL references:** None independently associated  
**Related findings:** FND-04147, FND-04148, FND-04149

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04154"></a>
## FND-04154: oneof declaration: chesscom.explanation_engine.v1.Opening._url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _url {

### Evidence

- **SRC-0419** `research/proto/chesscom/explanation_engine/v1/opening.proto` — [preserved redacted evidence](../evidence/text/859a88415f8cf198928bffe84b7eb4a0ffcc92b46009c4ae4bcc9bafa6d79f44.proto)
  Character offset 287.

```text
}
  oneof _tcn_moves {
  string tcn_moves = 2;
  }
  oneof _eco_code {
  string eco_code = 3;
  }
  oneof _url {
  string url = 4;
  }
}

```

**Source references:** SRC-0419, SRC-1390  
**URL references:** None independently associated  
**Related findings:** FND-04147, FND-04148, FND-04149

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04155"></a>
## FND-04155: chesscom.explanation_engine.v1.Opening.url = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string url = 4;

### Evidence

- **SRC-0419** `research/proto/chesscom/explanation_engine/v1/opening.proto` — [preserved redacted evidence](../evidence/text/859a88415f8cf198928bffe84b7eb4a0ffcc92b46009c4ae4bcc9bafa6d79f44.proto)
  Character offset 302.

```text
moves {
  string tcn_moves = 2;
  }
  oneof _eco_code {
  string eco_code = 3;
  }
  oneof _url {
  string url = 4;
  }
}

```

**Source references:** SRC-0419, SRC-1390  
**URL references:** None independently associated  
**Related findings:** FND-04147, FND-04148, FND-04149

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04156"></a>
## FND-04156: message declaration: chesscom.explanation_engine.v1.PunishMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PunishMove {

### Evidence

- **SRC-0420** `research/proto/chesscom/explanation_engine/v1/punish_move.proto` — [preserved redacted evidence](../evidence/text/6e645dc6a2d2f736326fc6551ea6cf264ec440518b292eb913241cfcbe8b5b70.proto)
  Character offset 120.

```text
explanation_engine/v1/punish_move.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message PunishMove {
  oneof _arrow {
  .chesscom.chess.v1.Arrow arrow = 1;
  }
  oneof _move {
  .chesscom.chess.v1.Move move = 6;
  }
  optional .chesscom.engine.v1.Evaluation evaluation = 2;
  optional .chesscom.explanation_engine.v1.Speech speech = 3;
  optional string show_moves = 4;
  optional string hide_moves =
```

**Source references:** SRC-0420, SRC-1391  
**URL references:** None independently associated  
**Related findings:** FND-04157, FND-04158

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04157"></a>
## FND-04157: oneof declaration: chesscom.explanation_engine.v1.PunishMove._arrow

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _arrow {

### Evidence

- **SRC-0420** `research/proto/chesscom/explanation_engine/v1/punish_move.proto` — [preserved redacted evidence](../evidence/text/6e645dc6a2d2f736326fc6551ea6cf264ec440518b292eb913241cfcbe8b5b70.proto)
  Character offset 143.

```text
unish_move.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message PunishMove {
  oneof _arrow {
  .chesscom.chess.v1.Arrow arrow = 1;
  }
  oneof _move {
  .chesscom.chess.v1.Move move = 6;
  }
  optional .chesscom.engine.v1.Evaluation evaluation = 2;
  optional .chesscom.explanation_engine.v1.Speech speech = 3;
  optional string show_moves = 4;
  optional string hide_moves = 5;
}

```

**Source references:** SRC-0420, SRC-1391  
**URL references:** None independently associated  
**Related findings:** FND-04156, FND-04158

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04158"></a>
## FND-04158: chesscom.explanation_engine.v1.PunishMove.arrow = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Arrow arrow = 1;

### Evidence

- **SRC-0420** `research/proto/chesscom/explanation_engine/v1/punish_move.proto` — [preserved redacted evidence](../evidence/text/6e645dc6a2d2f736326fc6551ea6cf264ec440518b292eb913241cfcbe8b5b70.proto)
  Character offset 160.

```text
// syntax: proto3

package chesscom.explanation_engine.v1;

message PunishMove {
  oneof _arrow {
  .chesscom.chess.v1.Arrow arrow = 1;
  }
  oneof _move {
  .chesscom.chess.v1.Move move = 6;
  }
  optional .chesscom.engine.v1.Evaluation evaluation = 2;
  optional .chesscom.explanation_engine.v1.Speech speech = 3;
  optional string show_moves = 4;
  optional string hide_moves = 5;
}

```

**Source references:** SRC-0420, SRC-1391  
**URL references:** None independently associated  
**Related findings:** FND-04156, FND-04157

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04159"></a>
## FND-04159: oneof declaration: chesscom.explanation_engine.v1.PunishMove._move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _move {

### Evidence

- **SRC-0420** `research/proto/chesscom/explanation_engine/v1/punish_move.proto` — [preserved redacted evidence](../evidence/text/6e645dc6a2d2f736326fc6551ea6cf264ec440518b292eb913241cfcbe8b5b70.proto)
  Character offset 202.

```text
ation_engine.v1;

message PunishMove {
  oneof _arrow {
  .chesscom.chess.v1.Arrow arrow = 1;
  }
  oneof _move {
  .chesscom.chess.v1.Move move = 6;
  }
  optional .chesscom.engine.v1.Evaluation evaluation = 2;
  optional .chesscom.explanation_engine.v1.Speech speech = 3;
  optional string show_moves = 4;
  optional string hide_moves = 5;
}

```

**Source references:** SRC-0420, SRC-1391  
**URL references:** None independently associated  
**Related findings:** FND-04156, FND-04157, FND-04158

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04160"></a>
## FND-04160: chesscom.explanation_engine.v1.PunishMove.move = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Move move = 6;

### Evidence

- **SRC-0420** `research/proto/chesscom/explanation_engine/v1/punish_move.proto` — [preserved redacted evidence](../evidence/text/6e645dc6a2d2f736326fc6551ea6cf264ec440518b292eb913241cfcbe8b5b70.proto)
  Character offset 218.

```text


message PunishMove {
  oneof _arrow {
  .chesscom.chess.v1.Arrow arrow = 1;
  }
  oneof _move {
  .chesscom.chess.v1.Move move = 6;
  }
  optional .chesscom.engine.v1.Evaluation evaluation = 2;
  optional .chesscom.explanation_engine.v1.Speech speech = 3;
  optional string show_moves = 4;
  optional string hide_moves = 5;
}

```

**Source references:** SRC-0420, SRC-1391  
**URL references:** None independently associated  
**Related findings:** FND-04156, FND-04157, FND-04158

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04161"></a>
## FND-04161: chesscom.explanation_engine.v1.PunishMove.evaluation = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.engine.v1.Evaluation evaluation = 2;

### Evidence

- **SRC-0420** `research/proto/chesscom/explanation_engine/v1/punish_move.proto` — [preserved redacted evidence](../evidence/text/6e645dc6a2d2f736326fc6551ea6cf264ec440518b292eb913241cfcbe8b5b70.proto)
  Character offset 258.

```text
  .chesscom.chess.v1.Arrow arrow = 1;
  }
  oneof _move {
  .chesscom.chess.v1.Move move = 6;
  }
  optional .chesscom.engine.v1.Evaluation evaluation = 2;
  optional .chesscom.explanation_engine.v1.Speech speech = 3;
  optional string show_moves = 4;
  optional string hide_moves = 5;
}

```

**Source references:** SRC-0420, SRC-1391  
**URL references:** None independently associated  
**Related findings:** FND-04156, FND-04157, FND-04158

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04162"></a>
## FND-04162: chesscom.explanation_engine.v1.PunishMove.speech = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech speech = 3;

### Evidence

- **SRC-0420** `research/proto/chesscom/explanation_engine/v1/punish_move.proto` — [preserved redacted evidence](../evidence/text/6e645dc6a2d2f736326fc6551ea6cf264ec440518b292eb913241cfcbe8b5b70.proto)
  Character offset 316.

```text
  .chesscom.chess.v1.Move move = 6;
  }
  optional .chesscom.engine.v1.Evaluation evaluation = 2;
  optional .chesscom.explanation_engine.v1.Speech speech = 3;
  optional string show_moves = 4;
  optional string hide_moves = 5;
}

```

**Source references:** SRC-0420, SRC-1391  
**URL references:** None independently associated  
**Related findings:** FND-04156, FND-04157, FND-04158

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04163"></a>
## FND-04163: chesscom.explanation_engine.v1.PunishMove.show_moves = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string show_moves = 4;

### Evidence

- **SRC-0420** `research/proto/chesscom/explanation_engine/v1/punish_move.proto` — [preserved redacted evidence](../evidence/text/6e645dc6a2d2f736326fc6551ea6cf264ec440518b292eb913241cfcbe8b5b70.proto)
  Character offset 378.

```text
ngine.v1.Evaluation evaluation = 2;
  optional .chesscom.explanation_engine.v1.Speech speech = 3;
  optional string show_moves = 4;
  optional string hide_moves = 5;
}

```

**Source references:** SRC-0420, SRC-1391  
**URL references:** None independently associated  
**Related findings:** FND-04156, FND-04157, FND-04158

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04164"></a>
## FND-04164: chesscom.explanation_engine.v1.PunishMove.hide_moves = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string hide_moves = 5;

### Evidence

- **SRC-0420** `research/proto/chesscom/explanation_engine/v1/punish_move.proto` — [preserved redacted evidence](../evidence/text/6e645dc6a2d2f736326fc6551ea6cf264ec440518b292eb913241cfcbe8b5b70.proto)
  Character offset 412.

```text
;
  optional .chesscom.explanation_engine.v1.Speech speech = 3;
  optional string show_moves = 4;
  optional string hide_moves = 5;
}

```

**Source references:** SRC-0420, SRC-1391  
**URL references:** None independently associated  
**Related findings:** FND-04156, FND-04157, FND-04158

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04165"></a>
## FND-04165: enum declaration: chesscom.explanation_engine.v1.PuzzleGenMode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PuzzleGenMode {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 119.

```text
/explanation_engine/v1/puzzle_gen.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum PuzzleGenMode {
  PUZZLE_GEN_MODE_UNSPECIFIED = 0;
  PUZZLE_GEN_MODE_TACTICAL = 1;
  PUZZLE_GEN_MODE_STRATEGIC = 2;
}

enum PuzzleWinningResult {
  PUZZLE_WINNING_RESULT_UNSPECIFIED = 0;
  PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD = 1;
}

enum TacticalGoalType {
  TACTICAL_GOAL_TYPE_UNSPECIFIED = 0;
  TACTICAL_GOAL
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04166"></a>
## FND-04166: chesscom.explanation_engine.v1.PuzzleGenMode.PUZZLE_GEN_MODE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_MODE_UNSPECIFIED = 0;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 142.

```text
puzzle_gen.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum PuzzleGenMode {
  PUZZLE_GEN_MODE_UNSPECIFIED = 0;
  PUZZLE_GEN_MODE_TACTICAL = 1;
  PUZZLE_GEN_MODE_STRATEGIC = 2;
}

enum PuzzleWinningResult {
  PUZZLE_WINNING_RESULT_UNSPECIFIED = 0;
  PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD = 1;
}

enum TacticalGoalType {
  TACTICAL_GOAL_TYPE_UNSPECIFIED = 0;
  TACTICAL_GOAL_TYPE_CHECKMATE = 1;
  
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04167"></a>
## FND-04167: chesscom.explanation_engine.v1.PuzzleGenMode.PUZZLE_GEN_MODE_TACTICAL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_MODE_TACTICAL = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 177.

```text

package chesscom.explanation_engine.v1;

enum PuzzleGenMode {
  PUZZLE_GEN_MODE_UNSPECIFIED = 0;
  PUZZLE_GEN_MODE_TACTICAL = 1;
  PUZZLE_GEN_MODE_STRATEGIC = 2;
}

enum PuzzleWinningResult {
  PUZZLE_WINNING_RESULT_UNSPECIFIED = 0;
  PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD = 1;
}

enum TacticalGoalType {
  TACTICAL_GOAL_TYPE_UNSPECIFIED = 0;
  TACTICAL_GOAL_TYPE_CHECKMATE = 1;
  TACTICAL_GOAL_TYPE_PROMOTION = 2;
 
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04168"></a>
## FND-04168: chesscom.explanation_engine.v1.PuzzleGenMode.PUZZLE_GEN_MODE_STRATEGIC = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_MODE_STRATEGIC = 2;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 209.

```text
gine.v1;

enum PuzzleGenMode {
  PUZZLE_GEN_MODE_UNSPECIFIED = 0;
  PUZZLE_GEN_MODE_TACTICAL = 1;
  PUZZLE_GEN_MODE_STRATEGIC = 2;
}

enum PuzzleWinningResult {
  PUZZLE_WINNING_RESULT_UNSPECIFIED = 0;
  PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD = 1;
}

enum TacticalGoalType {
  TACTICAL_GOAL_TYPE_UNSPECIFIED = 0;
  TACTICAL_GOAL_TYPE_CHECKMATE = 1;
  TACTICAL_GOAL_TYPE_PROMOTION = 2;
  TACTICAL_GOAL_TYPE_ATTACK_THE_K
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04169"></a>
## FND-04169: enum declaration: chesscom.explanation_engine.v1.PuzzleWinningResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PuzzleWinningResult {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 243.

```text
UZZLE_GEN_MODE_UNSPECIFIED = 0;
  PUZZLE_GEN_MODE_TACTICAL = 1;
  PUZZLE_GEN_MODE_STRATEGIC = 2;
}

enum PuzzleWinningResult {
  PUZZLE_WINNING_RESULT_UNSPECIFIED = 0;
  PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD = 1;
}

enum TacticalGoalType {
  TACTICAL_GOAL_TYPE_UNSPECIFIED = 0;
  TACTICAL_GOAL_TYPE_CHECKMATE = 1;
  TACTICAL_GOAL_TYPE_PROMOTION = 2;
  TACTICAL_GOAL_TYPE_ATTACK_THE_KING = 3;
  TACTICAL_GOAL_TYPE_WIN_
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04170"></a>
## FND-04170: chesscom.explanation_engine.v1.PuzzleWinningResult.PUZZLE_WINNING_RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_WINNING_RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 272.

```text
0;
  PUZZLE_GEN_MODE_TACTICAL = 1;
  PUZZLE_GEN_MODE_STRATEGIC = 2;
}

enum PuzzleWinningResult {
  PUZZLE_WINNING_RESULT_UNSPECIFIED = 0;
  PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD = 1;
}

enum TacticalGoalType {
  TACTICAL_GOAL_TYPE_UNSPECIFIED = 0;
  TACTICAL_GOAL_TYPE_CHECKMATE = 1;
  TACTICAL_GOAL_TYPE_PROMOTION = 2;
  TACTICAL_GOAL_TYPE_ATTACK_THE_KING = 3;
  TACTICAL_GOAL_TYPE_WIN_MATERIAL = 4;
  TACTICAL_GOAL
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04171"></a>
## FND-04171: chesscom.explanation_engine.v1.PuzzleWinningResult.PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 313.

```text
LE_GEN_MODE_STRATEGIC = 2;
}

enum PuzzleWinningResult {
  PUZZLE_WINNING_RESULT_UNSPECIFIED = 0;
  PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD = 1;
}

enum TacticalGoalType {
  TACTICAL_GOAL_TYPE_UNSPECIFIED = 0;
  TACTICAL_GOAL_TYPE_CHECKMATE = 1;
  TACTICAL_GOAL_TYPE_PROMOTION = 2;
  TACTICAL_GOAL_TYPE_ATTACK_THE_KING = 3;
  TACTICAL_GOAL_TYPE_WIN_MATERIAL = 4;
  TACTICAL_GOAL_TYPE_DEFENSE = 5;
  TACTICAL_GOAL_TYPE_P
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04172"></a>
## FND-04172: enum declaration: chesscom.explanation_engine.v1.TacticalGoalType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TacticalGoalType {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 362.

```text
esult {
  PUZZLE_WINNING_RESULT_UNSPECIFIED = 0;
  PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD = 1;
}

enum TacticalGoalType {
  TACTICAL_GOAL_TYPE_UNSPECIFIED = 0;
  TACTICAL_GOAL_TYPE_CHECKMATE = 1;
  TACTICAL_GOAL_TYPE_PROMOTION = 2;
  TACTICAL_GOAL_TYPE_ATTACK_THE_KING = 3;
  TACTICAL_GOAL_TYPE_WIN_MATERIAL = 4;
  TACTICAL_GOAL_TYPE_DEFENSE = 5;
  TACTICAL_GOAL_TYPE_PROMOTION_POSITION = 6;
  TACTICAL_GOAL_TYPE_DISTA
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04173"></a>
## FND-04173: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TACTICAL_GOAL_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 388.

```text
ESULT_UNSPECIFIED = 0;
  PUZZLE_WINNING_RESULT_CHECKMATE_ON_BOARD = 1;
}

enum TacticalGoalType {
  TACTICAL_GOAL_TYPE_UNSPECIFIED = 0;
  TACTICAL_GOAL_TYPE_CHECKMATE = 1;
  TACTICAL_GOAL_TYPE_PROMOTION = 2;
  TACTICAL_GOAL_TYPE_ATTACK_THE_KING = 3;
  TACTICAL_GOAL_TYPE_WIN_MATERIAL = 4;
  TACTICAL_GOAL_TYPE_DEFENSE = 5;
  TACTICAL_GOAL_TYPE_PROMOTION_POSITION = 6;
  TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE = 7;
}

enum 
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04174"></a>
## FND-04174: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_CHECKMATE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TACTICAL_GOAL_TYPE_CHECKMATE = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 426.

```text
G_RESULT_CHECKMATE_ON_BOARD = 1;
}

enum TacticalGoalType {
  TACTICAL_GOAL_TYPE_UNSPECIFIED = 0;
  TACTICAL_GOAL_TYPE_CHECKMATE = 1;
  TACTICAL_GOAL_TYPE_PROMOTION = 2;
  TACTICAL_GOAL_TYPE_ATTACK_THE_KING = 3;
  TACTICAL_GOAL_TYPE_WIN_MATERIAL = 4;
  TACTICAL_GOAL_TYPE_DEFENSE = 5;
  TACTICAL_GOAL_TYPE_PROMOTION_POSITION = 6;
  TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE = 7;
}

enum StrategicGoalType {
  STRATEGIC_GOAL_T
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
