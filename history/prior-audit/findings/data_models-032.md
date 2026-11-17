# data_models — findings 3101–3200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-03375"></a>
## FND-03375: chesscom.explanation_engine.v1.GetNonChessTextResponse.speech = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech speech = 1;

### Evidence

- **SRC-0376** `research/proto/chesscom/explanation_engine/v1/feature_get_non_chess_text.proto` — [preserved redacted evidence](../evidence/text/3ad4537c412cfce227f138beb38b45dd56ac328a0e4ded762d94a730deb42c8b.proto)
  Character offset 512.

```text
l .chesscom.explanation_engine.v1.NonChessTextType type = 1;
}

message GetNonChessTextResponse {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

```

**Source references:** SRC-0376, SRC-1347  
**URL references:** None independently associated  
**Related findings:** FND-03366, FND-03367, FND-03368

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03376"></a>
## FND-03376: message declaration: chesscom.explanation_engine.v1.GetOpeningRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetOpeningRequest {

### Evidence

- **SRC-0377** `research/proto/chesscom/explanation_engine/v1/feature_get_opening.proto` — [preserved redacted evidence](../evidence/text/7c61ee89af50402288f467ff35e239d1c5461d26946d2dde5b73b9b8aa9fdb43.proto)
  Character offset 128.

```text
ion_engine/v1/feature_get_opening.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetOpeningRequest {
  oneof _locale {
  .chesscom.explanation_engine.v1.Locale locale = 1;
  }
}

message GetOpeningResponse {
  oneof _opening {
  .chesscom.explanation_engine.v1.Opening opening = 1;
  }
}

```

