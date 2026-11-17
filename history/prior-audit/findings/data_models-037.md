# data_models — findings 3601–3700

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-03875"></a>
## FND-03875: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_EXPLICITLY_UNSCORED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NODE_FLAG_EXPLICITLY_UNSCORED = 2;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 190.

```text
scom.explanation_engine.v1;

enum NodeFlag {
  NODE_FLAG_UNSPECIFIED = 0;
  NODE_FLAG_PLAYED = 1;
  NODE_FLAG_EXPLICITLY_UNSCORED = 2;
  NODE_FLAG_SCORE_IS_WEAK = 4;
  NODE_FLAG_MANUALLY_ADDED = 8;
  NODE_FLAG_HAS_SCORE = 16;
  NODE_FLAG_HAS_DEPTH = 32;
  NODE_FLAG_HAS_ADDITIONAL_CHILDREN = 64;
  NODE_FLAG_HAS_CLOCK = 128;
}

message GameState {
  optional .chesscom.api.v1.SemanticVersion game_state_version = 1;
  op
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03876"></a>
## FND-03876: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_SCORE_IS_WEAK = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NODE_FLAG_SCORE_IS_WEAK = 4;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 227.

```text
eFlag {
  NODE_FLAG_UNSPECIFIED = 0;
  NODE_FLAG_PLAYED = 1;
  NODE_FLAG_EXPLICITLY_UNSCORED = 2;
  NODE_FLAG_SCORE_IS_WEAK = 4;
  NODE_FLAG_MANUALLY_ADDED = 8;
  NODE_FLAG_HAS_SCORE = 16;
  NODE_FLAG_HAS_DEPTH = 32;
  NODE_FLAG_HAS_ADDITIONAL_CHILDREN = 64;
  NODE_FLAG_HAS_CLOCK = 128;
}

message GameState {
  optional .chesscom.api.v1.SemanticVersion game_state_version = 1;
  optional .chesscom.explanation_engine.v
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03877"></a>
## FND-03877: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_MANUALLY_ADDED = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NODE_FLAG_MANUALLY_ADDED = 8;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 258.

```text
 = 0;
  NODE_FLAG_PLAYED = 1;
  NODE_FLAG_EXPLICITLY_UNSCORED = 2;
  NODE_FLAG_SCORE_IS_WEAK = 4;
  NODE_FLAG_MANUALLY_ADDED = 8;
  NODE_FLAG_HAS_SCORE = 16;
  NODE_FLAG_HAS_DEPTH = 32;
  NODE_FLAG_HAS_ADDITIONAL_CHILDREN = 64;
  NODE_FLAG_HAS_CLOCK = 128;
}

message GameState {
  optional .chesscom.api.v1.SemanticVersion game_state_version = 1;
  optional .chesscom.explanation_engine.v1.GameTree game_tree = 2;
  opt
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03878"></a>
## FND-03878: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_HAS_SCORE = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NODE_FLAG_HAS_SCORE = 16;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 290.

```text
NODE_FLAG_EXPLICITLY_UNSCORED = 2;
  NODE_FLAG_SCORE_IS_WEAK = 4;
  NODE_FLAG_MANUALLY_ADDED = 8;
  NODE_FLAG_HAS_SCORE = 16;
  NODE_FLAG_HAS_DEPTH = 32;
  NODE_FLAG_HAS_ADDITIONAL_CHILDREN = 64;
  NODE_FLAG_HAS_CLOCK = 128;
}

message GameState {
  optional .chesscom.api.v1.SemanticVersion game_state_version = 1;
  optional .chesscom.explanation_engine.v1.GameTree game_tree = 2;
  optional .chesscom.explanation_engi
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03879"></a>
## FND-03879: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_HAS_DEPTH = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NODE_FLAG_HAS_DEPTH = 32;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 318.

```text
D = 2;
  NODE_FLAG_SCORE_IS_WEAK = 4;
  NODE_FLAG_MANUALLY_ADDED = 8;
  NODE_FLAG_HAS_SCORE = 16;
  NODE_FLAG_HAS_DEPTH = 32;
  NODE_FLAG_HAS_ADDITIONAL_CHILDREN = 64;
  NODE_FLAG_HAS_CLOCK = 128;
}

message GameState {
  optional .chesscom.api.v1.SemanticVersion game_state_version = 1;
  optional .chesscom.explanation_engine.v1.GameTree game_tree = 2;
  optional .chesscom.explanation_engine.v1.GameSettings game_sett
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03880"></a>
## FND-03880: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_HAS_ADDITIONAL_CHILDREN = 64

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NODE_FLAG_HAS_ADDITIONAL_CHILDREN = 64;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 346.

```text
WEAK = 4;
  NODE_FLAG_MANUALLY_ADDED = 8;
  NODE_FLAG_HAS_SCORE = 16;
  NODE_FLAG_HAS_DEPTH = 32;
  NODE_FLAG_HAS_ADDITIONAL_CHILDREN = 64;
  NODE_FLAG_HAS_CLOCK = 128;
}

message GameState {
  optional .chesscom.api.v1.SemanticVersion game_state_version = 1;
  optional .chesscom.explanation_engine.v1.GameTree game_tree = 2;
  optional .chesscom.explanation_engine.v1.GameSettings game_settings = 3;
  optional .chessc
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03881"></a>
## FND-03881: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_HAS_CLOCK = 128

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NODE_FLAG_HAS_CLOCK = 128;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 388.

```text
  NODE_FLAG_HAS_SCORE = 16;
  NODE_FLAG_HAS_DEPTH = 32;
  NODE_FLAG_HAS_ADDITIONAL_CHILDREN = 64;
  NODE_FLAG_HAS_CLOCK = 128;
}

message GameState {
  optional .chesscom.api.v1.SemanticVersion game_state_version = 1;
  optional .chesscom.explanation_engine.v1.GameTree game_tree = 2;
  optional .chesscom.explanation_engine.v1.GameSettings game_settings = 3;
  optional .chesscom.chess.v1.GameMetadata game_metadata = 4
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03882"></a>
## FND-03882: message declaration: chesscom.explanation_engine.v1.GameState

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameState {

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 418.

```text
NODE_FLAG_HAS_DEPTH = 32;
  NODE_FLAG_HAS_ADDITIONAL_CHILDREN = 64;
  NODE_FLAG_HAS_CLOCK = 128;
}

message GameState {
  optional .chesscom.api.v1.SemanticVersion game_state_version = 1;
  optional .chesscom.explanation_engine.v1.GameTree game_tree = 2;
  optional .chesscom.explanation_engine.v1.GameSettings game_settings = 3;
  optional .chesscom.chess.v1.GameMetadata game_metadata = 4;
  optional .chesscom.engine.
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03883"></a>
## FND-03883: chesscom.explanation_engine.v1.GameState.game_state_version = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.SemanticVersion game_state_version = 1;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 440.

```text
32;
  NODE_FLAG_HAS_ADDITIONAL_CHILDREN = 64;
  NODE_FLAG_HAS_CLOCK = 128;
}

message GameState {
  optional .chesscom.api.v1.SemanticVersion game_state_version = 1;
  optional .chesscom.explanation_engine.v1.GameTree game_tree = 2;
  optional .chesscom.explanation_engine.v1.GameSettings game_settings = 3;
  optional .chesscom.chess.v1.GameMetadata game_metadata = 4;
  optional .chesscom.engine.v1.Engine default_eval
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03884"></a>
## FND-03884: chesscom.explanation_engine.v1.GameState.game_tree = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GameTree game_tree = 2;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 508.

```text
= 128;
}

