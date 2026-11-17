# data_models — findings 2301–2400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-02575"></a>
## FND-02575: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS = 33;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1301.

```text
CE = 30;
  ANALYSIS_TYPE_THREATENS_PINNED = 31;
  ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS = 32;
  ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS = 33;
  ANALYSIS_TYPE_FORCES_ISOLATED_PAWN = 34;
  ANALYSIS_TYPE_EQUAL_TRADE = 35;
  ANALYSIS_TYPE_IMMEDIATE_RECAPTURE = 36;
  ANALYSIS_TYPE_OBVIOUS_RECAPTURE = 37;
  ANALYSIS_TYPE_CAPTURES_CHECKER = 38;
  ANALYSIS_TYPE_COUNTER_THREAT = 39;
  ANALYSIS_TYPE_REMOVES_ATTACKER = 40;
  ANA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02576"></a>
## FND-02576: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORCES_ISOLATED_PAWN = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FORCES_ISOLATED_PAWN = 34;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1344.

```text
 31;
  ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS = 32;
  ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS = 33;
  ANALYSIS_TYPE_FORCES_ISOLATED_PAWN = 34;
  ANALYSIS_TYPE_EQUAL_TRADE = 35;
  ANALYSIS_TYPE_IMMEDIATE_RECAPTURE = 36;
  ANALYSIS_TYPE_OBVIOUS_RECAPTURE = 37;
  ANALYSIS_TYPE_CAPTURES_CHECKER = 38;
  ANALYSIS_TYPE_COUNTER_THREAT = 39;
  ANALYSIS_TYPE_REMOVES_ATTACKER = 40;
  ANALYSIS_TYPE_BLOCKS_ATTACKER = 41;
  ANALYSIS
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02577"></a>
## FND-02577: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_EQUAL_TRADE = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_EQUAL_TRADE = 35;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1387.

```text
PAWNS = 32;
  ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS = 33;
  ANALYSIS_TYPE_FORCES_ISOLATED_PAWN = 34;
  ANALYSIS_TYPE_EQUAL_TRADE = 35;
  ANALYSIS_TYPE_IMMEDIATE_RECAPTURE = 36;
  ANALYSIS_TYPE_OBVIOUS_RECAPTURE = 37;
  ANALYSIS_TYPE_CAPTURES_CHECKER = 38;
  ANALYSIS_TYPE_COUNTER_THREAT = 39;
  ANALYSIS_TYPE_REMOVES_ATTACKER = 40;
  ANALYSIS_TYPE_BLOCKS_ATTACKER = 41;
  ANALYSIS_TYPE_UNPINS_DEFENDER = 42;
  ANALYSIS_TYPE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02578"></a>
## FND-02578: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_IMMEDIATE_RECAPTURE = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_IMMEDIATE_RECAPTURE = 36;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1421.

```text
_DOUBLED_PAWNS = 33;
  ANALYSIS_TYPE_FORCES_ISOLATED_PAWN = 34;
  ANALYSIS_TYPE_EQUAL_TRADE = 35;
  ANALYSIS_TYPE_IMMEDIATE_RECAPTURE = 36;
  ANALYSIS_TYPE_OBVIOUS_RECAPTURE = 37;
  ANALYSIS_TYPE_CAPTURES_CHECKER = 38;
  ANALYSIS_TYPE_COUNTER_THREAT = 39;
  ANALYSIS_TYPE_REMOVES_ATTACKER = 40;
  ANALYSIS_TYPE_BLOCKS_ATTACKER = 41;
  ANALYSIS_TYPE_UNPINS_DEFENDER = 42;
  ANALYSIS_TYPE_PINS_ATTACKER = 43;
  ANALYSIS_TY
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02579"></a>
## FND-02579: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_OBVIOUS_RECAPTURE = 37

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_OBVIOUS_RECAPTURE = 37;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1463.

```text
S_ISOLATED_PAWN = 34;
  ANALYSIS_TYPE_EQUAL_TRADE = 35;
  ANALYSIS_TYPE_IMMEDIATE_RECAPTURE = 36;
  ANALYSIS_TYPE_OBVIOUS_RECAPTURE = 37;
  ANALYSIS_TYPE_CAPTURES_CHECKER = 38;
  ANALYSIS_TYPE_COUNTER_THREAT = 39;
  ANALYSIS_TYPE_REMOVES_ATTACKER = 40;
  ANALYSIS_TYPE_BLOCKS_ATTACKER = 41;
  ANALYSIS_TYPE_UNPINS_DEFENDER = 42;
  ANALYSIS_TYPE_PINS_ATTACKER = 43;
  ANALYSIS_TYPE_PIN = 44;
  ANALYSIS_TYPE_RELATIVE_PIN 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02580"></a>
## FND-02580: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CAPTURES_CHECKER = 38

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CAPTURES_CHECKER = 38;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1503.

```text
UAL_TRADE = 35;
  ANALYSIS_TYPE_IMMEDIATE_RECAPTURE = 36;
  ANALYSIS_TYPE_OBVIOUS_RECAPTURE = 37;
  ANALYSIS_TYPE_CAPTURES_CHECKER = 38;
  ANALYSIS_TYPE_COUNTER_THREAT = 39;
  ANALYSIS_TYPE_REMOVES_ATTACKER = 40;
  ANALYSIS_TYPE_BLOCKS_ATTACKER = 41;
  ANALYSIS_TYPE_UNPINS_DEFENDER = 42;
  ANALYSIS_TYPE_PINS_ATTACKER = 43;
  ANALYSIS_TYPE_PIN = 44;
  ANALYSIS_TYPE_RELATIVE_PIN = 45;
  ANALYSIS_TYPE_PROTECTS_PIECE = 4
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02581"></a>
## FND-02581: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_COUNTER_THREAT = 39

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_COUNTER_THREAT = 39;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1542.

```text
TE_RECAPTURE = 36;
  ANALYSIS_TYPE_OBVIOUS_RECAPTURE = 37;
  ANALYSIS_TYPE_CAPTURES_CHECKER = 38;
  ANALYSIS_TYPE_COUNTER_THREAT = 39;
  ANALYSIS_TYPE_REMOVES_ATTACKER = 40;
  ANALYSIS_TYPE_BLOCKS_ATTACKER = 41;
  ANALYSIS_TYPE_UNPINS_DEFENDER = 42;
  ANALYSIS_TYPE_PINS_ATTACKER = 43;
  ANALYSIS_TYPE_PIN = 44;
  ANALYSIS_TYPE_RELATIVE_PIN = 45;
  ANALYSIS_TYPE_PROTECTS_PIECE = 46;
  ANALYSIS_TYPE_DEFENDS_PIECE = 47;

```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02582"></a>
## FND-02582: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_REMOVES_ATTACKER = 40

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_REMOVES_ATTACKER = 40;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1579.

```text
VIOUS_RECAPTURE = 37;
  ANALYSIS_TYPE_CAPTURES_CHECKER = 38;
  ANALYSIS_TYPE_COUNTER_THREAT = 39;
  ANALYSIS_TYPE_REMOVES_ATTACKER = 40;
  ANALYSIS_TYPE_BLOCKS_ATTACKER = 41;
  ANALYSIS_TYPE_UNPINS_DEFENDER = 42;
  ANALYSIS_TYPE_PINS_ATTACKER = 43;
  ANALYSIS_TYPE_PIN = 44;
  ANALYSIS_TYPE_RELATIVE_PIN = 45;
  ANALYSIS_TYPE_PROTECTS_PIECE = 46;
  ANALYSIS_TYPE_DEFENDS_PIECE = 47;
  ANALYSIS_TYPE_CREATES_LUFT = 48;
  
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02583"></a>
## FND-02583: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BLOCKS_ATTACKER = 41

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BLOCKS_ATTACKER = 41;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1618.

```text
APTURES_CHECKER = 38;
  ANALYSIS_TYPE_COUNTER_THREAT = 39;
  ANALYSIS_TYPE_REMOVES_ATTACKER = 40;
  ANALYSIS_TYPE_BLOCKS_ATTACKER = 41;
  ANALYSIS_TYPE_UNPINS_DEFENDER = 42;
  ANALYSIS_TYPE_PINS_ATTACKER = 43;
  ANALYSIS_TYPE_PIN = 44;
  ANALYSIS_TYPE_RELATIVE_PIN = 45;
  ANALYSIS_TYPE_PROTECTS_PIECE = 46;
  ANALYSIS_TYPE_DEFENDS_PIECE = 47;
  ANALYSIS_TYPE_CREATES_LUFT = 48;
  ANALYSIS_TYPE_GAMBITS_PAWN = 49;
  ANAL
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02584"></a>
## FND-02584: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_UNPINS_DEFENDER = 42

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_UNPINS_DEFENDER = 42;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1656.

```text
COUNTER_THREAT = 39;
  ANALYSIS_TYPE_REMOVES_ATTACKER = 40;
  ANALYSIS_TYPE_BLOCKS_ATTACKER = 41;
  ANALYSIS_TYPE_UNPINS_DEFENDER = 42;
  ANALYSIS_TYPE_PINS_ATTACKER = 43;
  ANALYSIS_TYPE_PIN = 44;
  ANALYSIS_TYPE_RELATIVE_PIN = 45;
  ANALYSIS_TYPE_PROTECTS_PIECE = 46;
  ANALYSIS_TYPE_DEFENDS_PIECE = 47;
  ANALYSIS_TYPE_CREATES_LUFT = 48;
  ANALYSIS_TYPE_GAMBITS_PAWN = 49;
  ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02585"></a>
## FND-02585: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PINS_ATTACKER = 43

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PINS_ATTACKER = 43;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1694.

```text
EMOVES_ATTACKER = 40;
  ANALYSIS_TYPE_BLOCKS_ATTACKER = 41;
  ANALYSIS_TYPE_UNPINS_DEFENDER = 42;
  ANALYSIS_TYPE_PINS_ATTACKER = 43;
  ANALYSIS_TYPE_PIN = 44;
  ANALYSIS_TYPE_RELATIVE_PIN = 45;
  ANALYSIS_TYPE_PROTECTS_PIECE = 46;
  ANALYSIS_TYPE_DEFENDS_PIECE = 47;
  ANALYSIS_TYPE_CREATES_LUFT = 48;
  ANALYSIS_TYPE_GAMBITS_PAWN = 49;
  ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER = 50;
  ANALYSIS_TYPE_STRIKES_AT_CENT
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02586"></a>
## FND-02586: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PIN = 44

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PIN = 44;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1730.

```text
E_BLOCKS_ATTACKER = 41;
  ANALYSIS_TYPE_UNPINS_DEFENDER = 42;
  ANALYSIS_TYPE_PINS_ATTACKER = 43;
  ANALYSIS_TYPE_PIN = 44;
  ANALYSIS_TYPE_RELATIVE_PIN = 45;
  ANALYSIS_TYPE_PROTECTS_PIECE = 46;
  ANALYSIS_TYPE_DEFENDS_PIECE = 47;
  ANALYSIS_TYPE_CREATES_LUFT = 48;
  ANALYSIS_TYPE_GAMBITS_PAWN = 49;
  ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER = 50;
  ANALYSIS_TYPE_STRIKES_AT_CENTER = 51;
  ANALYSIS_TYPE_MAKES_PASSE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02587"></a>
## FND-02587: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_RELATIVE_PIN = 45

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_RELATIVE_PIN = 45;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1756.

```text
ANALYSIS_TYPE_UNPINS_DEFENDER = 42;
  ANALYSIS_TYPE_PINS_ATTACKER = 43;
  ANALYSIS_TYPE_PIN = 44;
  ANALYSIS_TYPE_RELATIVE_PIN = 45;
  ANALYSIS_TYPE_PROTECTS_PIECE = 46;
  ANALYSIS_TYPE_DEFENDS_PIECE = 47;
  ANALYSIS_TYPE_CREATES_LUFT = 48;
  ANALYSIS_TYPE_GAMBITS_PAWN = 49;
  ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER = 50;
  ANALYSIS_TYPE_STRIKES_AT_CENTER = 51;
  ANALYSIS_TYPE_MAKES_PASSED_PAWN = 52;
  ANALYSIS_TY
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02588"></a>
## FND-02588: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PROTECTS_PIECE = 46

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PROTECTS_PIECE = 46;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1791.

