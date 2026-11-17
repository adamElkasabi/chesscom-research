# data_models — findings 2401–2500

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-02675"></a>
## FND-02675: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CHECKS_AWAY_DEFENDER = 135

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CHECKS_AWAY_DEFENDER = 135;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5307.

```text
PE_MISSES_MATERIAL_LOSING_POSITION = 133;
  ANALYSIS_TYPE_MISSES_MATERIAL_WINNING_POSITION = 134;
  ANALYSIS_TYPE_CHECKS_AWAY_DEFENDER = 135;
  ANALYSIS_TYPE_PUNISH_MOVE_REFUTED_BY = 136;
  ANALYSIS_TYPE_PUNISH_MOVE_FALLBACK = 137;
  ANALYSIS_TYPE_PUNISH_MOVE_NONE = 138;
  ANALYSIS_TYPE_REMOVES_DEFENDER = 140;
  ANALYSIS_TYPE_REMOVES_MATE_DEFENDER = 141;
  ANALYSIS_TYPE_KICKS_DEFENDER = 142;
  ANALYSIS_TYPE_CAPTURES_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02676"></a>
## FND-02676: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PUNISH_MOVE_REFUTED_BY = 136

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PUNISH_MOVE_REFUTED_BY = 136;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5351.

```text
ANALYSIS_TYPE_MISSES_MATERIAL_WINNING_POSITION = 134;
  ANALYSIS_TYPE_CHECKS_AWAY_DEFENDER = 135;
  ANALYSIS_TYPE_PUNISH_MOVE_REFUTED_BY = 136;
  ANALYSIS_TYPE_PUNISH_MOVE_FALLBACK = 137;
  ANALYSIS_TYPE_PUNISH_MOVE_NONE = 138;
  ANALYSIS_TYPE_REMOVES_DEFENDER = 140;
  ANALYSIS_TYPE_REMOVES_MATE_DEFENDER = 141;
  ANALYSIS_TYPE_KICKS_DEFENDER = 142;
  ANALYSIS_TYPE_CAPTURES_MATE_DEFENDER = 143;
  ANALYSIS_TYPE_KICKS_M
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02677"></a>
## FND-02677: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PUNISH_MOVE_FALLBACK = 137

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PUNISH_MOVE_FALLBACK = 137;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5397.

```text
 = 134;
  ANALYSIS_TYPE_CHECKS_AWAY_DEFENDER = 135;
  ANALYSIS_TYPE_PUNISH_MOVE_REFUTED_BY = 136;
  ANALYSIS_TYPE_PUNISH_MOVE_FALLBACK = 137;
  ANALYSIS_TYPE_PUNISH_MOVE_NONE = 138;
  ANALYSIS_TYPE_REMOVES_DEFENDER = 140;
  ANALYSIS_TYPE_REMOVES_MATE_DEFENDER = 141;
  ANALYSIS_TYPE_KICKS_DEFENDER = 142;
  ANALYSIS_TYPE_CAPTURES_MATE_DEFENDER = 143;
  ANALYSIS_TYPE_KICKS_MATE_DEFENDER = 144;
  ANALYSIS_TYPE_MIDDLEGAME
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02678"></a>
## FND-02678: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PUNISH_MOVE_NONE = 138

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PUNISH_MOVE_NONE = 138;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5441.

```text
 = 135;
  ANALYSIS_TYPE_PUNISH_MOVE_REFUTED_BY = 136;
  ANALYSIS_TYPE_PUNISH_MOVE_FALLBACK = 137;
  ANALYSIS_TYPE_PUNISH_MOVE_NONE = 138;
  ANALYSIS_TYPE_REMOVES_DEFENDER = 140;
  ANALYSIS_TYPE_REMOVES_MATE_DEFENDER = 141;
  ANALYSIS_TYPE_KICKS_DEFENDER = 142;
  ANALYSIS_TYPE_CAPTURES_MATE_DEFENDER = 143;
  ANALYSIS_TYPE_KICKS_MATE_DEFENDER = 144;
  ANALYSIS_TYPE_MIDDLEGAME_START_NO_CASTLE = 145;
  ANALYSIS_TYPE_TRAD
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02679"></a>
## FND-02679: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_REMOVES_DEFENDER = 140

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_REMOVES_DEFENDER = 140;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5481.

```text
TED_BY = 136;
  ANALYSIS_TYPE_PUNISH_MOVE_FALLBACK = 137;
  ANALYSIS_TYPE_PUNISH_MOVE_NONE = 138;
  ANALYSIS_TYPE_REMOVES_DEFENDER = 140;
  ANALYSIS_TYPE_REMOVES_MATE_DEFENDER = 141;
  ANALYSIS_TYPE_KICKS_DEFENDER = 142;
  ANALYSIS_TYPE_CAPTURES_MATE_DEFENDER = 143;
  ANALYSIS_TYPE_KICKS_MATE_DEFENDER = 144;
  ANALYSIS_TYPE_MIDDLEGAME_START_NO_CASTLE = 145;
  ANALYSIS_TYPE_TRADE_TO_SIMPLIFY = 146;
  ANALYSIS_TYPE_BLO
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02680"></a>
## FND-02680: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_REMOVES_MATE_DEFENDER = 141

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_REMOVES_MATE_DEFENDER = 141;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5521.

```text
E_FALLBACK = 137;
  ANALYSIS_TYPE_PUNISH_MOVE_NONE = 138;
  ANALYSIS_TYPE_REMOVES_DEFENDER = 140;
  ANALYSIS_TYPE_REMOVES_MATE_DEFENDER = 141;
  ANALYSIS_TYPE_KICKS_DEFENDER = 142;
  ANALYSIS_TYPE_CAPTURES_MATE_DEFENDER = 143;
  ANALYSIS_TYPE_KICKS_MATE_DEFENDER = 144;
  ANALYSIS_TYPE_MIDDLEGAME_START_NO_CASTLE = 145;
  ANALYSIS_TYPE_TRADE_TO_SIMPLIFY = 146;
  ANALYSIS_TYPE_BLOCKADE = 147;
  ANALYSIS_TYPE_ATTACKS_PAW
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02681"></a>
## FND-02681: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_KICKS_DEFENDER = 142

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_KICKS_DEFENDER = 142;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5566.

```text
_NONE = 138;
  ANALYSIS_TYPE_REMOVES_DEFENDER = 140;
  ANALYSIS_TYPE_REMOVES_MATE_DEFENDER = 141;
  ANALYSIS_TYPE_KICKS_DEFENDER = 142;
  ANALYSIS_TYPE_CAPTURES_MATE_DEFENDER = 143;
  ANALYSIS_TYPE_KICKS_MATE_DEFENDER = 144;
  ANALYSIS_TYPE_MIDDLEGAME_START_NO_CASTLE = 145;
  ANALYSIS_TYPE_TRADE_TO_SIMPLIFY = 146;
  ANALYSIS_TYPE_BLOCKADE = 147;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN = 148;
  ANALYSIS_TYPE_SUPPORTS_PAWN_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02682"></a>
## FND-02682: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CAPTURES_MATE_DEFENDER = 143

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CAPTURES_MATE_DEFENDER = 143;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5604.

```text
EFENDER = 140;
  ANALYSIS_TYPE_REMOVES_MATE_DEFENDER = 141;
  ANALYSIS_TYPE_KICKS_DEFENDER = 142;
  ANALYSIS_TYPE_CAPTURES_MATE_DEFENDER = 143;
  ANALYSIS_TYPE_KICKS_MATE_DEFENDER = 144;
  ANALYSIS_TYPE_MIDDLEGAME_START_NO_CASTLE = 145;
  ANALYSIS_TYPE_TRADE_TO_SIMPLIFY = 146;
  ANALYSIS_TYPE_BLOCKADE = 147;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN = 148;
  ANALYSIS_TYPE_SUPPORTS_PAWN_CHAIN = 149;
  ANALYSIS_TYPE_CREATES_P
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02683"></a>
## FND-02683: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_KICKS_MATE_DEFENDER = 144

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_KICKS_MATE_DEFENDER = 144;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5650.

```text
FENDER = 141;
  ANALYSIS_TYPE_KICKS_DEFENDER = 142;
  ANALYSIS_TYPE_CAPTURES_MATE_DEFENDER = 143;
  ANALYSIS_TYPE_KICKS_MATE_DEFENDER = 144;
  ANALYSIS_TYPE_MIDDLEGAME_START_NO_CASTLE = 145;
  ANALYSIS_TYPE_TRADE_TO_SIMPLIFY = 146;
  ANALYSIS_TYPE_BLOCKADE = 147;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN = 148;
  ANALYSIS_TYPE_SUPPORTS_PAWN_CHAIN = 149;
  ANALYSIS_TYPE_CREATES_PAWN_CHAIN = 150;
  ANALYSIS_TYPE_UNTRIPLES_PAW
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02684"></a>
## FND-02684: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MIDDLEGAME_START_NO_CASTLE = 145

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_MIDDLEGAME_START_NO_CASTLE = 145;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5693.

```text
R = 142;
  ANALYSIS_TYPE_CAPTURES_MATE_DEFENDER = 143;
  ANALYSIS_TYPE_KICKS_MATE_DEFENDER = 144;
  ANALYSIS_TYPE_MIDDLEGAME_START_NO_CASTLE = 145;
  ANALYSIS_TYPE_TRADE_TO_SIMPLIFY = 146;
  ANALYSIS_TYPE_BLOCKADE = 147;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN = 148;
  ANALYSIS_TYPE_SUPPORTS_PAWN_CHAIN = 149;
  ANALYSIS_TYPE_CREATES_PAWN_CHAIN = 150;
  ANALYSIS_TYPE_UNTRIPLES_PAWNS = 151;
  ANALYSIS_TYPE_CREATES_BACKWARD_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02685"></a>
## FND-02685: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_TRADE_TO_SIMPLIFY = 146

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_TRADE_TO_SIMPLIFY = 146;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5743.

```text
143;
  ANALYSIS_TYPE_KICKS_MATE_DEFENDER = 144;
  ANALYSIS_TYPE_MIDDLEGAME_START_NO_CASTLE = 145;
  ANALYSIS_TYPE_TRADE_TO_SIMPLIFY = 146;
  ANALYSIS_TYPE_BLOCKADE = 147;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN = 148;
  ANALYSIS_TYPE_SUPPORTS_PAWN_CHAIN = 149;
  ANALYSIS_TYPE_CREATES_PAWN_CHAIN = 150;
  ANALYSIS_TYPE_UNTRIPLES_PAWNS = 151;
  ANALYSIS_TYPE_CREATES_BACKWARD_PAWN = 152;
  ANALYSIS_TYPE_CURES_BACKWARD_PAWN = 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02686"></a>
## FND-02686: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BLOCKADE = 147

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BLOCKADE = 147;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5784.

```text
= 144;
  ANALYSIS_TYPE_MIDDLEGAME_START_NO_CASTLE = 145;
  ANALYSIS_TYPE_TRADE_TO_SIMPLIFY = 146;
  ANALYSIS_TYPE_BLOCKADE = 147;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN = 148;
  ANALYSIS_TYPE_SUPPORTS_PAWN_CHAIN = 149;
  ANALYSIS_TYPE_CREATES_PAWN_CHAIN = 150;
  ANALYSIS_TYPE_UNTRIPLES_PAWNS = 151;
  ANALYSIS_TYPE_CREATES_BACKWARD_PAWN = 152;
  ANALYSIS_TYPE_CURES_BACKWARD_PAWN = 153;
  ANALYSIS_TYPE_MOVES_PAWN_IN_FRONT_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02687"></a>