message GameState {
  optional .chesscom.api.v1.SemanticVersion game_state_version = 1;
  optional .chesscom.explanation_engine.v1.GameTree game_tree = 2;
  optional .chesscom.explanation_engine.v1.GameSettings game_settings = 3;
  optional .chesscom.chess.v1.GameMetadata game_metadata = 4;
  optional .chesscom.engine.v1.Engine default_eval_source_engine = 5;
  optional .chesscom.explanation_engine.v1.Coach
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03885"></a>
## FND-03885: chesscom.explanation_engine.v1.GameState.game_settings = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GameSettings game_settings = 3;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 575.

```text
ersion game_state_version = 1;
  optional .chesscom.explanation_engine.v1.GameTree game_tree = 2;
  optional .chesscom.explanation_engine.v1.GameSettings game_settings = 3;
  optional .chesscom.chess.v1.GameMetadata game_metadata = 4;
  optional .chesscom.engine.v1.Engine default_eval_source_engine = 5;
  optional .chesscom.explanation_engine.v1.CoachState coach_state = 6;
  repeated .chesscom.explanation_engine.v1.G
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03886"></a>
## FND-03886: chesscom.explanation_engine.v1.GameState.game_metadata = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.GameMetadata game_metadata = 4;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 650.

```text
ameTree game_tree = 2;
  optional .chesscom.explanation_engine.v1.GameSettings game_settings = 3;
  optional .chesscom.chess.v1.GameMetadata game_metadata = 4;
  optional .chesscom.engine.v1.Engine default_eval_source_engine = 5;
  optional .chesscom.explanation_engine.v1.CoachState coach_state = 6;
  repeated .chesscom.explanation_engine.v1.GameState.CharmInferencesEntry charm_inferences = 7;
  repeated .chesscom.ex
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03887"></a>
## FND-03887: chesscom.explanation_engine.v1.GameState.default_eval_source_engine = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.engine.v1.Engine default_eval_source_engine = 5;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 712.

```text
.v1.GameSettings game_settings = 3;
  optional .chesscom.chess.v1.GameMetadata game_metadata = 4;
  optional .chesscom.engine.v1.Engine default_eval_source_engine = 5;
  optional .chesscom.explanation_engine.v1.CoachState coach_state = 6;
  repeated .chesscom.explanation_engine.v1.GameState.CharmInferencesEntry charm_inferences = 7;
  repeated .chesscom.explanation_engine.v1.GameState.AnnotationsEntry annotations = 8
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03888"></a>
## FND-03888: chesscom.explanation_engine.v1.GameState.coach_state = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CoachState coach_state = 6;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 782.

```text
Metadata game_metadata = 4;
  optional .chesscom.engine.v1.Engine default_eval_source_engine = 5;
  optional .chesscom.explanation_engine.v1.CoachState coach_state = 6;
  repeated .chesscom.explanation_engine.v1.GameState.CharmInferencesEntry charm_inferences = 7;
  repeated .chesscom.explanation_engine.v1.GameState.AnnotationsEntry annotations = 8;
  repeated .chesscom.explanation_engine.v1.GameState.CompactCharmInf
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03889"></a>
## FND-03889: chesscom.explanation_engine.v1.GameState.charm_inferences = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GameState.CharmInferencesEntry charm_inferences = 7;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 853.

```text
lt_eval_source_engine = 5;
  optional .chesscom.explanation_engine.v1.CoachState coach_state = 6;
  repeated .chesscom.explanation_engine.v1.GameState.CharmInferencesEntry charm_inferences = 7;
  repeated .chesscom.explanation_engine.v1.GameState.AnnotationsEntry annotations = 8;
  repeated .chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry compact_charm_inferences = 9;
  optional .chesscom.explana
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03890"></a>
## FND-03890: chesscom.explanation_engine.v1.GameState.annotations = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GameState.AnnotationsEntry annotations = 8;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 949.

```text
;
  repeated .chesscom.explanation_engine.v1.GameState.CharmInferencesEntry charm_inferences = 7;
  repeated .chesscom.explanation_engine.v1.GameState.AnnotationsEntry annotations = 8;
  repeated .chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry compact_charm_inferences = 9;
  optional .chesscom.explanation_engine.v1.CompactGameTree compact_game_tree = 10;
  repeated .chesscom.explanation_engine.v
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03891"></a>
## FND-03891: chesscom.explanation_engine.v1.GameState.compact_charm_inferences = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry compact_charm_inferences = 9;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1036.

```text
ences = 7;
  repeated .chesscom.explanation_engine.v1.GameState.AnnotationsEntry annotations = 8;
  repeated .chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry compact_charm_inferences = 9;
  optional .chesscom.explanation_engine.v1.CompactGameTree compact_game_tree = 10;
  repeated .chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry quantized_charm_inferences = 11;
  optional .
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03892"></a>
## FND-03892: chesscom.explanation_engine.v1.GameState.compact_game_tree = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CompactGameTree compact_game_tree = 10;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1147.

```text
hesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry compact_charm_inferences = 9;
  optional .chesscom.explanation_engine.v1.CompactGameTree compact_game_tree = 10;
  repeated .chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry quantized_charm_inferences = 11;
  optional .chesscom.explanation_engine.v1.CharmInferenceCodes charm_inference_codes = 12;
  message CharmInferencesEntry {
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03893"></a>
## FND-03893: chesscom.explanation_engine.v1.GameState.quantized_charm_inferences = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry quantized_charm_inferences = 11;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1230.

```text
nferences = 9;
  optional .chesscom.explanation_engine.v1.CompactGameTree compact_game_tree = 10;
  repeated .chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry quantized_charm_inferences = 11;
  optional .chesscom.explanation_engine.v1.CharmInferenceCodes charm_inference_codes = 12;
  message CharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.SimpleCharmIn
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03894"></a>
## FND-03894: chesscom.explanation_engine.v1.GameState.charm_inference_codes = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CharmInferenceCodes charm_inference_codes = 12;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1346.

```text
om.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry quantized_charm_inferences = 11;
  optional .chesscom.explanation_engine.v1.CharmInferenceCodes charm_inference_codes = 12;
  message CharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.SimpleCharmInferences value = 2;
  }
  message AnnotationsEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engi
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03895"></a>
## FND-03895: message declaration: chesscom.explanation_engine.v1.GameState.CharmInferencesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CharmInferencesEntry {

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1437.

```text
 = 11;
  optional .chesscom.explanation_engine.v1.CharmInferenceCodes charm_inference_codes = 12;
  message CharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.SimpleCharmInferences value = 2;
  }
  message AnnotationsEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.MoveAnnotation value = 2;
  }
  message CompactCharmInferencesEntry {
  optional int3
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03896"></a>
## FND-03896: chesscom.explanation_engine.v1.GameState.CharmInferencesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 key = 1;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1470.

```text
nation_engine.v1.CharmInferenceCodes charm_inference_codes = 12;
  message CharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.SimpleCharmInferences value = 2;
  }
  message AnnotationsEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.MoveAnnotation value = 2;
  }
  message CompactCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.e
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03897"></a>
## FND-03897: chesscom.explanation_engine.v1.GameState.CharmInferencesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.SimpleCharmInferences value = 2;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1496.

