# data_models — findings 3501–3600

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-03775"></a>
## FND-03775: chesscom.explanation_engine.v1.Metadata.annotated_pgn = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string annotated_pgn = 2;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 610.

```text
g opening = 6;
}

message Metadata {
  optional .chesscom.api.v1.SemanticVersion cee_version = 1;
  optional string annotated_pgn = 2;
}

message EvalGraph {
  repeated .chesscom.explanation_engine.v1.EvalGraphTick eval_graph_ticks = 1;
}

message EvalGraphTick {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 2;
  optional .chesscom.engine.v1.Score move_score = 1;
  optional bool 
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03776"></a>
## FND-03776: message declaration: chesscom.explanation_engine.v1.EvalGraph

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EvalGraph {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 648.

```text
 optional .chesscom.api.v1.SemanticVersion cee_version = 1;
  optional string annotated_pgn = 2;
}

message EvalGraph {
  repeated .chesscom.explanation_engine.v1.EvalGraphTick eval_graph_ticks = 1;
}

message EvalGraphTick {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 2;
  optional .chesscom.engine.v1.Score move_score = 1;
  optional bool is_key_moment = 3;
}

message Highligh
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03777"></a>
## FND-03777: chesscom.explanation_engine.v1.EvalGraph.eval_graph_ticks = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.EvalGraphTick eval_graph_ticks = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 670.

```text
i.v1.SemanticVersion cee_version = 1;
  optional string annotated_pgn = 2;
}

message EvalGraph {
  repeated .chesscom.explanation_engine.v1.EvalGraphTick eval_graph_ticks = 1;
}

message EvalGraphTick {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 2;
  optional .chesscom.engine.v1.Score move_score = 1;
  optional bool is_key_moment = 3;
}

message Highlights {
  optional string
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03778"></a>
## FND-03778: message declaration: chesscom.explanation_engine.v1.EvalGraphTick

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EvalGraphTick {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 750.

```text
ssage EvalGraph {
  repeated .chesscom.explanation_engine.v1.EvalGraphTick eval_graph_ticks = 1;
}

message EvalGraphTick {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 2;
  optional .chesscom.engine.v1.Score move_score = 1;
  optional bool is_key_moment = 3;
}

message Highlights {
  optional string game_summary = 1;
  optional .chesscom.explanation_engine.v1.Accuracy accuracy 
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03779"></a>
## FND-03779: chesscom.explanation_engine.v1.EvalGraphTick.move_classification = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 2;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 776.

```text
ed .chesscom.explanation_engine.v1.EvalGraphTick eval_graph_ticks = 1;
}

message EvalGraphTick {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 2;
  optional .chesscom.engine.v1.Score move_score = 1;
  optional bool is_key_moment = 3;
}

message Highlights {
  optional string game_summary = 1;
  optional .chesscom.explanation_engine.v1.Accuracy accuracy = 3;
  optional .chesscom.
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03780"></a>
## FND-03780: chesscom.explanation_engine.v1.EvalGraphTick.move_score = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.engine.v1.Score move_score = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 863.

```text
raphTick {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 2;
  optional .chesscom.engine.v1.Score move_score = 1;
  optional bool is_key_moment = 3;
}

message Highlights {
  optional string game_summary = 1;
  optional .chesscom.explanation_engine.v1.Accuracy accuracy = 3;
  optional .chesscom.explanation_engine.v1.ClassificationTallies classification_tallies = 4;
  optional .che
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03781"></a>
## FND-03781: chesscom.explanation_engine.v1.EvalGraphTick.is_key_moment = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_key_moment = 3;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 916.

```text
.MoveClassification move_classification = 2;
  optional .chesscom.engine.v1.Score move_score = 1;
  optional bool is_key_moment = 3;
}

message Highlights {
  optional string game_summary = 1;
  optional .chesscom.explanation_engine.v1.Accuracy accuracy = 3;
  optional .chesscom.explanation_engine.v1.ClassificationTallies classification_tallies = 4;
  optional .chesscom.explanation_engine.v1.GameReviewReportCard repo
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03782"></a>
## FND-03782: message declaration: chesscom.explanation_engine.v1.Highlights

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Highlights {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 952.

```text
ion = 2;
  optional .chesscom.engine.v1.Score move_score = 1;
  optional bool is_key_moment = 3;
}

message Highlights {
  optional string game_summary = 1;
  optional .chesscom.explanation_engine.v1.Accuracy accuracy = 3;
  optional .chesscom.explanation_engine.v1.ClassificationTallies classification_tallies = 4;
  optional .chesscom.explanation_engine.v1.GameReviewReportCard report_card = 5;
  optional .chesscom.ex
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03783"></a>
## FND-03783: chesscom.explanation_engine.v1.Highlights.game_summary = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_summary = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 975.

```text
esscom.engine.v1.Score move_score = 1;
  optional bool is_key_moment = 3;
}

message Highlights {
  optional string game_summary = 1;
  optional .chesscom.explanation_engine.v1.Accuracy accuracy = 3;
  optional .chesscom.explanation_engine.v1.ClassificationTallies classification_tallies = 4;
  optional .chesscom.explanation_engine.v1.GameReviewReportCard report_card = 5;
  optional .chesscom.explanation_engine.v1.Tak
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03784"></a>
## FND-03784: chesscom.explanation_engine.v1.Highlights.accuracy = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Accuracy accuracy = 3;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1011.

```text
1;
  optional bool is_key_moment = 3;
}

message Highlights {
  optional string game_summary = 1;
  optional .chesscom.explanation_engine.v1.Accuracy accuracy = 3;
  optional .chesscom.explanation_engine.v1.ClassificationTallies classification_tallies = 4;
  optional .chesscom.explanation_engine.v1.GameReviewReportCard report_card = 5;
  optional .chesscom.explanation_engine.v1.Takeaways takeaways = 6;
  optional .ch
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03785"></a>
## FND-03785: chesscom.explanation_engine.v1.Highlights.classification_tallies = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.ClassificationTallies classification_tallies = 4;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1077.

```text
tional string game_summary = 1;
  optional .chesscom.explanation_engine.v1.Accuracy accuracy = 3;
  optional .chesscom.explanation_engine.v1.ClassificationTallies classification_tallies = 4;
  optional .chesscom.explanation_engine.v1.GameReviewReportCard report_card = 5;
  optional .chesscom.explanation_engine.v1.Takeaways takeaways = 6;
  optional .chesscom.explanation_engine.v1.CoachEmotion game_summary_coach_emoti
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03786"></a>
## FND-03786: chesscom.explanation_engine.v1.Highlights.report_card = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GameReviewReportCard report_card = 5;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1170.

```text
= 3;
  optional .chesscom.explanation_engine.v1.ClassificationTallies classification_tallies = 4;
  optional .chesscom.explanation_engine.v1.GameReviewReportCard report_card = 5;
  optional .chesscom.explanation_engine.v1.Takeaways takeaways = 6;
  optional .chesscom.explanation_engine.v1.CoachEmotion game_summary_coach_emotion = 7;
  optional string game_summary_play = 8;
}

message ClassificationTallies {
  repeate
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03787"></a>
## FND-03787: chesscom.explanation_engine.v1.Highlights.takeaways = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Takeaways takeaways = 6;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1251.

```text
ion_tallies = 4;
  optional .chesscom.explanation_engine.v1.GameReviewReportCard report_card = 5;
  optional .chesscom.explanation_engine.v1.Takeaways takeaways = 6;
  optional .chesscom.explanation_engine.v1.CoachEmotion game_summary_coach_emotion = 7;
  optional string game_summary_play = 8;
}

message ClassificationTallies {
  repeated .chesscom.explanation_engine.v1.ClassificationTally white = 1;
  repeated .ches
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03788"></a>
## FND-03788: chesscom.explanation_engine.v1.Highlights.game_summary_coach_emotion = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CoachEmotion game_summary_coach_emotion = 7;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1319.

```text
ewReportCard report_card = 5;
  optional .chesscom.explanation_engine.v1.Takeaways takeaways = 6;
  optional .chesscom.explanation_engine.v1.CoachEmotion game_summary_coach_emotion = 7;
  optional string game_summary_play = 8;
}

message ClassificationTallies {
  repeated .chesscom.explanation_engine.v1.ClassificationTally white = 1;
  repeated .chesscom.explanation_engine.v1.ClassificationTally black = 2;
}

message
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03789"></a>
## FND-03789: chesscom.explanation_engine.v1.Highlights.game_summary_play = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_summary_play = 8;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1407.

```text
ways = 6;
  optional .chesscom.explanation_engine.v1.CoachEmotion game_summary_coach_emotion = 7;
  optional string game_summary_play = 8;
}

message ClassificationTallies {
  repeated .chesscom.explanation_engine.v1.ClassificationTally white = 1;
  repeated .chesscom.explanation_engine.v1.ClassificationTally black = 2;
}

message GameReviewReportCard {
  optional .chesscom.explanation_engine.v1.GameReviewPlayerRepor
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03790"></a>
## FND-03790: message declaration: chesscom.explanation_engine.v1.ClassificationTallies

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ClassificationTallies {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1449.

```text
_engine.v1.CoachEmotion game_summary_coach_emotion = 7;
  optional string game_summary_play = 8;
}