```text

  ANALYSIS_TYPE_PINS_ATTACKER = 43;
  ANALYSIS_TYPE_PIN = 44;
  ANALYSIS_TYPE_RELATIVE_PIN = 45;
  ANALYSIS_TYPE_PROTECTS_PIECE = 46;
  ANALYSIS_TYPE_DEFENDS_PIECE = 47;
  ANALYSIS_TYPE_CREATES_LUFT = 48;
  ANALYSIS_TYPE_GAMBITS_PAWN = 49;
  ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER = 50;
  ANALYSIS_TYPE_STRIKES_AT_CENTER = 51;
  ANALYSIS_TYPE_MAKES_PASSED_PAWN = 52;
  ANALYSIS_TYPE_PREVENTS_CASTLING = 53;
  ANALYS
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02589"></a>
## FND-02589: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DEFENDS_PIECE = 47

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DEFENDS_PIECE = 47;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1828.

```text
  ANALYSIS_TYPE_PIN = 44;
  ANALYSIS_TYPE_RELATIVE_PIN = 45;
  ANALYSIS_TYPE_PROTECTS_PIECE = 46;
  ANALYSIS_TYPE_DEFENDS_PIECE = 47;
  ANALYSIS_TYPE_CREATES_LUFT = 48;
  ANALYSIS_TYPE_GAMBITS_PAWN = 49;
  ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER = 50;
  ANALYSIS_TYPE_STRIKES_AT_CENTER = 51;
  ANALYSIS_TYPE_MAKES_PASSED_PAWN = 52;
  ANALYSIS_TYPE_PREVENTS_CASTLING = 53;
  ANALYSIS_TYPE_TAKES_OUTPOST = 54;
  ANALYSI
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02590"></a>
## FND-02590: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CREATES_LUFT = 48

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CREATES_LUFT = 48;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1864.

```text
_TYPE_RELATIVE_PIN = 45;
  ANALYSIS_TYPE_PROTECTS_PIECE = 46;
  ANALYSIS_TYPE_DEFENDS_PIECE = 47;
  ANALYSIS_TYPE_CREATES_LUFT = 48;
  ANALYSIS_TYPE_GAMBITS_PAWN = 49;
  ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER = 50;
  ANALYSIS_TYPE_STRIKES_AT_CENTER = 51;
  ANALYSIS_TYPE_MAKES_PASSED_PAWN = 52;
  ANALYSIS_TYPE_PREVENTS_CASTLING = 53;
  ANALYSIS_TYPE_TAKES_OUTPOST = 54;
  ANALYSIS_TYPE_CHALLENGES_OPEN_FILE = 55;
  
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02591"></a>
## FND-02591: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_GAMBITS_PAWN = 49

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_GAMBITS_PAWN = 49;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1899.

```text
_TYPE_PROTECTS_PIECE = 46;
  ANALYSIS_TYPE_DEFENDS_PIECE = 47;
  ANALYSIS_TYPE_CREATES_LUFT = 48;
  ANALYSIS_TYPE_GAMBITS_PAWN = 49;
  ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER = 50;
  ANALYSIS_TYPE_STRIKES_AT_CENTER = 51;
  ANALYSIS_TYPE_MAKES_PASSED_PAWN = 52;
  ANALYSIS_TYPE_PREVENTS_CASTLING = 53;
  ANALYSIS_TYPE_TAKES_OUTPOST = 54;
  ANALYSIS_TYPE_CHALLENGES_OPEN_FILE = 55;
  ANALYSIS_TYPE_TAKES_OPEN_FILE = 56;
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02592"></a>
## FND-02592: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER = 50

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER = 50;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1934.

```text
IS_TYPE_DEFENDS_PIECE = 47;
  ANALYSIS_TYPE_CREATES_LUFT = 48;
  ANALYSIS_TYPE_GAMBITS_PAWN = 49;
  ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER = 50;
  ANALYSIS_TYPE_STRIKES_AT_CENTER = 51;
  ANALYSIS_TYPE_MAKES_PASSED_PAWN = 52;
  ANALYSIS_TYPE_PREVENTS_CASTLING = 53;
  ANALYSIS_TYPE_TAKES_OUTPOST = 54;
  ANALYSIS_TYPE_CHALLENGES_OPEN_FILE = 55;
  ANALYSIS_TYPE_TAKES_OPEN_FILE = 56;
  ANALYSIS_TYPE_ROOK_BEHIND_OWN_PA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02593"></a>
## FND-02593: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_STRIKES_AT_CENTER = 51

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_STRIKES_AT_CENTER = 51;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1985.

```text
_LUFT = 48;
  ANALYSIS_TYPE_GAMBITS_PAWN = 49;
  ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER = 50;
  ANALYSIS_TYPE_STRIKES_AT_CENTER = 51;
  ANALYSIS_TYPE_MAKES_PASSED_PAWN = 52;
  ANALYSIS_TYPE_PREVENTS_CASTLING = 53;
  ANALYSIS_TYPE_TAKES_OUTPOST = 54;
  ANALYSIS_TYPE_CHALLENGES_OPEN_FILE = 55;
  ANALYSIS_TYPE_TAKES_OPEN_FILE = 56;
  ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN = 57;
  ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN = 58;
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02594"></a>
## FND-02594: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MAKES_PASSED_PAWN = 52

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_MAKES_PASSED_PAWN = 52;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2025.

```text
 = 49;
  ANALYSIS_TYPE_EXPLOITS_OVERLOADED_DEFENDER = 50;
  ANALYSIS_TYPE_STRIKES_AT_CENTER = 51;
  ANALYSIS_TYPE_MAKES_PASSED_PAWN = 52;
  ANALYSIS_TYPE_PREVENTS_CASTLING = 53;
  ANALYSIS_TYPE_TAKES_OUTPOST = 54;
  ANALYSIS_TYPE_CHALLENGES_OPEN_FILE = 55;
  ANALYSIS_TYPE_TAKES_OPEN_FILE = 56;
  ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN = 57;
  ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN = 58;
  ANALYSIS_TYPE_BLOCKS_CHECKER = 59;
  
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02595"></a>
## FND-02595: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PREVENTS_CASTLING = 53

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PREVENTS_CASTLING = 53;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2065.

```text
ED_DEFENDER = 50;
  ANALYSIS_TYPE_STRIKES_AT_CENTER = 51;
  ANALYSIS_TYPE_MAKES_PASSED_PAWN = 52;
  ANALYSIS_TYPE_PREVENTS_CASTLING = 53;
  ANALYSIS_TYPE_TAKES_OUTPOST = 54;
  ANALYSIS_TYPE_CHALLENGES_OPEN_FILE = 55;
  ANALYSIS_TYPE_TAKES_OPEN_FILE = 56;
  ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN = 57;
  ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN = 58;
  ANALYSIS_TYPE_BLOCKS_CHECKER = 59;
  ANALYSIS_TYPE_KICKS_CHECKER = 60;
  ANAL
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02596"></a>
## FND-02596: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_TAKES_OUTPOST = 54

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_TAKES_OUTPOST = 54;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2105.

```text
S_AT_CENTER = 51;
  ANALYSIS_TYPE_MAKES_PASSED_PAWN = 52;
  ANALYSIS_TYPE_PREVENTS_CASTLING = 53;
  ANALYSIS_TYPE_TAKES_OUTPOST = 54;
  ANALYSIS_TYPE_CHALLENGES_OPEN_FILE = 55;
  ANALYSIS_TYPE_TAKES_OPEN_FILE = 56;
  ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN = 57;
  ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN = 58;
  ANALYSIS_TYPE_BLOCKS_CHECKER = 59;
  ANALYSIS_TYPE_KICKS_CHECKER = 60;
  ANALYSIS_TYPE_EVADES_CHECK = 61;
  ANALYSIS_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02597"></a>
## FND-02597: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CHALLENGES_OPEN_FILE = 55

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CHALLENGES_OPEN_FILE = 55;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2141.

```text
KES_PASSED_PAWN = 52;
  ANALYSIS_TYPE_PREVENTS_CASTLING = 53;
  ANALYSIS_TYPE_TAKES_OUTPOST = 54;
  ANALYSIS_TYPE_CHALLENGES_OPEN_FILE = 55;
  ANALYSIS_TYPE_TAKES_OPEN_FILE = 56;
  ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN = 57;
  ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN = 58;
  ANALYSIS_TYPE_BLOCKS_CHECKER = 59;
  ANALYSIS_TYPE_KICKS_CHECKER = 60;
  ANALYSIS_TYPE_EVADES_CHECK = 61;
  ANALYSIS_TYPE_KICKS = 62;
  ANALYSIS_TYPE_ROO
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02598"></a>
## FND-02598: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_TAKES_OPEN_FILE = 56

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_TAKES_OPEN_FILE = 56;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2184.

```text
NTS_CASTLING = 53;
  ANALYSIS_TYPE_TAKES_OUTPOST = 54;
  ANALYSIS_TYPE_CHALLENGES_OPEN_FILE = 55;
  ANALYSIS_TYPE_TAKES_OPEN_FILE = 56;
  ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN = 57;
  ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN = 58;
  ANALYSIS_TYPE_BLOCKS_CHECKER = 59;
  ANALYSIS_TYPE_KICKS_CHECKER = 60;
  ANALYSIS_TYPE_EVADES_CHECK = 61;
  ANALYSIS_TYPE_KICKS = 62;
  ANALYSIS_TYPE_ROOK_ON_SEVENTH = 63;
  ANALYSIS_TYPE_DEVELOPS
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02599"></a>
## FND-02599: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN = 57

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN = 57;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2222.

```text
ES_OUTPOST = 54;
  ANALYSIS_TYPE_CHALLENGES_OPEN_FILE = 55;
  ANALYSIS_TYPE_TAKES_OPEN_FILE = 56;
  ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN = 57;
  ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN = 58;
  ANALYSIS_TYPE_BLOCKS_CHECKER = 59;
  ANALYSIS_TYPE_KICKS_CHECKER = 60;
  ANALYSIS_TYPE_EVADES_CHECK = 61;
  ANALYSIS_TYPE_KICKS = 62;
  ANALYSIS_TYPE_ROOK_ON_SEVENTH = 63;
  ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO = 64;
  ANALYSIS_TYPE_WINS
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02600"></a>
## FND-02600: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN = 58

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN = 58;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2265.