## FND-02687: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN = 148

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN = 148;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5816.

```text
E_START_NO_CASTLE = 145;
  ANALYSIS_TYPE_TRADE_TO_SIMPLIFY = 146;
  ANALYSIS_TYPE_BLOCKADE = 147;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN = 148;
  ANALYSIS_TYPE_SUPPORTS_PAWN_CHAIN = 149;
  ANALYSIS_TYPE_CREATES_PAWN_CHAIN = 150;
  ANALYSIS_TYPE_UNTRIPLES_PAWNS = 151;
  ANALYSIS_TYPE_CREATES_BACKWARD_PAWN = 152;
  ANALYSIS_TYPE_CURES_BACKWARD_PAWN = 153;
  ANALYSIS_TYPE_MOVES_PAWN_IN_FRONT_OF_KING = 154;
  ANALYSIS_TYPE_C
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02688"></a>
## FND-02688: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_SUPPORTS_PAWN_CHAIN = 149

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_SUPPORTS_PAWN_CHAIN = 149;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5858.

```text
RADE_TO_SIMPLIFY = 146;
  ANALYSIS_TYPE_BLOCKADE = 147;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN = 148;
  ANALYSIS_TYPE_SUPPORTS_PAWN_CHAIN = 149;
  ANALYSIS_TYPE_CREATES_PAWN_CHAIN = 150;
  ANALYSIS_TYPE_UNTRIPLES_PAWNS = 151;
  ANALYSIS_TYPE_CREATES_BACKWARD_PAWN = 152;
  ANALYSIS_TYPE_CURES_BACKWARD_PAWN = 153;
  ANALYSIS_TYPE_MOVES_PAWN_IN_FRONT_OF_KING = 154;
  ANALYSIS_TYPE_CURES_ISOLATED_PAWN = 155;
  ANALYSIS_TYPE_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02689"></a>
## FND-02689: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CREATES_PAWN_CHAIN = 150

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CREATES_PAWN_CHAIN = 150;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5901.

```text
CKADE = 147;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN = 148;
  ANALYSIS_TYPE_SUPPORTS_PAWN_CHAIN = 149;
  ANALYSIS_TYPE_CREATES_PAWN_CHAIN = 150;
  ANALYSIS_TYPE_UNTRIPLES_PAWNS = 151;
  ANALYSIS_TYPE_CREATES_BACKWARD_PAWN = 152;
  ANALYSIS_TYPE_CURES_BACKWARD_PAWN = 153;
  ANALYSIS_TYPE_MOVES_PAWN_IN_FRONT_OF_KING = 154;
  ANALYSIS_TYPE_CURES_ISOLATED_PAWN = 155;
  ANALYSIS_TYPE_CREATES_PROTECTED_PASSED_PAWN = 156;
  ANAL
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02690"></a>
## FND-02690: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_UNTRIPLES_PAWNS = 151

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_UNTRIPLES_PAWNS = 151;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5943.

```text
CHAIN = 148;
  ANALYSIS_TYPE_SUPPORTS_PAWN_CHAIN = 149;
  ANALYSIS_TYPE_CREATES_PAWN_CHAIN = 150;
  ANALYSIS_TYPE_UNTRIPLES_PAWNS = 151;
  ANALYSIS_TYPE_CREATES_BACKWARD_PAWN = 152;
  ANALYSIS_TYPE_CURES_BACKWARD_PAWN = 153;
  ANALYSIS_TYPE_MOVES_PAWN_IN_FRONT_OF_KING = 154;
  ANALYSIS_TYPE_CURES_ISOLATED_PAWN = 155;
  ANALYSIS_TYPE_CREATES_PROTECTED_PASSED_PAWN = 156;
  ANALYSIS_TYPE_ROOK_TAKES_OUTPOST = 157;
  ANAL
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02691"></a>
## FND-02691: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CREATES_BACKWARD_PAWN = 152

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CREATES_BACKWARD_PAWN = 152;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5982.

```text
AWN_CHAIN = 149;
  ANALYSIS_TYPE_CREATES_PAWN_CHAIN = 150;
  ANALYSIS_TYPE_UNTRIPLES_PAWNS = 151;
  ANALYSIS_TYPE_CREATES_BACKWARD_PAWN = 152;
  ANALYSIS_TYPE_CURES_BACKWARD_PAWN = 153;
  ANALYSIS_TYPE_MOVES_PAWN_IN_FRONT_OF_KING = 154;
  ANALYSIS_TYPE_CURES_ISOLATED_PAWN = 155;
  ANALYSIS_TYPE_CREATES_PROTECTED_PASSED_PAWN = 156;
  ANALYSIS_TYPE_ROOK_TAKES_OUTPOST = 157;
  ANALYSIS_TYPE_ISOLATES_PAWN_ON_SEMI_OPEN_FI
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02692"></a>
## FND-02692: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CURES_BACKWARD_PAWN = 153

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CURES_BACKWARD_PAWN = 153;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6027.

```text
_CHAIN = 150;
  ANALYSIS_TYPE_UNTRIPLES_PAWNS = 151;
  ANALYSIS_TYPE_CREATES_BACKWARD_PAWN = 152;
  ANALYSIS_TYPE_CURES_BACKWARD_PAWN = 153;
  ANALYSIS_TYPE_MOVES_PAWN_IN_FRONT_OF_KING = 154;
  ANALYSIS_TYPE_CURES_ISOLATED_PAWN = 155;
  ANALYSIS_TYPE_CREATES_PROTECTED_PASSED_PAWN = 156;
  ANALYSIS_TYPE_ROOK_TAKES_OUTPOST = 157;
  ANALYSIS_TYPE_ISOLATES_PAWN_ON_SEMI_OPEN_FILE = 158;
  ANALYSIS_TYPE_BACKWARD_PAWN_ON_SE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02693"></a>
## FND-02693: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MOVES_PAWN_IN_FRONT_OF_KING = 154

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_MOVES_PAWN_IN_FRONT_OF_KING = 154;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6070.

```text
NS = 151;
  ANALYSIS_TYPE_CREATES_BACKWARD_PAWN = 152;
  ANALYSIS_TYPE_CURES_BACKWARD_PAWN = 153;
  ANALYSIS_TYPE_MOVES_PAWN_IN_FRONT_OF_KING = 154;
  ANALYSIS_TYPE_CURES_ISOLATED_PAWN = 155;
  ANALYSIS_TYPE_CREATES_PROTECTED_PASSED_PAWN = 156;
  ANALYSIS_TYPE_ROOK_TAKES_OUTPOST = 157;
  ANALYSIS_TYPE_ISOLATES_PAWN_ON_SEMI_OPEN_FILE = 158;
  ANALYSIS_TYPE_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 159;
  ANALYSIS_TYPE_DOUBLED
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02694"></a>
## FND-02694: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CURES_ISOLATED_PAWN = 155

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CURES_ISOLATED_PAWN = 155;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6121.

```text
52;
  ANALYSIS_TYPE_CURES_BACKWARD_PAWN = 153;
  ANALYSIS_TYPE_MOVES_PAWN_IN_FRONT_OF_KING = 154;
  ANALYSIS_TYPE_CURES_ISOLATED_PAWN = 155;
  ANALYSIS_TYPE_CREATES_PROTECTED_PASSED_PAWN = 156;
  ANALYSIS_TYPE_ROOK_TAKES_OUTPOST = 157;
  ANALYSIS_TYPE_ISOLATES_PAWN_ON_SEMI_OPEN_FILE = 158;
  ANALYSIS_TYPE_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 159;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN = 160;
  ANALYSIS_TYPE_DOUBLED_BACKW
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02695"></a>
## FND-02695: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CREATES_PROTECTED_PASSED_PAWN = 156

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CREATES_PROTECTED_PASSED_PAWN = 156;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6164.

```text
53;
  ANALYSIS_TYPE_MOVES_PAWN_IN_FRONT_OF_KING = 154;
  ANALYSIS_TYPE_CURES_ISOLATED_PAWN = 155;
  ANALYSIS_TYPE_CREATES_PROTECTED_PASSED_PAWN = 156;
  ANALYSIS_TYPE_ROOK_TAKES_OUTPOST = 157;
  ANALYSIS_TYPE_ISOLATES_PAWN_ON_SEMI_OPEN_FILE = 158;
  ANALYSIS_TYPE_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 159;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN = 160;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 161;
  ANALYSI
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02696"></a>
## FND-02696: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ROOK_TAKES_OUTPOST = 157

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_ROOK_TAKES_OUTPOST = 157;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6217.

```text
;
  ANALYSIS_TYPE_CURES_ISOLATED_PAWN = 155;
  ANALYSIS_TYPE_CREATES_PROTECTED_PASSED_PAWN = 156;
  ANALYSIS_TYPE_ROOK_TAKES_OUTPOST = 157;
  ANALYSIS_TYPE_ISOLATES_PAWN_ON_SEMI_OPEN_FILE = 158;
  ANALYSIS_TYPE_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 159;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN = 160;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 161;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN = 162;
  ANALYSIS_TYPE_D
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02697"></a>
## FND-02697: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ISOLATES_PAWN_ON_SEMI_OPEN_FILE = 158

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_ISOLATES_PAWN_ON_SEMI_OPEN_FILE = 158;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6259.

```text
5;
  ANALYSIS_TYPE_CREATES_PROTECTED_PASSED_PAWN = 156;
  ANALYSIS_TYPE_ROOK_TAKES_OUTPOST = 157;
  ANALYSIS_TYPE_ISOLATES_PAWN_ON_SEMI_OPEN_FILE = 158;
  ANALYSIS_TYPE_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 159;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN = 160;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 161;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN = 162;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN_ON_SEMI_OPEN_FILE = 1
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02698"></a>
## FND-02698: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 159

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 159;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6314.

```text

  ANALYSIS_TYPE_ROOK_TAKES_OUTPOST = 157;
  ANALYSIS_TYPE_ISOLATES_PAWN_ON_SEMI_OPEN_FILE = 158;
  ANALYSIS_TYPE_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 159;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN = 160;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 161;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN = 162;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN_ON_SEMI_OPEN_FILE = 163;
  ANALYSIS_TYPE_CREATES_OPPONENT_PROTECTED_PASSED_P
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02699"></a>
## FND-02699: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN = 160

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN = 160;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6369.

```text
YPE_ISOLATES_PAWN_ON_SEMI_OPEN_FILE = 158;
  ANALYSIS_TYPE_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 159;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN = 160;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 161;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN = 162;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN_ON_SEMI_OPEN_FILE = 163;
  ANALYSIS_TYPE_CREATES_OPPONENT_PROTECTED_PASSED_PAWN = 164;
  ANALYSIS_TYPE_WEAKENED_CASTLED_KING = 165;
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02700"></a>
## FND-02700: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 161

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 161;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6414.

```text
ANALYSIS_TYPE_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 159;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN = 160;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 161;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN = 162;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN_ON_SEMI_OPEN_FILE = 163;
  ANALYSIS_TYPE_CREATES_OPPONENT_PROTECTED_PASSED_PAWN = 164;
  ANALYSIS_TYPE_WEAKENED_CASTLED_KING = 165;
  ANALYSIS_TYPE_MOVES_SAME_PIECE_IN_OPENING 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02701"></a>
