# data_models — findings 2701–2800

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-02975"></a>
## FND-02975: chesscom.explanation_engine.v1.MatcherRule.tags = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.AnalysisType tags = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3078.

```text
double weight = 4;
  }
  repeated .chesscom.explanation_engine.v1.Circumstance circumstances = 1;
  repeated .chesscom.explanation_engine.v1.AnalysisType tags = 2;
  repeated .chesscom.explanation_engine.v1.MoveClassification move_classifications = 3;
}

message NnMultRule {
  oneof body {
  .chesscom.explanation_engine.v1.PieceGate pieces = 1;
  .chesscom.explanation_engine.v1.MatcherGroup board_events = 2;
  }
}

m
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02976"></a>
## FND-02976: chesscom.explanation_engine.v1.MatcherRule.move_classifications = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.MoveClassification move_classifications = 3;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3144.

```text
Circumstance circumstances = 1;
  repeated .chesscom.explanation_engine.v1.AnalysisType tags = 2;
  repeated .chesscom.explanation_engine.v1.MoveClassification move_classifications = 3;
}

message NnMultRule {
  oneof body {
  .chesscom.explanation_engine.v1.PieceGate pieces = 1;
  .chesscom.explanation_engine.v1.MatcherGroup board_events = 2;
  }
}

message MatcherGroup {
  repeated .chesscom.explanation_engine.v1.M
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02977"></a>
## FND-02977: message declaration: chesscom.explanation_engine.v1.NnMultRule

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NnMultRule {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3233.

```text
ags = 2;
  repeated .chesscom.explanation_engine.v1.MoveClassification move_classifications = 3;
}

message NnMultRule {
  oneof body {
  .chesscom.explanation_engine.v1.PieceGate pieces = 1;
  .chesscom.explanation_engine.v1.MatcherGroup board_events = 2;
  }
}

message MatcherGroup {
  repeated .chesscom.explanation_engine.v1.MatcherRule matchers = 1;
}

message PieceGate {
  repeated .chesscom.chess.v1.PieceType p
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02978"></a>
## FND-02978: oneof declaration: chesscom.explanation_engine.v1.NnMultRule.body

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof body {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3256.

```text
esscom.explanation_engine.v1.MoveClassification move_classifications = 3;
}

message NnMultRule {
  oneof body {
  .chesscom.explanation_engine.v1.PieceGate pieces = 1;
  .chesscom.explanation_engine.v1.MatcherGroup board_events = 2;
  }
}

message MatcherGroup {
  repeated .chesscom.explanation_engine.v1.MatcherRule matchers = 1;
}

message PieceGate {
  repeated .chesscom.chess.v1.PieceType pieces = 1;
}

message P
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02979"></a>
## FND-02979: chesscom.explanation_engine.v1.NnMultRule.pieces = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PieceGate pieces = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3271.

```text
ion_engine.v1.MoveClassification move_classifications = 3;
}

message NnMultRule {
  oneof body {
  .chesscom.explanation_engine.v1.PieceGate pieces = 1;
  .chesscom.explanation_engine.v1.MatcherGroup board_events = 2;
  }
}

message MatcherGroup {
  repeated .chesscom.explanation_engine.v1.MatcherRule matchers = 1;
}

message PieceGate {
  repeated .chesscom.chess.v1.PieceType pieces = 1;
}

message PieceBonus {
  o
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02980"></a>
## FND-02980: chesscom.explanation_engine.v1.NnMultRule.board_events = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.MatcherGroup board_events = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3327.

```text
3;
}

message NnMultRule {
  oneof body {
  .chesscom.explanation_engine.v1.PieceGate pieces = 1;
  .chesscom.explanation_engine.v1.MatcherGroup board_events = 2;
  }
}

message MatcherGroup {
  repeated .chesscom.explanation_engine.v1.MatcherRule matchers = 1;
}

message PieceGate {
  repeated .chesscom.chess.v1.PieceType pieces = 1;
}

message PieceBonus {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  o
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02981"></a>
## FND-02981: message declaration: chesscom.explanation_engine.v1.MatcherGroup

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MatcherGroup {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3397.

```text
ne.v1.PieceGate pieces = 1;
  .chesscom.explanation_engine.v1.MatcherGroup board_events = 2;
  }
}

message MatcherGroup {
  repeated .chesscom.explanation_engine.v1.MatcherRule matchers = 1;
}

message PieceGate {
  repeated .chesscom.chess.v1.PieceType pieces = 1;
}

message PieceBonus {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double bonus = 2;
}

message EvalThreshold {
  optional int32 
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02982"></a>
## FND-02982: chesscom.explanation_engine.v1.MatcherGroup.matchers = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.MatcherRule matchers = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3422.

```text
1;
  .chesscom.explanation_engine.v1.MatcherGroup board_events = 2;
  }
}

message MatcherGroup {
  repeated .chesscom.explanation_engine.v1.MatcherRule matchers = 1;
}

message PieceGate {
  repeated .chesscom.chess.v1.PieceType pieces = 1;
}

message PieceBonus {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double bonus = 2;
}