```text
_OPEN_FILE = 55;
  ANALYSIS_TYPE_TAKES_OPEN_FILE = 56;
  ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN = 57;
  ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN = 58;
  ANALYSIS_TYPE_BLOCKS_CHECKER = 59;
  ANALYSIS_TYPE_KICKS_CHECKER = 60;
  ANALYSIS_TYPE_EVADES_CHECK = 61;
  ANALYSIS_TYPE_KICKS = 62;
  ANALYSIS_TYPE_ROOK_ON_SEVENTH = 63;
  ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO = 64;
  ANALYSIS_TYPE_WINS_TEMPO = 65;
  ANALYSIS_TYPE_OFFERS_TRADE =
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02601"></a>
## FND-02601: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BLOCKS_CHECKER = 59

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BLOCKS_CHECKER = 59;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2308.

```text
_FILE = 56;
  ANALYSIS_TYPE_ROOK_BEHIND_OWN_PAWN = 57;
  ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN = 58;
  ANALYSIS_TYPE_BLOCKS_CHECKER = 59;
  ANALYSIS_TYPE_KICKS_CHECKER = 60;
  ANALYSIS_TYPE_EVADES_CHECK = 61;
  ANALYSIS_TYPE_KICKS = 62;
  ANALYSIS_TYPE_ROOK_ON_SEVENTH = 63;
  ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO = 64;
  ANALYSIS_TYPE_WINS_TEMPO = 65;
  ANALYSIS_TYPE_OFFERS_TRADE = 66;
  ANALYSIS_TYPE_CAPTURE_THREAT = 67;
 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02602"></a>
## FND-02602: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_KICKS_CHECKER = 60

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_KICKS_CHECKER = 60;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2345.

```text
ND_OWN_PAWN = 57;
  ANALYSIS_TYPE_ROOK_BEHIND_OPP_PAWN = 58;
  ANALYSIS_TYPE_BLOCKS_CHECKER = 59;
  ANALYSIS_TYPE_KICKS_CHECKER = 60;
  ANALYSIS_TYPE_EVADES_CHECK = 61;
  ANALYSIS_TYPE_KICKS = 62;
  ANALYSIS_TYPE_ROOK_ON_SEVENTH = 63;
  ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO = 64;
  ANALYSIS_TYPE_WINS_TEMPO = 65;
  ANALYSIS_TYPE_OFFERS_TRADE = 66;
  ANALYSIS_TYPE_CAPTURE_THREAT = 67;
  ANALYSIS_TYPE_CONNECTS_ROOKS = 68;
 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02603"></a>
## FND-02603: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_EVADES_CHECK = 61

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_EVADES_CHECK = 61;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2381.

```text
OK_BEHIND_OPP_PAWN = 58;
  ANALYSIS_TYPE_BLOCKS_CHECKER = 59;
  ANALYSIS_TYPE_KICKS_CHECKER = 60;
  ANALYSIS_TYPE_EVADES_CHECK = 61;
  ANALYSIS_TYPE_KICKS = 62;
  ANALYSIS_TYPE_ROOK_ON_SEVENTH = 63;
  ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO = 64;
  ANALYSIS_TYPE_WINS_TEMPO = 65;
  ANALYSIS_TYPE_OFFERS_TRADE = 66;
  ANALYSIS_TYPE_CAPTURE_THREAT = 67;
  ANALYSIS_TYPE_CONNECTS_ROOKS = 68;
  ANALYSIS_TYPE_DOUBLES_ROOKS = 69;
 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02604"></a>
## FND-02604: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_KICKS = 62

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_KICKS = 62;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2416.

```text
_TYPE_BLOCKS_CHECKER = 59;
  ANALYSIS_TYPE_KICKS_CHECKER = 60;
  ANALYSIS_TYPE_EVADES_CHECK = 61;
  ANALYSIS_TYPE_KICKS = 62;
  ANALYSIS_TYPE_ROOK_ON_SEVENTH = 63;
  ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO = 64;
  ANALYSIS_TYPE_WINS_TEMPO = 65;
  ANALYSIS_TYPE_OFFERS_TRADE = 66;
  ANALYSIS_TYPE_CAPTURE_THREAT = 67;
  ANALYSIS_TYPE_CONNECTS_ROOKS = 68;
  ANALYSIS_TYPE_DOUBLES_ROOKS = 69;
  ANALYSIS_TYPE_UNDOUBLES_PAWNS = 71
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02605"></a>
## FND-02605: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ROOK_ON_SEVENTH = 63

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_ROOK_ON_SEVENTH = 63;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2444.

```text
 ANALYSIS_TYPE_KICKS_CHECKER = 60;
  ANALYSIS_TYPE_EVADES_CHECK = 61;
  ANALYSIS_TYPE_KICKS = 62;
  ANALYSIS_TYPE_ROOK_ON_SEVENTH = 63;
  ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO = 64;
  ANALYSIS_TYPE_WINS_TEMPO = 65;
  ANALYSIS_TYPE_OFFERS_TRADE = 66;
  ANALYSIS_TYPE_CAPTURE_THREAT = 67;
  ANALYSIS_TYPE_CONNECTS_ROOKS = 68;
  ANALYSIS_TYPE_DOUBLES_ROOKS = 69;
  ANALYSIS_TYPE_UNDOUBLES_PAWNS = 71;
  ANALYSIS_TYPE_FIANCHETTO
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02606"></a>
## FND-02606: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO = 64

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO = 64;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2482.

```text
NALYSIS_TYPE_EVADES_CHECK = 61;
  ANALYSIS_TYPE_KICKS = 62;
  ANALYSIS_TYPE_ROOK_ON_SEVENTH = 63;
  ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO = 64;
  ANALYSIS_TYPE_WINS_TEMPO = 65;
  ANALYSIS_TYPE_OFFERS_TRADE = 66;
  ANALYSIS_TYPE_CAPTURE_THREAT = 67;
  ANALYSIS_TYPE_CONNECTS_ROOKS = 68;
  ANALYSIS_TYPE_DOUBLES_ROOKS = 69;
  ANALYSIS_TYPE_UNDOUBLES_PAWNS = 71;
  ANALYSIS_TYPE_FIANCHETTO = 72;
  ANALYSIS_TYPE_CASTLES_SAME_SI
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02607"></a>
## FND-02607: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WINS_TEMPO = 65

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_WINS_TEMPO = 65;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2524.

```text
_TYPE_KICKS = 62;
  ANALYSIS_TYPE_ROOK_ON_SEVENTH = 63;
  ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO = 64;
  ANALYSIS_TYPE_WINS_TEMPO = 65;
  ANALYSIS_TYPE_OFFERS_TRADE = 66;
  ANALYSIS_TYPE_CAPTURE_THREAT = 67;
  ANALYSIS_TYPE_CONNECTS_ROOKS = 68;
  ANALYSIS_TYPE_DOUBLES_ROOKS = 69;
  ANALYSIS_TYPE_UNDOUBLES_PAWNS = 71;
  ANALYSIS_TYPE_FIANCHETTO = 72;
  ANALYSIS_TYPE_CASTLES_SAME_SIDE = 73;
  ANALYSIS_TYPE_CASTLES_OPPOSITE_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02608"></a>
## FND-02608: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_OFFERS_TRADE = 66

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_OFFERS_TRADE = 66;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2557.

```text
_ROOK_ON_SEVENTH = 63;
  ANALYSIS_TYPE_DEVELOPS_WITH_TEMPO = 64;
  ANALYSIS_TYPE_WINS_TEMPO = 65;
  ANALYSIS_TYPE_OFFERS_TRADE = 66;
  ANALYSIS_TYPE_CAPTURE_THREAT = 67;
  ANALYSIS_TYPE_CONNECTS_ROOKS = 68;
  ANALYSIS_TYPE_DOUBLES_ROOKS = 69;
  ANALYSIS_TYPE_UNDOUBLES_PAWNS = 71;
  ANALYSIS_TYPE_FIANCHETTO = 72;
  ANALYSIS_TYPE_CASTLES_SAME_SIDE = 73;
  ANALYSIS_TYPE_CASTLES_OPPOSITE_SIDE = 74;
  ANALYSIS_TYPE_CASTLE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02609"></a>
## FND-02609: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CAPTURE_THREAT = 67

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CAPTURE_THREAT = 67;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2592.

```text
YPE_DEVELOPS_WITH_TEMPO = 64;
  ANALYSIS_TYPE_WINS_TEMPO = 65;
  ANALYSIS_TYPE_OFFERS_TRADE = 66;
  ANALYSIS_TYPE_CAPTURE_THREAT = 67;
  ANALYSIS_TYPE_CONNECTS_ROOKS = 68;
  ANALYSIS_TYPE_DOUBLES_ROOKS = 69;
  ANALYSIS_TYPE_UNDOUBLES_PAWNS = 71;
  ANALYSIS_TYPE_FIANCHETTO = 72;
  ANALYSIS_TYPE_CASTLES_SAME_SIDE = 73;
  ANALYSIS_TYPE_CASTLES_OPPOSITE_SIDE = 74;
  ANALYSIS_TYPE_CASTLES_KING_SIDE = 75;
  ANALYSIS_TYPE_C
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02610"></a>
## FND-02610: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CONNECTS_ROOKS = 68

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CONNECTS_ROOKS = 68;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2629.

```text
SIS_TYPE_WINS_TEMPO = 65;
  ANALYSIS_TYPE_OFFERS_TRADE = 66;
  ANALYSIS_TYPE_CAPTURE_THREAT = 67;
  ANALYSIS_TYPE_CONNECTS_ROOKS = 68;
  ANALYSIS_TYPE_DOUBLES_ROOKS = 69;
  ANALYSIS_TYPE_UNDOUBLES_PAWNS = 71;
  ANALYSIS_TYPE_FIANCHETTO = 72;
  ANALYSIS_TYPE_CASTLES_SAME_SIDE = 73;
  ANALYSIS_TYPE_CASTLES_OPPOSITE_SIDE = 74;
  ANALYSIS_TYPE_CASTLES_KING_SIDE = 75;
  ANALYSIS_TYPE_CASTLES_QUEEN_SIDE = 76;
  ANALYSIS_TY
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02611"></a>
## FND-02611: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DOUBLES_ROOKS = 69

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DOUBLES_ROOKS = 69;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2666.

```text
TYPE_OFFERS_TRADE = 66;
  ANALYSIS_TYPE_CAPTURE_THREAT = 67;
  ANALYSIS_TYPE_CONNECTS_ROOKS = 68;
  ANALYSIS_TYPE_DOUBLES_ROOKS = 69;
  ANALYSIS_TYPE_UNDOUBLES_PAWNS = 71;
  ANALYSIS_TYPE_FIANCHETTO = 72;
  ANALYSIS_TYPE_CASTLES_SAME_SIDE = 73;
  ANALYSIS_TYPE_CASTLES_OPPOSITE_SIDE = 74;
  ANALYSIS_TYPE_CASTLES_KING_SIDE = 75;
  ANALYSIS_TYPE_CASTLES_QUEEN_SIDE = 76;
  ANALYSIS_TYPE_CAPTURES = 77;
  ANALYSIS_TYPE_ACT
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02612"></a>
## FND-02612: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_UNDOUBLES_PAWNS = 71

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_UNDOUBLES_PAWNS = 71;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2702.