## FND-02701: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN = 162

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN = 162;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6477.

```text
_TYPE_DOUBLED_BACKWARD_PAWN = 160;
  ANALYSIS_TYPE_DOUBLED_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 161;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN = 162;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN_ON_SEMI_OPEN_FILE = 163;
  ANALYSIS_TYPE_CREATES_OPPONENT_PROTECTED_PASSED_PAWN = 164;
  ANALYSIS_TYPE_WEAKENED_CASTLED_KING = 165;
  ANALYSIS_TYPE_MOVES_SAME_PIECE_IN_OPENING = 166;
  ANALYSIS_TYPE_TRADE_TO_WON_PAWN_ENDGAME = 167;
  ANALY
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02702"></a>
## FND-02702: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN_ON_SEMI_OPEN_FILE = 163

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN_ON_SEMI_OPEN_FILE = 163;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6522.

```text
_TYPE_DOUBLED_BACKWARD_PAWN_ON_SEMI_OPEN_FILE = 161;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN = 162;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN_ON_SEMI_OPEN_FILE = 163;
  ANALYSIS_TYPE_CREATES_OPPONENT_PROTECTED_PASSED_PAWN = 164;
  ANALYSIS_TYPE_WEAKENED_CASTLED_KING = 165;
  ANALYSIS_TYPE_MOVES_SAME_PIECE_IN_OPENING = 166;
  ANALYSIS_TYPE_TRADE_TO_WON_PAWN_ENDGAME = 167;
  ANALYSIS_TYPE_TRADE_TO_LOST_PAWN_ENDGAME = 168;
  
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02703"></a>
## FND-02703: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CREATES_OPPONENT_PROTECTED_PASSED_PAWN = 164

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CREATES_OPPONENT_PROTECTED_PASSED_PAWN = 164;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6585.

```text
_TYPE_DOUBLED_ISOLATED_PAWN = 162;
  ANALYSIS_TYPE_DOUBLED_ISOLATED_PAWN_ON_SEMI_OPEN_FILE = 163;
  ANALYSIS_TYPE_CREATES_OPPONENT_PROTECTED_PASSED_PAWN = 164;
  ANALYSIS_TYPE_WEAKENED_CASTLED_KING = 165;
  ANALYSIS_TYPE_MOVES_SAME_PIECE_IN_OPENING = 166;
  ANALYSIS_TYPE_TRADE_TO_WON_PAWN_ENDGAME = 167;
  ANALYSIS_TYPE_TRADE_TO_LOST_PAWN_ENDGAME = 168;
  ANALYSIS_TYPE_GOOD_TRADE_TO_DRAWN_PAWN_ENDGAME = 169;
  ANALYSI
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02704"></a>
## FND-02704: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WEAKENED_CASTLED_KING = 165

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_WEAKENED_CASTLED_KING = 165;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6647.

```text
LATED_PAWN_ON_SEMI_OPEN_FILE = 163;
  ANALYSIS_TYPE_CREATES_OPPONENT_PROTECTED_PASSED_PAWN = 164;
  ANALYSIS_TYPE_WEAKENED_CASTLED_KING = 165;
  ANALYSIS_TYPE_MOVES_SAME_PIECE_IN_OPENING = 166;
  ANALYSIS_TYPE_TRADE_TO_WON_PAWN_ENDGAME = 167;
  ANALYSIS_TYPE_TRADE_TO_LOST_PAWN_ENDGAME = 168;
  ANALYSIS_TYPE_GOOD_TRADE_TO_DRAWN_PAWN_ENDGAME = 169;
  ANALYSIS_TYPE_BAD_TRADE_TO_DRAWN_PAWN_ENDGAME = 170;
  ANALYSIS_TYPE_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02705"></a>
## FND-02705: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MOVES_SAME_PIECE_IN_OPENING = 166

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_MOVES_SAME_PIECE_IN_OPENING = 166;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6692.

```text
S_TYPE_CREATES_OPPONENT_PROTECTED_PASSED_PAWN = 164;
  ANALYSIS_TYPE_WEAKENED_CASTLED_KING = 165;
  ANALYSIS_TYPE_MOVES_SAME_PIECE_IN_OPENING = 166;
  ANALYSIS_TYPE_TRADE_TO_WON_PAWN_ENDGAME = 167;
  ANALYSIS_TYPE_TRADE_TO_LOST_PAWN_ENDGAME = 168;
  ANALYSIS_TYPE_GOOD_TRADE_TO_DRAWN_PAWN_ENDGAME = 169;
  ANALYSIS_TYPE_BAD_TRADE_TO_DRAWN_PAWN_ENDGAME = 170;
  ANALYSIS_TYPE_CHECKS_WITH_PIECE = 171;
  ANALYSIS_TYPE_KING
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02706"></a>
## FND-02706: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_TRADE_TO_WON_PAWN_ENDGAME = 167

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_TRADE_TO_WON_PAWN_ENDGAME = 167;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6743.

```text
;
  ANALYSIS_TYPE_WEAKENED_CASTLED_KING = 165;
  ANALYSIS_TYPE_MOVES_SAME_PIECE_IN_OPENING = 166;
  ANALYSIS_TYPE_TRADE_TO_WON_PAWN_ENDGAME = 167;
  ANALYSIS_TYPE_TRADE_TO_LOST_PAWN_ENDGAME = 168;
  ANALYSIS_TYPE_GOOD_TRADE_TO_DRAWN_PAWN_ENDGAME = 169;
  ANALYSIS_TYPE_BAD_TRADE_TO_DRAWN_PAWN_ENDGAME = 170;
  ANALYSIS_TYPE_CHECKS_WITH_PIECE = 171;
  ANALYSIS_TYPE_KING_REACHES_SQUARE_OF_PAWN = 172;
  ANALYSIS_TYPE_EXCH
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02707"></a>
## FND-02707: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_TRADE_TO_LOST_PAWN_ENDGAME = 168

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_TRADE_TO_LOST_PAWN_ENDGAME = 168;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6792.

```text
ANALYSIS_TYPE_MOVES_SAME_PIECE_IN_OPENING = 166;
  ANALYSIS_TYPE_TRADE_TO_WON_PAWN_ENDGAME = 167;
  ANALYSIS_TYPE_TRADE_TO_LOST_PAWN_ENDGAME = 168;
  ANALYSIS_TYPE_GOOD_TRADE_TO_DRAWN_PAWN_ENDGAME = 169;
  ANALYSIS_TYPE_BAD_TRADE_TO_DRAWN_PAWN_ENDGAME = 170;
  ANALYSIS_TYPE_CHECKS_WITH_PIECE = 171;
  ANALYSIS_TYPE_KING_REACHES_SQUARE_OF_PAWN = 172;
  ANALYSIS_TYPE_EXCHANGE_SACRIFICE = 173;
  ANALYSIS_TYPE_DISCOVERED_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02708"></a>
## FND-02708: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_GOOD_TRADE_TO_DRAWN_PAWN_ENDGAME = 169

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_GOOD_TRADE_TO_DRAWN_PAWN_ENDGAME = 169;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6842.

```text
 ANALYSIS_TYPE_TRADE_TO_WON_PAWN_ENDGAME = 167;
  ANALYSIS_TYPE_TRADE_TO_LOST_PAWN_ENDGAME = 168;
  ANALYSIS_TYPE_GOOD_TRADE_TO_DRAWN_PAWN_ENDGAME = 169;
  ANALYSIS_TYPE_BAD_TRADE_TO_DRAWN_PAWN_ENDGAME = 170;
  ANALYSIS_TYPE_CHECKS_WITH_PIECE = 171;
  ANALYSIS_TYPE_KING_REACHES_SQUARE_OF_PAWN = 172;
  ANALYSIS_TYPE_EXCHANGE_SACRIFICE = 173;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CAPTURE = 174;
  ANALYSIS_TYPE_DISCOVERED_C
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02709"></a>
## FND-02709: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BAD_TRADE_TO_DRAWN_PAWN_ENDGAME = 170

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BAD_TRADE_TO_DRAWN_PAWN_ENDGAME = 170;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6898.

```text
IS_TYPE_TRADE_TO_LOST_PAWN_ENDGAME = 168;
  ANALYSIS_TYPE_GOOD_TRADE_TO_DRAWN_PAWN_ENDGAME = 169;
  ANALYSIS_TYPE_BAD_TRADE_TO_DRAWN_PAWN_ENDGAME = 170;
  ANALYSIS_TYPE_CHECKS_WITH_PIECE = 171;
  ANALYSIS_TYPE_KING_REACHES_SQUARE_OF_PAWN = 172;
  ANALYSIS_TYPE_EXCHANGE_SACRIFICE = 173;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CAPTURE = 174;
  ANALYSIS_TYPE_DISCOVERED_CHECK_CAPTURE = 175;
  ANALYSIS_TYPE_GAINS_QUEENSIDE_SPAC
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02710"></a>
## FND-02710: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CHECKS_WITH_PIECE = 171

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CHECKS_WITH_PIECE = 171;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6953.

```text
PE_GOOD_TRADE_TO_DRAWN_PAWN_ENDGAME = 169;
  ANALYSIS_TYPE_BAD_TRADE_TO_DRAWN_PAWN_ENDGAME = 170;
  ANALYSIS_TYPE_CHECKS_WITH_PIECE = 171;
  ANALYSIS_TYPE_KING_REACHES_SQUARE_OF_PAWN = 172;
  ANALYSIS_TYPE_EXCHANGE_SACRIFICE = 173;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CAPTURE = 174;
  ANALYSIS_TYPE_DISCOVERED_CHECK_CAPTURE = 175;
  ANALYSIS_TYPE_GAINS_QUEENSIDE_SPACE = 176;
  ANALYSIS_TYPE_GAINS_KINGSIDE_SPACE = 177;
  
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02711"></a>
## FND-02711: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_KING_REACHES_SQUARE_OF_PAWN = 172

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_KING_REACHES_SQUARE_OF_PAWN = 172;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 6994.

```text
;
  ANALYSIS_TYPE_BAD_TRADE_TO_DRAWN_PAWN_ENDGAME = 170;
  ANALYSIS_TYPE_CHECKS_WITH_PIECE = 171;
  ANALYSIS_TYPE_KING_REACHES_SQUARE_OF_PAWN = 172;
  ANALYSIS_TYPE_EXCHANGE_SACRIFICE = 173;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CAPTURE = 174;
  ANALYSIS_TYPE_DISCOVERED_CHECK_CAPTURE = 175;
  ANALYSIS_TYPE_GAINS_QUEENSIDE_SPACE = 176;
  ANALYSIS_TYPE_GAINS_KINGSIDE_SPACE = 177;
  ANALYSIS_TYPE_GAINS_CENTRAL_SPACE = 178;

```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02712"></a>
## FND-02712: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_EXCHANGE_SACRIFICE = 173

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_EXCHANGE_SACRIFICE = 173;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7045.

