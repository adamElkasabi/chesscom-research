# data_models — findings 4201–4300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-04475"></a>
## FND-04475: chesscom.explanation_engine.v1.Skill.SKILL_MAKES_PROTECTED_PASSED_PAWN = 68

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_MAKES_PROTECTED_PASSED_PAWN = 68;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 2074.

```text
N = 65;
  SKILL_DOUBLED_ROOKS_ON_THE_SEVENTH = 66;
  SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN = 67;
  SKILL_MAKES_PROTECTED_PASSED_PAWN = 68;
  SKILL_KING_AND_PAWN_ENDGAMES = 69;
  SKILL_QUEEN_ENDGAMES = 70;
  SKILL_ROOK_ENDGAMES = 71;
  SKILL_KNIGHT_AND_BISHOP_ENDGAMES = 72;
}

message SkillsPosition {
  optional int32 ply = 1;
  repeated .chesscom.explanation_engine.v1.Skill skills = 2;
  optional string validation_h
```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04476"></a>
## FND-04476: chesscom.explanation_engine.v1.Skill.SKILL_KING_AND_PAWN_ENDGAMES = 69

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_KING_AND_PAWN_ENDGAMES = 69;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 2116.

```text
TH = 66;
  SKILL_ROOK_BEHIND_OPPOSING_PASSED_PAWN = 67;
  SKILL_MAKES_PROTECTED_PASSED_PAWN = 68;
  SKILL_KING_AND_PAWN_ENDGAMES = 69;
  SKILL_QUEEN_ENDGAMES = 70;
  SKILL_ROOK_ENDGAMES = 71;
  SKILL_KNIGHT_AND_BISHOP_ENDGAMES = 72;
}

message SkillsPosition {
  optional int32 ply = 1;
  repeated .chesscom.explanation_engine.v1.Skill skills = 2;
  optional string validation_hash = 3;
}

```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04477"></a>
## FND-04477: chesscom.explanation_engine.v1.Skill.SKILL_QUEEN_ENDGAMES = 70

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_QUEEN_ENDGAMES = 70;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 2153.

```text
_PASSED_PAWN = 67;
  SKILL_MAKES_PROTECTED_PASSED_PAWN = 68;
  SKILL_KING_AND_PAWN_ENDGAMES = 69;
  SKILL_QUEEN_ENDGAMES = 70;
  SKILL_ROOK_ENDGAMES = 71;
  SKILL_KNIGHT_AND_BISHOP_ENDGAMES = 72;
}

message SkillsPosition {
  optional int32 ply = 1;
  repeated .chesscom.explanation_engine.v1.Skill skills = 2;
  optional string validation_hash = 3;
}

```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04478"></a>
## FND-04478: chesscom.explanation_engine.v1.Skill.SKILL_ROOK_ENDGAMES = 71

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_ROOK_ENDGAMES = 71;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 2182.

```text
KES_PROTECTED_PASSED_PAWN = 68;
  SKILL_KING_AND_PAWN_ENDGAMES = 69;
  SKILL_QUEEN_ENDGAMES = 70;
  SKILL_ROOK_ENDGAMES = 71;
  SKILL_KNIGHT_AND_BISHOP_ENDGAMES = 72;
}

message SkillsPosition {
  optional int32 ply = 1;
  repeated .chesscom.explanation_engine.v1.Skill skills = 2;
  optional string validation_hash = 3;
}

```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04479"></a>
## FND-04479: chesscom.explanation_engine.v1.Skill.SKILL_KNIGHT_AND_BISHOP_ENDGAMES = 72

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_KNIGHT_AND_BISHOP_ENDGAMES = 72;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 2210.

```text
68;
  SKILL_KING_AND_PAWN_ENDGAMES = 69;
  SKILL_QUEEN_ENDGAMES = 70;
  SKILL_ROOK_ENDGAMES = 71;
  SKILL_KNIGHT_AND_BISHOP_ENDGAMES = 72;
}

message SkillsPosition {
  optional int32 ply = 1;
  repeated .chesscom.explanation_engine.v1.Skill skills = 2;
  optional string validation_hash = 3;
}

```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04480"></a>
## FND-04480: message declaration: chesscom.explanation_engine.v1.SkillsPosition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillsPosition {

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 2252.

```text
 SKILL_QUEEN_ENDGAMES = 70;
  SKILL_ROOK_ENDGAMES = 71;
  SKILL_KNIGHT_AND_BISHOP_ENDGAMES = 72;
}

message SkillsPosition {
  optional int32 ply = 1;
  repeated .chesscom.explanation_engine.v1.Skill skills = 2;
  optional string validation_hash = 3;
}

```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04481"></a>
## FND-04481: chesscom.explanation_engine.v1.SkillsPosition.ply = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 ply = 1;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 2279.

```text

  SKILL_ROOK_ENDGAMES = 71;
  SKILL_KNIGHT_AND_BISHOP_ENDGAMES = 72;
}

message SkillsPosition {
  optional int32 ply = 1;
  repeated .chesscom.explanation_engine.v1.Skill skills = 2;
  optional string validation_hash = 3;
}

```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04482"></a>
## FND-04482: chesscom.explanation_engine.v1.SkillsPosition.skills = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.Skill skills = 2;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 2305.

```text
1;
  SKILL_KNIGHT_AND_BISHOP_ENDGAMES = 72;
}

message SkillsPosition {
  optional int32 ply = 1;
  repeated .chesscom.explanation_engine.v1.Skill skills = 2;
  optional string validation_hash = 3;
}

```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04483"></a>
## FND-04483: chesscom.explanation_engine.v1.SkillsPosition.validation_hash = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string validation_hash = 3;

### Evidence

- **SRC-0426** `research/proto/chesscom/explanation_engine/v1/skills.proto` — [preserved redacted evidence](../evidence/text/e10b5823f0371c48be15b71f53fe8f37b2f0df525089ad86c3108f182af6f180.proto)
  Character offset 2366.

```text
Position {
  optional int32 ply = 1;
  repeated .chesscom.explanation_engine.v1.Skill skills = 2;
  optional string validation_hash = 3;
}

```

**Source references:** SRC-0426, SRC-1397  
**URL references:** None independently associated  
**Related findings:** FND-04406, FND-04407, FND-04408

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04484"></a>
## FND-04484: message declaration: chesscom.explanation_engine.v1.SentenceFragment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SentenceFragment {

### Evidence

- **SRC-0427** `research/proto/chesscom/explanation_engine/v1/speech.proto` — [preserved redacted evidence](../evidence/text/3b57d8d8e43c1f8a92852526249952b5320b67ded06101cbc404c3994229a2e0.proto)
  Character offset 115.

```text
scom/explanation_engine/v1/speech.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message SentenceFragment {
  optional string fragment = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
}

message Sentence {
  repeated .chesscom.explanation_engine.v1.SentenceFragment sentence_fragments = 1;
  optional string audio_url_hash = 2;
}

message Speech {
  repeated .chesscom.expla
```

**Source references:** SRC-0427, SRC-1398  
**URL references:** None independently associated  
**Related findings:** FND-04485, FND-04486

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04485"></a>
## FND-04485: chesscom.explanation_engine.v1.SentenceFragment.fragment = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string fragment = 1;

### Evidence

- **SRC-0427** `research/proto/chesscom/explanation_engine/v1/speech.proto` — [preserved redacted evidence](../evidence/text/3b57d8d8e43c1f8a92852526249952b5320b67ded06101cbc404c3994229a2e0.proto)
  Character offset 144.

```text
eech.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message SentenceFragment {
  optional string fragment = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
}

message Sentence {
  repeated .chesscom.explanation_engine.v1.SentenceFragment sentence_fragments = 1;
  optional string audio_url_hash = 2;
}

message Speech {
  repeated .chesscom.explanation_engine.v1.Sentence sen
```

**Source references:** SRC-0427, SRC-1398  
**URL references:** None independently associated  
**Related findings:** FND-04484, FND-04486

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04486"></a>
## FND-04486: chesscom.explanation_engine.v1.SentenceFragment.arrows_and_squares = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;

### Evidence

- **SRC-0427** `research/proto/chesscom/explanation_engine/v1/speech.proto` — [preserved redacted evidence](../evidence/text/3b57d8d8e43c1f8a92852526249952b5320b67ded06101cbc404c3994229a2e0.proto)
  Character offset 176.

```text
ckage chesscom.explanation_engine.v1;

message SentenceFragment {
  optional string fragment = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
}

message Sentence {
  repeated .chesscom.explanation_engine.v1.SentenceFragment sentence_fragments = 1;
  optional string audio_url_hash = 2;
}

message Speech {
  repeated .chesscom.explanation_engine.v1.Sentence sentences = 1;
}

message SpeechFor
```