```text
YPE_CAPTURE_THREAT = 67;
  ANALYSIS_TYPE_CONNECTS_ROOKS = 68;
  ANALYSIS_TYPE_DOUBLES_ROOKS = 69;
  ANALYSIS_TYPE_UNDOUBLES_PAWNS = 71;
  ANALYSIS_TYPE_FIANCHETTO = 72;
  ANALYSIS_TYPE_CASTLES_SAME_SIDE = 73;
  ANALYSIS_TYPE_CASTLES_OPPOSITE_SIDE = 74;
  ANALYSIS_TYPE_CASTLES_KING_SIDE = 75;
  ANALYSIS_TYPE_CASTLES_QUEEN_SIDE = 76;
  ANALYSIS_TYPE_CAPTURES = 77;
  ANALYSIS_TYPE_ACTIVATES_KING = 78;
  ANALYSIS_TYPE_DE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02613"></a>
## FND-02613: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FIANCHETTO = 72

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FIANCHETTO = 72;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2740.

```text
PE_CONNECTS_ROOKS = 68;
  ANALYSIS_TYPE_DOUBLES_ROOKS = 69;
  ANALYSIS_TYPE_UNDOUBLES_PAWNS = 71;
  ANALYSIS_TYPE_FIANCHETTO = 72;
  ANALYSIS_TYPE_CASTLES_SAME_SIDE = 73;
  ANALYSIS_TYPE_CASTLES_OPPOSITE_SIDE = 74;
  ANALYSIS_TYPE_CASTLES_KING_SIDE = 75;
  ANALYSIS_TYPE_CASTLES_QUEEN_SIDE = 76;
  ANALYSIS_TYPE_CAPTURES = 77;
  ANALYSIS_TYPE_ACTIVATES_KING = 78;
  ANALYSIS_TYPE_DEVELOPS = 79;
  ANALYSIS_TYPE_CENTRALIZ
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02614"></a>
## FND-02614: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CASTLES_SAME_SIDE = 73

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CASTLES_SAME_SIDE = 73;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2773.

```text
S_TYPE_DOUBLES_ROOKS = 69;
  ANALYSIS_TYPE_UNDOUBLES_PAWNS = 71;
  ANALYSIS_TYPE_FIANCHETTO = 72;
  ANALYSIS_TYPE_CASTLES_SAME_SIDE = 73;
  ANALYSIS_TYPE_CASTLES_OPPOSITE_SIDE = 74;
  ANALYSIS_TYPE_CASTLES_KING_SIDE = 75;
  ANALYSIS_TYPE_CASTLES_QUEEN_SIDE = 76;
  ANALYSIS_TYPE_CAPTURES = 77;
  ANALYSIS_TYPE_ACTIVATES_KING = 78;
  ANALYSIS_TYPE_DEVELOPS = 79;
  ANALYSIS_TYPE_CENTRALIZES_KNIGHT = 80;
  ANALYSIS_TYPE_B
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02615"></a>
## FND-02615: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CASTLES_OPPOSITE_SIDE = 74

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CASTLES_OPPOSITE_SIDE = 74;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2813.

```text
PE_UNDOUBLES_PAWNS = 71;
  ANALYSIS_TYPE_FIANCHETTO = 72;
  ANALYSIS_TYPE_CASTLES_SAME_SIDE = 73;
  ANALYSIS_TYPE_CASTLES_OPPOSITE_SIDE = 74;
  ANALYSIS_TYPE_CASTLES_KING_SIDE = 75;
  ANALYSIS_TYPE_CASTLES_QUEEN_SIDE = 76;
  ANALYSIS_TYPE_CAPTURES = 77;
  ANALYSIS_TYPE_ACTIVATES_KING = 78;
  ANALYSIS_TYPE_DEVELOPS = 79;
  ANALYSIS_TYPE_CENTRALIZES_KNIGHT = 80;
  ANALYSIS_TYPE_BISHOP_GAINS_SCOPE = 81;
  ANALYSIS_TYPE_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02616"></a>
## FND-02616: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CASTLES_KING_SIDE = 75

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CASTLES_KING_SIDE = 75;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2857.

```text
NCHETTO = 72;
  ANALYSIS_TYPE_CASTLES_SAME_SIDE = 73;
  ANALYSIS_TYPE_CASTLES_OPPOSITE_SIDE = 74;
  ANALYSIS_TYPE_CASTLES_KING_SIDE = 75;
  ANALYSIS_TYPE_CASTLES_QUEEN_SIDE = 76;
  ANALYSIS_TYPE_CAPTURES = 77;
  ANALYSIS_TYPE_ACTIVATES_KING = 78;
  ANALYSIS_TYPE_DEVELOPS = 79;
  ANALYSIS_TYPE_CENTRALIZES_KNIGHT = 80;
  ANALYSIS_TYPE_BISHOP_GAINS_SCOPE = 81;
  ANALYSIS_TYPE_PREPARES_BISHOP_DEVELOPMENT = 82;
  ANALYSIS
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02617"></a>
## FND-02617: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CASTLES_QUEEN_SIDE = 76

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CASTLES_QUEEN_SIDE = 76;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2897.

```text
ME_SIDE = 73;
  ANALYSIS_TYPE_CASTLES_OPPOSITE_SIDE = 74;
  ANALYSIS_TYPE_CASTLES_KING_SIDE = 75;
  ANALYSIS_TYPE_CASTLES_QUEEN_SIDE = 76;
  ANALYSIS_TYPE_CAPTURES = 77;
  ANALYSIS_TYPE_ACTIVATES_KING = 78;
  ANALYSIS_TYPE_DEVELOPS = 79;
  ANALYSIS_TYPE_CENTRALIZES_KNIGHT = 80;
  ANALYSIS_TYPE_BISHOP_GAINS_SCOPE = 81;
  ANALYSIS_TYPE_PREPARES_BISHOP_DEVELOPMENT = 82;
  ANALYSIS_TYPE_DELAYED_RECAPTURE = 83;
  ANALYSIS
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02618"></a>
## FND-02618: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CAPTURES = 77

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CAPTURES = 77;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2938.

```text
OSITE_SIDE = 74;
  ANALYSIS_TYPE_CASTLES_KING_SIDE = 75;
  ANALYSIS_TYPE_CASTLES_QUEEN_SIDE = 76;
  ANALYSIS_TYPE_CAPTURES = 77;
  ANALYSIS_TYPE_ACTIVATES_KING = 78;
  ANALYSIS_TYPE_DEVELOPS = 79;
  ANALYSIS_TYPE_CENTRALIZES_KNIGHT = 80;
  ANALYSIS_TYPE_BISHOP_GAINS_SCOPE = 81;
  ANALYSIS_TYPE_PREPARES_BISHOP_DEVELOPMENT = 82;
  ANALYSIS_TYPE_DELAYED_RECAPTURE = 83;
  ANALYSIS_TYPE_RETREAT = 84;
  ANALYSIS_TYPE_OBVIO
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02619"></a>
## FND-02619: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ACTIVATES_KING = 78

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_ACTIVATES_KING = 78;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 2969.

```text
E_CASTLES_KING_SIDE = 75;
  ANALYSIS_TYPE_CASTLES_QUEEN_SIDE = 76;
  ANALYSIS_TYPE_CAPTURES = 77;
  ANALYSIS_TYPE_ACTIVATES_KING = 78;
  ANALYSIS_TYPE_DEVELOPS = 79;
  ANALYSIS_TYPE_CENTRALIZES_KNIGHT = 80;
  ANALYSIS_TYPE_BISHOP_GAINS_SCOPE = 81;
  ANALYSIS_TYPE_PREPARES_BISHOP_DEVELOPMENT = 82;
  ANALYSIS_TYPE_DELAYED_RECAPTURE = 83;
  ANALYSIS_TYPE_RETREAT = 84;
  ANALYSIS_TYPE_OBVIOUS_RETREAT = 85;
  ANALYSIS_TYP
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02620"></a>
## FND-02620: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DEVELOPS = 79

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DEVELOPS = 79;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3006.

```text
TYPE_CASTLES_QUEEN_SIDE = 76;
  ANALYSIS_TYPE_CAPTURES = 77;
  ANALYSIS_TYPE_ACTIVATES_KING = 78;
  ANALYSIS_TYPE_DEVELOPS = 79;
  ANALYSIS_TYPE_CENTRALIZES_KNIGHT = 80;
  ANALYSIS_TYPE_BISHOP_GAINS_SCOPE = 81;
  ANALYSIS_TYPE_PREPARES_BISHOP_DEVELOPMENT = 82;
  ANALYSIS_TYPE_DELAYED_RECAPTURE = 83;
  ANALYSIS_TYPE_RETREAT = 84;
  ANALYSIS_TYPE_OBVIOUS_RETREAT = 85;
  ANALYSIS_TYPE_CRITICAL = 86;
  ANALYSIS_TYPE_WINN
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02621"></a>
## FND-02621: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CENTRALIZES_KNIGHT = 80

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CENTRALIZES_KNIGHT = 80;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3037.

```text
 ANALYSIS_TYPE_CAPTURES = 77;
  ANALYSIS_TYPE_ACTIVATES_KING = 78;
  ANALYSIS_TYPE_DEVELOPS = 79;
  ANALYSIS_TYPE_CENTRALIZES_KNIGHT = 80;
  ANALYSIS_TYPE_BISHOP_GAINS_SCOPE = 81;
  ANALYSIS_TYPE_PREPARES_BISHOP_DEVELOPMENT = 82;
  ANALYSIS_TYPE_DELAYED_RECAPTURE = 83;
  ANALYSIS_TYPE_RETREAT = 84;
  ANALYSIS_TYPE_OBVIOUS_RETREAT = 85;
  ANALYSIS_TYPE_CRITICAL = 86;
  ANALYSIS_TYPE_WINNING = 87;
  ANALYSIS_TYPE_COMEB
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02622"></a>
## FND-02622: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BISHOP_GAINS_SCOPE = 81

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BISHOP_GAINS_SCOPE = 81;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3078.

```text
TYPE_ACTIVATES_KING = 78;
  ANALYSIS_TYPE_DEVELOPS = 79;
  ANALYSIS_TYPE_CENTRALIZES_KNIGHT = 80;
  ANALYSIS_TYPE_BISHOP_GAINS_SCOPE = 81;
  ANALYSIS_TYPE_PREPARES_BISHOP_DEVELOPMENT = 82;
  ANALYSIS_TYPE_DELAYED_RECAPTURE = 83;
  ANALYSIS_TYPE_RETREAT = 84;
  ANALYSIS_TYPE_OBVIOUS_RETREAT = 85;
  ANALYSIS_TYPE_CRITICAL = 86;
  ANALYSIS_TYPE_WINNING = 87;
  ANALYSIS_TYPE_COMEBACK = 88;
  ANALYSIS_TYPE_BLUNDER_PUNISH 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02623"></a>
## FND-02623: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PREPARES_BISHOP_DEVELOPMENT = 82

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PREPARES_BISHOP_DEVELOPMENT = 82;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3119.

```text
_DEVELOPS = 79;
  ANALYSIS_TYPE_CENTRALIZES_KNIGHT = 80;
  ANALYSIS_TYPE_BISHOP_GAINS_SCOPE = 81;
  ANALYSIS_TYPE_PREPARES_BISHOP_DEVELOPMENT = 82;
  ANALYSIS_TYPE_DELAYED_RECAPTURE = 83;
  ANALYSIS_TYPE_RETREAT = 84;
  ANALYSIS_TYPE_OBVIOUS_RETREAT = 85;
  ANALYSIS_TYPE_CRITICAL = 86;
  ANALYSIS_TYPE_WINNING = 87;
  ANALYSIS_TYPE_COMEBACK = 88;
  ANALYSIS_TYPE_BLUNDER_PUNISH = 89;
  ANALYSIS_TYPE_TAKES_OPPORTUNITY =
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02624"></a>
## FND-02624: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DELAYED_RECAPTURE = 83

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DELAYED_RECAPTURE = 83;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3169.