```text
 170;
  ANALYSIS_TYPE_CHECKS_WITH_PIECE = 171;
  ANALYSIS_TYPE_KING_REACHES_SQUARE_OF_PAWN = 172;
  ANALYSIS_TYPE_EXCHANGE_SACRIFICE = 173;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CAPTURE = 174;
  ANALYSIS_TYPE_DISCOVERED_CHECK_CAPTURE = 175;
  ANALYSIS_TYPE_GAINS_QUEENSIDE_SPACE = 176;
  ANALYSIS_TYPE_GAINS_KINGSIDE_SPACE = 177;
  ANALYSIS_TYPE_GAINS_CENTRAL_SPACE = 178;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_MIDDLEGAME = 179
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02713"></a>
## FND-02713: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DISCOVERED_ATTACK_CAPTURE = 174

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DISCOVERED_ATTACK_CAPTURE = 174;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7087.

```text
171;
  ANALYSIS_TYPE_KING_REACHES_SQUARE_OF_PAWN = 172;
  ANALYSIS_TYPE_EXCHANGE_SACRIFICE = 173;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CAPTURE = 174;
  ANALYSIS_TYPE_DISCOVERED_CHECK_CAPTURE = 175;
  ANALYSIS_TYPE_GAINS_QUEENSIDE_SPACE = 176;
  ANALYSIS_TYPE_GAINS_KINGSIDE_SPACE = 177;
  ANALYSIS_TYPE_GAINS_CENTRAL_SPACE = 178;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_MIDDLEGAME = 179;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_ENDGA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02714"></a>
## FND-02714: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DISCOVERED_CHECK_CAPTURE = 175

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DISCOVERED_CHECK_CAPTURE = 175;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7136.

```text
= 172;
  ANALYSIS_TYPE_EXCHANGE_SACRIFICE = 173;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CAPTURE = 174;
  ANALYSIS_TYPE_DISCOVERED_CHECK_CAPTURE = 175;
  ANALYSIS_TYPE_GAINS_QUEENSIDE_SPACE = 176;
  ANALYSIS_TYPE_GAINS_KINGSIDE_SPACE = 177;
  ANALYSIS_TYPE_GAINS_CENTRAL_SPACE = 178;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_MIDDLEGAME = 179;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_ENDGAME = 180;
  ANALYSIS_TYPE_LADDER_MATE = 181;
  AN
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02715"></a>
## FND-02715: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_GAINS_QUEENSIDE_SPACE = 176

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_GAINS_QUEENSIDE_SPACE = 176;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7184.

```text

  ANALYSIS_TYPE_DISCOVERED_ATTACK_CAPTURE = 174;
  ANALYSIS_TYPE_DISCOVERED_CHECK_CAPTURE = 175;
  ANALYSIS_TYPE_GAINS_QUEENSIDE_SPACE = 176;
  ANALYSIS_TYPE_GAINS_KINGSIDE_SPACE = 177;
  ANALYSIS_TYPE_GAINS_CENTRAL_SPACE = 178;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_MIDDLEGAME = 179;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_ENDGAME = 180;
  ANALYSIS_TYPE_LADDER_MATE = 181;
  ANALYSIS_TYPE_AVOIDS_TRADE = 182;
  ANALYSIS_TYPE_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02716"></a>
## FND-02716: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_GAINS_KINGSIDE_SPACE = 177

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_GAINS_KINGSIDE_SPACE = 177;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7229.

```text
174;
  ANALYSIS_TYPE_DISCOVERED_CHECK_CAPTURE = 175;
  ANALYSIS_TYPE_GAINS_QUEENSIDE_SPACE = 176;
  ANALYSIS_TYPE_GAINS_KINGSIDE_SPACE = 177;
  ANALYSIS_TYPE_GAINS_CENTRAL_SPACE = 178;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_MIDDLEGAME = 179;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_ENDGAME = 180;
  ANALYSIS_TYPE_LADDER_MATE = 181;
  ANALYSIS_TYPE_AVOIDS_TRADE = 182;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_WIN = 183;
  ANALY
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02717"></a>
## FND-02717: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_GAINS_CENTRAL_SPACE = 178

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_GAINS_CENTRAL_SPACE = 178;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7273.

```text
E = 175;
  ANALYSIS_TYPE_GAINS_QUEENSIDE_SPACE = 176;
  ANALYSIS_TYPE_GAINS_KINGSIDE_SPACE = 177;
  ANALYSIS_TYPE_GAINS_CENTRAL_SPACE = 178;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_MIDDLEGAME = 179;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_ENDGAME = 180;
  ANALYSIS_TYPE_LADDER_MATE = 181;
  ANALYSIS_TYPE_AVOIDS_TRADE = 182;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_WIN = 183;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_DRAW = 1
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02718"></a>
## FND-02718: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PUSHES_PASSED_PAWN_MIDDLEGAME = 179

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PUSHES_PASSED_PAWN_MIDDLEGAME = 179;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7316.

```text
ACE = 176;
  ANALYSIS_TYPE_GAINS_KINGSIDE_SPACE = 177;
  ANALYSIS_TYPE_GAINS_CENTRAL_SPACE = 178;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_MIDDLEGAME = 179;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_ENDGAME = 180;
  ANALYSIS_TYPE_LADDER_MATE = 181;
  ANALYSIS_TYPE_AVOIDS_TRADE = 182;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_WIN = 183;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_DRAW = 184;
  ANALYSIS_TYPE_MOVES_TO_PASSIVE_SQUARE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02719"></a>
## FND-02719: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PUSHES_PASSED_PAWN_ENDGAME = 180

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PUSHES_PASSED_PAWN_ENDGAME = 180;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7369.

```text
;
  ANALYSIS_TYPE_GAINS_CENTRAL_SPACE = 178;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_MIDDLEGAME = 179;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_ENDGAME = 180;
  ANALYSIS_TYPE_LADDER_MATE = 181;
  ANALYSIS_TYPE_AVOIDS_TRADE = 182;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_WIN = 183;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_DRAW = 184;
  ANALYSIS_TYPE_MOVES_TO_PASSIVE_SQUARE = 185;
  ANALYSIS_TYPE_MANEUVERS_TO_ACTIVE_SQUARE = 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02720"></a>
## FND-02720: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_LADDER_MATE = 181

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_LADDER_MATE = 181;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7419.

```text
LYSIS_TYPE_PUSHES_PASSED_PAWN_MIDDLEGAME = 179;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_ENDGAME = 180;
  ANALYSIS_TYPE_LADDER_MATE = 181;
  ANALYSIS_TYPE_AVOIDS_TRADE = 182;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_WIN = 183;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_DRAW = 184;
  ANALYSIS_TYPE_MOVES_TO_PASSIVE_SQUARE = 185;
  ANALYSIS_TYPE_MANEUVERS_TO_ACTIVE_SQUARE = 186;
  ANALYSIS_TYPE_MOVES_TO_ACTIVE_SQUARE = 187;
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02721"></a>
## FND-02721: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_AVOIDS_TRADE = 182

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_AVOIDS_TRADE = 182;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7454.

```text
EGAME = 179;
  ANALYSIS_TYPE_PUSHES_PASSED_PAWN_ENDGAME = 180;
  ANALYSIS_TYPE_LADDER_MATE = 181;
  ANALYSIS_TYPE_AVOIDS_TRADE = 182;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_WIN = 183;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_DRAW = 184;
  ANALYSIS_TYPE_MOVES_TO_PASSIVE_SQUARE = 185;
  ANALYSIS_TYPE_MANEUVERS_TO_ACTIVE_SQUARE = 186;
  ANALYSIS_TYPE_MOVES_TO_ACTIVE_SQUARE = 187;
  ANALYSIS_TYPE_PUZZLE_HINT_FALLBA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02722"></a>
## FND-02722: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_WIN = 183

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_WIN = 183;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7490.

```text
PASSED_PAWN_ENDGAME = 180;
  ANALYSIS_TYPE_LADDER_MATE = 181;
  ANALYSIS_TYPE_AVOIDS_TRADE = 182;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_WIN = 183;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_DRAW = 184;
  ANALYSIS_TYPE_MOVES_TO_PASSIVE_SQUARE = 185;
  ANALYSIS_TYPE_MANEUVERS_TO_ACTIVE_SQUARE = 186;
  ANALYSIS_TYPE_MOVES_TO_ACTIVE_SQUARE = 187;
  ANALYSIS_TYPE_PUZZLE_HINT_FALLBACK = 188;
  ANALYSIS_TYPE_OPENS_UP_W
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02723"></a>
## FND-02723: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_DRAW = 184

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_DRAW = 184;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7544.

```text
 = 181;
  ANALYSIS_TYPE_AVOIDS_TRADE = 182;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_WIN = 183;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_DRAW = 184;
  ANALYSIS_TYPE_MOVES_TO_PASSIVE_SQUARE = 185;
  ANALYSIS_TYPE_MANEUVERS_TO_ACTIVE_SQUARE = 186;
  ANALYSIS_TYPE_MOVES_TO_ACTIVE_SQUARE = 187;
  ANALYSIS_TYPE_PUZZLE_HINT_FALLBACK = 188;
  ANALYSIS_TYPE_OPENS_UP_WEAK_KING = 189;
  ANALYSIS_TYPE_DEVELOPS_LAST_PIECE = 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02724"></a>
## FND-02724: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MOVES_TO_PASSIVE_SQUARE = 185

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_MOVES_TO_PASSIVE_SQUARE = 185;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7599.

```text
TYPE_GAINS_DIRECT_OPPOSITION_TO_WIN = 183;
  ANALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_DRAW = 184;
  ANALYSIS_TYPE_MOVES_TO_PASSIVE_SQUARE = 185;
  ANALYSIS_TYPE_MANEUVERS_TO_ACTIVE_SQUARE = 186;
  ANALYSIS_TYPE_MOVES_TO_ACTIVE_SQUARE = 187;
  ANALYSIS_TYPE_PUZZLE_HINT_FALLBACK = 188;
  ANALYSIS_TYPE_OPENS_UP_WEAK_KING = 189;
  ANALYSIS_TYPE_DEVELOPS_LAST_PIECE = 190;
  ANALYSIS_TYPE_DEVELOPS_CENTER = 191;
  ANALYSIS_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02725"></a>
## FND-02725: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MANEUVERS_TO_ACTIVE_SQUARE = 186

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_MANEUVERS_TO_ACTIVE_SQUARE = 186;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7646.

```text
ALYSIS_TYPE_GAINS_DIRECT_OPPOSITION_TO_DRAW = 184;
  ANALYSIS_TYPE_MOVES_TO_PASSIVE_SQUARE = 185;
  ANALYSIS_TYPE_MANEUVERS_TO_ACTIVE_SQUARE = 186;
  ANALYSIS_TYPE_MOVES_TO_ACTIVE_SQUARE = 187;
  ANALYSIS_TYPE_PUZZLE_HINT_FALLBACK = 188;
  ANALYSIS_TYPE_OPENS_UP_WEAK_KING = 189;
  ANALYSIS_TYPE_DEVELOPS_LAST_PIECE = 190;
  ANALYSIS_TYPE_DEVELOPS_CENTER = 191;
  ANALYSIS_TYPE_DEVELOPS_RECAPTURE = 192;
  ANALYSIS_TYPE_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02726"></a>
## FND-02726: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MOVES_TO_ACTIVE_SQUARE = 187

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_MOVES_TO_ACTIVE_SQUARE = 187;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7696.

