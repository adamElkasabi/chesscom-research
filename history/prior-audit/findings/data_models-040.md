# data_models — findings 3901–4000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-04175"></a>
## FND-04175: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_PROMOTION = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TACTICAL_GOAL_TYPE_PROMOTION = 2;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 462.

```text
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
  STRATEGIC_GOAL_TYPE_UNSPECIFIED = 0;
  STRATEGIC_GOA
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04176"></a>
## FND-04176: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_ATTACK_THE_KING = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TACTICAL_GOAL_TYPE_ATTACK_THE_KING = 3;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 498.

```text
OAL_TYPE_UNSPECIFIED = 0;
  TACTICAL_GOAL_TYPE_CHECKMATE = 1;
  TACTICAL_GOAL_TYPE_PROMOTION = 2;
  TACTICAL_GOAL_TYPE_ATTACK_THE_KING = 3;
  TACTICAL_GOAL_TYPE_WIN_MATERIAL = 4;
  TACTICAL_GOAL_TYPE_DEFENSE = 5;
  TACTICAL_GOAL_TYPE_PROMOTION_POSITION = 6;
  TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE = 7;
}

enum StrategicGoalType {
  STRATEGIC_GOAL_TYPE_UNSPECIFIED = 0;
  STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS = 1;
  STRATEGI
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04177"></a>
## FND-04177: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_WIN_MATERIAL = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TACTICAL_GOAL_TYPE_WIN_MATERIAL = 4;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 540.

```text
TYPE_CHECKMATE = 1;
  TACTICAL_GOAL_TYPE_PROMOTION = 2;
  TACTICAL_GOAL_TYPE_ATTACK_THE_KING = 3;
  TACTICAL_GOAL_TYPE_WIN_MATERIAL = 4;
  TACTICAL_GOAL_TYPE_DEFENSE = 5;
  TACTICAL_GOAL_TYPE_PROMOTION_POSITION = 6;
  TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE = 7;
}

enum StrategicGoalType {
  STRATEGIC_GOAL_TYPE_UNSPECIFIED = 0;
  STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS = 1;
  STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS = 2;
  STRATEGIC_
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04178"></a>
## FND-04178: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_DEFENSE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TACTICAL_GOAL_TYPE_DEFENSE = 5;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 579.

```text
E_PROMOTION = 2;
  TACTICAL_GOAL_TYPE_ATTACK_THE_KING = 3;
  TACTICAL_GOAL_TYPE_WIN_MATERIAL = 4;
  TACTICAL_GOAL_TYPE_DEFENSE = 5;
  TACTICAL_GOAL_TYPE_PROMOTION_POSITION = 6;
  TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE = 7;
}

enum StrategicGoalType {
  STRATEGIC_GOAL_TYPE_UNSPECIFIED = 0;
  STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS = 1;
  STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS = 2;
  STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES = 3;
  STRATE
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04179"></a>
## FND-04179: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_PROMOTION_POSITION = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TACTICAL_GOAL_TYPE_PROMOTION_POSITION = 6;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 613.

```text
YPE_ATTACK_THE_KING = 3;
  TACTICAL_GOAL_TYPE_WIN_MATERIAL = 4;
  TACTICAL_GOAL_TYPE_DEFENSE = 5;
  TACTICAL_GOAL_TYPE_PROMOTION_POSITION = 6;
  TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE = 7;
}

enum StrategicGoalType {
  STRATEGIC_GOAL_TYPE_UNSPECIFIED = 0;
  STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS = 1;
  STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS = 2;
  STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES = 3;
  STRATEGIC_GOAL_TYPE_RESTRICT_PIECES = 4;
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04180"></a>
## FND-04180: chesscom.explanation_engine.v1.TacticalGoalType.TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE = 7;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 658.

```text
_WIN_MATERIAL = 4;
  TACTICAL_GOAL_TYPE_DEFENSE = 5;
  TACTICAL_GOAL_TYPE_PROMOTION_POSITION = 6;
  TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE = 7;
}

enum StrategicGoalType {
  STRATEGIC_GOAL_TYPE_UNSPECIFIED = 0;
  STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS = 1;
  STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS = 2;
  STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES = 3;
  STRATEGIC_GOAL_TYPE_RESTRICT_PIECES = 4;
  STRATEGIC_GOAL_TYPE_TRADE_PIECES = 5;
  ST
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04181"></a>
## FND-04181: enum declaration: chesscom.explanation_engine.v1.StrategicGoalType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum StrategicGoalType {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 703.

```text
SE = 5;
  TACTICAL_GOAL_TYPE_PROMOTION_POSITION = 6;
  TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE = 7;
}

enum StrategicGoalType {
  STRATEGIC_GOAL_TYPE_UNSPECIFIED = 0;
  STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS = 1;
  STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS = 2;
  STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES = 3;
  STRATEGIC_GOAL_TYPE_RESTRICT_PIECES = 4;
  STRATEGIC_GOAL_TYPE_TRADE_PIECES = 5;
  STRATEGIC_GOAL_TYPE_ATTACK_THE_KING = 6;
}

enu
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04182"></a>
## FND-04182: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STRATEGIC_GOAL_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 730.

```text
E_PROMOTION_POSITION = 6;
  TACTICAL_GOAL_TYPE_DISTANT_CHECKMATE = 7;
}

enum StrategicGoalType {
  STRATEGIC_GOAL_TYPE_UNSPECIFIED = 0;
  STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS = 1;
  STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS = 2;
  STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES = 3;
  STRATEGIC_GOAL_TYPE_RESTRICT_PIECES = 4;
  STRATEGIC_GOAL_TYPE_TRADE_PIECES = 5;
  STRATEGIC_GOAL_TYPE_ATTACK_THE_KING = 6;
}