**Source references:** SRC-0377, SRC-1348  
**URL references:** None independently associated  
**Related findings:** FND-03377, FND-03378

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03377"></a>
## FND-03377: oneof declaration: chesscom.explanation_engine.v1.GetOpeningRequest._locale

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _locale {

### Evidence

- **SRC-0377** `research/proto/chesscom/explanation_engine/v1/feature_get_opening.proto` — [preserved redacted evidence](../evidence/text/7c61ee89af50402288f467ff35e239d1c5461d26946d2dde5b73b9b8aa9fdb43.proto)
  Character offset 158.

```text
ing.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetOpeningRequest {
  oneof _locale {
  .chesscom.explanation_engine.v1.Locale locale = 1;
  }
}

message GetOpeningResponse {
  oneof _opening {
  .chesscom.explanation_engine.v1.Opening opening = 1;
  }
}

```

**Source references:** SRC-0377, SRC-1348  
**URL references:** None independently associated  
**Related findings:** FND-03376, FND-03378

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03378"></a>
## FND-03378: chesscom.explanation_engine.v1.GetOpeningRequest.locale = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.Locale locale = 1;

### Evidence

- **SRC-0377** `research/proto/chesscom/explanation_engine/v1/feature_get_opening.proto` — [preserved redacted evidence](../evidence/text/7c61ee89af50402288f467ff35e239d1c5461d26946d2dde5b73b9b8aa9fdb43.proto)
  Character offset 176.

```text
x: proto3

package chesscom.explanation_engine.v1;

message GetOpeningRequest {
  oneof _locale {
  .chesscom.explanation_engine.v1.Locale locale = 1;
  }
}

message GetOpeningResponse {
  oneof _opening {
  .chesscom.explanation_engine.v1.Opening opening = 1;
  }
}

```

**Source references:** SRC-0377, SRC-1348  
**URL references:** None independently associated  
**Related findings:** FND-03376, FND-03377

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03379"></a>
## FND-03379: message declaration: chesscom.explanation_engine.v1.GetOpeningResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetOpeningResponse {

### Evidence

- **SRC-0377** `research/proto/chesscom/explanation_engine/v1/feature_get_opening.proto` — [preserved redacted evidence](../evidence/text/7c61ee89af50402288f467ff35e239d1c5461d26946d2dde5b73b9b8aa9fdb43.proto)
  Character offset 234.

```text
e GetOpeningRequest {
  oneof _locale {
  .chesscom.explanation_engine.v1.Locale locale = 1;
  }
}

message GetOpeningResponse {
  oneof _opening {
  .chesscom.explanation_engine.v1.Opening opening = 1;
  }
}

```

**Source references:** SRC-0377, SRC-1348  
**URL references:** None independently associated  
**Related findings:** FND-03376, FND-03377, FND-03378

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03380"></a>
## FND-03380: oneof declaration: chesscom.explanation_engine.v1.GetOpeningResponse._opening

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening {

### Evidence

- **SRC-0377** `research/proto/chesscom/explanation_engine/v1/feature_get_opening.proto` — [preserved redacted evidence](../evidence/text/7c61ee89af50402288f467ff35e239d1c5461d26946d2dde5b73b9b8aa9fdb43.proto)
  Character offset 265.

```text
locale {
  .chesscom.explanation_engine.v1.Locale locale = 1;
  }
}

message GetOpeningResponse {
  oneof _opening {
  .chesscom.explanation_engine.v1.Opening opening = 1;
  }
}

```

**Source references:** SRC-0377, SRC-1348  
**URL references:** None independently associated  
**Related findings:** FND-03376, FND-03377, FND-03378

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03381"></a>
## FND-03381: chesscom.explanation_engine.v1.GetOpeningResponse.opening = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.Opening opening = 1;

### Evidence

- **SRC-0377** `research/proto/chesscom/explanation_engine/v1/feature_get_opening.proto` — [preserved redacted evidence](../evidence/text/7c61ee89af50402288f467ff35e239d1c5461d26946d2dde5b73b9b8aa9fdb43.proto)
  Character offset 284.

```text
m.explanation_engine.v1.Locale locale = 1;
  }
}

message GetOpeningResponse {
  oneof _opening {
  .chesscom.explanation_engine.v1.Opening opening = 1;
  }
}

```

**Source references:** SRC-0377, SRC-1348  
**URL references:** None independently associated  
**Related findings:** FND-03376, FND-03377, FND-03378

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03382"></a>
## FND-03382: enum declaration: chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PgnAnnotationSerializationFormat {

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 124.

```text
anation_engine/v1/feature_get_pgn.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum PgnAnnotationSerializationFormat {
  PGN_ANNOTATION_SERIALIZATION_FORMAT_UNSPECIFIED = 0;
  PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_BASE = 1;
  PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_COM = 2;
}

message GetPgnRequest {
  oneof game_to_convert {
  .chesscom.chess.v1.Game game = 1;
  .chesscom.explanation_engin
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03383, FND-03384

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03383"></a>
## FND-03383: chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat.PGN_ANNOTATION_SERIALIZATION_FORMAT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PGN_ANNOTATION_SERIALIZATION_FORMAT_UNSPECIFIED = 0;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 166.

```text
 syntax: proto3

package chesscom.explanation_engine.v1;

enum PgnAnnotationSerializationFormat {
  PGN_ANNOTATION_SERIALIZATION_FORMAT_UNSPECIFIED = 0;
  PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_BASE = 1;
  PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_COM = 2;
}

message GetPgnRequest {
  oneof game_to_convert {
  .chesscom.chess.v1.Game game = 1;
  .chesscom.explanation_engine.v1.GameState game_state = 2;
  int32 sta
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03384

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03384"></a>
## FND-03384: chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat.PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_BASE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_BASE = 1;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 221.

```text
;

enum PgnAnnotationSerializationFormat {
  PGN_ANNOTATION_SERIALIZATION_FORMAT_UNSPECIFIED = 0;
  PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_BASE = 1;
  PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_COM = 2;
}

message GetPgnRequest {
  oneof game_to_convert {
  .chesscom.chess.v1.Game game = 1;
  .chesscom.explanation_engine.v1.GameState game_state = 2;
  int32 starting_game_point = 3;
  }
  oneof _pgn_fen_header_notat
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03385"></a>
## FND-03385: chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat.PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_COM = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_COM = 2;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 275.

```text
ATION_SERIALIZATION_FORMAT_UNSPECIFIED = 0;
  PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_BASE = 1;
  PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_COM = 2;
}

message GetPgnRequest {
  oneof game_to_convert {
  .chesscom.chess.v1.Game game = 1;
  .chesscom.explanation_engine.v1.GameState game_state = 2;
  int32 starting_game_point = 3;
  }
  oneof _pgn_fen_header_notation {
  .chesscom.explanation_engine.v1.FenNotation pg
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03386"></a>
## FND-03386: message declaration: chesscom.explanation_engine.v1.GetPgnRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetPgnRequest {

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 329.

```text
TATION_SERIALIZATION_FORMAT_CHESS_BASE = 1;
  PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_COM = 2;
}

message GetPgnRequest {
  oneof game_to_convert {
  .chesscom.chess.v1.Game game = 1;
  .chesscom.explanation_engine.v1.GameState game_state = 2;
  int32 starting_game_point = 3;
  }
  oneof _pgn_fen_header_notation {
  .chesscom.explanation_engine.v1.FenNotation pgn_fen_header_notation = 4;
  }
  oneof _main_line_only
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03387"></a>
## FND-03387: oneof declaration: chesscom.explanation_engine.v1.GetPgnRequest.game_to_convert

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof game_to_convert {

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 355.

```text
T_CHESS_BASE = 1;
  PGN_ANNOTATION_SERIALIZATION_FORMAT_CHESS_COM = 2;
}

message GetPgnRequest {
  oneof game_to_convert {
  .chesscom.chess.v1.Game game = 1;
  .chesscom.explanation_engine.v1.GameState game_state = 2;
  int32 starting_game_point = 3;
  }
  oneof _pgn_fen_header_notation {
  .chesscom.explanation_engine.v1.FenNotation pgn_fen_header_notation = 4;
  }
  oneof _main_line_only {
  bool main_line_only =
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03388"></a>
## FND-03388: chesscom.explanation_engine.v1.GetPgnRequest.game = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Game game = 1;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 381.

```text
NOTATION_SERIALIZATION_FORMAT_CHESS_COM = 2;
}

message GetPgnRequest {
  oneof game_to_convert {
  .chesscom.chess.v1.Game game = 1;
  .chesscom.explanation_engine.v1.GameState game_state = 2;
  int32 starting_game_point = 3;
  }
  oneof _pgn_fen_header_notation {
  .chesscom.explanation_engine.v1.FenNotation pgn_fen_header_notation = 4;
  }
  oneof _main_line_only {
  bool main_line_only = 5;
  }
  oneof _user_vari
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03389"></a>
## FND-03389: chesscom.explanation_engine.v1.GetPgnRequest.game_state = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.GameState game_state = 2;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 417.

```text
COM = 2;
}

message GetPgnRequest {
  oneof game_to_convert {
  .chesscom.chess.v1.Game game = 1;
  .chesscom.explanation_engine.v1.GameState game_state = 2;
  int32 starting_game_point = 3;
  }
  oneof _pgn_fen_header_notation {
  .chesscom.explanation_engine.v1.FenNotation pgn_fen_header_notation = 4;
  }
  oneof _main_line_only {
  bool main_line_only = 5;
  }
  oneof _user_variations_only {
  bool user_variations
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03390"></a>
## FND-03390: chesscom.explanation_engine.v1.GetPgnRequest.starting_game_point = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 starting_game_point = 3;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 477.

```text
{
  .chesscom.chess.v1.Game game = 1;
  .chesscom.explanation_engine.v1.GameState game_state = 2;
  int32 starting_game_point = 3;
  }
  oneof _pgn_fen_header_notation {
  .chesscom.explanation_engine.v1.FenNotation pgn_fen_header_notation = 4;
  }
  oneof _main_line_only {
  bool main_line_only = 5;
  }
  oneof _user_variations_only {
  bool user_variations_only = 6;
  }
  oneof _include_threats {
  bool include_thr
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03391"></a>
## FND-03391: oneof declaration: chesscom.explanation_engine.v1.GetPgnRequest._pgn_fen_header_notation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pgn_fen_header_notation {

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 514.

```text

  .chesscom.explanation_engine.v1.GameState game_state = 2;
  int32 starting_game_point = 3;
  }
  oneof _pgn_fen_header_notation {
  .chesscom.explanation_engine.v1.FenNotation pgn_fen_header_notation = 4;
  }
  oneof _main_line_only {
  bool main_line_only = 5;
  }
  oneof _user_variations_only {
  bool user_variations_only = 6;
  }
  oneof _include_threats {
  bool include_threats = 8;
  }
  oneof _include_all_sc
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03392"></a>
## FND-03392: chesscom.explanation_engine.v1.GetPgnRequest.pgn_fen_header_notation = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.FenNotation pgn_fen_header_notation = 4;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 549.

```text
GameState game_state = 2;
  int32 starting_game_point = 3;
  }
  oneof _pgn_fen_header_notation {
  .chesscom.explanation_engine.v1.FenNotation pgn_fen_header_notation = 4;
  }
  oneof _main_line_only {
  bool main_line_only = 5;
  }
  oneof _user_variations_only {
  bool user_variations_only = 6;
  }
  oneof _include_threats {
  bool include_threats = 8;
  }
  oneof _include_all_scored_gamepoints {
  bool include_al
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03393"></a>
## FND-03393: oneof declaration: chesscom.explanation_engine.v1.GetPgnRequest._main_line_only

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _main_line_only {

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 628.

```text
_header_notation {
  .chesscom.explanation_engine.v1.FenNotation pgn_fen_header_notation = 4;
  }
  oneof _main_line_only {
  bool main_line_only = 5;
  }
  oneof _user_variations_only {
  bool user_variations_only = 6;
  }
  oneof _include_threats {
  bool include_threats = 8;
  }
  oneof _include_all_scored_gamepoints {
  bool include_all_scored_gamepoints = 9;
  }
  oneof _unscored_gamepoint_limit {
  int32 unscor
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03394"></a>
## FND-03394: chesscom.explanation_engine.v1.GetPgnRequest.main_line_only = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool main_line_only = 5;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 654.

```text
scom.explanation_engine.v1.FenNotation pgn_fen_header_notation = 4;
  }
  oneof _main_line_only {
  bool main_line_only = 5;
  }
  oneof _user_variations_only {
  bool user_variations_only = 6;
  }
  oneof _include_threats {
  bool include_threats = 8;
  }
  oneof _include_all_scored_gamepoints {
  bool include_all_scored_gamepoints = 9;
  }
  oneof _unscored_gamepoint_limit {
  int32 unscored_gamepoint_limit = 10;
 
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03395"></a>
## FND-03395: oneof declaration: chesscom.explanation_engine.v1.GetPgnRequest._user_variations_only

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_variations_only {

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 685.

```text
otation pgn_fen_header_notation = 4;
  }
  oneof _main_line_only {
  bool main_line_only = 5;
  }
  oneof _user_variations_only {
  bool user_variations_only = 6;
  }
  oneof _include_threats {
  bool include_threats = 8;
  }
  oneof _include_all_scored_gamepoints {
  bool include_all_scored_gamepoints = 9;
  }
  oneof _unscored_gamepoint_limit {
  int32 unscored_gamepoint_limit = 10;
  }
  oneof _annotation_serializ
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03396"></a>
## FND-03396: chesscom.explanation_engine.v1.GetPgnRequest.user_variations_only = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool user_variations_only = 6;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 717.

```text
= 4;
  }
  oneof _main_line_only {
  bool main_line_only = 5;
  }
  oneof _user_variations_only {
  bool user_variations_only = 6;
  }
  oneof _include_threats {
  bool include_threats = 8;
  }
  oneof _include_all_scored_gamepoints {
  bool include_all_scored_gamepoints = 9;
  }
  oneof _unscored_gamepoint_limit {
  int32 unscored_gamepoint_limit = 10;
  }
  oneof _annotation_serialization_format {
  .chesscom.expla
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03397"></a>
## FND-03397: oneof declaration: chesscom.explanation_engine.v1.GetPgnRequest._include_threats

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _include_threats {

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 754.

```text
bool main_line_only = 5;
  }
  oneof _user_variations_only {
  bool user_variations_only = 6;
  }
  oneof _include_threats {
  bool include_threats = 8;
  }
  oneof _include_all_scored_gamepoints {
  bool include_all_scored_gamepoints = 9;
  }
  oneof _unscored_gamepoint_limit {
  int32 unscored_gamepoint_limit = 10;
  }
  oneof _annotation_serialization_format {
  .chesscom.explanation_engine.v1.PgnAnnotationSeriali
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03398"></a>
## FND-03398: chesscom.explanation_engine.v1.GetPgnRequest.include_threats = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool include_threats = 8;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 781.

```text
}
  oneof _user_variations_only {
  bool user_variations_only = 6;
  }
  oneof _include_threats {
  bool include_threats = 8;
  }
  oneof _include_all_scored_gamepoints {
  bool include_all_scored_gamepoints = 9;
  }
  oneof _unscored_gamepoint_limit {
  int32 unscored_gamepoint_limit = 10;
  }
  oneof _annotation_serialization_format {
  .chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat annotation_ser
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03399"></a>
## FND-03399: oneof declaration: chesscom.explanation_engine.v1.GetPgnRequest._include_all_scored_gamepoints

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _include_all_scored_gamepoints {

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 813.

```text
{
  bool user_variations_only = 6;
  }
  oneof _include_threats {
  bool include_threats = 8;
  }
  oneof _include_all_scored_gamepoints {
  bool include_all_scored_gamepoints = 9;
  }
  oneof _unscored_gamepoint_limit {
  int32 unscored_gamepoint_limit = 10;
  }
  oneof _annotation_serialization_format {
  .chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat annotation_serialization_format = 12;
  }
  re
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03400"></a>
## FND-03400: chesscom.explanation_engine.v1.GetPgnRequest.include_all_scored_gamepoints = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool include_all_scored_gamepoints = 9;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 854.

```text
oneof _include_threats {
  bool include_threats = 8;
  }
  oneof _include_all_scored_gamepoints {
  bool include_all_scored_gamepoints = 9;
  }
  oneof _unscored_gamepoint_limit {
  int32 unscored_gamepoint_limit = 10;
  }
  oneof _annotation_serialization_format {
  .chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat annotation_serialization_format = 12;
  }
  repeated int32 included_game_points = 7;
  
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03401"></a>
## FND-03401: oneof declaration: chesscom.explanation_engine.v1.GetPgnRequest._unscored_gamepoint_limit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _unscored_gamepoint_limit {

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 900.

```text
s = 8;
  }
  oneof _include_all_scored_gamepoints {
  bool include_all_scored_gamepoints = 9;
  }
  oneof _unscored_gamepoint_limit {
  int32 unscored_gamepoint_limit = 10;
  }
  oneof _annotation_serialization_format {
  .chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat annotation_serialization_format = 12;
  }
  repeated int32 included_game_points = 7;
  repeated int32 explicit_included_game_points =
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03402"></a>
## FND-03402: chesscom.explanation_engine.v1.GetPgnRequest.unscored_gamepoint_limit = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 unscored_gamepoint_limit = 10;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 936.

```text
ed_gamepoints {
  bool include_all_scored_gamepoints = 9;
  }
  oneof _unscored_gamepoint_limit {
  int32 unscored_gamepoint_limit = 10;
  }
  oneof _annotation_serialization_format {
  .chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat annotation_serialization_format = 12;
  }
  repeated int32 included_game_points = 7;
  repeated int32 explicit_included_game_points = 11;
}

message GetPgnResponse {
  o
```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03403"></a>
## FND-03403: oneof declaration: chesscom.explanation_engine.v1.GetPgnRequest._annotation_serialization_format

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _annotation_serialization_format {

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 979.

```text
amepoints = 9;
  }
  oneof _unscored_gamepoint_limit {
  int32 unscored_gamepoint_limit = 10;
  }
  oneof _annotation_serialization_format {
  .chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat annotation_serialization_format = 12;
  }
  repeated int32 included_game_points = 7;
  repeated int32 explicit_included_game_points = 11;
}

message GetPgnResponse {
  optional string pgn = 1;
}

```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03404"></a>
## FND-03404: chesscom.explanation_engine.v1.GetPgnRequest.annotation_serialization_format = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat annotation_serialization_format = 12;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 1022.

```text
int_limit {
  int32 unscored_gamepoint_limit = 10;
  }
  oneof _annotation_serialization_format {
  .chesscom.explanation_engine.v1.PgnAnnotationSerializationFormat annotation_serialization_format = 12;
  }
  repeated int32 included_game_points = 7;
  repeated int32 explicit_included_game_points = 11;
}

message GetPgnResponse {
  optional string pgn = 1;
}

```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03405"></a>
## FND-03405: chesscom.explanation_engine.v1.GetPgnRequest.included_game_points = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated int32 included_game_points = 7;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 1131.

```text
.explanation_engine.v1.PgnAnnotationSerializationFormat annotation_serialization_format = 12;
  }
  repeated int32 included_game_points = 7;
  repeated int32 explicit_included_game_points = 11;
}

message GetPgnResponse {
  optional string pgn = 1;
}

```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03406"></a>
## FND-03406: chesscom.explanation_engine.v1.GetPgnRequest.explicit_included_game_points = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated int32 explicit_included_game_points = 11;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 1174.

```text
zationFormat annotation_serialization_format = 12;
  }
  repeated int32 included_game_points = 7;
  repeated int32 explicit_included_game_points = 11;
}

message GetPgnResponse {
  optional string pgn = 1;
}

```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03407"></a>
## FND-03407: message declaration: chesscom.explanation_engine.v1.GetPgnResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetPgnResponse {

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 1228.

```text

  repeated int32 included_game_points = 7;
  repeated int32 explicit_included_game_points = 11;
}

message GetPgnResponse {
  optional string pgn = 1;
}

```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03408"></a>
## FND-03408: chesscom.explanation_engine.v1.GetPgnResponse.pgn = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string pgn = 1;

### Evidence

- **SRC-0378** `research/proto/chesscom/explanation_engine/v1/feature_get_pgn.proto` — [preserved redacted evidence](../evidence/text/a6b3457f30f78d5c42e6cbf3015dfe39941d66d44a0d969baca72b463a903589.proto)
  Character offset 1255.

```text
game_points = 7;
  repeated int32 explicit_included_game_points = 11;
}

message GetPgnResponse {
  optional string pgn = 1;
}

```

**Source references:** SRC-0378, SRC-1349  
**URL references:** None independently associated  
**Related findings:** FND-03382, FND-03383, FND-03384

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03409"></a>
## FND-03409: message declaration: chesscom.explanation_engine.v1.GetPunishMoveRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetPunishMoveRequest {

### Evidence

- **SRC-0379** `research/proto/chesscom/explanation_engine/v1/feature_get_punish_move.proto` — [preserved redacted evidence](../evidence/text/e2d69a11ce47ddaba33148a58c09ce59a3b88341454424b24cb57ab97ef0686e.proto)
  Character offset 132.

```text
engine/v1/feature_get_punish_move.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetPunishMoveRequest {
}

message GetPunishMoveResponse {
  optional .chesscom.explanation_engine.v1.PunishMove punish_move = 1;
}

```

**Source references:** SRC-0379, SRC-1350  
**URL references:** None independently associated  
**Related findings:** FND-03410, FND-03411

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03410"></a>
## FND-03410: message declaration: chesscom.explanation_engine.v1.GetPunishMoveResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetPunishMoveResponse {

### Evidence

- **SRC-0379** `research/proto/chesscom/explanation_engine/v1/feature_get_punish_move.proto` — [preserved redacted evidence](../evidence/text/e2d69a11ce47ddaba33148a58c09ce59a3b88341454424b24cb57ab97ef0686e.proto)
  Character offset 166.

```text
proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetPunishMoveRequest {
}

message GetPunishMoveResponse {
  optional .chesscom.explanation_engine.v1.PunishMove punish_move = 1;
}

```

**Source references:** SRC-0379, SRC-1350  
**URL references:** None independently associated  
**Related findings:** FND-03409, FND-03411

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03411"></a>
## FND-03411: chesscom.explanation_engine.v1.GetPunishMoveResponse.punish_move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.PunishMove punish_move = 1;

### Evidence

- **SRC-0379** `research/proto/chesscom/explanation_engine/v1/feature_get_punish_move.proto` — [preserved redacted evidence](../evidence/text/e2d69a11ce47ddaba33148a58c09ce59a3b88341454424b24cb57ab97ef0686e.proto)
  Character offset 200.

```text
hesscom.explanation_engine.v1;

message GetPunishMoveRequest {
}

message GetPunishMoveResponse {
  optional .chesscom.explanation_engine.v1.PunishMove punish_move = 1;
}

```

**Source references:** SRC-0379, SRC-1350  
**URL references:** None independently associated  
**Related findings:** FND-03409, FND-03410

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03412"></a>
## FND-03412: message declaration: chesscom.explanation_engine.v1.GetSanMovesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSanMovesRequest {

### Evidence

- **SRC-0380** `research/proto/chesscom/explanation_engine/v1/feature_get_san_moves.proto` — [preserved redacted evidence](../evidence/text/d36c253d6d8fd7da48b7b04016d23751543e65009be12f572a6146dc4f0d4590.proto)
  Character offset 130.

```text
n_engine/v1/feature_get_san_moves.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetSanMovesRequest {
  oneof variation {
  .chesscom.explanation_engine.v1.MoveList proto_moves = 2;
  .chesscom.explanation_engine.v1.UciMoveList uci_moves = 3;
  }
  oneof _fen {
  string fen = 1;
  }
}

message GetSanMovesResponse {
  repeated string san_moves = 1;
}

```

**Source references:** SRC-0380, SRC-1351  
**URL references:** None independently associated  
**Related findings:** FND-03413, FND-03414

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03413"></a>
## FND-03413: oneof declaration: chesscom.explanation_engine.v1.GetSanMovesRequest.variation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof variation {

### Evidence

- **SRC-0380** `research/proto/chesscom/explanation_engine/v1/feature_get_san_moves.proto` — [preserved redacted evidence](../evidence/text/d36c253d6d8fd7da48b7b04016d23751543e65009be12f572a6146dc4f0d4590.proto)
  Character offset 161.

```text
es.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetSanMovesRequest {
  oneof variation {
  .chesscom.explanation_engine.v1.MoveList proto_moves = 2;
  .chesscom.explanation_engine.v1.UciMoveList uci_moves = 3;
  }
  oneof _fen {
  string fen = 1;
  }
}

message GetSanMovesResponse {
  repeated string san_moves = 1;
}

```

**Source references:** SRC-0380, SRC-1351  
**URL references:** None independently associated  
**Related findings:** FND-03412, FND-03414

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03414"></a>
## FND-03414: chesscom.explanation_engine.v1.GetSanMovesRequest.proto_moves = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.MoveList proto_moves = 2;

### Evidence

- **SRC-0380** `research/proto/chesscom/explanation_engine/v1/feature_get_san_moves.proto` — [preserved redacted evidence](../evidence/text/d36c253d6d8fd7da48b7b04016d23751543e65009be12f572a6146dc4f0d4590.proto)
  Character offset 181.

```text
proto3

package chesscom.explanation_engine.v1;

message GetSanMovesRequest {
  oneof variation {
  .chesscom.explanation_engine.v1.MoveList proto_moves = 2;
  .chesscom.explanation_engine.v1.UciMoveList uci_moves = 3;
  }
  oneof _fen {
  string fen = 1;
  }
}

message GetSanMovesResponse {
  repeated string san_moves = 1;
}

```

**Source references:** SRC-0380, SRC-1351  
**URL references:** None independently associated  
**Related findings:** FND-03412, FND-03413

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03415"></a>
## FND-03415: chesscom.explanation_engine.v1.GetSanMovesRequest.uci_moves = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.UciMoveList uci_moves = 3;

### Evidence

- **SRC-0380** `research/proto/chesscom/explanation_engine/v1/feature_get_san_moves.proto` — [preserved redacted evidence](../evidence/text/d36c253d6d8fd7da48b7b04016d23751543e65009be12f572a6146dc4f0d4590.proto)
  Character offset 241.

```text
SanMovesRequest {
  oneof variation {
  .chesscom.explanation_engine.v1.MoveList proto_moves = 2;
  .chesscom.explanation_engine.v1.UciMoveList uci_moves = 3;
  }
  oneof _fen {
  string fen = 1;
  }
}

message GetSanMovesResponse {
  repeated string san_moves = 1;
}

```

**Source references:** SRC-0380, SRC-1351  
**URL references:** None independently associated  
**Related findings:** FND-03412, FND-03413, FND-03414

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03416"></a>
## FND-03416: oneof declaration: chesscom.explanation_engine.v1.GetSanMovesRequest._fen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fen {

### Evidence

- **SRC-0380** `research/proto/chesscom/explanation_engine/v1/feature_get_san_moves.proto` — [preserved redacted evidence](../evidence/text/d36c253d6d8fd7da48b7b04016d23751543e65009be12f572a6146dc4f0d4590.proto)
  Character offset 306.

```text
ine.v1.MoveList proto_moves = 2;
  .chesscom.explanation_engine.v1.UciMoveList uci_moves = 3;
  }
  oneof _fen {
  string fen = 1;
  }
}

message GetSanMovesResponse {
  repeated string san_moves = 1;
}

```

**Source references:** SRC-0380, SRC-1351  
**URL references:** None independently associated  
**Related findings:** FND-03412, FND-03413, FND-03414

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03417"></a>
## FND-03417: chesscom.explanation_engine.v1.GetSanMovesRequest.fen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string fen = 1;

### Evidence

- **SRC-0380** `research/proto/chesscom/explanation_engine/v1/feature_get_san_moves.proto` — [preserved redacted evidence](../evidence/text/d36c253d6d8fd7da48b7b04016d23751543e65009be12f572a6146dc4f0d4590.proto)
  Character offset 321.

```text
 proto_moves = 2;
  .chesscom.explanation_engine.v1.UciMoveList uci_moves = 3;
  }
  oneof _fen {
  string fen = 1;
  }
}

message GetSanMovesResponse {
  repeated string san_moves = 1;
}

```

**Source references:** SRC-0380, SRC-1351  
**URL references:** None independently associated  
**Related findings:** FND-03412, FND-03413, FND-03414

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03418"></a>
## FND-03418: message declaration: chesscom.explanation_engine.v1.GetSanMovesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSanMovesResponse {

### Evidence

- **SRC-0380** `research/proto/chesscom/explanation_engine/v1/feature_get_san_moves.proto` — [preserved redacted evidence](../evidence/text/d36c253d6d8fd7da48b7b04016d23751543e65009be12f572a6146dc4f0d4590.proto)
  Character offset 344.

```text
esscom.explanation_engine.v1.UciMoveList uci_moves = 3;
  }
  oneof _fen {
  string fen = 1;
  }
}

message GetSanMovesResponse {
  repeated string san_moves = 1;
}

```

**Source references:** SRC-0380, SRC-1351  
**URL references:** None independently associated  
**Related findings:** FND-03412, FND-03413, FND-03414

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03419"></a>
## FND-03419: chesscom.explanation_engine.v1.GetSanMovesResponse.san_moves = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string san_moves = 1;

### Evidence

- **SRC-0380** `research/proto/chesscom/explanation_engine/v1/feature_get_san_moves.proto` — [preserved redacted evidence](../evidence/text/d36c253d6d8fd7da48b7b04016d23751543e65009be12f572a6146dc4f0d4590.proto)
  Character offset 376.

```text
MoveList uci_moves = 3;
  }
  oneof _fen {
  string fen = 1;
  }
}

message GetSanMovesResponse {
  repeated string san_moves = 1;
}

```

**Source references:** SRC-0380, SRC-1351  
**URL references:** None independently associated  
**Related findings:** FND-03412, FND-03413, FND-03414

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03420"></a>
## FND-03420: message declaration: chesscom.explanation_engine.v1.LegalMovesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LegalMovesRequest {

### Evidence

- **SRC-0381** `research/proto/chesscom/explanation_engine/v1/feature_legal_moves.proto` — [preserved redacted evidence](../evidence/text/ee577d2a804a6b0584d70d971a6855c2701fcc2e74f0a9869017bb0ce000b5f9.proto)
  Character offset 128.

```text
ion_engine/v1/feature_legal_moves.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message LegalMovesRequest {
}

message LegalMovesResponse {
  repeated .chesscom.chess.v1.Move legal_moves = 1;
}

```

**Source references:** SRC-0381, SRC-1352  
**URL references:** None independently associated  
**Related findings:** FND-03421, FND-03422

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03421"></a>
## FND-03421: message declaration: chesscom.explanation_engine.v1.LegalMovesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LegalMovesResponse {

### Evidence

- **SRC-0381** `research/proto/chesscom/explanation_engine/v1/feature_legal_moves.proto` — [preserved redacted evidence](../evidence/text/ee577d2a804a6b0584d70d971a6855c2701fcc2e74f0a9869017bb0ce000b5f9.proto)
  Character offset 159.

```text
es.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message LegalMovesRequest {
}

message LegalMovesResponse {
  repeated .chesscom.chess.v1.Move legal_moves = 1;
}

```

**Source references:** SRC-0381, SRC-1352  
**URL references:** None independently associated  
**Related findings:** FND-03420, FND-03422

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03422"></a>
## FND-03422: chesscom.explanation_engine.v1.LegalMovesResponse.legal_moves = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Move legal_moves = 1;

### Evidence

- **SRC-0381** `research/proto/chesscom/explanation_engine/v1/feature_legal_moves.proto` — [preserved redacted evidence](../evidence/text/ee577d2a804a6b0584d70d971a6855c2701fcc2e74f0a9869017bb0ce000b5f9.proto)
  Character offset 190.

```text
kage chesscom.explanation_engine.v1;

message LegalMovesRequest {
}

message LegalMovesResponse {
  repeated .chesscom.chess.v1.Move legal_moves = 1;
}

```

**Source references:** SRC-0381, SRC-1352  
**URL references:** None independently associated  
**Related findings:** FND-03420, FND-03421

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03423"></a>
## FND-03423: message declaration: chesscom.explanation_engine.v1.LegalPremovesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LegalPremovesRequest {

### Evidence

- **SRC-0382** `research/proto/chesscom/explanation_engine/v1/feature_legal_premoves.proto` — [preserved redacted evidence](../evidence/text/807d14d01e723bdddd2996a2f19f80d51a3b1c44892e122c531b074fdd1b7e1c.proto)
  Character offset 131.

```text
_engine/v1/feature_legal_premoves.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message LegalPremovesRequest {
  oneof _from {
  .chesscom.chess.v1.Square from = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  repeated .chesscom.chess.v1.Move previous_premoves = 1;
}

message LegalPremovesResponse {
  repeated .chesscom.chess.v1.Move legal_premoves = 1;
}

```

**Source references:** SRC-0382, SRC-1353  
**URL references:** None independently associated  
**Related findings:** FND-03424, FND-03425

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03424"></a>
## FND-03424: oneof declaration: chesscom.explanation_engine.v1.LegalPremovesRequest._from

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _from {

### Evidence

- **SRC-0382** `research/proto/chesscom/explanation_engine/v1/feature_legal_premoves.proto` — [preserved redacted evidence](../evidence/text/807d14d01e723bdddd2996a2f19f80d51a3b1c44892e122c531b074fdd1b7e1c.proto)
  Character offset 164.

```text
.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message LegalPremovesRequest {
  oneof _from {
  .chesscom.chess.v1.Square from = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  repeated .chesscom.chess.v1.Move previous_premoves = 1;
}

message LegalPremovesResponse {
  repeated .chesscom.chess.v1.Move legal_premoves = 1;
}

```

**Source references:** SRC-0382, SRC-1353  
**URL references:** None independently associated  
**Related findings:** FND-03423, FND-03425

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03425"></a>
## FND-03425: chesscom.explanation_engine.v1.LegalPremovesRequest.from = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Square from = 2;

### Evidence

- **SRC-0382** `research/proto/chesscom/explanation_engine/v1/feature_legal_premoves.proto` — [preserved redacted evidence](../evidence/text/807d14d01e723bdddd2996a2f19f80d51a3b1c44892e122c531b074fdd1b7e1c.proto)
  Character offset 180.

```text
: proto3

package chesscom.explanation_engine.v1;

message LegalPremovesRequest {
  oneof _from {
  .chesscom.chess.v1.Square from = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  repeated .chesscom.chess.v1.Move previous_premoves = 1;
}

message LegalPremovesResponse {
  repeated .chesscom.chess.v1.Move legal_premoves = 1;
}

```

**Source references:** SRC-0382, SRC-1353  
**URL references:** None independently associated  
**Related findings:** FND-03423, FND-03424

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03426"></a>
## FND-03426: oneof declaration: chesscom.explanation_engine.v1.LegalPremovesRequest._color

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _color {

### Evidence

- **SRC-0382** `research/proto/chesscom/explanation_engine/v1/feature_legal_premoves.proto` — [preserved redacted evidence](../evidence/text/807d14d01e723bdddd2996a2f19f80d51a3b1c44892e122c531b074fdd1b7e1c.proto)
  Character offset 222.

```text
ine.v1;

message LegalPremovesRequest {
  oneof _from {
  .chesscom.chess.v1.Square from = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  repeated .chesscom.chess.v1.Move previous_premoves = 1;
}

message LegalPremovesResponse {
  repeated .chesscom.chess.v1.Move legal_premoves = 1;
}

```

**Source references:** SRC-0382, SRC-1353  
**URL references:** None independently associated  
**Related findings:** FND-03423, FND-03424, FND-03425

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03427"></a>
## FND-03427: chesscom.explanation_engine.v1.LegalPremovesRequest.color = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Color color = 3;

### Evidence

- **SRC-0382** `research/proto/chesscom/explanation_engine/v1/feature_legal_premoves.proto` — [preserved redacted evidence](../evidence/text/807d14d01e723bdddd2996a2f19f80d51a3b1c44892e122c531b074fdd1b7e1c.proto)
  Character offset 239.

```text
LegalPremovesRequest {
  oneof _from {
  .chesscom.chess.v1.Square from = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  repeated .chesscom.chess.v1.Move previous_premoves = 1;
}

message LegalPremovesResponse {
  repeated .chesscom.chess.v1.Move legal_premoves = 1;
}

```

**Source references:** SRC-0382, SRC-1353  
**URL references:** None independently associated  
**Related findings:** FND-03423, FND-03424, FND-03425

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03428"></a>
## FND-03428: chesscom.explanation_engine.v1.LegalPremovesRequest.previous_premoves = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Move previous_premoves = 1;

### Evidence

- **SRC-0382** `research/proto/chesscom/explanation_engine/v1/feature_legal_premoves.proto` — [preserved redacted evidence](../evidence/text/807d14d01e723bdddd2996a2f19f80d51a3b1c44892e122c531b074fdd1b7e1c.proto)
  Character offset 281.

```text
chesscom.chess.v1.Square from = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  repeated .chesscom.chess.v1.Move previous_premoves = 1;
}

message LegalPremovesResponse {
  repeated .chesscom.chess.v1.Move legal_premoves = 1;
}

```

**Source references:** SRC-0382, SRC-1353  
**URL references:** None independently associated  
**Related findings:** FND-03423, FND-03424, FND-03425

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03429"></a>
## FND-03429: message declaration: chesscom.explanation_engine.v1.LegalPremovesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LegalPremovesResponse {

### Evidence

- **SRC-0382** `research/proto/chesscom/explanation_engine/v1/feature_legal_premoves.proto` — [preserved redacted evidence](../evidence/text/807d14d01e723bdddd2996a2f19f80d51a3b1c44892e122c531b074fdd1b7e1c.proto)
  Character offset 340.

```text
chesscom.chess.v1.Color color = 3;
  }
  repeated .chesscom.chess.v1.Move previous_premoves = 1;
}

message LegalPremovesResponse {
  repeated .chesscom.chess.v1.Move legal_premoves = 1;
}

```

**Source references:** SRC-0382, SRC-1353  
**URL references:** None independently associated  
**Related findings:** FND-03423, FND-03424, FND-03425

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03430"></a>
## FND-03430: chesscom.explanation_engine.v1.LegalPremovesResponse.legal_premoves = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Move legal_premoves = 1;

### Evidence

- **SRC-0382** `research/proto/chesscom/explanation_engine/v1/feature_legal_premoves.proto` — [preserved redacted evidence](../evidence/text/807d14d01e723bdddd2996a2f19f80d51a3b1c44892e122c531b074fdd1b7e1c.proto)
  Character offset 374.

```text

  }
  repeated .chesscom.chess.v1.Move previous_premoves = 1;
}

message LegalPremovesResponse {
  repeated .chesscom.chess.v1.Move legal_premoves = 1;
}

```

**Source references:** SRC-0382, SRC-1353  
**URL references:** None independently associated  
**Related findings:** FND-03423, FND-03424, FND-03425

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03431"></a>
## FND-03431: message declaration: chesscom.explanation_engine.v1.LoadAndSetCoachRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LoadAndSetCoachRequest {

### Evidence

- **SRC-0383** `research/proto/chesscom/explanation_engine/v1/feature_load_and_set_coach.proto` — [preserved redacted evidence](../evidence/text/f0e52fe7d2f0aad84bd18c59ac700daf1c2cdf991a66a6d146308fcb7fe452ec.proto)
  Character offset 135.

```text
ine/v1/feature_load_and_set_coach.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message LoadAndSetCoachRequest {
  optional .chesscom.explanation_engine.v1.TextAsset text_asset = 2;
}

message LoadAndSetCoachResponse {
}

```

**Source references:** SRC-0383, SRC-1354  
**URL references:** None independently associated  
**Related findings:** FND-03432, FND-03433

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03432"></a>
## FND-03432: chesscom.explanation_engine.v1.LoadAndSetCoachRequest.text_asset = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.TextAsset text_asset = 2;

### Evidence

- **SRC-0383** `research/proto/chesscom/explanation_engine/v1/feature_load_and_set_coach.proto` — [preserved redacted evidence](../evidence/text/f0e52fe7d2f0aad84bd18c59ac700daf1c2cdf991a66a6d146308fcb7fe452ec.proto)
  Character offset 170.

```text
roto
// syntax: proto3

package chesscom.explanation_engine.v1;

message LoadAndSetCoachRequest {
  optional .chesscom.explanation_engine.v1.TextAsset text_asset = 2;
}

message LoadAndSetCoachResponse {
}

```

**Source references:** SRC-0383, SRC-1354  
**URL references:** None independently associated  
**Related findings:** FND-03431, FND-03433

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03433"></a>
## FND-03433: message declaration: chesscom.explanation_engine.v1.LoadAndSetCoachResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LoadAndSetCoachResponse {

### Evidence

- **SRC-0383** `research/proto/chesscom/explanation_engine/v1/feature_load_and_set_coach.proto` — [preserved redacted evidence](../evidence/text/f0e52fe7d2f0aad84bd18c59ac700daf1c2cdf991a66a6d146308fcb7fe452ec.proto)
  Character offset 240.

```text
ge LoadAndSetCoachRequest {
  optional .chesscom.explanation_engine.v1.TextAsset text_asset = 2;
}

message LoadAndSetCoachResponse {
}

```

**Source references:** SRC-0383, SRC-1354  
**URL references:** None independently associated  
**Related findings:** FND-03431, FND-03432

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03434"></a>
## FND-03434: enum declaration: chesscom.explanation_engine.v1.BotContentFormat

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum BotContentFormat {

### Evidence

- **SRC-0384** `research/proto/chesscom/explanation_engine/v1/feature_load_bot.proto` — [preserved redacted evidence](../evidence/text/9a04347a2a6693d2569fad4ff7d04dfc77a2480540695d6e0a7c945d46834551.proto)
  Character offset 125.

```text
nation_engine/v1/feature_load_bot.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum BotContentFormat {
  BOT_CONTENT_FORMAT_UNSPECIFIED = 0;
  BOT_CONTENT_FORMAT_JSON = 1;
  BOT_CONTENT_FORMAT_BASE64 = 2;
}

message LoadBotRequest {
  optional string bot_name = 1;
  optional .chesscom.explanation_engine.v1.BotContentFormat content_format = 2;
  optional string bot_content = 3;
  optional string a
```

**Source references:** SRC-0384, SRC-1355  
**URL references:** None independently associated  
**Related findings:** FND-03435, FND-03436

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03435"></a>
## FND-03435: chesscom.explanation_engine.v1.BotContentFormat.BOT_CONTENT_FORMAT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_CONTENT_FORMAT_UNSPECIFIED = 0;

### Evidence

- **SRC-0384** `research/proto/chesscom/explanation_engine/v1/feature_load_bot.proto` — [preserved redacted evidence](../evidence/text/9a04347a2a6693d2569fad4ff7d04dfc77a2480540695d6e0a7c945d46834551.proto)
  Character offset 151.

```text
oad_bot.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum BotContentFormat {
  BOT_CONTENT_FORMAT_UNSPECIFIED = 0;
  BOT_CONTENT_FORMAT_JSON = 1;
  BOT_CONTENT_FORMAT_BASE64 = 2;
}

message LoadBotRequest {
  optional string bot_name = 1;
  optional .chesscom.explanation_engine.v1.BotContentFormat content_format = 2;
  optional string bot_content = 3;
  optional string artifact_id = 4;
}

message
```

**Source references:** SRC-0384, SRC-1355  
**URL references:** None independently associated  
**Related findings:** FND-03434, FND-03436

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03436"></a>
## FND-03436: chesscom.explanation_engine.v1.BotContentFormat.BOT_CONTENT_FORMAT_JSON = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_CONTENT_FORMAT_JSON = 1;

### Evidence

- **SRC-0384** `research/proto/chesscom/explanation_engine/v1/feature_load_bot.proto` — [preserved redacted evidence](../evidence/text/9a04347a2a6693d2569fad4ff7d04dfc77a2480540695d6e0a7c945d46834551.proto)
  Character offset 189.

```text
ge chesscom.explanation_engine.v1;

enum BotContentFormat {
  BOT_CONTENT_FORMAT_UNSPECIFIED = 0;
  BOT_CONTENT_FORMAT_JSON = 1;
  BOT_CONTENT_FORMAT_BASE64 = 2;
}

message LoadBotRequest {
  optional string bot_name = 1;
  optional .chesscom.explanation_engine.v1.BotContentFormat content_format = 2;
  optional string bot_content = 3;
  optional string artifact_id = 4;
}

message LoadBotResponse {
}

```

**Source references:** SRC-0384, SRC-1355  
**URL references:** None independently associated  
**Related findings:** FND-03434, FND-03435

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03437"></a>
## FND-03437: chesscom.explanation_engine.v1.BotContentFormat.BOT_CONTENT_FORMAT_BASE64 = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_CONTENT_FORMAT_BASE64 = 2;

### Evidence

- **SRC-0384** `research/proto/chesscom/explanation_engine/v1/feature_load_bot.proto` — [preserved redacted evidence](../evidence/text/9a04347a2a6693d2569fad4ff7d04dfc77a2480540695d6e0a7c945d46834551.proto)
  Character offset 220.

```text
v1;

enum BotContentFormat {
  BOT_CONTENT_FORMAT_UNSPECIFIED = 0;
  BOT_CONTENT_FORMAT_JSON = 1;
  BOT_CONTENT_FORMAT_BASE64 = 2;
}

message LoadBotRequest {
  optional string bot_name = 1;
  optional .chesscom.explanation_engine.v1.BotContentFormat content_format = 2;
  optional string bot_content = 3;
  optional string artifact_id = 4;
}

message LoadBotResponse {
}

```

**Source references:** SRC-0384, SRC-1355  
**URL references:** None independently associated  
**Related findings:** FND-03434, FND-03435, FND-03436

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03438"></a>
## FND-03438: message declaration: chesscom.explanation_engine.v1.LoadBotRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LoadBotRequest {

### Evidence

- **SRC-0384** `research/proto/chesscom/explanation_engine/v1/feature_load_bot.proto` — [preserved redacted evidence](../evidence/text/9a04347a2a6693d2569fad4ff7d04dfc77a2480540695d6e0a7c945d46834551.proto)
  Character offset 254.

```text
_CONTENT_FORMAT_UNSPECIFIED = 0;
  BOT_CONTENT_FORMAT_JSON = 1;
  BOT_CONTENT_FORMAT_BASE64 = 2;
}

message LoadBotRequest {
  optional string bot_name = 1;
  optional .chesscom.explanation_engine.v1.BotContentFormat content_format = 2;
  optional string bot_content = 3;
  optional string artifact_id = 4;
}

message LoadBotResponse {
}

```

**Source references:** SRC-0384, SRC-1355  
**URL references:** None independently associated  
**Related findings:** FND-03434, FND-03435, FND-03436

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03439"></a>
## FND-03439: chesscom.explanation_engine.v1.LoadBotRequest.bot_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string bot_name = 1;

### Evidence

- **SRC-0384** `research/proto/chesscom/explanation_engine/v1/feature_load_bot.proto` — [preserved redacted evidence](../evidence/text/9a04347a2a6693d2569fad4ff7d04dfc77a2480540695d6e0a7c945d46834551.proto)
  Character offset 281.

```text
 = 0;
  BOT_CONTENT_FORMAT_JSON = 1;
  BOT_CONTENT_FORMAT_BASE64 = 2;
}

message LoadBotRequest {
  optional string bot_name = 1;
  optional .chesscom.explanation_engine.v1.BotContentFormat content_format = 2;
  optional string bot_content = 3;
  optional string artifact_id = 4;
}

message LoadBotResponse {
}

```

**Source references:** SRC-0384, SRC-1355  
**URL references:** None independently associated  
**Related findings:** FND-03434, FND-03435, FND-03436

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03440"></a>
## FND-03440: chesscom.explanation_engine.v1.LoadBotRequest.content_format = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.BotContentFormat content_format = 2;

### Evidence

- **SRC-0384** `research/proto/chesscom/explanation_engine/v1/feature_load_bot.proto` — [preserved redacted evidence](../evidence/text/9a04347a2a6693d2569fad4ff7d04dfc77a2480540695d6e0a7c945d46834551.proto)
  Character offset 313.

```text
= 1;
  BOT_CONTENT_FORMAT_BASE64 = 2;
}

message LoadBotRequest {
  optional string bot_name = 1;
  optional .chesscom.explanation_engine.v1.BotContentFormat content_format = 2;
  optional string bot_content = 3;
  optional string artifact_id = 4;
}

message LoadBotResponse {
}

```

**Source references:** SRC-0384, SRC-1355  
**URL references:** None independently associated  
**Related findings:** FND-03434, FND-03435, FND-03436

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03441"></a>
## FND-03441: chesscom.explanation_engine.v1.LoadBotRequest.bot_content = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string bot_content = 3;

### Evidence

- **SRC-0384** `research/proto/chesscom/explanation_engine/v1/feature_load_bot.proto` — [preserved redacted evidence](../evidence/text/9a04347a2a6693d2569fad4ff7d04dfc77a2480540695d6e0a7c945d46834551.proto)
  Character offset 393.

```text
ing bot_name = 1;
  optional .chesscom.explanation_engine.v1.BotContentFormat content_format = 2;
  optional string bot_content = 3;
  optional string artifact_id = 4;
}

message LoadBotResponse {
}

```

**Source references:** SRC-0384, SRC-1355  
**URL references:** None independently associated  
**Related findings:** FND-03434, FND-03435, FND-03436

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03442"></a>
## FND-03442: chesscom.explanation_engine.v1.LoadBotRequest.artifact_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string artifact_id = 4;

### Evidence

- **SRC-0384** `research/proto/chesscom/explanation_engine/v1/feature_load_bot.proto` — [preserved redacted evidence](../evidence/text/9a04347a2a6693d2569fad4ff7d04dfc77a2480540695d6e0a7c945d46834551.proto)
  Character offset 428.

```text
com.explanation_engine.v1.BotContentFormat content_format = 2;
  optional string bot_content = 3;
  optional string artifact_id = 4;
}

message LoadBotResponse {
}

```

**Source references:** SRC-0384, SRC-1355  
**URL references:** None independently associated  
**Related findings:** FND-03434, FND-03435, FND-03436

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03443"></a>
## FND-03443: message declaration: chesscom.explanation_engine.v1.LoadBotResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LoadBotResponse {

### Evidence

- **SRC-0384** `research/proto/chesscom/explanation_engine/v1/feature_load_bot.proto` — [preserved redacted evidence](../evidence/text/9a04347a2a6693d2569fad4ff7d04dfc77a2480540695d6e0a7c945d46834551.proto)
  Character offset 464.

```text
Format content_format = 2;
  optional string bot_content = 3;
  optional string artifact_id = 4;
}

message LoadBotResponse {
}

```

**Source references:** SRC-0384, SRC-1355  
**URL references:** None independently associated  
**Related findings:** FND-03434, FND-03435, FND-03436

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03444"></a>
## FND-03444: message declaration: chesscom.explanation_engine.v1.LoadCoachRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LoadCoachRequest {

### Evidence

- **SRC-0385** `research/proto/chesscom/explanation_engine/v1/feature_load_coach.proto` — [preserved redacted evidence](../evidence/text/658fa68edb376dc2f4d24cce93282d19c4dfcefc0e49aed1a49b6598be9fcb02.proto)
  Character offset 127.

```text
tion_engine/v1/feature_load_coach.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message LoadCoachRequest {
  optional .chesscom.explanation_engine.v1.TextAsset text_asset = 2;
}

message LoadCoachResponse {
}

```

**Source references:** SRC-0385, SRC-1356  
**URL references:** None independently associated  
**Related findings:** FND-03445, FND-03446

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03445"></a>
## FND-03445: chesscom.explanation_engine.v1.LoadCoachRequest.text_asset = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.TextAsset text_asset = 2;

### Evidence

- **SRC-0385** `research/proto/chesscom/explanation_engine/v1/feature_load_coach.proto` — [preserved redacted evidence](../evidence/text/658fa68edb376dc2f4d24cce93282d19c4dfcefc0e49aed1a49b6598be9fcb02.proto)
  Character offset 156.

```text
oach.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message LoadCoachRequest {
  optional .chesscom.explanation_engine.v1.TextAsset text_asset = 2;
}

message LoadCoachResponse {
}

```

**Source references:** SRC-0385, SRC-1356  
**URL references:** None independently associated  
**Related findings:** FND-03444, FND-03446

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03446"></a>
## FND-03446: message declaration: chesscom.explanation_engine.v1.LoadCoachResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LoadCoachResponse {

### Evidence

- **SRC-0385** `research/proto/chesscom/explanation_engine/v1/feature_load_coach.proto` — [preserved redacted evidence](../evidence/text/658fa68edb376dc2f4d24cce93282d19c4dfcefc0e49aed1a49b6598be9fcb02.proto)
  Character offset 226.

```text

message LoadCoachRequest {
  optional .chesscom.explanation_engine.v1.TextAsset text_asset = 2;
}

message LoadCoachResponse {
}

```

**Source references:** SRC-0385, SRC-1356  
**URL references:** None independently associated  
**Related findings:** FND-03444, FND-03445

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03447"></a>
## FND-03447: message declaration: chesscom.explanation_engine.v1.LoadGameStateRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LoadGameStateRequest {

### Evidence

- **SRC-0386** `research/proto/chesscom/explanation_engine/v1/feature_load_game_state.proto` — [preserved redacted evidence](../evidence/text/7b5b4396109e99fc004a68c7ba51fea14a9f3ab4aafed65e11f814d5772143cb.proto)
  Character offset 132.

```text
engine/v1/feature_load_game_state.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message LoadGameStateRequest {
  optional .chesscom.explanation_engine.v1.GameState game_state = 1;
}

message LoadGameStateResponse {
  repeated .chesscom.explanation_engine.v1.GamePointInfo played_line = 1;
}

```

**Source references:** SRC-0386, SRC-1357  
**URL references:** None independently associated  
**Related findings:** FND-03448, FND-03449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03448"></a>
## FND-03448: chesscom.explanation_engine.v1.LoadGameStateRequest.game_state = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GameState game_state = 1;

### Evidence

- **SRC-0386** `research/proto/chesscom/explanation_engine/v1/feature_load_game_state.proto` — [preserved redacted evidence](../evidence/text/7b5b4396109e99fc004a68c7ba51fea14a9f3ab4aafed65e11f814d5772143cb.proto)
  Character offset 165.

```text
.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message LoadGameStateRequest {
  optional .chesscom.explanation_engine.v1.GameState game_state = 1;
}

message LoadGameStateResponse {
  repeated .chesscom.explanation_engine.v1.GamePointInfo played_line = 1;
}

```

**Source references:** SRC-0386, SRC-1357  
**URL references:** None independently associated  
**Related findings:** FND-03447, FND-03449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03449"></a>
## FND-03449: message declaration: chesscom.explanation_engine.v1.LoadGameStateResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LoadGameStateResponse {

### Evidence

- **SRC-0386** `research/proto/chesscom/explanation_engine/v1/feature_load_game_state.proto` — [preserved redacted evidence](../evidence/text/7b5b4396109e99fc004a68c7ba51fea14a9f3ab4aafed65e11f814d5772143cb.proto)
  Character offset 235.

```text
sage LoadGameStateRequest {
  optional .chesscom.explanation_engine.v1.GameState game_state = 1;
}

message LoadGameStateResponse {
  repeated .chesscom.explanation_engine.v1.GamePointInfo played_line = 1;
}

```

**Source references:** SRC-0386, SRC-1357  
**URL references:** None independently associated  
**Related findings:** FND-03447, FND-03448

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03450"></a>
## FND-03450: chesscom.explanation_engine.v1.LoadGameStateResponse.played_line = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GamePointInfo played_line = 1;

### Evidence

- **SRC-0386** `research/proto/chesscom/explanation_engine/v1/feature_load_game_state.proto` — [preserved redacted evidence](../evidence/text/7b5b4396109e99fc004a68c7ba51fea14a9f3ab4aafed65e11f814d5772143cb.proto)
  Character offset 269.

```text
onal .chesscom.explanation_engine.v1.GameState game_state = 1;
}

message LoadGameStateResponse {
  repeated .chesscom.explanation_engine.v1.GamePointInfo played_line = 1;
}

```

**Source references:** SRC-0386, SRC-1357  
**URL references:** None independently associated  
**Related findings:** FND-03447, FND-03448, FND-03449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03451"></a>
## FND-03451: message declaration: chesscom.explanation_engine.v1.LuaCompletionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LuaCompletionRequest {

### Evidence

- **SRC-0387** `research/proto/chesscom/explanation_engine/v1/feature_lua_completion.proto` — [preserved redacted evidence](../evidence/text/f1033c665db180d3869daebb1e2b62c81445ce8ed636ee531072e50eaef5d8ce.proto)
  Character offset 131.

```text
_engine/v1/feature_lua_completion.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message LuaCompletionRequest {
}

message LuaCompletionResponse {
  repeated string items = 1;
}

```

**Source references:** SRC-0387, SRC-1358  
**URL references:** None independently associated  
**Related findings:** FND-03452, FND-03453

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03452"></a>
## FND-03452: message declaration: chesscom.explanation_engine.v1.LuaCompletionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LuaCompletionResponse {

### Evidence

- **SRC-0387** `research/proto/chesscom/explanation_engine/v1/feature_lua_completion.proto` — [preserved redacted evidence](../evidence/text/f1033c665db180d3869daebb1e2b62c81445ce8ed636ee531072e50eaef5d8ce.proto)
  Character offset 165.

```text
proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message LuaCompletionRequest {
}

message LuaCompletionResponse {
  repeated string items = 1;
}

```

**Source references:** SRC-0387, SRC-1358  
**URL references:** None independently associated  
**Related findings:** FND-03451, FND-03453

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03453"></a>
## FND-03453: chesscom.explanation_engine.v1.LuaCompletionResponse.items = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string items = 1;

### Evidence

- **SRC-0387** `research/proto/chesscom/explanation_engine/v1/feature_lua_completion.proto` — [preserved redacted evidence](../evidence/text/f1033c665db180d3869daebb1e2b62c81445ce8ed636ee531072e50eaef5d8ce.proto)
  Character offset 199.

```text
hesscom.explanation_engine.v1;

message LuaCompletionRequest {
}

message LuaCompletionResponse {
  repeated string items = 1;
}

```

**Source references:** SRC-0387, SRC-1358  
**URL references:** None independently associated  
**Related findings:** FND-03451, FND-03452

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03454"></a>
## FND-03454: message declaration: chesscom.explanation_engine.v1.MakeMovesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MakeMovesRequest {

### Evidence

- **SRC-0388** `research/proto/chesscom/explanation_engine/v1/feature_make_moves.proto` — [preserved redacted evidence](../evidence/text/e93344443ee3f0ebce574dc1f0e6dbf4d447d437a9150bbf979c52a3de0edb2f.proto)
  Character offset 127.

```text
tion_engine/v1/feature_make_moves.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message MakeMovesRequest {
  repeated .chesscom.chess.v1.Move moves = 1;
  optional bool is_played_line = 2;
}

message MakeMovesResponse {
  repeated .chesscom.explanation_engine.v1.GamePointInfo line = 1;
}

```

**Source references:** SRC-0388, SRC-1359  
**URL references:** None independently associated  
**Related findings:** FND-03455, FND-03456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03455"></a>
## FND-03455: chesscom.explanation_engine.v1.MakeMovesRequest.moves = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Move moves = 1;

### Evidence

- **SRC-0388** `research/proto/chesscom/explanation_engine/v1/feature_make_moves.proto` — [preserved redacted evidence](../evidence/text/e93344443ee3f0ebce574dc1f0e6dbf4d447d437a9150bbf979c52a3de0edb2f.proto)
  Character offset 156.

```text
oves.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message MakeMovesRequest {
  repeated .chesscom.chess.v1.Move moves = 1;
  optional bool is_played_line = 2;
}

message MakeMovesResponse {
  repeated .chesscom.explanation_engine.v1.GamePointInfo line = 1;
}

```

**Source references:** SRC-0388, SRC-1359  
**URL references:** None independently associated  
**Related findings:** FND-03454, FND-03456

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03456"></a>
## FND-03456: chesscom.explanation_engine.v1.MakeMovesRequest.is_played_line = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_played_line = 2;

### Evidence

- **SRC-0388** `research/proto/chesscom/explanation_engine/v1/feature_make_moves.proto` — [preserved redacted evidence](../evidence/text/e93344443ee3f0ebce574dc1f0e6dbf4d447d437a9150bbf979c52a3de0edb2f.proto)
  Character offset 202.

```text
.explanation_engine.v1;

message MakeMovesRequest {
  repeated .chesscom.chess.v1.Move moves = 1;
  optional bool is_played_line = 2;
}

message MakeMovesResponse {
  repeated .chesscom.explanation_engine.v1.GamePointInfo line = 1;
}

```

**Source references:** SRC-0388, SRC-1359  
**URL references:** None independently associated  
**Related findings:** FND-03454, FND-03455

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03457"></a>
## FND-03457: message declaration: chesscom.explanation_engine.v1.MakeMovesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MakeMovesResponse {

### Evidence

- **SRC-0388** `research/proto/chesscom/explanation_engine/v1/feature_make_moves.proto` — [preserved redacted evidence](../evidence/text/e93344443ee3f0ebce574dc1f0e6dbf4d447d437a9150bbf979c52a3de0edb2f.proto)
  Character offset 239.

```text
MovesRequest {
  repeated .chesscom.chess.v1.Move moves = 1;
  optional bool is_played_line = 2;
}

message MakeMovesResponse {
  repeated .chesscom.explanation_engine.v1.GamePointInfo line = 1;
}

```

**Source references:** SRC-0388, SRC-1359  
**URL references:** None independently associated  
**Related findings:** FND-03454, FND-03455, FND-03456

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03458"></a>
## FND-03458: chesscom.explanation_engine.v1.MakeMovesResponse.line = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GamePointInfo line = 1;

### Evidence

- **SRC-0388** `research/proto/chesscom/explanation_engine/v1/feature_make_moves.proto` — [preserved redacted evidence](../evidence/text/e93344443ee3f0ebce574dc1f0e6dbf4d447d437a9150bbf979c52a3de0edb2f.proto)
  Character offset 269.

```text
sscom.chess.v1.Move moves = 1;
  optional bool is_played_line = 2;
}

message MakeMovesResponse {
  repeated .chesscom.explanation_engine.v1.GamePointInfo line = 1;
}

```

**Source references:** SRC-0388, SRC-1359  
**URL references:** None independently associated  
**Related findings:** FND-03454, FND-03455, FND-03456

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03459"></a>
## FND-03459: message declaration: chesscom.explanation_engine.v1.MoveClassificationRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MoveClassificationRequest {

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 136.

```text
ne/v1/feature_move_classification.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message MoveClassificationRequest {
  optional bool stream_results = 1;
  optional bool enable_pv_classifications = 2;
}

message MoveClassificationResponse {
  oneof _alternative {
  .chesscom.explanation_engine.v1.AltMoveClassification alternative = 2;
  }
  oneof _pv_classifications {
  .chesscom.explanation_engine.
```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03460, FND-03461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03460"></a>
## FND-03460: chesscom.explanation_engine.v1.MoveClassificationRequest.stream_results = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool stream_results = 1;

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 174.

```text
o
// syntax: proto3

package chesscom.explanation_engine.v1;

message MoveClassificationRequest {
  optional bool stream_results = 1;
  optional bool enable_pv_classifications = 2;
}

message MoveClassificationResponse {
  oneof _alternative {
  .chesscom.explanation_engine.v1.AltMoveClassification alternative = 2;
  }
  oneof _pv_classifications {
  .chesscom.explanation_engine.v1.PvClassifications pv_classification
```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03461"></a>
## FND-03461: chesscom.explanation_engine.v1.MoveClassificationRequest.enable_pv_classifications = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_pv_classifications = 2;

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 210.

```text
m.explanation_engine.v1;

message MoveClassificationRequest {
  optional bool stream_results = 1;
  optional bool enable_pv_classifications = 2;
}

message MoveClassificationResponse {
  oneof _alternative {
  .chesscom.explanation_engine.v1.AltMoveClassification alternative = 2;
  }
  oneof _pv_classifications {
  .chesscom.explanation_engine.v1.PvClassifications pv_classifications = 4;
  }
  optional .chesscom.expl
```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03462"></a>
## FND-03462: message declaration: chesscom.explanation_engine.v1.MoveClassificationResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MoveClassificationResponse {

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 258.

```text
tionRequest {
  optional bool stream_results = 1;
  optional bool enable_pv_classifications = 2;
}

message MoveClassificationResponse {
  oneof _alternative {
  .chesscom.explanation_engine.v1.AltMoveClassification alternative = 2;
  }
  oneof _pv_classifications {
  .chesscom.explanation_engine.v1.PvClassifications pv_classifications = 4;
  }
  optional .chesscom.explanation_engine.v1.EvalClassification active = 1;
```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460, FND-03461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03463"></a>
## FND-03463: oneof declaration: chesscom.explanation_engine.v1.MoveClassificationResponse._alternative

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _alternative {

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 297.

```text
sults = 1;
  optional bool enable_pv_classifications = 2;
}

message MoveClassificationResponse {
  oneof _alternative {
  .chesscom.explanation_engine.v1.AltMoveClassification alternative = 2;
  }
  oneof _pv_classifications {
  .chesscom.explanation_engine.v1.PvClassifications pv_classifications = 4;
  }
  optional .chesscom.explanation_engine.v1.EvalClassification active = 1;
  optional float progress = 3;
}

mess
```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460, FND-03461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03464"></a>
## FND-03464: chesscom.explanation_engine.v1.MoveClassificationResponse.alternative = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.AltMoveClassification alternative = 2;

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 320.

```text
ool enable_pv_classifications = 2;
}

message MoveClassificationResponse {
  oneof _alternative {
  .chesscom.explanation_engine.v1.AltMoveClassification alternative = 2;
  }
  oneof _pv_classifications {
  .chesscom.explanation_engine.v1.PvClassifications pv_classifications = 4;
  }
  optional .chesscom.explanation_engine.v1.EvalClassification active = 1;
  optional float progress = 3;
}

message PvClassifications {
```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460, FND-03461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03465"></a>
## FND-03465: oneof declaration: chesscom.explanation_engine.v1.MoveClassificationResponse._pv_classifications

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pv_classifications {

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 397.

```text
oneof _alternative {
  .chesscom.explanation_engine.v1.AltMoveClassification alternative = 2;
  }
  oneof _pv_classifications {
  .chesscom.explanation_engine.v1.PvClassifications pv_classifications = 4;
  }
  optional .chesscom.explanation_engine.v1.EvalClassification active = 1;
  optional float progress = 3;
}

message PvClassifications {
  repeated .chesscom.explanation_engine.v1.EvalClassification classification
```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460, FND-03461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03466"></a>
## FND-03466: chesscom.explanation_engine.v1.MoveClassificationResponse.pv_classifications = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.PvClassifications pv_classifications = 4;

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 427.

```text
om.explanation_engine.v1.AltMoveClassification alternative = 2;
  }
  oneof _pv_classifications {
  .chesscom.explanation_engine.v1.PvClassifications pv_classifications = 4;
  }
  optional .chesscom.explanation_engine.v1.EvalClassification active = 1;
  optional float progress = 3;
}

message PvClassifications {
  repeated .chesscom.explanation_engine.v1.EvalClassification classifications = 1;
}

message AltMoveClass
```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460, FND-03461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03467"></a>
## FND-03467: chesscom.explanation_engine.v1.MoveClassificationResponse.active = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.EvalClassification active = 1;

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 507.

```text
classifications {
  .chesscom.explanation_engine.v1.PvClassifications pv_classifications = 4;
  }
  optional .chesscom.explanation_engine.v1.EvalClassification active = 1;
  optional float progress = 3;
}

message PvClassifications {
  repeated .chesscom.explanation_engine.v1.EvalClassification classifications = 1;
}

message AltMoveClassification {
  optional .chesscom.explanation_engine.v1.EvalClassification classi
```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460, FND-03461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03468"></a>
## FND-03468: chesscom.explanation_engine.v1.MoveClassificationResponse.progress = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float progress = 3;

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 581.

```text
lassifications = 4;
  }
  optional .chesscom.explanation_engine.v1.EvalClassification active = 1;
  optional float progress = 3;
}

message PvClassifications {
  repeated .chesscom.explanation_engine.v1.EvalClassification classifications = 1;
}

message AltMoveClassification {
  optional .chesscom.explanation_engine.v1.EvalClassification classification = 2;
  optional .chesscom.chess.v1.Move move = 3;
  optional floa
```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460, FND-03461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03469"></a>
## FND-03469: message declaration: chesscom.explanation_engine.v1.PvClassifications

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PvClassifications {

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 613.

```text
al .chesscom.explanation_engine.v1.EvalClassification active = 1;
  optional float progress = 3;
}

message PvClassifications {
  repeated .chesscom.explanation_engine.v1.EvalClassification classifications = 1;
}

message AltMoveClassification {
  optional .chesscom.explanation_engine.v1.EvalClassification classification = 2;
  optional .chesscom.chess.v1.Move move = 3;
  optional float progress = 4;
}

```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460, FND-03461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03470"></a>
## FND-03470: chesscom.explanation_engine.v1.PvClassifications.classifications = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.EvalClassification classifications = 1;

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 643.

```text
e.v1.EvalClassification active = 1;
  optional float progress = 3;
}

message PvClassifications {
  repeated .chesscom.explanation_engine.v1.EvalClassification classifications = 1;
}

message AltMoveClassification {
  optional .chesscom.explanation_engine.v1.EvalClassification classification = 2;
  optional .chesscom.chess.v1.Move move = 3;
  optional float progress = 4;
}

```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460, FND-03461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03471"></a>
## FND-03471: message declaration: chesscom.explanation_engine.v1.AltMoveClassification

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AltMoveClassification {

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 727.

```text
sifications {
  repeated .chesscom.explanation_engine.v1.EvalClassification classifications = 1;
}

message AltMoveClassification {
  optional .chesscom.explanation_engine.v1.EvalClassification classification = 2;
  optional .chesscom.chess.v1.Move move = 3;
  optional float progress = 4;
}

```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460, FND-03461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03472"></a>
## FND-03472: chesscom.explanation_engine.v1.AltMoveClassification.classification = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.EvalClassification classification = 2;

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 761.

```text
.explanation_engine.v1.EvalClassification classifications = 1;
}

message AltMoveClassification {
  optional .chesscom.explanation_engine.v1.EvalClassification classification = 2;
  optional .chesscom.chess.v1.Move move = 3;
  optional float progress = 4;
}

```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460, FND-03461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03473"></a>
## FND-03473: chesscom.explanation_engine.v1.AltMoveClassification.move = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move move = 3;

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 843.

```text
lassification {
  optional .chesscom.explanation_engine.v1.EvalClassification classification = 2;
  optional .chesscom.chess.v1.Move move = 3;
  optional float progress = 4;
}

```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460, FND-03461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03474"></a>
## FND-03474: chesscom.explanation_engine.v1.AltMoveClassification.progress = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float progress = 4;

### Evidence

- **SRC-0389** `research/proto/chesscom/explanation_engine/v1/feature_move_classification.proto` — [preserved redacted evidence](../evidence/text/9cd8b1fd4b2537fea9efdf36e0f53996b1d6599cc6eedded96712b6a05d025ca.proto)
  Character offset 888.

```text
ion_engine.v1.EvalClassification classification = 2;
  optional .chesscom.chess.v1.Move move = 3;
  optional float progress = 4;
}

```

**Source references:** SRC-0389, SRC-1360  
**URL references:** None independently associated  
**Related findings:** FND-03459, FND-03460, FND-03461

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