```text
 = 80;
  ANALYSIS_TYPE_BISHOP_GAINS_SCOPE = 81;
  ANALYSIS_TYPE_PREPARES_BISHOP_DEVELOPMENT = 82;
  ANALYSIS_TYPE_DELAYED_RECAPTURE = 83;
  ANALYSIS_TYPE_RETREAT = 84;
  ANALYSIS_TYPE_OBVIOUS_RETREAT = 85;
  ANALYSIS_TYPE_CRITICAL = 86;
  ANALYSIS_TYPE_WINNING = 87;
  ANALYSIS_TYPE_COMEBACK = 88;
  ANALYSIS_TYPE_BLUNDER_PUNISH = 89;
  ANALYSIS_TYPE_TAKES_OPPORTUNITY = 90;
  ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT = 91;
  
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02625"></a>
## FND-02625: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_RETREAT = 84

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_RETREAT = 84;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3209.

```text
E = 81;
  ANALYSIS_TYPE_PREPARES_BISHOP_DEVELOPMENT = 82;
  ANALYSIS_TYPE_DELAYED_RECAPTURE = 83;
  ANALYSIS_TYPE_RETREAT = 84;
  ANALYSIS_TYPE_OBVIOUS_RETREAT = 85;
  ANALYSIS_TYPE_CRITICAL = 86;
  ANALYSIS_TYPE_WINNING = 87;
  ANALYSIS_TYPE_COMEBACK = 88;
  ANALYSIS_TYPE_BLUNDER_PUNISH = 89;
  ANALYSIS_TYPE_TAKES_OPPORTUNITY = 90;
  ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT = 91;
  ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG = 92;

```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02626"></a>
## FND-02626: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_OBVIOUS_RETREAT = 85

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_OBVIOUS_RETREAT = 85;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3239.

```text
ES_BISHOP_DEVELOPMENT = 82;
  ANALYSIS_TYPE_DELAYED_RECAPTURE = 83;
  ANALYSIS_TYPE_RETREAT = 84;
  ANALYSIS_TYPE_OBVIOUS_RETREAT = 85;
  ANALYSIS_TYPE_CRITICAL = 86;
  ANALYSIS_TYPE_WINNING = 87;
  ANALYSIS_TYPE_COMEBACK = 88;
  ANALYSIS_TYPE_BLUNDER_PUNISH = 89;
  ANALYSIS_TYPE_TAKES_OPPORTUNITY = 90;
  ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT = 91;
  ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG = 92;
  ANALYSIS_TYPE_CAPTURE_THREAT
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02627"></a>
## FND-02627: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CRITICAL = 86

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CRITICAL = 86;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3277.

```text
_TYPE_DELAYED_RECAPTURE = 83;
  ANALYSIS_TYPE_RETREAT = 84;
  ANALYSIS_TYPE_OBVIOUS_RETREAT = 85;
  ANALYSIS_TYPE_CRITICAL = 86;
  ANALYSIS_TYPE_WINNING = 87;
  ANALYSIS_TYPE_COMEBACK = 88;
  ANALYSIS_TYPE_BLUNDER_PUNISH = 89;
  ANALYSIS_TYPE_TAKES_OPPORTUNITY = 90;
  ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT = 91;
  ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG = 92;
  ANALYSIS_TYPE_CAPTURE_THREAT_FROM = 93;
  ANALYSIS_TYPE_CAPTURE_TH
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02628"></a>
## FND-02628: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WINNING = 87

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_WINNING = 87;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3308.

```text
 ANALYSIS_TYPE_RETREAT = 84;
  ANALYSIS_TYPE_OBVIOUS_RETREAT = 85;
  ANALYSIS_TYPE_CRITICAL = 86;
  ANALYSIS_TYPE_WINNING = 87;
  ANALYSIS_TYPE_COMEBACK = 88;
  ANALYSIS_TYPE_BLUNDER_PUNISH = 89;
  ANALYSIS_TYPE_TAKES_OPPORTUNITY = 90;
  ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT = 91;
  ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG = 92;
  ANALYSIS_TYPE_CAPTURE_THREAT_FROM = 93;
  ANALYSIS_TYPE_CAPTURE_THREAT_TO = 94;
  ANALYSIS_TYPE_W
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02629"></a>
## FND-02629: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_COMEBACK = 88

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_COMEBACK = 88;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3338.

```text
 ANALYSIS_TYPE_OBVIOUS_RETREAT = 85;
  ANALYSIS_TYPE_CRITICAL = 86;
  ANALYSIS_TYPE_WINNING = 87;
  ANALYSIS_TYPE_COMEBACK = 88;
  ANALYSIS_TYPE_BLUNDER_PUNISH = 89;
  ANALYSIS_TYPE_TAKES_OPPORTUNITY = 90;
  ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT = 91;
  ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG = 92;
  ANALYSIS_TYPE_CAPTURE_THREAT_FROM = 93;
  ANALYSIS_TYPE_CAPTURE_THREAT_TO = 94;
  ANALYSIS_TYPE_WINS_MATERIAL = 95;
  ANALYSIS_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02630"></a>
## FND-02630: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BLUNDER_PUNISH = 89

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BLUNDER_PUNISH = 89;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3369.

```text
= 85;
  ANALYSIS_TYPE_CRITICAL = 86;
  ANALYSIS_TYPE_WINNING = 87;
  ANALYSIS_TYPE_COMEBACK = 88;
  ANALYSIS_TYPE_BLUNDER_PUNISH = 89;
  ANALYSIS_TYPE_TAKES_OPPORTUNITY = 90;
  ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT = 91;
  ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG = 92;
  ANALYSIS_TYPE_CAPTURE_THREAT_FROM = 93;
  ANALYSIS_TYPE_CAPTURE_THREAT_TO = 94;
  ANALYSIS_TYPE_WINS_MATERIAL = 95;
  ANALYSIS_TYPE_KEYMOMENT_BAD_FASTER_MATE 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02631"></a>
## FND-02631: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_TAKES_OPPORTUNITY = 90

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_TAKES_OPPORTUNITY = 90;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3406.

```text
  ANALYSIS_TYPE_WINNING = 87;
  ANALYSIS_TYPE_COMEBACK = 88;
  ANALYSIS_TYPE_BLUNDER_PUNISH = 89;
  ANALYSIS_TYPE_TAKES_OPPORTUNITY = 90;
  ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT = 91;
  ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG = 92;
  ANALYSIS_TYPE_CAPTURE_THREAT_FROM = 93;
  ANALYSIS_TYPE_CAPTURE_THREAT_TO = 94;
  ANALYSIS_TYPE_WINS_MATERIAL = 95;
  ANALYSIS_TYPE_KEYMOMENT_BAD_FASTER_MATE = 96;
  ANALYSIS_TYPE_NO_LONGER_MATE 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02632"></a>
## FND-02632: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT = 91

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT = 91;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3446.

```text
_TYPE_COMEBACK = 88;
  ANALYSIS_TYPE_BLUNDER_PUNISH = 89;
  ANALYSIS_TYPE_TAKES_OPPORTUNITY = 90;
  ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT = 91;
  ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG = 92;
  ANALYSIS_TYPE_CAPTURE_THREAT_FROM = 93;
  ANALYSIS_TYPE_CAPTURE_THREAT_TO = 94;
  ANALYSIS_TYPE_WINS_MATERIAL = 95;
  ANALYSIS_TYPE_KEYMOMENT_BAD_FASTER_MATE = 96;
  ANALYSIS_TYPE_NO_LONGER_MATE = 97;
  ANALYSIS_TYPE_BAD_CAPTURE_CHOICE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02633"></a>
## FND-02633: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG = 92

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG = 92;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3489.

```text
R_PUNISH = 89;
  ANALYSIS_TYPE_TAKES_OPPORTUNITY = 90;
  ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT = 91;
  ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG = 92;
  ANALYSIS_TYPE_CAPTURE_THREAT_FROM = 93;
  ANALYSIS_TYPE_CAPTURE_THREAT_TO = 94;
  ANALYSIS_TYPE_WINS_MATERIAL = 95;
  ANALYSIS_TYPE_KEYMOMENT_BAD_FASTER_MATE = 96;
  ANALYSIS_TYPE_NO_LONGER_MATE = 97;
  ANALYSIS_TYPE_BAD_CAPTURE_CHOICE = 98;
  ANALYSIS_TYPE_LOSES_MATERIAL = 100
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02634"></a>
## FND-02634: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CAPTURE_THREAT_FROM = 93

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CAPTURE_THREAT_FROM = 93;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3531.

```text
TUNITY = 90;
  ANALYSIS_TYPE_NMP_MATE_IN_X_THREAT = 91;
  ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG = 92;
  ANALYSIS_TYPE_CAPTURE_THREAT_FROM = 93;
  ANALYSIS_TYPE_CAPTURE_THREAT_TO = 94;
  ANALYSIS_TYPE_WINS_MATERIAL = 95;
  ANALYSIS_TYPE_KEYMOMENT_BAD_FASTER_MATE = 96;
  ANALYSIS_TYPE_NO_LONGER_MATE = 97;
  ANALYSIS_TYPE_BAD_CAPTURE_CHOICE = 98;
  ANALYSIS_TYPE_LOSES_MATERIAL = 100;
  ANALYSIS_TYPE_LOSES_CASTLING_RIGHTS = 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02635"></a>
## FND-02635: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CAPTURE_THREAT_TO = 94

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CAPTURE_THREAT_TO = 94;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3573.

```text
_THREAT = 91;
  ANALYSIS_TYPE_NMP_MUTUAL_ZUGZWANG = 92;
  ANALYSIS_TYPE_CAPTURE_THREAT_FROM = 93;
  ANALYSIS_TYPE_CAPTURE_THREAT_TO = 94;
  ANALYSIS_TYPE_WINS_MATERIAL = 95;
  ANALYSIS_TYPE_KEYMOMENT_BAD_FASTER_MATE = 96;
  ANALYSIS_TYPE_NO_LONGER_MATE = 97;
  ANALYSIS_TYPE_BAD_CAPTURE_CHOICE = 98;
  ANALYSIS_TYPE_LOSES_MATERIAL = 100;
  ANALYSIS_TYPE_LOSES_CASTLING_RIGHTS = 101;
  ANALYSIS_TYPE_DOUBLES_CASTLE_PAWNS 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02636"></a>
## FND-02636: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WINS_MATERIAL = 95

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_WINS_MATERIAL = 95;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3613.

```text
_ZUGZWANG = 92;
  ANALYSIS_TYPE_CAPTURE_THREAT_FROM = 93;
  ANALYSIS_TYPE_CAPTURE_THREAT_TO = 94;
  ANALYSIS_TYPE_WINS_MATERIAL = 95;
  ANALYSIS_TYPE_KEYMOMENT_BAD_FASTER_MATE = 96;
  ANALYSIS_TYPE_NO_LONGER_MATE = 97;
  ANALYSIS_TYPE_BAD_CAPTURE_CHOICE = 98;
  ANALYSIS_TYPE_LOSES_MATERIAL = 100;
  ANALYSIS_TYPE_LOSES_CASTLING_RIGHTS = 101;
  ANALYSIS_TYPE_DOUBLES_CASTLE_PAWNS = 102;
  ANALYSIS_TYPE_DOUBLES_PAWNS = 1
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02637"></a>
## FND-02637: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_KEYMOMENT_BAD_FASTER_MATE = 96

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_KEYMOMENT_BAD_FASTER_MATE = 96;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3649.