```text
renceCodes charm_inference_codes = 12;
  message CharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.SimpleCharmInferences value = 2;
  }
  message AnnotationsEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.MoveAnnotation value = 2;
  }
  message CompactCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.Compa
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03898"></a>
## FND-03898: message declaration: chesscom.explanation_engine.v1.GameState.AnnotationsEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AnnotationsEntry {

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1576.

```text
al int32 key = 1;
  optional .chesscom.explanation_engine.v1.SimpleCharmInferences value = 2;
  }
  message AnnotationsEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.MoveAnnotation value = 2;
  }
  message CompactCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;
  }
  message QuantizedCharmInferencesEntry {
  opt
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03899"></a>
## FND-03899: chesscom.explanation_engine.v1.GameState.AnnotationsEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 key = 1;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1470.

```text
nation_engine.v1.CharmInferenceCodes charm_inference_codes = 12;
  message CharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.SimpleCharmInferences value = 2;
  }
  message AnnotationsEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.MoveAnnotation value = 2;
  }
  message CompactCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.e
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03900"></a>
## FND-03900: chesscom.explanation_engine.v1.GameState.AnnotationsEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveAnnotation value = 2;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1631.

```text
ne.v1.SimpleCharmInferences value = 2;
  }
  message AnnotationsEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.MoveAnnotation value = 2;
  }
  message CompactCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;
  }
  message QuantizedCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_e
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03901"></a>
## FND-03901: message declaration: chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CompactCharmInferencesEntry {

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1704.

```text
 optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.MoveAnnotation value = 2;
  }
  message CompactCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;
  }
  message QuantizedCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;
  }
}

message GameTree {
  re
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03902"></a>
## FND-03902: chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 key = 1;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1470.

```text
nation_engine.v1.CharmInferenceCodes charm_inference_codes = 12;
  message CharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.SimpleCharmInferences value = 2;
  }
  message AnnotationsEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.MoveAnnotation value = 2;
  }
  message CompactCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.e
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03903"></a>
## FND-03903: chesscom.explanation_engine.v1.GameState.CompactCharmInferencesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1770.

```text
1.MoveAnnotation value = 2;
  }
  message CompactCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;
  }
  message QuantizedCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;
  }
}

message GameTree {
  repeated .chesscom.explanation_engine.v1.GameTreeNode nodes = 1;
}


```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03904"></a>
## FND-03904: message declaration: chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message QuantizedCharmInferencesEntry {

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1851.

```text
l int32 key = 1;
  optional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;
  }
  message QuantizedCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;
  }
}

message GameTree {
  repeated .chesscom.explanation_engine.v1.GameTreeNode nodes = 1;
}

message GameTreeNode {
  oneof board_state {
  string initial_fen = 1;
  int32 le
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03905"></a>
## FND-03905: chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 key = 1;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1470.

```text
nation_engine.v1.CharmInferenceCodes charm_inference_codes = 12;
  message CharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.SimpleCharmInferences value = 2;
  }
  message AnnotationsEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.MoveAnnotation value = 2;
  }
  message CompactCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.e
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03906"></a>
## FND-03906: chesscom.explanation_engine.v1.GameState.QuantizedCharmInferencesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 1770.

```text
1.MoveAnnotation value = 2;
  }
  message CompactCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;
  }
  message QuantizedCharmInferencesEntry {
  optional int32 key = 1;
  optional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;
  }
}

message GameTree {
  repeated .chesscom.explanation_engine.v1.GameTreeNode nodes = 1;
}


```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03907"></a>
## FND-03907: message declaration: chesscom.explanation_engine.v1.GameTree

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameTree {

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2001.

```text
 int32 key = 1;
  optional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;
  }
}

message GameTree {
  repeated .chesscom.explanation_engine.v1.GameTreeNode nodes = 1;
}

message GameTreeNode {
  oneof board_state {
  string initial_fen = 1;
  int32 legal_move_index = 2;
  }
  oneof _score {
  sint32 score = 5;
  }
  oneof _depth {
  sint32 depth = 6;
  }
  oneof _time_on_clock_deciseconds {
  int32
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03908"></a>
## FND-03908: chesscom.explanation_engine.v1.GameTree.nodes = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GameTreeNode nodes = 1;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2022.

```text
ional .chesscom.explanation_engine.v1.CompactCharmInferences value = 2;
  }
}

message GameTree {
  repeated .chesscom.explanation_engine.v1.GameTreeNode nodes = 1;
}