enum PuzzleThemeType {
  PUZZL
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04183"></a>
## FND-04183: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 769.

```text
AL_TYPE_DISTANT_CHECKMATE = 7;
}

enum StrategicGoalType {
  STRATEGIC_GOAL_TYPE_UNSPECIFIED = 0;
  STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS = 1;
  STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS = 2;
  STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES = 3;
  STRATEGIC_GOAL_TYPE_RESTRICT_PIECES = 4;
  STRATEGIC_GOAL_TYPE_TRADE_PIECES = 5;
  STRATEGIC_GOAL_TYPE_ATTACK_THE_KING = 6;
}

enum PuzzleThemeType {
  PUZZLE_THEME_TYPE_UNSPECIFIED = 0;
  PUZZLE_
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04184"></a>
## FND-04184: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS = 2;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 810.

```text
rategicGoalType {
  STRATEGIC_GOAL_TYPE_UNSPECIFIED = 0;
  STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS = 1;
  STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS = 2;
  STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES = 3;
  STRATEGIC_GOAL_TYPE_RESTRICT_PIECES = 4;
  STRATEGIC_GOAL_TYPE_TRADE_PIECES = 5;
  STRATEGIC_GOAL_TYPE_ATTACK_THE_KING = 6;
}

enum PuzzleThemeType {
  PUZZLE_THEME_TYPE_UNSPECIFIED = 0;
  PUZZLE_THEME_TYPE_MATE_IN_1 = 1;
  PUZZLE_THEME_
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04185"></a>
## FND-04185: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES = 3;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 850.

```text
UNSPECIFIED = 0;
  STRATEGIC_GOAL_TYPE_IMPROVE_PAWNS = 1;
  STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS = 2;
  STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES = 3;
  STRATEGIC_GOAL_TYPE_RESTRICT_PIECES = 4;
  STRATEGIC_GOAL_TYPE_TRADE_PIECES = 5;
  STRATEGIC_GOAL_TYPE_ATTACK_THE_KING = 6;
}

enum PuzzleThemeType {
  PUZZLE_THEME_TYPE_UNSPECIFIED = 0;
  PUZZLE_THEME_TYPE_MATE_IN_1 = 1;
  PUZZLE_THEME_TYPE_MATE_IN_2 = 2;
  PUZZLE_THEME_TYPE_
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04186"></a>
## FND-04186: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_RESTRICT_PIECES = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STRATEGIC_GOAL_TYPE_RESTRICT_PIECES = 4;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 893.

```text
OVE_PAWNS = 1;
  STRATEGIC_GOAL_TYPE_WEAKEN_PAWNS = 2;
  STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES = 3;
  STRATEGIC_GOAL_TYPE_RESTRICT_PIECES = 4;
  STRATEGIC_GOAL_TYPE_TRADE_PIECES = 5;
  STRATEGIC_GOAL_TYPE_ATTACK_THE_KING = 6;
}

enum PuzzleThemeType {
  PUZZLE_THEME_TYPE_UNSPECIFIED = 0;
  PUZZLE_THEME_TYPE_MATE_IN_1 = 1;
  PUZZLE_THEME_TYPE_MATE_IN_2 = 2;
  PUZZLE_THEME_TYPE_SCHOLARS_MATE = 3;
  PUZZLE_THEME_TYPE_ENDG
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04187"></a>
## FND-04187: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_TRADE_PIECES = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STRATEGIC_GOAL_TYPE_TRADE_PIECES = 5;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 936.

```text
_PAWNS = 2;
  STRATEGIC_GOAL_TYPE_ACTIVATE_PIECES = 3;
  STRATEGIC_GOAL_TYPE_RESTRICT_PIECES = 4;
  STRATEGIC_GOAL_TYPE_TRADE_PIECES = 5;
  STRATEGIC_GOAL_TYPE_ATTACK_THE_KING = 6;
}

enum PuzzleThemeType {
  PUZZLE_THEME_TYPE_UNSPECIFIED = 0;
  PUZZLE_THEME_TYPE_MATE_IN_1 = 1;
  PUZZLE_THEME_TYPE_MATE_IN_2 = 2;
  PUZZLE_THEME_TYPE_SCHOLARS_MATE = 3;
  PUZZLE_THEME_TYPE_ENDGAME_TACTICS = 4;
  PUZZLE_THEME_TYPE_TRAPPE
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04188"></a>
## FND-04188: chesscom.explanation_engine.v1.StrategicGoalType.STRATEGIC_GOAL_TYPE_ATTACK_THE_KING = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STRATEGIC_GOAL_TYPE_ATTACK_THE_KING = 6;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 976.

```text
TE_PIECES = 3;
  STRATEGIC_GOAL_TYPE_RESTRICT_PIECES = 4;
  STRATEGIC_GOAL_TYPE_TRADE_PIECES = 5;
  STRATEGIC_GOAL_TYPE_ATTACK_THE_KING = 6;
}

enum PuzzleThemeType {
  PUZZLE_THEME_TYPE_UNSPECIFIED = 0;
  PUZZLE_THEME_TYPE_MATE_IN_1 = 1;
  PUZZLE_THEME_TYPE_MATE_IN_2 = 2;
  PUZZLE_THEME_TYPE_SCHOLARS_MATE = 3;
  PUZZLE_THEME_TYPE_ENDGAME_TACTICS = 4;
  PUZZLE_THEME_TYPE_TRAPPED_PIECE = 5;
  PUZZLE_THEME_TYPE_FORK = 
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04189"></a>
## FND-04189: enum declaration: chesscom.explanation_engine.v1.PuzzleThemeType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PuzzleThemeType {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1020.

```text
T_PIECES = 4;
  STRATEGIC_GOAL_TYPE_TRADE_PIECES = 5;
  STRATEGIC_GOAL_TYPE_ATTACK_THE_KING = 6;
}

enum PuzzleThemeType {
  PUZZLE_THEME_TYPE_UNSPECIFIED = 0;
  PUZZLE_THEME_TYPE_MATE_IN_1 = 1;
  PUZZLE_THEME_TYPE_MATE_IN_2 = 2;
  PUZZLE_THEME_TYPE_SCHOLARS_MATE = 3;
  PUZZLE_THEME_TYPE_ENDGAME_TACTICS = 4;
  PUZZLE_THEME_TYPE_TRAPPED_PIECE = 5;
  PUZZLE_THEME_TYPE_FORK = 6;
  PUZZLE_THEME_TYPE_SKEWER = 7;
  PUZZLE_
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04190"></a>
## FND-04190: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1045.

```text
_GOAL_TYPE_TRADE_PIECES = 5;
  STRATEGIC_GOAL_TYPE_ATTACK_THE_KING = 6;
}

enum PuzzleThemeType {
  PUZZLE_THEME_TYPE_UNSPECIFIED = 0;
  PUZZLE_THEME_TYPE_MATE_IN_1 = 1;
  PUZZLE_THEME_TYPE_MATE_IN_2 = 2;
  PUZZLE_THEME_TYPE_SCHOLARS_MATE = 3;
  PUZZLE_THEME_TYPE_ENDGAME_TACTICS = 4;
  PUZZLE_THEME_TYPE_TRAPPED_PIECE = 5;
  PUZZLE_THEME_TYPE_FORK = 6;
  PUZZLE_THEME_TYPE_SKEWER = 7;
  PUZZLE_THEME_TYPE_HANGING_PIECE 
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04191"></a>
## FND-04191: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_MATE_IN_1 = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_MATE_IN_1 = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1082.

```text
GIC_GOAL_TYPE_ATTACK_THE_KING = 6;
}

enum PuzzleThemeType {
  PUZZLE_THEME_TYPE_UNSPECIFIED = 0;
  PUZZLE_THEME_TYPE_MATE_IN_1 = 1;
  PUZZLE_THEME_TYPE_MATE_IN_2 = 2;
  PUZZLE_THEME_TYPE_SCHOLARS_MATE = 3;
  PUZZLE_THEME_TYPE_ENDGAME_TACTICS = 4;
  PUZZLE_THEME_TYPE_TRAPPED_PIECE = 5;
  PUZZLE_THEME_TYPE_FORK = 6;
  PUZZLE_THEME_TYPE_SKEWER = 7;
  PUZZLE_THEME_TYPE_HANGING_PIECE = 8;
  PUZZLE_THEME_TYPE_DISCOVERY = 
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04192"></a>
## FND-04192: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_MATE_IN_2 = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_MATE_IN_2 = 2;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1117.

```text
}

enum PuzzleThemeType {
  PUZZLE_THEME_TYPE_UNSPECIFIED = 0;
  PUZZLE_THEME_TYPE_MATE_IN_1 = 1;
  PUZZLE_THEME_TYPE_MATE_IN_2 = 2;
  PUZZLE_THEME_TYPE_SCHOLARS_MATE = 3;
  PUZZLE_THEME_TYPE_ENDGAME_TACTICS = 4;
  PUZZLE_THEME_TYPE_TRAPPED_PIECE = 5;
  PUZZLE_THEME_TYPE_FORK = 6;
  PUZZLE_THEME_TYPE_SKEWER = 7;
  PUZZLE_THEME_TYPE_HANGING_PIECE = 8;
  PUZZLE_THEME_TYPE_DISCOVERY = 9;
  PUZZLE_THEME_TYPE_QUEEN_SACRIF
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04193"></a>
## FND-04193: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_SCHOLARS_MATE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_SCHOLARS_MATE = 3;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1152.

```text
THEME_TYPE_UNSPECIFIED = 0;
  PUZZLE_THEME_TYPE_MATE_IN_1 = 1;
  PUZZLE_THEME_TYPE_MATE_IN_2 = 2;
  PUZZLE_THEME_TYPE_SCHOLARS_MATE = 3;
  PUZZLE_THEME_TYPE_ENDGAME_TACTICS = 4;
  PUZZLE_THEME_TYPE_TRAPPED_PIECE = 5;
  PUZZLE_THEME_TYPE_FORK = 6;
  PUZZLE_THEME_TYPE_SKEWER = 7;
  PUZZLE_THEME_TYPE_HANGING_PIECE = 8;
  PUZZLE_THEME_TYPE_DISCOVERY = 9;
  PUZZLE_THEME_TYPE_QUEEN_SACRIFICE = 10;
  PUZZLE_THEME_TYPE_OPPOS
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04194"></a>
## FND-04194: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_ENDGAME_TACTICS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_ENDGAME_TACTICS = 4;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1191.

```text
EME_TYPE_MATE_IN_1 = 1;
  PUZZLE_THEME_TYPE_MATE_IN_2 = 2;
  PUZZLE_THEME_TYPE_SCHOLARS_MATE = 3;
  PUZZLE_THEME_TYPE_ENDGAME_TACTICS = 4;
  PUZZLE_THEME_TYPE_TRAPPED_PIECE = 5;
  PUZZLE_THEME_TYPE_FORK = 6;
  PUZZLE_THEME_TYPE_SKEWER = 7;
  PUZZLE_THEME_TYPE_HANGING_PIECE = 8;
  PUZZLE_THEME_TYPE_DISCOVERY = 9;
  PUZZLE_THEME_TYPE_QUEEN_SACRIFICE = 10;
  PUZZLE_THEME_TYPE_OPPOSITION = 11;
  PUZZLE_THEME_TYPE_MATE_IN
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04195"></a>
## FND-04195: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_TRAPPED_PIECE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_TRAPPED_PIECE = 5;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1232.

```text
PE_MATE_IN_2 = 2;
  PUZZLE_THEME_TYPE_SCHOLARS_MATE = 3;
  PUZZLE_THEME_TYPE_ENDGAME_TACTICS = 4;
  PUZZLE_THEME_TYPE_TRAPPED_PIECE = 5;
  PUZZLE_THEME_TYPE_FORK = 6;
  PUZZLE_THEME_TYPE_SKEWER = 7;
  PUZZLE_THEME_TYPE_HANGING_PIECE = 8;
  PUZZLE_THEME_TYPE_DISCOVERY = 9;
  PUZZLE_THEME_TYPE_QUEEN_SACRIFICE = 10;
  PUZZLE_THEME_TYPE_OPPOSITION = 11;
  PUZZLE_THEME_TYPE_MATE_IN_3_PLUS = 12;
  PUZZLE_THEME_TYPE_MATING_
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04196"></a>
## FND-04196: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_FORK = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_FORK = 6;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1271.

```text
CHOLARS_MATE = 3;
  PUZZLE_THEME_TYPE_ENDGAME_TACTICS = 4;
  PUZZLE_THEME_TYPE_TRAPPED_PIECE = 5;
  PUZZLE_THEME_TYPE_FORK = 6;
  PUZZLE_THEME_TYPE_SKEWER = 7;
  PUZZLE_THEME_TYPE_HANGING_PIECE = 8;
  PUZZLE_THEME_TYPE_DISCOVERY = 9;
  PUZZLE_THEME_TYPE_QUEEN_SACRIFICE = 10;
  PUZZLE_THEME_TYPE_OPPOSITION = 11;
  PUZZLE_THEME_TYPE_MATE_IN_3_PLUS = 12;
  PUZZLE_THEME_TYPE_MATING_NET = 13;
  PUZZLE_THEME_TYPE_PAWN_ENDG
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04197"></a>
## FND-04197: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_SKEWER = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_SKEWER = 7;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1301.

```text
ME_TYPE_ENDGAME_TACTICS = 4;
  PUZZLE_THEME_TYPE_TRAPPED_PIECE = 5;
  PUZZLE_THEME_TYPE_FORK = 6;
  PUZZLE_THEME_TYPE_SKEWER = 7;
  PUZZLE_THEME_TYPE_HANGING_PIECE = 8;
  PUZZLE_THEME_TYPE_DISCOVERY = 9;
  PUZZLE_THEME_TYPE_QUEEN_SACRIFICE = 10;
  PUZZLE_THEME_TYPE_OPPOSITION = 11;
  PUZZLE_THEME_TYPE_MATE_IN_3_PLUS = 12;
  PUZZLE_THEME_TYPE_MATING_NET = 13;
  PUZZLE_THEME_TYPE_PAWN_ENDGAME = 14;
  PUZZLE_THEME_TYPE_
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04198"></a>
## FND-04198: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_HANGING_PIECE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_HANGING_PIECE = 8;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1333.

```text
UZZLE_THEME_TYPE_TRAPPED_PIECE = 5;
  PUZZLE_THEME_TYPE_FORK = 6;
  PUZZLE_THEME_TYPE_SKEWER = 7;
  PUZZLE_THEME_TYPE_HANGING_PIECE = 8;
  PUZZLE_THEME_TYPE_DISCOVERY = 9;
  PUZZLE_THEME_TYPE_QUEEN_SACRIFICE = 10;
  PUZZLE_THEME_TYPE_OPPOSITION = 11;
  PUZZLE_THEME_TYPE_MATE_IN_3_PLUS = 12;
  PUZZLE_THEME_TYPE_MATING_NET = 13;
  PUZZLE_THEME_TYPE_PAWN_ENDGAME = 14;
  PUZZLE_THEME_TYPE_PROMOTION = 15;
  PUZZLE_THEME_T
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04199"></a>
## FND-04199: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_DISCOVERY = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_DISCOVERY = 9;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1372.

```text
UZZLE_THEME_TYPE_FORK = 6;
  PUZZLE_THEME_TYPE_SKEWER = 7;
  PUZZLE_THEME_TYPE_HANGING_PIECE = 8;
  PUZZLE_THEME_TYPE_DISCOVERY = 9;
  PUZZLE_THEME_TYPE_QUEEN_SACRIFICE = 10;
  PUZZLE_THEME_TYPE_OPPOSITION = 11;
  PUZZLE_THEME_TYPE_MATE_IN_3_PLUS = 12;
  PUZZLE_THEME_TYPE_MATING_NET = 13;
  PUZZLE_THEME_TYPE_PAWN_ENDGAME = 14;
  PUZZLE_THEME_TYPE_PROMOTION = 15;
  PUZZLE_THEME_TYPE_UNDER_PROMOTION = 16;
  PUZZLE_THEM
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04200"></a>
## FND-04200: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_QUEEN_SACRIFICE = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_QUEEN_SACRIFICE = 10;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1407.

```text
_THEME_TYPE_SKEWER = 7;
  PUZZLE_THEME_TYPE_HANGING_PIECE = 8;
  PUZZLE_THEME_TYPE_DISCOVERY = 9;
  PUZZLE_THEME_TYPE_QUEEN_SACRIFICE = 10;
  PUZZLE_THEME_TYPE_OPPOSITION = 11;
  PUZZLE_THEME_TYPE_MATE_IN_3_PLUS = 12;
  PUZZLE_THEME_TYPE_MATING_NET = 13;
  PUZZLE_THEME_TYPE_PAWN_ENDGAME = 14;
  PUZZLE_THEME_TYPE_PROMOTION = 15;
  PUZZLE_THEME_TYPE_UNDER_PROMOTION = 16;
  PUZZLE_THEME_TYPE_SACRIFICE = 17;
  PUZZLE_THE
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04201"></a>
## FND-04201: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_OPPOSITION = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_OPPOSITION = 11;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1449.

```text
E_HANGING_PIECE = 8;
  PUZZLE_THEME_TYPE_DISCOVERY = 9;
  PUZZLE_THEME_TYPE_QUEEN_SACRIFICE = 10;
  PUZZLE_THEME_TYPE_OPPOSITION = 11;
  PUZZLE_THEME_TYPE_MATE_IN_3_PLUS = 12;
  PUZZLE_THEME_TYPE_MATING_NET = 13;
  PUZZLE_THEME_TYPE_PAWN_ENDGAME = 14;
  PUZZLE_THEME_TYPE_PROMOTION = 15;
  PUZZLE_THEME_TYPE_UNDER_PROMOTION = 16;
  PUZZLE_THEME_TYPE_SACRIFICE = 17;
  PUZZLE_THEME_TYPE_BACK_RANK_MATE = 18;
  PUZZLE_THEM
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04202"></a>
## FND-04202: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_MATE_IN_3_PLUS = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_MATE_IN_3_PLUS = 12;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1486.

```text
YPE_DISCOVERY = 9;
  PUZZLE_THEME_TYPE_QUEEN_SACRIFICE = 10;
  PUZZLE_THEME_TYPE_OPPOSITION = 11;
  PUZZLE_THEME_TYPE_MATE_IN_3_PLUS = 12;
  PUZZLE_THEME_TYPE_MATING_NET = 13;
  PUZZLE_THEME_TYPE_PAWN_ENDGAME = 14;
  PUZZLE_THEME_TYPE_PROMOTION = 15;
  PUZZLE_THEME_TYPE_UNDER_PROMOTION = 16;
  PUZZLE_THEME_TYPE_SACRIFICE = 17;
  PUZZLE_THEME_TYPE_BACK_RANK_MATE = 18;
  PUZZLE_THEME_TYPE_PIN = 19;
  PUZZLE_THEME_TYPE_
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04203"></a>
## FND-04203: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_MATING_NET = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_MATING_NET = 13;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1527.

```text
EEN_SACRIFICE = 10;
  PUZZLE_THEME_TYPE_OPPOSITION = 11;
  PUZZLE_THEME_TYPE_MATE_IN_3_PLUS = 12;
  PUZZLE_THEME_TYPE_MATING_NET = 13;
  PUZZLE_THEME_TYPE_PAWN_ENDGAME = 14;
  PUZZLE_THEME_TYPE_PROMOTION = 15;
  PUZZLE_THEME_TYPE_UNDER_PROMOTION = 16;
  PUZZLE_THEME_TYPE_SACRIFICE = 17;
  PUZZLE_THEME_TYPE_BACK_RANK_MATE = 18;
  PUZZLE_THEME_TYPE_PIN = 19;
  PUZZLE_THEME_TYPE_KING_SAFETY = 20;
  PUZZLE_THEME_TYPE_PIE
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04204"></a>
## FND-04204: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_PAWN_ENDGAME = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_PAWN_ENDGAME = 14;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1564.

```text
PE_OPPOSITION = 11;
  PUZZLE_THEME_TYPE_MATE_IN_3_PLUS = 12;
  PUZZLE_THEME_TYPE_MATING_NET = 13;
  PUZZLE_THEME_TYPE_PAWN_ENDGAME = 14;
  PUZZLE_THEME_TYPE_PROMOTION = 15;
  PUZZLE_THEME_TYPE_UNDER_PROMOTION = 16;
  PUZZLE_THEME_TYPE_SACRIFICE = 17;
  PUZZLE_THEME_TYPE_BACK_RANK_MATE = 18;
  PUZZLE_THEME_TYPE_PIN = 19;
  PUZZLE_THEME_TYPE_KING_SAFETY = 20;
  PUZZLE_THEME_TYPE_PIECE_PLAY = 21;
  PUZZLE_THEME_TYPE_PAW
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04205"></a>
## FND-04205: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_PROMOTION = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_PROMOTION = 15;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1603.

```text
_MATE_IN_3_PLUS = 12;
  PUZZLE_THEME_TYPE_MATING_NET = 13;
  PUZZLE_THEME_TYPE_PAWN_ENDGAME = 14;
  PUZZLE_THEME_TYPE_PROMOTION = 15;
  PUZZLE_THEME_TYPE_UNDER_PROMOTION = 16;
  PUZZLE_THEME_TYPE_SACRIFICE = 17;
  PUZZLE_THEME_TYPE_BACK_RANK_MATE = 18;
  PUZZLE_THEME_TYPE_PIN = 19;
  PUZZLE_THEME_TYPE_KING_SAFETY = 20;
  PUZZLE_THEME_TYPE_PIECE_PLAY = 21;
  PUZZLE_THEME_TYPE_PAWN_STRUCTURE = 22;
  PUZZLE_THEME_TYPE_L
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04206"></a>
## FND-04206: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_UNDER_PROMOTION = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_UNDER_PROMOTION = 16;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1639.

```text
_TYPE_MATING_NET = 13;
  PUZZLE_THEME_TYPE_PAWN_ENDGAME = 14;
  PUZZLE_THEME_TYPE_PROMOTION = 15;
  PUZZLE_THEME_TYPE_UNDER_PROMOTION = 16;
  PUZZLE_THEME_TYPE_SACRIFICE = 17;
  PUZZLE_THEME_TYPE_BACK_RANK_MATE = 18;
  PUZZLE_THEME_TYPE_PIN = 19;
  PUZZLE_THEME_TYPE_KING_SAFETY = 20;
  PUZZLE_THEME_TYPE_PIECE_PLAY = 21;
  PUZZLE_THEME_TYPE_PAWN_STRUCTURE = 22;
  PUZZLE_THEME_TYPE_LADDER_MATE = 23;
}

message PuzzleGe
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04207"></a>
## FND-04207: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_SACRIFICE = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_SACRIFICE = 17;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1681.

```text
_PAWN_ENDGAME = 14;
  PUZZLE_THEME_TYPE_PROMOTION = 15;
  PUZZLE_THEME_TYPE_UNDER_PROMOTION = 16;
  PUZZLE_THEME_TYPE_SACRIFICE = 17;
  PUZZLE_THEME_TYPE_BACK_RANK_MATE = 18;
  PUZZLE_THEME_TYPE_PIN = 19;
  PUZZLE_THEME_TYPE_KING_SAFETY = 20;
  PUZZLE_THEME_TYPE_PIECE_PLAY = 21;
  PUZZLE_THEME_TYPE_PAWN_STRUCTURE = 22;
  PUZZLE_THEME_TYPE_LADDER_MATE = 23;
}

message PuzzleGen {
  oneof _puzzle {
  .chesscom.explanat
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04208"></a>
## FND-04208: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_BACK_RANK_MATE = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_BACK_RANK_MATE = 18;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1717.

```text
YPE_PROMOTION = 15;
  PUZZLE_THEME_TYPE_UNDER_PROMOTION = 16;
  PUZZLE_THEME_TYPE_SACRIFICE = 17;
  PUZZLE_THEME_TYPE_BACK_RANK_MATE = 18;
  PUZZLE_THEME_TYPE_PIN = 19;
  PUZZLE_THEME_TYPE_KING_SAFETY = 20;
  PUZZLE_THEME_TYPE_PIECE_PLAY = 21;
  PUZZLE_THEME_TYPE_PAWN_STRUCTURE = 22;
  PUZZLE_THEME_TYPE_LADDER_MATE = 23;
}