```text
URE_THREAT_FROM = 93;
  ANALYSIS_TYPE_CAPTURE_THREAT_TO = 94;
  ANALYSIS_TYPE_WINS_MATERIAL = 95;
  ANALYSIS_TYPE_KEYMOMENT_BAD_FASTER_MATE = 96;
  ANALYSIS_TYPE_NO_LONGER_MATE = 97;
  ANALYSIS_TYPE_BAD_CAPTURE_CHOICE = 98;
  ANALYSIS_TYPE_LOSES_MATERIAL = 100;
  ANALYSIS_TYPE_LOSES_CASTLING_RIGHTS = 101;
  ANALYSIS_TYPE_DOUBLES_CASTLE_PAWNS = 102;
  ANALYSIS_TYPE_DOUBLES_PAWNS = 103;
  ANALYSIS_TYPE_ISOLATES_PAWN = 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02638"></a>
## FND-02638: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_NO_LONGER_MATE = 97

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_NO_LONGER_MATE = 97;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3697.

```text
REAT_TO = 94;
  ANALYSIS_TYPE_WINS_MATERIAL = 95;
  ANALYSIS_TYPE_KEYMOMENT_BAD_FASTER_MATE = 96;
  ANALYSIS_TYPE_NO_LONGER_MATE = 97;
  ANALYSIS_TYPE_BAD_CAPTURE_CHOICE = 98;
  ANALYSIS_TYPE_LOSES_MATERIAL = 100;
  ANALYSIS_TYPE_LOSES_CASTLING_RIGHTS = 101;
  ANALYSIS_TYPE_DOUBLES_CASTLE_PAWNS = 102;
  ANALYSIS_TYPE_DOUBLES_PAWNS = 103;
  ANALYSIS_TYPE_ISOLATES_PAWN = 104;
  ANALYSIS_TYPE_ROOK_PASSIVE_PROTECTION = 1
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02639"></a>
## FND-02639: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BAD_CAPTURE_CHOICE = 98

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BAD_CAPTURE_CHOICE = 98;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3734.

```text
TERIAL = 95;
  ANALYSIS_TYPE_KEYMOMENT_BAD_FASTER_MATE = 96;
  ANALYSIS_TYPE_NO_LONGER_MATE = 97;
  ANALYSIS_TYPE_BAD_CAPTURE_CHOICE = 98;
  ANALYSIS_TYPE_LOSES_MATERIAL = 100;
  ANALYSIS_TYPE_LOSES_CASTLING_RIGHTS = 101;
  ANALYSIS_TYPE_DOUBLES_CASTLE_PAWNS = 102;
  ANALYSIS_TYPE_DOUBLES_PAWNS = 103;
  ANALYSIS_TYPE_ISOLATES_PAWN = 104;
  ANALYSIS_TYPE_ROOK_PASSIVE_PROTECTION = 105;
  ANALYSIS_TYPE_WINNING_TO_BETTER
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02640"></a>
## FND-02640: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_LOSES_MATERIAL = 100

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_LOSES_MATERIAL = 100;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3775.

```text
D_FASTER_MATE = 96;
  ANALYSIS_TYPE_NO_LONGER_MATE = 97;
  ANALYSIS_TYPE_BAD_CAPTURE_CHOICE = 98;
  ANALYSIS_TYPE_LOSES_MATERIAL = 100;
  ANALYSIS_TYPE_LOSES_CASTLING_RIGHTS = 101;
  ANALYSIS_TYPE_DOUBLES_CASTLE_PAWNS = 102;
  ANALYSIS_TYPE_DOUBLES_PAWNS = 103;
  ANALYSIS_TYPE_ISOLATES_PAWN = 104;
  ANALYSIS_TYPE_ROOK_PASSIVE_PROTECTION = 105;
  ANALYSIS_TYPE_WINNING_TO_BETTER = 106;
  ANALYSIS_TYPE_WINNING_TO_EQUAL 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02641"></a>
## FND-02641: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_LOSES_CASTLING_RIGHTS = 101

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_LOSES_CASTLING_RIGHTS = 101;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3813.

```text
_LONGER_MATE = 97;
  ANALYSIS_TYPE_BAD_CAPTURE_CHOICE = 98;
  ANALYSIS_TYPE_LOSES_MATERIAL = 100;
  ANALYSIS_TYPE_LOSES_CASTLING_RIGHTS = 101;
  ANALYSIS_TYPE_DOUBLES_CASTLE_PAWNS = 102;
  ANALYSIS_TYPE_DOUBLES_PAWNS = 103;
  ANALYSIS_TYPE_ISOLATES_PAWN = 104;
  ANALYSIS_TYPE_ROOK_PASSIVE_PROTECTION = 105;
  ANALYSIS_TYPE_WINNING_TO_BETTER = 106;
  ANALYSIS_TYPE_WINNING_TO_EQUAL = 107;
  ANALYSIS_TYPE_WINNING_TO_WORS
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02642"></a>
## FND-02642: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DOUBLES_CASTLE_PAWNS = 102

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DOUBLES_CASTLE_PAWNS = 102;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3858.

```text
E_CHOICE = 98;
  ANALYSIS_TYPE_LOSES_MATERIAL = 100;
  ANALYSIS_TYPE_LOSES_CASTLING_RIGHTS = 101;
  ANALYSIS_TYPE_DOUBLES_CASTLE_PAWNS = 102;
  ANALYSIS_TYPE_DOUBLES_PAWNS = 103;
  ANALYSIS_TYPE_ISOLATES_PAWN = 104;
  ANALYSIS_TYPE_ROOK_PASSIVE_PROTECTION = 105;
  ANALYSIS_TYPE_WINNING_TO_BETTER = 106;
  ANALYSIS_TYPE_WINNING_TO_EQUAL = 107;
  ANALYSIS_TYPE_WINNING_TO_WORSE = 108;
  ANALYSIS_TYPE_WINNING_TO_LOSING = 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02643"></a>
## FND-02643: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DOUBLES_PAWNS = 103

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DOUBLES_PAWNS = 103;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3902.

```text
L = 100;
  ANALYSIS_TYPE_LOSES_CASTLING_RIGHTS = 101;
  ANALYSIS_TYPE_DOUBLES_CASTLE_PAWNS = 102;
  ANALYSIS_TYPE_DOUBLES_PAWNS = 103;
  ANALYSIS_TYPE_ISOLATES_PAWN = 104;
  ANALYSIS_TYPE_ROOK_PASSIVE_PROTECTION = 105;
  ANALYSIS_TYPE_WINNING_TO_BETTER = 106;
  ANALYSIS_TYPE_WINNING_TO_EQUAL = 107;
  ANALYSIS_TYPE_WINNING_TO_WORSE = 108;
  ANALYSIS_TYPE_WINNING_TO_LOSING = 109;
  ANALYSIS_TYPE_BETTER_TO_EQUAL = 110;

```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02644"></a>
## FND-02644: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ISOLATES_PAWN = 104

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_ISOLATES_PAWN = 104;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3939.

```text
NG_RIGHTS = 101;
  ANALYSIS_TYPE_DOUBLES_CASTLE_PAWNS = 102;
  ANALYSIS_TYPE_DOUBLES_PAWNS = 103;
  ANALYSIS_TYPE_ISOLATES_PAWN = 104;
  ANALYSIS_TYPE_ROOK_PASSIVE_PROTECTION = 105;
  ANALYSIS_TYPE_WINNING_TO_BETTER = 106;
  ANALYSIS_TYPE_WINNING_TO_EQUAL = 107;
  ANALYSIS_TYPE_WINNING_TO_WORSE = 108;
  ANALYSIS_TYPE_WINNING_TO_LOSING = 109;
  ANALYSIS_TYPE_BETTER_TO_EQUAL = 110;
  ANALYSIS_TYPE_BETTER_TO_WORSE = 111
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02645"></a>
## FND-02645: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ROOK_PASSIVE_PROTECTION = 105

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_ROOK_PASSIVE_PROTECTION = 105;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 3976.

```text
LES_CASTLE_PAWNS = 102;
  ANALYSIS_TYPE_DOUBLES_PAWNS = 103;
  ANALYSIS_TYPE_ISOLATES_PAWN = 104;
  ANALYSIS_TYPE_ROOK_PASSIVE_PROTECTION = 105;
  ANALYSIS_TYPE_WINNING_TO_BETTER = 106;
  ANALYSIS_TYPE_WINNING_TO_EQUAL = 107;
  ANALYSIS_TYPE_WINNING_TO_WORSE = 108;
  ANALYSIS_TYPE_WINNING_TO_LOSING = 109;
  ANALYSIS_TYPE_BETTER_TO_EQUAL = 110;
  ANALYSIS_TYPE_BETTER_TO_WORSE = 111;
  ANALYSIS_TYPE_BETTER_TO_LOSING = 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02646"></a>
## FND-02646: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WINNING_TO_BETTER = 106

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_WINNING_TO_BETTER = 106;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4023.

```text
_PAWNS = 103;
  ANALYSIS_TYPE_ISOLATES_PAWN = 104;
  ANALYSIS_TYPE_ROOK_PASSIVE_PROTECTION = 105;
  ANALYSIS_TYPE_WINNING_TO_BETTER = 106;
  ANALYSIS_TYPE_WINNING_TO_EQUAL = 107;
  ANALYSIS_TYPE_WINNING_TO_WORSE = 108;
  ANALYSIS_TYPE_WINNING_TO_LOSING = 109;
  ANALYSIS_TYPE_BETTER_TO_EQUAL = 110;
  ANALYSIS_TYPE_BETTER_TO_WORSE = 111;
  ANALYSIS_TYPE_BETTER_TO_LOSING = 112;
  ANALYSIS_TYPE_EQUAL_TO_WORSE = 113;
  AN
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02647"></a>
## FND-02647: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WINNING_TO_EQUAL = 107

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_WINNING_TO_EQUAL = 107;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4064.

```text
WN = 104;
  ANALYSIS_TYPE_ROOK_PASSIVE_PROTECTION = 105;
  ANALYSIS_TYPE_WINNING_TO_BETTER = 106;
  ANALYSIS_TYPE_WINNING_TO_EQUAL = 107;
  ANALYSIS_TYPE_WINNING_TO_WORSE = 108;
  ANALYSIS_TYPE_WINNING_TO_LOSING = 109;
  ANALYSIS_TYPE_BETTER_TO_EQUAL = 110;
  ANALYSIS_TYPE_BETTER_TO_WORSE = 111;
  ANALYSIS_TYPE_BETTER_TO_LOSING = 112;
  ANALYSIS_TYPE_EQUAL_TO_WORSE = 113;
  ANALYSIS_TYPE_EQUAL_TO_LOSING = 114;
  ANAL
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02648"></a>
## FND-02648: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WINNING_TO_WORSE = 108

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_WINNING_TO_WORSE = 108;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4104.