message GameTreeNode {
  oneof board_state {
  string initial_fen = 1;
  int32 legal_move_index = 2;
  }
  oneof _score {
  sint32 score = 5;
  }
  oneof _depth {
  sint32 depth = 6;
  }
  oneof _time_on_clock_deciseconds {
  int32 time_on_clock_decise
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03909"></a>
## FND-03909: message declaration: chesscom.explanation_engine.v1.GameTreeNode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameTreeNode {

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2090.

```text
 2;
  }
}

message GameTree {
  repeated .chesscom.explanation_engine.v1.GameTreeNode nodes = 1;
}

message GameTreeNode {
  oneof board_state {
  string initial_fen = 1;
  int32 legal_move_index = 2;
  }
  oneof _score {
  sint32 score = 5;
  }
  oneof _depth {
  sint32 depth = 6;
  }
  oneof _time_on_clock_deciseconds {
  int32 time_on_clock_deciseconds = 8;
  }
  optional bool is_played = 3;
  optional bool is_exp
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03910"></a>
## FND-03910: oneof declaration: chesscom.explanation_engine.v1.GameTreeNode.board_state

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof board_state {

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2115.

```text
ee {
  repeated .chesscom.explanation_engine.v1.GameTreeNode nodes = 1;
}

message GameTreeNode {
  oneof board_state {
  string initial_fen = 1;
  int32 legal_move_index = 2;
  }
  oneof _score {
  sint32 score = 5;
  }
  oneof _depth {
  sint32 depth = 6;
  }
  oneof _time_on_clock_deciseconds {
  int32 time_on_clock_deciseconds = 8;
  }
  optional bool is_played = 3;
  optional bool is_explicitly_unscored = 4;
  o
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03911"></a>
## FND-03911: chesscom.explanation_engine.v1.GameTreeNode.initial_fen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string initial_fen = 1;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2137.

```text
com.explanation_engine.v1.GameTreeNode nodes = 1;
}

message GameTreeNode {
  oneof board_state {
  string initial_fen = 1;
  int32 legal_move_index = 2;
  }
  oneof _score {
  sint32 score = 5;
  }
  oneof _depth {
  sint32 depth = 6;
  }
  oneof _time_on_clock_deciseconds {
  int32 time_on_clock_deciseconds = 8;
  }
  optional bool is_played = 3;
  optional bool is_explicitly_unscored = 4;
  optional sint32 additio
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03912"></a>
## FND-03912: chesscom.explanation_engine.v1.GameTreeNode.legal_move_index = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 legal_move_index = 2;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2163.

```text
GameTreeNode nodes = 1;
}

message GameTreeNode {
  oneof board_state {
  string initial_fen = 1;
  int32 legal_move_index = 2;
  }
  oneof _score {
  sint32 score = 5;
  }
  oneof _depth {
  sint32 depth = 6;
  }
  oneof _time_on_clock_deciseconds {
  int32 time_on_clock_deciseconds = 8;
  }
  optional bool is_played = 3;
  optional bool is_explicitly_unscored = 4;
  optional sint32 additional_children = 7;
  option
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03913"></a>
## FND-03913: oneof declaration: chesscom.explanation_engine.v1.GameTreeNode._score

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _score {

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2197.

```text
 GameTreeNode {
  oneof board_state {
  string initial_fen = 1;
  int32 legal_move_index = 2;
  }
  oneof _score {
  sint32 score = 5;
  }
  oneof _depth {
  sint32 depth = 6;
  }
  oneof _time_on_clock_deciseconds {
  int32 time_on_clock_deciseconds = 8;
  }
  optional bool is_played = 3;
  optional bool is_explicitly_unscored = 4;
  optional sint32 additional_children = 7;
  optional bool score_is_weak = 9;
  optio
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03914"></a>
## FND-03914: chesscom.explanation_engine.v1.GameTreeNode.score = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

sint32 score = 5;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2214.

```text
 oneof board_state {
  string initial_fen = 1;
  int32 legal_move_index = 2;
  }
  oneof _score {
  sint32 score = 5;
  }
  oneof _depth {
  sint32 depth = 6;
  }
  oneof _time_on_clock_deciseconds {
  int32 time_on_clock_deciseconds = 8;
  }
  optional bool is_played = 3;
  optional bool is_explicitly_unscored = 4;
  optional sint32 additional_children = 7;
  optional bool score_is_weak = 9;
  optional bool manually
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03915"></a>
## FND-03915: oneof declaration: chesscom.explanation_engine.v1.GameTreeNode._depth

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _depth {

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2238.

```text
tring initial_fen = 1;
  int32 legal_move_index = 2;
  }
  oneof _score {
  sint32 score = 5;
  }
  oneof _depth {
  sint32 depth = 6;
  }
  oneof _time_on_clock_deciseconds {
  int32 time_on_clock_deciseconds = 8;
  }
  optional bool is_played = 3;
  optional bool is_explicitly_unscored = 4;
  optional sint32 additional_children = 7;
  optional bool score_is_weak = 9;
  optional bool manually_added = 10;
}

message 
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03916"></a>
## FND-03916: chesscom.explanation_engine.v1.GameTreeNode.depth = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

sint32 depth = 6;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2255.

```text
 = 1;
  int32 legal_move_index = 2;
  }
  oneof _score {
  sint32 score = 5;
  }
  oneof _depth {
  sint32 depth = 6;
  }
  oneof _time_on_clock_deciseconds {
  int32 time_on_clock_deciseconds = 8;
  }
  optional bool is_played = 3;
  optional bool is_explicitly_unscored = 4;
  optional sint32 additional_children = 7;
  optional bool score_is_weak = 9;
  optional bool manually_added = 10;
}

message CompactGameTree {
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03917"></a>
## FND-03917: oneof declaration: chesscom.explanation_engine.v1.GameTreeNode._time_on_clock_deciseconds

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_on_clock_deciseconds {

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2279.

```text
_index = 2;
  }
  oneof _score {
  sint32 score = 5;
  }
  oneof _depth {
  sint32 depth = 6;
  }
  oneof _time_on_clock_deciseconds {
  int32 time_on_clock_deciseconds = 8;
  }
  optional bool is_played = 3;
  optional bool is_explicitly_unscored = 4;
  optional sint32 additional_children = 7;
  optional bool score_is_weak = 9;
  optional bool manually_added = 10;
}

message CompactGameTree {
  optional string initi
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03918"></a>
## FND-03918: chesscom.explanation_engine.v1.GameTreeNode.time_on_clock_deciseconds = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 time_on_clock_deciseconds = 8;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2316.

```text
nt32 score = 5;
  }
  oneof _depth {
  sint32 depth = 6;
  }
  oneof _time_on_clock_deciseconds {
  int32 time_on_clock_deciseconds = 8;
  }
  optional bool is_played = 3;
  optional bool is_explicitly_unscored = 4;
  optional sint32 additional_children = 7;
  optional bool score_is_weak = 9;
  optional bool manually_added = 10;
}

message CompactGameTree {
  optional string initial_fen = 1;
  repeated uint32 legal_m
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03919"></a>
## FND-03919: chesscom.explanation_engine.v1.GameTreeNode.is_played = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_played = 3;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2359.

```text
32 depth = 6;
  }
  oneof _time_on_clock_deciseconds {
  int32 time_on_clock_deciseconds = 8;
  }
  optional bool is_played = 3;
  optional bool is_explicitly_unscored = 4;
  optional sint32 additional_children = 7;
  optional bool score_is_weak = 9;
  optional bool manually_added = 10;
}

message CompactGameTree {
  optional string initial_fen = 1;
  repeated uint32 legal_move_indexes = 2;
  optional bytes node_flag
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03920"></a>
## FND-03920: chesscom.explanation_engine.v1.GameTreeNode.is_explicitly_unscored = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_explicitly_unscored = 4;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2390.

```text
_on_clock_deciseconds {
  int32 time_on_clock_deciseconds = 8;
  }
  optional bool is_played = 3;
  optional bool is_explicitly_unscored = 4;
  optional sint32 additional_children = 7;
  optional bool score_is_weak = 9;
  optional bool manually_added = 10;
}

message CompactGameTree {
  optional string initial_fen = 1;
  repeated uint32 legal_move_indexes = 2;
  optional bytes node_flags = 3;
  repeated sint32 additi
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03921"></a>
## FND-03921: chesscom.explanation_engine.v1.GameTreeNode.additional_children = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional sint32 additional_children = 7;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2434.

```text
k_deciseconds = 8;
  }
  optional bool is_played = 3;
  optional bool is_explicitly_unscored = 4;
  optional sint32 additional_children = 7;
  optional bool score_is_weak = 9;
  optional bool manually_added = 10;
}

message CompactGameTree {
  optional string initial_fen = 1;
  repeated uint32 legal_move_indexes = 2;
  optional bytes node_flags = 3;
  repeated sint32 additional_children = 4;
  repeated sint32 scores 
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03922"></a>
## FND-03922: chesscom.explanation_engine.v1.GameTreeNode.score_is_weak = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool score_is_weak = 9;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2477.

```text
layed = 3;
  optional bool is_explicitly_unscored = 4;
  optional sint32 additional_children = 7;
  optional bool score_is_weak = 9;
  optional bool manually_added = 10;
}

message CompactGameTree {
  optional string initial_fen = 1;
  repeated uint32 legal_move_indexes = 2;
  optional bytes node_flags = 3;
  repeated sint32 additional_children = 4;
  repeated sint32 scores = 5;
  repeated sint32 depths = 6;
  repeat
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03923"></a>
## FND-03923: chesscom.explanation_engine.v1.GameTreeNode.manually_added = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool manually_added = 10;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2512.

```text
citly_unscored = 4;
  optional sint32 additional_children = 7;
  optional bool score_is_weak = 9;
  optional bool manually_added = 10;
}

message CompactGameTree {
  optional string initial_fen = 1;
  repeated uint32 legal_move_indexes = 2;
  optional bytes node_flags = 3;
  repeated sint32 additional_children = 4;
  repeated sint32 scores = 5;
  repeated sint32 depths = 6;
  repeated uint32 clocks_deciseconds = 7;
}
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03924"></a>
## FND-03924: message declaration: chesscom.explanation_engine.v1.CompactGameTree

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CompactGameTree {

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2550.

```text
additional_children = 7;
  optional bool score_is_weak = 9;
  optional bool manually_added = 10;
}

message CompactGameTree {
  optional string initial_fen = 1;
  repeated uint32 legal_move_indexes = 2;
  optional bytes node_flags = 3;
  repeated sint32 additional_children = 4;
  repeated sint32 scores = 5;
  repeated sint32 depths = 6;
  repeated uint32 clocks_deciseconds = 7;
}

```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03925"></a>
## FND-03925: chesscom.explanation_engine.v1.CompactGameTree.initial_fen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string initial_fen = 1;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2578.

```text
ptional bool score_is_weak = 9;
  optional bool manually_added = 10;
}

message CompactGameTree {
  optional string initial_fen = 1;
  repeated uint32 legal_move_indexes = 2;
  optional bytes node_flags = 3;
  repeated sint32 additional_children = 4;
  repeated sint32 scores = 5;
  repeated sint32 depths = 6;
  repeated uint32 clocks_deciseconds = 7;
}

```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03926"></a>
## FND-03926: chesscom.explanation_engine.v1.CompactGameTree.legal_move_indexes = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 legal_move_indexes = 2;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2613.

```text
ptional bool manually_added = 10;
}

message CompactGameTree {
  optional string initial_fen = 1;
  repeated uint32 legal_move_indexes = 2;
  optional bytes node_flags = 3;
  repeated sint32 additional_children = 4;
  repeated sint32 scores = 5;
  repeated sint32 depths = 6;
  repeated uint32 clocks_deciseconds = 7;
}

```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03927"></a>
## FND-03927: chesscom.explanation_engine.v1.CompactGameTree.node_flags = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bytes node_flags = 3;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2655.

```text
ge CompactGameTree {
  optional string initial_fen = 1;
  repeated uint32 legal_move_indexes = 2;
  optional bytes node_flags = 3;
  repeated sint32 additional_children = 4;
  repeated sint32 scores = 5;
  repeated sint32 depths = 6;
  repeated uint32 clocks_deciseconds = 7;
}

```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03928"></a>
## FND-03928: chesscom.explanation_engine.v1.CompactGameTree.additional_children = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated sint32 additional_children = 4;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2688.

```text
tring initial_fen = 1;
  repeated uint32 legal_move_indexes = 2;
  optional bytes node_flags = 3;
  repeated sint32 additional_children = 4;
  repeated sint32 scores = 5;
  repeated sint32 depths = 6;
  repeated uint32 clocks_deciseconds = 7;
}

