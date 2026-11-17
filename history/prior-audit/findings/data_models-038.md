# data_models — findings 3701–3800

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-03975"></a>
## FND-03975: oneof declaration: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest._do_selected_line_verification

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _do_selected_line_verification {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 1971.

```text
PuzzleGenRequest {
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
  .chesscom.explanation_engine.v1.PuzzleGenMode mode = 7;
  }
  oneof _engine
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03976"></a>
## FND-03976: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.do_selected_line_verification = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool do_selected_line_verification = 4;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2012.

```text
e_generation {
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
  .chesscom.explanation_engine.v1.PuzzleGenMode mode = 7;
  }
  oneof _engine {
  .chesscom.explanation_engine.v1.CeeI
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03977"></a>
## FND-03977: oneof declaration: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest._do_pitch_verification

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _do_pitch_verification {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2058.

```text
n = 3;
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
  .chesscom.explanation_engine.v1.PuzzleGenMode mode = 7;
  }
  oneof _engine {
  .chesscom.explanation_engine.v1.CeeInternalEngine engine = 8;
  }
  oneof _include
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03978"></a>
## FND-03978: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.do_pitch_verification = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool do_pitch_verification = 5;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2091.

```text
ine_verification {
  bool do_selected_line_verification = 4;
  }
  oneof _do_pitch_verification {
  bool do_pitch_verification = 5;
  }
  oneof _add_variations_to_pgn {
  bool add_variations_to_pgn = 6;
  }
  oneof _mode {
  .chesscom.explanation_engine.v1.PuzzleGenMode mode = 7;
  }
  oneof _engine {
  .chesscom.explanation_engine.v1.CeeInternalEngine engine = 8;
  }
  oneof _include_board_events_in_pgn {
  bool inc
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03979"></a>
## FND-03979: oneof declaration: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest._add_variations_to_pgn

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _add_variations_to_pgn {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2129.

```text
line_verification = 4;
  }
  oneof _do_pitch_verification {
  bool do_pitch_verification = 5;
  }
  oneof _add_variations_to_pgn {
  bool add_variations_to_pgn = 6;
  }
  oneof _mode {
  .chesscom.explanation_engine.v1.PuzzleGenMode mode = 7;
  }
  oneof _engine {
  .chesscom.explanation_engine.v1.CeeInternalEngine engine = 8;
  }
  oneof _include_board_events_in_pgn {
  bool include_board_events_in_pgn = 9;
  }
  on
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03980"></a>
## FND-03980: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.add_variations_to_pgn = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool add_variations_to_pgn = 6;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2162.

```text
f _do_pitch_verification {
  bool do_pitch_verification = 5;
  }
  oneof _add_variations_to_pgn {
  bool add_variations_to_pgn = 6;
  }
  oneof _mode {
  .chesscom.explanation_engine.v1.PuzzleGenMode mode = 7;
  }
  oneof _engine {
  .chesscom.explanation_engine.v1.CeeInternalEngine engine = 8;
  }
  oneof _include_board_events_in_pgn {
  bool include_board_events_in_pgn = 9;
  }
  oneof _filter_board_events_in_pgn {
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03981"></a>
## FND-03981: oneof declaration: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest._mode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _mode {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2200.

```text
itch_verification = 5;
  }
  oneof _add_variations_to_pgn {
  bool add_variations_to_pgn = 6;
  }
  oneof _mode {
  .chesscom.explanation_engine.v1.PuzzleGenMode mode = 7;
  }
  oneof _engine {
  .chesscom.explanation_engine.v1.CeeInternalEngine engine = 8;
  }
  oneof _include_board_events_in_pgn {
  bool include_board_events_in_pgn = 9;
  }
  oneof _filter_board_events_in_pgn {
  bool filter_board_events_in_pgn = 1
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03982"></a>
## FND-03982: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.mode = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleGenMode mode = 7;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2216.

```text
n = 5;
  }
  oneof _add_variations_to_pgn {
  bool add_variations_to_pgn = 6;
  }
  oneof _mode {
  .chesscom.explanation_engine.v1.PuzzleGenMode mode = 7;
  }
  oneof _engine {
  .chesscom.explanation_engine.v1.CeeInternalEngine engine = 8;
  }
  oneof _include_board_events_in_pgn {
  bool include_board_events_in_pgn = 9;
  }
  oneof _filter_board_events_in_pgn {
  bool filter_board_events_in_pgn = 10;
  }
  oneof _
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03983"></a>
## FND-03983: oneof declaration: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest._engine

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _engine {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2278.

```text
ons_to_pgn = 6;
  }
  oneof _mode {
  .chesscom.explanation_engine.v1.PuzzleGenMode mode = 7;
  }
  oneof _engine {
  .chesscom.explanation_engine.v1.CeeInternalEngine engine = 8;
  }
  oneof _include_board_events_in_pgn {
  bool include_board_events_in_pgn = 9;
  }
  oneof _filter_board_events_in_pgn {
  bool filter_board_events_in_pgn = 10;
  }
  oneof _include_speech_in_pgn {
  bool include_speech_in_pgn = 11;
  }
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03984"></a>
## FND-03984: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.engine = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.CeeInternalEngine engine = 8;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2296.

```text
}
  oneof _mode {
  .chesscom.explanation_engine.v1.PuzzleGenMode mode = 7;
  }
  oneof _engine {
  .chesscom.explanation_engine.v1.CeeInternalEngine engine = 8;
  }
  oneof _include_board_events_in_pgn {
  bool include_board_events_in_pgn = 9;
  }
  oneof _filter_board_events_in_pgn {
  bool filter_board_events_in_pgn = 10;
  }
  oneof _include_speech_in_pgn {
  bool include_speech_in_pgn = 11;
  }
  optional bool s
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03985"></a>
## FND-03985: oneof declaration: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest._include_board_events_in_pgn

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _include_board_events_in_pgn {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2364.

```text
de = 7;
  }
  oneof _engine {
  .chesscom.explanation_engine.v1.CeeInternalEngine engine = 8;
  }
  oneof _include_board_events_in_pgn {
  bool include_board_events_in_pgn = 9;
  }
  oneof _filter_board_events_in_pgn {
  bool filter_board_events_in_pgn = 10;
  }
  oneof _include_speech_in_pgn {
  bool include_speech_in_pgn = 11;
  }
  optional bool stream_progress = 1;
  repeated .chesscom.chess.v1.Move full_selected
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03986"></a>
## FND-03986: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.include_board_events_in_pgn = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool include_board_events_in_pgn = 9;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2403.

```text
om.explanation_engine.v1.CeeInternalEngine engine = 8;
  }
  oneof _include_board_events_in_pgn {
  bool include_board_events_in_pgn = 9;
  }
  oneof _filter_board_events_in_pgn {
  bool filter_board_events_in_pgn = 10;
  }
  oneof _include_speech_in_pgn {
  bool include_speech_in_pgn = 11;
  }
  optional bool stream_progress = 1;
  repeated .chesscom.chess.v1.Move full_selected_line = 2;
  optional int32 heartbeat_i
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03987"></a>
## FND-03987: oneof declaration: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest._filter_board_events_in_pgn

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _filter_board_events_in_pgn {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2447.

```text
ngine = 8;
  }
  oneof _include_board_events_in_pgn {
  bool include_board_events_in_pgn = 9;
  }
  oneof _filter_board_events_in_pgn {
  bool filter_board_events_in_pgn = 10;
  }
  oneof _include_speech_in_pgn {
  bool include_speech_in_pgn = 11;
  }
  optional bool stream_progress = 1;
  repeated .chesscom.chess.v1.Move full_selected_line = 2;
  optional int32 heartbeat_interval_seconds = 12;
}

message InternalFea
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03988"></a>
## FND-03988: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.filter_board_events_in_pgn = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool filter_board_events_in_pgn = 10;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2485.

```text
events_in_pgn {
  bool include_board_events_in_pgn = 9;
  }
  oneof _filter_board_events_in_pgn {
  bool filter_board_events_in_pgn = 10;
  }
  oneof _include_speech_in_pgn {
  bool include_speech_in_pgn = 11;
  }
  optional bool stream_progress = 1;
  repeated .chesscom.chess.v1.Move full_selected_line = 2;
  optional int32 heartbeat_interval_seconds = 12;
}

message InternalFeaturePuzzleGenResponse {
  oneof puzzle
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03989"></a>
## FND-03989: oneof declaration: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest._include_speech_in_pgn

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _include_speech_in_pgn {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2529.

```text
in_pgn = 9;
  }
  oneof _filter_board_events_in_pgn {
  bool filter_board_events_in_pgn = 10;
  }
  oneof _include_speech_in_pgn {
  bool include_speech_in_pgn = 11;
  }
  optional bool stream_progress = 1;
  repeated .chesscom.chess.v1.Move full_selected_line = 2;
  optional int32 heartbeat_interval_seconds = 12;
}

message InternalFeaturePuzzleGenResponse {
  oneof puzzle_response {
  .chesscom.explanation_engine.v
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03990"></a>
## FND-03990: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.include_speech_in_pgn = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool include_speech_in_pgn = 11;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2562.

```text
oard_events_in_pgn {
  bool filter_board_events_in_pgn = 10;
  }
  oneof _include_speech_in_pgn {
  bool include_speech_in_pgn = 11;
  }
  optional bool stream_progress = 1;
  repeated .chesscom.chess.v1.Move full_selected_line = 2;
  optional int32 heartbeat_interval_seconds = 12;
}

message InternalFeaturePuzzleGenResponse {
  oneof puzzle_response {
  .chesscom.explanation_engine.v1.PuzzleGen puzzle_gen = 1;
  .ch
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03991"></a>
## FND-03991: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.stream_progress = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool stream_progress = 1;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2601.

```text
d_events_in_pgn = 10;
  }
  oneof _include_speech_in_pgn {
  bool include_speech_in_pgn = 11;
  }
  optional bool stream_progress = 1;
  repeated .chesscom.chess.v1.Move full_selected_line = 2;
  optional int32 heartbeat_interval_seconds = 12;
}

message InternalFeaturePuzzleGenResponse {
  oneof puzzle_response {
  .chesscom.explanation_engine.v1.PuzzleGen puzzle_gen = 1;
  .chesscom.explanation_engine.v1.PuzzleGenP
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03992"></a>
## FND-03992: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.full_selected_line = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Move full_selected_line = 2;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2638.

```text
clude_speech_in_pgn {
  bool include_speech_in_pgn = 11;
  }
  optional bool stream_progress = 1;
  repeated .chesscom.chess.v1.Move full_selected_line = 2;
  optional int32 heartbeat_interval_seconds = 12;
}

message InternalFeaturePuzzleGenResponse {
  oneof puzzle_response {
  .chesscom.explanation_engine.v1.PuzzleGen puzzle_gen = 1;
  .chesscom.explanation_engine.v1.PuzzleGenPhase progress = 2;
  }
  oneof _failu
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03993"></a>
## FND-03993: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenRequest.heartbeat_interval_seconds = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 heartbeat_interval_seconds = 12;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2697.

```text
}
  optional bool stream_progress = 1;
  repeated .chesscom.chess.v1.Move full_selected_line = 2;
  optional int32 heartbeat_interval_seconds = 12;
}

message InternalFeaturePuzzleGenResponse {
  oneof puzzle_response {
  .chesscom.explanation_engine.v1.PuzzleGen puzzle_gen = 1;
  .chesscom.explanation_engine.v1.PuzzleGenPhase progress = 2;
  }
  oneof _failure_reason {
  .chesscom.explanation_engine.v1.PuzzleGenFail
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03994"></a>
## FND-03994: message declaration: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InternalFeaturePuzzleGenResponse {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2748.

```text
chesscom.chess.v1.Move full_selected_line = 2;
  optional int32 heartbeat_interval_seconds = 12;
}

message InternalFeaturePuzzleGenResponse {
  oneof puzzle_response {
  .chesscom.explanation_engine.v1.PuzzleGen puzzle_gen = 1;
  .chesscom.explanation_engine.v1.PuzzleGenPhase progress = 2;
  }
  oneof _failure_reason {
  .chesscom.explanation_engine.v1.PuzzleGenFailureReason failure_reason = 4;
  }
  optional string
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03995"></a>
## FND-03995: oneof declaration: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse.puzzle_response

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof puzzle_response {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2793.

```text
;
  optional int32 heartbeat_interval_seconds = 12;
}

message InternalFeaturePuzzleGenResponse {
  oneof puzzle_response {
  .chesscom.explanation_engine.v1.PuzzleGen puzzle_gen = 1;
  .chesscom.explanation_engine.v1.PuzzleGenPhase progress = 2;
  }
  oneof _failure_reason {
  .chesscom.explanation_engine.v1.PuzzleGenFailureReason failure_reason = 4;
  }
  optional string log = 3;
  optional bool is_heartbeat = 5;
}
```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03996"></a>
## FND-03996: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse.puzzle_gen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleGen puzzle_gen = 1;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2819.

```text
at_interval_seconds = 12;
}

message InternalFeaturePuzzleGenResponse {
  oneof puzzle_response {
  .chesscom.explanation_engine.v1.PuzzleGen puzzle_gen = 1;
  .chesscom.explanation_engine.v1.PuzzleGenPhase progress = 2;
  }
  oneof _failure_reason {
  .chesscom.explanation_engine.v1.PuzzleGenFailureReason failure_reason = 4;
  }
  optional string log = 3;
  optional bool is_heartbeat = 5;
}

```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03997"></a>
## FND-03997: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse.progress = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleGenPhase progress = 2;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2879.

```text
nResponse {
  oneof puzzle_response {
  .chesscom.explanation_engine.v1.PuzzleGen puzzle_gen = 1;
  .chesscom.explanation_engine.v1.PuzzleGenPhase progress = 2;
  }
  oneof _failure_reason {
  .chesscom.explanation_engine.v1.PuzzleGenFailureReason failure_reason = 4;
  }
  optional string log = 3;
  optional bool is_heartbeat = 5;
}

```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03998"></a>
## FND-03998: oneof declaration: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse._failure_reason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _failure_reason {

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2946.

```text
e.v1.PuzzleGen puzzle_gen = 1;
  .chesscom.explanation_engine.v1.PuzzleGenPhase progress = 2;
  }
  oneof _failure_reason {
  .chesscom.explanation_engine.v1.PuzzleGenFailureReason failure_reason = 4;
  }
  optional string log = 3;
  optional bool is_heartbeat = 5;
}

```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03999"></a>
## FND-03999: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse.failure_reason = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PuzzleGenFailureReason failure_reason = 4;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 2972.

```text
= 1;
  .chesscom.explanation_engine.v1.PuzzleGenPhase progress = 2;
  }
  oneof _failure_reason {
  .chesscom.explanation_engine.v1.PuzzleGenFailureReason failure_reason = 4;
  }
  optional string log = 3;
  optional bool is_heartbeat = 5;
}

```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04000"></a>
## FND-04000: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse.log = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string log = 3;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 3053.

```text
failure_reason {
  .chesscom.explanation_engine.v1.PuzzleGenFailureReason failure_reason = 4;
  }
  optional string log = 3;
  optional bool is_heartbeat = 5;
}

```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04001"></a>
## FND-04001: chesscom.explanation_engine.v1.InternalFeaturePuzzleGenResponse.is_heartbeat = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_heartbeat = 5;

### Evidence

- **SRC-0409** `research/proto/chesscom/explanation_engine/v1/internal_feature_puzzle_gen.proto` — [preserved redacted evidence](../evidence/text/0deb8fbc33da2d8a6c3445df4c6269689e3b28c35dbac8bbb722990608ab9d80.proto)
  Character offset 3080.

```text
m.explanation_engine.v1.PuzzleGenFailureReason failure_reason = 4;
  }
  optional string log = 3;
  optional bool is_heartbeat = 5;
}

```

**Source references:** SRC-0409, SRC-1380  
**URL references:** None independently associated  
**Related findings:** FND-03939, FND-03940, FND-03941

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04002"></a>
## FND-04002: message declaration: chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InternalFeatureUpdateDeveloperOptionsRequest {

### Evidence

- **SRC-0410** `research/proto/chesscom/explanation_engine/v1/internal_feature_update_developer_options.proto` — [preserved redacted evidence](../evidence/text/685a53093142e19f4c7353f627c2833c65ef29ea2eada6dd2b9a96eb5d1103be.proto)
  Character offset 150.

```text
_feature_update_developer_options.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message InternalFeatureUpdateDeveloperOptionsRequest {
  optional .chesscom.explanation_engine.v1.DeveloperOptions options = 1;
}

message InternalFeatureUpdateDeveloperOptionsResponse {
  optional .chesscom.explanation_engine.v1.DeveloperOptions options = 1;
}

message DeveloperOptions {
  oneof _coach_debug_info {
  
```

**Source references:** SRC-0410, SRC-1381  
**URL references:** None independently associated  
**Related findings:** FND-04003, FND-04004

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04003"></a>
## FND-04003: chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsRequest.options = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.DeveloperOptions options = 1;

### Evidence

- **SRC-0410** `research/proto/chesscom/explanation_engine/v1/internal_feature_update_developer_options.proto` — [preserved redacted evidence](../evidence/text/685a53093142e19f4c7353f627c2833c65ef29ea2eada6dd2b9a96eb5d1103be.proto)
  Character offset 207.

```text


package chesscom.explanation_engine.v1;

message InternalFeatureUpdateDeveloperOptionsRequest {
  optional .chesscom.explanation_engine.v1.DeveloperOptions options = 1;
}

message InternalFeatureUpdateDeveloperOptionsResponse {
  optional .chesscom.explanation_engine.v1.DeveloperOptions options = 1;
}

message DeveloperOptions {
  oneof _coach_debug_info {
  bool coach_debug_info = 3;
  }
  oneof _assume_speech_alw
```

**Source references:** SRC-0410, SRC-1381  
**URL references:** None independently associated  
**Related findings:** FND-04002, FND-04004

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04004"></a>
## FND-04004: message declaration: chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InternalFeatureUpdateDeveloperOptionsResponse {

### Evidence

- **SRC-0410** `research/proto/chesscom/explanation_engine/v1/internal_feature_update_developer_options.proto` — [preserved redacted evidence](../evidence/text/685a53093142e19f4c7353f627c2833c65ef29ea2eada6dd2b9a96eb5d1103be.proto)
  Character offset 281.

```text
veloperOptionsRequest {
  optional .chesscom.explanation_engine.v1.DeveloperOptions options = 1;
}

message InternalFeatureUpdateDeveloperOptionsResponse {
  optional .chesscom.explanation_engine.v1.DeveloperOptions options = 1;
}

message DeveloperOptions {
  oneof _coach_debug_info {
  bool coach_debug_info = 3;
  }
  oneof _assume_speech_always_present {
  bool assume_speech_always_present = 4;
  }
}

```

**Source references:** SRC-0410, SRC-1381  
**URL references:** None independently associated  
**Related findings:** FND-04002, FND-04003

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04005"></a>
## FND-04005: chesscom.explanation_engine.v1.InternalFeatureUpdateDeveloperOptionsResponse.options = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.DeveloperOptions options = 1;

### Evidence

- **SRC-0410** `research/proto/chesscom/explanation_engine/v1/internal_feature_update_developer_options.proto` — [preserved redacted evidence](../evidence/text/685a53093142e19f4c7353f627c2833c65ef29ea2eada6dd2b9a96eb5d1103be.proto)
  Character offset 207.

```text


package chesscom.explanation_engine.v1;

message InternalFeatureUpdateDeveloperOptionsRequest {
  optional .chesscom.explanation_engine.v1.DeveloperOptions options = 1;
}

message InternalFeatureUpdateDeveloperOptionsResponse {
  optional .chesscom.explanation_engine.v1.DeveloperOptions options = 1;
}

message DeveloperOptions {
  oneof _coach_debug_info {
  bool coach_debug_info = 3;
  }
  oneof _assume_speech_alw
```

**Source references:** SRC-0410, SRC-1381  
**URL references:** None independently associated  
**Related findings:** FND-04002, FND-04003, FND-04004

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04006"></a>
## FND-04006: message declaration: chesscom.explanation_engine.v1.DeveloperOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DeveloperOptions {

### Evidence

- **SRC-0410** `research/proto/chesscom/explanation_engine/v1/internal_feature_update_developer_options.proto` — [preserved redacted evidence](../evidence/text/685a53093142e19f4c7353f627c2833c65ef29ea2eada6dd2b9a96eb5d1103be.proto)
  Character offset 413.

```text
eloperOptionsResponse {
  optional .chesscom.explanation_engine.v1.DeveloperOptions options = 1;
}

message DeveloperOptions {
  oneof _coach_debug_info {
  bool coach_debug_info = 3;
  }
  oneof _assume_speech_always_present {
  bool assume_speech_always_present = 4;
  }
}

```

**Source references:** SRC-0410, SRC-1381  
**URL references:** None independently associated  
**Related findings:** FND-04002, FND-04003, FND-04004

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04007"></a>
## FND-04007: oneof declaration: chesscom.explanation_engine.v1.DeveloperOptions._coach_debug_info

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _coach_debug_info {

### Evidence

- **SRC-0410** `research/proto/chesscom/explanation_engine/v1/internal_feature_update_developer_options.proto` — [preserved redacted evidence](../evidence/text/685a53093142e19f4c7353f627c2833c65ef29ea2eada6dd2b9a96eb5d1103be.proto)
  Character offset 442.

```text
ional .chesscom.explanation_engine.v1.DeveloperOptions options = 1;
}

message DeveloperOptions {
  oneof _coach_debug_info {
  bool coach_debug_info = 3;
  }
  oneof _assume_speech_always_present {
  bool assume_speech_always_present = 4;
  }
}

```

**Source references:** SRC-0410, SRC-1381  
**URL references:** None independently associated  
**Related findings:** FND-04002, FND-04003, FND-04004

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04008"></a>
## FND-04008: chesscom.explanation_engine.v1.DeveloperOptions.coach_debug_info = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool coach_debug_info = 3;

### Evidence

- **SRC-0410** `research/proto/chesscom/explanation_engine/v1/internal_feature_update_developer_options.proto` — [preserved redacted evidence](../evidence/text/685a53093142e19f4c7353f627c2833c65ef29ea2eada6dd2b9a96eb5d1103be.proto)
  Character offset 470.

```text
engine.v1.DeveloperOptions options = 1;
}

message DeveloperOptions {
  oneof _coach_debug_info {
  bool coach_debug_info = 3;
  }
  oneof _assume_speech_always_present {
  bool assume_speech_always_present = 4;
  }
}

```

**Source references:** SRC-0410, SRC-1381  
**URL references:** None independently associated  
**Related findings:** FND-04002, FND-04003, FND-04004

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04009"></a>
## FND-04009: oneof declaration: chesscom.explanation_engine.v1.DeveloperOptions._assume_speech_always_present

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _assume_speech_always_present {

### Evidence

- **SRC-0410** `research/proto/chesscom/explanation_engine/v1/internal_feature_update_developer_options.proto` — [preserved redacted evidence](../evidence/text/685a53093142e19f4c7353f627c2833c65ef29ea2eada6dd2b9a96eb5d1103be.proto)
  Character offset 503.

```text
s = 1;
}

message DeveloperOptions {
  oneof _coach_debug_info {
  bool coach_debug_info = 3;
  }
  oneof _assume_speech_always_present {
  bool assume_speech_always_present = 4;
  }
}

```

**Source references:** SRC-0410, SRC-1381  
**URL references:** None independently associated  
**Related findings:** FND-04002, FND-04003, FND-04004

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04010"></a>
## FND-04010: chesscom.explanation_engine.v1.DeveloperOptions.assume_speech_always_present = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool assume_speech_always_present = 4;

### Evidence

- **SRC-0410** `research/proto/chesscom/explanation_engine/v1/internal_feature_update_developer_options.proto` — [preserved redacted evidence](../evidence/text/685a53093142e19f4c7353f627c2833c65ef29ea2eada6dd2b9a96eb5d1103be.proto)
  Character offset 543.

```text
neof _coach_debug_info {
  bool coach_debug_info = 3;
  }
  oneof _assume_speech_always_present {
  bool assume_speech_always_present = 4;
  }
}

```

**Source references:** SRC-0410, SRC-1381  
**URL references:** None independently associated  
**Related findings:** FND-04002, FND-04003, FND-04004

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04011"></a>
## FND-04011: message declaration: chesscom.explanation_engine.v1.InvalidGameUnparsable

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InvalidGameUnparsable {

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 121.

```text
xplanation_engine/v1/invalid_game.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message InvalidGameUnparsable {
}

message InvalidGameIllegalMove {
}

message InvalidGameIllegalKingCount {
}

message InvalidGamePawnOnBackRank {
}

message InvalidGameKingsAdjacent {
}

message InvalidGameKingCapturable {
}

message InvalidGame {
  oneof invalid_game {
  .chesscom.explanation_engine.v1.InvalidGameUn
```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04012, FND-04013

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04012"></a>
## FND-04012: message declaration: chesscom.explanation_engine.v1.InvalidGameIllegalMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InvalidGameIllegalMove {

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 156.

```text
roto
// syntax: proto3

package chesscom.explanation_engine.v1;

message InvalidGameUnparsable {
}

message InvalidGameIllegalMove {
}

message InvalidGameIllegalKingCount {
}

message InvalidGamePawnOnBackRank {
}

message InvalidGameKingsAdjacent {
}

message InvalidGameKingCapturable {
}

message InvalidGame {
  oneof invalid_game {
  .chesscom.explanation_engine.v1.InvalidGameUnparsable unparsable = 1;
  .chessco
```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04011, FND-04013

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04013"></a>
## FND-04013: message declaration: chesscom.explanation_engine.v1.InvalidGameIllegalKingCount

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InvalidGameIllegalKingCount {

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 192.

```text
scom.explanation_engine.v1;

message InvalidGameUnparsable {
}

message InvalidGameIllegalMove {
}

message InvalidGameIllegalKingCount {
}

message InvalidGamePawnOnBackRank {
}

message InvalidGameKingsAdjacent {
}

message InvalidGameKingCapturable {
}

message InvalidGame {
  oneof invalid_game {
  .chesscom.explanation_engine.v1.InvalidGameUnparsable unparsable = 1;
  .chesscom.explanation_engine.v1.InvalidGameI
```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04011, FND-04012

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04014"></a>
## FND-04014: message declaration: chesscom.explanation_engine.v1.InvalidGamePawnOnBackRank

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InvalidGamePawnOnBackRank {

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 233.

```text
lidGameUnparsable {
}

message InvalidGameIllegalMove {
}

message InvalidGameIllegalKingCount {
}

message InvalidGamePawnOnBackRank {
}

message InvalidGameKingsAdjacent {
}

message InvalidGameKingCapturable {
}

message InvalidGame {
  oneof invalid_game {
  .chesscom.explanation_engine.v1.InvalidGameUnparsable unparsable = 1;
  .chesscom.explanation_engine.v1.InvalidGameIllegalMove illegal_move = 2;
  .chesscom.
```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04011, FND-04012, FND-04013

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04015"></a>
## FND-04015: message declaration: chesscom.explanation_engine.v1.InvalidGameKingsAdjacent

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InvalidGameKingsAdjacent {

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 272.

```text
ameIllegalMove {
}

message InvalidGameIllegalKingCount {
}

message InvalidGamePawnOnBackRank {
}

message InvalidGameKingsAdjacent {
}

message InvalidGameKingCapturable {
}

message InvalidGame {
  oneof invalid_game {
  .chesscom.explanation_engine.v1.InvalidGameUnparsable unparsable = 1;
  .chesscom.explanation_engine.v1.InvalidGameIllegalMove illegal_move = 2;
  .chesscom.explanation_engine.v1.InvalidGameIllega
```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04011, FND-04012, FND-04013

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04016"></a>
## FND-04016: message declaration: chesscom.explanation_engine.v1.InvalidGameKingCapturable

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InvalidGameKingCapturable {

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 310.

```text
eIllegalKingCount {
}

message InvalidGamePawnOnBackRank {
}

message InvalidGameKingsAdjacent {
}

message InvalidGameKingCapturable {
}

message InvalidGame {
  oneof invalid_game {
  .chesscom.explanation_engine.v1.InvalidGameUnparsable unparsable = 1;
  .chesscom.explanation_engine.v1.InvalidGameIllegalMove illegal_move = 2;
  .chesscom.explanation_engine.v1.InvalidGameIllegalKingCount illegal_king_count = 3;
  .
```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04011, FND-04012, FND-04013

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04017"></a>
## FND-04017: message declaration: chesscom.explanation_engine.v1.InvalidGame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InvalidGame {

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 349.

```text
amePawnOnBackRank {
}

message InvalidGameKingsAdjacent {
}

message InvalidGameKingCapturable {
}

message InvalidGame {
  oneof invalid_game {
  .chesscom.explanation_engine.v1.InvalidGameUnparsable unparsable = 1;
  .chesscom.explanation_engine.v1.InvalidGameIllegalMove illegal_move = 2;
  .chesscom.explanation_engine.v1.InvalidGameIllegalKingCount illegal_king_count = 3;
  .chesscom.explanation_engine.v1.InvalidG
```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04011, FND-04012, FND-04013

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04018"></a>
## FND-04018: oneof declaration: chesscom.explanation_engine.v1.InvalidGame.invalid_game

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof invalid_game {

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 373.

```text
essage InvalidGameKingsAdjacent {
}

message InvalidGameKingCapturable {
}

message InvalidGame {
  oneof invalid_game {
  .chesscom.explanation_engine.v1.InvalidGameUnparsable unparsable = 1;
  .chesscom.explanation_engine.v1.InvalidGameIllegalMove illegal_move = 2;
  .chesscom.explanation_engine.v1.InvalidGameIllegalKingCount illegal_king_count = 3;
  .chesscom.explanation_engine.v1.InvalidGamePawnOnBackRank pawn_o
```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04011, FND-04012, FND-04013

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04019"></a>
## FND-04019: chesscom.explanation_engine.v1.InvalidGame.unparsable = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.InvalidGameUnparsable unparsable = 1;

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 396.

```text
Adjacent {
}

message InvalidGameKingCapturable {
}

message InvalidGame {
  oneof invalid_game {
  .chesscom.explanation_engine.v1.InvalidGameUnparsable unparsable = 1;
  .chesscom.explanation_engine.v1.InvalidGameIllegalMove illegal_move = 2;
  .chesscom.explanation_engine.v1.InvalidGameIllegalKingCount illegal_king_count = 3;
  .chesscom.explanation_engine.v1.InvalidGamePawnOnBackRank pawn_on_back_rank = 4;
  .che
```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04011, FND-04012, FND-04013

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04020"></a>
## FND-04020: chesscom.explanation_engine.v1.InvalidGame.illegal_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.InvalidGameIllegalMove illegal_move = 2;

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 468.

```text
 {
  oneof invalid_game {
  .chesscom.explanation_engine.v1.InvalidGameUnparsable unparsable = 1;
  .chesscom.explanation_engine.v1.InvalidGameIllegalMove illegal_move = 2;
  .chesscom.explanation_engine.v1.InvalidGameIllegalKingCount illegal_king_count = 3;
  .chesscom.explanation_engine.v1.InvalidGamePawnOnBackRank pawn_on_back_rank = 4;
  .chesscom.explanation_engine.v1.InvalidGameKingsAdjacent kings_adjacent = 5;
```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04011, FND-04012, FND-04013

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04021"></a>
## FND-04021: chesscom.explanation_engine.v1.InvalidGame.illegal_king_count = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.InvalidGameIllegalKingCount illegal_king_count = 3;

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 543.

```text
rsable unparsable = 1;
  .chesscom.explanation_engine.v1.InvalidGameIllegalMove illegal_move = 2;
  .chesscom.explanation_engine.v1.InvalidGameIllegalKingCount illegal_king_count = 3;
  .chesscom.explanation_engine.v1.InvalidGamePawnOnBackRank pawn_on_back_rank = 4;
  .chesscom.explanation_engine.v1.InvalidGameKingsAdjacent kings_adjacent = 5;
  .chesscom.explanation_engine.v1.InvalidGameKingCapturable king_capturabl
```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04011, FND-04012, FND-04013

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04022"></a>
## FND-04022: chesscom.explanation_engine.v1.InvalidGame.pawn_on_back_rank = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.InvalidGamePawnOnBackRank pawn_on_back_rank = 4;

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 629.

```text
l_move = 2;
  .chesscom.explanation_engine.v1.InvalidGameIllegalKingCount illegal_king_count = 3;
  .chesscom.explanation_engine.v1.InvalidGamePawnOnBackRank pawn_on_back_rank = 4;
  .chesscom.explanation_engine.v1.InvalidGameKingsAdjacent kings_adjacent = 5;
  .chesscom.explanation_engine.v1.InvalidGameKingCapturable king_capturable = 6;
  }
}

```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04011, FND-04012, FND-04013

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04023"></a>
## FND-04023: chesscom.explanation_engine.v1.InvalidGame.kings_adjacent = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.InvalidGameKingsAdjacent kings_adjacent = 5;

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 712.

```text
ing_count = 3;
  .chesscom.explanation_engine.v1.InvalidGamePawnOnBackRank pawn_on_back_rank = 4;
  .chesscom.explanation_engine.v1.InvalidGameKingsAdjacent kings_adjacent = 5;
  .chesscom.explanation_engine.v1.InvalidGameKingCapturable king_capturable = 6;
  }
}

```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04011, FND-04012, FND-04013

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04024"></a>
## FND-04024: chesscom.explanation_engine.v1.InvalidGame.king_capturable = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.InvalidGameKingCapturable king_capturable = 6;

### Evidence

- **SRC-0411** `research/proto/chesscom/explanation_engine/v1/invalid_game.proto` — [preserved redacted evidence](../evidence/text/f517d5647a0af0d70a49c34959e51b9657a6fd8e338c6c6dab234e35f768e2f3.proto)
  Character offset 791.

```text
_on_back_rank = 4;
  .chesscom.explanation_engine.v1.InvalidGameKingsAdjacent kings_adjacent = 5;
  .chesscom.explanation_engine.v1.InvalidGameKingCapturable king_capturable = 6;
  }
}

```

**Source references:** SRC-0411, SRC-1382  
**URL references:** None independently associated  
**Related findings:** FND-04011, FND-04012, FND-04013

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04025"></a>
## FND-04025: enum declaration: chesscom.explanation_engine.v1.Locale

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Locale {

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 117.

```text
om/explanation_engine/v1/language.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum Locale {
  LOCALE_UNSPECIFIED = 0;
  LOCALE_DE_DE = 1;
  LOCALE_EN_US = 2;
  LOCALE_ES_ES = 3;
  LOCALE_FR_FR = 4;
  LOCALE_IT_IT = 5;
  LOCALE_PL_PL = 6;
  LOCALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04026, FND-04027

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04026"></a>
## FND-04026: chesscom.explanation_engine.v1.Locale.LOCALE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOCALE_UNSPECIFIED = 0;

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 133.

```text
ngine/v1/language.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum Locale {
  LOCALE_UNSPECIFIED = 0;
  LOCALE_DE_DE = 1;
  LOCALE_EN_US = 2;
  LOCALE_ES_ES = 3;
  LOCALE_FR_FR = 4;
  LOCALE_IT_IT = 5;
  LOCALE_PL_PL = 6;
  LOCALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04025, FND-04027

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04027"></a>
## FND-04027: chesscom.explanation_engine.v1.Locale.LOCALE_DE_DE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOCALE_DE_DE = 1;

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 159.

```text
 syntax: proto3

package chesscom.explanation_engine.v1;

enum Locale {
  LOCALE_UNSPECIFIED = 0;
  LOCALE_DE_DE = 1;
  LOCALE_EN_US = 2;
  LOCALE_ES_ES = 3;
  LOCALE_FR_FR = 4;
  LOCALE_IT_IT = 5;
  LOCALE_PL_PL = 6;
  LOCALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04025, FND-04026

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04028"></a>
## FND-04028: chesscom.explanation_engine.v1.Locale.LOCALE_EN_US = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOCALE_EN_US = 2;

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 179.

```text
kage chesscom.explanation_engine.v1;

enum Locale {
  LOCALE_UNSPECIFIED = 0;
  LOCALE_DE_DE = 1;
  LOCALE_EN_US = 2;
  LOCALE_ES_ES = 3;
  LOCALE_FR_FR = 4;
  LOCALE_IT_IT = 5;
  LOCALE_PL_PL = 6;
  LOCALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04025, FND-04026, FND-04027

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04029"></a>
## FND-04029: chesscom.explanation_engine.v1.Locale.LOCALE_ES_ES = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOCALE_ES_ES = 3;

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 199.

```text
ation_engine.v1;

enum Locale {
  LOCALE_UNSPECIFIED = 0;
  LOCALE_DE_DE = 1;
  LOCALE_EN_US = 2;
  LOCALE_ES_ES = 3;
  LOCALE_FR_FR = 4;
  LOCALE_IT_IT = 5;
  LOCALE_PL_PL = 6;
  LOCALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04025, FND-04026, FND-04027

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04030"></a>
## FND-04030: chesscom.explanation_engine.v1.Locale.LOCALE_FR_FR = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOCALE_FR_FR = 4;

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 219.

```text
um Locale {
  LOCALE_UNSPECIFIED = 0;
  LOCALE_DE_DE = 1;
  LOCALE_EN_US = 2;
  LOCALE_ES_ES = 3;
  LOCALE_FR_FR = 4;
  LOCALE_IT_IT = 5;
  LOCALE_PL_PL = 6;
  LOCALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04025, FND-04026, FND-04027

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04031"></a>
## FND-04031: chesscom.explanation_engine.v1.Locale.LOCALE_IT_IT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOCALE_IT_IT = 5;

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 239.

```text
_UNSPECIFIED = 0;
  LOCALE_DE_DE = 1;
  LOCALE_EN_US = 2;
  LOCALE_ES_ES = 3;
  LOCALE_FR_FR = 4;
  LOCALE_IT_IT = 5;
  LOCALE_PL_PL = 6;
  LOCALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04025, FND-04026, FND-04027

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04032"></a>
## FND-04032: chesscom.explanation_engine.v1.Locale.LOCALE_PL_PL = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOCALE_PL_PL = 6;

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 259.

```text
LOCALE_DE_DE = 1;
  LOCALE_EN_US = 2;
  LOCALE_ES_ES = 3;
  LOCALE_FR_FR = 4;
  LOCALE_IT_IT = 5;
  LOCALE_PL_PL = 6;
  LOCALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04025, FND-04026, FND-04027

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04033"></a>
## FND-04033: chesscom.explanation_engine.v1.Locale.LOCALE_PT_PT = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOCALE_PT_PT = 7;

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 279.

```text
LOCALE_EN_US = 2;
  LOCALE_ES_ES = 3;
  LOCALE_FR_FR = 4;
  LOCALE_IT_IT = 5;
  LOCALE_PL_PL = 6;
  LOCALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04025, FND-04026, FND-04027

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04034"></a>
## FND-04034: chesscom.explanation_engine.v1.Locale.LOCALE_RU_RU = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOCALE_RU_RU = 8;

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 299.

```text
LOCALE_ES_ES = 3;
  LOCALE_FR_FR = 4;
  LOCALE_IT_IT = 5;
  LOCALE_PL_PL = 6;
  LOCALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04025, FND-04026, FND-04027

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04035"></a>
## FND-04035: chesscom.explanation_engine.v1.Locale.LOCALE_TR_TR = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOCALE_TR_TR = 9;

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 319.

```text
LOCALE_FR_FR = 4;
  LOCALE_IT_IT = 5;
  LOCALE_PL_PL = 6;
  LOCALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04025, FND-04026, FND-04027

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04036"></a>
## FND-04036: chesscom.explanation_engine.v1.Locale.LOCALE_AR_SA = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOCALE_AR_SA = 10;

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 339.

```text
LOCALE_IT_IT = 5;
  LOCALE_PL_PL = 6;
  LOCALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04025, FND-04026, FND-04027

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04037"></a>
## FND-04037: chesscom.explanation_engine.v1.Locale.LOCALE_ID_ID = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOCALE_ID_ID = 11;

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 360.

```text
OCALE_PL_PL = 6;
  LOCALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04025, FND-04026, FND-04027

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04038"></a>
## FND-04038: chesscom.explanation_engine.v1.Locale.LOCALE_KO_KR = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LOCALE_KO_KR = 12;

### Evidence

- **SRC-0412** `research/proto/chesscom/explanation_engine/v1/language.proto` — [preserved redacted evidence](../evidence/text/6e95590661adfb29621b88536cc809d7e662e7c8835d594c01027cf94a0c5b04.proto)
  Character offset 381.

```text
CALE_PT_PT = 7;
  LOCALE_RU_RU = 8;
  LOCALE_TR_TR = 9;
  LOCALE_AR_SA = 10;
  LOCALE_ID_ID = 11;
  LOCALE_KO_KR = 12;
}

```

**Source references:** SRC-0412, SRC-1383  
**URL references:** None independently associated  
**Related findings:** FND-04025, FND-04026, FND-04027

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04039"></a>
## FND-04039: enum declaration: chesscom.explanation_engine.v1.AnnotationColor

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum AnnotationColor {

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 124.

```text
anation_engine/v1/move_annotation.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum AnnotationColor {
  ANNOTATION_COLOR_UNSPECIFIED = 0;
  ANNOTATION_COLOR_GREEN = 1;
  ANNOTATION_COLOR_RED = 2;
  ANNOTATION_COLOR_YELLOW = 3;
  ANNOTATION_COLOR_BLUE = 4;
}

message AnnotationArrow {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.e
```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04040, FND-04041

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04040"></a>
## FND-04040: chesscom.explanation_engine.v1.AnnotationColor.ANNOTATION_COLOR_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANNOTATION_COLOR_UNSPECIFIED = 0;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 149.

```text
notation.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum AnnotationColor {
  ANNOTATION_COLOR_UNSPECIFIED = 0;
  ANNOTATION_COLOR_GREEN = 1;
  ANNOTATION_COLOR_RED = 2;
  ANNOTATION_COLOR_YELLOW = 3;
  ANNOTATION_COLOR_BLUE = 4;
}

message AnnotationArrow {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.explanation_engine.v1.Anno
```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04041

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04041"></a>
## FND-04041: chesscom.explanation_engine.v1.AnnotationColor.ANNOTATION_COLOR_GREEN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANNOTATION_COLOR_GREEN = 1;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 185.

```text
ckage chesscom.explanation_engine.v1;

enum AnnotationColor {
  ANNOTATION_COLOR_UNSPECIFIED = 0;
  ANNOTATION_COLOR_GREEN = 1;
  ANNOTATION_COLOR_RED = 2;
  ANNOTATION_COLOR_YELLOW = 3;
  ANNOTATION_COLOR_BLUE = 4;
}

message AnnotationArrow {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 3;
}

message An
```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04042"></a>
## FND-04042: chesscom.explanation_engine.v1.AnnotationColor.ANNOTATION_COLOR_RED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANNOTATION_COLOR_RED = 2;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 215.

```text
ine.v1;

enum AnnotationColor {
  ANNOTATION_COLOR_UNSPECIFIED = 0;
  ANNOTATION_COLOR_GREEN = 1;
  ANNOTATION_COLOR_RED = 2;
  ANNOTATION_COLOR_YELLOW = 3;
  ANNOTATION_COLOR_BLUE = 4;
}

message AnnotationArrow {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 3;
}

message AnnotationSquare {
  optional .c
```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04043"></a>
## FND-04043: chesscom.explanation_engine.v1.AnnotationColor.ANNOTATION_COLOR_YELLOW = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANNOTATION_COLOR_YELLOW = 3;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 243.

```text
r {
  ANNOTATION_COLOR_UNSPECIFIED = 0;
  ANNOTATION_COLOR_GREEN = 1;
  ANNOTATION_COLOR_RED = 2;
  ANNOTATION_COLOR_YELLOW = 3;
  ANNOTATION_COLOR_BLUE = 4;
}

message AnnotationArrow {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 3;
}

message AnnotationSquare {
  optional .chesscom.chess.v1.Square squa
```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04044"></a>
## FND-04044: chesscom.explanation_engine.v1.AnnotationColor.ANNOTATION_COLOR_BLUE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANNOTATION_COLOR_BLUE = 4;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 274.

```text
IED = 0;
  ANNOTATION_COLOR_GREEN = 1;
  ANNOTATION_COLOR_RED = 2;
  ANNOTATION_COLOR_YELLOW = 3;
  ANNOTATION_COLOR_BLUE = 4;
}

message AnnotationArrow {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 3;
}

message AnnotationSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.ex
```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04045"></a>
## FND-04045: message declaration: chesscom.explanation_engine.v1.AnnotationArrow

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AnnotationArrow {

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 304.

```text
EEN = 1;
  ANNOTATION_COLOR_RED = 2;
  ANNOTATION_COLOR_YELLOW = 3;
  ANNOTATION_COLOR_BLUE = 4;
}

message AnnotationArrow {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 3;
}

message AnnotationSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.explanation_engine.v1.Annotation
```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04046"></a>
## FND-04046: chesscom.explanation_engine.v1.AnnotationArrow.from = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square from = 1;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 332.

```text
RED = 2;
  ANNOTATION_COLOR_YELLOW = 3;
  ANNOTATION_COLOR_BLUE = 4;
}

message AnnotationArrow {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 3;
}

message AnnotationSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 2;
}

message 
```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04047"></a>
## FND-04047: chesscom.explanation_engine.v1.AnnotationArrow.to = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square to = 2;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 379.

```text
ATION_COLOR_BLUE = 4;
}

message AnnotationArrow {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 3;
}

message AnnotationSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 2;
}

message MoveAnnotation {
  oneof _before_comment {
  st
```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04048"></a>
## FND-04048: chesscom.explanation_engine.v1.AnnotationArrow.color = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.AnnotationColor color = 3;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 424.

```text
row {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 3;
}

message AnnotationSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 2;
}

message MoveAnnotation {
  oneof _before_comment {
  string before_comment = 2;
  }
  repeated strin
```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04049"></a>
## FND-04049: message declaration: chesscom.explanation_engine.v1.AnnotationSquare

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AnnotationSquare {

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 495.

```text
om.chess.v1.Square to = 2;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 3;
}

message AnnotationSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 2;
}

message MoveAnnotation {
  oneof _before_comment {
  string before_comment = 2;
  }
  repeated string comments = 1;
  repeated int32 nags = 3;
  repeated .chesscom.explana
```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04050"></a>
## FND-04050: chesscom.explanation_engine.v1.AnnotationSquare.square = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square square = 1;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 524.

```text
optional .chesscom.explanation_engine.v1.AnnotationColor color = 3;
}

message AnnotationSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 2;
}

message MoveAnnotation {
  oneof _before_comment {
  string before_comment = 2;
  }
  repeated string comments = 1;
  repeated int32 nags = 3;
  repeated .chesscom.explanation_engine.v1.AnnotationArro
```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04051"></a>
## FND-04051: chesscom.explanation_engine.v1.AnnotationSquare.color = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.AnnotationColor color = 2;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 573.

```text
onColor color = 3;
}

message AnnotationSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 2;
}

message MoveAnnotation {
  oneof _before_comment {
  string before_comment = 2;
  }
  repeated string comments = 1;
  repeated int32 nags = 3;
  repeated .chesscom.explanation_engine.v1.AnnotationArrow arrows = 4;
  repeated .chesscom.explanation_en
```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04052"></a>
## FND-04052: message declaration: chesscom.explanation_engine.v1.MoveAnnotation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MoveAnnotation {

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 644.

```text
hess.v1.Square square = 1;
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 2;
}

message MoveAnnotation {
  oneof _before_comment {
  string before_comment = 2;
  }
  repeated string comments = 1;
  repeated int32 nags = 3;
  repeated .chesscom.explanation_engine.v1.AnnotationArrow arrows = 4;
  repeated .chesscom.explanation_engine.v1.AnnotationSquare highlighted_squares = 5;
}

```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04053"></a>
## FND-04053: oneof declaration: chesscom.explanation_engine.v1.MoveAnnotation._before_comment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _before_comment {

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 671.

```text
  optional .chesscom.explanation_engine.v1.AnnotationColor color = 2;
}

message MoveAnnotation {
  oneof _before_comment {
  string before_comment = 2;
  }
  repeated string comments = 1;
  repeated int32 nags = 3;
  repeated .chesscom.explanation_engine.v1.AnnotationArrow arrows = 4;
  repeated .chesscom.explanation_engine.v1.AnnotationSquare highlighted_squares = 5;
}

```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04054"></a>
## FND-04054: chesscom.explanation_engine.v1.MoveAnnotation.before_comment = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string before_comment = 2;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 697.

```text
nation_engine.v1.AnnotationColor color = 2;
}

message MoveAnnotation {
  oneof _before_comment {
  string before_comment = 2;
  }
  repeated string comments = 1;
  repeated int32 nags = 3;
  repeated .chesscom.explanation_engine.v1.AnnotationArrow arrows = 4;
  repeated .chesscom.explanation_engine.v1.AnnotationSquare highlighted_squares = 5;
}

```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04055"></a>
## FND-04055: chesscom.explanation_engine.v1.MoveAnnotation.comments = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string comments = 1;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 730.

```text
color = 2;
}

message MoveAnnotation {
  oneof _before_comment {
  string before_comment = 2;
  }
  repeated string comments = 1;
  repeated int32 nags = 3;
  repeated .chesscom.explanation_engine.v1.AnnotationArrow arrows = 4;
  repeated .chesscom.explanation_engine.v1.AnnotationSquare highlighted_squares = 5;
}

```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04056"></a>
## FND-04056: chesscom.explanation_engine.v1.MoveAnnotation.nags = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated int32 nags = 3;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 762.

```text
tion {
  oneof _before_comment {
  string before_comment = 2;
  }
  repeated string comments = 1;
  repeated int32 nags = 3;
  repeated .chesscom.explanation_engine.v1.AnnotationArrow arrows = 4;
  repeated .chesscom.explanation_engine.v1.AnnotationSquare highlighted_squares = 5;
}

```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04057"></a>
## FND-04057: chesscom.explanation_engine.v1.MoveAnnotation.arrows = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.AnnotationArrow arrows = 4;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 789.

```text
ent {
  string before_comment = 2;
  }
  repeated string comments = 1;
  repeated int32 nags = 3;
  repeated .chesscom.explanation_engine.v1.AnnotationArrow arrows = 4;
  repeated .chesscom.explanation_engine.v1.AnnotationSquare highlighted_squares = 5;
}

```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04058"></a>
## FND-04058: chesscom.explanation_engine.v1.MoveAnnotation.highlighted_squares = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.AnnotationSquare highlighted_squares = 5;

### Evidence

- **SRC-0413** `research/proto/chesscom/explanation_engine/v1/move_annotation.proto` — [preserved redacted evidence](../evidence/text/47ff53837e620a5009e02f9efe35920a7877b716d9f0934f9a53d41d7b999d38.proto)
  Character offset 860.

```text
  repeated int32 nags = 3;
  repeated .chesscom.explanation_engine.v1.AnnotationArrow arrows = 4;
  repeated .chesscom.explanation_engine.v1.AnnotationSquare highlighted_squares = 5;
}

```

**Source references:** SRC-0413, SRC-1384  
**URL references:** None independently associated  
**Related findings:** FND-04039, FND-04040, FND-04041

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04059"></a>
## FND-04059: enum declaration: chesscom.explanation_engine.v1.MoveClassification

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MoveClassification {

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 128.

```text
ion_engine/v1/move_classification.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum MoveClassification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_BOOK = 1;
  MOVE_CLASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CL
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04060"></a>
## FND-04060: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_UNSPECIFIED = 0;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 156.

```text
ation.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum MoveClassification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_BOOK = 1;
  MOVE_CLASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04061"></a>
## FND-04061: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_BOOK = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_BOOK = 1;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 195.

```text
chesscom.explanation_engine.v1;

enum MoveClassification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_BOOK = 1;
  MOVE_CLASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04062"></a>
## FND-04062: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_BRILLIANT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_BRILLIANT = 2;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 227.

```text

enum MoveClassification {
  MOVE_CLASSIFICATION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_BOOK = 1;
  MOVE_CLASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED = 10;
  M
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04063"></a>
## FND-04063: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_GREAT_FIND = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_GREAT_FIND = 3;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 264.

```text
SSIFICATION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_BOOK = 1;
  MOVE_CLASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOV
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04064"></a>
## FND-04064: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_BEST = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_BEST = 4;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 302.

```text
ASSIFICATION_BOOK = 1;
  MOVE_CLASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_TRICKY = 20;
}

enum 
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04065"></a>
## FND-04065: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_EXCELLENT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_EXCELLENT = 5;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 334.

```text
ASSIFICATION_BRILLIANT = 2;
  MOVE_CLASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_TRICKY = 20;
}

enum MoveClassificationVersion {
  MO
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04066"></a>
## FND-04066: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_GOOD = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_GOOD = 6;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 371.

```text
ASSIFICATION_GREAT_FIND = 3;
  MOVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_TRICKY = 20;
}

enum MoveClassificationVersion {
  MOVE_CLASSIFICATION_VERSION_UNSPECIFIED
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04067"></a>
## FND-04067: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_INACCURACY = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_INACCURACY = 7;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 403.

```text
OVE_CLASSIFICATION_BEST = 4;
  MOVE_CLASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_TRICKY = 20;
}

enum MoveClassificationVersion {
  MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_VERS
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04068"></a>
## FND-04068: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_MISTAKE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_MISTAKE = 8;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 441.

```text
ASSIFICATION_EXCELLENT = 5;
  MOVE_CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_TRICKY = 20;
}

enum MoveClassificationVersion {
  MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_VERSION_V2 = 1;
  MOVE_CLASSIFICATION_VERS
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04069"></a>
## FND-04069: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_BLUNDER = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_BLUNDER = 9;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 476.

```text
CLASSIFICATION_GOOD = 6;
  MOVE_CLASSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_TRICKY = 20;
}

enum MoveClassificationVersion {
  MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_VERSION_V2 = 1;
  MOVE_CLASSIFICATION_VERSION_V3 = 2;
}

message EvalClassifi
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04070"></a>
## FND-04070: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_MISSED = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_MISSED = 10;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 511.

```text
SSIFICATION_INACCURACY = 7;
  MOVE_CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_TRICKY = 20;
}

enum MoveClassificationVersion {
  MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_VERSION_V2 = 1;
  MOVE_CLASSIFICATION_VERSION_V3 = 2;
}

message EvalClassification {
  optional .chesscom.expla
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04071"></a>
## FND-04071: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_FORCED = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_FORCED = 11;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 546.

```text
CLASSIFICATION_MISTAKE = 8;
  MOVE_CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_TRICKY = 20;
}

enum MoveClassificationVersion {
  MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_VERSION_V2 = 1;
  MOVE_CLASSIFICATION_VERSION_V3 = 2;
}

message EvalClassification {
  optional .chesscom.explanation_engine.v1.MoveClassification
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04072"></a>
## FND-04072: chesscom.explanation_engine.v1.MoveClassification.MOVE_CLASSIFICATION_TRICKY = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_TRICKY = 20;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 581.

```text
CLASSIFICATION_BLUNDER = 9;
  MOVE_CLASSIFICATION_MISSED = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_TRICKY = 20;
}

enum MoveClassificationVersion {
  MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_VERSION_V2 = 1;
  MOVE_CLASSIFICATION_VERSION_V3 = 2;
}

message EvalClassification {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optiona
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04073"></a>
## FND-04073: enum declaration: chesscom.explanation_engine.v1.MoveClassificationVersion

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MoveClassificationVersion {

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 617.

```text
LASSIFICATION_MISSED = 10;
  MOVE_CLASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_TRICKY = 20;
}

enum MoveClassificationVersion {
  MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0;
  MOVE_CLASSIFICATION_VERSION_V2 = 1;
  MOVE_CLASSIFICATION_VERSION_V3 = 2;
}

message EvalClassification {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional .chesscom.engine.v1.Evaluation eva
```

**Source references:** SRC-0414, SRC-1385  
**URL references:** None independently associated  
**Related findings:** FND-04059, FND-04060, FND-04061

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04074"></a>
## FND-04074: chesscom.explanation_engine.v1.MoveClassificationVersion.MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_CLASSIFICATION_VERSION_UNSPECIFIED = 0;

### Evidence

- **SRC-0414** `research/proto/chesscom/explanation_engine/v1/move_classification.proto` — [preserved redacted evidence](../evidence/text/db349c9153d69920da69029d7ec236609f6eac4c026b89a24af386de80432348.proto)
  Character offset 652.

```text
LASSIFICATION_FORCED = 11;
  MOVE_CLASSIFICATION_TRICKY = 20;
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
