# data_models — findings 4001–4100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-04275"></a>
## FND-04275: oneof declaration: chesscom.explanation_engine.v1.TacticalGoal.goal

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof goal {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5468.

```text
ional .chesscom.explanation_engine.v1.PuzzleThemeType theme_type = 255;
}

message TacticalGoal {
  oneof goal {
  .chesscom.explanation_engine.v1.TacticalGoalCheckmate checkmate = 1;
  .chesscom.explanation_engine.v1.TacticalGoalPromotion promotion = 2;
  .chesscom.explanation_engine.v1.TacticalGoalAttackTheKing attack_the_king = 3;
  .chesscom.explanation_engine.v1.TacticalGoalWinMaterial win_material = 4;
  .chess
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04276"></a>
## FND-04276: chesscom.explanation_engine.v1.TacticalGoal.checkmate = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.TacticalGoalCheckmate checkmate = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5483.

```text
.explanation_engine.v1.PuzzleThemeType theme_type = 255;
}

message TacticalGoal {
  oneof goal {
  .chesscom.explanation_engine.v1.TacticalGoalCheckmate checkmate = 1;
  .chesscom.explanation_engine.v1.TacticalGoalPromotion promotion = 2;
  .chesscom.explanation_engine.v1.TacticalGoalAttackTheKing attack_the_king = 3;
  .chesscom.explanation_engine.v1.TacticalGoalWinMaterial win_material = 4;
  .chesscom.explanation
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04277"></a>
## FND-04277: chesscom.explanation_engine.v1.TacticalGoal.promotion = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.TacticalGoalPromotion promotion = 2;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5554.

```text
ticalGoal {
  oneof goal {
  .chesscom.explanation_engine.v1.TacticalGoalCheckmate checkmate = 1;
  .chesscom.explanation_engine.v1.TacticalGoalPromotion promotion = 2;
  .chesscom.explanation_engine.v1.TacticalGoalAttackTheKing attack_the_king = 3;
  .chesscom.explanation_engine.v1.TacticalGoalWinMaterial win_material = 4;
  .chesscom.explanation_engine.v1.TacticalGoalDefense defense = 5;
  .chesscom.explanation_eng
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04278"></a>
## FND-04278: chesscom.explanation_engine.v1.TacticalGoal.attack_the_king = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.TacticalGoalAttackTheKing attack_the_king = 3;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5625.

```text
alCheckmate checkmate = 1;
  .chesscom.explanation_engine.v1.TacticalGoalPromotion promotion = 2;
  .chesscom.explanation_engine.v1.TacticalGoalAttackTheKing attack_the_king = 3;
  .chesscom.explanation_engine.v1.TacticalGoalWinMaterial win_material = 4;
  .chesscom.explanation_engine.v1.TacticalGoalDefense defense = 5;
  .chesscom.explanation_engine.v1.TacticalGoalPromotionPosition promotion_position = 6;
  .chessco
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04279"></a>
## FND-04279: chesscom.explanation_engine.v1.TacticalGoal.win_material = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.TacticalGoalWinMaterial win_material = 4;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5706.

```text
n promotion = 2;
  .chesscom.explanation_engine.v1.TacticalGoalAttackTheKing attack_the_king = 3;
  .chesscom.explanation_engine.v1.TacticalGoalWinMaterial win_material = 4;
  .chesscom.explanation_engine.v1.TacticalGoalDefense defense = 5;
  .chesscom.explanation_engine.v1.TacticalGoalPromotionPosition promotion_position = 6;
  .chesscom.explanation_engine.v1.TacticalGoalDistantCheckmate distant_checkmate = 7;
  }
 
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04280"></a>
## FND-04280: chesscom.explanation_engine.v1.TacticalGoal.defense = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.TacticalGoalDefense defense = 5;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5782.

```text
 attack_the_king = 3;
  .chesscom.explanation_engine.v1.TacticalGoalWinMaterial win_material = 4;
  .chesscom.explanation_engine.v1.TacticalGoalDefense defense = 5;
  .chesscom.explanation_engine.v1.TacticalGoalPromotionPosition promotion_position = 6;
  .chesscom.explanation_engine.v1.TacticalGoalDistantCheckmate distant_checkmate = 7;
  }
  optional .chesscom.explanation_engine.v1.TacticalGoalType goal_type = 255;

```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04281"></a>
## FND-04281: chesscom.explanation_engine.v1.TacticalGoal.promotion_position = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.TacticalGoalPromotionPosition promotion_position = 6;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5849.

```text
lWinMaterial win_material = 4;
  .chesscom.explanation_engine.v1.TacticalGoalDefense defense = 5;
  .chesscom.explanation_engine.v1.TacticalGoalPromotionPosition promotion_position = 6;
  .chesscom.explanation_engine.v1.TacticalGoalDistantCheckmate distant_checkmate = 7;
  }
  optional .chesscom.explanation_engine.v1.TacticalGoalType goal_type = 255;
}

message StrategicGoal {
  optional .chesscom.explanation_engine.
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04282"></a>
## FND-04282: chesscom.explanation_engine.v1.TacticalGoal.distant_checkmate = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.TacticalGoalDistantCheckmate distant_checkmate = 7;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5937.

```text
ense = 5;
  .chesscom.explanation_engine.v1.TacticalGoalPromotionPosition promotion_position = 6;
  .chesscom.explanation_engine.v1.TacticalGoalDistantCheckmate distant_checkmate = 7;
  }
  optional .chesscom.explanation_engine.v1.TacticalGoalType goal_type = 255;
}

message StrategicGoal {
  optional .chesscom.explanation_engine.v1.StrategicGoalType goal_type = 255;
}

message TacticalGoalCheckmate {
}

message Tact
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04283"></a>
## FND-04283: chesscom.explanation_engine.v1.TacticalGoal.goal_type = 255

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.TacticalGoalType goal_type = 255;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6027.

```text
on = 6;
  .chesscom.explanation_engine.v1.TacticalGoalDistantCheckmate distant_checkmate = 7;
  }
  optional .chesscom.explanation_engine.v1.TacticalGoalType goal_type = 255;
}

message StrategicGoal {
  optional .chesscom.explanation_engine.v1.StrategicGoalType goal_type = 255;
}

message TacticalGoalCheckmate {
}

message TacticalGoalPromotion {
}

message TacticalGoalAttackTheKing {
}

message TacticalGoalDefense 
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04284"></a>
## FND-04284: message declaration: chesscom.explanation_engine.v1.StrategicGoal

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StrategicGoal {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6105.

```text
_checkmate = 7;
  }
  optional .chesscom.explanation_engine.v1.TacticalGoalType goal_type = 255;
}

message StrategicGoal {
  optional .chesscom.explanation_engine.v1.StrategicGoalType goal_type = 255;
}

message TacticalGoalCheckmate {
}

message TacticalGoalPromotion {
}

message TacticalGoalAttackTheKing {
}

message TacticalGoalDefense {
}

message TacticalGoalWinMaterial {
  oneof _won_piece {
  .chesscom.chess.
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04285"></a>
## FND-04285: chesscom.explanation_engine.v1.StrategicGoal.goal_type = 255

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.StrategicGoalType goal_type = 255;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6131.

```text
onal .chesscom.explanation_engine.v1.TacticalGoalType goal_type = 255;
}

message StrategicGoal {
  optional .chesscom.explanation_engine.v1.StrategicGoalType goal_type = 255;
}

message TacticalGoalCheckmate {
}

message TacticalGoalPromotion {
}

message TacticalGoalAttackTheKing {
}

message TacticalGoalDefense {
}