```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03929"></a>
## FND-03929: chesscom.explanation_engine.v1.CompactGameTree.scores = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated sint32 scores = 5;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2731.

```text
gal_move_indexes = 2;
  optional bytes node_flags = 3;
  repeated sint32 additional_children = 4;
  repeated sint32 scores = 5;
  repeated sint32 depths = 6;
  repeated uint32 clocks_deciseconds = 7;
}

```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03930"></a>
## FND-03930: chesscom.explanation_engine.v1.CompactGameTree.depths = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated sint32 depths = 6;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2761.

```text
al bytes node_flags = 3;
  repeated sint32 additional_children = 4;
  repeated sint32 scores = 5;
  repeated sint32 depths = 6;
  repeated uint32 clocks_deciseconds = 7;
}

```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03931"></a>
## FND-03931: chesscom.explanation_engine.v1.CompactGameTree.clocks_deciseconds = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 clocks_deciseconds = 7;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 2791.

```text
eated sint32 additional_children = 4;
  repeated sint32 scores = 5;
  repeated sint32 depths = 6;
  repeated uint32 clocks_deciseconds = 7;
}

```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873, FND-03874

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03932"></a>
## FND-03932: message declaration: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InternalFeatureMaiaBotMoveRequest {

### Evidence

- **SRC-0408** `research/proto/chesscom/explanation_engine/v1/internal_feature_maia_botmove.proto` — [preserved redacted evidence](../evidence/text/ebf7ef3b338768978909e35e952aec7307e5bc25a194335bc85bd2e247b5ca99.proto)
  Character offset 138.

```text
/v1/internal_feature_maia_botmove.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message InternalFeatureMaiaBotMoveRequest {
  optional int32 elo_self = 1;
  optional int32 elo_oppo = 2;
  optional string json = 3;
}

message InternalFeatureMaiaBotMoveResponse {
  optional .chesscom.chess.v1.Move move = 1;
  optional string json = 2;
}

```

**Source references:** SRC-0408, SRC-1379  
**URL references:** None independently associated  
**Related findings:** FND-03933, FND-03934

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03933"></a>
## FND-03933: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveRequest.elo_self = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 elo_self = 1;

### Evidence

- **SRC-0408** `research/proto/chesscom/explanation_engine/v1/internal_feature_maia_botmove.proto` — [preserved redacted evidence](../evidence/text/ebf7ef3b338768978909e35e952aec7307e5bc25a194335bc85bd2e247b5ca99.proto)
  Character offset 184.

```text
tax: proto3

package chesscom.explanation_engine.v1;

message InternalFeatureMaiaBotMoveRequest {
  optional int32 elo_self = 1;
  optional int32 elo_oppo = 2;
  optional string json = 3;
}

message InternalFeatureMaiaBotMoveResponse {
  optional .chesscom.chess.v1.Move move = 1;
  optional string json = 2;
}

```

**Source references:** SRC-0408, SRC-1379  
**URL references:** None independently associated  
**Related findings:** FND-03932, FND-03934

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03934"></a>
## FND-03934: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveRequest.elo_oppo = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 elo_oppo = 2;

### Evidence

- **SRC-0408** `research/proto/chesscom/explanation_engine/v1/internal_feature_maia_botmove.proto` — [preserved redacted evidence](../evidence/text/ebf7ef3b338768978909e35e952aec7307e5bc25a194335bc85bd2e247b5ca99.proto)
  Character offset 215.

```text
xplanation_engine.v1;

message InternalFeatureMaiaBotMoveRequest {
  optional int32 elo_self = 1;
  optional int32 elo_oppo = 2;
  optional string json = 3;
}

message InternalFeatureMaiaBotMoveResponse {
  optional .chesscom.chess.v1.Move move = 1;
  optional string json = 2;
}

```

**Source references:** SRC-0408, SRC-1379  
**URL references:** None independently associated  
**Related findings:** FND-03932, FND-03933

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03935"></a>
## FND-03935: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveRequest.json = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string json = 3;

### Evidence

- **SRC-0408** `research/proto/chesscom/explanation_engine/v1/internal_feature_maia_botmove.proto` — [preserved redacted evidence](../evidence/text/ebf7ef3b338768978909e35e952aec7307e5bc25a194335bc85bd2e247b5ca99.proto)
  Character offset 246.

```text
InternalFeatureMaiaBotMoveRequest {
  optional int32 elo_self = 1;
  optional int32 elo_oppo = 2;
  optional string json = 3;
}

message InternalFeatureMaiaBotMoveResponse {
  optional .chesscom.chess.v1.Move move = 1;
  optional string json = 2;
}

```

**Source references:** SRC-0408, SRC-1379  
**URL references:** None independently associated  
**Related findings:** FND-03932, FND-03933, FND-03934

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03936"></a>
## FND-03936: message declaration: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InternalFeatureMaiaBotMoveResponse {

### Evidence

- **SRC-0408** `research/proto/chesscom/explanation_engine/v1/internal_feature_maia_botmove.proto` — [preserved redacted evidence](../evidence/text/ebf7ef3b338768978909e35e952aec7307e5bc25a194335bc85bd2e247b5ca99.proto)
  Character offset 275.

```text
uest {
  optional int32 elo_self = 1;
  optional int32 elo_oppo = 2;
  optional string json = 3;
}

message InternalFeatureMaiaBotMoveResponse {
  optional .chesscom.chess.v1.Move move = 1;
  optional string json = 2;
}

```

**Source references:** SRC-0408, SRC-1379  
**URL references:** None independently associated  
**Related findings:** FND-03932, FND-03933, FND-03934

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03937"></a>
## FND-03937: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveResponse.move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move move = 1;

### Evidence

- **SRC-0408** `research/proto/chesscom/explanation_engine/v1/internal_feature_maia_botmove.proto` — [preserved redacted evidence](../evidence/text/ebf7ef3b338768978909e35e952aec7307e5bc25a194335bc85bd2e247b5ca99.proto)
  Character offset 322.

```text
l int32 elo_oppo = 2;
  optional string json = 3;
}

message InternalFeatureMaiaBotMoveResponse {
  optional .chesscom.chess.v1.Move move = 1;
  optional string json = 2;
}