message PuzzleGen {
  oneof _puzzle {
  .chesscom.explanation_engine.v1.Puzzle puzzle = 1;
  }
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04209"></a>
## FND-04209: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_PIN = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_PIN = 19;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1758.

```text
NDER_PROMOTION = 16;
  PUZZLE_THEME_TYPE_SACRIFICE = 17;
  PUZZLE_THEME_TYPE_BACK_RANK_MATE = 18;
  PUZZLE_THEME_TYPE_PIN = 19;
  PUZZLE_THEME_TYPE_KING_SAFETY = 20;
  PUZZLE_THEME_TYPE_PIECE_PLAY = 21;
  PUZZLE_THEME_TYPE_PAWN_STRUCTURE = 22;
  PUZZLE_THEME_TYPE_LADDER_MATE = 23;
}

message PuzzleGen {
  oneof _puzzle {
  .chesscom.explanation_engine.v1.Puzzle puzzle = 1;
  }
  optional .chesscom.explanation_engine.
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04210"></a>
## FND-04210: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_KING_SAFETY = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_KING_SAFETY = 20;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1788.

```text
THEME_TYPE_SACRIFICE = 17;
  PUZZLE_THEME_TYPE_BACK_RANK_MATE = 18;
  PUZZLE_THEME_TYPE_PIN = 19;
  PUZZLE_THEME_TYPE_KING_SAFETY = 20;
  PUZZLE_THEME_TYPE_PIECE_PLAY = 21;
  PUZZLE_THEME_TYPE_PAWN_STRUCTURE = 22;
  PUZZLE_THEME_TYPE_LADDER_MATE = 23;
}