message ClassificationTallies {
  repeated .chesscom.explanation_engine.v1.ClassificationTally white = 1;
  repeated .chesscom.explanation_engine.v1.ClassificationTally black = 2;
}

message GameReviewReportCard {
  optional .chesscom.explanation_engine.v1.GameReviewPlayerReportCard white = 1;
  optional .chesscom.expl
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03791"></a>
## FND-03791: chesscom.explanation_engine.v1.ClassificationTallies.white = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.ClassificationTally white = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1483.

```text
ry_coach_emotion = 7;
  optional string game_summary_play = 8;
}

message ClassificationTallies {
  repeated .chesscom.explanation_engine.v1.ClassificationTally white = 1;
  repeated .chesscom.explanation_engine.v1.ClassificationTally black = 2;
}

message GameReviewReportCard {
  optional .chesscom.explanation_engine.v1.GameReviewPlayerReportCard white = 1;
  optional .chesscom.explanation_engine.v1.GameReviewPlayer
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03792"></a>
## FND-03792: chesscom.explanation_engine.v1.ClassificationTallies.black = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.ClassificationTally black = 2;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1557.

```text
ClassificationTallies {
  repeated .chesscom.explanation_engine.v1.ClassificationTally white = 1;
  repeated .chesscom.explanation_engine.v1.ClassificationTally black = 2;
}

message GameReviewReportCard {
  optional .chesscom.explanation_engine.v1.GameReviewPlayerReportCard white = 1;
  optional .chesscom.explanation_engine.v1.GameReviewPlayerReportCard black = 2;
  optional string speech = 3;
}

message Accuracy {

```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03793"></a>
## FND-03793: message declaration: chesscom.explanation_engine.v1.GameReviewReportCard

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewReportCard {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1632.

```text
cationTally white = 1;
  repeated .chesscom.explanation_engine.v1.ClassificationTally black = 2;
}

message GameReviewReportCard {
  optional .chesscom.explanation_engine.v1.GameReviewPlayerReportCard white = 1;
  optional .chesscom.explanation_engine.v1.GameReviewPlayerReportCard black = 2;
  optional string speech = 3;
}

message Accuracy {
  optional float white = 1;
  optional float black = 2;
}

message Classifi
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03794"></a>
## FND-03794: chesscom.explanation_engine.v1.GameReviewReportCard.white = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GameReviewPlayerReportCard white = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1665.

```text
 .chesscom.explanation_engine.v1.ClassificationTally black = 2;
}

message GameReviewReportCard {
  optional .chesscom.explanation_engine.v1.GameReviewPlayerReportCard white = 1;
  optional .chesscom.explanation_engine.v1.GameReviewPlayerReportCard black = 2;
  optional string speech = 3;
}

message Accuracy {
  optional float white = 1;
  optional float black = 2;
}

message ClassificationTally {
  optional .chessco
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03795"></a>
## FND-03795: chesscom.explanation_engine.v1.GameReviewReportCard.black = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GameReviewPlayerReportCard black = 2;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1746.

```text
viewReportCard {
  optional .chesscom.explanation_engine.v1.GameReviewPlayerReportCard white = 1;
  optional .chesscom.explanation_engine.v1.GameReviewPlayerReportCard black = 2;
  optional string speech = 3;
}

message Accuracy {
  optional float white = 1;
  optional float black = 2;
}

message ClassificationTally {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional in
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03796"></a>
## FND-03796: chesscom.explanation_engine.v1.GameReviewReportCard.speech = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string speech = 3;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1827.

```text
tCard white = 1;
  optional .chesscom.explanation_engine.v1.GameReviewPlayerReportCard black = 2;
  optional string speech = 3;
}

message Accuracy {
  optional float white = 1;
  optional float black = 2;
}

message ClassificationTally {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 tally = 2;
}

message GameReviewPlayerReportCard {
  oneof _game_rating_v2 {

```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03797"></a>
## FND-03797: message declaration: chesscom.explanation_engine.v1.Accuracy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Accuracy {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1858.

```text
esscom.explanation_engine.v1.GameReviewPlayerReportCard black = 2;
  optional string speech = 3;
}

message Accuracy {
  optional float white = 1;
  optional float black = 2;
}

message ClassificationTally {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 tally = 2;
}

message GameReviewPlayerReportCard {
  oneof _game_rating_v2 {
  int32 game_rating_v2 = 5;
  }
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03798"></a>
## FND-03798: chesscom.explanation_engine.v1.Accuracy.white = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float white = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1879.

```text
gine.v1.GameReviewPlayerReportCard black = 2;
  optional string speech = 3;
}

message Accuracy {
  optional float white = 1;
  optional float black = 2;
}

message ClassificationTally {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 tally = 2;
}

message GameReviewPlayerReportCard {
  oneof _game_rating_v2 {
  int32 game_rating_v2 = 5;
  }
  repeated .chesscom
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03799"></a>
## FND-03799: chesscom.explanation_engine.v1.Accuracy.black = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float black = 2;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1907.

```text
rtCard black = 2;
  optional string speech = 3;
}

message Accuracy {
  optional float white = 1;
  optional float black = 2;
}

message ClassificationTally {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 tally = 2;
}

message GameReviewPlayerReportCard {
  oneof _game_rating_v2 {
  int32 game_rating_v2 = 5;
  }
  repeated .chesscom.explanation_engine.v1.GameP
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03800"></a>
## FND-03800: message declaration: chesscom.explanation_engine.v1.ClassificationTally

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ClassificationTally {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1936.

```text
string speech = 3;
}

message Accuracy {
  optional float white = 1;
  optional float black = 2;
}

message ClassificationTally {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 tally = 2;
}

message GameReviewPlayerReportCard {
  oneof _game_rating_v2 {
  int32 game_rating_v2 = 5;
  }
  repeated .chesscom.explanation_engine.v1.GamePhaseReportCard reports_by_pha
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03801"></a>
## FND-03801: chesscom.explanation_engine.v1.ClassificationTally.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 1968.

```text
curacy {
  optional float white = 1;
  optional float black = 2;
}

message ClassificationTally {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 tally = 2;
}

message GameReviewPlayerReportCard {
  oneof _game_rating_v2 {
  int32 game_rating_v2 = 5;
  }
  repeated .chesscom.explanation_engine.v1.GamePhaseReportCard reports_by_phase = 1;
  repeated .chesscom.exp
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03802"></a>
## FND-03802: chesscom.explanation_engine.v1.ClassificationTally.tally = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 tally = 2;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2055.

```text
ionTally {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 tally = 2;
}

message GameReviewPlayerReportCard {
  oneof _game_rating_v2 {
  int32 game_rating_v2 = 5;
  }
  repeated .chesscom.explanation_engine.v1.GamePhaseReportCard reports_by_phase = 1;
  repeated .chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard reports_by_category = 2;
  optional i
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03803"></a>
## FND-03803: message declaration: chesscom.explanation_engine.v1.GameReviewPlayerReportCard

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewPlayerReportCard {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2084.

```text
om.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 tally = 2;
}

message GameReviewPlayerReportCard {
  oneof _game_rating_v2 {
  int32 game_rating_v2 = 5;
  }
  repeated .chesscom.explanation_engine.v1.GamePhaseReportCard reports_by_phase = 1;
  repeated .chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard reports_by_category = 2;
  optional int32 effective_rating = 4;
}

```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03804"></a>
## FND-03804: oneof declaration: chesscom.explanation_engine.v1.GameReviewPlayerReportCard._game_rating_v2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_rating_v2 {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2123.

```text
tion move_classification = 1;
  optional int32 tally = 2;
}

message GameReviewPlayerReportCard {
  oneof _game_rating_v2 {
  int32 game_rating_v2 = 5;
  }
  repeated .chesscom.explanation_engine.v1.GamePhaseReportCard reports_by_phase = 1;
  repeated .chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard reports_by_category = 2;
  optional int32 effective_rating = 4;
}

message GamePhaseReportCard {
  option
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03805"></a>
## FND-03805: chesscom.explanation_engine.v1.GameReviewPlayerReportCard.game_rating_v2 = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 game_rating_v2 = 5;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2149.

```text
 1;
  optional int32 tally = 2;
}

message GameReviewPlayerReportCard {
  oneof _game_rating_v2 {
  int32 game_rating_v2 = 5;
  }
  repeated .chesscom.explanation_engine.v1.GamePhaseReportCard reports_by_phase = 1;
  repeated .chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard reports_by_category = 2;
  optional int32 effective_rating = 4;
}

message GamePhaseReportCard {
  optional .chesscom.explanation_e
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03806"></a>
## FND-03806: chesscom.explanation_engine.v1.GameReviewPlayerReportCard.reports_by_phase = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GamePhaseReportCard reports_by_phase = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2181.

```text
}

message GameReviewPlayerReportCard {
  oneof _game_rating_v2 {
  int32 game_rating_v2 = 5;
  }
  repeated .chesscom.explanation_engine.v1.GamePhaseReportCard reports_by_phase = 1;
  repeated .chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard reports_by_category = 2;
  optional int32 effective_rating = 4;
}

message GamePhaseReportCard {
  optional .chesscom.explanation_engine.v1.MoveClassification accu
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03807"></a>
## FND-03807: chesscom.explanation_engine.v1.GameReviewPlayerReportCard.reports_by_category = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard reports_by_category = 2;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2266.

```text
_v2 = 5;
  }
  repeated .chesscom.explanation_engine.v1.GamePhaseReportCard reports_by_phase = 1;
  repeated .chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard reports_by_category = 2;
  optional int32 effective_rating = 4;
}

message GamePhaseReportCard {
  optional .chesscom.explanation_engine.v1.MoveClassification accuracy_glyph = 1;
  optional .chesscom.chess.v1.GamePhase phase = 2;
  optional float a
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03808"></a>
## FND-03808: chesscom.explanation_engine.v1.GameReviewPlayerReportCard.effective_rating = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 effective_rating = 4;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2365.

```text
 repeated .chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard reports_by_category = 2;
  optional int32 effective_rating = 4;
}

message GamePhaseReportCard {
  optional .chesscom.explanation_engine.v1.MoveClassification accuracy_glyph = 1;
  optional .chesscom.chess.v1.GamePhase phase = 2;
  optional float accuracy = 3;
}

message AdvancedStatCategoryReportCard {
  optional .chesscom.stats.v1.AdvancedStat
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03809"></a>
## FND-03809: message declaration: chesscom.explanation_engine.v1.GamePhaseReportCard

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GamePhaseReportCard {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2405.

```text
1.AdvancedStatCategoryReportCard reports_by_category = 2;
  optional int32 effective_rating = 4;
}

message GamePhaseReportCard {
  optional .chesscom.explanation_engine.v1.MoveClassification accuracy_glyph = 1;
  optional .chesscom.chess.v1.GamePhase phase = 2;
  optional float accuracy = 3;
}

message AdvancedStatCategoryReportCard {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03810"></a>
## FND-03810: chesscom.explanation_engine.v1.GamePhaseReportCard.accuracy_glyph = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification accuracy_glyph = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2437.

```text
 reports_by_category = 2;
  optional int32 effective_rating = 4;
}

message GamePhaseReportCard {
  optional .chesscom.explanation_engine.v1.MoveClassification accuracy_glyph = 1;
  optional .chesscom.chess.v1.GamePhase phase = 2;
  optional float accuracy = 3;
}

message AdvancedStatCategoryReportCard {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1.MoveClassi
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03811"></a>
## FND-03811: chesscom.explanation_engine.v1.GamePhaseReportCard.phase = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.GamePhase phase = 2;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2519.

```text
aseReportCard {
  optional .chesscom.explanation_engine.v1.MoveClassification accuracy_glyph = 1;
  optional .chesscom.chess.v1.GamePhase phase = 2;
  optional float accuracy = 3;
}

message AdvancedStatCategoryReportCard {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification performance = 2;
  optional int32 new_rating = 3;
  optional int32 rating
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03812"></a>
## FND-03812: chesscom.explanation_engine.v1.GamePhaseReportCard.accuracy = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float accuracy = 3;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2570.

```text
gine.v1.MoveClassification accuracy_glyph = 1;
  optional .chesscom.chess.v1.GamePhase phase = 2;
  optional float accuracy = 3;
}

message AdvancedStatCategoryReportCard {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification performance = 2;
  optional int32 new_rating = 3;
  optional int32 rating_change = 4;
}

message Review {
  optional string 
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03813"></a>
## FND-03813: message declaration: chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AdvancedStatCategoryReportCard {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2602.

```text
acy_glyph = 1;
  optional .chesscom.chess.v1.GamePhase phase = 2;
  optional float accuracy = 3;
}

message AdvancedStatCategoryReportCard {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification performance = 2;
  optional int32 new_rating = 3;
  optional int32 rating_change = 4;
}

message Review {
  optional string game_summary = 1;
  optional str
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03814"></a>
## FND-03814: chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard.category = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.stats.v1.AdvancedStatType category = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2645.

```text
1.GamePhase phase = 2;
  optional float accuracy = 3;
}

message AdvancedStatCategoryReportCard {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification performance = 2;
  optional int32 new_rating = 3;
  optional int32 rating_change = 4;
}

message Review {
  optional string game_summary = 1;
  optional string starting_fen = 2;
  repeated .chesscom.
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03815"></a>
## FND-03815: chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard.performance = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification performance = 2;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2706.

```text
age AdvancedStatCategoryReportCard {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification performance = 2;
  optional int32 new_rating = 3;
  optional int32 rating_change = 4;
}

message Review {
  optional string game_summary = 1;
  optional string starting_fen = 2;
  repeated .chesscom.explanation_engine.v1.PlayedMove played_moves = 3;
  optional
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03816"></a>
## FND-03816: chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard.new_rating = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 new_rating = 3;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2785.

```text
Type category = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification performance = 2;
  optional int32 new_rating = 3;
  optional int32 rating_change = 4;
}

message Review {
  optional string game_summary = 1;
  optional string starting_fen = 2;
  repeated .chesscom.explanation_engine.v1.PlayedMove played_moves = 3;
  optional string final_fen = 4;
}

message PlayedMove {
  oneof _best_alternative_move {
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03817"></a>
## FND-03817: chesscom.explanation_engine.v1.AdvancedStatCategoryReportCard.rating_change = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 rating_change = 4;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2818.

```text
esscom.explanation_engine.v1.MoveClassification performance = 2;
  optional int32 new_rating = 3;
  optional int32 rating_change = 4;
}

message Review {
  optional string game_summary = 1;
  optional string starting_fen = 2;
  repeated .chesscom.explanation_engine.v1.PlayedMove played_moves = 3;
  optional string final_fen = 4;
}

message PlayedMove {
  oneof _best_alternative_move {
  .chesscom.explanation_engine.v
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03818"></a>
## FND-03818: message declaration: chesscom.explanation_engine.v1.Review

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Review {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2855.

```text
sification performance = 2;
  optional int32 new_rating = 3;
  optional int32 rating_change = 4;
}

message Review {
  optional string game_summary = 1;
  optional string starting_fen = 2;
  repeated .chesscom.explanation_engine.v1.PlayedMove played_moves = 3;
  optional string final_fen = 4;
}

message PlayedMove {
  oneof _best_alternative_move {
  .chesscom.explanation_engine.v1.Move best_alternative_move = 3;
  }
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03819"></a>
## FND-03819: chesscom.explanation_engine.v1.Review.game_summary = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_summary = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 975.

```text
esscom.engine.v1.Score move_score = 1;
  optional bool is_key_moment = 3;
}

message Highlights {
  optional string game_summary = 1;
  optional .chesscom.explanation_engine.v1.Accuracy accuracy = 3;
  optional .chesscom.explanation_engine.v1.ClassificationTallies classification_tallies = 4;
  optional .chesscom.explanation_engine.v1.GameReviewReportCard report_card = 5;
  optional .chesscom.explanation_engine.v1.Tak
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03820"></a>
## FND-03820: chesscom.explanation_engine.v1.Review.starting_fen = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string starting_fen = 2;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2910.

```text
 = 3;
  optional int32 rating_change = 4;
}

message Review {
  optional string game_summary = 1;
  optional string starting_fen = 2;
  repeated .chesscom.explanation_engine.v1.PlayedMove played_moves = 3;
  optional string final_fen = 4;
}

message PlayedMove {
  oneof _best_alternative_move {
  .chesscom.explanation_engine.v1.Move best_alternative_move = 3;
  }
  oneof _best_next_move {
  .chesscom.chess.v1.Move be
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03821"></a>
## FND-03821: chesscom.explanation_engine.v1.Review.played_moves = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.PlayedMove played_moves = 3;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 2946.

```text
 = 4;
}

message Review {
  optional string game_summary = 1;
  optional string starting_fen = 2;
  repeated .chesscom.explanation_engine.v1.PlayedMove played_moves = 3;
  optional string final_fen = 4;
}

message PlayedMove {
  oneof _best_alternative_move {
  .chesscom.explanation_engine.v1.Move best_alternative_move = 3;
  }
  oneof _best_next_move {
  .chesscom.chess.v1.Move best_next_move = 8;
  }
  optional boo
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03822"></a>
## FND-03822: chesscom.explanation_engine.v1.Review.final_fen = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string final_fen = 4;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3018.

```text
 string starting_fen = 2;
  repeated .chesscom.explanation_engine.v1.PlayedMove played_moves = 3;
  optional string final_fen = 4;
}

message PlayedMove {
  oneof _best_alternative_move {
  .chesscom.explanation_engine.v1.Move best_alternative_move = 3;
  }
  oneof _best_next_move {
  .chesscom.chess.v1.Move best_next_move = 8;
  }
  optional bool is_key_moment = 1;
  optional .chesscom.explanation_engine.v1.Move pla
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03823"></a>
## FND-03823: message declaration: chesscom.explanation_engine.v1.PlayedMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayedMove {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3052.

```text
ed .chesscom.explanation_engine.v1.PlayedMove played_moves = 3;
  optional string final_fen = 4;
}

message PlayedMove {
  oneof _best_alternative_move {
  .chesscom.explanation_engine.v1.Move best_alternative_move = 3;
  }
  oneof _best_next_move {
  .chesscom.chess.v1.Move best_next_move = 8;
  }
  optional bool is_key_moment = 1;
  optional .chesscom.explanation_engine.v1.Move played_move = 2;
  optional .chesscom
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03824"></a>
## FND-03824: oneof declaration: chesscom.explanation_engine.v1.PlayedMove._best_alternative_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _best_alternative_move {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3075.

```text
n_engine.v1.PlayedMove played_moves = 3;
  optional string final_fen = 4;
}

message PlayedMove {
  oneof _best_alternative_move {
  .chesscom.explanation_engine.v1.Move best_alternative_move = 3;
  }
  oneof _best_next_move {
  .chesscom.chess.v1.Move best_next_move = 8;
  }
  optional bool is_key_moment = 1;
  optional .chesscom.explanation_engine.v1.Move played_move = 2;
  optional .chesscom.chess.v1.Color moved_c
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03825"></a>
## FND-03825: chesscom.explanation_engine.v1.PlayedMove.best_alternative_move = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.Move best_alternative_move = 3;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3108.

```text
es = 3;
  optional string final_fen = 4;
}

message PlayedMove {
  oneof _best_alternative_move {
  .chesscom.explanation_engine.v1.Move best_alternative_move = 3;
  }
  oneof _best_next_move {
  .chesscom.chess.v1.Move best_next_move = 8;
  }
  optional bool is_key_moment = 1;
  optional .chesscom.explanation_engine.v1.Move played_move = 2;
  optional .chesscom.chess.v1.Color moved_color = 4;
  optional .chesscom.ex
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03826"></a>
## FND-03826: oneof declaration: chesscom.explanation_engine.v1.PlayedMove._best_next_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _best_next_move {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3178.

```text
of _best_alternative_move {
  .chesscom.explanation_engine.v1.Move best_alternative_move = 3;
  }
  oneof _best_next_move {
  .chesscom.chess.v1.Move best_next_move = 8;
  }
  optional bool is_key_moment = 1;
  optional .chesscom.explanation_engine.v1.Move played_move = 2;
  optional .chesscom.chess.v1.Color moved_color = 4;
  optional .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 5;
  optional .chessc
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03827"></a>
## FND-03827: chesscom.explanation_engine.v1.PlayedMove.best_next_move = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Move best_next_move = 8;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3204.

```text
{
  .chesscom.explanation_engine.v1.Move best_alternative_move = 3;
  }
  oneof _best_next_move {
  .chesscom.chess.v1.Move best_next_move = 8;
  }
  optional bool is_key_moment = 1;
  optional .chesscom.explanation_engine.v1.Move played_move = 2;
  optional .chesscom.chess.v1.Color moved_color = 4;
  optional .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 5;
  optional .chesscom.explanation_engine.v1.S
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03828"></a>
## FND-03828: chesscom.explanation_engine.v1.PlayedMove.is_key_moment = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_key_moment = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3254.

```text
rnative_move = 3;
  }
  oneof _best_next_move {
  .chesscom.chess.v1.Move best_next_move = 8;
  }
  optional bool is_key_moment = 1;
  optional .chesscom.explanation_engine.v1.Move played_move = 2;
  optional .chesscom.chess.v1.Color moved_color = 4;
  optional .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 5;
  optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 6;
  repeated .chess
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03829"></a>
## FND-03829: chesscom.explanation_engine.v1.PlayedMove.played_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Move played_move = 2;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3289.

```text
_next_move {
  .chesscom.chess.v1.Move best_next_move = 8;
  }
  optional bool is_key_moment = 1;
  optional .chesscom.explanation_engine.v1.Move played_move = 2;
  optional .chesscom.chess.v1.Color moved_color = 4;
  optional .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 5;
  optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 6;
  repeated .chesscom.explanation_engine.v1.PlayedMov
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03830"></a>
## FND-03830: chesscom.explanation_engine.v1.PlayedMove.moved_color = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Color moved_color = 4;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3354.

```text
optional bool is_key_moment = 1;
  optional .chesscom.explanation_engine.v1.Move played_move = 2;
  optional .chesscom.chess.v1.Color moved_color = 4;
  optional .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 5;
  optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 6;
  repeated .chesscom.explanation_engine.v1.PlayedMove explain_line = 7;
}

message Move {
  optional .chesscom.chess.
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03831"></a>
## FND-03831: chesscom.explanation_engine.v1.PlayedMove.coach_emotion = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 5;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3407.

```text
.explanation_engine.v1.Move played_move = 2;
  optional .chesscom.chess.v1.Color moved_color = 4;
  optional .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 5;
  optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 6;
  repeated .chesscom.explanation_engine.v1.PlayedMove explain_line = 7;
}

message Move {
  optional .chesscom.chess.v1.Move move = 1;
  optional .chesscom.explanation_en
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03832"></a>
## FND-03832: chesscom.explanation_engine.v1.PlayedMove.skills_earned = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 6;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3482.

```text
Color moved_color = 4;
  optional .chesscom.explanation_engine.v1.CoachEmotion coach_emotion = 5;
  optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 6;
  repeated .chesscom.explanation_engine.v1.PlayedMove explain_line = 7;
}

message Move {
  optional .chesscom.chess.v1.Move move = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional .chesscom.en
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03833"></a>
## FND-03833: chesscom.explanation_engine.v1.PlayedMove.explain_line = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.PlayedMove explain_line = 7;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3559.

```text
n coach_emotion = 5;
  optional .chesscom.explanation_engine.v1.SkillsPosition skills_earned = 6;
  repeated .chesscom.explanation_engine.v1.PlayedMove explain_line = 7;
}

message Move {
  optional .chesscom.chess.v1.Move move = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional .chesscom.engine.v1.Score score = 4;
  optional .chesscom.explanation_engine.v1.Speech sp
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03834"></a>
## FND-03834: message declaration: chesscom.explanation_engine.v1.Move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Move {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3632.

```text
ition skills_earned = 6;
  repeated .chesscom.explanation_engine.v1.PlayedMove explain_line = 7;
}

message Move {
  optional .chesscom.chess.v1.Move move = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional .chesscom.engine.v1.Score score = 4;
  optional .chesscom.explanation_engine.v1.Speech speech = 5;
  repeated .chesscom.explanation_engine.v1.ShowMoves show_moves
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03835"></a>
## FND-03835: chesscom.explanation_engine.v1.Move.move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move move = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3649.

```text
ed = 6;
  repeated .chesscom.explanation_engine.v1.PlayedMove explain_line = 7;
}

message Move {
  optional .chesscom.chess.v1.Move move = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional .chesscom.engine.v1.Score score = 4;
  optional .chesscom.explanation_engine.v1.Speech speech = 5;
  repeated .chesscom.explanation_engine.v1.ShowMoves show_moves_buttons = 6;
  o
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03836"></a>
## FND-03836: chesscom.explanation_engine.v1.Move.move_classification = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3694.

```text
ne.v1.PlayedMove explain_line = 7;
}

message Move {
  optional .chesscom.chess.v1.Move move = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional .chesscom.engine.v1.Score score = 4;
  optional .chesscom.explanation_engine.v1.Speech speech = 5;
  repeated .chesscom.explanation_engine.v1.ShowMoves show_moves_buttons = 6;
  optional .chesscom.chess.v1.BoardMarkings boar
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03837"></a>
## FND-03837: chesscom.explanation_engine.v1.Move.score = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.engine.v1.Score score = 4;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3781.

```text
 move = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional .chesscom.engine.v1.Score score = 4;
  optional .chesscom.explanation_engine.v1.Speech speech = 5;
  repeated .chesscom.explanation_engine.v1.ShowMoves show_moves_buttons = 6;
  optional .chesscom.chess.v1.BoardMarkings board_markings = 7;
}

message ShowMoves {
  repeated .chesscom.chess.v1.Move moves_to_show
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03838"></a>
## FND-03838: chesscom.explanation_engine.v1.Move.speech = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech speech = 5;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3829.

```text
ne.v1.MoveClassification move_classification = 3;
  optional .chesscom.engine.v1.Score score = 4;
  optional .chesscom.explanation_engine.v1.Speech speech = 5;
  repeated .chesscom.explanation_engine.v1.ShowMoves show_moves_buttons = 6;
  optional .chesscom.chess.v1.BoardMarkings board_markings = 7;
}

message ShowMoves {
  repeated .chesscom.chess.v1.Move moves_to_show = 1;
  optional string show_text = 2;
  optiona
```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03839"></a>
## FND-03839: chesscom.explanation_engine.v1.Move.show_moves_buttons = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.ShowMoves show_moves_buttons = 6;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3891.

```text
chesscom.engine.v1.Score score = 4;
  optional .chesscom.explanation_engine.v1.Speech speech = 5;
  repeated .chesscom.explanation_engine.v1.ShowMoves show_moves_buttons = 6;
  optional .chesscom.chess.v1.BoardMarkings board_markings = 7;
}

message ShowMoves {
  repeated .chesscom.chess.v1.Move moves_to_show = 1;
  optional string show_text = 2;
  optional string hide_text = 3;
}

```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03840"></a>
## FND-03840: chesscom.explanation_engine.v1.Move.board_markings = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.BoardMarkings board_markings = 7;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 3968.

```text
1.Speech speech = 5;
  repeated .chesscom.explanation_engine.v1.ShowMoves show_moves_buttons = 6;
  optional .chesscom.chess.v1.BoardMarkings board_markings = 7;
}

message ShowMoves {
  repeated .chesscom.chess.v1.Move moves_to_show = 1;
  optional string show_text = 2;
  optional string hide_text = 3;
}

```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03841"></a>
## FND-03841: message declaration: chesscom.explanation_engine.v1.ShowMoves

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ShowMoves {

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 4033.

```text
howMoves show_moves_buttons = 6;
  optional .chesscom.chess.v1.BoardMarkings board_markings = 7;
}

message ShowMoves {
  repeated .chesscom.chess.v1.Move moves_to_show = 1;
  optional string show_text = 2;
  optional string hide_text = 3;
}

```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03842"></a>
## FND-03842: chesscom.explanation_engine.v1.ShowMoves.moves_to_show = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Move moves_to_show = 1;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 4055.

```text
ttons = 6;
  optional .chesscom.chess.v1.BoardMarkings board_markings = 7;
}

message ShowMoves {
  repeated .chesscom.chess.v1.Move moves_to_show = 1;
  optional string show_text = 2;
  optional string hide_text = 3;
}

```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03843"></a>
## FND-03843: chesscom.explanation_engine.v1.ShowMoves.show_text = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string show_text = 2;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 4109.

```text
 board_markings = 7;
}

message ShowMoves {
  repeated .chesscom.chess.v1.Move moves_to_show = 1;
  optional string show_text = 2;
  optional string hide_text = 3;
}

```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03844"></a>
## FND-03844: chesscom.explanation_engine.v1.ShowMoves.hide_text = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string hide_text = 3;

### Evidence

- **SRC-0405** `research/proto/chesscom/explanation_engine/v1/game_review.proto` — [preserved redacted evidence](../evidence/text/9fc05cae68afbe111b201c912c315bf543489ef4f0349ded568654e1b8fd4cf0.proto)
  Character offset 4142.

```text
howMoves {
  repeated .chesscom.chess.v1.Move moves_to_show = 1;
  optional string show_text = 2;
  optional string hide_text = 3;
}

```

**Source references:** SRC-0405, SRC-1376  
**URL references:** None independently associated  
**Related findings:** FND-03766, FND-03767, FND-03768

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03845"></a>
## FND-03845: message declaration: chesscom.explanation_engine.v1.GameSettings

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameSettings {

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 122.

```text
planation_engine/v1/game_settings.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GameSettings {
  oneof search {
  .chesscom.explanation_engine.v1.SearchSettings search_settings = 8;
  .chesscom.explanation_engine.v1.GameReviewSearchSettings game_review_search_settings = 9;
  .chesscom.explanation_engine.v1.SearchPreset preset = 13;
  }
  oneof _user_color {
  .chesscom.chess.v1.Color user_
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03846, FND-03847

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03846"></a>
## FND-03846: oneof declaration: chesscom.explanation_engine.v1.GameSettings.search

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof search {

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 147.

```text
settings.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GameSettings {
  oneof search {
  .chesscom.explanation_engine.v1.SearchSettings search_settings = 8;
  .chesscom.explanation_engine.v1.GameReviewSearchSettings game_review_search_settings = 9;
  .chesscom.explanation_engine.v1.SearchPreset preset = 13;
  }
  oneof _user_color {
  .chesscom.chess.v1.Color user_color = 3;
  }
  oneof _l
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03847

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03847"></a>
## FND-03847: chesscom.explanation_engine.v1.GameSettings.search_settings = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.SearchSettings search_settings = 8;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 164.

```text
 syntax: proto3

package chesscom.explanation_engine.v1;

message GameSettings {
  oneof search {
  .chesscom.explanation_engine.v1.SearchSettings search_settings = 8;
  .chesscom.explanation_engine.v1.GameReviewSearchSettings game_review_search_settings = 9;
  .chesscom.explanation_engine.v1.SearchPreset preset = 13;
  }
  oneof _user_color {
  .chesscom.chess.v1.Color user_color = 3;
  }
  oneof _locale {
  .chessc
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03848"></a>
## FND-03848: chesscom.explanation_engine.v1.GameSettings.game_review_search_settings = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.GameReviewSearchSettings game_review_search_settings = 9;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 234.

```text
Settings {
  oneof search {
  .chesscom.explanation_engine.v1.SearchSettings search_settings = 8;
  .chesscom.explanation_engine.v1.GameReviewSearchSettings game_review_search_settings = 9;
  .chesscom.explanation_engine.v1.SearchPreset preset = 13;
  }
  oneof _user_color {
  .chesscom.chess.v1.Color user_color = 3;
  }
  oneof _locale {
  .chesscom.explanation_engine.v1.Locale locale = 4;
  }
  oneof _game_phase_ve
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03849"></a>
## FND-03849: chesscom.explanation_engine.v1.GameSettings.preset = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.SearchPreset preset = 13;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 326.

```text
 = 8;
  .chesscom.explanation_engine.v1.GameReviewSearchSettings game_review_search_settings = 9;
  .chesscom.explanation_engine.v1.SearchPreset preset = 13;
  }
  oneof _user_color {
  .chesscom.chess.v1.Color user_color = 3;
  }
  oneof _locale {
  .chesscom.explanation_engine.v1.Locale locale = 4;
  }
  oneof _game_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 5;
  }
  one
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03850"></a>
## FND-03850: oneof declaration: chesscom.explanation_engine.v1.GameSettings._user_color

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_color {

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 390.

```text
 game_review_search_settings = 9;
  .chesscom.explanation_engine.v1.SearchPreset preset = 13;
  }
  oneof _user_color {
  .chesscom.chess.v1.Color user_color = 3;
  }
  oneof _locale {
  .chesscom.explanation_engine.v1.Locale locale = 4;
  }
  oneof _game_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 5;
  }
  oneof _game_analysis_speech_version {
  .chesscom.explanation_engin
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03851"></a>
## FND-03851: chesscom.explanation_engine.v1.GameSettings.user_color = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Color user_color = 3;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 412.

```text
ttings = 9;
  .chesscom.explanation_engine.v1.SearchPreset preset = 13;
  }
  oneof _user_color {
  .chesscom.chess.v1.Color user_color = 3;
  }
  oneof _locale {
  .chesscom.explanation_engine.v1.Locale locale = 4;
  }
  oneof _game_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 5;
  }
  oneof _game_analysis_speech_version {
  .chesscom.explanation_engine.v1.GameAnalysisSpeec
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03852"></a>
## FND-03852: oneof declaration: chesscom.explanation_engine.v1.GameSettings._locale

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _locale {

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 459.

```text
earchPreset preset = 13;
  }
  oneof _user_color {
  .chesscom.chess.v1.Color user_color = 3;
  }
  oneof _locale {
  .chesscom.explanation_engine.v1.Locale locale = 4;
  }
  oneof _game_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 5;
  }
  oneof _game_analysis_speech_version {
  .chesscom.explanation_engine.v1.GameAnalysisSpeechVersion game_analysis_speech_version = 6;
  }

```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03853"></a>
## FND-03853: chesscom.explanation_engine.v1.GameSettings.locale = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.Locale locale = 4;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 477.

```text
 = 13;
  }
  oneof _user_color {
  .chesscom.chess.v1.Color user_color = 3;
  }
  oneof _locale {
  .chesscom.explanation_engine.v1.Locale locale = 4;
  }
  oneof _game_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 5;
  }
  oneof _game_analysis_speech_version {
  .chesscom.explanation_engine.v1.GameAnalysisSpeechVersion game_analysis_speech_version = 6;
  }
  oneof _move_clas
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03854"></a>
## FND-03854: oneof declaration: chesscom.explanation_engine.v1.GameSettings._game_phase_version

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_phase_version {

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 534.

```text
or user_color = 3;
  }
  oneof _locale {
  .chesscom.explanation_engine.v1.Locale locale = 4;
  }
  oneof _game_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 5;
  }
  oneof _game_analysis_speech_version {
  .chesscom.explanation_engine.v1.GameAnalysisSpeechVersion game_analysis_speech_version = 6;
  }
  oneof _move_classification_version {
  .chesscom.explanation_engine.v1.Mo
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03855"></a>
## FND-03855: chesscom.explanation_engine.v1.GameSettings.game_phase_version = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 5;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 564.

```text
 _locale {
  .chesscom.explanation_engine.v1.Locale locale = 4;
  }
  oneof _game_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 5;
  }
  oneof _game_analysis_speech_version {
  .chesscom.explanation_engine.v1.GameAnalysisSpeechVersion game_analysis_speech_version = 6;
  }
  oneof _move_classification_version {
  .chesscom.explanation_engine.v1.MoveClassificationVersion move_c
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03856"></a>
## FND-03856: oneof declaration: chesscom.explanation_engine.v1.GameSettings._game_analysis_speech_version

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_analysis_speech_version {

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 643.

```text
me_phase_version {
  .chesscom.explanation_engine.v1.GamePhaseVersion game_phase_version = 5;
  }
  oneof _game_analysis_speech_version {
  .chesscom.explanation_engine.v1.GameAnalysisSpeechVersion game_analysis_speech_version = 6;
  }
  oneof _move_classification_version {
  .chesscom.explanation_engine.v1.MoveClassificationVersion move_classification_version = 7;
  }
  oneof _force_disable_internal_engine_searches 
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03857"></a>
## FND-03857: chesscom.explanation_engine.v1.GameSettings.game_analysis_speech_version = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.GameAnalysisSpeechVersion game_analysis_speech_version = 6;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 683.

```text
on_engine.v1.GamePhaseVersion game_phase_version = 5;
  }
  oneof _game_analysis_speech_version {
  .chesscom.explanation_engine.v1.GameAnalysisSpeechVersion game_analysis_speech_version = 6;
  }
  oneof _move_classification_version {
  .chesscom.explanation_engine.v1.MoveClassificationVersion move_classification_version = 7;
  }
  oneof _force_disable_internal_engine_searches {
  bool force_disable_internal_engine_s
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03858"></a>
## FND-03858: oneof declaration: chesscom.explanation_engine.v1.GameSettings._move_classification_version

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _move_classification_version {

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 781.

```text
  .chesscom.explanation_engine.v1.GameAnalysisSpeechVersion game_analysis_speech_version = 6;
  }
  oneof _move_classification_version {
  .chesscom.explanation_engine.v1.MoveClassificationVersion move_classification_version = 7;
  }
  oneof _force_disable_internal_engine_searches {
  bool force_disable_internal_engine_searches = 10;
  }
  oneof _enable_skills {
  bool enable_skills = 14;
  }
  repeated string enable
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03859"></a>
## FND-03859: chesscom.explanation_engine.v1.GameSettings.move_classification_version = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.MoveClassificationVersion move_classification_version = 7;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 820.

```text
nalysisSpeechVersion game_analysis_speech_version = 6;
  }
  oneof _move_classification_version {
  .chesscom.explanation_engine.v1.MoveClassificationVersion move_classification_version = 7;
  }
  oneof _force_disable_internal_engine_searches {
  bool force_disable_internal_engine_searches = 10;
  }
  oneof _enable_skills {
  bool enable_skills = 14;
  }
  repeated string enabled_feature_flags = 11;
  repeated .chess
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03860"></a>
## FND-03860: oneof declaration: chesscom.explanation_engine.v1.GameSettings._force_disable_internal_engine_searches

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _force_disable_internal_engine_searches {

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 917.

```text

  .chesscom.explanation_engine.v1.MoveClassificationVersion move_classification_version = 7;
  }
  oneof _force_disable_internal_engine_searches {
  bool force_disable_internal_engine_searches = 10;
  }
  oneof _enable_skills {
  bool enable_skills = 14;
  }
  repeated string enabled_feature_flags = 11;
  repeated .chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry feature_flag_config = 12;
  message
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03861"></a>
## FND-03861: chesscom.explanation_engine.v1.GameSettings.force_disable_internal_engine_searches = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool force_disable_internal_engine_searches = 10;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 967.

```text
ionVersion move_classification_version = 7;
  }
  oneof _force_disable_internal_engine_searches {
  bool force_disable_internal_engine_searches = 10;
  }
  oneof _enable_skills {
  bool enable_skills = 14;
  }
  repeated string enabled_feature_flags = 11;
  repeated .chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry feature_flag_config = 12;
  message FeatureFlagConfigEntry {
  optional string key = 
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03862"></a>
## FND-03862: oneof declaration: chesscom.explanation_engine.v1.GameSettings._enable_skills

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _enable_skills {

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 1023.

```text
_force_disable_internal_engine_searches {
  bool force_disable_internal_engine_searches = 10;
  }
  oneof _enable_skills {
  bool enable_skills = 14;
  }
  repeated string enabled_feature_flags = 11;
  repeated .chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry feature_flag_config = 12;
  message FeatureFlagConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message SearchSet
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03863"></a>
## FND-03863: chesscom.explanation_engine.v1.GameSettings.enable_skills = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool enable_skills = 14;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 1048.

```text
ngine_searches {
  bool force_disable_internal_engine_searches = 10;
  }
  oneof _enable_skills {
  bool enable_skills = 14;
  }
  repeated string enabled_feature_flags = 11;
  repeated .chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry feature_flag_config = 12;
  message FeatureFlagConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message SearchSettings {
  optional .chess
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03864"></a>
## FND-03864: chesscom.explanation_engine.v1.GameSettings.enabled_feature_flags = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string enabled_feature_flags = 11;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 1079.

```text
isable_internal_engine_searches = 10;
  }
  oneof _enable_skills {
  bool enable_skills = 14;
  }
  repeated string enabled_feature_flags = 11;
  repeated .chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry feature_flag_config = 12;
  message FeatureFlagConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message SearchSettings {
  optional .chesscom.explanation_engine.v1.Searc
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03865"></a>
## FND-03865: chesscom.explanation_engine.v1.GameSettings.feature_flag_config = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry feature_flag_config = 12;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 1125.

```text
eof _enable_skills {
  bool enable_skills = 14;
  }
  repeated string enabled_feature_flags = 11;
  repeated .chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry feature_flag_config = 12;
  message FeatureFlagConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message SearchSettings {
  optional .chesscom.explanation_engine.v1.SearchParameters search_parameters = 1;
  optional 
```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03866"></a>
## FND-03866: message declaration: chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FeatureFlagConfigEntry {

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 1230.

```text
ted .chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry feature_flag_config = 12;
  message FeatureFlagConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message SearchSettings {
  optional .chesscom.explanation_engine.v1.SearchParameters search_parameters = 1;
  optional .chesscom.explanation_engine.v1.SearchParameters null_move_search_parameters = 2;
}

```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03867"></a>
## FND-03867: chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 1265.

```text
.GameSettings.FeatureFlagConfigEntry feature_flag_config = 12;
  message FeatureFlagConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message SearchSettings {
  optional .chesscom.explanation_engine.v1.SearchParameters search_parameters = 1;
  optional .chesscom.explanation_engine.v1.SearchParameters null_move_search_parameters = 2;
}

```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03868"></a>
## FND-03868: chesscom.explanation_engine.v1.GameSettings.FeatureFlagConfigEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 1292.

```text
nfigEntry feature_flag_config = 12;
  message FeatureFlagConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message SearchSettings {
  optional .chesscom.explanation_engine.v1.SearchParameters search_parameters = 1;
  optional .chesscom.explanation_engine.v1.SearchParameters null_move_search_parameters = 2;
}

```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03869"></a>
## FND-03869: message declaration: chesscom.explanation_engine.v1.SearchSettings

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SearchSettings {

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 1326.

```text
;
  message FeatureFlagConfigEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message SearchSettings {
  optional .chesscom.explanation_engine.v1.SearchParameters search_parameters = 1;
  optional .chesscom.explanation_engine.v1.SearchParameters null_move_search_parameters = 2;
}

```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03870"></a>
## FND-03870: chesscom.explanation_engine.v1.SearchSettings.search_parameters = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.SearchParameters search_parameters = 1;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 1353.

```text
igEntry {
  optional string key = 1;
  optional string value = 2;
  }
}

message SearchSettings {
  optional .chesscom.explanation_engine.v1.SearchParameters search_parameters = 1;
  optional .chesscom.explanation_engine.v1.SearchParameters null_move_search_parameters = 2;
}

```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03871"></a>
## FND-03871: chesscom.explanation_engine.v1.SearchSettings.null_move_search_parameters = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.SearchParameters null_move_search_parameters = 2;

### Evidence

- **SRC-0406** `research/proto/chesscom/explanation_engine/v1/game_settings.proto` — [preserved redacted evidence](../evidence/text/35a295ef15e97658494692fbda49dd5765cad7be00b1743791c2a57fe82c3c0f.proto)
  Character offset 1436.

```text
archSettings {
  optional .chesscom.explanation_engine.v1.SearchParameters search_parameters = 1;
  optional .chesscom.explanation_engine.v1.SearchParameters null_move_search_parameters = 2;
}

```

**Source references:** SRC-0406, SRC-1377  
**URL references:** None independently associated  
**Related findings:** FND-03845, FND-03846, FND-03847

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03872"></a>
## FND-03872: enum declaration: chesscom.explanation_engine.v1.NodeFlag

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum NodeFlag {

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 119.

```text
/explanation_engine/v1/game_state.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

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
 
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03873, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03873"></a>
## FND-03873: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NODE_FLAG_UNSPECIFIED = 0;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 137.

```text
e/v1/game_state.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

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
  optional .chessco
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03874

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03874"></a>
## FND-03874: chesscom.explanation_engine.v1.NodeFlag.NODE_FLAG_PLAYED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NODE_FLAG_PLAYED = 1;

### Evidence

- **SRC-0407** `research/proto/chesscom/explanation_engine/v1/game_state.proto` — [preserved redacted evidence](../evidence/text/f168c5474edbd0e7764f44a22d3afe612ff7b18946d6a46733816803b0807ff1.proto)
  Character offset 166.

```text
ax: proto3

package chesscom.explanation_engine.v1;

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
  optional .chesscom.api.v1.SemanticVersion game
```

**Source references:** SRC-0407, SRC-1378  
**URL references:** None independently associated  
**Related findings:** FND-03872, FND-03873

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