**Source references:** SRC-0427, SRC-1398  
**URL references:** None independently associated  
**Related findings:** FND-04484, FND-04485

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04487"></a>
## FND-04487: message declaration: chesscom.explanation_engine.v1.Sentence

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Sentence {

### Evidence

- **SRC-0427** `research/proto/chesscom/explanation_engine/v1/speech.proto` — [preserved redacted evidence](../evidence/text/3b57d8d8e43c1f8a92852526249952b5320b67ded06101cbc404c3994229a2e0.proto)
  Character offset 248.

```text
onal string fragment = 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
}

message Sentence {
  repeated .chesscom.explanation_engine.v1.SentenceFragment sentence_fragments = 1;
  optional string audio_url_hash = 2;
}

message Speech {
  repeated .chesscom.explanation_engine.v1.Sentence sentences = 1;
}

message SpeechForLocale {
  optional .chesscom.explanation_engine.v1.Locale locale = 1;
 
```

**Source references:** SRC-0427, SRC-1398  
**URL references:** None independently associated  
**Related findings:** FND-04484, FND-04485, FND-04486

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04488"></a>
## FND-04488: chesscom.explanation_engine.v1.Sentence.sentence_fragments = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.SentenceFragment sentence_fragments = 1;

### Evidence

- **SRC-0427** `research/proto/chesscom/explanation_engine/v1/speech.proto` — [preserved redacted evidence](../evidence/text/3b57d8d8e43c1f8a92852526249952b5320b67ded06101cbc404c3994229a2e0.proto)
  Character offset 269.

```text
= 1;
  optional .chesscom.chess.v1.ArrowsAndSquares arrows_and_squares = 2;
}

message Sentence {
  repeated .chesscom.explanation_engine.v1.SentenceFragment sentence_fragments = 1;
  optional string audio_url_hash = 2;
}

message Speech {
  repeated .chesscom.explanation_engine.v1.Sentence sentences = 1;
}

message SpeechForLocale {
  optional .chesscom.explanation_engine.v1.Locale locale = 1;
  optional .chesscom.e
```

**Source references:** SRC-0427, SRC-1398  
**URL references:** None independently associated  
**Related findings:** FND-04484, FND-04485, FND-04486

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04489"></a>
## FND-04489: chesscom.explanation_engine.v1.Sentence.audio_url_hash = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string audio_url_hash = 2;

### Evidence

- **SRC-0427** `research/proto/chesscom/explanation_engine/v1/speech.proto` — [preserved redacted evidence](../evidence/text/3b57d8d8e43c1f8a92852526249952b5320b67ded06101cbc404c3994229a2e0.proto)
  Character offset 353.

```text
ge Sentence {
  repeated .chesscom.explanation_engine.v1.SentenceFragment sentence_fragments = 1;
  optional string audio_url_hash = 2;
}

message Speech {
  repeated .chesscom.explanation_engine.v1.Sentence sentences = 1;
}

message SpeechForLocale {
  optional .chesscom.explanation_engine.v1.Locale locale = 1;
  optional .chesscom.explanation_engine.v1.Speech speech = 2;
}

```

**Source references:** SRC-0427, SRC-1398  
**URL references:** None independently associated  
**Related findings:** FND-04484, FND-04485, FND-04486

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04490"></a>
## FND-04490: message declaration: chesscom.explanation_engine.v1.Speech

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Speech {

### Evidence

- **SRC-0427** `research/proto/chesscom/explanation_engine/v1/speech.proto` — [preserved redacted evidence](../evidence/text/3b57d8d8e43c1f8a92852526249952b5320b67ded06101cbc404c3994229a2e0.proto)
  Character offset 392.

```text
anation_engine.v1.SentenceFragment sentence_fragments = 1;
  optional string audio_url_hash = 2;
}

message Speech {
  repeated .chesscom.explanation_engine.v1.Sentence sentences = 1;
}

message SpeechForLocale {
  optional .chesscom.explanation_engine.v1.Locale locale = 1;
  optional .chesscom.explanation_engine.v1.Speech speech = 2;
}

```

**Source references:** SRC-0427, SRC-1398  
**URL references:** None independently associated  
**Related findings:** FND-04484, FND-04485, FND-04486

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04491"></a>
## FND-04491: chesscom.explanation_engine.v1.Speech.sentences = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.Sentence sentences = 1;

### Evidence

- **SRC-0427** `research/proto/chesscom/explanation_engine/v1/speech.proto` — [preserved redacted evidence](../evidence/text/3b57d8d8e43c1f8a92852526249952b5320b67ded06101cbc404c3994229a2e0.proto)
  Character offset 411.

```text
entenceFragment sentence_fragments = 1;
  optional string audio_url_hash = 2;
}

message Speech {
  repeated .chesscom.explanation_engine.v1.Sentence sentences = 1;
}

message SpeechForLocale {
  optional .chesscom.explanation_engine.v1.Locale locale = 1;
  optional .chesscom.explanation_engine.v1.Speech speech = 2;
}

```

**Source references:** SRC-0427, SRC-1398  
**URL references:** None independently associated  
**Related findings:** FND-04484, FND-04485, FND-04486

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04492"></a>
## FND-04492: message declaration: chesscom.explanation_engine.v1.SpeechForLocale

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SpeechForLocale {

### Evidence

- **SRC-0427** `research/proto/chesscom/explanation_engine/v1/speech.proto` — [preserved redacted evidence](../evidence/text/3b57d8d8e43c1f8a92852526249952b5320b67ded06101cbc404c3994229a2e0.proto)
  Character offset 479.

```text
hash = 2;
}

message Speech {
  repeated .chesscom.explanation_engine.v1.Sentence sentences = 1;
}

message SpeechForLocale {
  optional .chesscom.explanation_engine.v1.Locale locale = 1;
  optional .chesscom.explanation_engine.v1.Speech speech = 2;
}

```

**Source references:** SRC-0427, SRC-1398  
**URL references:** None independently associated  
**Related findings:** FND-04484, FND-04485, FND-04486

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04493"></a>
## FND-04493: chesscom.explanation_engine.v1.SpeechForLocale.locale = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Locale locale = 1;

### Evidence

- **SRC-0427** `research/proto/chesscom/explanation_engine/v1/speech.proto` — [preserved redacted evidence](../evidence/text/3b57d8d8e43c1f8a92852526249952b5320b67ded06101cbc404c3994229a2e0.proto)
  Character offset 507.

```text
{
  repeated .chesscom.explanation_engine.v1.Sentence sentences = 1;
}

message SpeechForLocale {
  optional .chesscom.explanation_engine.v1.Locale locale = 1;
  optional .chesscom.explanation_engine.v1.Speech speech = 2;
}

```

**Source references:** SRC-0427, SRC-1398  
**URL references:** None independently associated  
**Related findings:** FND-04484, FND-04485, FND-04486

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04494"></a>
## FND-04494: chesscom.explanation_engine.v1.SpeechForLocale.speech = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech speech = 2;

### Evidence

- **SRC-0427** `research/proto/chesscom/explanation_engine/v1/speech.proto` — [preserved redacted evidence](../evidence/text/3b57d8d8e43c1f8a92852526249952b5320b67ded06101cbc404c3994229a2e0.proto)
  Character offset 569.

```text
s = 1;
}

message SpeechForLocale {
  optional .chesscom.explanation_engine.v1.Locale locale = 1;
  optional .chesscom.explanation_engine.v1.Speech speech = 2;
}

```

**Source references:** SRC-0427, SRC-1398  
**URL references:** None independently associated  
**Related findings:** FND-04484, FND-04485, FND-04486

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04495"></a>
## FND-04495: message declaration: chesscom.explanation_engine.v1.SpeechDebugInfo

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SpeechDebugInfo {

### Evidence

- **SRC-0428** `research/proto/chesscom/explanation_engine/v1/speech_debug_info.proto` — [preserved redacted evidence](../evidence/text/ae029d8fd5f9502c541cf0536e1dce2484d1d4d97a4a24752bc8633b1991015f.proto)
  Character offset 126.

```text
ation_engine/v1/speech_debug_info.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message SpeechDebugInfo {
  optional string source = 1;
  repeated string botchat_triggers = 2;
  repeated string board_events = 3;
  repeated string selected_keys = 4;
}

```

**Source references:** SRC-0428, SRC-1399  
**URL references:** None independently associated  
**Related findings:** FND-04496, FND-04497

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04496"></a>
## FND-04496: chesscom.explanation_engine.v1.SpeechDebugInfo.source = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string source = 1;

### Evidence

- **SRC-0428** `research/proto/chesscom/explanation_engine/v1/speech_debug_info.proto` — [preserved redacted evidence](../evidence/text/ae029d8fd5f9502c541cf0536e1dce2484d1d4d97a4a24752bc8633b1991015f.proto)
  Character offset 154.

```text
_info.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message SpeechDebugInfo {
  optional string source = 1;
  repeated string botchat_triggers = 2;
  repeated string board_events = 3;
  repeated string selected_keys = 4;
}

```

**Source references:** SRC-0428, SRC-1399  
**URL references:** None independently associated  
**Related findings:** FND-04495, FND-04497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04497"></a>
## FND-04497: chesscom.explanation_engine.v1.SpeechDebugInfo.botchat_triggers = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string botchat_triggers = 2;

### Evidence

- **SRC-0428** `research/proto/chesscom/explanation_engine/v1/speech_debug_info.proto` — [preserved redacted evidence](../evidence/text/ae029d8fd5f9502c541cf0536e1dce2484d1d4d97a4a24752bc8633b1991015f.proto)
  Character offset 184.

```text

package chesscom.explanation_engine.v1;

message SpeechDebugInfo {
  optional string source = 1;
  repeated string botchat_triggers = 2;
  repeated string board_events = 3;
  repeated string selected_keys = 4;
}

```

**Source references:** SRC-0428, SRC-1399  
**URL references:** None independently associated  
**Related findings:** FND-04495, FND-04496

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04498"></a>
## FND-04498: chesscom.explanation_engine.v1.SpeechDebugInfo.board_events = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string board_events = 3;

### Evidence

- **SRC-0428** `research/proto/chesscom/explanation_engine/v1/speech_debug_info.proto` — [preserved redacted evidence](../evidence/text/ae029d8fd5f9502c541cf0536e1dce2484d1d4d97a4a24752bc8633b1991015f.proto)
  Character offset 224.

```text


message SpeechDebugInfo {
  optional string source = 1;
  repeated string botchat_triggers = 2;
  repeated string board_events = 3;
  repeated string selected_keys = 4;
}

```

**Source references:** SRC-0428, SRC-1399  
**URL references:** None independently associated  
**Related findings:** FND-04495, FND-04496, FND-04497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04499"></a>
## FND-04499: chesscom.explanation_engine.v1.SpeechDebugInfo.selected_keys = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string selected_keys = 4;

### Evidence

- **SRC-0428** `research/proto/chesscom/explanation_engine/v1/speech_debug_info.proto` — [preserved redacted evidence](../evidence/text/ae029d8fd5f9502c541cf0536e1dce2484d1d4d97a4a24752bc8633b1991015f.proto)
  Character offset 260.

```text
al string source = 1;
  repeated string botchat_triggers = 2;
  repeated string board_events = 3;
  repeated string selected_keys = 4;
}

```

**Source references:** SRC-0428, SRC-1399  
**URL references:** None independently associated  
**Related findings:** FND-04495, FND-04496, FND-04497

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04500"></a>
## FND-04500: message declaration: chesscom.explanation_engine.v1.AdvancedStatsUser

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AdvancedStatsUser {

### Evidence

- **SRC-0429** `research/proto/chesscom/explanation_engine/v1/stats.proto` — [preserved redacted evidence](../evidence/text/413134ddabdeb2a84ce52a4b296471953f0d650b28344846ad3d8820e1713a53.proto)
  Character offset 114.

```text
sscom/explanation_engine/v1/stats.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message AdvancedStatsUser {
  repeated .chesscom.stats.v1.AdvancedStatPercentile advanced_stats_percentiles = 1;
  repeated .chesscom.stats.v1.AdvancedStatCategoryStats category_performances = 2;
}

message AdvancedStatsOther {
  repeated .chesscom.stats.v1.AdvancedStatCategoryGamePerformance white_player_category_perf
```

**Source references:** SRC-0429, SRC-1400  
**URL references:** None independently associated  
**Related findings:** FND-04501, FND-04502

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04501"></a>
## FND-04501: chesscom.explanation_engine.v1.AdvancedStatsUser.advanced_stats_percentiles = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.stats.v1.AdvancedStatPercentile advanced_stats_percentiles = 1;

### Evidence

- **SRC-0429** `research/proto/chesscom/explanation_engine/v1/stats.proto` — [preserved redacted evidence](../evidence/text/413134ddabdeb2a84ce52a4b296471953f0d650b28344846ad3d8820e1713a53.proto)
  Character offset 144.

```text
ats.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message AdvancedStatsUser {
  repeated .chesscom.stats.v1.AdvancedStatPercentile advanced_stats_percentiles = 1;
  repeated .chesscom.stats.v1.AdvancedStatCategoryStats category_performances = 2;
}

message AdvancedStatsOther {
  repeated .chesscom.stats.v1.AdvancedStatCategoryGamePerformance white_player_category_performances = 1;
  repeated .ches
```

**Source references:** SRC-0429, SRC-1400  
**URL references:** None independently associated  
**Related findings:** FND-04500, FND-04502

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04502"></a>
## FND-04502: chesscom.explanation_engine.v1.AdvancedStatsUser.category_performances = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.stats.v1.AdvancedStatCategoryStats category_performances = 2;

### Evidence

- **SRC-0429** `research/proto/chesscom/explanation_engine/v1/stats.proto` — [preserved redacted evidence](../evidence/text/413134ddabdeb2a84ce52a4b296471953f0d650b28344846ad3d8820e1713a53.proto)
  Character offset 229.

```text
dStatsUser {
  repeated .chesscom.stats.v1.AdvancedStatPercentile advanced_stats_percentiles = 1;
  repeated .chesscom.stats.v1.AdvancedStatCategoryStats category_performances = 2;
}

message AdvancedStatsOther {
  repeated .chesscom.stats.v1.AdvancedStatCategoryGamePerformance white_player_category_performances = 1;
  repeated .chesscom.stats.v1.AdvancedStatCategoryGamePerformance black_player_category_performances 
```

**Source references:** SRC-0429, SRC-1400  
**URL references:** None independently associated  
**Related findings:** FND-04500, FND-04501

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04503"></a>
## FND-04503: message declaration: chesscom.explanation_engine.v1.AdvancedStatsOther

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AdvancedStatsOther {

### Evidence

- **SRC-0429** `research/proto/chesscom/explanation_engine/v1/stats.proto` — [preserved redacted evidence](../evidence/text/413134ddabdeb2a84ce52a4b296471953f0d650b28344846ad3d8820e1713a53.proto)
  Character offset 313.

```text
centiles = 1;
  repeated .chesscom.stats.v1.AdvancedStatCategoryStats category_performances = 2;
}

message AdvancedStatsOther {
  repeated .chesscom.stats.v1.AdvancedStatCategoryGamePerformance white_player_category_performances = 1;
  repeated .chesscom.stats.v1.AdvancedStatCategoryGamePerformance black_player_category_performances = 2;
  repeated .chesscom.stats.v1.AdvancedStatPercentile user_advanced_stats_percen
```

**Source references:** SRC-0429, SRC-1400  
**URL references:** None independently associated  
**Related findings:** FND-04500, FND-04501, FND-04502

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04504"></a>
## FND-04504: chesscom.explanation_engine.v1.AdvancedStatsOther.white_player_category_performances = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.stats.v1.AdvancedStatCategoryGamePerformance white_player_category_performances = 1;

### Evidence

- **SRC-0429** `research/proto/chesscom/explanation_engine/v1/stats.proto` — [preserved redacted evidence](../evidence/text/413134ddabdeb2a84ce52a4b296471953f0d650b28344846ad3d8820e1713a53.proto)
  Character offset 344.

```text
com.stats.v1.AdvancedStatCategoryStats category_performances = 2;
}

message AdvancedStatsOther {
  repeated .chesscom.stats.v1.AdvancedStatCategoryGamePerformance white_player_category_performances = 1;
  repeated .chesscom.stats.v1.AdvancedStatCategoryGamePerformance black_player_category_performances = 2;
  repeated .chesscom.stats.v1.AdvancedStatPercentile user_advanced_stats_percentiles = 3;
}

message AdvancedS
```

**Source references:** SRC-0429, SRC-1400  
**URL references:** None independently associated  
**Related findings:** FND-04500, FND-04501, FND-04502

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04505"></a>
## FND-04505: chesscom.explanation_engine.v1.AdvancedStatsOther.black_player_category_performances = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.stats.v1.AdvancedStatCategoryGamePerformance black_player_category_performances = 2;

### Evidence

- **SRC-0429** `research/proto/chesscom/explanation_engine/v1/stats.proto` — [preserved redacted evidence](../evidence/text/413134ddabdeb2a84ce52a4b296471953f0d650b28344846ad3d8820e1713a53.proto)
  Character offset 450.

```text
ed .chesscom.stats.v1.AdvancedStatCategoryGamePerformance white_player_category_performances = 1;
  repeated .chesscom.stats.v1.AdvancedStatCategoryGamePerformance black_player_category_performances = 2;
  repeated .chesscom.stats.v1.AdvancedStatPercentile user_advanced_stats_percentiles = 3;
}

message AdvancedStatsForGame {
  oneof advanced_stats {
  .chesscom.explanation_engine.v1.AdvancedStatsUser advanced_stats_
```

**Source references:** SRC-0429, SRC-1400  
**URL references:** None independently associated  
**Related findings:** FND-04500, FND-04501, FND-04502

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04506"></a>
## FND-04506: chesscom.explanation_engine.v1.AdvancedStatsOther.user_advanced_stats_percentiles = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.stats.v1.AdvancedStatPercentile user_advanced_stats_percentiles = 3;

### Evidence

- **SRC-0429** `research/proto/chesscom/explanation_engine/v1/stats.proto` — [preserved redacted evidence](../evidence/text/413134ddabdeb2a84ce52a4b296471953f0d650b28344846ad3d8820e1713a53.proto)
  Character offset 556.

```text
ed .chesscom.stats.v1.AdvancedStatCategoryGamePerformance black_player_category_performances = 2;
  repeated .chesscom.stats.v1.AdvancedStatPercentile user_advanced_stats_percentiles = 3;
}

message AdvancedStatsForGame {
  oneof advanced_stats {
  .chesscom.explanation_engine.v1.AdvancedStatsUser advanced_stats_user = 1;
  .chesscom.explanation_engine.v1.AdvancedStatsOther advanced_stats_other = 2;
  }
}

```

**Source references:** SRC-0429, SRC-1400  
**URL references:** None independently associated  
**Related findings:** FND-04500, FND-04501, FND-04502

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04507"></a>
## FND-04507: message declaration: chesscom.explanation_engine.v1.AdvancedStatsForGame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AdvancedStatsForGame {

### Evidence

- **SRC-0429** `research/proto/chesscom/explanation_engine/v1/stats.proto` — [preserved redacted evidence](../evidence/text/413134ddabdeb2a84ce52a4b296471953f0d650b28344846ad3d8820e1713a53.proto)
  Character offset 647.

```text
s = 2;
  repeated .chesscom.stats.v1.AdvancedStatPercentile user_advanced_stats_percentiles = 3;
}

message AdvancedStatsForGame {
  oneof advanced_stats {
  .chesscom.explanation_engine.v1.AdvancedStatsUser advanced_stats_user = 1;
  .chesscom.explanation_engine.v1.AdvancedStatsOther advanced_stats_other = 2;
  }
}

```

**Source references:** SRC-0429, SRC-1400  
**URL references:** None independently associated  
**Related findings:** FND-04500, FND-04501, FND-04502

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04508"></a>
## FND-04508: oneof declaration: chesscom.explanation_engine.v1.AdvancedStatsForGame.advanced_stats

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof advanced_stats {

### Evidence

- **SRC-0429** `research/proto/chesscom/explanation_engine/v1/stats.proto` — [preserved redacted evidence](../evidence/text/413134ddabdeb2a84ce52a4b296471953f0d650b28344846ad3d8820e1713a53.proto)
  Character offset 680.

```text
.v1.AdvancedStatPercentile user_advanced_stats_percentiles = 3;
}

message AdvancedStatsForGame {
  oneof advanced_stats {
  .chesscom.explanation_engine.v1.AdvancedStatsUser advanced_stats_user = 1;
  .chesscom.explanation_engine.v1.AdvancedStatsOther advanced_stats_other = 2;
  }
}

```

**Source references:** SRC-0429, SRC-1400  
**URL references:** None independently associated  
**Related findings:** FND-04500, FND-04501, FND-04502

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04509"></a>
## FND-04509: chesscom.explanation_engine.v1.AdvancedStatsForGame.advanced_stats_user = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.AdvancedStatsUser advanced_stats_user = 1;

### Evidence

- **SRC-0429** `research/proto/chesscom/explanation_engine/v1/stats.proto` — [preserved redacted evidence](../evidence/text/413134ddabdeb2a84ce52a4b296471953f0d650b28344846ad3d8820e1713a53.proto)
  Character offset 705.

```text
e user_advanced_stats_percentiles = 3;
}

message AdvancedStatsForGame {
  oneof advanced_stats {
  .chesscom.explanation_engine.v1.AdvancedStatsUser advanced_stats_user = 1;
  .chesscom.explanation_engine.v1.AdvancedStatsOther advanced_stats_other = 2;
  }
}

```

**Source references:** SRC-0429, SRC-1400  
**URL references:** None independently associated  
**Related findings:** FND-04500, FND-04501, FND-04502

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04510"></a>
## FND-04510: chesscom.explanation_engine.v1.AdvancedStatsForGame.advanced_stats_other = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.AdvancedStatsOther advanced_stats_other = 2;

### Evidence

- **SRC-0429** `research/proto/chesscom/explanation_engine/v1/stats.proto` — [preserved redacted evidence](../evidence/text/413134ddabdeb2a84ce52a4b296471953f0d650b28344846ad3d8820e1713a53.proto)
  Character offset 782.

```text
eof advanced_stats {
  .chesscom.explanation_engine.v1.AdvancedStatsUser advanced_stats_user = 1;
  .chesscom.explanation_engine.v1.AdvancedStatsOther advanced_stats_other = 2;
  }
}

```

**Source references:** SRC-0429, SRC-1400  
**URL references:** None independently associated  
**Related findings:** FND-04500, FND-04501, FND-04502

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04511"></a>
## FND-04511: enum declaration: chesscom.explanation_engine.v1.TakeawayClassification

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TakeawayClassification {

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 118.

```text
m/explanation_engine/v1/takeaways.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum TakeawayClassification {
  TAKEAWAY_CLASSIFICATION_UNSPECIFIED = 0;
  TAKEAWAY_CLASSIFICATION_BUILDING_STRENGTH = 1;
  TAKEAWAY_CLASSIFICATION_BE_AWARE = 2;
  TAKEAWAY_CLASSIFICATION_MAKING_PROGRESS = 3;
  TAKEAWAY_CLASSIFICATION_LEARNING_OPPORTUNITY = 4;
}

enum TakeawayPerformance {
  TAKEAWAY_PERFORMANCE_UNSPEC
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04512, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04512"></a>
## FND-04512: chesscom.explanation_engine.v1.TakeawayClassification.TAKEAWAY_CLASSIFICATION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TAKEAWAY_CLASSIFICATION_UNSPECIFIED = 0;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 150.

```text
s.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum TakeawayClassification {
  TAKEAWAY_CLASSIFICATION_UNSPECIFIED = 0;
  TAKEAWAY_CLASSIFICATION_BUILDING_STRENGTH = 1;
  TAKEAWAY_CLASSIFICATION_BE_AWARE = 2;
  TAKEAWAY_CLASSIFICATION_MAKING_PROGRESS = 3;
  TAKEAWAY_CLASSIFICATION_LEARNING_OPPORTUNITY = 4;
}

enum TakeawayPerformance {
  TAKEAWAY_PERFORMANCE_UNSPECIFIED = 0;
  TAKEAWAY_PERFORMANC
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04513"></a>
## FND-04513: chesscom.explanation_engine.v1.TakeawayClassification.TAKEAWAY_CLASSIFICATION_BUILDING_STRENGTH = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TAKEAWAY_CLASSIFICATION_BUILDING_STRENGTH = 1;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 193.

```text
.explanation_engine.v1;

enum TakeawayClassification {
  TAKEAWAY_CLASSIFICATION_UNSPECIFIED = 0;
  TAKEAWAY_CLASSIFICATION_BUILDING_STRENGTH = 1;
  TAKEAWAY_CLASSIFICATION_BE_AWARE = 2;
  TAKEAWAY_CLASSIFICATION_MAKING_PROGRESS = 3;
  TAKEAWAY_CLASSIFICATION_LEARNING_OPPORTUNITY = 4;
}

enum TakeawayPerformance {
  TAKEAWAY_PERFORMANCE_UNSPECIFIED = 0;
  TAKEAWAY_PERFORMANCE_GOOD = 1;
  TAKEAWAY_PERFORMANCE_BAD = 2;
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04514"></a>
## FND-04514: chesscom.explanation_engine.v1.TakeawayClassification.TAKEAWAY_CLASSIFICATION_BE_AWARE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TAKEAWAY_CLASSIFICATION_BE_AWARE = 2;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 242.

```text
ion {
  TAKEAWAY_CLASSIFICATION_UNSPECIFIED = 0;
  TAKEAWAY_CLASSIFICATION_BUILDING_STRENGTH = 1;
  TAKEAWAY_CLASSIFICATION_BE_AWARE = 2;
  TAKEAWAY_CLASSIFICATION_MAKING_PROGRESS = 3;
  TAKEAWAY_CLASSIFICATION_LEARNING_OPPORTUNITY = 4;
}

enum TakeawayPerformance {
  TAKEAWAY_PERFORMANCE_UNSPECIFIED = 0;
  TAKEAWAY_PERFORMANCE_GOOD = 1;
  TAKEAWAY_PERFORMANCE_BAD = 2;
}

message Takeaway {
  oneof _example {
  .ches
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04515"></a>
## FND-04515: chesscom.explanation_engine.v1.TakeawayClassification.TAKEAWAY_CLASSIFICATION_MAKING_PROGRESS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TAKEAWAY_CLASSIFICATION_MAKING_PROGRESS = 3;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 282.

```text
IED = 0;
  TAKEAWAY_CLASSIFICATION_BUILDING_STRENGTH = 1;
  TAKEAWAY_CLASSIFICATION_BE_AWARE = 2;
  TAKEAWAY_CLASSIFICATION_MAKING_PROGRESS = 3;
  TAKEAWAY_CLASSIFICATION_LEARNING_OPPORTUNITY = 4;
}

enum TakeawayPerformance {
  TAKEAWAY_PERFORMANCE_UNSPECIFIED = 0;
  TAKEAWAY_PERFORMANCE_GOOD = 1;
  TAKEAWAY_PERFORMANCE_BAD = 2;
}

message Takeaway {
  oneof _example {
  .chesscom.stats.v1.AdvancedStatExample exampl
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04516"></a>
## FND-04516: chesscom.explanation_engine.v1.TakeawayClassification.TAKEAWAY_CLASSIFICATION_LEARNING_OPPORTUNITY = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TAKEAWAY_CLASSIFICATION_LEARNING_OPPORTUNITY = 4;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 329.

```text
ENGTH = 1;
  TAKEAWAY_CLASSIFICATION_BE_AWARE = 2;
  TAKEAWAY_CLASSIFICATION_MAKING_PROGRESS = 3;
  TAKEAWAY_CLASSIFICATION_LEARNING_OPPORTUNITY = 4;
}

enum TakeawayPerformance {
  TAKEAWAY_PERFORMANCE_UNSPECIFIED = 0;
  TAKEAWAY_PERFORMANCE_GOOD = 1;
  TAKEAWAY_PERFORMANCE_BAD = 2;
}

message Takeaway {
  oneof _example {
  .chesscom.stats.v1.AdvancedStatExample example = 4;
  }
  oneof _train_speech {
  string tra
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04517"></a>
## FND-04517: enum declaration: chesscom.explanation_engine.v1.TakeawayPerformance

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TakeawayPerformance {

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 382.

```text
TAKEAWAY_CLASSIFICATION_MAKING_PROGRESS = 3;
  TAKEAWAY_CLASSIFICATION_LEARNING_OPPORTUNITY = 4;
}

enum TakeawayPerformance {
  TAKEAWAY_PERFORMANCE_UNSPECIFIED = 0;
  TAKEAWAY_PERFORMANCE_GOOD = 1;
  TAKEAWAY_PERFORMANCE_BAD = 2;
}

message Takeaway {
  oneof _example {
  .chesscom.stats.v1.AdvancedStatExample example = 4;
  }
  oneof _train_speech {
  string train_speech = 6;
  }
  oneof _train_item_type {
  .ches
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04518"></a>
## FND-04518: chesscom.explanation_engine.v1.TakeawayPerformance.TAKEAWAY_PERFORMANCE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TAKEAWAY_PERFORMANCE_UNSPECIFIED = 0;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 411.

```text
G_PROGRESS = 3;
  TAKEAWAY_CLASSIFICATION_LEARNING_OPPORTUNITY = 4;
}

enum TakeawayPerformance {
  TAKEAWAY_PERFORMANCE_UNSPECIFIED = 0;
  TAKEAWAY_PERFORMANCE_GOOD = 1;
  TAKEAWAY_PERFORMANCE_BAD = 2;
}

message Takeaway {
  oneof _example {
  .chesscom.stats.v1.AdvancedStatExample example = 4;
  }
  oneof _train_speech {
  string train_speech = 6;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType t
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04519"></a>
## FND-04519: chesscom.explanation_engine.v1.TakeawayPerformance.TAKEAWAY_PERFORMANCE_GOOD = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TAKEAWAY_PERFORMANCE_GOOD = 1;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 451.

```text
N_LEARNING_OPPORTUNITY = 4;
}

enum TakeawayPerformance {
  TAKEAWAY_PERFORMANCE_UNSPECIFIED = 0;
  TAKEAWAY_PERFORMANCE_GOOD = 1;
  TAKEAWAY_PERFORMANCE_BAD = 2;
}

message Takeaway {
  oneof _example {
  .chesscom.stats.v1.AdvancedStatExample example = 4;
  }
  oneof _train_speech {
  string train_speech = 6;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 7;
  }
  optional .ches
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04520"></a>
## FND-04520: chesscom.explanation_engine.v1.TakeawayPerformance.TAKEAWAY_PERFORMANCE_BAD = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TAKEAWAY_PERFORMANCE_BAD = 2;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 484.

```text
um TakeawayPerformance {
  TAKEAWAY_PERFORMANCE_UNSPECIFIED = 0;
  TAKEAWAY_PERFORMANCE_GOOD = 1;
  TAKEAWAY_PERFORMANCE_BAD = 2;
}

message Takeaway {
  oneof _example {
  .chesscom.stats.v1.AdvancedStatExample example = 4;
  }
  oneof _train_speech {
  string train_speech = 6;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 7;
  }
  optional .chesscom.stats.v1.AdvancedStatType ca
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04521"></a>
## FND-04521: message declaration: chesscom.explanation_engine.v1.Takeaway

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Takeaway {

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 517.

```text
AY_PERFORMANCE_UNSPECIFIED = 0;
  TAKEAWAY_PERFORMANCE_GOOD = 1;
  TAKEAWAY_PERFORMANCE_BAD = 2;
}

message Takeaway {
  oneof _example {
  .chesscom.stats.v1.AdvancedStatExample example = 4;
  }
  oneof _train_speech {
  string train_speech = 6;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 7;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04522"></a>
## FND-04522: oneof declaration: chesscom.explanation_engine.v1.Takeaway._example

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _example {

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 538.

```text
IFIED = 0;
  TAKEAWAY_PERFORMANCE_GOOD = 1;
  TAKEAWAY_PERFORMANCE_BAD = 2;
}

message Takeaway {
  oneof _example {
  .chesscom.stats.v1.AdvancedStatExample example = 4;
  }
  oneof _train_speech {
  string train_speech = 6;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 7;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04523"></a>
## FND-04523: chesscom.explanation_engine.v1.Takeaway.example = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.stats.v1.AdvancedStatExample example = 4;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 557.

```text
AY_PERFORMANCE_GOOD = 1;
  TAKEAWAY_PERFORMANCE_BAD = 2;
}

message Takeaway {
  oneof _example {
  .chesscom.stats.v1.AdvancedStatExample example = 4;
  }
  oneof _train_speech {
  string train_speech = 6;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 7;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1.TakeawayClassifica
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04524"></a>
## FND-04524: oneof declaration: chesscom.explanation_engine.v1.Takeaway._train_speech

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _train_speech {

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 615.

```text


message Takeaway {
  oneof _example {
  .chesscom.stats.v1.AdvancedStatExample example = 4;
  }
  oneof _train_speech {
  string train_speech = 6;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 7;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1.TakeawayClassification classification = 2;
  optional string speech = 3;
  o
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04525"></a>
## FND-04525: chesscom.explanation_engine.v1.Takeaway.train_speech = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string train_speech = 6;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 639.

```text
neof _example {
  .chesscom.stats.v1.AdvancedStatExample example = 4;
  }
  oneof _train_speech {
  string train_speech = 6;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 7;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1.TakeawayClassification classification = 2;
  optional string speech = 3;
  optional .chesscom.explan
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04526"></a>
## FND-04526: oneof declaration: chesscom.explanation_engine.v1.Takeaway._train_item_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _train_item_type {

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 670.

```text
ts.v1.AdvancedStatExample example = 4;
  }
  oneof _train_speech {
  string train_speech = 6;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 7;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1.TakeawayClassification classification = 2;
  optional string speech = 3;
  optional .chesscom.explanation_engine.v1.TakeawayPerform
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04527"></a>
## FND-04527: chesscom.explanation_engine.v1.Takeaway.train_item_type = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.train.v1.TrainItemType train_item_type = 7;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 697.

```text
xample = 4;
  }
  oneof _train_speech {
  string train_speech = 6;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 7;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1.TakeawayClassification classification = 2;
  optional string speech = 3;
  optional .chesscom.explanation_engine.v1.TakeawayPerformance performance = 5;
}

me
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04528"></a>
## FND-04528: chesscom.explanation_engine.v1.Takeaway.category = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.stats.v1.AdvancedStatType category = 1;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 757.

```text
h = 6;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 7;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1.TakeawayClassification classification = 2;
  optional string speech = 3;
  optional .chesscom.explanation_engine.v1.TakeawayPerformance performance = 5;
}

message Takeaways {
  repeated .chesscom.explanation_engine.v1
```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04529"></a>
## FND-04529: chesscom.explanation_engine.v1.Takeaway.classification = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.TakeawayClassification classification = 2;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 818.

```text
ainItemType train_item_type = 7;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1.TakeawayClassification classification = 2;
  optional string speech = 3;
  optional .chesscom.explanation_engine.v1.TakeawayPerformance performance = 5;
}

message Takeaways {
  repeated .chesscom.explanation_engine.v1.Takeaway takeaways = 1;
}

```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04530"></a>
## FND-04530: chesscom.explanation_engine.v1.Takeaway.speech = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string speech = 3;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 904.

```text
tegory = 1;
  optional .chesscom.explanation_engine.v1.TakeawayClassification classification = 2;
  optional string speech = 3;
  optional .chesscom.explanation_engine.v1.TakeawayPerformance performance = 5;
}

message Takeaways {
  repeated .chesscom.explanation_engine.v1.Takeaway takeaways = 1;
}

```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04531"></a>
## FND-04531: chesscom.explanation_engine.v1.Takeaway.performance = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.TakeawayPerformance performance = 5;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 934.

```text
om.explanation_engine.v1.TakeawayClassification classification = 2;
  optional string speech = 3;
  optional .chesscom.explanation_engine.v1.TakeawayPerformance performance = 5;
}

message Takeaways {
  repeated .chesscom.explanation_engine.v1.Takeaway takeaways = 1;
}

```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04532"></a>
## FND-04532: message declaration: chesscom.explanation_engine.v1.Takeaways

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Takeaways {

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 1015.

```text
ring speech = 3;
  optional .chesscom.explanation_engine.v1.TakeawayPerformance performance = 5;
}

message Takeaways {
  repeated .chesscom.explanation_engine.v1.Takeaway takeaways = 1;
}

```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04533"></a>
## FND-04533: chesscom.explanation_engine.v1.Takeaways.takeaways = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.Takeaway takeaways = 1;

### Evidence

- **SRC-0430** `research/proto/chesscom/explanation_engine/v1/takeaways.proto` — [preserved redacted evidence](../evidence/text/46b93f333a1bf84276451bf593133ae09510b460ce5191389e388a8b6d531e35.proto)
  Character offset 1037.

```text
ional .chesscom.explanation_engine.v1.TakeawayPerformance performance = 5;
}

message Takeaways {
  repeated .chesscom.explanation_engine.v1.Takeaway takeaways = 1;
}

```

**Source references:** SRC-0430, SRC-1401  
**URL references:** None independently associated  
**Related findings:** FND-04511, FND-04512, FND-04513

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04534"></a>
## FND-04534: message declaration: chesscom.explanation_engine.v1.TcnGame

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TcnGame {

### Evidence

- **SRC-0431** `research/proto/chesscom/explanation_engine/v1/tcn.proto` — [preserved redacted evidence](../evidence/text/89c1b8afc0a2776550c544ed5fac96abdd2879cd733aea0d985a66032f460c88.proto)
  Character offset 112.

```text
hesscom/explanation_engine/v1/tcn.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message TcnGame {
  oneof _initial_fen {
  string initial_fen = 2;
  }
  optional string tcn = 1;
  repeated uint32 move_timestamps = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0431, SRC-1402  
**URL references:** None independently associated  
**Related findings:** FND-04535, FND-04536

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04535"></a>
## FND-04535: oneof declaration: chesscom.explanation_engine.v1.TcnGame._initial_fen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _initial_fen {

### Evidence

- **SRC-0431** `research/proto/chesscom/explanation_engine/v1/tcn.proto` — [preserved redacted evidence](../evidence/text/89c1b8afc0a2776550c544ed5fac96abdd2879cd733aea0d985a66032f460c88.proto)
  Character offset 132.

```text
engine/v1/tcn.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message TcnGame {
  oneof _initial_fen {
  string initial_fen = 2;
  }
  optional string tcn = 1;
  repeated uint32 move_timestamps = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0431, SRC-1402  
**URL references:** None independently associated  
**Related findings:** FND-04534, FND-04536

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04536"></a>
## FND-04536: chesscom.explanation_engine.v1.TcnGame.initial_fen = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string initial_fen = 2;

### Evidence

- **SRC-0431** `research/proto/chesscom/explanation_engine/v1/tcn.proto` — [preserved redacted evidence](../evidence/text/89c1b8afc0a2776550c544ed5fac96abdd2879cd733aea0d985a66032f460c88.proto)
  Character offset 155.

```text
syntax: proto3

package chesscom.explanation_engine.v1;

message TcnGame {
  oneof _initial_fen {
  string initial_fen = 2;
  }
  optional string tcn = 1;
  repeated uint32 move_timestamps = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0431, SRC-1402  
**URL references:** None independently associated  
**Related findings:** FND-04534, FND-04535

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04537"></a>
## FND-04537: chesscom.explanation_engine.v1.TcnGame.tcn = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string tcn = 1;

### Evidence

- **SRC-0431** `research/proto/chesscom/explanation_engine/v1/tcn.proto` — [preserved redacted evidence](../evidence/text/89c1b8afc0a2776550c544ed5fac96abdd2879cd733aea0d985a66032f460c88.proto)
  Character offset 185.

```text
om.explanation_engine.v1;

message TcnGame {
  oneof _initial_fen {
  string initial_fen = 2;
  }
  optional string tcn = 1;
  repeated uint32 move_timestamps = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0431, SRC-1402  
**URL references:** None independently associated  
**Related findings:** FND-04534, FND-04535, FND-04536

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04538"></a>
## FND-04538: chesscom.explanation_engine.v1.TcnGame.move_timestamps = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 move_timestamps = 3;

### Evidence

- **SRC-0431** `research/proto/chesscom/explanation_engine/v1/tcn.proto` — [preserved redacted evidence](../evidence/text/89c1b8afc0a2776550c544ed5fac96abdd2879cd733aea0d985a66032f460c88.proto)
  Character offset 212.

```text
message TcnGame {
  oneof _initial_fen {
  string initial_fen = 2;
  }
  optional string tcn = 1;
  repeated uint32 move_timestamps = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0431, SRC-1402  
**URL references:** None independently associated  
**Related findings:** FND-04534, FND-04535, FND-04536

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04539"></a>
## FND-04539: chesscom.explanation_engine.v1.TcnGame.metadata = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.GameMetadata metadata = 4;

### Evidence

- **SRC-0431** `research/proto/chesscom/explanation_engine/v1/tcn.proto` — [preserved redacted evidence](../evidence/text/89c1b8afc0a2776550c544ed5fac96abdd2879cd733aea0d985a66032f460c88.proto)
  Character offset 251.

```text
{
  string initial_fen = 2;
  }
  optional string tcn = 1;
  repeated uint32 move_timestamps = 3;
  optional .chesscom.chess.v1.GameMetadata metadata = 4;
}

```

**Source references:** SRC-0431, SRC-1402  
**URL references:** None independently associated  
**Related findings:** FND-04534, FND-04535, FND-04536

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04540"></a>
## FND-04540: message declaration: chesscom.explanation_engine.v1.TextAsset

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TextAsset {

### Evidence

- **SRC-0432** `research/proto/chesscom/explanation_engine/v1/text_asset.proto` — [preserved redacted evidence](../evidence/text/ec7091ed045983515b6c7d45cb1f8dbd9d23fb13f2818ec2536ea83cf32af6ec.proto)
  Character offset 119.

```text
/explanation_engine/v1/text_asset.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message TextAsset {
  oneof content {
  bytes encrypted_compressed_in_base64 = 1;
  string json = 2;
  string artifact_id = 6;
  }
  optional string text_id = 4;
  optional string locale = 5;
}

```

**Source references:** SRC-0432, SRC-1403  
**URL references:** None independently associated  
**Related findings:** FND-04541, FND-04542

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04541"></a>
## FND-04541: oneof declaration: chesscom.explanation_engine.v1.TextAsset.content

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof content {

### Evidence

- **SRC-0432** `research/proto/chesscom/explanation_engine/v1/text_asset.proto` — [preserved redacted evidence](../evidence/text/ec7091ed045983515b6c7d45cb1f8dbd9d23fb13f2818ec2536ea83cf32af6ec.proto)
  Character offset 141.

```text
/text_asset.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message TextAsset {
  oneof content {
  bytes encrypted_compressed_in_base64 = 1;
  string json = 2;
  string artifact_id = 6;
  }
  optional string text_id = 4;
  optional string locale = 5;
}

```

**Source references:** SRC-0432, SRC-1403  
**URL references:** None independently associated  
**Related findings:** FND-04540, FND-04542

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04542"></a>
## FND-04542: chesscom.explanation_engine.v1.TextAsset.encrypted_compressed_in_base64 = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bytes encrypted_compressed_in_base64 = 1;

### Evidence

- **SRC-0432** `research/proto/chesscom/explanation_engine/v1/text_asset.proto` — [preserved redacted evidence](../evidence/text/ec7091ed045983515b6c7d45cb1f8dbd9d23fb13f2818ec2536ea83cf32af6ec.proto)
  Character offset 159.

```text
// syntax: proto3

package chesscom.explanation_engine.v1;

message TextAsset {
  oneof content {
  bytes encrypted_compressed_in_base64 = 1;
  string json = 2;
  string artifact_id = 6;
  }
  optional string text_id = 4;
  optional string locale = 5;
}

```

**Source references:** SRC-0432, SRC-1403  
**URL references:** None independently associated  
**Related findings:** FND-04540, FND-04541

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04543"></a>
## FND-04543: chesscom.explanation_engine.v1.TextAsset.json = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string json = 2;

### Evidence

- **SRC-0432** `research/proto/chesscom/explanation_engine/v1/text_asset.proto` — [preserved redacted evidence](../evidence/text/ec7091ed045983515b6c7d45cb1f8dbd9d23fb13f2818ec2536ea83cf32af6ec.proto)
  Character offset 203.

```text
ion_engine.v1;

message TextAsset {
  oneof content {
  bytes encrypted_compressed_in_base64 = 1;
  string json = 2;
  string artifact_id = 6;
  }
  optional string text_id = 4;
  optional string locale = 5;
}

```

**Source references:** SRC-0432, SRC-1403  
**URL references:** None independently associated  
**Related findings:** FND-04540, FND-04541, FND-04542

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04544"></a>
## FND-04544: chesscom.explanation_engine.v1.TextAsset.artifact_id = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string artifact_id = 6;

### Evidence

- **SRC-0432** `research/proto/chesscom/explanation_engine/v1/text_asset.proto` — [preserved redacted evidence](../evidence/text/ec7091ed045983515b6c7d45cb1f8dbd9d23fb13f2818ec2536ea83cf32af6ec.proto)
  Character offset 222.

```text
sage TextAsset {
  oneof content {
  bytes encrypted_compressed_in_base64 = 1;
  string json = 2;
  string artifact_id = 6;
  }
  optional string text_id = 4;
  optional string locale = 5;
}

```

**Source references:** SRC-0432, SRC-1403  
**URL references:** None independently associated  
**Related findings:** FND-04540, FND-04541, FND-04542

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04545"></a>
## FND-04545: chesscom.explanation_engine.v1.TextAsset.text_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string text_id = 4;

### Evidence

- **SRC-0432** `research/proto/chesscom/explanation_engine/v1/text_asset.proto` — [preserved redacted evidence](../evidence/text/ec7091ed045983515b6c7d45cb1f8dbd9d23fb13f2818ec2536ea83cf32af6ec.proto)
  Character offset 252.

```text
nt {
  bytes encrypted_compressed_in_base64 = 1;
  string json = 2;
  string artifact_id = 6;
  }
  optional string text_id = 4;
  optional string locale = 5;
}

```

**Source references:** SRC-0432, SRC-1403  
**URL references:** None independently associated  
**Related findings:** FND-04540, FND-04541, FND-04542

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04546"></a>
## FND-04546: chesscom.explanation_engine.v1.TextAsset.locale = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string locale = 5;

### Evidence

- **SRC-0432** `research/proto/chesscom/explanation_engine/v1/text_asset.proto` — [preserved redacted evidence](../evidence/text/ec7091ed045983515b6c7d45cb1f8dbd9d23fb13f2818ec2536ea83cf32af6ec.proto)
  Character offset 283.

```text
ed_in_base64 = 1;
  string json = 2;
  string artifact_id = 6;
  }
  optional string text_id = 4;
  optional string locale = 5;
}

```

**Source references:** SRC-0432, SRC-1403  
**URL references:** None independently associated  
**Related findings:** FND-04540, FND-04541, FND-04542

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04547"></a>
## FND-04547: message declaration: chesscom.explanation_engine.v1.TorchSearchMode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TorchSearchMode {

### Evidence

- **SRC-0433** `research/proto/chesscom/explanation_engine/v1/torch_search_mode.proto` — [preserved redacted evidence](../evidence/text/e8ae3321a9e8827b1c2acb5a539aaedd4938e9cc15bcbc93b3d53930560f51e0.proto)
  Character offset 126.

```text
ation_engine/v1/torch_search_mode.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message TorchSearchMode {
  oneof mode {
  .chesscom.explanation_engine.v1.TorchSearchMode.Human human = 1;
  .chesscom.explanation_engine.v1.TorchSearchMode.Multisearch multisearch = 2;
  }
  message Human {
    oneof _disable_maia {
  bool disable_maia = 1;
    }
  }
  message Multisearch {
    oneof _reduce_nodes_on
```

**Source references:** SRC-0433, SRC-1404  
**URL references:** None independently associated  
**Related findings:** FND-04548, FND-04549

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04548"></a>
## FND-04548: oneof declaration: chesscom.explanation_engine.v1.TorchSearchMode.mode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof mode {

### Evidence

- **SRC-0433** `research/proto/chesscom/explanation_engine/v1/torch_search_mode.proto` — [preserved redacted evidence](../evidence/text/e8ae3321a9e8827b1c2acb5a539aaedd4938e9cc15bcbc93b3d53930560f51e0.proto)
  Character offset 154.

```text
_mode.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message TorchSearchMode {
  oneof mode {
  .chesscom.explanation_engine.v1.TorchSearchMode.Human human = 1;
  .chesscom.explanation_engine.v1.TorchSearchMode.Multisearch multisearch = 2;
  }
  message Human {
    oneof _disable_maia {
  bool disable_maia = 1;
    }
  }
  message Multisearch {
    oneof _reduce_nodes_on_successive_searches {
  boo
```

**Source references:** SRC-0433, SRC-1404  
**URL references:** None independently associated  
**Related findings:** FND-04547, FND-04549

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04549"></a>
## FND-04549: chesscom.explanation_engine.v1.TorchSearchMode.human = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.TorchSearchMode.Human human = 1;

### Evidence

- **SRC-0433** `research/proto/chesscom/explanation_engine/v1/torch_search_mode.proto` — [preserved redacted evidence](../evidence/text/e8ae3321a9e8827b1c2acb5a539aaedd4938e9cc15bcbc93b3d53930560f51e0.proto)
  Character offset 169.

```text
syntax: proto3

package chesscom.explanation_engine.v1;

message TorchSearchMode {
  oneof mode {
  .chesscom.explanation_engine.v1.TorchSearchMode.Human human = 1;
  .chesscom.explanation_engine.v1.TorchSearchMode.Multisearch multisearch = 2;
  }
  message Human {
    oneof _disable_maia {
  bool disable_maia = 1;
    }
  }
  message Multisearch {
    oneof _reduce_nodes_on_successive_searches {
  bool reduce_nodes_
```

**Source references:** SRC-0433, SRC-1404  
**URL references:** None independently associated  
**Related findings:** FND-04547, FND-04548

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04550"></a>
## FND-04550: chesscom.explanation_engine.v1.TorchSearchMode.multisearch = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.TorchSearchMode.Multisearch multisearch = 2;

### Evidence

- **SRC-0433** `research/proto/chesscom/explanation_engine/v1/torch_search_mode.proto` — [preserved redacted evidence](../evidence/text/e8ae3321a9e8827b1c2acb5a539aaedd4938e9cc15bcbc93b3d53930560f51e0.proto)
  Character offset 236.

```text
rchSearchMode {
  oneof mode {
  .chesscom.explanation_engine.v1.TorchSearchMode.Human human = 1;
  .chesscom.explanation_engine.v1.TorchSearchMode.Multisearch multisearch = 2;
  }
  message Human {
    oneof _disable_maia {
  bool disable_maia = 1;
    }
  }
  message Multisearch {
    oneof _reduce_nodes_on_successive_searches {
  bool reduce_nodes_on_successive_searches = 1;
    }
  }
}

```

**Source references:** SRC-0433, SRC-1404  
**URL references:** None independently associated  
**Related findings:** FND-04547, FND-04548, FND-04549

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04551"></a>
## FND-04551: message declaration: chesscom.explanation_engine.v1.TorchSearchMode.Human

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Human {

### Evidence

- **SRC-0433** `research/proto/chesscom/explanation_engine/v1/torch_search_mode.proto` — [preserved redacted evidence](../evidence/text/e8ae3321a9e8827b1c2acb5a539aaedd4938e9cc15bcbc93b3d53930560f51e0.proto)
  Character offset 319.

```text
man human = 1;
  .chesscom.explanation_engine.v1.TorchSearchMode.Multisearch multisearch = 2;
  }
  message Human {
    oneof _disable_maia {
  bool disable_maia = 1;
    }
  }
  message Multisearch {
    oneof _reduce_nodes_on_successive_searches {
  bool reduce_nodes_on_successive_searches = 1;
    }
  }
}

```

**Source references:** SRC-0433, SRC-1404  
**URL references:** None independently associated  
**Related findings:** FND-04547, FND-04548, FND-04549

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04552"></a>
## FND-04552: oneof declaration: chesscom.explanation_engine.v1.TorchSearchMode.Human._disable_maia

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _disable_maia {

### Evidence

- **SRC-0433** `research/proto/chesscom/explanation_engine/v1/torch_search_mode.proto` — [preserved redacted evidence](../evidence/text/e8ae3321a9e8827b1c2acb5a539aaedd4938e9cc15bcbc93b3d53930560f51e0.proto)
  Character offset 339.

```text
esscom.explanation_engine.v1.TorchSearchMode.Multisearch multisearch = 2;
  }
  message Human {
    oneof _disable_maia {
  bool disable_maia = 1;
    }
  }
  message Multisearch {
    oneof _reduce_nodes_on_successive_searches {
  bool reduce_nodes_on_successive_searches = 1;
    }
  }
}

```

**Source references:** SRC-0433, SRC-1404  
**URL references:** None independently associated  
**Related findings:** FND-04547, FND-04548, FND-04549

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04553"></a>
## FND-04553: chesscom.explanation_engine.v1.TorchSearchMode.Human.disable_maia = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool disable_maia = 1;

### Evidence

- **SRC-0433** `research/proto/chesscom/explanation_engine/v1/torch_search_mode.proto` — [preserved redacted evidence](../evidence/text/e8ae3321a9e8827b1c2acb5a539aaedd4938e9cc15bcbc93b3d53930560f51e0.proto)
  Character offset 363.

```text
e.v1.TorchSearchMode.Multisearch multisearch = 2;
  }
  message Human {
    oneof _disable_maia {
  bool disable_maia = 1;
    }
  }
  message Multisearch {
    oneof _reduce_nodes_on_successive_searches {
  bool reduce_nodes_on_successive_searches = 1;
    }
  }
}

```

**Source references:** SRC-0433, SRC-1404  
**URL references:** None independently associated  
**Related findings:** FND-04547, FND-04548, FND-04549

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04554"></a>
## FND-04554: message declaration: chesscom.explanation_engine.v1.TorchSearchMode.Multisearch

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Multisearch {

### Evidence

- **SRC-0433** `research/proto/chesscom/explanation_engine/v1/torch_search_mode.proto` — [preserved redacted evidence](../evidence/text/e8ae3321a9e8827b1c2acb5a539aaedd4938e9cc15bcbc93b3d53930560f51e0.proto)
  Character offset 398.

```text
ltisearch = 2;
  }
  message Human {
    oneof _disable_maia {
  bool disable_maia = 1;
    }
  }
  message Multisearch {
    oneof _reduce_nodes_on_successive_searches {
  bool reduce_nodes_on_successive_searches = 1;
    }
  }
}

```

**Source references:** SRC-0433, SRC-1404  
**URL references:** None independently associated  
**Related findings:** FND-04547, FND-04548, FND-04549

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04555"></a>
## FND-04555: oneof declaration: chesscom.explanation_engine.v1.TorchSearchMode.Multisearch._reduce_nodes_on_successive_searches

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _reduce_nodes_on_successive_searches {

### Evidence

- **SRC-0433** `research/proto/chesscom/explanation_engine/v1/torch_search_mode.proto` — [preserved redacted evidence](../evidence/text/e8ae3321a9e8827b1c2acb5a539aaedd4938e9cc15bcbc93b3d53930560f51e0.proto)
  Character offset 424.

```text
ge Human {
    oneof _disable_maia {
  bool disable_maia = 1;
    }
  }
  message Multisearch {
    oneof _reduce_nodes_on_successive_searches {
  bool reduce_nodes_on_successive_searches = 1;
    }
  }
}

```

**Source references:** SRC-0433, SRC-1404  
**URL references:** None independently associated  
**Related findings:** FND-04547, FND-04548, FND-04549

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04556"></a>
## FND-04556: chesscom.explanation_engine.v1.TorchSearchMode.Multisearch.reduce_nodes_on_successive_searches = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool reduce_nodes_on_successive_searches = 1;

### Evidence

- **SRC-0433** `research/proto/chesscom/explanation_engine/v1/torch_search_mode.proto` — [preserved redacted evidence](../evidence/text/e8ae3321a9e8827b1c2acb5a539aaedd4938e9cc15bcbc93b3d53930560f51e0.proto)
  Character offset 471.

```text
able_maia = 1;
    }
  }
  message Multisearch {
    oneof _reduce_nodes_on_successive_searches {
  bool reduce_nodes_on_successive_searches = 1;
    }
  }
}

```

**Source references:** SRC-0433, SRC-1404  
**URL references:** None independently associated  
**Related findings:** FND-04547, FND-04548, FND-04549

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04557"></a>
## FND-04557: message declaration: chesscom.flair.v1.Flair

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Flair {

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 88.

```text
// source: chesscom/flair/v1/flair.proto
// syntax: proto3

package chesscom.flair.v1;

message Flair {
  oneof _legacy_code {
  string legacy_code = 16;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  repeated .chesscom.flair.v1.Flair.ImagesEntry images = 4;
  optional .chesscom.flair.v1.Flair.Category category = 5;
  optional int32 display_priority = 6;
  o
```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04558, FND-04559

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04558"></a>
## FND-04558: oneof declaration: chesscom.flair.v1.Flair._legacy_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _legacy_code {

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 106.

```text
rce: chesscom/flair/v1/flair.proto
// syntax: proto3

package chesscom.flair.v1;

message Flair {
  oneof _legacy_code {
  string legacy_code = 16;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  repeated .chesscom.flair.v1.Flair.ImagesEntry images = 4;
  optional .chesscom.flair.v1.Flair.Category category = 5;
  optional int32 display_priority = 6;
  optional .chesscom.
```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04559

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04559"></a>
## FND-04559: chesscom.flair.v1.Flair.legacy_code = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string legacy_code = 16;

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 129.

```text
flair.proto
// syntax: proto3

package chesscom.flair.v1;

message Flair {
  oneof _legacy_code {
  string legacy_code = 16;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  repeated .chesscom.flair.v1.Flair.ImagesEntry images = 4;
  optional .chesscom.flair.v1.Flair.Category category = 5;
  optional int32 display_priority = 6;
  optional .chesscom.unlockables.v1.Unlockab
```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04560"></a>
## FND-04560: chesscom.flair.v1.Flair.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 160.

```text
package chesscom.flair.v1;

message Flair {
  oneof _legacy_code {
  string legacy_code = 16;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  repeated .chesscom.flair.v1.Flair.ImagesEntry images = 4;
  optional .chesscom.flair.v1.Flair.Category category = 5;
  optional int32 display_priority = 6;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 
```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04561"></a>
## FND-04561: chesscom.flair.v1.Flair.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 186.

```text


message Flair {
  oneof _legacy_code {
  string legacy_code = 16;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  repeated .chesscom.flair.v1.Flair.ImagesEntry images = 4;
  optional .chesscom.flair.v1.Flair.Category category = 5;
  optional int32 display_priority = 6;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 7;
  message ImagesEntry {
```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04562"></a>
## FND-04562: chesscom.flair.v1.Flair.description = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string description = 3;

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 214.

```text
egacy_code {
  string legacy_code = 16;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  repeated .chesscom.flair.v1.Flair.ImagesEntry images = 4;
  optional .chesscom.flair.v1.Flair.Category category = 5;
  optional int32 display_priority = 6;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 7;
  message ImagesEntry {
  optional string key = 1;

```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04563"></a>
## FND-04563: chesscom.flair.v1.Flair.images = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.flair.v1.Flair.ImagesEntry images = 4;

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 249.

```text
 16;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  repeated .chesscom.flair.v1.Flair.ImagesEntry images = 4;
  optional .chesscom.flair.v1.Flair.Category category = 5;
  optional int32 display_priority = 6;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 7;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
  
```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04564"></a>
## FND-04564: chesscom.flair.v1.Flair.category = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.flair.v1.Flair.Category category = 5;

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 309.

```text
2;
  optional string description = 3;
  repeated .chesscom.flair.v1.Flair.ImagesEntry images = 4;
  optional .chesscom.flair.v1.Flair.Category category = 5;
  optional int32 display_priority = 6;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 7;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
  message Category {
  optional string name = 1;
  }
}

messag
```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04565"></a>
## FND-04565: chesscom.flair.v1.Flair.display_priority = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 display_priority = 6;

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 368.

```text
flair.v1.Flair.ImagesEntry images = 4;
  optional .chesscom.flair.v1.Flair.Category category = 5;
  optional int32 display_priority = 6;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 7;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
  message Category {
  optional string name = 1;
  }
}

message FlairSelectionItem {
  optional .chesscom.flair.v1.Flair 
```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04566"></a>
## FND-04566: chesscom.flair.v1.Flair.unlockable_preview = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 7;

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 407.

```text
  optional .chesscom.flair.v1.Flair.Category category = 5;
  optional int32 display_priority = 6;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 7;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
  message Category {
  optional string name = 1;
  }
}

message FlairSelectionItem {
  optional .chesscom.flair.v1.Flair flair = 1;
  optional bool available = 
```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04567"></a>
## FND-04567: message declaration: chesscom.flair.v1.Flair.ImagesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ImagesEntry {

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 485.

```text
splay_priority = 6;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 7;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
  message Category {
  optional string name = 1;
  }
}

message FlairSelectionItem {
  optional .chesscom.flair.v1.Flair flair = 1;
  optional bool available = 2;
}

```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04568"></a>
## FND-04568: chesscom.flair.v1.Flair.ImagesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 509.

```text
tional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 7;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
  message Category {
  optional string name = 1;
  }
}

message FlairSelectionItem {
  optional .chesscom.flair.v1.Flair flair = 1;
  optional bool available = 2;
}

```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04569"></a>
## FND-04569: chesscom.flair.v1.Flair.ImagesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 536.

```text
s.v1.UnlockablePreview unlockable_preview = 7;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
  message Category {
  optional string name = 1;
  }
}

message FlairSelectionItem {
  optional .chesscom.flair.v1.Flair flair = 1;
  optional bool available = 2;
}

```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04570"></a>
## FND-04570: message declaration: chesscom.flair.v1.Flair.Category

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Category {

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 569.

```text
_preview = 7;
  message ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
  message Category {
  optional string name = 1;
  }
}

message FlairSelectionItem {
  optional .chesscom.flair.v1.Flair flair = 1;
  optional bool available = 2;
}

```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04571"></a>
## FND-04571: chesscom.flair.v1.Flair.Category.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 590.

```text
ge ImagesEntry {
  optional string key = 1;
  optional string value = 2;
  }
  message Category {
  optional string name = 1;
  }
}

message FlairSelectionItem {
  optional .chesscom.flair.v1.Flair flair = 1;
  optional bool available = 2;
}

```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04572"></a>
## FND-04572: message declaration: chesscom.flair.v1.FlairSelectionItem

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FlairSelectionItem {

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 623.

```text
g key = 1;
  optional string value = 2;
  }
  message Category {
  optional string name = 1;
  }
}

message FlairSelectionItem {
  optional .chesscom.flair.v1.Flair flair = 1;
  optional bool available = 2;
}

```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-04573"></a>
## FND-04573: chesscom.flair.v1.FlairSelectionItem.flair = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.flair.v1.Flair flair = 1;

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 654.

```text
lue = 2;
  }
  message Category {
  optional string name = 1;
  }
}

message FlairSelectionItem {
  optional .chesscom.flair.v1.Flair flair = 1;
  optional bool available = 2;
}

```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-04574"></a>
## FND-04574: chesscom.flair.v1.FlairSelectionItem.available = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool available = 2;

### Evidence

- **SRC-0434** `research/proto/chesscom/flair/v1/flair.proto` — [preserved redacted evidence](../evidence/text/7ca133b87670fc75ac9fecc45e1b98f2afe81cbc6410347379c10484a44b3c7e.proto)
  Character offset 701.

```text
ring name = 1;
  }
}

message FlairSelectionItem {
  optional .chesscom.flair.v1.Flair flair = 1;
  optional bool available = 2;
}

```

**Source references:** SRC-0434, SRC-1405  
**URL references:** None independently associated  
**Related findings:** FND-04557, FND-04558, FND-04559

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