```

**Source references:** SRC-0408, SRC-1379  
**URL references:** None independently associated  
**Related findings:** FND-03932, FND-03933, FND-03934

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03938"></a>
## FND-03938: chesscom.explanation_engine.v1.InternalFeatureMaiaBotMoveResponse.json = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string json = 2;

### Evidence

- **SRC-0408** `research/proto/chesscom/explanation_engine/v1/internal_feature_maia_botmove.proto` — [preserved redacted evidence](../evidence/text/ebf7ef3b338768978909e35e952aec7307e5bc25a194335bc85bd2e247b5ca99.proto)
  Character offset 367.

```text
= 3;
}

message InternalFeatureMaiaBotMoveResponse {
  optional .chesscom.chess.v1.Move move = 1;
  optional string json = 2;
}

```

**Source references:** SRC-0408, SRC-1379  
**URL references:** None independently associated  
**Related findings:** FND-03932, FND-03933, FND-03934

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03939"></a>
## FND-03939: enum declaration: chesscom.explanation_engine.v1.PuzzleGenPhase

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PuzzleGenPhase {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 136.

```text
ne/v1/internal_feature_puzzle_gen.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum PuzzleGenPhase {
  PUZZLE_GEN_PHASE_UNSPECIFIED = 0;
  PUZZLE_GEN_PHASE_INIT = 1;
  PUZZLE_GEN_PHASE_BUILDING_PUZZLE_TREE = 2;
  PUZZLE_GEN_PHASE_ADDED_PUZZLE_TREE_NODE = 3;
  PUZZLE_GEN_PHASE_SELECTING_PUZZLE_LINE = 4;
  PUZZLE_GEN_PHASE_VERIFYING_SELECTED_LINE_EVALS = 5;
  PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFI
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03940"></a>
## FND-03940: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_PHASE_UNSPECIFIED = 0;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 160.

```text
uzzle_gen.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum PuzzleGenPhase {
  PUZZLE_GEN_PHASE_UNSPECIFIED = 0;
  PUZZLE_GEN_PHASE_INIT = 1;
  PUZZLE_GEN_PHASE_BUILDING_PUZZLE_TREE = 2;
  PUZZLE_GEN_PHASE_ADDED_PUZZLE_TREE_NODE = 3;
  PUZZLE_GEN_PHASE_SELECTING_PUZZLE_LINE = 4;
  PUZZLE_GEN_PHASE_VERIFYING_SELECTED_LINE_EVALS = 5;
  PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS = 6;

```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03941"></a>
## FND-03941: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_INIT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_PHASE_INIT = 1;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 196.

```text
ackage chesscom.explanation_engine.v1;

enum PuzzleGenPhase {
  PUZZLE_GEN_PHASE_UNSPECIFIED = 0;
  PUZZLE_GEN_PHASE_INIT = 1;
  PUZZLE_GEN_PHASE_BUILDING_PUZZLE_TREE = 2;
  PUZZLE_GEN_PHASE_ADDED_PUZZLE_TREE_NODE = 3;
  PUZZLE_GEN_PHASE_SELECTING_PUZZLE_LINE = 4;
  PUZZLE_GEN_PHASE_VERIFYING_SELECTED_LINE_EVALS = 5;
  PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS = 6;
  PUZZLE_GEN_PHASE_COMPUTING_GOALS =
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03942"></a>
## FND-03942: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_BUILDING_PUZZLE_TREE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_PHASE_BUILDING_PUZZLE_TREE = 2;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 225.

```text
ngine.v1;

enum PuzzleGenPhase {
  PUZZLE_GEN_PHASE_UNSPECIFIED = 0;
  PUZZLE_GEN_PHASE_INIT = 1;
  PUZZLE_GEN_PHASE_BUILDING_PUZZLE_TREE = 2;
  PUZZLE_GEN_PHASE_ADDED_PUZZLE_TREE_NODE = 3;
  PUZZLE_GEN_PHASE_SELECTING_PUZZLE_LINE = 4;
  PUZZLE_GEN_PHASE_VERIFYING_SELECTED_LINE_EVALS = 5;
  PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS = 6;
  PUZZLE_GEN_PHASE_COMPUTING_GOALS = 7;
  PUZZLE_GEN_PHASE_COMPUT
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03943"></a>
## FND-03943: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_ADDED_PUZZLE_TREE_NODE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_PHASE_ADDED_PUZZLE_TREE_NODE = 3;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 270.

```text
_PHASE_UNSPECIFIED = 0;
  PUZZLE_GEN_PHASE_INIT = 1;
  PUZZLE_GEN_PHASE_BUILDING_PUZZLE_TREE = 2;
  PUZZLE_GEN_PHASE_ADDED_PUZZLE_TREE_NODE = 3;
  PUZZLE_GEN_PHASE_SELECTING_PUZZLE_LINE = 4;
  PUZZLE_GEN_PHASE_VERIFYING_SELECTED_LINE_EVALS = 5;
  PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS = 6;
  PUZZLE_GEN_PHASE_COMPUTING_GOALS = 7;
  PUZZLE_GEN_PHASE_COMPUTING_THEMES = 8;
  PUZZLE_GEN_PHASE_DONE = 9;

```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03944"></a>
## FND-03944: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_SELECTING_PUZZLE_LINE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_PHASE_SELECTING_PUZZLE_LINE = 4;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 317.

```text
 = 1;
  PUZZLE_GEN_PHASE_BUILDING_PUZZLE_TREE = 2;
  PUZZLE_GEN_PHASE_ADDED_PUZZLE_TREE_NODE = 3;
  PUZZLE_GEN_PHASE_SELECTING_PUZZLE_LINE = 4;
  PUZZLE_GEN_PHASE_VERIFYING_SELECTED_LINE_EVALS = 5;
  PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS = 6;
  PUZZLE_GEN_PHASE_COMPUTING_GOALS = 7;
  PUZZLE_GEN_PHASE_COMPUTING_THEMES = 8;
  PUZZLE_GEN_PHASE_DONE = 9;
}

enum PuzzleGenFailureType {
  PUZZLE_GEN_FAI
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03945"></a>
## FND-03945: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_VERIFYING_SELECTED_LINE_EVALS = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_PHASE_VERIFYING_SELECTED_LINE_EVALS = 5;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 363.

```text
= 2;
  PUZZLE_GEN_PHASE_ADDED_PUZZLE_TREE_NODE = 3;
  PUZZLE_GEN_PHASE_SELECTING_PUZZLE_LINE = 4;
  PUZZLE_GEN_PHASE_VERIFYING_SELECTED_LINE_EVALS = 5;
  PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS = 6;
  PUZZLE_GEN_PHASE_COMPUTING_GOALS = 7;
  PUZZLE_GEN_PHASE_COMPUTING_THEMES = 8;
  PUZZLE_GEN_PHASE_DONE = 9;
}

enum PuzzleGenFailureType {
  PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED = 0;
  PUZZLE_GEN_FAILUR
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03946"></a>
## FND-03946: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS = 6;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 417.

```text
PUZZLE_GEN_PHASE_SELECTING_PUZZLE_LINE = 4;
  PUZZLE_GEN_PHASE_VERIFYING_SELECTED_LINE_EVALS = 5;
  PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS = 6;
  PUZZLE_GEN_PHASE_COMPUTING_GOALS = 7;
  PUZZLE_GEN_PHASE_COMPUTING_THEMES = 8;
  PUZZLE_GEN_PHASE_DONE = 9;
}

enum PuzzleGenFailureType {
  PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED = 0;
  PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE = 1;
  PUZZLE_GEN_FAILURE_TYPE_PUZ
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03947"></a>
## FND-03947: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_COMPUTING_GOALS = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_PHASE_COMPUTING_GOALS = 7;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 482.

```text
RIFYING_SELECTED_LINE_EVALS = 5;
  PUZZLE_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS = 6;
  PUZZLE_GEN_PHASE_COMPUTING_GOALS = 7;
  PUZZLE_GEN_PHASE_COMPUTING_THEMES = 8;
  PUZZLE_GEN_PHASE_DONE = 9;
}

enum PuzzleGenFailureType {
  PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED = 0;
  PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE = 1;
  PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT = 2;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03948"></a>
## FND-03948: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_COMPUTING_THEMES = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_PHASE_COMPUTING_THEMES = 8;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 522.

```text
E_GEN_PHASE_PUZZLE_POSITION_VERIFICATION_IN_PROGRESS = 6;
  PUZZLE_GEN_PHASE_COMPUTING_GOALS = 7;
  PUZZLE_GEN_PHASE_COMPUTING_THEMES = 8;
  PUZZLE_GEN_PHASE_DONE = 9;
}

enum PuzzleGenFailureType {
  PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED = 0;
  PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE = 1;
  PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT = 2;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME = 3;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PI
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03949"></a>
## FND-03949: chesscom.explanation_engine.v1.PuzzleGenPhase.PUZZLE_GEN_PHASE_DONE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_PHASE_DONE = 9;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 563.

```text
IN_PROGRESS = 6;
  PUZZLE_GEN_PHASE_COMPUTING_GOALS = 7;
  PUZZLE_GEN_PHASE_COMPUTING_THEMES = 8;
  PUZZLE_GEN_PHASE_DONE = 9;
}

enum PuzzleGenFailureType {
  PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED = 0;
  PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE = 1;
  PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT = 2;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME = 3;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING = 4;
  PUZZLE_GEN_FAILURE_
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03950"></a>
## FND-03950: enum declaration: chesscom.explanation_engine.v1.PuzzleGenFailureType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PuzzleGenFailureType {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 593.

```text
PHASE_COMPUTING_GOALS = 7;
  PUZZLE_GEN_PHASE_COMPUTING_THEMES = 8;
  PUZZLE_GEN_PHASE_DONE = 9;
}

enum PuzzleGenFailureType {
  PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED = 0;
  PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE = 1;
  PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT = 2;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME = 3;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING = 4;
  PUZZLE_GEN_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING 
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03951"></a>
## FND-03951: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 623.

```text
UZZLE_GEN_PHASE_COMPUTING_THEMES = 8;
  PUZZLE_GEN_PHASE_DONE = 9;
}

enum PuzzleGenFailureType {
  PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED = 0;
  PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE = 1;
  PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT = 2;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME = 3;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING = 4;
  PUZZLE_GEN_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING = 5;
  PUZZLE_GEN_FAILURE_TYPE
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03952"></a>
## FND-03952: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE = 1;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 666.

```text
ZLE_GEN_PHASE_DONE = 9;
}

enum PuzzleGenFailureType {
  PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED = 0;
  PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE = 1;
  PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT = 2;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME = 3;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING = 4;
  PUZZLE_GEN_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING = 5;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_TOO_STRONG = 6;
  PUZZLE_GEN_FA
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03953"></a>
## FND-03953: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT = 2;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 710.

```text
lureType {
  PUZZLE_GEN_FAILURE_TYPE_UNSPECIFIED = 0;
  PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE = 1;
  PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT = 2;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME = 3;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING = 4;
  PUZZLE_GEN_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING = 5;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_TOO_STRONG = 6;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_BEST_MOVE_TOO_LOSING
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03954"></a>
## FND-03954: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME = 3;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 758.

```text
 = 0;
  PUZZLE_GEN_FAILURE_TYPE_ILLEGAL_MOVE = 1;
  PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT = 2;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME = 3;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING = 4;
  PUZZLE_GEN_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING = 5;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_TOO_STRONG = 6;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_BEST_MOVE_TOO_LOSING = 7;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03955"></a>
## FND-03955: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING = 4;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 810.

```text
PUZZLE_GEN_FAILURE_TYPE_PUZZLE_TOO_SHORT = 2;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME = 3;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING = 4;
  PUZZLE_GEN_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING = 5;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_TOO_STRONG = 6;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_BEST_MOVE_TOO_LOSING = 7;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_ABSOLUTE = 8;
  PUZZLE_GEN_FAILURE
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03956"></a>
## FND-03956: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING = 5;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 864.

```text
_GEN_FAILURE_TYPE_PITCH_MOVE_ENDS_GAME = 3;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING = 4;
  PUZZLE_GEN_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING = 5;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_TOO_STRONG = 6;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_BEST_MOVE_TOO_LOSING = 7;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_ABSOLUTE = 8;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_RELATIVE = 9;

```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03957"></a>
## FND-03957: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_TOO_STRONG = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_TOO_STRONG = 6;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 920.

```text
_FAILURE_TYPE_AFTER_PITCH_TOO_LOSING = 4;
  PUZZLE_GEN_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING = 5;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_TOO_STRONG = 6;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_BEST_MOVE_TOO_LOSING = 7;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_ABSOLUTE = 8;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_RELATIVE = 9;
  PUZZLE_GEN_FAILURE_TYPE_PLAYER_MOVE_NOT_CRITICAL = 10;
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03958"></a>
## FND-03958: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_BEST_MOVE_TOO_LOSING = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_BEST_MOVE_TOO_LOSING = 7;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 973.

```text
N_FAILURE_TYPE_BEFORE_PITCH_TOO_WINNING = 5;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_TOO_STRONG = 6;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_BEST_MOVE_TOO_LOSING = 7;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_ABSOLUTE = 8;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_RELATIVE = 9;
  PUZZLE_GEN_FAILURE_TYPE_PLAYER_MOVE_NOT_CRITICAL = 10;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_NOT_A_MISTAKE =
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03959"></a>
## FND-03959: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_ABSOLUTE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_ABSOLUTE = 8;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1038.

```text
_TYPE_PITCH_MOVE_TOO_STRONG = 6;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_BEST_MOVE_TOO_LOSING = 7;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_ABSOLUTE = 8;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_RELATIVE = 9;
  PUZZLE_GEN_FAILURE_TYPE_PLAYER_MOVE_NOT_CRITICAL = 10;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_NOT_A_MISTAKE = 11;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_GAME_PHASE = 12
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03960"></a>
## FND-03960: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_RELATIVE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_RELATIVE = 9;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1112.

```text
ST_MOVE_TOO_LOSING = 7;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_ABSOLUTE = 8;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_RELATIVE = 9;
  PUZZLE_GEN_FAILURE_TYPE_PLAYER_MOVE_NOT_CRITICAL = 10;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_NOT_A_MISTAKE = 11;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_GAME_PHASE = 12;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_LOSES_MATERIAL = 13;
  PUZZLE_GEN_F
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03961"></a>
## FND-03961: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PLAYER_MOVE_NOT_CRITICAL = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_PLAYER_MOVE_NOT_CRITICAL = 10;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1186.

```text
O_WINNING_ABSOLUTE = 8;
  PUZZLE_GEN_FAILURE_TYPE_AFTER_PLAYER_ALT_MOVE_TOO_WINNING_RELATIVE = 9;
  PUZZLE_GEN_FAILURE_TYPE_PLAYER_MOVE_NOT_CRITICAL = 10;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_NOT_A_MISTAKE = 11;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_GAME_PHASE = 12;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_LOSES_MATERIAL = 13;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_MATERIAL_IMBALANCE = 14;
  PUZZLE_GEN_FAILURE_TYPE_
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03962"></a>
## FND-03962: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_NOT_A_MISTAKE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_NOT_A_MISTAKE = 11;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1243.

```text
LAYER_ALT_MOVE_TOO_WINNING_RELATIVE = 9;
  PUZZLE_GEN_FAILURE_TYPE_PLAYER_MOVE_NOT_CRITICAL = 10;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_NOT_A_MISTAKE = 11;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_GAME_PHASE = 12;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_LOSES_MATERIAL = 13;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_MATERIAL_IMBALANCE = 14;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_EXPECTED_OUTCOME = 15;
  PUZZLE_GEN_FA
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03963"></a>
## FND-03963: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_GAME_PHASE = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_GAME_PHASE = 12;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1300.

```text
LURE_TYPE_PLAYER_MOVE_NOT_CRITICAL = 10;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_NOT_A_MISTAKE = 11;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_GAME_PHASE = 12;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_LOSES_MATERIAL = 13;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_MATERIAL_IMBALANCE = 14;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_EXPECTED_OUTCOME = 15;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_BOARD_EVENT = 16;
}

messag
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03964"></a>
## FND-03964: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_LOSES_MATERIAL = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_LOSES_MATERIAL = 13;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1362.

```text
TYPE_PITCH_MOVE_NOT_A_MISTAKE = 11;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_GAME_PHASE = 12;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_LOSES_MATERIAL = 13;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_MATERIAL_IMBALANCE = 14;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_EXPECTED_OUTCOME = 15;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_BOARD_EVENT = 16;
}

message PuzzleGenFailureReason {
  optional .chesscom.explanation_en
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03965"></a>
## FND-03965: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_MATERIAL_IMBALANCE = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_MATERIAL_IMBALANCE = 14;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1420.

```text
YPE_PITCH_MOVE_INVALID_GAME_PHASE = 12;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_LOSES_MATERIAL = 13;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_MATERIAL_IMBALANCE = 14;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_EXPECTED_OUTCOME = 15;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_BOARD_EVENT = 16;
}

message PuzzleGenFailureReason {
  optional .chesscom.explanation_engine.v1.PuzzleGenPhase failure_phase = 1;
  optional .ches
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03966"></a>
## FND-03966: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_EXPECTED_OUTCOME = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_EXPECTED_OUTCOME = 15;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1482.

```text
YPE_PITCH_MOVE_LOSES_MATERIAL = 13;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_MATERIAL_IMBALANCE = 14;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_EXPECTED_OUTCOME = 15;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_BOARD_EVENT = 16;
}

message PuzzleGenFailureReason {
  optional .chesscom.explanation_engine.v1.PuzzleGenPhase failure_phase = 1;
  optional .chesscom.explanation_engine.v1.PuzzleGenFailureType failure_type =
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03967"></a>
## FND-03967: chesscom.explanation_engine.v1.PuzzleGenFailureType.PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_BOARD_EVENT = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_BOARD_EVENT = 16;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1550.

```text
MOVE_MATERIAL_IMBALANCE = 14;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_EXPECTED_OUTCOME = 15;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_BOARD_EVENT = 16;
}

message PuzzleGenFailureReason {
  optional .chesscom.explanation_engine.v1.PuzzleGenPhase failure_phase = 1;
  optional .chesscom.explanation_engine.v1.PuzzleGenFailureType failure_type = 2;
  optional string failure_message = 3;
}

message InternalFeatur
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03968"></a>
## FND-03968: message declaration: chesscom.explanation_engine.v1.PuzzleGenFailureReason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PuzzleGenFailureReason {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1614.

```text
VE_INVALID_EXPECTED_OUTCOME = 15;
  PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_BOARD_EVENT = 16;
}

message PuzzleGenFailureReason {
  optional .chesscom.explanation_engine.v1.PuzzleGenPhase failure_phase = 1;
  optional .chesscom.explanation_engine.v1.PuzzleGenFailureType failure_type = 2;
  optional string failure_message = 3;
}

message InternalFeaturePuzzleGenRequest {
  oneof _do_puzzle_tree_generation {
  bool 
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03969"></a>
## FND-03969: chesscom.explanation_engine.v1.PuzzleGenFailureReason.failure_phase = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.PuzzleGenPhase failure_phase = 1;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1649.

```text
 PUZZLE_GEN_FAILURE_TYPE_PITCH_MOVE_INVALID_BOARD_EVENT = 16;
}

message PuzzleGenFailureReason {
  optional .chesscom.explanation_engine.v1.PuzzleGenPhase failure_phase = 1;
  optional .chesscom.explanation_engine.v1.PuzzleGenFailureType failure_type = 2;
  optional string failure_message = 3;
}

message InternalFeaturePuzzleGenRequest {
  oneof _do_puzzle_tree_generation {
  bool do_puzzle_tree_generation = 3;
  }

```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03970"></a>
## FND-03970: chesscom.explanation_engine.v1.PuzzleGenFailureReason.failure_type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.PuzzleGenFailureType failure_type = 2;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1726.

```text
leGenFailureReason {
  optional .chesscom.explanation_engine.v1.PuzzleGenPhase failure_phase = 1;
  optional .chesscom.explanation_engine.v1.PuzzleGenFailureType failure_type = 2;
  optional string failure_message = 3;
}

message InternalFeaturePuzzleGenRequest {
  oneof _do_puzzle_tree_generation {
  bool do_puzzle_tree_generation = 3;
  }
  oneof _do_selected_line_verification {
  bool do_selected_line_verification
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03971"></a>
## FND-03971: chesscom.explanation_engine.v1.PuzzleGenFailureReason.failure_message = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string failure_message = 3;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1808.

```text
lure_phase = 1;
  optional .chesscom.explanation_engine.v1.PuzzleGenFailureType failure_type = 2;
  optional string failure_message = 3;
}

message InternalFeaturePuzzleGenRequest {
  oneof _do_puzzle_tree_generation {
  bool do_puzzle_tree_generation = 3;
  }
  oneof _do_selected_line_verification {
  bool do_selected_line_verification = 4;
  }
  oneof _do_pitch_verification {
  bool do_pitch_verification = 5;
  }
 
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03972"></a>
## FND-03972: message declaration: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InternalFeaturePuzzleGenRequest {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1848.

```text
lanation_engine.v1.PuzzleGenFailureType failure_type = 2;
  optional string failure_message = 3;
}

message InternalFeaturePuzzleGenRequest {
  oneof _do_puzzle_tree_generation {
  bool do_puzzle_tree_generation = 3;
  }
  oneof _do_selected_line_verification {
  bool do_selected_line_verification = 4;
  }
  oneof _do_pitch_verification {
  bool do_pitch_verification = 5;
  }
  oneof _add_variations_to_pgn {
  bool a
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03973"></a>
## FND-03973: oneof declaration: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest._do_puzzle_tree_generation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _do_puzzle_tree_generation {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1892.

```text
ure_type = 2;
  optional string failure_message = 3;
}

message InternalFeaturePuzzleGenRequest {
  oneof _do_puzzle_tree_generation {
  bool do_puzzle_tree_generation = 3;
  }
  oneof _do_selected_line_verification {
  bool do_selected_line_verification = 4;
  }
  oneof _do_pitch_verification {
  bool do_pitch_verification = 5;
  }
  oneof _add_variations_to_pgn {
  bool add_variations_to_pgn = 6;
  }
  oneof _mode 
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03974"></a>
## FND-03974: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.do_puzzle_tree_generation = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool do_puzzle_tree_generation = 3;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1929.

```text
re_message = 3;
}

message InternalFeaturePuzzleGenRequest {
  oneof _do_puzzle_tree_generation {
  bool do_puzzle_tree_generation = 3;
  }
  oneof _do_selected_line_verification {
  bool do_selected_line_verification = 4;
  }
  oneof _do_pitch_verification {
  bool do_pitch_verification = 5;
  }
  oneof _add_variations_to_pgn {
  bool add_variations_to_pgn = 6;
  }
  oneof _mode {
  .chesscom.explanation_engine.v1.P
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