message PuzzleGen {
  oneof _puzzle {
  .chesscom.explanation_engine.v1.Puzzle puzzle = 1;
  }
  optional .chesscom.explanation_engine.v1.GameState puzzle_game_state
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04211"></a>
## FND-04211: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_PIECE_PLAY = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_PIECE_PLAY = 21;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1826.

```text
EME_TYPE_BACK_RANK_MATE = 18;
  PUZZLE_THEME_TYPE_PIN = 19;
  PUZZLE_THEME_TYPE_KING_SAFETY = 20;
  PUZZLE_THEME_TYPE_PIECE_PLAY = 21;
  PUZZLE_THEME_TYPE_PAWN_STRUCTURE = 22;
  PUZZLE_THEME_TYPE_LADDER_MATE = 23;
}

message PuzzleGen {
  oneof _puzzle {
  .chesscom.explanation_engine.v1.Puzzle puzzle = 1;
  }
  optional .chesscom.explanation_engine.v1.GameState puzzle_game_state = 2;
  optional .chesscom.explanation
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04212"></a>
## FND-04212: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_PAWN_STRUCTURE = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_PAWN_STRUCTURE = 22;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1863.

```text
E_THEME_TYPE_PIN = 19;
  PUZZLE_THEME_TYPE_KING_SAFETY = 20;
  PUZZLE_THEME_TYPE_PIECE_PLAY = 21;
  PUZZLE_THEME_TYPE_PAWN_STRUCTURE = 22;
  PUZZLE_THEME_TYPE_LADDER_MATE = 23;
}

message PuzzleGen {
  oneof _puzzle {
  .chesscom.explanation_engine.v1.Puzzle puzzle = 1;
  }
  optional .chesscom.explanation_engine.v1.GameState puzzle_game_state = 2;
  optional .chesscom.explanation_engine.v1.PuzzleGenMode mode = 3;
  
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04213"></a>
## FND-04213: chesscom.explanation_engine.v1.PuzzleThemeType.PUZZLE_THEME_TYPE_LADDER_MATE = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_THEME_TYPE_LADDER_MATE = 23;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1904.

```text
E_KING_SAFETY = 20;
  PUZZLE_THEME_TYPE_PIECE_PLAY = 21;
  PUZZLE_THEME_TYPE_PAWN_STRUCTURE = 22;
  PUZZLE_THEME_TYPE_LADDER_MATE = 23;
}

message PuzzleGen {
  oneof _puzzle {
  .chesscom.explanation_engine.v1.Puzzle puzzle = 1;
  }
  optional .chesscom.explanation_engine.v1.GameState puzzle_game_state = 2;
  optional .chesscom.explanation_engine.v1.PuzzleGenMode mode = 3;
  optional .chesscom.api.v1.SemanticVersion
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04214"></a>
## FND-04214: message declaration: chesscom.explanation_engine.v1.PuzzleGen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleGen {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1943.

```text
_PIECE_PLAY = 21;
  PUZZLE_THEME_TYPE_PAWN_STRUCTURE = 22;
  PUZZLE_THEME_TYPE_LADDER_MATE = 23;
}