```text

  ANALYSIS_TYPE_MOVES_TO_PASSIVE_SQUARE = 185;
  ANALYSIS_TYPE_MANEUVERS_TO_ACTIVE_SQUARE = 186;
  ANALYSIS_TYPE_MOVES_TO_ACTIVE_SQUARE = 187;
  ANALYSIS_TYPE_PUZZLE_HINT_FALLBACK = 188;
  ANALYSIS_TYPE_OPENS_UP_WEAK_KING = 189;
  ANALYSIS_TYPE_DEVELOPS_LAST_PIECE = 190;
  ANALYSIS_TYPE_DEVELOPS_CENTER = 191;
  ANALYSIS_TYPE_DEVELOPS_RECAPTURE = 192;
  ANALYSIS_TYPE_DEVELOPS_OPENING = 193;
  ANALYSIS_TYPE_DEVELOPS_M
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02727"></a>
## FND-02727: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PUZZLE_HINT_FALLBACK = 188

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PUZZLE_HINT_FALLBACK = 188;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7742.

```text
;
  ANALYSIS_TYPE_MANEUVERS_TO_ACTIVE_SQUARE = 186;
  ANALYSIS_TYPE_MOVES_TO_ACTIVE_SQUARE = 187;
  ANALYSIS_TYPE_PUZZLE_HINT_FALLBACK = 188;
  ANALYSIS_TYPE_OPENS_UP_WEAK_KING = 189;
  ANALYSIS_TYPE_DEVELOPS_LAST_PIECE = 190;
  ANALYSIS_TYPE_DEVELOPS_CENTER = 191;
  ANALYSIS_TYPE_DEVELOPS_RECAPTURE = 192;
  ANALYSIS_TYPE_DEVELOPS_OPENING = 193;
  ANALYSIS_TYPE_DEVELOPS_MIDDLEGAME = 194;
  ANALYSIS_TYPE_FORCES_STALEM
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02728"></a>
## FND-02728: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_OPENS_UP_WEAK_KING = 189

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_OPENS_UP_WEAK_KING = 189;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7786.

```text
 = 186;
  ANALYSIS_TYPE_MOVES_TO_ACTIVE_SQUARE = 187;
  ANALYSIS_TYPE_PUZZLE_HINT_FALLBACK = 188;
  ANALYSIS_TYPE_OPENS_UP_WEAK_KING = 189;
  ANALYSIS_TYPE_DEVELOPS_LAST_PIECE = 190;
  ANALYSIS_TYPE_DEVELOPS_CENTER = 191;
  ANALYSIS_TYPE_DEVELOPS_RECAPTURE = 192;
  ANALYSIS_TYPE_DEVELOPS_OPENING = 193;
  ANALYSIS_TYPE_DEVELOPS_MIDDLEGAME = 194;
  ANALYSIS_TYPE_FORCES_STALEMATE = 195;
  ANALYSIS_TYPE_FORCES_DRAW_STALE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02729"></a>
## FND-02729: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DEVELOPS_LAST_PIECE = 190

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DEVELOPS_LAST_PIECE = 190;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7828.

```text
UARE = 187;
  ANALYSIS_TYPE_PUZZLE_HINT_FALLBACK = 188;
  ANALYSIS_TYPE_OPENS_UP_WEAK_KING = 189;
  ANALYSIS_TYPE_DEVELOPS_LAST_PIECE = 190;
  ANALYSIS_TYPE_DEVELOPS_CENTER = 191;
  ANALYSIS_TYPE_DEVELOPS_RECAPTURE = 192;
  ANALYSIS_TYPE_DEVELOPS_OPENING = 193;
  ANALYSIS_TYPE_DEVELOPS_MIDDLEGAME = 194;
  ANALYSIS_TYPE_FORCES_STALEMATE = 195;
  ANALYSIS_TYPE_FORCES_DRAW_STALEMATE_IF_CAPTURED = 196;
  ANALYSIS_TYPE_ST
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02730"></a>
## FND-02730: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DEVELOPS_CENTER = 191

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DEVELOPS_CENTER = 191;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7871.

```text
LBACK = 188;
  ANALYSIS_TYPE_OPENS_UP_WEAK_KING = 189;
  ANALYSIS_TYPE_DEVELOPS_LAST_PIECE = 190;
  ANALYSIS_TYPE_DEVELOPS_CENTER = 191;
  ANALYSIS_TYPE_DEVELOPS_RECAPTURE = 192;
  ANALYSIS_TYPE_DEVELOPS_OPENING = 193;
  ANALYSIS_TYPE_DEVELOPS_MIDDLEGAME = 194;
  ANALYSIS_TYPE_FORCES_STALEMATE = 195;
  ANALYSIS_TYPE_FORCES_DRAW_STALEMATE_IF_CAPTURED = 196;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_BLUNDERED = 197;
  ANA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02731"></a>
## FND-02731: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DEVELOPS_RECAPTURE = 192

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DEVELOPS_RECAPTURE = 192;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7910.

```text
EAK_KING = 189;
  ANALYSIS_TYPE_DEVELOPS_LAST_PIECE = 190;
  ANALYSIS_TYPE_DEVELOPS_CENTER = 191;
  ANALYSIS_TYPE_DEVELOPS_RECAPTURE = 192;
  ANALYSIS_TYPE_DEVELOPS_OPENING = 193;
  ANALYSIS_TYPE_DEVELOPS_MIDDLEGAME = 194;
  ANALYSIS_TYPE_FORCES_STALEMATE = 195;
  ANALYSIS_TYPE_FORCES_DRAW_STALEMATE_IF_CAPTURED = 196;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_BLUNDERED = 197;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_FORCE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02732"></a>
## FND-02732: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DEVELOPS_OPENING = 193

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DEVELOPS_OPENING = 193;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7952.

```text
AST_PIECE = 190;
  ANALYSIS_TYPE_DEVELOPS_CENTER = 191;
  ANALYSIS_TYPE_DEVELOPS_RECAPTURE = 192;
  ANALYSIS_TYPE_DEVELOPS_OPENING = 193;
  ANALYSIS_TYPE_DEVELOPS_MIDDLEGAME = 194;
  ANALYSIS_TYPE_FORCES_STALEMATE = 195;
  ANALYSIS_TYPE_FORCES_DRAW_STALEMATE_IF_CAPTURED = 196;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_BLUNDERED = 197;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_FORCED = 198;
  ANALYSIS_TYPE_STALEMATE_WHEN_DR
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02733"></a>
## FND-02733: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DEVELOPS_MIDDLEGAME = 194

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DEVELOPS_MIDDLEGAME = 194;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 7992.

```text
S_CENTER = 191;
  ANALYSIS_TYPE_DEVELOPS_RECAPTURE = 192;
  ANALYSIS_TYPE_DEVELOPS_OPENING = 193;
  ANALYSIS_TYPE_DEVELOPS_MIDDLEGAME = 194;
  ANALYSIS_TYPE_FORCES_STALEMATE = 195;
  ANALYSIS_TYPE_FORCES_DRAW_STALEMATE_IF_CAPTURED = 196;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_BLUNDERED = 197;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_FORCED = 198;
  ANALYSIS_TYPE_STALEMATE_WHEN_DRAWING = 199;
  ANALYSIS_TYPE_ATTACKS_PAW
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02734"></a>
## FND-02734: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORCES_STALEMATE = 195

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FORCES_STALEMATE = 195;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8035.

```text
CAPTURE = 192;
  ANALYSIS_TYPE_DEVELOPS_OPENING = 193;
  ANALYSIS_TYPE_DEVELOPS_MIDDLEGAME = 194;
  ANALYSIS_TYPE_FORCES_STALEMATE = 195;
  ANALYSIS_TYPE_FORCES_DRAW_STALEMATE_IF_CAPTURED = 196;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_BLUNDERED = 197;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_FORCED = 198;
  ANALYSIS_TYPE_STALEMATE_WHEN_DRAWING = 199;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN_COVER = 200;
  ANALYSIS_TYPE_TAKES_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02735"></a>
## FND-02735: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORCES_DRAW_STALEMATE_IF_CAPTURED = 196

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FORCES_DRAW_STALEMATE_IF_CAPTURED = 196;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8075.

```text
OPENING = 193;
  ANALYSIS_TYPE_DEVELOPS_MIDDLEGAME = 194;
  ANALYSIS_TYPE_FORCES_STALEMATE = 195;
  ANALYSIS_TYPE_FORCES_DRAW_STALEMATE_IF_CAPTURED = 196;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_BLUNDERED = 197;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_FORCED = 198;
  ANALYSIS_TYPE_STALEMATE_WHEN_DRAWING = 199;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN_COVER = 200;
  ANALYSIS_TYPE_TAKES_OUTPOST_WITH_TEMPO = 201;
  ANALYSIS_TYP
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02736"></a>
## FND-02736: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_BLUNDERED = 197

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_BLUNDERED = 197;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8132.

```text

  ANALYSIS_TYPE_FORCES_STALEMATE = 195;
  ANALYSIS_TYPE_FORCES_DRAW_STALEMATE_IF_CAPTURED = 196;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_BLUNDERED = 197;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_FORCED = 198;
  ANALYSIS_TYPE_STALEMATE_WHEN_DRAWING = 199;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN_COVER = 200;
  ANALYSIS_TYPE_TAKES_OUTPOST_WITH_TEMPO = 201;
  ANALYSIS_TYPE_TRADES_PAWNS_TO_DEFEND = 202;
  ANALYSIS_TYPE_PAWN_STOR
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02737"></a>
## FND-02737: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_FORCED = 198

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_FORCED = 198;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8188.

```text
_FORCES_DRAW_STALEMATE_IF_CAPTURED = 196;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_BLUNDERED = 197;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_FORCED = 198;
  ANALYSIS_TYPE_STALEMATE_WHEN_DRAWING = 199;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN_COVER = 200;
  ANALYSIS_TYPE_TAKES_OUTPOST_WITH_TEMPO = 201;
  ANALYSIS_TYPE_TRADES_PAWNS_TO_DEFEND = 202;
  ANALYSIS_TYPE_PAWN_STORM = 203;
  ANALYSIS_TYPE_LAUNCHES_PAWN_STORM = 204;
  AN
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02738"></a>
## FND-02738: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_STALEMATE_WHEN_DRAWING = 199

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_STALEMATE_WHEN_DRAWING = 199;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8241.

```text
TYPE_STALEMATE_WHEN_WINNING_BLUNDERED = 197;
  ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_FORCED = 198;
  ANALYSIS_TYPE_STALEMATE_WHEN_DRAWING = 199;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN_COVER = 200;
  ANALYSIS_TYPE_TAKES_OUTPOST_WITH_TEMPO = 201;
  ANALYSIS_TYPE_TRADES_PAWNS_TO_DEFEND = 202;
  ANALYSIS_TYPE_PAWN_STORM = 203;
  ANALYSIS_TYPE_LAUNCHES_PAWN_STORM = 204;
  ANALYSIS_TYPE_FIRST_MOVE_CENTER_PAWN = 205;
  ANALYSIS_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02739"></a>
## FND-02739: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN_COVER = 200

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN_COVER = 200;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8287.

```text
 ANALYSIS_TYPE_STALEMATE_WHEN_WINNING_FORCED = 198;
  ANALYSIS_TYPE_STALEMATE_WHEN_DRAWING = 199;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN_COVER = 200;
  ANALYSIS_TYPE_TAKES_OUTPOST_WITH_TEMPO = 201;
  ANALYSIS_TYPE_TRADES_PAWNS_TO_DEFEND = 202;
  ANALYSIS_TYPE_PAWN_STORM = 203;
  ANALYSIS_TYPE_LAUNCHES_PAWN_STORM = 204;
  ANALYSIS_TYPE_FIRST_MOVE_CENTER_PAWN = 205;
  ANALYSIS_TYPE_PILE_TRADE = 206;
  ANALYSIS_TYPE_OPENS_U
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02740"></a>
## FND-02740: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_TAKES_OUTPOST_WITH_TEMPO = 201

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_TAKES_OUTPOST_WITH_TEMPO = 201;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8335.