message TacticalGoalWinMaterial {
  oneof _won_piece {
  .chesscom.chess.v1.Piece won_piece = 1;
  
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04286"></a>
## FND-04286: message declaration: chesscom.explanation_engine.v1.TacticalGoalCheckmate

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TacticalGoalCheckmate {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6210.

```text
ge StrategicGoal {
  optional .chesscom.explanation_engine.v1.StrategicGoalType goal_type = 255;
}

message TacticalGoalCheckmate {
}

message TacticalGoalPromotion {
}

message TacticalGoalAttackTheKing {
}

message TacticalGoalDefense {
}

message TacticalGoalWinMaterial {
  oneof _won_piece {
  .chesscom.chess.v1.Piece won_piece = 1;
  }
}

message TacticalGoalPromotionPosition {
}

message TacticalGoalDistantChec
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04287"></a>
## FND-04287: message declaration: chesscom.explanation_engine.v1.TacticalGoalPromotion

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TacticalGoalPromotion {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6245.

```text
scom.explanation_engine.v1.StrategicGoalType goal_type = 255;
}

message TacticalGoalCheckmate {
}

message TacticalGoalPromotion {
}

message TacticalGoalAttackTheKing {
}

message TacticalGoalDefense {
}

message TacticalGoalWinMaterial {
  oneof _won_piece {
  .chesscom.chess.v1.Piece won_piece = 1;
  }
}

message TacticalGoalPromotionPosition {
}

message TacticalGoalDistantCheckmate {
}

message PuzzleThemeMateI
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04288"></a>
## FND-04288: message declaration: chesscom.explanation_engine.v1.TacticalGoalAttackTheKing

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TacticalGoalAttackTheKing {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6280.

```text
cGoalType goal_type = 255;
}

message TacticalGoalCheckmate {
}

message TacticalGoalPromotion {
}

message TacticalGoalAttackTheKing {
}

message TacticalGoalDefense {
}

message TacticalGoalWinMaterial {
  oneof _won_piece {
  .chesscom.chess.v1.Piece won_piece = 1;
  }
}

message TacticalGoalPromotionPosition {
}

message TacticalGoalDistantCheckmate {
}

message PuzzleThemeMateIn1 {
}

message PuzzleThemeMateIn2 
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04289"></a>
## FND-04289: message declaration: chesscom.explanation_engine.v1.TacticalGoalDefense

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TacticalGoalDefense {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6319.

```text
acticalGoalCheckmate {
}

message TacticalGoalPromotion {
}

message TacticalGoalAttackTheKing {
}

message TacticalGoalDefense {
}

message TacticalGoalWinMaterial {
  oneof _won_piece {
  .chesscom.chess.v1.Piece won_piece = 1;
  }
}

message TacticalGoalPromotionPosition {
}

message TacticalGoalDistantCheckmate {
}

message PuzzleThemeMateIn1 {
}

message PuzzleThemeMateIn2 {
}

message PuzzleThemeMateIn3Plus {
}
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04290"></a>
## FND-04290: message declaration: chesscom.explanation_engine.v1.TacticalGoalWinMaterial

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TacticalGoalWinMaterial {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6352.

```text
 TacticalGoalPromotion {
}

message TacticalGoalAttackTheKing {
}

message TacticalGoalDefense {
}

message TacticalGoalWinMaterial {
  oneof _won_piece {
  .chesscom.chess.v1.Piece won_piece = 1;
  }
}

message TacticalGoalPromotionPosition {
}

message TacticalGoalDistantCheckmate {
}

message PuzzleThemeMateIn1 {
}

message PuzzleThemeMateIn2 {
}

message PuzzleThemeMateIn3Plus {
}

message PuzzleThemeScholarsMate
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04291"></a>
## FND-04291: oneof declaration: chesscom.explanation_engine.v1.TacticalGoalWinMaterial._won_piece

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _won_piece {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6388.

```text
TacticalGoalAttackTheKing {
}

message TacticalGoalDefense {
}

message TacticalGoalWinMaterial {
  oneof _won_piece {
  .chesscom.chess.v1.Piece won_piece = 1;
  }
}

message TacticalGoalPromotionPosition {
}

message TacticalGoalDistantCheckmate {
}

message PuzzleThemeMateIn1 {
}

message PuzzleThemeMateIn2 {
}

message PuzzleThemeMateIn3Plus {
}

message PuzzleThemeScholarsMate {
}

message PuzzleThemeEndgameTact
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04292"></a>
## FND-04292: chesscom.explanation_engine.v1.TacticalGoalWinMaterial.won_piece = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Piece won_piece = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6409.

```text
King {
}

message TacticalGoalDefense {
}

message TacticalGoalWinMaterial {
  oneof _won_piece {
  .chesscom.chess.v1.Piece won_piece = 1;
  }
}

message TacticalGoalPromotionPosition {
}

message TacticalGoalDistantCheckmate {
}

message PuzzleThemeMateIn1 {
}

message PuzzleThemeMateIn2 {
}

message PuzzleThemeMateIn3Plus {
}

message PuzzleThemeScholarsMate {
}

message PuzzleThemeEndgameTactics {
}

message Puzz
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04293"></a>
## FND-04293: message declaration: chesscom.explanation_engine.v1.TacticalGoalPromotionPosition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TacticalGoalPromotionPosition {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6456.

```text
age TacticalGoalWinMaterial {
  oneof _won_piece {
  .chesscom.chess.v1.Piece won_piece = 1;
  }
}

message TacticalGoalPromotionPosition {
}

message TacticalGoalDistantCheckmate {
}

message PuzzleThemeMateIn1 {
}

message PuzzleThemeMateIn2 {
}

message PuzzleThemeMateIn3Plus {
}

message PuzzleThemeScholarsMate {
}

message PuzzleThemeEndgameTactics {
}

message PuzzleThemeTrappedPiece {
}

message PuzzleThemeFor
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04294"></a>
## FND-04294: message declaration: chesscom.explanation_engine.v1.TacticalGoalDistantCheckmate

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TacticalGoalDistantCheckmate {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6499.

```text
piece {
  .chesscom.chess.v1.Piece won_piece = 1;
  }
}

message TacticalGoalPromotionPosition {
}

message TacticalGoalDistantCheckmate {
}

message PuzzleThemeMateIn1 {
}

message PuzzleThemeMateIn2 {
}

message PuzzleThemeMateIn3Plus {
}

message PuzzleThemeScholarsMate {
}

message PuzzleThemeEndgameTactics {
}

message PuzzleThemeTrappedPiece {
}

message PuzzleThemeFork {
}

message PuzzleThemeSkewer {
}

messa
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04295"></a>
## FND-04295: message declaration: chesscom.explanation_engine.v1.PuzzleThemeMateIn1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeMateIn1 {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6541.

```text
ce = 1;
  }
}

message TacticalGoalPromotionPosition {
}

message TacticalGoalDistantCheckmate {
}

message PuzzleThemeMateIn1 {
}

message PuzzleThemeMateIn2 {
}

message PuzzleThemeMateIn3Plus {
}

message PuzzleThemeScholarsMate {
}

message PuzzleThemeEndgameTactics {
}

message PuzzleThemeTrappedPiece {
}

message PuzzleThemeFork {
}

message PuzzleThemeSkewer {
}

message PuzzleThemeHangingPiece {
}

message Pu
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04296"></a>
## FND-04296: message declaration: chesscom.explanation_engine.v1.PuzzleThemeMateIn2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeMateIn2 {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6573.

```text
oalPromotionPosition {
}

message TacticalGoalDistantCheckmate {
}

message PuzzleThemeMateIn1 {
}

message PuzzleThemeMateIn2 {
}

message PuzzleThemeMateIn3Plus {
}

message PuzzleThemeScholarsMate {
}

message PuzzleThemeEndgameTactics {
}

message PuzzleThemeTrappedPiece {
}

message PuzzleThemeFork {
}

message PuzzleThemeSkewer {
}

message PuzzleThemeHangingPiece {
}

message PuzzleThemeDiscovery {
}

message 
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04297"></a>
## FND-04297: message declaration: chesscom.explanation_engine.v1.PuzzleThemeMateIn3Plus

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeMateIn3Plus {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6605.

```text
e TacticalGoalDistantCheckmate {
}

message PuzzleThemeMateIn1 {
}

message PuzzleThemeMateIn2 {
}

message PuzzleThemeMateIn3Plus {
}

message PuzzleThemeScholarsMate {
}

message PuzzleThemeEndgameTactics {
}

message PuzzleThemeTrappedPiece {
}

message PuzzleThemeFork {
}

message PuzzleThemeSkewer {
}

message PuzzleThemeHangingPiece {
}

message PuzzleThemeDiscovery {
}

message PuzzleThemeQueenSacrifice {
}

m
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04298"></a>
## FND-04298: message declaration: chesscom.explanation_engine.v1.PuzzleThemeScholarsMate

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeScholarsMate {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6641.

```text
message PuzzleThemeMateIn1 {
}

message PuzzleThemeMateIn2 {
}

message PuzzleThemeMateIn3Plus {
}

message PuzzleThemeScholarsMate {
}

message PuzzleThemeEndgameTactics {
}

message PuzzleThemeTrappedPiece {
}

message PuzzleThemeFork {
}

message PuzzleThemeSkewer {
}

message PuzzleThemeHangingPiece {
}

message PuzzleThemeDiscovery {
}

message PuzzleThemeQueenSacrifice {
}

message PuzzleThemeOpposition {
}

me
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04299"></a>
## FND-04299: message declaration: chesscom.explanation_engine.v1.PuzzleThemeEndgameTactics

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeEndgameTactics {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6678.

```text
ge PuzzleThemeMateIn2 {
}

message PuzzleThemeMateIn3Plus {
}

message PuzzleThemeScholarsMate {
}

message PuzzleThemeEndgameTactics {
}

message PuzzleThemeTrappedPiece {
}

message PuzzleThemeFork {
}

message PuzzleThemeSkewer {
}

message PuzzleThemeHangingPiece {
}

message PuzzleThemeDiscovery {
}

message PuzzleThemeQueenSacrifice {
}

message PuzzleThemeOpposition {
}

message PuzzleThemeMatingNet {
}

messa
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04300"></a>
## FND-04300: message declaration: chesscom.explanation_engine.v1.PuzzleThemeTrappedPiece

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeTrappedPiece {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6717.

```text
leThemeMateIn3Plus {
}

message PuzzleThemeScholarsMate {
}

message PuzzleThemeEndgameTactics {
}

message PuzzleThemeTrappedPiece {
}

message PuzzleThemeFork {
}

message PuzzleThemeSkewer {
}

message PuzzleThemeHangingPiece {
}

message PuzzleThemeDiscovery {
}

message PuzzleThemeQueenSacrifice {
}

message PuzzleThemeOpposition {
}

message PuzzleThemeMatingNet {
}

message PuzzleThemePawnEndgame {
}

message 
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04301"></a>
## FND-04301: message declaration: chesscom.explanation_engine.v1.PuzzleThemeFork

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeFork {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6754.

```text
eThemeScholarsMate {
}

message PuzzleThemeEndgameTactics {
}

message PuzzleThemeTrappedPiece {
}

message PuzzleThemeFork {
}

message PuzzleThemeSkewer {
}

message PuzzleThemeHangingPiece {
}

message PuzzleThemeDiscovery {
}

message PuzzleThemeQueenSacrifice {
}

message PuzzleThemeOpposition {
}

message PuzzleThemeMatingNet {
}

message PuzzleThemePawnEndgame {
}

message PuzzleThemePromotion {
}

message Puz
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04302"></a>
## FND-04302: message declaration: chesscom.explanation_engine.v1.PuzzleThemeSkewer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeSkewer {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6783.

```text
ge PuzzleThemeEndgameTactics {
}

message PuzzleThemeTrappedPiece {
}

message PuzzleThemeFork {
}

message PuzzleThemeSkewer {
}

message PuzzleThemeHangingPiece {
}

message PuzzleThemeDiscovery {
}

message PuzzleThemeQueenSacrifice {
}

message PuzzleThemeOpposition {
}

message PuzzleThemeMatingNet {
}

message PuzzleThemePawnEndgame {
}

message PuzzleThemePromotion {
}

message PuzzleThemeUnderPromotion {
}

m
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04303"></a>
## FND-04303: message declaration: chesscom.explanation_engine.v1.PuzzleThemeHangingPiece

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeHangingPiece {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6814.

```text
}

message PuzzleThemeTrappedPiece {
}

message PuzzleThemeFork {
}

message PuzzleThemeSkewer {
}

message PuzzleThemeHangingPiece {
}

message PuzzleThemeDiscovery {
}

message PuzzleThemeQueenSacrifice {
}

message PuzzleThemeOpposition {
}

message PuzzleThemeMatingNet {
}

message PuzzleThemePawnEndgame {
}

message PuzzleThemePromotion {
}

message PuzzleThemeUnderPromotion {
}

message PuzzleThemeSacrifice {
}
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04304"></a>
## FND-04304: message declaration: chesscom.explanation_engine.v1.PuzzleThemeDiscovery

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeDiscovery {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6851.

```text
}

message PuzzleThemeFork {
}

message PuzzleThemeSkewer {
}

message PuzzleThemeHangingPiece {
}

message PuzzleThemeDiscovery {
}

message PuzzleThemeQueenSacrifice {
}

message PuzzleThemeOpposition {
}

message PuzzleThemeMatingNet {
}

message PuzzleThemePawnEndgame {
}

message PuzzleThemePromotion {
}

message PuzzleThemeUnderPromotion {
}

message PuzzleThemeSacrifice {
}

message PuzzleThemeBackRankMate {
}
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04305"></a>
## FND-04305: message declaration: chesscom.explanation_engine.v1.PuzzleThemeQueenSacrifice

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeQueenSacrifice {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6885.

```text
ssage PuzzleThemeSkewer {
}

message PuzzleThemeHangingPiece {
}

message PuzzleThemeDiscovery {
}

message PuzzleThemeQueenSacrifice {
}

message PuzzleThemeOpposition {
}

message PuzzleThemeMatingNet {
}

message PuzzleThemePawnEndgame {
}

message PuzzleThemePromotion {
}

message PuzzleThemeUnderPromotion {
}

message PuzzleThemeSacrifice {
}

message PuzzleThemeBackRankMate {
}

message PuzzleThemePin {
}

mess
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04306"></a>
## FND-04306: message declaration: chesscom.explanation_engine.v1.PuzzleThemeOpposition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeOpposition {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6924.

```text
zzleThemeHangingPiece {
}

message PuzzleThemeDiscovery {
}

message PuzzleThemeQueenSacrifice {
}

message PuzzleThemeOpposition {
}

message PuzzleThemeMatingNet {
}

message PuzzleThemePawnEndgame {
}

message PuzzleThemePromotion {
}

message PuzzleThemeUnderPromotion {
}

message PuzzleThemeSacrifice {
}

message PuzzleThemeBackRankMate {
}

message PuzzleThemePin {
}

message PuzzleThemeKingSafety {
  oneof _su
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04307"></a>
## FND-04307: message declaration: chesscom.explanation_engine.v1.PuzzleThemeMatingNet

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeMatingNet {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6959.

```text
PuzzleThemeDiscovery {
}

message PuzzleThemeQueenSacrifice {
}

message PuzzleThemeOpposition {
}

message PuzzleThemeMatingNet {
}

message PuzzleThemePawnEndgame {
}

message PuzzleThemePromotion {
}

message PuzzleThemeUnderPromotion {
}

message PuzzleThemeSacrifice {
}

message PuzzleThemeBackRankMate {
}

message PuzzleThemePin {
}

message PuzzleThemeKingSafety {
  oneof _subtheme_weaken {
  .chesscom.explana
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04308"></a>
## FND-04308: message declaration: chesscom.explanation_engine.v1.PuzzleThemePawnEndgame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemePawnEndgame {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 6993.

```text
PuzzleThemeQueenSacrifice {
}

message PuzzleThemeOpposition {
}

message PuzzleThemeMatingNet {
}

message PuzzleThemePawnEndgame {
}

message PuzzleThemePromotion {
}

message PuzzleThemeUnderPromotion {
}

message PuzzleThemeSacrifice {
}

message PuzzleThemeBackRankMate {
}

message PuzzleThemePin {
}

message PuzzleThemeKingSafety {
  oneof _subtheme_weaken {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingS
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04309"></a>
## FND-04309: message declaration: chesscom.explanation_engine.v1.PuzzleThemePromotion

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemePromotion {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7029.

```text
ge PuzzleThemeOpposition {
}

message PuzzleThemeMatingNet {
}

message PuzzleThemePawnEndgame {
}

message PuzzleThemePromotion {
}

message PuzzleThemeUnderPromotion {
}

message PuzzleThemeSacrifice {
}

message PuzzleThemeBackRankMate {
}

message PuzzleThemePin {
}

message PuzzleThemeKingSafety {
  oneof _subtheme_weaken {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken subtheme_weaken = 1;
  }
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04310"></a>
## FND-04310: message declaration: chesscom.explanation_engine.v1.PuzzleThemeUnderPromotion

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeUnderPromotion {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7063.

```text
age PuzzleThemeMatingNet {
}

message PuzzleThemePawnEndgame {
}

message PuzzleThemePromotion {
}

message PuzzleThemeUnderPromotion {
}

message PuzzleThemeSacrifice {
}

message PuzzleThemeBackRankMate {
}

message PuzzleThemePin {
}

message PuzzleThemeKingSafety {
  oneof _subtheme_weaken {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken subtheme_weaken = 1;
  }
  oneof _subtheme_attack {
  .che
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04311"></a>
## FND-04311: message declaration: chesscom.explanation_engine.v1.PuzzleThemeSacrifice

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeSacrifice {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7102.

```text
uzzleThemePawnEndgame {
}

message PuzzleThemePromotion {
}

message PuzzleThemeUnderPromotion {
}

message PuzzleThemeSacrifice {
}

message PuzzleThemeBackRankMate {
}

message PuzzleThemePin {
}

message PuzzleThemeKingSafety {
  oneof _subtheme_weaken {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken subtheme_weaken = 1;
  }
  oneof _subtheme_attack {
  .chesscom.explanation_engine.v1.PuzzleSubth
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04312"></a>
## FND-04312: message declaration: chesscom.explanation_engine.v1.PuzzleThemeBackRankMate

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeBackRankMate {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7136.

```text
 PuzzleThemePromotion {
}

message PuzzleThemeUnderPromotion {
}

message PuzzleThemeSacrifice {
}

message PuzzleThemeBackRankMate {
}

message PuzzleThemePin {
}

message PuzzleThemeKingSafety {
  oneof _subtheme_weaken {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken subtheme_weaken = 1;
  }
  oneof _subtheme_attack {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack subtheme_attac
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04313"></a>
## FND-04313: message declaration: chesscom.explanation_engine.v1.PuzzleThemePin

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemePin {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7173.

```text
zzleThemeUnderPromotion {
}

message PuzzleThemeSacrifice {
}

message PuzzleThemeBackRankMate {
}

message PuzzleThemePin {
}

message PuzzleThemeKingSafety {
  oneof _subtheme_weaken {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken subtheme_weaken = 1;
  }
  oneof _subtheme_attack {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack subtheme_attack = 2;
  }
  oneof _subtheme_defend {
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04314"></a>
## FND-04314: message declaration: chesscom.explanation_engine.v1.PuzzleThemeKingSafety

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeKingSafety {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7201.

```text

message PuzzleThemeSacrifice {
}

message PuzzleThemeBackRankMate {
}

message PuzzleThemePin {
}

message PuzzleThemeKingSafety {
  oneof _subtheme_weaken {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken subtheme_weaken = 1;
  }
  oneof _subtheme_attack {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack subtheme_attack = 2;
  }
  oneof _subtheme_defend {
  .chesscom.explanation_eng
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04315"></a>
## FND-04315: oneof declaration: chesscom.explanation_engine.v1.PuzzleThemeKingSafety._subtheme_weaken

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subtheme_weaken {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7235.

```text

message PuzzleThemeBackRankMate {
}

message PuzzleThemePin {
}

message PuzzleThemeKingSafety {
  oneof _subtheme_weaken {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken subtheme_weaken = 1;
  }
  oneof _subtheme_attack {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack subtheme_attack = 2;
  }
  oneof _subtheme_defend {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyDef
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04316"></a>
## FND-04316: chesscom.explanation_engine.v1.PuzzleThemeKingSafety.subtheme_weaken = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken subtheme_weaken = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7262.

```text
kMate {
}

message PuzzleThemePin {
}

message PuzzleThemeKingSafety {
  oneof _subtheme_weaken {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken subtheme_weaken = 1;
  }
  oneof _subtheme_attack {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack subtheme_attack = 2;
  }
  oneof _subtheme_defend {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyDefend subtheme_defend = 3;
  
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04317"></a>
## FND-04317: oneof declaration: chesscom.explanation_engine.v1.PuzzleThemeKingSafety._subtheme_attack

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subtheme_attack {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7352.

```text
eaken {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken subtheme_weaken = 1;
  }
  oneof _subtheme_attack {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack subtheme_attack = 2;
  }
  oneof _subtheme_defend {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyDefend subtheme_defend = 3;
  }
}

message PuzzleSubthemeKingSafetyWeaken {
}

message PuzzleSubthemeKingSafetyAttack {

```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04318"></a>
## FND-04318: chesscom.explanation_engine.v1.PuzzleThemeKingSafety.subtheme_attack = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack subtheme_attack = 2;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7379.

```text
tion_engine.v1.PuzzleSubthemeKingSafetyWeaken subtheme_weaken = 1;
  }
  oneof _subtheme_attack {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack subtheme_attack = 2;
  }
  oneof _subtheme_defend {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyDefend subtheme_defend = 3;
  }
}

message PuzzleSubthemeKingSafetyWeaken {
}

message PuzzleSubthemeKingSafetyAttack {
}

message PuzzleSubthemeKi
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04319"></a>
## FND-04319: oneof declaration: chesscom.explanation_engine.v1.PuzzleThemeKingSafety._subtheme_defend

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subtheme_defend {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7469.

```text
ttack {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack subtheme_attack = 2;
  }
  oneof _subtheme_defend {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyDefend subtheme_defend = 3;
  }
}

message PuzzleSubthemeKingSafetyWeaken {
}

message PuzzleSubthemeKingSafetyAttack {
}

message PuzzleSubthemeKingSafetyDefend {
}

message PuzzleThemePiecePlay {
  oneof _subtheme_activity {
  .chessco
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04320"></a>
## FND-04320: chesscom.explanation_engine.v1.PuzzleThemeKingSafety.subtheme_defend = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyDefend subtheme_defend = 3;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7496.

```text
tion_engine.v1.PuzzleSubthemeKingSafetyAttack subtheme_attack = 2;
  }
  oneof _subtheme_defend {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyDefend subtheme_defend = 3;
  }
}

message PuzzleSubthemeKingSafetyWeaken {
}

message PuzzleSubthemeKingSafetyAttack {
}

message PuzzleSubthemeKingSafetyDefend {
}

message PuzzleThemePiecePlay {
  oneof _subtheme_activity {
  .chesscom.explanation_engine.v1.Puz
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04321"></a>
## FND-04321: message declaration: chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyWeaken

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleSubthemeKingSafetyWeaken {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7587.

```text
fend {
  .chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyDefend subtheme_defend = 3;
  }
}

message PuzzleSubthemeKingSafetyWeaken {
}

message PuzzleSubthemeKingSafetyAttack {
}

message PuzzleSubthemeKingSafetyDefend {
}

message PuzzleThemePiecePlay {
  oneof _subtheme_activity {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayActivity subtheme_activity = 1;
  }
  oneof _subtheme_prevention {
  .c
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04322"></a>
## FND-04322: message declaration: chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyAttack

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleSubthemeKingSafetyAttack {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7631.

```text
zleSubthemeKingSafetyDefend subtheme_defend = 3;
  }
}

message PuzzleSubthemeKingSafetyWeaken {
}

message PuzzleSubthemeKingSafetyAttack {
}

message PuzzleSubthemeKingSafetyDefend {
}

message PuzzleThemePiecePlay {
  oneof _subtheme_activity {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayActivity subtheme_activity = 1;
  }
  oneof _subtheme_prevention {
  .chesscom.explanation_engine.v1.PuzzleSubtheme
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04323"></a>
## FND-04323: message declaration: chesscom.explanation_engine.v1.PuzzleSubthemeKingSafetyDefend

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleSubthemeKingSafetyDefend {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7675.

```text
= 3;
  }
}

message PuzzleSubthemeKingSafetyWeaken {
}

message PuzzleSubthemeKingSafetyAttack {
}

message PuzzleSubthemeKingSafetyDefend {
}

message PuzzleThemePiecePlay {
  oneof _subtheme_activity {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayActivity subtheme_activity = 1;
  }
  oneof _subtheme_prevention {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayPrevention subtheme_prevention = 2;
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04324"></a>
## FND-04324: message declaration: chesscom.explanation_engine.v1.PuzzleThemePiecePlay

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemePiecePlay {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7719.

```text
Weaken {
}

message PuzzleSubthemeKingSafetyAttack {
}

message PuzzleSubthemeKingSafetyDefend {
}

message PuzzleThemePiecePlay {
  oneof _subtheme_activity {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayActivity subtheme_activity = 1;
  }
  oneof _subtheme_prevention {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayPrevention subtheme_prevention = 2;
  }
  oneof _subtheme_trades {
  .chesscom.
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04325"></a>
## FND-04325: oneof declaration: chesscom.explanation_engine.v1.PuzzleThemePiecePlay._subtheme_activity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subtheme_activity {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7752.

```text
eKingSafetyAttack {
}

message PuzzleSubthemeKingSafetyDefend {
}

message PuzzleThemePiecePlay {
  oneof _subtheme_activity {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayActivity subtheme_activity = 1;
  }
  oneof _subtheme_prevention {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayPrevention subtheme_prevention = 2;
  }
  oneof _subtheme_trades {
  .chesscom.explanation_engine.v1.PuzzleSubth
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04326"></a>
## FND-04326: chesscom.explanation_engine.v1.PuzzleThemePiecePlay.subtheme_activity = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayActivity subtheme_activity = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7781.

```text
e PuzzleSubthemeKingSafetyDefend {
}

message PuzzleThemePiecePlay {
  oneof _subtheme_activity {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayActivity subtheme_activity = 1;
  }
  oneof _subtheme_prevention {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayPrevention subtheme_prevention = 2;
  }
  oneof _subtheme_trades {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayTrades subtheme_t
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04327"></a>
## FND-04327: oneof declaration: chesscom.explanation_engine.v1.PuzzleThemePiecePlay._subtheme_prevention

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subtheme_prevention {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7874.

```text
ty {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayActivity subtheme_activity = 1;
  }
  oneof _subtheme_prevention {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayPrevention subtheme_prevention = 2;
  }
  oneof _subtheme_trades {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayTrades subtheme_trades = 3;
  }
}

message PuzzleSubthemePiecePlayActivity {
}

message PuzzleSubthemePiecePla
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04328"></a>
## FND-04328: chesscom.explanation_engine.v1.PuzzleThemePiecePlay.subtheme_prevention = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayPrevention subtheme_prevention = 2;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 7905.

```text
gine.v1.PuzzleSubthemePiecePlayActivity subtheme_activity = 1;
  }
  oneof _subtheme_prevention {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayPrevention subtheme_prevention = 2;
  }
  oneof _subtheme_trades {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayTrades subtheme_trades = 3;
  }
}

message PuzzleSubthemePiecePlayActivity {
}

message PuzzleSubthemePiecePlayPrevention {
}

message Puzzle
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04329"></a>
## FND-04329: oneof declaration: chesscom.explanation_engine.v1.PuzzleThemePiecePlay._subtheme_trades

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subtheme_trades {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 8002.

```text

  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayPrevention subtheme_prevention = 2;
  }
  oneof _subtheme_trades {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayTrades subtheme_trades = 3;
  }
}

message PuzzleSubthemePiecePlayActivity {
}

message PuzzleSubthemePiecePlayPrevention {
}

message PuzzleSubthemePiecePlayTrades {
}

message PuzzleThemePawnStructure {
  oneof _subtheme_healthy {
  .ch
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04330"></a>
## FND-04330: chesscom.explanation_engine.v1.PuzzleThemePiecePlay.subtheme_trades = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayTrades subtheme_trades = 3;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 8029.

```text
gine.v1.PuzzleSubthemePiecePlayPrevention subtheme_prevention = 2;
  }
  oneof _subtheme_trades {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayTrades subtheme_trades = 3;
  }
}

message PuzzleSubthemePiecePlayActivity {
}

message PuzzleSubthemePiecePlayPrevention {
}

message PuzzleSubthemePiecePlayTrades {
}

message PuzzleThemePawnStructure {
  oneof _subtheme_healthy {
  .chesscom.explanation_engine.v
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04331"></a>
## FND-04331: message declaration: chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayActivity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleSubthemePiecePlayActivity {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 8119.

```text
rades {
  .chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayTrades subtheme_trades = 3;
  }
}

message PuzzleSubthemePiecePlayActivity {
}

message PuzzleSubthemePiecePlayPrevention {
}

message PuzzleSubthemePiecePlayTrades {
}

message PuzzleThemePawnStructure {
  oneof _subtheme_healthy {
  .chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureHealthy subtheme_healthy = 1;
  }
  oneof _subtheme_creates_w
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04332"></a>
## FND-04332: message declaration: chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayPrevention

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleSubthemePiecePlayPrevention {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 8164.

```text
zleSubthemePiecePlayTrades subtheme_trades = 3;
  }
}

message PuzzleSubthemePiecePlayActivity {
}

message PuzzleSubthemePiecePlayPrevention {
}

message PuzzleSubthemePiecePlayTrades {
}

message PuzzleThemePawnStructure {
  oneof _subtheme_healthy {
  .chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureHealthy subtheme_healthy = 1;
  }
  oneof _subtheme_creates_weaknesses {
  .chesscom.explanation_engine.v1
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04333"></a>
## FND-04333: message declaration: chesscom.explanation_engine.v1.PuzzleSubthemePiecePlayTrades

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleSubthemePiecePlayTrades {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 8211.

```text

  }
}

message PuzzleSubthemePiecePlayActivity {
}

message PuzzleSubthemePiecePlayPrevention {
}

message PuzzleSubthemePiecePlayTrades {
}

message PuzzleThemePawnStructure {
  oneof _subtheme_healthy {
  .chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureHealthy subtheme_healthy = 1;
  }
  oneof _subtheme_creates_weaknesses {
  .chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureCreatesWeaknesses s
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04334"></a>
## FND-04334: message declaration: chesscom.explanation_engine.v1.PuzzleThemePawnStructure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemePawnStructure {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 8254.

```text
vity {
}

message PuzzleSubthemePiecePlayPrevention {
}

message PuzzleSubthemePiecePlayTrades {
}

message PuzzleThemePawnStructure {
  oneof _subtheme_healthy {
  .chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureHealthy subtheme_healthy = 1;
  }
  oneof _subtheme_creates_weaknesses {
  .chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureCreatesWeaknesses subtheme_creates_weaknesses = 2;
  }
}

mess
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04335"></a>
## FND-04335: oneof declaration: chesscom.explanation_engine.v1.PuzzleThemePawnStructure._subtheme_healthy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subtheme_healthy {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 8291.

```text
PlayPrevention {
}

message PuzzleSubthemePiecePlayTrades {
}

message PuzzleThemePawnStructure {
  oneof _subtheme_healthy {
  .chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureHealthy subtheme_healthy = 1;
  }
  oneof _subtheme_creates_weaknesses {
  .chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureCreatesWeaknesses subtheme_creates_weaknesses = 2;
  }
}

message PuzzleSubthemePawnStructureHealth
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04336"></a>
## FND-04336: chesscom.explanation_engine.v1.PuzzleThemePawnStructure.subtheme_healthy = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureHealthy subtheme_healthy = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 8319.

```text
PuzzleSubthemePiecePlayTrades {
}

message PuzzleThemePawnStructure {
  oneof _subtheme_healthy {
  .chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureHealthy subtheme_healthy = 1;
  }
  oneof _subtheme_creates_weaknesses {
  .chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureCreatesWeaknesses subtheme_creates_weaknesses = 2;
  }
}

message PuzzleSubthemePawnStructureHealthy {
}

message PuzzleSubthem
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04337"></a>
## FND-04337: oneof declaration: chesscom.explanation_engine.v1.PuzzleThemePawnStructure._subtheme_creates_weaknesses

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subtheme_creates_weaknesses {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 8414.

```text
 {
  .chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureHealthy subtheme_healthy = 1;
  }
  oneof _subtheme_creates_weaknesses {
  .chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureCreatesWeaknesses subtheme_creates_weaknesses = 2;
  }
}

message PuzzleSubthemePawnStructureHealthy {
}

message PuzzleSubthemePawnStructureCreatesWeaknesses {
}

message PuzzleThemeLadderMate {
}

```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04338"></a>
## FND-04338: chesscom.explanation_engine.v1.PuzzleThemePawnStructure.subtheme_creates_weaknesses = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureCreatesWeaknesses subtheme_creates_weaknesses = 2;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 8453.

```text
zzleSubthemePawnStructureHealthy subtheme_healthy = 1;
  }
  oneof _subtheme_creates_weaknesses {
  .chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureCreatesWeaknesses subtheme_creates_weaknesses = 2;
  }
}

message PuzzleSubthemePawnStructureHealthy {
}

message PuzzleSubthemePawnStructureCreatesWeaknesses {
}

message PuzzleThemeLadderMate {
}

```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04339"></a>
## FND-04339: message declaration: chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureHealthy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleSubthemePawnStructureHealthy {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 8570.

```text
tion_engine.v1.PuzzleSubthemePawnStructureCreatesWeaknesses subtheme_creates_weaknesses = 2;
  }
}

message PuzzleSubthemePawnStructureHealthy {
}

message PuzzleSubthemePawnStructureCreatesWeaknesses {
}

message PuzzleThemeLadderMate {
}

```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04340"></a>
## FND-04340: message declaration: chesscom.explanation_engine.v1.PuzzleSubthemePawnStructureCreatesWeaknesses

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleSubthemePawnStructureCreatesWeaknesses {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 8618.

```text
sWeaknesses subtheme_creates_weaknesses = 2;
  }
}

message PuzzleSubthemePawnStructureHealthy {
}

message PuzzleSubthemePawnStructureCreatesWeaknesses {
}

message PuzzleThemeLadderMate {
}

```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04341"></a>
## FND-04341: message declaration: chesscom.explanation_engine.v1.PuzzleThemeLadderMate

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleThemeLadderMate {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 8676.

```text
e PuzzleSubthemePawnStructureHealthy {
}

message PuzzleSubthemePawnStructureCreatesWeaknesses {
}

message PuzzleThemeLadderMate {
}

```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04342"></a>
## FND-04342: message declaration: chesscom.explanation_engine.v1.GamePhaseGlyph

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GamePhaseGlyph {

### Evidence

- **SRC-0422** `research/proto/chesscom/explanation_engine/v1/report_card.proto` — [preserved redacted evidence](../evidence/text/57378977a8fd9985584cb48a5659c7a90b4de18307d70d8ccfa646d7e88e2765.proto)
  Character offset 120.

```text
explanation_engine/v1/report_card.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GamePhaseGlyph {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification glyph = 2;
}

message PlayerReportCard {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.GamePhaseGlyph glyph_by_phase = 2;
  optional 
```

**Source references:** SRC-0422, SRC-1393  
**URL references:** None independently associated  
**Related findings:** FND-04343, FND-04344

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04343"></a>
## FND-04343: chesscom.explanation_engine.v1.GamePhaseGlyph.game_phase = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.GamePhase game_phase = 1;

### Evidence

- **SRC-0422** `research/proto/chesscom/explanation_engine/v1/report_card.proto` — [preserved redacted evidence](../evidence/text/57378977a8fd9985584cb48a5659c7a90b4de18307d70d8ccfa646d7e88e2765.proto)
  Character offset 147.

```text
t_card.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GamePhaseGlyph {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification glyph = 2;
}

message PlayerReportCard {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.GamePhaseGlyph glyph_by_phase = 2;
  optional int32 effective_rating = 3;
```

**Source references:** SRC-0422, SRC-1393  
**URL references:** None independently associated  
**Related findings:** FND-04342, FND-04344

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04344"></a>
## FND-04344: chesscom.explanation_engine.v1.GamePhaseGlyph.glyph = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification glyph = 2;

### Evidence

- **SRC-0422** `research/proto/chesscom/explanation_engine/v1/report_card.proto` — [preserved redacted evidence](../evidence/text/57378977a8fd9985584cb48a5659c7a90b4de18307d70d8ccfa646d7e88e2765.proto)
  Character offset 203.

```text
tion_engine.v1;

message GamePhaseGlyph {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification glyph = 2;
}

message PlayerReportCard {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.GamePhaseGlyph glyph_by_phase = 2;
  optional int32 effective_rating = 3;
}

message ReportCard {
  repeated .chesscom.explanatio
```

**Source references:** SRC-0422, SRC-1393  
**URL references:** None independently associated  
**Related findings:** FND-04342, FND-04343

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04345"></a>
## FND-04345: message declaration: chesscom.explanation_engine.v1.PlayerReportCard

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayerReportCard {

### Evidence

- **SRC-0422** `research/proto/chesscom/explanation_engine/v1/report_card.proto` — [preserved redacted evidence](../evidence/text/57378977a8fd9985584cb48a5659c7a90b4de18307d70d8ccfa646d7e88e2765.proto)
  Character offset 277.

```text
mePhase game_phase = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification glyph = 2;
}

message PlayerReportCard {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.GamePhaseGlyph glyph_by_phase = 2;
  optional int32 effective_rating = 3;
}

message ReportCard {
  repeated .chesscom.explanation_engine.v1.PlayerReportCard report_card_by_color = 1;
  optional string s
```

**Source references:** SRC-0422, SRC-1393  
**URL references:** None independently associated  
**Related findings:** FND-04342, FND-04343, FND-04344

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04346"></a>
## FND-04346: chesscom.explanation_engine.v1.PlayerReportCard.color = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Color color = 1;

### Evidence

- **SRC-0422** `research/proto/chesscom/explanation_engine/v1/report_card.proto` — [preserved redacted evidence](../evidence/text/57378977a8fd9985584cb48a5659c7a90b4de18307d70d8ccfa646d7e88e2765.proto)
  Character offset 306.

```text
ional .chesscom.explanation_engine.v1.MoveClassification glyph = 2;
}

message PlayerReportCard {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.GamePhaseGlyph glyph_by_phase = 2;
  optional int32 effective_rating = 3;
}

message ReportCard {
  repeated .chesscom.explanation_engine.v1.PlayerReportCard report_card_by_color = 1;
  optional string speech = 2;
}

```

**Source references:** SRC-0422, SRC-1393  
**URL references:** None independently associated  
**Related findings:** FND-04342, FND-04343, FND-04344

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04347"></a>
## FND-04347: chesscom.explanation_engine.v1.PlayerReportCard.glyph_by_phase = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GamePhaseGlyph glyph_by_phase = 2;

### Evidence

- **SRC-0422** `research/proto/chesscom/explanation_engine/v1/report_card.proto` — [preserved redacted evidence](../evidence/text/57378977a8fd9985584cb48a5659c7a90b4de18307d70d8ccfa646d7e88e2765.proto)
  Character offset 353.

```text
ification glyph = 2;
}

message PlayerReportCard {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.GamePhaseGlyph glyph_by_phase = 2;
  optional int32 effective_rating = 3;
}

message ReportCard {
  repeated .chesscom.explanation_engine.v1.PlayerReportCard report_card_by_color = 1;
  optional string speech = 2;
}

```

**Source references:** SRC-0422, SRC-1393  
**URL references:** None independently associated  
**Related findings:** FND-04342, FND-04343, FND-04344

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04348"></a>
## FND-04348: chesscom.explanation_engine.v1.PlayerReportCard.effective_rating = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 effective_rating = 3;

### Evidence

- **SRC-0422** `research/proto/chesscom/explanation_engine/v1/report_card.proto` — [preserved redacted evidence](../evidence/text/57378977a8fd9985584cb48a5659c7a90b4de18307d70d8ccfa646d7e88e2765.proto)
  Character offset 431.

```text
v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.GamePhaseGlyph glyph_by_phase = 2;
  optional int32 effective_rating = 3;
}

message ReportCard {
  repeated .chesscom.explanation_engine.v1.PlayerReportCard report_card_by_color = 1;
  optional string speech = 2;
}

```

**Source references:** SRC-0422, SRC-1393  
**URL references:** None independently associated  
**Related findings:** FND-04342, FND-04343, FND-04344

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04349"></a>
## FND-04349: message declaration: chesscom.explanation_engine.v1.ReportCard

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ReportCard {

### Evidence

- **SRC-0422** `research/proto/chesscom/explanation_engine/v1/report_card.proto` — [preserved redacted evidence](../evidence/text/57378977a8fd9985584cb48a5659c7a90b4de18307d70d8ccfa646d7e88e2765.proto)
  Character offset 471.

```text
.explanation_engine.v1.GamePhaseGlyph glyph_by_phase = 2;
  optional int32 effective_rating = 3;
}

message ReportCard {
  repeated .chesscom.explanation_engine.v1.PlayerReportCard report_card_by_color = 1;
  optional string speech = 2;
}

```

**Source references:** SRC-0422, SRC-1393  
**URL references:** None independently associated  
**Related findings:** FND-04342, FND-04343, FND-04344

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04350"></a>
## FND-04350: chesscom.explanation_engine.v1.ReportCard.report_card_by_color = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.PlayerReportCard report_card_by_color = 1;

### Evidence

- **SRC-0422** `research/proto/chesscom/explanation_engine/v1/report_card.proto` — [preserved redacted evidence](../evidence/text/57378977a8fd9985584cb48a5659c7a90b4de18307d70d8ccfa646d7e88e2765.proto)
  Character offset 494.

```text
GamePhaseGlyph glyph_by_phase = 2;
  optional int32 effective_rating = 3;
}

message ReportCard {
  repeated .chesscom.explanation_engine.v1.PlayerReportCard report_card_by_color = 1;
  optional string speech = 2;
}

```

**Source references:** SRC-0422, SRC-1393  
**URL references:** None independently associated  
**Related findings:** FND-04342, FND-04343, FND-04344

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04351"></a>
## FND-04351: chesscom.explanation_engine.v1.ReportCard.speech = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string speech = 2;

### Evidence

- **SRC-0422** `research/proto/chesscom/explanation_engine/v1/report_card.proto` — [preserved redacted evidence](../evidence/text/57378977a8fd9985584cb48a5659c7a90b4de18307d70d8ccfa646d7e88e2765.proto)
  Character offset 580.

```text
eportCard {
  repeated .chesscom.explanation_engine.v1.PlayerReportCard report_card_by_color = 1;
  optional string speech = 2;
}

```

**Source references:** SRC-0422, SRC-1393  
**URL references:** None independently associated  
**Related findings:** FND-04342, FND-04343, FND-04344

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04352"></a>
## FND-04352: enum declaration: chesscom.explanation_engine.v1.SearchPreset

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SearchPreset {

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 115.

```text
scom/explanation_engine/v1/search.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum SearchPreset {
  SEARCH_PRESET_UNSPECIFIED = 0;
  SEARCH_PRESET_PLAY_BOT_STANDARD = 1;
  SEARCH_PRESET_PLAY_BOT_FAST = 2;
  SEARCH_PRESET_GAME_REVIEW_FAST = 3;
  SEARCH_PRESET_GAME_REVIEW_STANDARD = 4;
  SEARCH_PRESET_GAME_REVIEW_DEEP = 5;
  SEARCH_PRESET_GAME_REVIEW_MAXIMUM = 6;
}

enum MultiLineStrategy {
  MULT
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04353"></a>
## FND-04353: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEARCH_PRESET_UNSPECIFIED = 0;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 137.

```text
e/v1/search.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum SearchPreset {
  SEARCH_PRESET_UNSPECIFIED = 0;
  SEARCH_PRESET_PLAY_BOT_STANDARD = 1;
  SEARCH_PRESET_PLAY_BOT_FAST = 2;
  SEARCH_PRESET_GAME_REVIEW_FAST = 3;
  SEARCH_PRESET_GAME_REVIEW_STANDARD = 4;
  SEARCH_PRESET_GAME_REVIEW_DEEP = 5;
  SEARCH_PRESET_GAME_REVIEW_MAXIMUM = 6;
}

enum MultiLineStrategy {
  MULTI_LINE_STRATEGY_UNSPEC
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04354"></a>
## FND-04354: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_PLAY_BOT_STANDARD = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEARCH_PRESET_PLAY_BOT_STANDARD = 1;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 170.

```text
o3

package chesscom.explanation_engine.v1;

enum SearchPreset {
  SEARCH_PRESET_UNSPECIFIED = 0;
  SEARCH_PRESET_PLAY_BOT_STANDARD = 1;
  SEARCH_PRESET_PLAY_BOT_FAST = 2;
  SEARCH_PRESET_GAME_REVIEW_FAST = 3;
  SEARCH_PRESET_GAME_REVIEW_STANDARD = 4;
  SEARCH_PRESET_GAME_REVIEW_DEEP = 5;
  SEARCH_PRESET_GAME_REVIEW_MAXIMUM = 6;
}

enum MultiLineStrategy {
  MULTI_LINE_STRATEGY_UNSPECIFIED = 0;
  MULTI_LINE_STRATEGY_
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04355"></a>
## FND-04355: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_PLAY_BOT_FAST = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEARCH_PRESET_PLAY_BOT_FAST = 2;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 209.

```text
.v1;

enum SearchPreset {
  SEARCH_PRESET_UNSPECIFIED = 0;
  SEARCH_PRESET_PLAY_BOT_STANDARD = 1;
  SEARCH_PRESET_PLAY_BOT_FAST = 2;
  SEARCH_PRESET_GAME_REVIEW_FAST = 3;
  SEARCH_PRESET_GAME_REVIEW_STANDARD = 4;
  SEARCH_PRESET_GAME_REVIEW_DEEP = 5;
  SEARCH_PRESET_GAME_REVIEW_MAXIMUM = 6;
}

enum MultiLineStrategy {
  MULTI_LINE_STRATEGY_UNSPECIFIED = 0;
  MULTI_LINE_STRATEGY_UCI = 1;
  MULTI_LINE_STRATEGY_MULTISEA
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04356"></a>
## FND-04356: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_GAME_REVIEW_FAST = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEARCH_PRESET_GAME_REVIEW_FAST = 3;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 244.

```text
PRESET_UNSPECIFIED = 0;
  SEARCH_PRESET_PLAY_BOT_STANDARD = 1;
  SEARCH_PRESET_PLAY_BOT_FAST = 2;
  SEARCH_PRESET_GAME_REVIEW_FAST = 3;
  SEARCH_PRESET_GAME_REVIEW_STANDARD = 4;
  SEARCH_PRESET_GAME_REVIEW_DEEP = 5;
  SEARCH_PRESET_GAME_REVIEW_MAXIMUM = 6;
}

enum MultiLineStrategy {
  MULTI_LINE_STRATEGY_UNSPECIFIED = 0;
  MULTI_LINE_STRATEGY_UCI = 1;
  MULTI_LINE_STRATEGY_MULTISEARCH = 2;
}

message SearchParameter
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04357"></a>
## FND-04357: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_GAME_REVIEW_STANDARD = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEARCH_PRESET_GAME_REVIEW_STANDARD = 4;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 282.

```text
T_PLAY_BOT_STANDARD = 1;
  SEARCH_PRESET_PLAY_BOT_FAST = 2;
  SEARCH_PRESET_GAME_REVIEW_FAST = 3;
  SEARCH_PRESET_GAME_REVIEW_STANDARD = 4;
  SEARCH_PRESET_GAME_REVIEW_DEEP = 5;
  SEARCH_PRESET_GAME_REVIEW_MAXIMUM = 6;
}

enum MultiLineStrategy {
  MULTI_LINE_STRATEGY_UNSPECIFIED = 0;
  MULTI_LINE_STRATEGY_UCI = 1;
  MULTI_LINE_STRATEGY_MULTISEARCH = 2;
}

message SearchParameters {
  oneof _depth_limit {
  int32 dep
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04358"></a>
## FND-04358: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_GAME_REVIEW_DEEP = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEARCH_PRESET_GAME_REVIEW_DEEP = 5;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 324.

```text
LAY_BOT_FAST = 2;
  SEARCH_PRESET_GAME_REVIEW_FAST = 3;
  SEARCH_PRESET_GAME_REVIEW_STANDARD = 4;
  SEARCH_PRESET_GAME_REVIEW_DEEP = 5;
  SEARCH_PRESET_GAME_REVIEW_MAXIMUM = 6;
}

enum MultiLineStrategy {
  MULTI_LINE_STRATEGY_UNSPECIFIED = 0;
  MULTI_LINE_STRATEGY_UCI = 1;
  MULTI_LINE_STRATEGY_MULTISEARCH = 2;
}

message SearchParameters {
  oneof _depth_limit {
  int32 depth_limit = 1;
  }
  oneof _nodes_limit {
 
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04359"></a>
## FND-04359: chesscom.explanation_engine.v1.SearchPreset.SEARCH_PRESET_GAME_REVIEW_MAXIMUM = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SEARCH_PRESET_GAME_REVIEW_MAXIMUM = 6;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 362.

```text
_REVIEW_FAST = 3;
  SEARCH_PRESET_GAME_REVIEW_STANDARD = 4;
  SEARCH_PRESET_GAME_REVIEW_DEEP = 5;
  SEARCH_PRESET_GAME_REVIEW_MAXIMUM = 6;
}

enum MultiLineStrategy {
  MULTI_LINE_STRATEGY_UNSPECIFIED = 0;
  MULTI_LINE_STRATEGY_UCI = 1;
  MULTI_LINE_STRATEGY_MULTISEARCH = 2;
}

message SearchParameters {
  oneof _depth_limit {
  int32 depth_limit = 1;
  }
  oneof _nodes_limit {
  int32 nodes_limit = 2;
  }
  oneof _t
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04360"></a>
## FND-04360: enum declaration: chesscom.explanation_engine.v1.MultiLineStrategy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MultiLineStrategy {

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 404.

```text
IEW_STANDARD = 4;
  SEARCH_PRESET_GAME_REVIEW_DEEP = 5;
  SEARCH_PRESET_GAME_REVIEW_MAXIMUM = 6;
}

enum MultiLineStrategy {
  MULTI_LINE_STRATEGY_UNSPECIFIED = 0;
  MULTI_LINE_STRATEGY_UCI = 1;
  MULTI_LINE_STRATEGY_MULTISEARCH = 2;
}

message SearchParameters {
  oneof _depth_limit {
  int32 depth_limit = 1;
  }
  oneof _nodes_limit {
  int32 nodes_limit = 2;
  }
  oneof _time_limit_ms {
  int32 time_limit_ms = 3;

```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04361"></a>
## FND-04361: chesscom.explanation_engine.v1.MultiLineStrategy.MULTI_LINE_STRATEGY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MULTI_LINE_STRATEGY_UNSPECIFIED = 0;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 431.

```text
PRESET_GAME_REVIEW_DEEP = 5;
  SEARCH_PRESET_GAME_REVIEW_MAXIMUM = 6;
}

enum MultiLineStrategy {
  MULTI_LINE_STRATEGY_UNSPECIFIED = 0;
  MULTI_LINE_STRATEGY_UCI = 1;
  MULTI_LINE_STRATEGY_MULTISEARCH = 2;
}

message SearchParameters {
  oneof _depth_limit {
  int32 depth_limit = 1;
  }
  oneof _nodes_limit {
  int32 nodes_limit = 2;
  }
  oneof _time_limit_ms {
  int32 time_limit_ms = 3;
  }
  oneof _num_lines {
  
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04362"></a>
## FND-04362: chesscom.explanation_engine.v1.MultiLineStrategy.MULTI_LINE_STRATEGY_UCI = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MULTI_LINE_STRATEGY_UCI = 1;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 470.

```text
RESET_GAME_REVIEW_MAXIMUM = 6;
}

enum MultiLineStrategy {
  MULTI_LINE_STRATEGY_UNSPECIFIED = 0;
  MULTI_LINE_STRATEGY_UCI = 1;
  MULTI_LINE_STRATEGY_MULTISEARCH = 2;
}

message SearchParameters {
  oneof _depth_limit {
  int32 depth_limit = 1;
  }
  oneof _nodes_limit {
  int32 nodes_limit = 2;
  }
  oneof _time_limit_ms {
  int32 time_limit_ms = 3;
  }
  oneof _num_lines {
  int32 num_lines = 4;
  }
  oneof _multi
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04363"></a>
## FND-04363: chesscom.explanation_engine.v1.MultiLineStrategy.MULTI_LINE_STRATEGY_MULTISEARCH = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MULTI_LINE_STRATEGY_MULTISEARCH = 2;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 501.

```text
}

enum MultiLineStrategy {
  MULTI_LINE_STRATEGY_UNSPECIFIED = 0;
  MULTI_LINE_STRATEGY_UCI = 1;
  MULTI_LINE_STRATEGY_MULTISEARCH = 2;
}

message SearchParameters {
  oneof _depth_limit {
  int32 depth_limit = 1;
  }
  oneof _nodes_limit {
  int32 nodes_limit = 2;
  }
  oneof _time_limit_ms {
  int32 time_limit_ms = 3;
  }
  oneof _num_lines {
  int32 num_lines = 4;
  }
  oneof _multi_line_strategy {
  .chesscom.ex
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04364"></a>
## FND-04364: message declaration: chesscom.explanation_engine.v1.SearchParameters

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SearchParameters {

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 541.

```text
_STRATEGY_UNSPECIFIED = 0;
  MULTI_LINE_STRATEGY_UCI = 1;
  MULTI_LINE_STRATEGY_MULTISEARCH = 2;
}

message SearchParameters {
  oneof _depth_limit {
  int32 depth_limit = 1;
  }
  oneof _nodes_limit {
  int32 nodes_limit = 2;
  }
  oneof _time_limit_ms {
  int32 time_limit_ms = 3;
  }
  oneof _num_lines {
  int32 num_lines = 4;
  }
  oneof _multi_line_strategy {
  .chesscom.explanation_engine.v1.MultiLineStrategy mu
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04365"></a>
## FND-04365: oneof declaration: chesscom.explanation_engine.v1.SearchParameters._depth_limit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _depth_limit {

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 570.

```text
MULTI_LINE_STRATEGY_UCI = 1;
  MULTI_LINE_STRATEGY_MULTISEARCH = 2;
}

message SearchParameters {
  oneof _depth_limit {
  int32 depth_limit = 1;
  }
  oneof _nodes_limit {
  int32 nodes_limit = 2;
  }
  oneof _time_limit_ms {
  int32 time_limit_ms = 3;
  }
  oneof _num_lines {
  int32 num_lines = 4;
  }
  oneof _multi_line_strategy {
  .chesscom.explanation_engine.v1.MultiLineStrategy multi_line_strategy = 5;
  }
  
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04366"></a>
## FND-04366: chesscom.explanation_engine.v1.SearchParameters.depth_limit = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 depth_limit = 1;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 593.

```text
 = 1;
  MULTI_LINE_STRATEGY_MULTISEARCH = 2;
}

message SearchParameters {
  oneof _depth_limit {
  int32 depth_limit = 1;
  }
  oneof _nodes_limit {
  int32 nodes_limit = 2;
  }
  oneof _time_limit_ms {
  int32 time_limit_ms = 3;
  }
  oneof _num_lines {
  int32 num_lines = 4;
  }
  oneof _multi_line_strategy {
  .chesscom.explanation_engine.v1.MultiLineStrategy multi_line_strategy = 5;
  }
  oneof _num_threads {
  
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04367"></a>
## FND-04367: oneof declaration: chesscom.explanation_engine.v1.SearchParameters._nodes_limit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _nodes_limit {

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 622.

```text
ULTISEARCH = 2;
}

message SearchParameters {
  oneof _depth_limit {
  int32 depth_limit = 1;
  }
  oneof _nodes_limit {
  int32 nodes_limit = 2;
  }
  oneof _time_limit_ms {
  int32 time_limit_ms = 3;
  }
  oneof _num_lines {
  int32 num_lines = 4;
  }
  oneof _multi_line_strategy {
  .chesscom.explanation_engine.v1.MultiLineStrategy multi_line_strategy = 5;
  }
  oneof _num_threads {
  int32 num_threads = 6;
  }
}

```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04368"></a>
## FND-04368: chesscom.explanation_engine.v1.SearchParameters.nodes_limit = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 nodes_limit = 2;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 645.

```text
age SearchParameters {
  oneof _depth_limit {
  int32 depth_limit = 1;
  }
  oneof _nodes_limit {
  int32 nodes_limit = 2;
  }
  oneof _time_limit_ms {
  int32 time_limit_ms = 3;
  }
  oneof _num_lines {
  int32 num_lines = 4;
  }
  oneof _multi_line_strategy {
  .chesscom.explanation_engine.v1.MultiLineStrategy multi_line_strategy = 5;
  }
  oneof _num_threads {
  int32 num_threads = 6;
  }
}

message GameReviewSear
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04369"></a>
## FND-04369: oneof declaration: chesscom.explanation_engine.v1.SearchParameters._time_limit_ms

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_limit_ms {

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 674.

```text
f _depth_limit {
  int32 depth_limit = 1;
  }
  oneof _nodes_limit {
  int32 nodes_limit = 2;
  }
  oneof _time_limit_ms {
  int32 time_limit_ms = 3;
  }
  oneof _num_lines {
  int32 num_lines = 4;
  }
  oneof _multi_line_strategy {
  .chesscom.explanation_engine.v1.MultiLineStrategy multi_line_strategy = 5;
  }
  oneof _num_threads {
  int32 num_threads = 6;
  }
}

message GameReviewSearchSettings {
  optional .ches
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04370"></a>
## FND-04370: chesscom.explanation_engine.v1.SearchParameters.time_limit_ms = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 time_limit_ms = 3;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 699.

```text
depth_limit = 1;
  }
  oneof _nodes_limit {
  int32 nodes_limit = 2;
  }
  oneof _time_limit_ms {
  int32 time_limit_ms = 3;
  }
  oneof _num_lines {
  int32 num_lines = 4;
  }
  oneof _multi_line_strategy {
  .chesscom.explanation_engine.v1.MultiLineStrategy multi_line_strategy = 5;
  }
  oneof _num_threads {
  int32 num_threads = 6;
  }
}

message GameReviewSearchSettings {
  optional .chesscom.engine.v1.Strength s
```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04371"></a>
## FND-04371: oneof declaration: chesscom.explanation_engine.v1.SearchParameters._num_lines

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _num_lines {

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 730.

```text
odes_limit {
  int32 nodes_limit = 2;
  }
  oneof _time_limit_ms {
  int32 time_limit_ms = 3;
  }
  oneof _num_lines {
  int32 num_lines = 4;
  }
  oneof _multi_line_strategy {
  .chesscom.explanation_engine.v1.MultiLineStrategy multi_line_strategy = 5;
  }
  oneof _num_threads {
  int32 num_threads = 6;
  }
}

message GameReviewSearchSettings {
  optional .chesscom.engine.v1.Strength strength = 1;
}

```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04372"></a>
## FND-04372: chesscom.explanation_engine.v1.SearchParameters.num_lines = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 num_lines = 4;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 751.

```text
nodes_limit = 2;
  }
  oneof _time_limit_ms {
  int32 time_limit_ms = 3;
  }
  oneof _num_lines {
  int32 num_lines = 4;
  }
  oneof _multi_line_strategy {
  .chesscom.explanation_engine.v1.MultiLineStrategy multi_line_strategy = 5;
  }
  oneof _num_threads {
  int32 num_threads = 6;
  }
}

message GameReviewSearchSettings {
  optional .chesscom.engine.v1.Strength strength = 1;
}

```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04373"></a>
## FND-04373: oneof declaration: chesscom.explanation_engine.v1.SearchParameters._multi_line_strategy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _multi_line_strategy {

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 778.

```text
f _time_limit_ms {
  int32 time_limit_ms = 3;
  }
  oneof _num_lines {
  int32 num_lines = 4;
  }
  oneof _multi_line_strategy {
  .chesscom.explanation_engine.v1.MultiLineStrategy multi_line_strategy = 5;
  }
  oneof _num_threads {
  int32 num_threads = 6;
  }
}

message GameReviewSearchSettings {
  optional .chesscom.engine.v1.Strength strength = 1;
}

```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04374"></a>
## FND-04374: chesscom.explanation_engine.v1.SearchParameters.multi_line_strategy = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.MultiLineStrategy multi_line_strategy = 5;

### Evidence

- **SRC-0423** `research/proto/chesscom/explanation_engine/v1/search.proto` — [preserved redacted evidence](../evidence/text/848d0b74e96be353c25f50e0978b520a3bc10553ab7a00640d97745bc2f92c01.proto)
  Character offset 809.

```text
_limit_ms = 3;
  }
  oneof _num_lines {
  int32 num_lines = 4;
  }
  oneof _multi_line_strategy {
  .chesscom.explanation_engine.v1.MultiLineStrategy multi_line_strategy = 5;
  }
  oneof _num_threads {
  int32 num_threads = 6;
  }
}

message GameReviewSearchSettings {
  optional .chesscom.engine.v1.Strength strength = 1;
}

```

**Source references:** SRC-0423, SRC-1394  
**URL references:** None independently associated  
**Related findings:** FND-04352, FND-04353, FND-04354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