message PuzzleGen {
  oneof _puzzle {
  .chesscom.explanation_engine.v1.Puzzle puzzle = 1;
  }
  optional .chesscom.explanation_engine.v1.GameState puzzle_game_state = 2;
  optional .chesscom.explanation_engine.v1.PuzzleGenMode mode = 3;
  optional .chesscom.api.v1.SemanticVersion cee_version = 4;
  optional float puzz
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04215"></a>
## FND-04215: oneof declaration: chesscom.explanation_engine.v1.PuzzleGen._puzzle

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzle {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1965.

```text
ZZLE_THEME_TYPE_PAWN_STRUCTURE = 22;
  PUZZLE_THEME_TYPE_LADDER_MATE = 23;
}

message PuzzleGen {
  oneof _puzzle {
  .chesscom.explanation_engine.v1.Puzzle puzzle = 1;
  }
  optional .chesscom.explanation_engine.v1.GameState puzzle_game_state = 2;
  optional .chesscom.explanation_engine.v1.PuzzleGenMode mode = 3;
  optional .chesscom.api.v1.SemanticVersion cee_version = 4;
  optional float puzzle_quality_score = 5;

```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04216"></a>
## FND-04216: chesscom.explanation_engine.v1.PuzzleGen.puzzle = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.Puzzle puzzle = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 1983.

```text
WN_STRUCTURE = 22;
  PUZZLE_THEME_TYPE_LADDER_MATE = 23;
}

message PuzzleGen {
  oneof _puzzle {
  .chesscom.explanation_engine.v1.Puzzle puzzle = 1;
  }
  optional .chesscom.explanation_engine.v1.GameState puzzle_game_state = 2;
  optional .chesscom.explanation_engine.v1.PuzzleGenMode mode = 3;
  optional .chesscom.api.v1.SemanticVersion cee_version = 4;
  optional float puzzle_quality_score = 5;
}

message Puzzle 
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04217"></a>
## FND-04217: chesscom.explanation_engine.v1.PuzzleGen.puzzle_game_state = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GameState puzzle_game_state = 2;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2040.

```text
}

message PuzzleGen {
  oneof _puzzle {
  .chesscom.explanation_engine.v1.Puzzle puzzle = 1;
  }
  optional .chesscom.explanation_engine.v1.GameState puzzle_game_state = 2;
  optional .chesscom.explanation_engine.v1.PuzzleGenMode mode = 3;
  optional .chesscom.api.v1.SemanticVersion cee_version = 4;
  optional float puzzle_quality_score = 5;
}

message Puzzle {
  oneof _puzzle_goal {
  .chesscom.explanation_engine.v
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04218"></a>
## FND-04218: chesscom.explanation_engine.v1.PuzzleGen.mode = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.PuzzleGenMode mode = 3;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2116.

```text
uzzle puzzle = 1;
  }
  optional .chesscom.explanation_engine.v1.GameState puzzle_game_state = 2;
  optional .chesscom.explanation_engine.v1.PuzzleGenMode mode = 3;
  optional .chesscom.api.v1.SemanticVersion cee_version = 4;
  optional float puzzle_quality_score = 5;
}

message Puzzle {
  oneof _puzzle_goal {
  .chesscom.explanation_engine.v1.PuzzleGoal puzzle_goal = 5;
  }
  oneof _origin_game_metadata {
  .chessco
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04219"></a>
## FND-04219: chesscom.explanation_engine.v1.PuzzleGen.cee_version = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.SemanticVersion cee_version = 4;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2183.

```text
meState puzzle_game_state = 2;
  optional .chesscom.explanation_engine.v1.PuzzleGenMode mode = 3;
  optional .chesscom.api.v1.SemanticVersion cee_version = 4;
  optional float puzzle_quality_score = 5;
}

message Puzzle {
  oneof _puzzle_goal {
  .chesscom.explanation_engine.v1.PuzzleGoal puzzle_goal = 5;
  }
  oneof _origin_game_metadata {
  .chesscom.chess.v1.GameMetadata origin_game_metadata = 7;
  }
  oneof _orig
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04220"></a>
## FND-04220: chesscom.explanation_engine.v1.PuzzleGen.puzzle_quality_score = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float puzzle_quality_score = 5;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2244.

```text
on_engine.v1.PuzzleGenMode mode = 3;
  optional .chesscom.api.v1.SemanticVersion cee_version = 4;
  optional float puzzle_quality_score = 5;
}

message Puzzle {
  oneof _puzzle_goal {
  .chesscom.explanation_engine.v1.PuzzleGoal puzzle_goal = 5;
  }
  oneof _origin_game_metadata {
  .chesscom.chess.v1.GameMetadata origin_game_metadata = 7;
  }
  oneof _origin_game_ply {
  int32 origin_game_ply = 11;
  }
  optional st
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04221"></a>
## FND-04221: message declaration: chesscom.explanation_engine.v1.Puzzle

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Puzzle {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2288.

```text
nal .chesscom.api.v1.SemanticVersion cee_version = 4;
  optional float puzzle_quality_score = 5;
}

message Puzzle {
  oneof _puzzle_goal {
  .chesscom.explanation_engine.v1.PuzzleGoal puzzle_goal = 5;
  }
  oneof _origin_game_metadata {
  .chesscom.chess.v1.GameMetadata origin_game_metadata = 7;
  }
  oneof _origin_game_ply {
  int32 origin_game_ply = 11;
  }
  optional string annotated_puzzle_pgn = 1;
  optional st
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04222"></a>
## FND-04222: oneof declaration: chesscom.explanation_engine.v1.Puzzle._puzzle_goal

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzle_goal {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2307.

```text
1.SemanticVersion cee_version = 4;
  optional float puzzle_quality_score = 5;
}

message Puzzle {
  oneof _puzzle_goal {
  .chesscom.explanation_engine.v1.PuzzleGoal puzzle_goal = 5;
  }
  oneof _origin_game_metadata {
  .chesscom.chess.v1.GameMetadata origin_game_metadata = 7;
  }
  oneof _origin_game_ply {
  int32 origin_game_ply = 11;
  }
  optional string annotated_puzzle_pgn = 1;
  optional string initial_fen = 
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04223"></a>
## FND-04223: chesscom.explanation_engine.v1.Puzzle.puzzle_goal = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleGoal puzzle_goal = 5;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2330.

```text
ersion = 4;
  optional float puzzle_quality_score = 5;
}

message Puzzle {
  oneof _puzzle_goal {
  .chesscom.explanation_engine.v1.PuzzleGoal puzzle_goal = 5;
  }
  oneof _origin_game_metadata {
  .chesscom.chess.v1.GameMetadata origin_game_metadata = 7;
  }
  oneof _origin_game_ply {
  int32 origin_game_ply = 11;
  }
  optional string annotated_puzzle_pgn = 1;
  optional string initial_fen = 2;
  repeated .chesscom
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04224"></a>
## FND-04224: oneof declaration: chesscom.explanation_engine.v1.Puzzle._origin_game_metadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _origin_game_metadata {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2396.

```text
Puzzle {
  oneof _puzzle_goal {
  .chesscom.explanation_engine.v1.PuzzleGoal puzzle_goal = 5;
  }
  oneof _origin_game_metadata {
  .chesscom.chess.v1.GameMetadata origin_game_metadata = 7;
  }
  oneof _origin_game_ply {
  int32 origin_game_ply = 11;
  }
  optional string annotated_puzzle_pgn = 1;
  optional string initial_fen = 2;
  repeated .chesscom.explanation_engine.v1.PuzzleMove puzzle_moves = 3;
  repeated .ch
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04225"></a>
## FND-04225: chesscom.explanation_engine.v1.Puzzle.origin_game_metadata = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.GameMetadata origin_game_metadata = 7;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2428.

```text
  .chesscom.explanation_engine.v1.PuzzleGoal puzzle_goal = 5;
  }
  oneof _origin_game_metadata {
  .chesscom.chess.v1.GameMetadata origin_game_metadata = 7;
  }
  oneof _origin_game_ply {
  int32 origin_game_ply = 11;
  }
  optional string annotated_puzzle_pgn = 1;
  optional string initial_fen = 2;
  repeated .chesscom.explanation_engine.v1.PuzzleMove puzzle_moves = 3;
  repeated .chesscom.explanation_engine.v1.Puz
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04226"></a>
## FND-04226: oneof declaration: chesscom.explanation_engine.v1.Puzzle._origin_game_ply

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _origin_game_ply {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2492.

```text
}
  oneof _origin_game_metadata {
  .chesscom.chess.v1.GameMetadata origin_game_metadata = 7;
  }
  oneof _origin_game_ply {
  int32 origin_game_ply = 11;
  }
  optional string annotated_puzzle_pgn = 1;
  optional string initial_fen = 2;
  repeated .chesscom.explanation_engine.v1.PuzzleMove puzzle_moves = 3;
  repeated .chesscom.explanation_engine.v1.PuzzleTheme puzzle_themes = 4;
  optional .chesscom.chess.v1.GamePh
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04227"></a>
## FND-04227: chesscom.explanation_engine.v1.Puzzle.origin_game_ply = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 origin_game_ply = 11;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2519.

```text
data {
  .chesscom.chess.v1.GameMetadata origin_game_metadata = 7;
  }
  oneof _origin_game_ply {
  int32 origin_game_ply = 11;
  }
  optional string annotated_puzzle_pgn = 1;
  optional string initial_fen = 2;
  repeated .chesscom.explanation_engine.v1.PuzzleMove puzzle_moves = 3;
  repeated .chesscom.explanation_engine.v1.PuzzleTheme puzzle_themes = 4;
  optional .chesscom.chess.v1.GamePhase game_phase = 6;
  repea
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04228"></a>
## FND-04228: chesscom.explanation_engine.v1.Puzzle.annotated_puzzle_pgn = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string annotated_puzzle_pgn = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2553.

```text
tadata origin_game_metadata = 7;
  }
  oneof _origin_game_ply {
  int32 origin_game_ply = 11;
  }
  optional string annotated_puzzle_pgn = 1;
  optional string initial_fen = 2;
  repeated .chesscom.explanation_engine.v1.PuzzleMove puzzle_moves = 3;
  repeated .chesscom.explanation_engine.v1.PuzzleTheme puzzle_themes = 4;
  optional .chesscom.chess.v1.GamePhase game_phase = 6;
  repeated .chesscom.explanation_engine.v
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04229"></a>
## FND-04229: chesscom.explanation_engine.v1.Puzzle.initial_fen = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string initial_fen = 2;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2597.

```text
 _origin_game_ply {
  int32 origin_game_ply = 11;
  }
  optional string annotated_puzzle_pgn = 1;
  optional string initial_fen = 2;
  repeated .chesscom.explanation_engine.v1.PuzzleMove puzzle_moves = 3;
  repeated .chesscom.explanation_engine.v1.PuzzleTheme puzzle_themes = 4;
  optional .chesscom.chess.v1.GamePhase game_phase = 6;
  repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_goal_speech = 8;
  
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04230"></a>
## FND-04230: chesscom.explanation_engine.v1.Puzzle.puzzle_moves = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.PuzzleMove puzzle_moves = 3;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2632.

```text
game_ply = 11;
  }
  optional string annotated_puzzle_pgn = 1;
  optional string initial_fen = 2;
  repeated .chesscom.explanation_engine.v1.PuzzleMove puzzle_moves = 3;
  repeated .chesscom.explanation_engine.v1.PuzzleTheme puzzle_themes = 4;
  optional .chesscom.chess.v1.GamePhase game_phase = 6;
  repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_goal_speech = 8;
  optional .chesscom.chess.v1.Positio
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04231"></a>
## FND-04231: chesscom.explanation_engine.v1.Puzzle.puzzle_themes = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.PuzzleTheme puzzle_themes = 4;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2704.

```text
l string initial_fen = 2;
  repeated .chesscom.explanation_engine.v1.PuzzleMove puzzle_moves = 3;
  repeated .chesscom.explanation_engine.v1.PuzzleTheme puzzle_themes = 4;
  optional .chesscom.chess.v1.GamePhase game_phase = 6;
  repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_goal_speech = 8;
  optional .chesscom.chess.v1.Position initial_position = 9;
  optional .chesscom.explanation_engine.v1.Puzzl
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04232"></a>
## FND-04232: chesscom.explanation_engine.v1.Puzzle.game_phase = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.GamePhase game_phase = 6;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2778.

```text
eMove puzzle_moves = 3;
  repeated .chesscom.explanation_engine.v1.PuzzleTheme puzzle_themes = 4;
  optional .chesscom.chess.v1.GamePhase game_phase = 6;
  repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_goal_speech = 8;
  optional .chesscom.chess.v1.Position initial_position = 9;
  optional .chesscom.explanation_engine.v1.PuzzleResult puzzle_result = 10;
}

message PuzzleMove {
  optional .chesscom.c
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04233"></a>
## FND-04233: chesscom.explanation_engine.v1.Puzzle.puzzle_goal_speech = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_goal_speech = 8;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2834.

```text
_engine.v1.PuzzleTheme puzzle_themes = 4;
  optional .chesscom.chess.v1.GamePhase game_phase = 6;
  repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_goal_speech = 8;
  optional .chesscom.chess.v1.Position initial_position = 9;
  optional .chesscom.explanation_engine.v1.PuzzleResult puzzle_result = 10;
}

message PuzzleMove {
  optional .chesscom.chess.v1.Move move = 1;
  optional .chesscom.explanation_
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04234"></a>
## FND-04234: chesscom.explanation_engine.v1.Puzzle.initial_position = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Position initial_position = 9;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2917.

```text
ame_phase = 6;
  repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_goal_speech = 8;
  optional .chesscom.chess.v1.Position initial_position = 9;
  optional .chesscom.explanation_engine.v1.PuzzleResult puzzle_result = 10;
}

message PuzzleMove {
  optional .chesscom.chess.v1.Move move = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification classification = 2;
  repeated .chesscom.explanation_e
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04235"></a>
## FND-04235: chesscom.explanation_engine.v1.Puzzle.puzzle_result = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.PuzzleResult puzzle_result = 10;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 2978.

```text
echForLocale puzzle_goal_speech = 8;
  optional .chesscom.chess.v1.Position initial_position = 9;
  optional .chesscom.explanation_engine.v1.PuzzleResult puzzle_result = 10;
}

message PuzzleMove {
  optional .chesscom.chess.v1.Move move = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification classification = 2;
  repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_hint_speech = 3;
  optional i
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04236"></a>
## FND-04236: message declaration: chesscom.explanation_engine.v1.PuzzleMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleMove {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3055.

```text
nitial_position = 9;
  optional .chesscom.explanation_engine.v1.PuzzleResult puzzle_result = 10;
}

message PuzzleMove {
  optional .chesscom.chess.v1.Move move = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification classification = 2;
  repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_hint_speech = 3;
  optional int32 legal_alternate_moves = 4;
}

message PuzzleResult {
  oneof result {
  
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04237"></a>
## FND-04237: chesscom.explanation_engine.v1.PuzzleMove.move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move move = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3078.

```text
optional .chesscom.explanation_engine.v1.PuzzleResult puzzle_result = 10;
}

message PuzzleMove {
  optional .chesscom.chess.v1.Move move = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification classification = 2;
  repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_hint_speech = 3;
  optional int32 legal_alternate_moves = 4;
}

message PuzzleResult {
  oneof result {
  .chesscom.explanation_e
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04238"></a>
## FND-04238: chesscom.explanation_engine.v1.PuzzleMove.classification = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification classification = 2;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3123.

```text
leResult puzzle_result = 10;
}

message PuzzleMove {
  optional .chesscom.chess.v1.Move move = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification classification = 2;
  repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_hint_speech = 3;
  optional int32 legal_alternate_moves = 4;
}

message PuzzleResult {
  oneof result {
  .chesscom.explanation_engine.v1.PuzzleWinningResult winning_result =
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04239"></a>
## FND-04239: chesscom.explanation_engine.v1.PuzzleMove.puzzle_hint_speech = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_hint_speech = 3;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3205.

```text
.Move move = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification classification = 2;
  repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_hint_speech = 3;
  optional int32 legal_alternate_moves = 4;
}

message PuzzleResult {
  oneof result {
  .chesscom.explanation_engine.v1.PuzzleWinningResult winning_result = 1;
  }
}

message PuzzleGoal {
  oneof goal_type {
  .chesscom.explanation_engine
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04240"></a>
## FND-04240: chesscom.explanation_engine.v1.PuzzleMove.legal_alternate_moves = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 legal_alternate_moves = 4;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3288.

```text
ification = 2;
  repeated .chesscom.explanation_engine.v1.SpeechForLocale puzzle_hint_speech = 3;
  optional int32 legal_alternate_moves = 4;
}

message PuzzleResult {
  oneof result {
  .chesscom.explanation_engine.v1.PuzzleWinningResult winning_result = 1;
  }
}

message PuzzleGoal {
  oneof goal_type {
  .chesscom.explanation_engine.v1.TacticalGoal tactical_goal = 1;
  .chesscom.explanation_engine.v1.StrategicGoal
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04241"></a>
## FND-04241: message declaration: chesscom.explanation_engine.v1.PuzzleResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleResult {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3333.

```text
on_engine.v1.SpeechForLocale puzzle_hint_speech = 3;
  optional int32 legal_alternate_moves = 4;
}

message PuzzleResult {
  oneof result {
  .chesscom.explanation_engine.v1.PuzzleWinningResult winning_result = 1;
  }
}

message PuzzleGoal {
  oneof goal_type {
  .chesscom.explanation_engine.v1.TacticalGoal tactical_goal = 1;
  .chesscom.explanation_engine.v1.StrategicGoal strategic_goal = 2;
  }
}

message PuzzleThe
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04242"></a>
## FND-04242: oneof declaration: chesscom.explanation_engine.v1.PuzzleResult.result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof result {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3358.

```text
ale puzzle_hint_speech = 3;
  optional int32 legal_alternate_moves = 4;
}

message PuzzleResult {
  oneof result {
  .chesscom.explanation_engine.v1.PuzzleWinningResult winning_result = 1;
  }
}

message PuzzleGoal {
  oneof goal_type {
  .chesscom.explanation_engine.v1.TacticalGoal tactical_goal = 1;
  .chesscom.explanation_engine.v1.StrategicGoal strategic_goal = 2;
  }
}

message PuzzleTheme {
  oneof theme {
  .c
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04243"></a>
## FND-04243: chesscom.explanation_engine.v1.PuzzleResult.winning_result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleWinningResult winning_result = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3375.

```text
peech = 3;
  optional int32 legal_alternate_moves = 4;
}

message PuzzleResult {
  oneof result {
  .chesscom.explanation_engine.v1.PuzzleWinningResult winning_result = 1;
  }
}

message PuzzleGoal {
  oneof goal_type {
  .chesscom.explanation_engine.v1.TacticalGoal tactical_goal = 1;
  .chesscom.explanation_engine.v1.StrategicGoal strategic_goal = 2;
  }
}

message PuzzleTheme {
  oneof theme {
  .chesscom.explanati
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04244"></a>
## FND-04244: message declaration: chesscom.explanation_engine.v1.PuzzleGoal

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleGoal {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3454.

```text
{
  oneof result {
  .chesscom.explanation_engine.v1.PuzzleWinningResult winning_result = 1;
  }
}

message PuzzleGoal {
  oneof goal_type {
  .chesscom.explanation_engine.v1.TacticalGoal tactical_goal = 1;
  .chesscom.explanation_engine.v1.StrategicGoal strategic_goal = 2;
  }
}

message PuzzleTheme {
  oneof theme {
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn1 mate_in_1 = 1;
  .chesscom.explanation_engine.v
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04245"></a>
## FND-04245: oneof declaration: chesscom.explanation_engine.v1.PuzzleGoal.goal_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof goal_type {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3477.

```text
hesscom.explanation_engine.v1.PuzzleWinningResult winning_result = 1;
  }
}

message PuzzleGoal {
  oneof goal_type {
  .chesscom.explanation_engine.v1.TacticalGoal tactical_goal = 1;
  .chesscom.explanation_engine.v1.StrategicGoal strategic_goal = 2;
  }
}

message PuzzleTheme {
  oneof theme {
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn1 mate_in_1 = 1;
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn2 ma
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04246"></a>
## FND-04246: chesscom.explanation_engine.v1.PuzzleGoal.tactical_goal = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.TacticalGoal tactical_goal = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3497.

```text
engine.v1.PuzzleWinningResult winning_result = 1;
  }
}

message PuzzleGoal {
  oneof goal_type {
  .chesscom.explanation_engine.v1.TacticalGoal tactical_goal = 1;
  .chesscom.explanation_engine.v1.StrategicGoal strategic_goal = 2;
  }
}

message PuzzleTheme {
  oneof theme {
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn1 mate_in_1 = 1;
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn2 mate_in_2 = 2;
  .ches
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04247"></a>
## FND-04247: chesscom.explanation_engine.v1.PuzzleGoal.strategic_goal = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.StrategicGoal strategic_goal = 2;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3563.

```text
uzzleGoal {
  oneof goal_type {
  .chesscom.explanation_engine.v1.TacticalGoal tactical_goal = 1;
  .chesscom.explanation_engine.v1.StrategicGoal strategic_goal = 2;
  }
}

message PuzzleTheme {
  oneof theme {
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn1 mate_in_1 = 1;
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn2 mate_in_2 = 2;
  .chesscom.explanation_engine.v1.PuzzleThemeScholarsMate scholars_mate =
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04248"></a>
## FND-04248: message declaration: chesscom.explanation_engine.v1.PuzzleTheme

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleTheme {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3636.

```text
lGoal tactical_goal = 1;
  .chesscom.explanation_engine.v1.StrategicGoal strategic_goal = 2;
  }
}

message PuzzleTheme {
  oneof theme {
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn1 mate_in_1 = 1;
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn2 mate_in_2 = 2;
  .chesscom.explanation_engine.v1.PuzzleThemeScholarsMate scholars_mate = 3;
  .chesscom.explanation_engine.v1.PuzzleThemeEndgameTactics endgame_t
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04249"></a>
## FND-04249: oneof declaration: chesscom.explanation_engine.v1.PuzzleTheme.theme

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof theme {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3660.

```text

  .chesscom.explanation_engine.v1.StrategicGoal strategic_goal = 2;
  }
}

message PuzzleTheme {
  oneof theme {
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn1 mate_in_1 = 1;
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn2 mate_in_2 = 2;
  .chesscom.explanation_engine.v1.PuzzleThemeScholarsMate scholars_mate = 3;
  .chesscom.explanation_engine.v1.PuzzleThemeEndgameTactics endgame_tactics = 4;
  .chesscom.
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04250"></a>
## FND-04250: chesscom.explanation_engine.v1.PuzzleTheme.mate_in_1 = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeMateIn1 mate_in_1 = 1;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3676.

```text
lanation_engine.v1.StrategicGoal strategic_goal = 2;
  }
}

message PuzzleTheme {
  oneof theme {
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn1 mate_in_1 = 1;
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn2 mate_in_2 = 2;
  .chesscom.explanation_engine.v1.PuzzleThemeScholarsMate scholars_mate = 3;
  .chesscom.explanation_engine.v1.PuzzleThemeEndgameTactics endgame_tactics = 4;
  .chesscom.explanation_engi
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04251"></a>
## FND-04251: chesscom.explanation_engine.v1.PuzzleTheme.mate_in_2 = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeMateIn2 mate_in_2 = 2;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3744.

```text
PuzzleTheme {
  oneof theme {
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn1 mate_in_1 = 1;
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn2 mate_in_2 = 2;
  .chesscom.explanation_engine.v1.PuzzleThemeScholarsMate scholars_mate = 3;
  .chesscom.explanation_engine.v1.PuzzleThemeEndgameTactics endgame_tactics = 4;
  .chesscom.explanation_engine.v1.PuzzleThemeTrappedPiece trapped_piece = 5;
  .chesscom.explana
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04252"></a>
## FND-04252: chesscom.explanation_engine.v1.PuzzleTheme.scholars_mate = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeScholarsMate scholars_mate = 3;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3812.

```text
leThemeMateIn1 mate_in_1 = 1;
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn2 mate_in_2 = 2;
  .chesscom.explanation_engine.v1.PuzzleThemeScholarsMate scholars_mate = 3;
  .chesscom.explanation_engine.v1.PuzzleThemeEndgameTactics endgame_tactics = 4;
  .chesscom.explanation_engine.v1.PuzzleThemeTrappedPiece trapped_piece = 5;
  .chesscom.explanation_engine.v1.PuzzleThemeFork fork = 6;
  .chesscom.explanation_eng
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04253"></a>
## FND-04253: chesscom.explanation_engine.v1.PuzzleTheme.endgame_tactics = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeEndgameTactics endgame_tactics = 4;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3889.

```text
teIn2 mate_in_2 = 2;
  .chesscom.explanation_engine.v1.PuzzleThemeScholarsMate scholars_mate = 3;
  .chesscom.explanation_engine.v1.PuzzleThemeEndgameTactics endgame_tactics = 4;
  .chesscom.explanation_engine.v1.PuzzleThemeTrappedPiece trapped_piece = 5;
  .chesscom.explanation_engine.v1.PuzzleThemeFork fork = 6;
  .chesscom.explanation_engine.v1.PuzzleThemeSkewer skewer = 7;
  .chesscom.explanation_engine.v1.Puzzle
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04254"></a>
## FND-04254: chesscom.explanation_engine.v1.PuzzleTheme.trapped_piece = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeTrappedPiece trapped_piece = 5;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 3970.

```text
holars_mate = 3;
  .chesscom.explanation_engine.v1.PuzzleThemeEndgameTactics endgame_tactics = 4;
  .chesscom.explanation_engine.v1.PuzzleThemeTrappedPiece trapped_piece = 5;
  .chesscom.explanation_engine.v1.PuzzleThemeFork fork = 6;
  .chesscom.explanation_engine.v1.PuzzleThemeSkewer skewer = 7;
  .chesscom.explanation_engine.v1.PuzzleThemeHangingPiece hanging_piece = 8;
  .chesscom.explanation_engine.v1.PuzzleThem
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04255"></a>
## FND-04255: chesscom.explanation_engine.v1.PuzzleTheme.fork = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeFork fork = 6;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 4047.

```text
endgame_tactics = 4;
  .chesscom.explanation_engine.v1.PuzzleThemeTrappedPiece trapped_piece = 5;
  .chesscom.explanation_engine.v1.PuzzleThemeFork fork = 6;
  .chesscom.explanation_engine.v1.PuzzleThemeSkewer skewer = 7;
  .chesscom.explanation_engine.v1.PuzzleThemeHangingPiece hanging_piece = 8;
  .chesscom.explanation_engine.v1.PuzzleThemeDiscovery discovery = 9;
  .chesscom.explanation_engine.v1.PuzzleThemeQueenS
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04256"></a>
## FND-04256: chesscom.explanation_engine.v1.PuzzleTheme.skewer = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeSkewer skewer = 7;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 4107.

```text
eThemeTrappedPiece trapped_piece = 5;
  .chesscom.explanation_engine.v1.PuzzleThemeFork fork = 6;
  .chesscom.explanation_engine.v1.PuzzleThemeSkewer skewer = 7;
  .chesscom.explanation_engine.v1.PuzzleThemeHangingPiece hanging_piece = 8;
  .chesscom.explanation_engine.v1.PuzzleThemeDiscovery discovery = 9;
  .chesscom.explanation_engine.v1.PuzzleThemeQueenSacrifice queen_sacrifice = 10;
  .chesscom.explanation_engin
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04257"></a>
## FND-04257: chesscom.explanation_engine.v1.PuzzleTheme.hanging_piece = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeHangingPiece hanging_piece = 8;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 4171.

```text
gine.v1.PuzzleThemeFork fork = 6;
  .chesscom.explanation_engine.v1.PuzzleThemeSkewer skewer = 7;
  .chesscom.explanation_engine.v1.PuzzleThemeHangingPiece hanging_piece = 8;
  .chesscom.explanation_engine.v1.PuzzleThemeDiscovery discovery = 9;
  .chesscom.explanation_engine.v1.PuzzleThemeQueenSacrifice queen_sacrifice = 10;
  .chesscom.explanation_engine.v1.PuzzleThemeOpposition opposition = 11;
  .chesscom.explanat
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04258"></a>
## FND-04258: chesscom.explanation_engine.v1.PuzzleTheme.discovery = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeDiscovery discovery = 9;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 4248.

```text
meSkewer skewer = 7;
  .chesscom.explanation_engine.v1.PuzzleThemeHangingPiece hanging_piece = 8;
  .chesscom.explanation_engine.v1.PuzzleThemeDiscovery discovery = 9;
  .chesscom.explanation_engine.v1.PuzzleThemeQueenSacrifice queen_sacrifice = 10;
  .chesscom.explanation_engine.v1.PuzzleThemeOpposition opposition = 11;
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn3Plus mate_in_3_plus = 12;
  .chesscom.explana
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04259"></a>
## FND-04259: chesscom.explanation_engine.v1.PuzzleTheme.queen_sacrifice = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeQueenSacrifice queen_sacrifice = 10;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 4318.

```text
ingPiece hanging_piece = 8;
  .chesscom.explanation_engine.v1.PuzzleThemeDiscovery discovery = 9;
  .chesscom.explanation_engine.v1.PuzzleThemeQueenSacrifice queen_sacrifice = 10;
  .chesscom.explanation_engine.v1.PuzzleThemeOpposition opposition = 11;
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn3Plus mate_in_3_plus = 12;
  .chesscom.explanation_engine.v1.PuzzleThemeMatingNet mating_net = 13;
  .chesscom.expla
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04260"></a>
## FND-04260: chesscom.explanation_engine.v1.PuzzleTheme.opposition = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeOpposition opposition = 11;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 4400.

```text
 discovery = 9;
  .chesscom.explanation_engine.v1.PuzzleThemeQueenSacrifice queen_sacrifice = 10;
  .chesscom.explanation_engine.v1.PuzzleThemeOpposition opposition = 11;
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn3Plus mate_in_3_plus = 12;
  .chesscom.explanation_engine.v1.PuzzleThemeMatingNet mating_net = 13;
  .chesscom.explanation_engine.v1.PuzzleThemePawnEndgame pawn_endgame = 14;
  .chesscom.explanation
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04261"></a>
## FND-04261: chesscom.explanation_engine.v1.PuzzleTheme.mate_in_3_plus = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeMateIn3Plus mate_in_3_plus = 12;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 4473.

```text
ce queen_sacrifice = 10;
  .chesscom.explanation_engine.v1.PuzzleThemeOpposition opposition = 11;
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn3Plus mate_in_3_plus = 12;
  .chesscom.explanation_engine.v1.PuzzleThemeMatingNet mating_net = 13;
  .chesscom.explanation_engine.v1.PuzzleThemePawnEndgame pawn_endgame = 14;
  .chesscom.explanation_engine.v1.PuzzleThemePromotion promotion = 15;
  .chesscom.explanation_e
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04262"></a>
## FND-04262: chesscom.explanation_engine.v1.PuzzleTheme.mating_net = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeMatingNet mating_net = 13;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 4551.

```text
on opposition = 11;
  .chesscom.explanation_engine.v1.PuzzleThemeMateIn3Plus mate_in_3_plus = 12;
  .chesscom.explanation_engine.v1.PuzzleThemeMatingNet mating_net = 13;
  .chesscom.explanation_engine.v1.PuzzleThemePawnEndgame pawn_endgame = 14;
  .chesscom.explanation_engine.v1.PuzzleThemePromotion promotion = 15;
  .chesscom.explanation_engine.v1.PuzzleThemeUnderPromotion under_promotion = 16;
  .chesscom.explanati
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04263"></a>
## FND-04263: chesscom.explanation_engine.v1.PuzzleTheme.pawn_endgame = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemePawnEndgame pawn_endgame = 14;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 4623.

```text
Plus mate_in_3_plus = 12;
  .chesscom.explanation_engine.v1.PuzzleThemeMatingNet mating_net = 13;
  .chesscom.explanation_engine.v1.PuzzleThemePawnEndgame pawn_endgame = 14;
  .chesscom.explanation_engine.v1.PuzzleThemePromotion promotion = 15;
  .chesscom.explanation_engine.v1.PuzzleThemeUnderPromotion under_promotion = 16;
  .chesscom.explanation_engine.v1.PuzzleThemeSacrifice sacrifice = 17;
  .chesscom.explanatio
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04264"></a>
## FND-04264: chesscom.explanation_engine.v1.PuzzleTheme.promotion = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemePromotion promotion = 15;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 4699.

```text
gNet mating_net = 13;
  .chesscom.explanation_engine.v1.PuzzleThemePawnEndgame pawn_endgame = 14;
  .chesscom.explanation_engine.v1.PuzzleThemePromotion promotion = 15;
  .chesscom.explanation_engine.v1.PuzzleThemeUnderPromotion under_promotion = 16;
  .chesscom.explanation_engine.v1.PuzzleThemeSacrifice sacrifice = 17;
  .chesscom.explanation_engine.v1.PuzzleThemeBackRankMate back_rank_mate = 18;
  .chesscom.explana
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04265"></a>
## FND-04265: chesscom.explanation_engine.v1.PuzzleTheme.under_promotion = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeUnderPromotion under_promotion = 16;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 4770.

```text
Endgame pawn_endgame = 14;
  .chesscom.explanation_engine.v1.PuzzleThemePromotion promotion = 15;
  .chesscom.explanation_engine.v1.PuzzleThemeUnderPromotion under_promotion = 16;
  .chesscom.explanation_engine.v1.PuzzleThemeSacrifice sacrifice = 17;
  .chesscom.explanation_engine.v1.PuzzleThemeBackRankMate back_rank_mate = 18;
  .chesscom.explanation_engine.v1.PuzzleThemePin pin = 19;
  .chesscom.explanation_engine.
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04266"></a>
## FND-04266: chesscom.explanation_engine.v1.PuzzleTheme.sacrifice = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeSacrifice sacrifice = 17;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 4852.

```text
promotion = 15;
  .chesscom.explanation_engine.v1.PuzzleThemeUnderPromotion under_promotion = 16;
  .chesscom.explanation_engine.v1.PuzzleThemeSacrifice sacrifice = 17;
  .chesscom.explanation_engine.v1.PuzzleThemeBackRankMate back_rank_mate = 18;
  .chesscom.explanation_engine.v1.PuzzleThemePin pin = 19;
  .chesscom.explanation_engine.v1.PuzzleThemeKingSafety king_safety = 20;
  .chesscom.explanation_engine.v1.Puzzl
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04267"></a>
## FND-04267: chesscom.explanation_engine.v1.PuzzleTheme.back_rank_mate = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeBackRankMate back_rank_mate = 18;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 4923.

```text
tion under_promotion = 16;
  .chesscom.explanation_engine.v1.PuzzleThemeSacrifice sacrifice = 17;
  .chesscom.explanation_engine.v1.PuzzleThemeBackRankMate back_rank_mate = 18;
  .chesscom.explanation_engine.v1.PuzzleThemePin pin = 19;
  .chesscom.explanation_engine.v1.PuzzleThemeKingSafety king_safety = 20;
  .chesscom.explanation_engine.v1.PuzzleThemePiecePlay piece_play = 21;
  .chesscom.explanation_engine.v1.Puzz
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04268"></a>
## FND-04268: chesscom.explanation_engine.v1.PuzzleTheme.pin = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemePin pin = 19;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5002.

```text
ce sacrifice = 17;
  .chesscom.explanation_engine.v1.PuzzleThemeBackRankMate back_rank_mate = 18;
  .chesscom.explanation_engine.v1.PuzzleThemePin pin = 19;
  .chesscom.explanation_engine.v1.PuzzleThemeKingSafety king_safety = 20;
  .chesscom.explanation_engine.v1.PuzzleThemePiecePlay piece_play = 21;
  .chesscom.explanation_engine.v1.PuzzleThemePawnStructure pawn_structure = 22;
  .chesscom.explanation_engine.v1.Puz
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04269"></a>
## FND-04269: chesscom.explanation_engine.v1.PuzzleTheme.king_safety = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeKingSafety king_safety = 20;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5061.

```text
ThemeBackRankMate back_rank_mate = 18;
  .chesscom.explanation_engine.v1.PuzzleThemePin pin = 19;
  .chesscom.explanation_engine.v1.PuzzleThemeKingSafety king_safety = 20;
  .chesscom.explanation_engine.v1.PuzzleThemePiecePlay piece_play = 21;
  .chesscom.explanation_engine.v1.PuzzleThemePawnStructure pawn_structure = 22;
  .chesscom.explanation_engine.v1.PuzzleThemeLadderMate ladder_mate = 23;
  }
  optional .chessc
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04270"></a>
## FND-04270: chesscom.explanation_engine.v1.PuzzleTheme.piece_play = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemePiecePlay piece_play = 21;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5135.

```text
uzzleThemePin pin = 19;
  .chesscom.explanation_engine.v1.PuzzleThemeKingSafety king_safety = 20;
  .chesscom.explanation_engine.v1.PuzzleThemePiecePlay piece_play = 21;
  .chesscom.explanation_engine.v1.PuzzleThemePawnStructure pawn_structure = 22;
  .chesscom.explanation_engine.v1.PuzzleThemeLadderMate ladder_mate = 23;
  }
  optional .chesscom.explanation_engine.v1.PuzzleThemeType theme_type = 255;
}

message Tact
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04271"></a>
## FND-04271: chesscom.explanation_engine.v1.PuzzleTheme.pawn_structure = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemePawnStructure pawn_structure = 22;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5207.

```text
gSafety king_safety = 20;
  .chesscom.explanation_engine.v1.PuzzleThemePiecePlay piece_play = 21;
  .chesscom.explanation_engine.v1.PuzzleThemePawnStructure pawn_structure = 22;
  .chesscom.explanation_engine.v1.PuzzleThemeLadderMate ladder_mate = 23;
  }
  optional .chesscom.explanation_engine.v1.PuzzleThemeType theme_type = 255;
}

message TacticalGoal {
  oneof goal {
  .chesscom.explanation_engine.v1.TacticalGoal
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04272"></a>
## FND-04272: chesscom.explanation_engine.v1.PuzzleTheme.ladder_mate = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleThemeLadderMate ladder_mate = 23;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5287.

```text
 piece_play = 21;
  .chesscom.explanation_engine.v1.PuzzleThemePawnStructure pawn_structure = 22;
  .chesscom.explanation_engine.v1.PuzzleThemeLadderMate ladder_mate = 23;
  }
  optional .chesscom.explanation_engine.v1.PuzzleThemeType theme_type = 255;
}

message TacticalGoal {
  oneof goal {
  .chesscom.explanation_engine.v1.TacticalGoalCheckmate checkmate = 1;
  .chesscom.explanation_engine.v1.TacticalGoalPromotion
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04273"></a>
## FND-04273: chesscom.explanation_engine.v1.PuzzleTheme.theme_type = 255

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.PuzzleThemeType theme_type = 255;

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5365.

```text
awn_structure = 22;
  .chesscom.explanation_engine.v1.PuzzleThemeLadderMate ladder_mate = 23;
  }
  optional .chesscom.explanation_engine.v1.PuzzleThemeType theme_type = 255;
}

message TacticalGoal {
  oneof goal {
  .chesscom.explanation_engine.v1.TacticalGoalCheckmate checkmate = 1;
  .chesscom.explanation_engine.v1.TacticalGoalPromotion promotion = 2;
  .chesscom.explanation_engine.v1.TacticalGoalAttackTheKing at
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04274"></a>
## FND-04274: message declaration: chesscom.explanation_engine.v1.TacticalGoal

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TacticalGoal {

### Evidence

- **SRC-0421** `research/proto/chesscom/explanation_engine/v1/puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/f40fce06d7b3ddfb65aaa5a9c16ffcf9445f06056504afa198dd921d3ecb1433.proto)
  Character offset 5443.

```text
dder_mate = 23;
  }
  optional .chesscom.explanation_engine.v1.PuzzleThemeType theme_type = 255;
}

message TacticalGoal {
  oneof goal {
  .chesscom.explanation_engine.v1.TacticalGoalCheckmate checkmate = 1;
  .chesscom.explanation_engine.v1.TacticalGoalPromotion promotion = 2;
  .chesscom.explanation_engine.v1.TacticalGoalAttackTheKing attack_the_king = 3;
  .chesscom.explanation_engine.v1.TacticalGoalWinMaterial w
```

**Source references:** SRC-0421, SRC-1392  
**URL references:** None independently associated  
**Related findings:** FND-04165, FND-04166, FND-04167

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