```text
98;
  ANALYSIS_TYPE_STALEMATE_WHEN_DRAWING = 199;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN_COVER = 200;
  ANALYSIS_TYPE_TAKES_OUTPOST_WITH_TEMPO = 201;
  ANALYSIS_TYPE_TRADES_PAWNS_TO_DEFEND = 202;
  ANALYSIS_TYPE_PAWN_STORM = 203;
  ANALYSIS_TYPE_LAUNCHES_PAWN_STORM = 204;
  ANALYSIS_TYPE_FIRST_MOVE_CENTER_PAWN = 205;
  ANALYSIS_TYPE_PILE_TRADE = 206;
  ANALYSIS_TYPE_OPENS_UP_SCOPE = 207;
  ANALYSIS_TYPE_FORCED = 208;
  A
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02741"></a>
## FND-02741: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_TRADES_PAWNS_TO_DEFEND = 202

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_TRADES_PAWNS_TO_DEFEND = 202;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8383.

```text
;
  ANALYSIS_TYPE_ATTACKS_PAWN_CHAIN_COVER = 200;
  ANALYSIS_TYPE_TAKES_OUTPOST_WITH_TEMPO = 201;
  ANALYSIS_TYPE_TRADES_PAWNS_TO_DEFEND = 202;
  ANALYSIS_TYPE_PAWN_STORM = 203;
  ANALYSIS_TYPE_LAUNCHES_PAWN_STORM = 204;
  ANALYSIS_TYPE_FIRST_MOVE_CENTER_PAWN = 205;
  ANALYSIS_TYPE_PILE_TRADE = 206;
  ANALYSIS_TYPE_OPENS_UP_SCOPE = 207;
  ANALYSIS_TYPE_FORCED = 208;
  ANALYSIS_TYPE_WINS_TIME_OUT_WINNING_POSITION = 20
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02742"></a>
## FND-02742: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PAWN_STORM = 203

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PAWN_STORM = 203;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8429.

```text
00;
  ANALYSIS_TYPE_TAKES_OUTPOST_WITH_TEMPO = 201;
  ANALYSIS_TYPE_TRADES_PAWNS_TO_DEFEND = 202;
  ANALYSIS_TYPE_PAWN_STORM = 203;
  ANALYSIS_TYPE_LAUNCHES_PAWN_STORM = 204;
  ANALYSIS_TYPE_FIRST_MOVE_CENTER_PAWN = 205;
  ANALYSIS_TYPE_PILE_TRADE = 206;
  ANALYSIS_TYPE_OPENS_UP_SCOPE = 207;
  ANALYSIS_TYPE_FORCED = 208;
  ANALYSIS_TYPE_WINS_TIME_OUT_WINNING_POSITION = 209;
  ANALYSIS_TYPE_WINS_TIME_OUT_LOSING_POSITI
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02743"></a>
## FND-02743: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_LAUNCHES_PAWN_STORM = 204

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_LAUNCHES_PAWN_STORM = 204;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8463.

```text
WITH_TEMPO = 201;
  ANALYSIS_TYPE_TRADES_PAWNS_TO_DEFEND = 202;
  ANALYSIS_TYPE_PAWN_STORM = 203;
  ANALYSIS_TYPE_LAUNCHES_PAWN_STORM = 204;
  ANALYSIS_TYPE_FIRST_MOVE_CENTER_PAWN = 205;
  ANALYSIS_TYPE_PILE_TRADE = 206;
  ANALYSIS_TYPE_OPENS_UP_SCOPE = 207;
  ANALYSIS_TYPE_FORCED = 208;
  ANALYSIS_TYPE_WINS_TIME_OUT_WINNING_POSITION = 209;
  ANALYSIS_TYPE_WINS_TIME_OUT_LOSING_POSITION = 210;
  ANALYSIS_TYPE_WINS_TIM
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02744"></a>
## FND-02744: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FIRST_MOVE_CENTER_PAWN = 205

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FIRST_MOVE_CENTER_PAWN = 205;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8506.

```text
WNS_TO_DEFEND = 202;
  ANALYSIS_TYPE_PAWN_STORM = 203;
  ANALYSIS_TYPE_LAUNCHES_PAWN_STORM = 204;
  ANALYSIS_TYPE_FIRST_MOVE_CENTER_PAWN = 205;
  ANALYSIS_TYPE_PILE_TRADE = 206;
  ANALYSIS_TYPE_OPENS_UP_SCOPE = 207;
  ANALYSIS_TYPE_FORCED = 208;
  ANALYSIS_TYPE_WINS_TIME_OUT_WINNING_POSITION = 209;
  ANALYSIS_TYPE_WINS_TIME_OUT_LOSING_POSITION = 210;
  ANALYSIS_TYPE_WINS_TIME_OUT_EQUAL_POSITION = 211;
  ANALYSIS_TYPE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02745"></a>
## FND-02745: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PILE_TRADE = 206

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PILE_TRADE = 206;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8552.

```text
M = 203;
  ANALYSIS_TYPE_LAUNCHES_PAWN_STORM = 204;
  ANALYSIS_TYPE_FIRST_MOVE_CENTER_PAWN = 205;
  ANALYSIS_TYPE_PILE_TRADE = 206;
  ANALYSIS_TYPE_OPENS_UP_SCOPE = 207;
  ANALYSIS_TYPE_FORCED = 208;
  ANALYSIS_TYPE_WINS_TIME_OUT_WINNING_POSITION = 209;
  ANALYSIS_TYPE_WINS_TIME_OUT_LOSING_POSITION = 210;
  ANALYSIS_TYPE_WINS_TIME_OUT_EQUAL_POSITION = 211;
  ANALYSIS_TYPE_ELIMINATES_OPPONENT_PASSED_PAWN = 212;
  ANAL
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02746"></a>
## FND-02746: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_OPENS_UP_SCOPE = 207

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_OPENS_UP_SCOPE = 207;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8586.

```text
PAWN_STORM = 204;
  ANALYSIS_TYPE_FIRST_MOVE_CENTER_PAWN = 205;
  ANALYSIS_TYPE_PILE_TRADE = 206;
  ANALYSIS_TYPE_OPENS_UP_SCOPE = 207;
  ANALYSIS_TYPE_FORCED = 208;
  ANALYSIS_TYPE_WINS_TIME_OUT_WINNING_POSITION = 209;
  ANALYSIS_TYPE_WINS_TIME_OUT_LOSING_POSITION = 210;
  ANALYSIS_TYPE_WINS_TIME_OUT_EQUAL_POSITION = 211;
  ANALYSIS_TYPE_ELIMINATES_OPPONENT_PASSED_PAWN = 212;
  ANALYSIS_TYPE_CREATES_KING_FLIGHT_SQUA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02747"></a>
## FND-02747: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORCED = 208

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FORCED = 208;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8624.

```text
T_MOVE_CENTER_PAWN = 205;
  ANALYSIS_TYPE_PILE_TRADE = 206;
  ANALYSIS_TYPE_OPENS_UP_SCOPE = 207;
  ANALYSIS_TYPE_FORCED = 208;
  ANALYSIS_TYPE_WINS_TIME_OUT_WINNING_POSITION = 209;
  ANALYSIS_TYPE_WINS_TIME_OUT_LOSING_POSITION = 210;
  ANALYSIS_TYPE_WINS_TIME_OUT_EQUAL_POSITION = 211;
  ANALYSIS_TYPE_ELIMINATES_OPPONENT_PASSED_PAWN = 212;
  ANALYSIS_TYPE_CREATES_KING_FLIGHT_SQUARE = 213;
  ANALYSIS_TYPE_VACATES_PUSH
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02748"></a>
## FND-02748: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WINS_TIME_OUT_WINNING_POSITION = 209

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_WINS_TIME_OUT_WINNING_POSITION = 209;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8654.

```text
ALYSIS_TYPE_PILE_TRADE = 206;
  ANALYSIS_TYPE_OPENS_UP_SCOPE = 207;
  ANALYSIS_TYPE_FORCED = 208;
  ANALYSIS_TYPE_WINS_TIME_OUT_WINNING_POSITION = 209;
  ANALYSIS_TYPE_WINS_TIME_OUT_LOSING_POSITION = 210;
  ANALYSIS_TYPE_WINS_TIME_OUT_EQUAL_POSITION = 211;
  ANALYSIS_TYPE_ELIMINATES_OPPONENT_PASSED_PAWN = 212;
  ANALYSIS_TYPE_CREATES_KING_FLIGHT_SQUARE = 213;
  ANALYSIS_TYPE_VACATES_PUSHING_SQUARE = 214;
  ANALYSIS_T
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02749"></a>
## FND-02749: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WINS_TIME_OUT_LOSING_POSITION = 210

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_WINS_TIME_OUT_LOSING_POSITION = 210;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8708.

```text
_SCOPE = 207;
  ANALYSIS_TYPE_FORCED = 208;
  ANALYSIS_TYPE_WINS_TIME_OUT_WINNING_POSITION = 209;
  ANALYSIS_TYPE_WINS_TIME_OUT_LOSING_POSITION = 210;
  ANALYSIS_TYPE_WINS_TIME_OUT_EQUAL_POSITION = 211;
  ANALYSIS_TYPE_ELIMINATES_OPPONENT_PASSED_PAWN = 212;
  ANALYSIS_TYPE_CREATES_KING_FLIGHT_SQUARE = 213;
  ANALYSIS_TYPE_VACATES_PUSHING_SQUARE = 214;
  ANALYSIS_TYPE_BLOCKADE_MOVING_PAWN = 215;
  ANALYSIS_TYPE_PICK_U
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02750"></a>
## FND-02750: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WINS_TIME_OUT_EQUAL_POSITION = 211

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_WINS_TIME_OUT_EQUAL_POSITION = 211;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8761.

```text
S_TYPE_WINS_TIME_OUT_WINNING_POSITION = 209;
  ANALYSIS_TYPE_WINS_TIME_OUT_LOSING_POSITION = 210;
  ANALYSIS_TYPE_WINS_TIME_OUT_EQUAL_POSITION = 211;
  ANALYSIS_TYPE_ELIMINATES_OPPONENT_PASSED_PAWN = 212;
  ANALYSIS_TYPE_CREATES_KING_FLIGHT_SQUARE = 213;
  ANALYSIS_TYPE_VACATES_PUSHING_SQUARE = 214;
  ANALYSIS_TYPE_BLOCKADE_MOVING_PAWN = 215;
  ANALYSIS_TYPE_PICK_UP_PIECE_IN_TACTIC = 216;
  ANALYSIS_TYPE_CONTROLS_OPP
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02751"></a>
## FND-02751: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ELIMINATES_OPPONENT_PASSED_PAWN = 212

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_ELIMINATES_OPPONENT_PASSED_PAWN = 212;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8813.

```text
SIS_TYPE_WINS_TIME_OUT_LOSING_POSITION = 210;
  ANALYSIS_TYPE_WINS_TIME_OUT_EQUAL_POSITION = 211;
  ANALYSIS_TYPE_ELIMINATES_OPPONENT_PASSED_PAWN = 212;
  ANALYSIS_TYPE_CREATES_KING_FLIGHT_SQUARE = 213;
  ANALYSIS_TYPE_VACATES_PUSHING_SQUARE = 214;
  ANALYSIS_TYPE_BLOCKADE_MOVING_PAWN = 215;
  ANALYSIS_TYPE_PICK_UP_PIECE_IN_TACTIC = 216;
  ANALYSIS_TYPE_CONTROLS_OPPONENT_PROMOTION_SQUARE = 217;
  ANALYSIS_TYPE_PROTEC
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02752"></a>
## FND-02752: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CREATES_KING_FLIGHT_SQUARE = 213

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CREATES_KING_FLIGHT_SQUARE = 213;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8868.