```text
ROTECTION = 105;
  ANALYSIS_TYPE_WINNING_TO_BETTER = 106;
  ANALYSIS_TYPE_WINNING_TO_EQUAL = 107;
  ANALYSIS_TYPE_WINNING_TO_WORSE = 108;
  ANALYSIS_TYPE_WINNING_TO_LOSING = 109;
  ANALYSIS_TYPE_BETTER_TO_EQUAL = 110;
  ANALYSIS_TYPE_BETTER_TO_WORSE = 111;
  ANALYSIS_TYPE_BETTER_TO_LOSING = 112;
  ANALYSIS_TYPE_EQUAL_TO_WORSE = 113;
  ANALYSIS_TYPE_EQUAL_TO_LOSING = 114;
  ANALYSIS_TYPE_WORSE_TO_LOSING = 115;
  ANALY
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02649"></a>
## FND-02649: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WINNING_TO_LOSING = 109

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_WINNING_TO_LOSING = 109;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4144.

```text
_TO_BETTER = 106;
  ANALYSIS_TYPE_WINNING_TO_EQUAL = 107;
  ANALYSIS_TYPE_WINNING_TO_WORSE = 108;
  ANALYSIS_TYPE_WINNING_TO_LOSING = 109;
  ANALYSIS_TYPE_BETTER_TO_EQUAL = 110;
  ANALYSIS_TYPE_BETTER_TO_WORSE = 111;
  ANALYSIS_TYPE_BETTER_TO_LOSING = 112;
  ANALYSIS_TYPE_EQUAL_TO_WORSE = 113;
  ANALYSIS_TYPE_EQUAL_TO_LOSING = 114;
  ANALYSIS_TYPE_WORSE_TO_LOSING = 115;
  ANALYSIS_TYPE_UNDERPROMOTION = 116;
  ANALYSI
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02650"></a>
## FND-02650: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BETTER_TO_EQUAL = 110

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BETTER_TO_EQUAL = 110;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4185.

```text
_TO_EQUAL = 107;
  ANALYSIS_TYPE_WINNING_TO_WORSE = 108;
  ANALYSIS_TYPE_WINNING_TO_LOSING = 109;
  ANALYSIS_TYPE_BETTER_TO_EQUAL = 110;
  ANALYSIS_TYPE_BETTER_TO_WORSE = 111;
  ANALYSIS_TYPE_BETTER_TO_LOSING = 112;
  ANALYSIS_TYPE_EQUAL_TO_WORSE = 113;
  ANALYSIS_TYPE_EQUAL_TO_LOSING = 114;
  ANALYSIS_TYPE_WORSE_TO_LOSING = 115;
  ANALYSIS_TYPE_UNDERPROMOTION = 116;
  ANALYSIS_TYPE_UNDERPROMOTION_MATE = 117;
  ANALY
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02651"></a>
## FND-02651: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BETTER_TO_WORSE = 111

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BETTER_TO_WORSE = 111;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4224.

```text
G_TO_WORSE = 108;
  ANALYSIS_TYPE_WINNING_TO_LOSING = 109;
  ANALYSIS_TYPE_BETTER_TO_EQUAL = 110;
  ANALYSIS_TYPE_BETTER_TO_WORSE = 111;
  ANALYSIS_TYPE_BETTER_TO_LOSING = 112;
  ANALYSIS_TYPE_EQUAL_TO_WORSE = 113;
  ANALYSIS_TYPE_EQUAL_TO_LOSING = 114;
  ANALYSIS_TYPE_WORSE_TO_LOSING = 115;
  ANALYSIS_TYPE_UNDERPROMOTION = 116;
  ANALYSIS_TYPE_UNDERPROMOTION_MATE = 117;
  ANALYSIS_TYPE_FORCES_REPETITION = 118;
  ANA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02652"></a>
## FND-02652: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BETTER_TO_LOSING = 112

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BETTER_TO_LOSING = 112;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4263.

```text
NG_TO_LOSING = 109;
  ANALYSIS_TYPE_BETTER_TO_EQUAL = 110;
  ANALYSIS_TYPE_BETTER_TO_WORSE = 111;
  ANALYSIS_TYPE_BETTER_TO_LOSING = 112;
  ANALYSIS_TYPE_EQUAL_TO_WORSE = 113;
  ANALYSIS_TYPE_EQUAL_TO_LOSING = 114;
  ANALYSIS_TYPE_WORSE_TO_LOSING = 115;
  ANALYSIS_TYPE_UNDERPROMOTION = 116;
  ANALYSIS_TYPE_UNDERPROMOTION_MATE = 117;
  ANALYSIS_TYPE_FORCES_REPETITION = 118;
  ANALYSIS_TYPE_UNPINS_WITH_DEFENSE = 119;
 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02653"></a>
## FND-02653: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_EQUAL_TO_WORSE = 113

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_EQUAL_TO_WORSE = 113;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4303.

```text
ER_TO_EQUAL = 110;
  ANALYSIS_TYPE_BETTER_TO_WORSE = 111;
  ANALYSIS_TYPE_BETTER_TO_LOSING = 112;
  ANALYSIS_TYPE_EQUAL_TO_WORSE = 113;
  ANALYSIS_TYPE_EQUAL_TO_LOSING = 114;
  ANALYSIS_TYPE_WORSE_TO_LOSING = 115;
  ANALYSIS_TYPE_UNDERPROMOTION = 116;
  ANALYSIS_TYPE_UNDERPROMOTION_MATE = 117;
  ANALYSIS_TYPE_FORCES_REPETITION = 118;
  ANALYSIS_TYPE_UNPINS_WITH_DEFENSE = 119;
  ANALYSIS_TYPE_DISCOVERED_CHECK_ATTACK =
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02654"></a>
## FND-02654: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_EQUAL_TO_LOSING = 114

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_EQUAL_TO_LOSING = 114;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4341.

```text
TER_TO_WORSE = 111;
  ANALYSIS_TYPE_BETTER_TO_LOSING = 112;
  ANALYSIS_TYPE_EQUAL_TO_WORSE = 113;
  ANALYSIS_TYPE_EQUAL_TO_LOSING = 114;
  ANALYSIS_TYPE_WORSE_TO_LOSING = 115;
  ANALYSIS_TYPE_UNDERPROMOTION = 116;
  ANALYSIS_TYPE_UNDERPROMOTION_MATE = 117;
  ANALYSIS_TYPE_FORCES_REPETITION = 118;
  ANALYSIS_TYPE_UNPINS_WITH_DEFENSE = 119;
  ANALYSIS_TYPE_DISCOVERED_CHECK_ATTACK = 120;
  ANALYSIS_TYPE_EXPLOITS_PINNED_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02655"></a>
## FND-02655: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WORSE_TO_LOSING = 115

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_WORSE_TO_LOSING = 115;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4380.

```text
TER_TO_LOSING = 112;
  ANALYSIS_TYPE_EQUAL_TO_WORSE = 113;
  ANALYSIS_TYPE_EQUAL_TO_LOSING = 114;
  ANALYSIS_TYPE_WORSE_TO_LOSING = 115;
  ANALYSIS_TYPE_UNDERPROMOTION = 116;
  ANALYSIS_TYPE_UNDERPROMOTION_MATE = 117;
  ANALYSIS_TYPE_FORCES_REPETITION = 118;
  ANALYSIS_TYPE_UNPINS_WITH_DEFENSE = 119;
  ANALYSIS_TYPE_DISCOVERED_CHECK_ATTACK = 120;
  ANALYSIS_TYPE_EXPLOITS_PINNED_DEFENDER = 121;
  ANALYSIS_TYPE_PINS_DE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02656"></a>
## FND-02656: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_UNDERPROMOTION = 116

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_UNDERPROMOTION = 116;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4419.

```text
UAL_TO_WORSE = 113;
  ANALYSIS_TYPE_EQUAL_TO_LOSING = 114;
  ANALYSIS_TYPE_WORSE_TO_LOSING = 115;
  ANALYSIS_TYPE_UNDERPROMOTION = 116;
  ANALYSIS_TYPE_UNDERPROMOTION_MATE = 117;
  ANALYSIS_TYPE_FORCES_REPETITION = 118;
  ANALYSIS_TYPE_UNPINS_WITH_DEFENSE = 119;
  ANALYSIS_TYPE_DISCOVERED_CHECK_ATTACK = 120;
  ANALYSIS_TYPE_EXPLOITS_PINNED_DEFENDER = 121;
  ANALYSIS_TYPE_PINS_DEFENDER = 122;
  ANALYSIS_TYPE_MAINTAINE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02657"></a>
## FND-02657: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_UNDERPROMOTION_MATE = 117

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_UNDERPROMOTION_MATE = 117;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4457.

```text
UAL_TO_LOSING = 114;
  ANALYSIS_TYPE_WORSE_TO_LOSING = 115;
  ANALYSIS_TYPE_UNDERPROMOTION = 116;
  ANALYSIS_TYPE_UNDERPROMOTION_MATE = 117;
  ANALYSIS_TYPE_FORCES_REPETITION = 118;
  ANALYSIS_TYPE_UNPINS_WITH_DEFENSE = 119;
  ANALYSIS_TYPE_DISCOVERED_CHECK_ATTACK = 120;
  ANALYSIS_TYPE_EXPLOITS_PINNED_DEFENDER = 121;
  ANALYSIS_TYPE_PINS_DEFENDER = 122;
  ANALYSIS_TYPE_MAINTAINED_MATE = 123;
  ANALYSIS_TYPE_FORCES_L
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02658"></a>
## FND-02658: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORCES_REPETITION = 118

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FORCES_REPETITION = 118;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4500.

```text
TO_LOSING = 115;
  ANALYSIS_TYPE_UNDERPROMOTION = 116;
  ANALYSIS_TYPE_UNDERPROMOTION_MATE = 117;
  ANALYSIS_TYPE_FORCES_REPETITION = 118;
  ANALYSIS_TYPE_UNPINS_WITH_DEFENSE = 119;
  ANALYSIS_TYPE_DISCOVERED_CHECK_ATTACK = 120;
  ANALYSIS_TYPE_EXPLOITS_PINNED_DEFENDER = 121;
  ANALYSIS_TYPE_PINS_DEFENDER = 122;
  ANALYSIS_TYPE_MAINTAINED_MATE = 123;
  ANALYSIS_TYPE_FORCES_LOSES_CASTLING_RIGHTS = 124;
  ANALYSIS_TYPE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02659"></a>
## FND-02659: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_UNPINS_WITH_DEFENSE = 119

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_UNPINS_WITH_DEFENSE = 119;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4541.

```text
MOTION = 116;
  ANALYSIS_TYPE_UNDERPROMOTION_MATE = 117;
  ANALYSIS_TYPE_FORCES_REPETITION = 118;
  ANALYSIS_TYPE_UNPINS_WITH_DEFENSE = 119;
  ANALYSIS_TYPE_DISCOVERED_CHECK_ATTACK = 120;
  ANALYSIS_TYPE_EXPLOITS_PINNED_DEFENDER = 121;
  ANALYSIS_TYPE_PINS_DEFENDER = 122;
  ANALYSIS_TYPE_MAINTAINED_MATE = 123;
  ANALYSIS_TYPE_FORCES_LOSES_CASTLING_RIGHTS = 124;
  ANALYSIS_TYPE_WINS_MATERIAL_NOT_FREE = 125;
  ANALYSIS
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02660"></a>
## FND-02660: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DISCOVERED_CHECK_ATTACK = 120

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DISCOVERED_CHECK_ATTACK = 120;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4584.

```text
N_MATE = 117;
  ANALYSIS_TYPE_FORCES_REPETITION = 118;
  ANALYSIS_TYPE_UNPINS_WITH_DEFENSE = 119;
  ANALYSIS_TYPE_DISCOVERED_CHECK_ATTACK = 120;
  ANALYSIS_TYPE_EXPLOITS_PINNED_DEFENDER = 121;
  ANALYSIS_TYPE_PINS_DEFENDER = 122;
  ANALYSIS_TYPE_MAINTAINED_MATE = 123;
  ANALYSIS_TYPE_FORCES_LOSES_CASTLING_RIGHTS = 124;
  ANALYSIS_TYPE_WINS_MATERIAL_NOT_FREE = 125;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE_MATE = 126;

```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02661"></a>
## FND-02661: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_EXPLOITS_PINNED_DEFENDER = 121

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_EXPLOITS_PINNED_DEFENDER = 121;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4631.