message EvalThreshold {
  optional int32 cp = 1;
  optional double
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02983"></a>
## FND-02983: message declaration: chesscom.explanation_engine.v1.PieceGate

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PieceGate {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3492.

```text
}
}

message MatcherGroup {
  repeated .chesscom.explanation_engine.v1.MatcherRule matchers = 1;
}

message PieceGate {
  repeated .chesscom.chess.v1.PieceType pieces = 1;
}

message PieceBonus {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double bonus = 2;
}

message EvalThreshold {
  optional int32 cp = 1;
  optional double penalty = 2;
}

message EvalRange {
  optional int32 min_cp = 1;
  op
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02984"></a>
## FND-02984: chesscom.explanation_engine.v1.PieceGate.pieces = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.PieceType pieces = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3514.

```text
oup {
  repeated .chesscom.explanation_engine.v1.MatcherRule matchers = 1;
}

message PieceGate {
  repeated .chesscom.chess.v1.PieceType pieces = 1;
}

message PieceBonus {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double bonus = 2;
}

message EvalThreshold {
  optional int32 cp = 1;
  optional double penalty = 2;
}

message EvalRange {
  optional int32 min_cp = 1;
  optional int32 max_cp = 
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02985"></a>
## FND-02985: message declaration: chesscom.explanation_engine.v1.PieceBonus

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PieceBonus {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3567.

```text
herRule matchers = 1;
}

message PieceGate {
  repeated .chesscom.chess.v1.PieceType pieces = 1;
}

message PieceBonus {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double bonus = 2;
}

message EvalThreshold {
  optional int32 cp = 1;
  optional double penalty = 2;
}

message EvalRange {
  optional int32 min_cp = 1;
  optional int32 max_cp = 2;
}

message BotMoveBehaviorContext {
  oneof _game_
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02986"></a>
## FND-02986: chesscom.explanation_engine.v1.PieceBonus.piece_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.PieceType piece_type = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3590.

```text


message PieceGate {
  repeated .chesscom.chess.v1.PieceType pieces = 1;
}

message PieceBonus {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double bonus = 2;
}

message EvalThreshold {
  optional int32 cp = 1;
  optional double penalty = 2;
}

message EvalRange {
  optional int32 min_cp = 1;
  optional int32 max_cp = 2;
}

message BotMoveBehaviorContext {
  oneof _game_phase {
  .chesscom.che
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02987"></a>
## FND-02987: chesscom.explanation_engine.v1.PieceBonus.bonus = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double bonus = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3646.

```text
eType pieces = 1;
}

message PieceBonus {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double bonus = 2;
}

message EvalThreshold {
  optional int32 cp = 1;
  optional double penalty = 2;
}

message EvalRange {
  optional int32 min_cp = 1;
  optional int32 max_cp = 2;
}

message BotMoveBehaviorContext {
  oneof _game_phase {
  .chesscom.chess.v1.GamePhase game_phase = 1;
  }
  oneof _eval_range 
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02988"></a>
## FND-02988: message declaration: chesscom.explanation_engine.v1.EvalThreshold

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EvalThreshold {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3676.

```text
ieceBonus {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double bonus = 2;
}

message EvalThreshold {
  optional int32 cp = 1;
  optional double penalty = 2;
}

message EvalRange {
  optional int32 min_cp = 1;
  optional int32 max_cp = 2;
}

message BotMoveBehaviorContext {
  oneof _game_phase {
  .chesscom.chess.v1.GamePhase game_phase = 1;
  }
  oneof _eval_range {
  .chesscom.explanation_engi
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02989"></a>
## FND-02989: chesscom.explanation_engine.v1.EvalThreshold.cp = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 cp = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3702.

```text
esscom.chess.v1.PieceType piece_type = 1;
  optional double bonus = 2;
}

message EvalThreshold {
  optional int32 cp = 1;
  optional double penalty = 2;
}

message EvalRange {
  optional int32 min_cp = 1;
  optional int32 max_cp = 2;
}

message BotMoveBehaviorContext {
  oneof _game_phase {
  .chesscom.chess.v1.GamePhase game_phase = 1;
  }
  oneof _eval_range {
  .chesscom.explanation_engine.v1.EvalRange eval_range
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02990"></a>
## FND-02990: chesscom.explanation_engine.v1.EvalThreshold.penalty = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double penalty = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3727.

```text
 piece_type = 1;
  optional double bonus = 2;
}

message EvalThreshold {
  optional int32 cp = 1;
  optional double penalty = 2;
}

message EvalRange {
  optional int32 min_cp = 1;
  optional int32 max_cp = 2;
}

message BotMoveBehaviorContext {
  oneof _game_phase {
  .chesscom.chess.v1.GamePhase game_phase = 1;
  }
  oneof _eval_range {
  .chesscom.explanation_engine.v1.EvalRange eval_range = 2;
  }
  repeated .che
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02991"></a>
## FND-02991: message declaration: chesscom.explanation_engine.v1.EvalRange

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EvalRange {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3759.

```text
le bonus = 2;
}

message EvalThreshold {
  optional int32 cp = 1;
  optional double penalty = 2;
}

message EvalRange {
  optional int32 min_cp = 1;
  optional int32 max_cp = 2;
}

message BotMoveBehaviorContext {
  oneof _game_phase {
  .chesscom.chess.v1.GamePhase game_phase = 1;
  }
  oneof _eval_range {
  .chesscom.explanation_engine.v1.EvalRange eval_range = 2;
  }
  repeated .chesscom.explanation_engine.v1.Matc
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02992"></a>
## FND-02992: chesscom.explanation_engine.v1.EvalRange.min_cp = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 min_cp = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3781.

```text
ge EvalThreshold {
  optional int32 cp = 1;
  optional double penalty = 2;
}

message EvalRange {
  optional int32 min_cp = 1;
  optional int32 max_cp = 2;
}

message BotMoveBehaviorContext {
  oneof _game_phase {
  .chesscom.chess.v1.GamePhase game_phase = 1;
  }
  oneof _eval_range {
  .chesscom.explanation_engine.v1.EvalRange eval_range = 2;
  }
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 3;
  r
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02993"></a>
## FND-02993: chesscom.explanation_engine.v1.EvalRange.max_cp = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 max_cp = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3810.

```text
 int32 cp = 1;
  optional double penalty = 2;
}

message EvalRange {
  optional int32 min_cp = 1;
  optional int32 max_cp = 2;
}

message BotMoveBehaviorContext {
  oneof _game_phase {
  .chesscom.chess.v1.GamePhase game_phase = 1;
  }
  oneof _eval_range {
  .chesscom.explanation_engine.v1.EvalRange eval_range = 2;
  }
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 3;
  repeated .chesscom.explanation
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02994"></a>
## FND-02994: message declaration: chesscom.explanation_engine.v1.BotMoveBehaviorContext

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotMoveBehaviorContext {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3840.

```text
le penalty = 2;
}

message EvalRange {
  optional int32 min_cp = 1;
  optional int32 max_cp = 2;
}

message BotMoveBehaviorContext {
  oneof _game_phase {
  .chesscom.chess.v1.GamePhase game_phase = 1;
  }
  oneof _eval_range {
  .chesscom.explanation_engine.v1.EvalRange eval_range = 2;
  }
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 3;
  repeated .chesscom.explanation_engine.v1.PositionShape posit
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02995"></a>
## FND-02995: oneof declaration: chesscom.explanation_engine.v1.BotMoveBehaviorContext._game_phase

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_phase {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3875.

```text
e {
  optional int32 min_cp = 1;
  optional int32 max_cp = 2;
}

message BotMoveBehaviorContext {
  oneof _game_phase {
  .chesscom.chess.v1.GamePhase game_phase = 1;
  }
  oneof _eval_range {
  .chesscom.explanation_engine.v1.EvalRange eval_range = 2;
  }
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 3;
  repeated .chesscom.explanation_engine.v1.PositionShape position_shapes = 4;
}

message LegacyBo
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02996"></a>
## FND-02996: chesscom.explanation_engine.v1.BotMoveBehaviorContext.game_phase = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.GamePhase game_phase = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3897.

```text
in_cp = 1;
  optional int32 max_cp = 2;
}

message BotMoveBehaviorContext {
  oneof _game_phase {
  .chesscom.chess.v1.GamePhase game_phase = 1;
  }
  oneof _eval_range {
  .chesscom.explanation_engine.v1.EvalRange eval_range = 2;
  }
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 3;
  repeated .chesscom.explanation_engine.v1.PositionShape position_shapes = 4;
}

message LegacyBot {
  optional int32 r
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02997"></a>
## FND-02997: oneof declaration: chesscom.explanation_engine.v1.BotMoveBehaviorContext._eval_range

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _eval_range {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3948.

```text
BotMoveBehaviorContext {
  oneof _game_phase {
  .chesscom.chess.v1.GamePhase game_phase = 1;
  }
  oneof _eval_range {
  .chesscom.explanation_engine.v1.EvalRange eval_range = 2;
  }
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 3;
  repeated .chesscom.explanation_engine.v1.PositionShape position_shapes = 4;
}

message LegacyBot {
  optional int32 rating = 1;
  optional .chesscom.explanation_engine.
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02998"></a>
## FND-02998: chesscom.explanation_engine.v1.BotMoveBehaviorContext.eval_range = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.EvalRange eval_range = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3970.

```text
 {
  oneof _game_phase {
  .chesscom.chess.v1.GamePhase game_phase = 1;
  }
  oneof _eval_range {
  .chesscom.explanation_engine.v1.EvalRange eval_range = 2;
  }
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 3;
  repeated .chesscom.explanation_engine.v1.PositionShape position_shapes = 4;
}

message LegacyBot {
  optional int32 rating = 1;
  optional .chesscom.explanation_engine.v1.BotPersonality pers
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02999"></a>
## FND-02999: chesscom.explanation_engine.v1.BotMoveBehaviorContext.rules = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.MatcherRule rules = 3;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4034.

```text
se = 1;
  }
  oneof _eval_range {
  .chesscom.explanation_engine.v1.EvalRange eval_range = 2;
  }
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 3;
  repeated .chesscom.explanation_engine.v1.PositionShape position_shapes = 4;
}

message LegacyBot {
  optional int32 rating = 1;
  optional .chesscom.explanation_engine.v1.BotPersonality personality = 2;
  optional double weight = 3;
}

message NnConfig {
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03000"></a>
## FND-03000: chesscom.explanation_engine.v1.BotMoveBehaviorContext.position_shapes = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.PositionShape position_shapes = 4;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4100.

```text
1.EvalRange eval_range = 2;
  }
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 3;
  repeated .chesscom.explanation_engine.v1.PositionShape position_shapes = 4;
}

message LegacyBot {
  optional int32 rating = 1;
  optional .chesscom.explanation_engine.v1.BotPersonality personality = 2;
  optional double weight = 3;
}

message NnConfig {
  optional .chesscom.explanation_engine.v1.ModelArch arch = 1;
  
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03001"></a>
## FND-03001: message declaration: chesscom.explanation_engine.v1.LegacyBot

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LegacyBot {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4179.

```text
herRule rules = 3;
  repeated .chesscom.explanation_engine.v1.PositionShape position_shapes = 4;
}

message LegacyBot {
  optional int32 rating = 1;
  optional .chesscom.explanation_engine.v1.BotPersonality personality = 2;
  optional double weight = 3;
}

message NnConfig {
  optional .chesscom.explanation_engine.v1.ModelArch arch = 1;
  optional string model = 2;
  optional int32 rating = 3;
  optional double weigh
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03002"></a>
## FND-03002: chesscom.explanation_engine.v1.LegacyBot.rating = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 rating = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4201.

```text
epeated .chesscom.explanation_engine.v1.PositionShape position_shapes = 4;
}

message LegacyBot {
  optional int32 rating = 1;
  optional .chesscom.explanation_engine.v1.BotPersonality personality = 2;
  optional double weight = 3;
}

message NnConfig {
  optional .chesscom.explanation_engine.v1.ModelArch arch = 1;
  optional string model = 2;
  optional int32 rating = 3;
  optional double weight = 4;
  optional int3
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03003"></a>
## FND-03003: chesscom.explanation_engine.v1.LegacyBot.personality = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.BotPersonality personality = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4230.

```text
_engine.v1.PositionShape position_shapes = 4;
}

message LegacyBot {
  optional int32 rating = 1;
  optional .chesscom.explanation_engine.v1.BotPersonality personality = 2;
  optional double weight = 3;
}

message NnConfig {
  optional .chesscom.explanation_engine.v1.ModelArch arch = 1;
  optional string model = 2;
  optional int32 rating = 3;
  optional double weight = 4;
  optional int32 charm_input_search_depth = 
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03004"></a>
## FND-03004: chesscom.explanation_engine.v1.LegacyBot.weight = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double weight = 3;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2316.

```text
e.v1.CoherenceConfig coherence = 11;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 4;
  repeated .chesscom.explanation_engine.v1.PieceBonus piece_bonuses = 5;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 8;
}

message NnMultBehavior {
  oneof _max_eval_drop {
  int32 max_eval_drop
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03005"></a>
## FND-03005: message declaration: chesscom.explanation_engine.v1.NnConfig

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NnConfig {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4336.

```text
al .chesscom.explanation_engine.v1.BotPersonality personality = 2;
  optional double weight = 3;
}

message NnConfig {
  optional .chesscom.explanation_engine.v1.ModelArch arch = 1;
  optional string model = 2;
  optional int32 rating = 3;
  optional double weight = 4;
  optional int32 charm_input_search_depth = 5;
  optional double temperature = 6;
  optional string rating_scale = 7;
  optional double time_taken_mul
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03006"></a>
## FND-03006: chesscom.explanation_engine.v1.NnConfig.arch = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.ModelArch arch = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4357.

```text
ion_engine.v1.BotPersonality personality = 2;
  optional double weight = 3;
}

message NnConfig {
  optional .chesscom.explanation_engine.v1.ModelArch arch = 1;
  optional string model = 2;
  optional int32 rating = 3;
  optional double weight = 4;
  optional int32 charm_input_search_depth = 5;
  optional double temperature = 6;
  optional string rating_scale = 7;
  optional double time_taken_multiplier = 8;
}

messa
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03007"></a>
## FND-03007: chesscom.explanation_engine.v1.NnConfig.model = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string model = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4420.

```text
 weight = 3;
}

message NnConfig {
  optional .chesscom.explanation_engine.v1.ModelArch arch = 1;
  optional string model = 2;
  optional int32 rating = 3;
  optional double weight = 4;
  optional int32 charm_input_search_depth = 5;
  optional double temperature = 6;
  optional string rating_scale = 7;
  optional double time_taken_multiplier = 8;
}

message CoherenceConfig {
  optional int32 n_back = 1;
  optional .c
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03008"></a>
## FND-03008: chesscom.explanation_engine.v1.NnConfig.rating = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 rating = 3;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4449.

```text
fig {
  optional .chesscom.explanation_engine.v1.ModelArch arch = 1;
  optional string model = 2;
  optional int32 rating = 3;
  optional double weight = 4;
  optional int32 charm_input_search_depth = 5;
  optional double temperature = 6;
  optional string rating_scale = 7;
  optional double time_taken_multiplier = 8;
}

message CoherenceConfig {
  optional int32 n_back = 1;
  optional .chesscom.explanation_engine.v1
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03009"></a>
## FND-03009: chesscom.explanation_engine.v1.NnConfig.weight = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double weight = 4;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4478.

```text
planation_engine.v1.ModelArch arch = 1;
  optional string model = 2;
  optional int32 rating = 3;
  optional double weight = 4;
  optional int32 charm_input_search_depth = 5;
  optional double temperature = 6;
  optional string rating_scale = 7;
  optional double time_taken_multiplier = 8;
}

message CoherenceConfig {
  optional int32 n_back = 1;
  optional .chesscom.explanation_engine.v1.ModelArch arch = 2;
  option
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03010"></a>
## FND-03010: chesscom.explanation_engine.v1.NnConfig.charm_input_search_depth = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 charm_input_search_depth = 5;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4508.

```text
arch = 1;
  optional string model = 2;
  optional int32 rating = 3;
  optional double weight = 4;
  optional int32 charm_input_search_depth = 5;
  optional double temperature = 6;
  optional string rating_scale = 7;
  optional double time_taken_multiplier = 8;
}

message CoherenceConfig {
  optional int32 n_back = 1;
  optional .chesscom.explanation_engine.v1.ModelArch arch = 2;
  optional string model = 3;
  optiona
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03011"></a>
## FND-03011: chesscom.explanation_engine.v1.NnConfig.temperature = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double temperature = 6;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4555.

```text
al int32 rating = 3;
  optional double weight = 4;
  optional int32 charm_input_search_depth = 5;
  optional double temperature = 6;
  optional string rating_scale = 7;
  optional double time_taken_multiplier = 8;
}

message CoherenceConfig {
  optional int32 n_back = 1;
  optional .chesscom.explanation_engine.v1.ModelArch arch = 2;
  optional string model = 3;
  optional int32 rating = 4;
  optional int32 charm_inpu
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03012"></a>
## FND-03012: chesscom.explanation_engine.v1.NnConfig.rating_scale = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string rating_scale = 7;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4590.

```text
ble weight = 4;
  optional int32 charm_input_search_depth = 5;
  optional double temperature = 6;
  optional string rating_scale = 7;
  optional double time_taken_multiplier = 8;
}

message CoherenceConfig {
  optional int32 n_back = 1;
  optional .chesscom.explanation_engine.v1.ModelArch arch = 2;
  optional string model = 3;
  optional int32 rating = 4;
  optional int32 charm_input_search_depth = 5;
  optional doub
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03013"></a>
## FND-03013: chesscom.explanation_engine.v1.NnConfig.time_taken_multiplier = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double time_taken_multiplier = 8;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4626.

```text
rm_input_search_depth = 5;
  optional double temperature = 6;
  optional string rating_scale = 7;
  optional double time_taken_multiplier = 8;
}

message CoherenceConfig {
  optional int32 n_back = 1;
  optional .chesscom.explanation_engine.v1.ModelArch arch = 2;
  optional string model = 3;
  optional int32 rating = 4;
  optional int32 charm_input_search_depth = 5;
  optional double weight = 6;
}

```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03014"></a>
## FND-03014: message declaration: chesscom.explanation_engine.v1.CoherenceConfig

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoherenceConfig {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4672.

```text
emperature = 6;
  optional string rating_scale = 7;
  optional double time_taken_multiplier = 8;
}

message CoherenceConfig {
  optional int32 n_back = 1;
  optional .chesscom.explanation_engine.v1.ModelArch arch = 2;
  optional string model = 3;
  optional int32 rating = 4;
  optional int32 charm_input_search_depth = 5;
  optional double weight = 6;
}

```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03015"></a>
## FND-03015: chesscom.explanation_engine.v1.CoherenceConfig.n_back = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 n_back = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4700.

```text
tring rating_scale = 7;
  optional double time_taken_multiplier = 8;
}

message CoherenceConfig {
  optional int32 n_back = 1;
  optional .chesscom.explanation_engine.v1.ModelArch arch = 2;
  optional string model = 3;
  optional int32 rating = 4;
  optional int32 charm_input_search_depth = 5;
  optional double weight = 6;
}

```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03016"></a>
## FND-03016: chesscom.explanation_engine.v1.CoherenceConfig.arch = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.ModelArch arch = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4729.

```text
ional double time_taken_multiplier = 8;
}

message CoherenceConfig {
  optional int32 n_back = 1;
  optional .chesscom.explanation_engine.v1.ModelArch arch = 2;
  optional string model = 3;
  optional int32 rating = 4;
  optional int32 charm_input_search_depth = 5;
  optional double weight = 6;
}

```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03017"></a>
## FND-03017: chesscom.explanation_engine.v1.CoherenceConfig.model = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string model = 3;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4792.

```text
fig {
  optional int32 n_back = 1;
  optional .chesscom.explanation_engine.v1.ModelArch arch = 2;
  optional string model = 3;
  optional int32 rating = 4;
  optional int32 charm_input_search_depth = 5;
  optional double weight = 6;
}

```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03018"></a>
## FND-03018: chesscom.explanation_engine.v1.CoherenceConfig.rating = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 rating = 4;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4821.

```text
 = 1;
  optional .chesscom.explanation_engine.v1.ModelArch arch = 2;
  optional string model = 3;
  optional int32 rating = 4;
  optional int32 charm_input_search_depth = 5;
  optional double weight = 6;
}

```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03019"></a>
## FND-03019: chesscom.explanation_engine.v1.CoherenceConfig.charm_input_search_depth = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 charm_input_search_depth = 5;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4508.

```text
arch = 1;
  optional string model = 2;
  optional int32 rating = 3;
  optional double weight = 4;
  optional int32 charm_input_search_depth = 5;
  optional double temperature = 6;
  optional string rating_scale = 7;
  optional double time_taken_multiplier = 8;
}

message CoherenceConfig {
  optional int32 n_back = 1;
  optional .chesscom.explanation_engine.v1.ModelArch arch = 2;
  optional string model = 3;
  optiona
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03020"></a>
## FND-03020: chesscom.explanation_engine.v1.CoherenceConfig.weight = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double weight = 6;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 4897.

```text
nal string model = 3;
  optional int32 rating = 4;
  optional int32 charm_input_search_depth = 5;
  optional double weight = 6;
}

```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03021"></a>
## FND-03021: enum declaration: chesscom.explanation_engine.v1.CeeInternalComponent

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CeeInternalComponent {

### Evidence

- **SRC-0340** `research/proto/chesscom/explanation_engine/v1/cee_internal_component.proto` — [preserved redacted evidence](../evidence/text/470e21f9637b87367f386a2e6d2c25353ca0a58768fbe11166b756dc3576e7e9.proto)
  Character offset 131.

```text
_engine/v1/cee_internal_component.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum CeeInternalComponent {
  CEE_INTERNAL_COMPONENT_UNSPECIFIED = 0;
  CEE_INTERNAL_COMPONENT_LUA = 1;
  CEE_INTERNAL_COMPONENT_POSITION_DIFFICULTY = 2;
  CEE_INTERNAL_COMPONENT_TORCH_SMALL = 3;
  CEE_INTERNAL_COMPONENT_TORCH_LARGE = 4;
  CEE_INTERNAL_COMPONENT_KOMODO = 5;
  CEE_INTERNAL_COMPONENT_INTERNAL_FEATURES = 
```

**Source references:** SRC-0340, SRC-1311  
**URL references:** None independently associated  
**Related findings:** FND-03022, FND-03023

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03022"></a>
## FND-03022: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CEE_INTERNAL_COMPONENT_UNSPECIFIED = 0;

### Evidence

- **SRC-0340** `research/proto/chesscom/explanation_engine/v1/cee_internal_component.proto` — [preserved redacted evidence](../evidence/text/470e21f9637b87367f386a2e6d2c25353ca0a58768fbe11166b756dc3576e7e9.proto)
  Character offset 161.

```text
ent.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum CeeInternalComponent {
  CEE_INTERNAL_COMPONENT_UNSPECIFIED = 0;
  CEE_INTERNAL_COMPONENT_LUA = 1;
  CEE_INTERNAL_COMPONENT_POSITION_DIFFICULTY = 2;
  CEE_INTERNAL_COMPONENT_TORCH_SMALL = 3;
  CEE_INTERNAL_COMPONENT_TORCH_LARGE = 4;
  CEE_INTERNAL_COMPONENT_KOMODO = 5;
  CEE_INTERNAL_COMPONENT_INTERNAL_FEATURES = 6;
}

```

**Source references:** SRC-0340, SRC-1311  
**URL references:** None independently associated  
**Related findings:** FND-03021, FND-03023

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03023"></a>
## FND-03023: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_LUA = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CEE_INTERNAL_COMPONENT_LUA = 1;

### Evidence

- **SRC-0340** `research/proto/chesscom/explanation_engine/v1/cee_internal_component.proto` — [preserved redacted evidence](../evidence/text/470e21f9637b87367f386a2e6d2c25353ca0a58768fbe11166b756dc3576e7e9.proto)
  Character offset 203.

```text
com.explanation_engine.v1;

enum CeeInternalComponent {
  CEE_INTERNAL_COMPONENT_UNSPECIFIED = 0;
  CEE_INTERNAL_COMPONENT_LUA = 1;
  CEE_INTERNAL_COMPONENT_POSITION_DIFFICULTY = 2;
  CEE_INTERNAL_COMPONENT_TORCH_SMALL = 3;
  CEE_INTERNAL_COMPONENT_TORCH_LARGE = 4;
  CEE_INTERNAL_COMPONENT_KOMODO = 5;
  CEE_INTERNAL_COMPONENT_INTERNAL_FEATURES = 6;
}

```

**Source references:** SRC-0340, SRC-1311  
**URL references:** None independently associated  
**Related findings:** FND-03021, FND-03022

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03024"></a>
## FND-03024: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_POSITION_DIFFICULTY = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CEE_INTERNAL_COMPONENT_POSITION_DIFFICULTY = 2;

### Evidence

- **SRC-0340** `research/proto/chesscom/explanation_engine/v1/cee_internal_component.proto` — [preserved redacted evidence](../evidence/text/470e21f9637b87367f386a2e6d2c25353ca0a58768fbe11166b756dc3576e7e9.proto)
  Character offset 237.

```text
eeInternalComponent {
  CEE_INTERNAL_COMPONENT_UNSPECIFIED = 0;
  CEE_INTERNAL_COMPONENT_LUA = 1;
  CEE_INTERNAL_COMPONENT_POSITION_DIFFICULTY = 2;
  CEE_INTERNAL_COMPONENT_TORCH_SMALL = 3;
  CEE_INTERNAL_COMPONENT_TORCH_LARGE = 4;
  CEE_INTERNAL_COMPONENT_KOMODO = 5;
  CEE_INTERNAL_COMPONENT_INTERNAL_FEATURES = 6;
}

```

**Source references:** SRC-0340, SRC-1311  
**URL references:** None independently associated  
**Related findings:** FND-03021, FND-03022, FND-03023

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03025"></a>
## FND-03025: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_TORCH_SMALL = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CEE_INTERNAL_COMPONENT_TORCH_SMALL = 3;

### Evidence

- **SRC-0340** `research/proto/chesscom/explanation_engine/v1/cee_internal_component.proto` — [preserved redacted evidence](../evidence/text/470e21f9637b87367f386a2e6d2c25353ca0a58768fbe11166b756dc3576e7e9.proto)
  Character offset 287.

```text
PECIFIED = 0;
  CEE_INTERNAL_COMPONENT_LUA = 1;
  CEE_INTERNAL_COMPONENT_POSITION_DIFFICULTY = 2;
  CEE_INTERNAL_COMPONENT_TORCH_SMALL = 3;
  CEE_INTERNAL_COMPONENT_TORCH_LARGE = 4;
  CEE_INTERNAL_COMPONENT_KOMODO = 5;
  CEE_INTERNAL_COMPONENT_INTERNAL_FEATURES = 6;
}

```

**Source references:** SRC-0340, SRC-1311  
**URL references:** None independently associated  
**Related findings:** FND-03021, FND-03022, FND-03023

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03026"></a>
## FND-03026: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_TORCH_LARGE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CEE_INTERNAL_COMPONENT_TORCH_LARGE = 4;

### Evidence

- **SRC-0340** `research/proto/chesscom/explanation_engine/v1/cee_internal_component.proto` — [preserved redacted evidence](../evidence/text/470e21f9637b87367f386a2e6d2c25353ca0a58768fbe11166b756dc3576e7e9.proto)
  Character offset 329.

```text
 = 1;
  CEE_INTERNAL_COMPONENT_POSITION_DIFFICULTY = 2;
  CEE_INTERNAL_COMPONENT_TORCH_SMALL = 3;
  CEE_INTERNAL_COMPONENT_TORCH_LARGE = 4;
  CEE_INTERNAL_COMPONENT_KOMODO = 5;
  CEE_INTERNAL_COMPONENT_INTERNAL_FEATURES = 6;
}

```

**Source references:** SRC-0340, SRC-1311  
**URL references:** None independently associated  
**Related findings:** FND-03021, FND-03022, FND-03023

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03027"></a>
## FND-03027: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_KOMODO = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CEE_INTERNAL_COMPONENT_KOMODO = 5;

### Evidence

- **SRC-0340** `research/proto/chesscom/explanation_engine/v1/cee_internal_component.proto` — [preserved redacted evidence](../evidence/text/470e21f9637b87367f386a2e6d2c25353ca0a58768fbe11166b756dc3576e7e9.proto)
  Character offset 371.

```text
FFICULTY = 2;
  CEE_INTERNAL_COMPONENT_TORCH_SMALL = 3;
  CEE_INTERNAL_COMPONENT_TORCH_LARGE = 4;
  CEE_INTERNAL_COMPONENT_KOMODO = 5;
  CEE_INTERNAL_COMPONENT_INTERNAL_FEATURES = 6;
}

```

**Source references:** SRC-0340, SRC-1311  
**URL references:** None independently associated  
**Related findings:** FND-03021, FND-03022, FND-03023

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03028"></a>
## FND-03028: chesscom.explanation_engine.v1.CeeInternalComponent.CEE_INTERNAL_COMPONENT_INTERNAL_FEATURES = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CEE_INTERNAL_COMPONENT_INTERNAL_FEATURES = 6;

### Evidence

- **SRC-0340** `research/proto/chesscom/explanation_engine/v1/cee_internal_component.proto` — [preserved redacted evidence](../evidence/text/470e21f9637b87367f386a2e6d2c25353ca0a58768fbe11166b756dc3576e7e9.proto)
  Character offset 408.

```text
T_TORCH_SMALL = 3;
  CEE_INTERNAL_COMPONENT_TORCH_LARGE = 4;
  CEE_INTERNAL_COMPONENT_KOMODO = 5;
  CEE_INTERNAL_COMPONENT_INTERNAL_FEATURES = 6;
}

```

**Source references:** SRC-0340, SRC-1311  
**URL references:** None independently associated  
**Related findings:** FND-03021, FND-03022, FND-03023

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03029"></a>
## FND-03029: enum declaration: chesscom.explanation_engine.v1.CeeInternalEngine

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CeeInternalEngine {

### Evidence

- **SRC-0341** `research/proto/chesscom/explanation_engine/v1/cee_internal_engine.proto` — [preserved redacted evidence](../evidence/text/98ca10826cb4a27acf63a8735614c26c7ed53debcdfe59679396662012b5ec99.proto)
  Character offset 128.

```text
ion_engine/v1/cee_internal_engine.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum CeeInternalEngine {
  CEE_INTERNAL_ENGINE_UNSPECIFIED = 0;
  CEE_INTERNAL_ENGINE_KOMODO = 1;
  CEE_INTERNAL_ENGINE_TORCH = 2;
}

```

**Source references:** SRC-0341, SRC-1312  
**URL references:** None independently associated  
**Related findings:** FND-03030, FND-03031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03030"></a>
## FND-03030: chesscom.explanation_engine.v1.CeeInternalEngine.CEE_INTERNAL_ENGINE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CEE_INTERNAL_ENGINE_UNSPECIFIED = 0;

### Evidence

- **SRC-0341** `research/proto/chesscom/explanation_engine/v1/cee_internal_engine.proto` — [preserved redacted evidence](../evidence/text/98ca10826cb4a27acf63a8735614c26c7ed53debcdfe59679396662012b5ec99.proto)
  Character offset 155.

```text
engine.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum CeeInternalEngine {
  CEE_INTERNAL_ENGINE_UNSPECIFIED = 0;
  CEE_INTERNAL_ENGINE_KOMODO = 1;
  CEE_INTERNAL_ENGINE_TORCH = 2;
}

```

**Source references:** SRC-0341, SRC-1312  
**URL references:** None independently associated  
**Related findings:** FND-03029, FND-03031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03031"></a>
## FND-03031: chesscom.explanation_engine.v1.CeeInternalEngine.CEE_INTERNAL_ENGINE_KOMODO = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CEE_INTERNAL_ENGINE_KOMODO = 1;

### Evidence

- **SRC-0341** `research/proto/chesscom/explanation_engine/v1/cee_internal_engine.proto` — [preserved redacted evidence](../evidence/text/98ca10826cb4a27acf63a8735614c26c7ed53debcdfe59679396662012b5ec99.proto)
  Character offset 194.

```text
 chesscom.explanation_engine.v1;

enum CeeInternalEngine {
  CEE_INTERNAL_ENGINE_UNSPECIFIED = 0;
  CEE_INTERNAL_ENGINE_KOMODO = 1;
  CEE_INTERNAL_ENGINE_TORCH = 2;
}

```

**Source references:** SRC-0341, SRC-1312  
**URL references:** None independently associated  
**Related findings:** FND-03029, FND-03030

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03032"></a>
## FND-03032: chesscom.explanation_engine.v1.CeeInternalEngine.CEE_INTERNAL_ENGINE_TORCH = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CEE_INTERNAL_ENGINE_TORCH = 2;

### Evidence

- **SRC-0341** `research/proto/chesscom/explanation_engine/v1/cee_internal_engine.proto` — [preserved redacted evidence](../evidence/text/98ca10826cb4a27acf63a8735614c26c7ed53debcdfe59679396662012b5ec99.proto)
  Character offset 228.

```text
enum CeeInternalEngine {
  CEE_INTERNAL_ENGINE_UNSPECIFIED = 0;
  CEE_INTERNAL_ENGINE_KOMODO = 1;
  CEE_INTERNAL_ENGINE_TORCH = 2;
}

```

**Source references:** SRC-0341, SRC-1312  
**URL references:** None independently associated  
**Related findings:** FND-03029, FND-03030, FND-03031

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03033"></a>
## FND-03033: message declaration: chesscom.explanation_engine.v1.MovePrediction

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MovePrediction {

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 124.

```text
anation_engine/v1/charm_inference.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message MovePrediction {
  optional .chesscom.chess.v1.Move move = 1;
  optional string uci_move = 2;
  optional float probability = 3;
}

message CharmInferenceResult {
  oneof _engine {
  .chesscom.engine.v1.Engine engine = 11;
  }
  optional string model_key = 1;
  optional int32 elo = 2;
  repeated .chesscom.explan
```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03034, FND-03035

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03034"></a>
## FND-03034: chesscom.explanation_engine.v1.MovePrediction.move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move move = 1;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 151.

```text
erence.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message MovePrediction {
  optional .chesscom.chess.v1.Move move = 1;
  optional string uci_move = 2;
  optional float probability = 3;
}

message CharmInferenceResult {
  oneof _engine {
  .chesscom.engine.v1.Engine engine = 11;
  }
  optional string model_key = 1;
  optional int32 elo = 2;
  repeated .chesscom.explanation_engine.v1.MovePredict
```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03035

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03035"></a>
## FND-03035: chesscom.explanation_engine.v1.MovePrediction.uci_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string uci_move = 2;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 196.

```text
com.explanation_engine.v1;

message MovePrediction {
  optional .chesscom.chess.v1.Move move = 1;
  optional string uci_move = 2;
  optional float probability = 3;
}

message CharmInferenceResult {
  oneof _engine {
  .chesscom.engine.v1.Engine engine = 11;
  }
  optional string model_key = 1;
  optional int32 elo = 2;
  repeated .chesscom.explanation_engine.v1.MovePrediction moves = 3;
  optional float expected_poin
```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03036"></a>
## FND-03036: chesscom.explanation_engine.v1.MovePrediction.probability = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float probability = 3;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 228.

```text
age MovePrediction {
  optional .chesscom.chess.v1.Move move = 1;
  optional string uci_move = 2;
  optional float probability = 3;
}

message CharmInferenceResult {
  oneof _engine {
  .chesscom.engine.v1.Engine engine = 11;
  }
  optional string model_key = 1;
  optional int32 elo = 2;
  repeated .chesscom.explanation_engine.v1.MovePrediction moves = 3;
  optional float expected_points = 4;
  repeated float rank_pr
```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03037"></a>
## FND-03037: message declaration: chesscom.explanation_engine.v1.CharmInferenceResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CharmInferenceResult {

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 263.

```text
esscom.chess.v1.Move move = 1;
  optional string uci_move = 2;
  optional float probability = 3;
}

message CharmInferenceResult {
  oneof _engine {
  .chesscom.engine.v1.Engine engine = 11;
  }
  optional string model_key = 1;
  optional int32 elo = 2;
  repeated .chesscom.explanation_engine.v1.MovePrediction moves = 3;
  optional float expected_points = 4;
  repeated float rank_probabilities = 5;
  repeated float s
```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03038"></a>
## FND-03038: oneof declaration: chesscom.explanation_engine.v1.CharmInferenceResult._engine

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _engine {

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 296.

```text
optional string uci_move = 2;
  optional float probability = 3;
}

message CharmInferenceResult {
  oneof _engine {
  .chesscom.engine.v1.Engine engine = 11;
  }
  optional string model_key = 1;
  optional int32 elo = 2;
  repeated .chesscom.explanation_engine.v1.MovePrediction moves = 3;
  optional float expected_points = 4;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repe
```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03039"></a>
## FND-03039: chesscom.explanation_engine.v1.CharmInferenceResult.engine = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.engine.v1.Engine engine = 11;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 314.

```text
i_move = 2;
  optional float probability = 3;
}

message CharmInferenceResult {
  oneof _engine {
  .chesscom.engine.v1.Engine engine = 11;
  }
  optional string model_key = 1;
  optional int32 elo = 2;
  repeated .chesscom.explanation_engine.v1.MovePrediction moves = 3;
  optional float expected_points = 4;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_ta
```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03040"></a>
## FND-03040: chesscom.explanation_engine.v1.CharmInferenceResult.model_key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string model_key = 1;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 360.

```text
}

message CharmInferenceResult {
  oneof _engine {
  .chesscom.engine.v1.Engine engine = 11;
  }
  optional string model_key = 1;
  optional int32 elo = 2;
  repeated .chesscom.explanation_engine.v1.MovePrediction moves = 3;
  optional float expected_points = 4;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_pr
```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03041"></a>
## FND-03041: chesscom.explanation_engine.v1.CharmInferenceResult.elo = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 elo = 2;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 393.

```text

  oneof _engine {
  .chesscom.engine.v1.Engine engine = 11;
  }
  optional string model_key = 1;
  optional int32 elo = 2;
  repeated .chesscom.explanation_engine.v1.MovePrediction moves = 3;
  optional float expected_points = 4;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float
```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03042"></a>
## FND-03042: chesscom.explanation_engine.v1.CharmInferenceResult.moves = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.MovePrediction moves = 3;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 419.

```text
scom.engine.v1.Engine engine = 11;
  }
  optional string model_key = 1;
  optional int32 elo = 2;
  repeated .chesscom.explanation_engine.v1.MovePrediction moves = 3;
  optional float expected_points = 4;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive
```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03043"></a>
## FND-03043: chesscom.explanation_engine.v1.CharmInferenceResult.expected_points = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float expected_points = 4;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 488.

```text
1;
  optional int32 elo = 2;
  repeated .chesscom.explanation_engine.v1.MovePrediction moves = 3;
  optional float expected_points = 4;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
  repeated string engine_line_uci_moves = 10;
}

```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03044"></a>
## FND-03044: chesscom.explanation_engine.v1.CharmInferenceResult.rank_probabilities = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated float rank_probabilities = 5;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 526.

```text
d .chesscom.explanation_engine.v1.MovePrediction moves = 3;
  optional float expected_points = 4;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
  repeated string engine_line_uci_moves = 10;
}

```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03045"></a>
## FND-03045: chesscom.explanation_engine.v1.CharmInferenceResult.strength_probabilities = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated float strength_probabilities = 6;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 567.

```text
diction moves = 3;
  optional float expected_points = 4;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
  repeated string engine_line_uci_moves = 10;
}

```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03046"></a>
## FND-03046: chesscom.explanation_engine.v1.CharmInferenceResult.time_taken_probabilities = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated float time_taken_probabilities = 7;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 612.

```text
points = 4;
  repeated float rank_probabilities = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
  repeated string engine_line_uci_moves = 10;
}

```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03047"></a>
## FND-03047: chesscom.explanation_engine.v1.CharmInferenceResult.ldw_probabilities = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated float ldw_probabilities = 8;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 659.

```text
 = 5;
  repeated float strength_probabilities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
  repeated string engine_line_uci_moves = 10;
}

```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03048"></a>
## FND-03048: chesscom.explanation_engine.v1.CharmInferenceResult.strength_rating_sensitive_probabilities = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated float strength_rating_sensitive_probabilities = 9;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 699.

```text
ities = 6;
  repeated float time_taken_probabilities = 7;
  repeated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
  repeated string engine_line_uci_moves = 10;
}

```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03049"></a>
## FND-03049: chesscom.explanation_engine.v1.CharmInferenceResult.engine_line_uci_moves = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string engine_line_uci_moves = 10;

### Evidence

- **SRC-0342** `research/proto/chesscom/explanation_engine/v1/charm_inference.proto` — [preserved redacted evidence](../evidence/text/51eb507e9bc00c2ef264047b0fef409d55df1ee1dc528ca678db10848a5be94b.proto)
  Character offset 761.

```text
peated float ldw_probabilities = 8;
  repeated float strength_rating_sensitive_probabilities = 9;
  repeated string engine_line_uci_moves = 10;
}

```

**Source references:** SRC-0342, SRC-1313  
**URL references:** None independently associated  
**Related findings:** FND-03033, FND-03034, FND-03035

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03050"></a>
## FND-03050: message declaration: chesscom.explanation_engine.v1.CharmInferenceCode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CharmInferenceCode {

### Evidence

- **SRC-0343** `research/proto/chesscom/explanation_engine/v1/charm_inference_code.proto` — [preserved redacted evidence](../evidence/text/b2f5e0af26a2fcda370f95955d3efb19c5b2dcc80d34c03893e1f0a520dd300a.proto)
  Character offset 129.

```text
on_engine/v1/charm_inference_code.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message CharmInferenceCode {
  optional string model_key = 1;
  repeated int32 ratings = 2;
  repeated uint32 engine_line_move_indexes = 3;
  optional bytes coded_values = 4;
}

message NodeCharmInferenceCodes {
  repeated .chesscom.explanation_engine.v1.CharmInferenceCode inferences = 1;
}

message CharmInferenceCodes
```

**Source references:** SRC-0343, SRC-1314  
**URL references:** None independently associated  
**Related findings:** FND-03051, FND-03052

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03051"></a>
## FND-03051: chesscom.explanation_engine.v1.CharmInferenceCode.model_key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string model_key = 1;

### Evidence

- **SRC-0343** `research/proto/chesscom/explanation_engine/v1/charm_inference_code.proto` — [preserved redacted evidence](../evidence/text/b2f5e0af26a2fcda370f95955d3efb19c5b2dcc80d34c03893e1f0a520dd300a.proto)
  Character offset 160.

```text
de.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message CharmInferenceCode {
  optional string model_key = 1;
  repeated int32 ratings = 2;
  repeated uint32 engine_line_move_indexes = 3;
  optional bytes coded_values = 4;
}

message NodeCharmInferenceCodes {
  repeated .chesscom.explanation_engine.v1.CharmInferenceCode inferences = 1;
}

message CharmInferenceCodes {
  optional int32 codebook_ve
```

**Source references:** SRC-0343, SRC-1314  
**URL references:** None independently associated  
**Related findings:** FND-03050, FND-03052

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03052"></a>
## FND-03052: chesscom.explanation_engine.v1.CharmInferenceCode.ratings = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated int32 ratings = 2;

### Evidence

- **SRC-0343** `research/proto/chesscom/explanation_engine/v1/charm_inference_code.proto` — [preserved redacted evidence](../evidence/text/b2f5e0af26a2fcda370f95955d3efb19c5b2dcc80d34c03893e1f0a520dd300a.proto)
  Character offset 193.

```text
ge chesscom.explanation_engine.v1;

message CharmInferenceCode {
  optional string model_key = 1;
  repeated int32 ratings = 2;
  repeated uint32 engine_line_move_indexes = 3;
  optional bytes coded_values = 4;
}

message NodeCharmInferenceCodes {
  repeated .chesscom.explanation_engine.v1.CharmInferenceCode inferences = 1;
}

message CharmInferenceCodes {
  optional int32 codebook_version = 1;
  repeated .chesscom.e
```

**Source references:** SRC-0343, SRC-1314  
**URL references:** None independently associated  
**Related findings:** FND-03050, FND-03051

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03053"></a>
## FND-03053: chesscom.explanation_engine.v1.CharmInferenceCode.engine_line_move_indexes = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 engine_line_move_indexes = 3;

### Evidence

- **SRC-0343** `research/proto/chesscom/explanation_engine/v1/charm_inference_code.proto` — [preserved redacted evidence](../evidence/text/b2f5e0af26a2fcda370f95955d3efb19c5b2dcc80d34c03893e1f0a520dd300a.proto)
  Character offset 223.

```text
.v1;

message CharmInferenceCode {
  optional string model_key = 1;
  repeated int32 ratings = 2;
  repeated uint32 engine_line_move_indexes = 3;
  optional bytes coded_values = 4;
}

message NodeCharmInferenceCodes {
  repeated .chesscom.explanation_engine.v1.CharmInferenceCode inferences = 1;
}

message CharmInferenceCodes {
  optional int32 codebook_version = 1;
  repeated .chesscom.explanation_engine.v1.CharmInfe
```

**Source references:** SRC-0343, SRC-1314  
**URL references:** None independently associated  
**Related findings:** FND-03050, FND-03051, FND-03052

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03054"></a>
## FND-03054: chesscom.explanation_engine.v1.CharmInferenceCode.coded_values = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bytes coded_values = 4;

### Evidence

- **SRC-0343** `research/proto/chesscom/explanation_engine/v1/charm_inference_code.proto` — [preserved redacted evidence](../evidence/text/b2f5e0af26a2fcda370f95955d3efb19c5b2dcc80d34c03893e1f0a520dd300a.proto)
  Character offset 271.

```text
ring model_key = 1;
  repeated int32 ratings = 2;
  repeated uint32 engine_line_move_indexes = 3;
  optional bytes coded_values = 4;
}

message NodeCharmInferenceCodes {
  repeated .chesscom.explanation_engine.v1.CharmInferenceCode inferences = 1;
}

message CharmInferenceCodes {
  optional int32 codebook_version = 1;
  repeated .chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry nodes = 2;
  message Nodes
```

**Source references:** SRC-0343, SRC-1314  
**URL references:** None independently associated  
**Related findings:** FND-03050, FND-03051, FND-03052

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03055"></a>
## FND-03055: message declaration: chesscom.explanation_engine.v1.NodeCharmInferenceCodes

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NodeCharmInferenceCodes {

### Evidence

- **SRC-0343** `research/proto/chesscom/explanation_engine/v1/charm_inference_code.proto` — [preserved redacted evidence](../evidence/text/b2f5e0af26a2fcda370f95955d3efb19c5b2dcc80d34c03893e1f0a520dd300a.proto)
  Character offset 307.

```text
 ratings = 2;
  repeated uint32 engine_line_move_indexes = 3;
  optional bytes coded_values = 4;
}

message NodeCharmInferenceCodes {
  repeated .chesscom.explanation_engine.v1.CharmInferenceCode inferences = 1;
}

message CharmInferenceCodes {
  optional int32 codebook_version = 1;
  repeated .chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry nodes = 2;
  message NodesEntry {
  optional int32 key = 1;
  
```

**Source references:** SRC-0343, SRC-1314  
**URL references:** None independently associated  
**Related findings:** FND-03050, FND-03051, FND-03052

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03056"></a>
## FND-03056: chesscom.explanation_engine.v1.NodeCharmInferenceCodes.inferences = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.CharmInferenceCode inferences = 1;

### Evidence

- **SRC-0343** `research/proto/chesscom/explanation_engine/v1/charm_inference_code.proto` — [preserved redacted evidence](../evidence/text/b2f5e0af26a2fcda370f95955d3efb19c5b2dcc80d34c03893e1f0a520dd300a.proto)
  Character offset 343.

```text
ne_line_move_indexes = 3;
  optional bytes coded_values = 4;
}

message NodeCharmInferenceCodes {
  repeated .chesscom.explanation_engine.v1.CharmInferenceCode inferences = 1;
}

message CharmInferenceCodes {
  optional int32 codebook_version = 1;
  repeated .chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry nodes = 2;
  message NodesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engin
```

**Source references:** SRC-0343, SRC-1314  
**URL references:** None independently associated  
**Related findings:** FND-03050, FND-03051, FND-03052

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03057"></a>
## FND-03057: message declaration: chesscom.explanation_engine.v1.CharmInferenceCodes

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CharmInferenceCodes {

### Evidence

- **SRC-0343** `research/proto/chesscom/explanation_engine/v1/charm_inference_code.proto` — [preserved redacted evidence](../evidence/text/b2f5e0af26a2fcda370f95955d3efb19c5b2dcc80d34c03893e1f0a520dd300a.proto)
  Character offset 422.

```text
rmInferenceCodes {
  repeated .chesscom.explanation_engine.v1.CharmInferenceCode inferences = 1;
}

message CharmInferenceCodes {
  optional int32 codebook_version = 1;
  repeated .chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry nodes = 2;
  message NodesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.NodeCharmInferenceCodes value = 2;
  }
}

```

**Source references:** SRC-0343, SRC-1314  
**URL references:** None independently associated  
**Related findings:** FND-03050, FND-03051, FND-03052

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03058"></a>
## FND-03058: chesscom.explanation_engine.v1.CharmInferenceCodes.codebook_version = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 codebook_version = 1;

### Evidence

- **SRC-0343** `research/proto/chesscom/explanation_engine/v1/charm_inference_code.proto` — [preserved redacted evidence](../evidence/text/b2f5e0af26a2fcda370f95955d3efb19c5b2dcc80d34c03893e1f0a520dd300a.proto)
  Character offset 454.

```text
hesscom.explanation_engine.v1.CharmInferenceCode inferences = 1;
}

message CharmInferenceCodes {
  optional int32 codebook_version = 1;
  repeated .chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry nodes = 2;
  message NodesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.NodeCharmInferenceCodes value = 2;
  }
}

```

**Source references:** SRC-0343, SRC-1314  
**URL references:** None independently associated  
**Related findings:** FND-03050, FND-03051, FND-03052

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03059"></a>
## FND-03059: chesscom.explanation_engine.v1.CharmInferenceCodes.nodes = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry nodes = 2;

### Evidence

- **SRC-0343** `research/proto/chesscom/explanation_engine/v1/charm_inference_code.proto` — [preserved redacted evidence](../evidence/text/b2f5e0af26a2fcda370f95955d3efb19c5b2dcc80d34c03893e1f0a520dd300a.proto)
  Character offset 493.

```text
renceCode inferences = 1;
}

message CharmInferenceCodes {
  optional int32 codebook_version = 1;
  repeated .chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry nodes = 2;
  message NodesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.NodeCharmInferenceCodes value = 2;
  }
}

```

**Source references:** SRC-0343, SRC-1314  
**URL references:** None independently associated  
**Related findings:** FND-03050, FND-03051, FND-03052

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03060"></a>
## FND-03060: message declaration: chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NodesEntry {

### Evidence

- **SRC-0343** `research/proto/chesscom/explanation_engine/v1/charm_inference_code.proto` — [preserved redacted evidence](../evidence/text/b2f5e0af26a2fcda370f95955d3efb19c5b2dcc80d34c03893e1f0a520dd300a.proto)
  Character offset 578.

```text
version = 1;
  repeated .chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry nodes = 2;
  message NodesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.NodeCharmInferenceCodes value = 2;
  }
}

```

**Source references:** SRC-0343, SRC-1314  
**URL references:** None independently associated  
**Related findings:** FND-03050, FND-03051, FND-03052

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03061"></a>
## FND-03061: chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 key = 1;

### Evidence

- **SRC-0343** `research/proto/chesscom/explanation_engine/v1/charm_inference_code.proto` — [preserved redacted evidence](../evidence/text/b2f5e0af26a2fcda370f95955d3efb19c5b2dcc80d34c03893e1f0a520dd300a.proto)
  Character offset 601.

```text
 .chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry nodes = 2;
  message NodesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.NodeCharmInferenceCodes value = 2;
  }
}

```

**Source references:** SRC-0343, SRC-1314  
**URL references:** None independently associated  
**Related findings:** FND-03050, FND-03051, FND-03052

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03062"></a>
## FND-03062: chesscom.explanation_engine.v1.CharmInferenceCodes.NodesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.NodeCharmInferenceCodes value = 2;

### Evidence

- **SRC-0343** `research/proto/chesscom/explanation_engine/v1/charm_inference_code.proto` — [preserved redacted evidence](../evidence/text/b2f5e0af26a2fcda370f95955d3efb19c5b2dcc80d34c03893e1f0a520dd300a.proto)
  Character offset 627.

```text
ine.v1.CharmInferenceCodes.NodesEntry nodes = 2;
  message NodesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.NodeCharmInferenceCodes value = 2;
  }
}

```

**Source references:** SRC-0343, SRC-1314  
**URL references:** None independently associated  
**Related findings:** FND-03050, FND-03051, FND-03052

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03063"></a>
## FND-03063: enum declaration: chesscom.explanation_engine.v1.Circumstance

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Circumstance {

### Evidence

- **SRC-0344** `research/proto/chesscom/explanation_engine/v1/circumstance.proto` — [preserved redacted evidence](../evidence/text/30234f7a2613bc8a2c60cae71eaf07153e1f639c10890dbd8d40c247d36bce99.proto)
  Character offset 121.

```text
xplanation_engine/v1/circumstance.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum Circumstance {
  CIRCUMSTANCE_UNSPECIFIED = 0;
  CIRCUMSTANCE_BASE = 1;
  CIRCUMSTANCE_THREATENS = 2;
  CIRCUMSTANCE_PREVENTS = 3;
  CIRCUMSTANCE_PERMITS = 4;
  CIRCUMSTANCE_MISSES = 5;
  CIRCUMSTANCE_MISSES_SAME = 6;
  CIRCUMSTANCE_ENDGAME = 7;
  CIRCUMSTANCE_GAME_STATUS = 8;
  CIRCUMSTANCE_LEADS_TO = 9;
  CIRCUM
```

**Source references:** SRC-0344, SRC-1315  
**URL references:** None independently associated  
**Related findings:** FND-03064, FND-03065

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03064"></a>
## FND-03064: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CIRCUMSTANCE_UNSPECIFIED = 0;

### Evidence

- **SRC-0344** `research/proto/chesscom/explanation_engine/v1/circumstance.proto` — [preserved redacted evidence](../evidence/text/30234f7a2613bc8a2c60cae71eaf07153e1f639c10890dbd8d40c247d36bce99.proto)
  Character offset 143.

```text
ircumstance.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum Circumstance {
  CIRCUMSTANCE_UNSPECIFIED = 0;
  CIRCUMSTANCE_BASE = 1;
  CIRCUMSTANCE_THREATENS = 2;
  CIRCUMSTANCE_PREVENTS = 3;
  CIRCUMSTANCE_PERMITS = 4;
  CIRCUMSTANCE_MISSES = 5;
  CIRCUMSTANCE_MISSES_SAME = 6;
  CIRCUMSTANCE_ENDGAME = 7;
  CIRCUMSTANCE_GAME_STATUS = 8;
  CIRCUMSTANCE_LEADS_TO = 9;
  CIRCUMSTANCE_WINS_MATERIAL =
```

**Source references:** SRC-0344, SRC-1315  
**URL references:** None independently associated  
**Related findings:** FND-03063, FND-03065

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03065"></a>
## FND-03065: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_BASE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CIRCUMSTANCE_BASE = 1;

### Evidence

- **SRC-0344** `research/proto/chesscom/explanation_engine/v1/circumstance.proto` — [preserved redacted evidence](../evidence/text/30234f7a2613bc8a2c60cae71eaf07153e1f639c10890dbd8d40c247d36bce99.proto)
  Character offset 175.

```text
to3

package chesscom.explanation_engine.v1;

enum Circumstance {
  CIRCUMSTANCE_UNSPECIFIED = 0;
  CIRCUMSTANCE_BASE = 1;
  CIRCUMSTANCE_THREATENS = 2;
  CIRCUMSTANCE_PREVENTS = 3;
  CIRCUMSTANCE_PERMITS = 4;
  CIRCUMSTANCE_MISSES = 5;
  CIRCUMSTANCE_MISSES_SAME = 6;
  CIRCUMSTANCE_ENDGAME = 7;
  CIRCUMSTANCE_GAME_STATUS = 8;
  CIRCUMSTANCE_LEADS_TO = 9;
  CIRCUMSTANCE_WINS_MATERIAL = 10;
  CIRCUMSTANCE_GAME_OVER = 
```

**Source references:** SRC-0344, SRC-1315  
**URL references:** None independently associated  
**Related findings:** FND-03063, FND-03064

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03066"></a>
## FND-03066: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_THREATENS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CIRCUMSTANCE_THREATENS = 2;

### Evidence

- **SRC-0344** `research/proto/chesscom/explanation_engine/v1/circumstance.proto` — [preserved redacted evidence](../evidence/text/30234f7a2613bc8a2c60cae71eaf07153e1f639c10890dbd8d40c247d36bce99.proto)
  Character offset 200.

```text
lanation_engine.v1;

enum Circumstance {
  CIRCUMSTANCE_UNSPECIFIED = 0;
  CIRCUMSTANCE_BASE = 1;
  CIRCUMSTANCE_THREATENS = 2;
  CIRCUMSTANCE_PREVENTS = 3;
  CIRCUMSTANCE_PERMITS = 4;
  CIRCUMSTANCE_MISSES = 5;
  CIRCUMSTANCE_MISSES_SAME = 6;
  CIRCUMSTANCE_ENDGAME = 7;
  CIRCUMSTANCE_GAME_STATUS = 8;
  CIRCUMSTANCE_LEADS_TO = 9;
  CIRCUMSTANCE_WINS_MATERIAL = 10;
  CIRCUMSTANCE_GAME_OVER = 11;
  CIRCUMSTANCE_MATE =
```

**Source references:** SRC-0344, SRC-1315  
**URL references:** None independently associated  
**Related findings:** FND-03063, FND-03064, FND-03065

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03067"></a>
## FND-03067: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_PREVENTS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CIRCUMSTANCE_PREVENTS = 3;

### Evidence

- **SRC-0344** `research/proto/chesscom/explanation_engine/v1/circumstance.proto` — [preserved redacted evidence](../evidence/text/30234f7a2613bc8a2c60cae71eaf07153e1f639c10890dbd8d40c247d36bce99.proto)
  Character offset 230.

```text
umstance {
  CIRCUMSTANCE_UNSPECIFIED = 0;
  CIRCUMSTANCE_BASE = 1;
  CIRCUMSTANCE_THREATENS = 2;
  CIRCUMSTANCE_PREVENTS = 3;
  CIRCUMSTANCE_PERMITS = 4;
  CIRCUMSTANCE_MISSES = 5;
  CIRCUMSTANCE_MISSES_SAME = 6;
  CIRCUMSTANCE_ENDGAME = 7;
  CIRCUMSTANCE_GAME_STATUS = 8;
  CIRCUMSTANCE_LEADS_TO = 9;
  CIRCUMSTANCE_WINS_MATERIAL = 10;
  CIRCUMSTANCE_GAME_OVER = 11;
  CIRCUMSTANCE_MATE = 12;
  CIRCUMSTANCE_BRILLIANT 
```

**Source references:** SRC-0344, SRC-1315  
**URL references:** None independently associated  
**Related findings:** FND-03063, FND-03064, FND-03065

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03068"></a>
## FND-03068: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_PERMITS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CIRCUMSTANCE_PERMITS = 4;

### Evidence

- **SRC-0344** `research/proto/chesscom/explanation_engine/v1/circumstance.proto` — [preserved redacted evidence](../evidence/text/30234f7a2613bc8a2c60cae71eaf07153e1f639c10890dbd8d40c247d36bce99.proto)
  Character offset 259.

```text
PECIFIED = 0;
  CIRCUMSTANCE_BASE = 1;
  CIRCUMSTANCE_THREATENS = 2;
  CIRCUMSTANCE_PREVENTS = 3;
  CIRCUMSTANCE_PERMITS = 4;
  CIRCUMSTANCE_MISSES = 5;
  CIRCUMSTANCE_MISSES_SAME = 6;
  CIRCUMSTANCE_ENDGAME = 7;
  CIRCUMSTANCE_GAME_STATUS = 8;
  CIRCUMSTANCE_LEADS_TO = 9;
  CIRCUMSTANCE_WINS_MATERIAL = 10;
  CIRCUMSTANCE_GAME_OVER = 11;
  CIRCUMSTANCE_MATE = 12;
  CIRCUMSTANCE_BRILLIANT = 13;
  CIRCUMSTANCE_GREAT_FI
```

**Source references:** SRC-0344, SRC-1315  
**URL references:** None independently associated  
**Related findings:** FND-03063, FND-03064, FND-03065

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03069"></a>
## FND-03069: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_MISSES = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CIRCUMSTANCE_MISSES = 5;

### Evidence

- **SRC-0344** `research/proto/chesscom/explanation_engine/v1/circumstance.proto` — [preserved redacted evidence](../evidence/text/30234f7a2613bc8a2c60cae71eaf07153e1f639c10890dbd8d40c247d36bce99.proto)
  Character offset 287.

```text
_BASE = 1;
  CIRCUMSTANCE_THREATENS = 2;
  CIRCUMSTANCE_PREVENTS = 3;
  CIRCUMSTANCE_PERMITS = 4;
  CIRCUMSTANCE_MISSES = 5;
  CIRCUMSTANCE_MISSES_SAME = 6;
  CIRCUMSTANCE_ENDGAME = 7;
  CIRCUMSTANCE_GAME_STATUS = 8;
  CIRCUMSTANCE_LEADS_TO = 9;
  CIRCUMSTANCE_WINS_MATERIAL = 10;
  CIRCUMSTANCE_GAME_OVER = 11;
  CIRCUMSTANCE_MATE = 12;
  CIRCUMSTANCE_BRILLIANT = 13;
  CIRCUMSTANCE_GREAT_FIND = 14;
  CIRCUMSTANCE_LONG
```

**Source references:** SRC-0344, SRC-1315  
**URL references:** None independently associated  
**Related findings:** FND-03063, FND-03064, FND-03065

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03070"></a>
## FND-03070: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_MISSES_SAME = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CIRCUMSTANCE_MISSES_SAME = 6;

### Evidence

- **SRC-0344** `research/proto/chesscom/explanation_engine/v1/circumstance.proto` — [preserved redacted evidence](../evidence/text/30234f7a2613bc8a2c60cae71eaf07153e1f639c10890dbd8d40c247d36bce99.proto)
  Character offset 314.

```text
HREATENS = 2;
  CIRCUMSTANCE_PREVENTS = 3;
  CIRCUMSTANCE_PERMITS = 4;
  CIRCUMSTANCE_MISSES = 5;
  CIRCUMSTANCE_MISSES_SAME = 6;
  CIRCUMSTANCE_ENDGAME = 7;
  CIRCUMSTANCE_GAME_STATUS = 8;
  CIRCUMSTANCE_LEADS_TO = 9;
  CIRCUMSTANCE_WINS_MATERIAL = 10;
  CIRCUMSTANCE_GAME_OVER = 11;
  CIRCUMSTANCE_MATE = 12;
  CIRCUMSTANCE_BRILLIANT = 13;
  CIRCUMSTANCE_GREAT_FIND = 14;
  CIRCUMSTANCE_LONG_THINK = 15;
  CIRCUMSTANCE
```

**Source references:** SRC-0344, SRC-1315  
**URL references:** None independently associated  
**Related findings:** FND-03063, FND-03064, FND-03065

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03071"></a>
## FND-03071: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_ENDGAME = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CIRCUMSTANCE_ENDGAME = 7;

### Evidence

- **SRC-0344** `research/proto/chesscom/explanation_engine/v1/circumstance.proto` — [preserved redacted evidence](../evidence/text/30234f7a2613bc8a2c60cae71eaf07153e1f639c10890dbd8d40c247d36bce99.proto)
  Character offset 346.

```text
VENTS = 3;
  CIRCUMSTANCE_PERMITS = 4;
  CIRCUMSTANCE_MISSES = 5;
  CIRCUMSTANCE_MISSES_SAME = 6;
  CIRCUMSTANCE_ENDGAME = 7;
  CIRCUMSTANCE_GAME_STATUS = 8;
  CIRCUMSTANCE_LEADS_TO = 9;
  CIRCUMSTANCE_WINS_MATERIAL = 10;
  CIRCUMSTANCE_GAME_OVER = 11;
  CIRCUMSTANCE_MATE = 12;
  CIRCUMSTANCE_BRILLIANT = 13;
  CIRCUMSTANCE_GREAT_FIND = 14;
  CIRCUMSTANCE_LONG_THINK = 15;
  CIRCUMSTANCE_SHORT_THINK = 16;
  CIRCUMSTANC
```

**Source references:** SRC-0344, SRC-1315  
**URL references:** None independently associated  
**Related findings:** FND-03063, FND-03064, FND-03065

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03072"></a>
## FND-03072: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_GAME_STATUS = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CIRCUMSTANCE_GAME_STATUS = 8;

### Evidence

- **SRC-0344** `research/proto/chesscom/explanation_engine/v1/circumstance.proto` — [preserved redacted evidence](../evidence/text/30234f7a2613bc8a2c60cae71eaf07153e1f639c10890dbd8d40c247d36bce99.proto)
  Character offset 374.

```text
RMITS = 4;
  CIRCUMSTANCE_MISSES = 5;
  CIRCUMSTANCE_MISSES_SAME = 6;
  CIRCUMSTANCE_ENDGAME = 7;
  CIRCUMSTANCE_GAME_STATUS = 8;
  CIRCUMSTANCE_LEADS_TO = 9;
  CIRCUMSTANCE_WINS_MATERIAL = 10;
  CIRCUMSTANCE_GAME_OVER = 11;
  CIRCUMSTANCE_MATE = 12;
  CIRCUMSTANCE_BRILLIANT = 13;
  CIRCUMSTANCE_GREAT_FIND = 14;
  CIRCUMSTANCE_LONG_THINK = 15;
  CIRCUMSTANCE_SHORT_THINK = 16;
  CIRCUMSTANCE_TIME_TROUBLE = 17;
  CIRCU
```

**Source references:** SRC-0344, SRC-1315  
**URL references:** None independently associated  
**Related findings:** FND-03063, FND-03064, FND-03065

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03073"></a>
## FND-03073: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_LEADS_TO = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CIRCUMSTANCE_LEADS_TO = 9;

### Evidence

- **SRC-0344** `research/proto/chesscom/explanation_engine/v1/circumstance.proto` — [preserved redacted evidence](../evidence/text/30234f7a2613bc8a2c60cae71eaf07153e1f639c10890dbd8d40c247d36bce99.proto)
  Character offset 406.

```text
 = 5;
  CIRCUMSTANCE_MISSES_SAME = 6;
  CIRCUMSTANCE_ENDGAME = 7;
  CIRCUMSTANCE_GAME_STATUS = 8;
  CIRCUMSTANCE_LEADS_TO = 9;
  CIRCUMSTANCE_WINS_MATERIAL = 10;
  CIRCUMSTANCE_GAME_OVER = 11;
  CIRCUMSTANCE_MATE = 12;
  CIRCUMSTANCE_BRILLIANT = 13;
  CIRCUMSTANCE_GREAT_FIND = 14;
  CIRCUMSTANCE_LONG_THINK = 15;
  CIRCUMSTANCE_SHORT_THINK = 16;
  CIRCUMSTANCE_TIME_TROUBLE = 17;
  CIRCUMSTANCE_FORCES = 18;
}

```

**Source references:** SRC-0344, SRC-1315  
**URL references:** None independently associated  
**Related findings:** FND-03063, FND-03064, FND-03065

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03074"></a>
## FND-03074: chesscom.explanation_engine.v1.Circumstance.CIRCUMSTANCE_WINS_MATERIAL = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CIRCUMSTANCE_WINS_MATERIAL = 10;

### Evidence

- **SRC-0344** `research/proto/chesscom/explanation_engine/v1/circumstance.proto` — [preserved redacted evidence](../evidence/text/30234f7a2613bc8a2c60cae71eaf07153e1f639c10890dbd8d40c247d36bce99.proto)
  Character offset 435.

```text
AME = 6;
  CIRCUMSTANCE_ENDGAME = 7;
  CIRCUMSTANCE_GAME_STATUS = 8;
  CIRCUMSTANCE_LEADS_TO = 9;
  CIRCUMSTANCE_WINS_MATERIAL = 10;
  CIRCUMSTANCE_GAME_OVER = 11;
  CIRCUMSTANCE_MATE = 12;
  CIRCUMSTANCE_BRILLIANT = 13;
  CIRCUMSTANCE_GREAT_FIND = 14;
  CIRCUMSTANCE_LONG_THINK = 15;
  CIRCUMSTANCE_SHORT_THINK = 16;
  CIRCUMSTANCE_TIME_TROUBLE = 17;
  CIRCUMSTANCE_FORCES = 18;
}

```

**Source references:** SRC-0344, SRC-1315  
**URL references:** None independently associated  
**Related findings:** FND-03063, FND-03064, FND-03065

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