```text
S_TYPE_WINS_TIME_OUT_EQUAL_POSITION = 211;
  ANALYSIS_TYPE_ELIMINATES_OPPONENT_PASSED_PAWN = 212;
  ANALYSIS_TYPE_CREATES_KING_FLIGHT_SQUARE = 213;
  ANALYSIS_TYPE_VACATES_PUSHING_SQUARE = 214;
  ANALYSIS_TYPE_BLOCKADE_MOVING_PAWN = 215;
  ANALYSIS_TYPE_PICK_UP_PIECE_IN_TACTIC = 216;
  ANALYSIS_TYPE_CONTROLS_OPPONENT_PROMOTION_SQUARE = 217;
  ANALYSIS_TYPE_PROTECTS_PASSED_PAWN = 218;
  ANALYSIS_TYPE_BLOCKADES_OPPONEN
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02753"></a>
## FND-02753: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_VACATES_PUSHING_SQUARE = 214

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_VACATES_PUSHING_SQUARE = 214;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8918.

```text
SIS_TYPE_ELIMINATES_OPPONENT_PASSED_PAWN = 212;
  ANALYSIS_TYPE_CREATES_KING_FLIGHT_SQUARE = 213;
  ANALYSIS_TYPE_VACATES_PUSHING_SQUARE = 214;
  ANALYSIS_TYPE_BLOCKADE_MOVING_PAWN = 215;
  ANALYSIS_TYPE_PICK_UP_PIECE_IN_TACTIC = 216;
  ANALYSIS_TYPE_CONTROLS_OPPONENT_PROMOTION_SQUARE = 217;
  ANALYSIS_TYPE_PROTECTS_PASSED_PAWN = 218;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PROMOTION_SQUARE = 219;
  ANALYSIS_TYPE_CONTROLS
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02754"></a>
## FND-02754: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BLOCKADE_MOVING_PAWN = 215

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BLOCKADE_MOVING_PAWN = 215;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 8964.

```text
;
  ANALYSIS_TYPE_CREATES_KING_FLIGHT_SQUARE = 213;
  ANALYSIS_TYPE_VACATES_PUSHING_SQUARE = 214;
  ANALYSIS_TYPE_BLOCKADE_MOVING_PAWN = 215;
  ANALYSIS_TYPE_PICK_UP_PIECE_IN_TACTIC = 216;
  ANALYSIS_TYPE_CONTROLS_OPPONENT_PROMOTION_SQUARE = 217;
  ANALYSIS_TYPE_PROTECTS_PASSED_PAWN = 218;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PROMOTION_SQUARE = 219;
  ANALYSIS_TYPE_CONTROLS_OPP_PUSHING_SQUARE = 220;
  ANALYSIS_TYPE_BLO
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02755"></a>
## FND-02755: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PICK_UP_PIECE_IN_TACTIC = 216

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PICK_UP_PIECE_IN_TACTIC = 216;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9008.

```text
 = 213;
  ANALYSIS_TYPE_VACATES_PUSHING_SQUARE = 214;
  ANALYSIS_TYPE_BLOCKADE_MOVING_PAWN = 215;
  ANALYSIS_TYPE_PICK_UP_PIECE_IN_TACTIC = 216;
  ANALYSIS_TYPE_CONTROLS_OPPONENT_PROMOTION_SQUARE = 217;
  ANALYSIS_TYPE_PROTECTS_PASSED_PAWN = 218;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PROMOTION_SQUARE = 219;
  ANALYSIS_TYPE_CONTROLS_OPP_PUSHING_SQUARE = 220;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PUSHING_SQUARE = 221;
  ANAL
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02756"></a>
## FND-02756: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CONTROLS_OPPONENT_PROMOTION_SQUARE = 217

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CONTROLS_OPPONENT_PROMOTION_SQUARE = 217;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9055.

```text
= 214;
  ANALYSIS_TYPE_BLOCKADE_MOVING_PAWN = 215;
  ANALYSIS_TYPE_PICK_UP_PIECE_IN_TACTIC = 216;
  ANALYSIS_TYPE_CONTROLS_OPPONENT_PROMOTION_SQUARE = 217;
  ANALYSIS_TYPE_PROTECTS_PASSED_PAWN = 218;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PROMOTION_SQUARE = 219;
  ANALYSIS_TYPE_CONTROLS_OPP_PUSHING_SQUARE = 220;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PUSHING_SQUARE = 221;
  ANALYSIS_TYPE_GOOD_TRADE = 222;
  ANALYSIS_TYPE_BLO
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02757"></a>
## FND-02757: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PROTECTS_PASSED_PAWN = 218

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PROTECTS_PASSED_PAWN = 218;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9113.

```text
SIS_TYPE_PICK_UP_PIECE_IN_TACTIC = 216;
  ANALYSIS_TYPE_CONTROLS_OPPONENT_PROMOTION_SQUARE = 217;
  ANALYSIS_TYPE_PROTECTS_PASSED_PAWN = 218;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PROMOTION_SQUARE = 219;
  ANALYSIS_TYPE_CONTROLS_OPP_PUSHING_SQUARE = 220;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PUSHING_SQUARE = 221;
  ANALYSIS_TYPE_GOOD_TRADE = 222;
  ANALYSIS_TYPE_BLOCKS_CENTRAL_PAWN = 223;
  ANALYSIS_TYPE_NEVER_PLAY_F3 = 22
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02758"></a>
## FND-02758: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BLOCKADES_OPPONENT_PROMOTION_SQUARE = 219

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BLOCKADES_OPPONENT_PROMOTION_SQUARE = 219;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9157.

```text
ALYSIS_TYPE_CONTROLS_OPPONENT_PROMOTION_SQUARE = 217;
  ANALYSIS_TYPE_PROTECTS_PASSED_PAWN = 218;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PROMOTION_SQUARE = 219;
  ANALYSIS_TYPE_CONTROLS_OPP_PUSHING_SQUARE = 220;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PUSHING_SQUARE = 221;
  ANALYSIS_TYPE_GOOD_TRADE = 222;
  ANALYSIS_TYPE_BLOCKS_CENTRAL_PAWN = 223;
  ANALYSIS_TYPE_NEVER_PLAY_F3 = 224;
  ANALYSIS_TYPE_IGNORES_ATTACKED_PIECE = 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02759"></a>
## FND-02759: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CONTROLS_OPP_PUSHING_SQUARE = 220

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CONTROLS_OPP_PUSHING_SQUARE = 220;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9216.

```text
LYSIS_TYPE_PROTECTS_PASSED_PAWN = 218;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PROMOTION_SQUARE = 219;
  ANALYSIS_TYPE_CONTROLS_OPP_PUSHING_SQUARE = 220;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PUSHING_SQUARE = 221;
  ANALYSIS_TYPE_GOOD_TRADE = 222;
  ANALYSIS_TYPE_BLOCKS_CENTRAL_PAWN = 223;
  ANALYSIS_TYPE_NEVER_PLAY_F3 = 224;
  ANALYSIS_TYPE_IGNORES_ATTACKED_PIECE = 225;
  ANALYSIS_TYPE_DID_NOT_RECAPTURE = 226;
  ANALYSIS_TY
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02760"></a>
## FND-02760: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BLOCKADES_OPPONENT_PUSHING_SQUARE = 221

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BLOCKADES_OPPONENT_PUSHING_SQUARE = 221;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9267.

```text
YPE_BLOCKADES_OPPONENT_PROMOTION_SQUARE = 219;
  ANALYSIS_TYPE_CONTROLS_OPP_PUSHING_SQUARE = 220;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PUSHING_SQUARE = 221;
  ANALYSIS_TYPE_GOOD_TRADE = 222;
  ANALYSIS_TYPE_BLOCKS_CENTRAL_PAWN = 223;
  ANALYSIS_TYPE_NEVER_PLAY_F3 = 224;
  ANALYSIS_TYPE_IGNORES_ATTACKED_PIECE = 225;
  ANALYSIS_TYPE_DID_NOT_RECAPTURE = 226;
  ANALYSIS_TYPE_PUTS_PAWN_IN_CENTER = 227;
  ANALYSIS_TYPE_PREPA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02761"></a>
## FND-02761: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_GOOD_TRADE = 222

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_GOOD_TRADE = 222;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9324.

```text
_TYPE_CONTROLS_OPP_PUSHING_SQUARE = 220;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PUSHING_SQUARE = 221;
  ANALYSIS_TYPE_GOOD_TRADE = 222;
  ANALYSIS_TYPE_BLOCKS_CENTRAL_PAWN = 223;
  ANALYSIS_TYPE_NEVER_PLAY_F3 = 224;
  ANALYSIS_TYPE_IGNORES_ATTACKED_PIECE = 225;
  ANALYSIS_TYPE_DID_NOT_RECAPTURE = 226;
  ANALYSIS_TYPE_PUTS_PAWN_IN_CENTER = 227;
  ANALYSIS_TYPE_PREPARES_CENTRAL_PUSH = 228;
  ANALYSIS_TYPE_MOVES_PINNED_PIEC
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02762"></a>
## FND-02762: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BLOCKS_CENTRAL_PAWN = 223

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BLOCKS_CENTRAL_PAWN = 223;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9358.

```text
= 220;
  ANALYSIS_TYPE_BLOCKADES_OPPONENT_PUSHING_SQUARE = 221;
  ANALYSIS_TYPE_GOOD_TRADE = 222;
  ANALYSIS_TYPE_BLOCKS_CENTRAL_PAWN = 223;
  ANALYSIS_TYPE_NEVER_PLAY_F3 = 224;
  ANALYSIS_TYPE_IGNORES_ATTACKED_PIECE = 225;
  ANALYSIS_TYPE_DID_NOT_RECAPTURE = 226;
  ANALYSIS_TYPE_PUTS_PAWN_IN_CENTER = 227;
  ANALYSIS_TYPE_PREPARES_CENTRAL_PUSH = 228;
  ANALYSIS_TYPE_MOVES_PINNED_PIECE = 229;
  ANALYSIS_TYPE_PREVENTS_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02763"></a>
## FND-02763: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_NEVER_PLAY_F3 = 224

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_NEVER_PLAY_F3 = 224;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9401.

```text
USHING_SQUARE = 221;
  ANALYSIS_TYPE_GOOD_TRADE = 222;
  ANALYSIS_TYPE_BLOCKS_CENTRAL_PAWN = 223;
  ANALYSIS_TYPE_NEVER_PLAY_F3 = 224;
  ANALYSIS_TYPE_IGNORES_ATTACKED_PIECE = 225;
  ANALYSIS_TYPE_DID_NOT_RECAPTURE = 226;
  ANALYSIS_TYPE_PUTS_PAWN_IN_CENTER = 227;
  ANALYSIS_TYPE_PREPARES_CENTRAL_PUSH = 228;
  ANALYSIS_TYPE_MOVES_PINNED_PIECE = 229;
  ANALYSIS_TYPE_PREVENTS_CENTRAL_BREAK = 230;
  ANALYSIS_TYPE_REMOVE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02764"></a>