```text
 = 118;
  ANALYSIS_TYPE_UNPINS_WITH_DEFENSE = 119;
  ANALYSIS_TYPE_DISCOVERED_CHECK_ATTACK = 120;
  ANALYSIS_TYPE_EXPLOITS_PINNED_DEFENDER = 121;
  ANALYSIS_TYPE_PINS_DEFENDER = 122;
  ANALYSIS_TYPE_MAINTAINED_MATE = 123;
  ANALYSIS_TYPE_FORCES_LOSES_CASTLING_RIGHTS = 124;
  ANALYSIS_TYPE_WINS_MATERIAL_NOT_FREE = 125;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE_MATE = 126;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE_MATE =
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02662"></a>
## FND-02662: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PINS_DEFENDER = 122

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PINS_DEFENDER = 122;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4679.

```text
9;
  ANALYSIS_TYPE_DISCOVERED_CHECK_ATTACK = 120;
  ANALYSIS_TYPE_EXPLOITS_PINNED_DEFENDER = 121;
  ANALYSIS_TYPE_PINS_DEFENDER = 122;
  ANALYSIS_TYPE_MAINTAINED_MATE = 123;
  ANALYSIS_TYPE_FORCES_LOSES_CASTLING_RIGHTS = 124;
  ANALYSIS_TYPE_WINS_MATERIAL_NOT_FREE = 125;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE_MATE = 126;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE_MATE = 127;
  ANALYSIS_TYPE_IGNORES_THREAT_MATE = 128;
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02663"></a>
## FND-02663: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MAINTAINED_MATE = 123

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_MAINTAINED_MATE = 123;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4716.

```text
TTACK = 120;
  ANALYSIS_TYPE_EXPLOITS_PINNED_DEFENDER = 121;
  ANALYSIS_TYPE_PINS_DEFENDER = 122;
  ANALYSIS_TYPE_MAINTAINED_MATE = 123;
  ANALYSIS_TYPE_FORCES_LOSES_CASTLING_RIGHTS = 124;
  ANALYSIS_TYPE_WINS_MATERIAL_NOT_FREE = 125;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE_MATE = 126;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE_MATE = 127;
  ANALYSIS_TYPE_IGNORES_THREAT_MATE = 128;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE_M
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02664"></a>
## FND-02664: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORCES_LOSES_CASTLING_RIGHTS = 124

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FORCES_LOSES_CASTLING_RIGHTS = 124;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4755.

```text
INNED_DEFENDER = 121;
  ANALYSIS_TYPE_PINS_DEFENDER = 122;
  ANALYSIS_TYPE_MAINTAINED_MATE = 123;
  ANALYSIS_TYPE_FORCES_LOSES_CASTLING_RIGHTS = 124;
  ANALYSIS_TYPE_WINS_MATERIAL_NOT_FREE = 125;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE_MATE = 126;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE_MATE = 127;
  ANALYSIS_TYPE_IGNORES_THREAT_MATE = 128;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE_MATE = 129;
  ANALYSIS_TYPE_BACK_RANK_MA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02665"></a>
## FND-02665: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_WINS_MATERIAL_NOT_FREE = 125

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_WINS_MATERIAL_NOT_FREE = 125;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4807.

```text
= 122;
  ANALYSIS_TYPE_MAINTAINED_MATE = 123;
  ANALYSIS_TYPE_FORCES_LOSES_CASTLING_RIGHTS = 124;
  ANALYSIS_TYPE_WINS_MATERIAL_NOT_FREE = 125;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE_MATE = 126;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE_MATE = 127;
  ANALYSIS_TYPE_IGNORES_THREAT_MATE = 128;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE_MATE = 129;
  ANALYSIS_TYPE_BACK_RANK_MATE = 130;
  ANALYSIS_TYPE_LOSES_MATERIAL_LOSING_POSI
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02666"></a>
## FND-02666: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE_MATE = 126

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE_MATE = 126;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4853.

```text
  ANALYSIS_TYPE_FORCES_LOSES_CASTLING_RIGHTS = 124;
  ANALYSIS_TYPE_WINS_MATERIAL_NOT_FREE = 125;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE_MATE = 126;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE_MATE = 127;
  ANALYSIS_TYPE_IGNORES_THREAT_MATE = 128;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE_MATE = 129;
  ANALYSIS_TYPE_BACK_RANK_MATE = 130;
  ANALYSIS_TYPE_LOSES_MATERIAL_LOSING_POSITION = 131;
  ANALYSIS_TYPE_LOSES_MATERIAL_WIN
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02667"></a>
## FND-02667: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE_MATE = 127

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE_MATE = 127;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4906.

```text
 ANALYSIS_TYPE_WINS_MATERIAL_NOT_FREE = 125;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE_MATE = 126;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE_MATE = 127;
  ANALYSIS_TYPE_IGNORES_THREAT_MATE = 128;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE_MATE = 129;
  ANALYSIS_TYPE_BACK_RANK_MATE = 130;
  ANALYSIS_TYPE_LOSES_MATERIAL_LOSING_POSITION = 131;
  ANALYSIS_TYPE_LOSES_MATERIAL_WINNING_POSITION = 132;
  ANALYSIS_TYPE_MISSES_MATERIAL_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02668"></a>
## FND-02668: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_IGNORES_THREAT_MATE = 128

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_IGNORES_THREAT_MATE = 128;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 4959.

```text
IS_TYPE_DIRECT_SACRIFICE_CAPTURE_MATE = 126;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE_MATE = 127;
  ANALYSIS_TYPE_IGNORES_THREAT_MATE = 128;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE_MATE = 129;
  ANALYSIS_TYPE_BACK_RANK_MATE = 130;
  ANALYSIS_TYPE_LOSES_MATERIAL_LOSING_POSITION = 131;
  ANALYSIS_TYPE_LOSES_MATERIAL_WINNING_POSITION = 132;
  ANALYSIS_TYPE_MISSES_MATERIAL_LOSING_POSITION = 133;
  ANALYSIS_TYPE_MISSES_MATERIA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02669"></a>
## FND-02669: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_INDIRECT_SACRIFICE_MATE = 129

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_INDIRECT_SACRIFICE_MATE = 129;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5002.

```text
;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE_MATE = 127;
  ANALYSIS_TYPE_IGNORES_THREAT_MATE = 128;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE_MATE = 129;
  ANALYSIS_TYPE_BACK_RANK_MATE = 130;
  ANALYSIS_TYPE_LOSES_MATERIAL_LOSING_POSITION = 131;
  ANALYSIS_TYPE_LOSES_MATERIAL_WINNING_POSITION = 132;
  ANALYSIS_TYPE_MISSES_MATERIAL_LOSING_POSITION = 133;
  ANALYSIS_TYPE_MISSES_MATERIAL_WINNING_POSITION = 134;
  ANALYSIS_TYPE_C
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02670"></a>
## FND-02670: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_BACK_RANK_MATE = 130

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_BACK_RANK_MATE = 130;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5049.

```text
 = 127;
  ANALYSIS_TYPE_IGNORES_THREAT_MATE = 128;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE_MATE = 129;
  ANALYSIS_TYPE_BACK_RANK_MATE = 130;
  ANALYSIS_TYPE_LOSES_MATERIAL_LOSING_POSITION = 131;
  ANALYSIS_TYPE_LOSES_MATERIAL_WINNING_POSITION = 132;
  ANALYSIS_TYPE_MISSES_MATERIAL_LOSING_POSITION = 133;
  ANALYSIS_TYPE_MISSES_MATERIAL_WINNING_POSITION = 134;
  ANALYSIS_TYPE_CHECKS_AWAY_DEFENDER = 135;
  ANALYSIS_TYPE_PUNI
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02671"></a>
## FND-02671: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_LOSES_MATERIAL_LOSING_POSITION = 131

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_LOSES_MATERIAL_LOSING_POSITION = 131;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5087.

```text
_MATE = 128;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE_MATE = 129;
  ANALYSIS_TYPE_BACK_RANK_MATE = 130;
  ANALYSIS_TYPE_LOSES_MATERIAL_LOSING_POSITION = 131;
  ANALYSIS_TYPE_LOSES_MATERIAL_WINNING_POSITION = 132;
  ANALYSIS_TYPE_MISSES_MATERIAL_LOSING_POSITION = 133;
  ANALYSIS_TYPE_MISSES_MATERIAL_WINNING_POSITION = 134;
  ANALYSIS_TYPE_CHECKS_AWAY_DEFENDER = 135;
  ANALYSIS_TYPE_PUNISH_MOVE_REFUTED_BY = 136;
  ANALYSIS_T
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02672"></a>
## FND-02672: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_LOSES_MATERIAL_WINNING_POSITION = 132

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_LOSES_MATERIAL_WINNING_POSITION = 132;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5141.

```text
 129;
  ANALYSIS_TYPE_BACK_RANK_MATE = 130;
  ANALYSIS_TYPE_LOSES_MATERIAL_LOSING_POSITION = 131;
  ANALYSIS_TYPE_LOSES_MATERIAL_WINNING_POSITION = 132;
  ANALYSIS_TYPE_MISSES_MATERIAL_LOSING_POSITION = 133;
  ANALYSIS_TYPE_MISSES_MATERIAL_WINNING_POSITION = 134;
  ANALYSIS_TYPE_CHECKS_AWAY_DEFENDER = 135;
  ANALYSIS_TYPE_PUNISH_MOVE_REFUTED_BY = 136;
  ANALYSIS_TYPE_PUNISH_MOVE_FALLBACK = 137;
  ANALYSIS_TYPE_PUNISH
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02673"></a>
## FND-02673: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MISSES_MATERIAL_LOSING_POSITION = 133

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_MISSES_MATERIAL_LOSING_POSITION = 133;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5196.

```text
TYPE_LOSES_MATERIAL_LOSING_POSITION = 131;
  ANALYSIS_TYPE_LOSES_MATERIAL_WINNING_POSITION = 132;
  ANALYSIS_TYPE_MISSES_MATERIAL_LOSING_POSITION = 133;
  ANALYSIS_TYPE_MISSES_MATERIAL_WINNING_POSITION = 134;
  ANALYSIS_TYPE_CHECKS_AWAY_DEFENDER = 135;
  ANALYSIS_TYPE_PUNISH_MOVE_REFUTED_BY = 136;
  ANALYSIS_TYPE_PUNISH_MOVE_FALLBACK = 137;
  ANALYSIS_TYPE_PUNISH_MOVE_NONE = 138;
  ANALYSIS_TYPE_REMOVES_DEFENDER = 14
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02674"></a>
## FND-02674: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MISSES_MATERIAL_WINNING_POSITION = 134

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_MISSES_MATERIAL_WINNING_POSITION = 134;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 5251.

```text
YPE_LOSES_MATERIAL_WINNING_POSITION = 132;
  ANALYSIS_TYPE_MISSES_MATERIAL_LOSING_POSITION = 133;
  ANALYSIS_TYPE_MISSES_MATERIAL_WINNING_POSITION = 134;
  ANALYSIS_TYPE_CHECKS_AWAY_DEFENDER = 135;
  ANALYSIS_TYPE_PUNISH_MOVE_REFUTED_BY = 136;
  ANALYSIS_TYPE_PUNISH_MOVE_FALLBACK = 137;
  ANALYSIS_TYPE_PUNISH_MOVE_NONE = 138;
  ANALYSIS_TYPE_REMOVES_DEFENDER = 140;
  ANALYSIS_TYPE_REMOVES_MATE_DEFENDER = 141;
  ANALY
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