## FND-02764: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_IGNORES_ATTACKED_PIECE = 225

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_IGNORES_ATTACKED_PIECE = 225;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9438.

```text
GOOD_TRADE = 222;
  ANALYSIS_TYPE_BLOCKS_CENTRAL_PAWN = 223;
  ANALYSIS_TYPE_NEVER_PLAY_F3 = 224;
  ANALYSIS_TYPE_IGNORES_ATTACKED_PIECE = 225;
  ANALYSIS_TYPE_DID_NOT_RECAPTURE = 226;
  ANALYSIS_TYPE_PUTS_PAWN_IN_CENTER = 227;
  ANALYSIS_TYPE_PREPARES_CENTRAL_PUSH = 228;
  ANALYSIS_TYPE_MOVES_PINNED_PIECE = 229;
  ANALYSIS_TYPE_PREVENTS_CENTRAL_BREAK = 230;
  ANALYSIS_TYPE_REMOVES_OWN_DEFENDER = 231;
  ANALYSIS_TYPE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02765"></a>
## FND-02765: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DID_NOT_RECAPTURE = 226

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DID_NOT_RECAPTURE = 226;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9484.

```text
AL_PAWN = 223;
  ANALYSIS_TYPE_NEVER_PLAY_F3 = 224;
  ANALYSIS_TYPE_IGNORES_ATTACKED_PIECE = 225;
  ANALYSIS_TYPE_DID_NOT_RECAPTURE = 226;
  ANALYSIS_TYPE_PUTS_PAWN_IN_CENTER = 227;
  ANALYSIS_TYPE_PREPARES_CENTRAL_PUSH = 228;
  ANALYSIS_TYPE_MOVES_PINNED_PIECE = 229;
  ANALYSIS_TYPE_PREVENTS_CENTRAL_BREAK = 230;
  ANALYSIS_TYPE_REMOVES_OWN_DEFENDER = 231;
  ANALYSIS_TYPE_RECAPTURES_TOWARD_CENTER = 232;
  ANALYSIS_TY
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02766"></a>
## FND-02766: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PUTS_PAWN_IN_CENTER = 227

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PUTS_PAWN_IN_CENTER = 227;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9525.

```text
_F3 = 224;
  ANALYSIS_TYPE_IGNORES_ATTACKED_PIECE = 225;
  ANALYSIS_TYPE_DID_NOT_RECAPTURE = 226;
  ANALYSIS_TYPE_PUTS_PAWN_IN_CENTER = 227;
  ANALYSIS_TYPE_PREPARES_CENTRAL_PUSH = 228;
  ANALYSIS_TYPE_MOVES_PINNED_PIECE = 229;
  ANALYSIS_TYPE_PREVENTS_CENTRAL_BREAK = 230;
  ANALYSIS_TYPE_REMOVES_OWN_DEFENDER = 231;
  ANALYSIS_TYPE_RECAPTURES_TOWARD_CENTER = 232;
  ANALYSIS_TYPE_TOO_EARLY_QUEEN_DEVELOPMENT = 233;
  A
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02767"></a>
## FND-02767: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PREPARES_CENTRAL_PUSH = 228

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PREPARES_CENTRAL_PUSH = 228;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9568.

```text
_PIECE = 225;
  ANALYSIS_TYPE_DID_NOT_RECAPTURE = 226;
  ANALYSIS_TYPE_PUTS_PAWN_IN_CENTER = 227;
  ANALYSIS_TYPE_PREPARES_CENTRAL_PUSH = 228;
  ANALYSIS_TYPE_MOVES_PINNED_PIECE = 229;
  ANALYSIS_TYPE_PREVENTS_CENTRAL_BREAK = 230;
  ANALYSIS_TYPE_REMOVES_OWN_DEFENDER = 231;
  ANALYSIS_TYPE_RECAPTURES_TOWARD_CENTER = 232;
  ANALYSIS_TYPE_TOO_EARLY_QUEEN_DEVELOPMENT = 233;
  ANALYSIS_TYPE_CENTRAL_BREAK = 234;
  ANALYSI
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02768"></a>
## FND-02768: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MOVES_PINNED_PIECE = 229

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_MOVES_PINNED_PIECE = 229;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9613.

```text
RE = 226;
  ANALYSIS_TYPE_PUTS_PAWN_IN_CENTER = 227;
  ANALYSIS_TYPE_PREPARES_CENTRAL_PUSH = 228;
  ANALYSIS_TYPE_MOVES_PINNED_PIECE = 229;
  ANALYSIS_TYPE_PREVENTS_CENTRAL_BREAK = 230;
  ANALYSIS_TYPE_REMOVES_OWN_DEFENDER = 231;
  ANALYSIS_TYPE_RECAPTURES_TOWARD_CENTER = 232;
  ANALYSIS_TYPE_TOO_EARLY_QUEEN_DEVELOPMENT = 233;
  ANALYSIS_TYPE_CENTRAL_BREAK = 234;
  ANALYSIS_TYPE_HANGS_PIECE = 235;
  ANALYSIS_TYPE_FRE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02769"></a>
## FND-02769: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PREVENTS_CENTRAL_BREAK = 230

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PREVENTS_CENTRAL_BREAK = 230;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9655.

```text
TER = 227;
  ANALYSIS_TYPE_PREPARES_CENTRAL_PUSH = 228;
  ANALYSIS_TYPE_MOVES_PINNED_PIECE = 229;
  ANALYSIS_TYPE_PREVENTS_CENTRAL_BREAK = 230;
  ANALYSIS_TYPE_REMOVES_OWN_DEFENDER = 231;
  ANALYSIS_TYPE_RECAPTURES_TOWARD_CENTER = 232;
  ANALYSIS_TYPE_TOO_EARLY_QUEEN_DEVELOPMENT = 233;
  ANALYSIS_TYPE_CENTRAL_BREAK = 234;
  ANALYSIS_TYPE_HANGS_PIECE = 235;
  ANALYSIS_TYPE_FREE_PIECE_FROM_DISTANCE = 236;
  ANALYSIS_TY
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02770"></a>
## FND-02770: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_REMOVES_OWN_DEFENDER = 231

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_REMOVES_OWN_DEFENDER = 231;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9701.

```text
SH = 228;
  ANALYSIS_TYPE_MOVES_PINNED_PIECE = 229;
  ANALYSIS_TYPE_PREVENTS_CENTRAL_BREAK = 230;
  ANALYSIS_TYPE_REMOVES_OWN_DEFENDER = 231;
  ANALYSIS_TYPE_RECAPTURES_TOWARD_CENTER = 232;
  ANALYSIS_TYPE_TOO_EARLY_QUEEN_DEVELOPMENT = 233;
  ANALYSIS_TYPE_CENTRAL_BREAK = 234;
  ANALYSIS_TYPE_HANGS_PIECE = 235;
  ANALYSIS_TYPE_FREE_PIECE_FROM_DISTANCE = 236;
  ANALYSIS_TYPE_ESCAPES_THREAT = 237;
  ANALYSIS_TYPE_TEMPO
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02771"></a>
## FND-02771: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_RECAPTURES_TOWARD_CENTER = 232

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_RECAPTURES_TOWARD_CENTER = 232;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9745.

```text
 = 229;
  ANALYSIS_TYPE_PREVENTS_CENTRAL_BREAK = 230;
  ANALYSIS_TYPE_REMOVES_OWN_DEFENDER = 231;
  ANALYSIS_TYPE_RECAPTURES_TOWARD_CENTER = 232;
  ANALYSIS_TYPE_TOO_EARLY_QUEEN_DEVELOPMENT = 233;
  ANALYSIS_TYPE_CENTRAL_BREAK = 234;
  ANALYSIS_TYPE_HANGS_PIECE = 235;
  ANALYSIS_TYPE_FREE_PIECE_FROM_DISTANCE = 236;
  ANALYSIS_TYPE_ESCAPES_THREAT = 237;
  ANALYSIS_TYPE_TEMPO_BEFORE_FREE_PIECE = 238;
  ANALYSIS_TYPE_CR
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02772"></a>
## FND-02772: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_TOO_EARLY_QUEEN_DEVELOPMENT = 233

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_TOO_EARLY_QUEEN_DEVELOPMENT = 233;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9793.

```text
 230;
  ANALYSIS_TYPE_REMOVES_OWN_DEFENDER = 231;
  ANALYSIS_TYPE_RECAPTURES_TOWARD_CENTER = 232;
  ANALYSIS_TYPE_TOO_EARLY_QUEEN_DEVELOPMENT = 233;
  ANALYSIS_TYPE_CENTRAL_BREAK = 234;
  ANALYSIS_TYPE_HANGS_PIECE = 235;
  ANALYSIS_TYPE_FREE_PIECE_FROM_DISTANCE = 236;
  ANALYSIS_TYPE_ESCAPES_THREAT = 237;
  ANALYSIS_TYPE_TEMPO_BEFORE_FREE_PIECE = 238;
  ANALYSIS_TYPE_CREATES_BATTERY = 239;
  ANALYSIS_TYPE_TAKES_OPPOS
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02773"></a>
## FND-02773: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CENTRAL_BREAK = 234

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CENTRAL_BREAK = 234;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9844.

```text
 ANALYSIS_TYPE_RECAPTURES_TOWARD_CENTER = 232;
  ANALYSIS_TYPE_TOO_EARLY_QUEEN_DEVELOPMENT = 233;
  ANALYSIS_TYPE_CENTRAL_BREAK = 234;
  ANALYSIS_TYPE_HANGS_PIECE = 235;
  ANALYSIS_TYPE_FREE_PIECE_FROM_DISTANCE = 236;
  ANALYSIS_TYPE_ESCAPES_THREAT = 237;
  ANALYSIS_TYPE_TEMPO_BEFORE_FREE_PIECE = 238;
  ANALYSIS_TYPE_CREATES_BATTERY = 239;
  ANALYSIS_TYPE_TAKES_OPPOSITION = 240;
  ANALYSIS_TYPE_ROYAL_FORK = 241;
  AN
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02774"></a>
## FND-02774: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_HANGS_PIECE = 235

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_HANGS_PIECE = 235;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 9881.

```text
ER = 232;
  ANALYSIS_TYPE_TOO_EARLY_QUEEN_DEVELOPMENT = 233;
  ANALYSIS_TYPE_CENTRAL_BREAK = 234;
  ANALYSIS_TYPE_HANGS_PIECE = 235;
  ANALYSIS_TYPE_FREE_PIECE_FROM_DISTANCE = 236;
  ANALYSIS_TYPE_ESCAPES_THREAT = 237;
  ANALYSIS_TYPE_TEMPO_BEFORE_FREE_PIECE = 238;
  ANALYSIS_TYPE_CREATES_BATTERY = 239;
  ANALYSIS_TYPE_TAKES_OPPOSITION = 240;
  ANALYSIS_TYPE_ROYAL_FORK = 241;
  ANALYSIS_TYPE_PREPARES_TO_CASTLE_KINGSI
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
