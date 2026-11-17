# data_models — findings 5101–5200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-05375"></a>
## FND-05375: chesscom.game_review.v2.GameReviewMoveClassificationClicked.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6869.

```text
nEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClassificationsExpandClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassifi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05376"></a>
## FND-05376: message declaration: chesscom.game_review.v2.GameReviewStartGameClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewStartGameClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7483.

```text
 = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameTy
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05377"></a>
## FND-05377: oneof declaration: chesscom.game_review.v2.GameReviewStartGameClicked._game_review_screen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_review_screen {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6518.

```text
esscom.game_review.v2.GameReviewResult result = 1;
  }
}

message GameReviewSelfAnalysisClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional int32 percent_reviewed = 3;
}

message GameReviewOverviewScreenEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.Game
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05378"></a>
## FND-05378: chesscom.game_review.v2.GameReviewStartGameClicked.game_review_screen = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7552.

```text
on move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;
}

message GameReviewMoveFeedbackButtonClicked {
  
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05379"></a>
## FND-05379: oneof declaration: chesscom.game_review.v2.GameReviewStartGameClicked._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05380"></a>
## FND-05380: chesscom.game_review.v2.GameReviewStartGameClicked.result = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7642.

```text
creen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;
}

message GameReviewMoveFeedbackButtonClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_oppon
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05381"></a>
## FND-05381: chesscom.game_review.v2.GameReviewStartGameClicked.time_class = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.TimeClass time_class = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7702.

```text
iew_screen = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;
}

message GameReviewMoveFeedbackButtonClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05382"></a>
## FND-05382: chesscom.game_review.v2.GameReviewStartGameClicked.game_type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7758.

```text
eview.v2.GameReviewResult result = 4;
  }
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;
}

message GameReviewMoveFeedbackButtonClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05383"></a>
## FND-05383: message declaration: chesscom.game_review.v2.GameReviewMoveFeedbackButtonClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewMoveFeedbackButtonClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7824.

```text
ss.v1.TimeClass time_class = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;
}

message GameReviewMoveFeedbackButtonClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05384"></a>
## FND-05384: oneof declaration: chesscom.game_review.v2.GameReviewMoveFeedbackButtonClicked._user_or_opponent_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_or_opponent_move {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7207.

```text
result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05385"></a>
## FND-05385: chesscom.game_review.v2.GameReviewMoveFeedbackButtonClicked.user_or_opponent_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7240.

```text
s_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chessco
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05386"></a>
## FND-05386: oneof declaration: chesscom.game_review.v2.GameReviewMoveFeedbackButtonClicked._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05387"></a>
## FND-05387: chesscom.game_review.v2.GameReviewMoveFeedbackButtonClicked.result = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7642.

```text
creen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;
}

message GameReviewMoveFeedbackButtonClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_oppon
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05388"></a>
## FND-05388: chesscom.game_review.v2.GameReviewMoveFeedbackButtonClicked.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6869.

```text
nEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClassificationsExpandClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassifi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05389"></a>
## FND-05389: chesscom.game_review.v2.GameReviewMoveFeedbackButtonClicked.button_name = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewMoveFeedbackButton button_name = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8147.

```text
t = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional .chesscom.game_review.v2.GameReviewMoveFeedbackButton button_name = 3;
  optional int32 percent_reviewed = 5;
}

message GameReviewMovesMoveNodeClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.Ga
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05390"></a>
## FND-05390: chesscom.game_review.v2.GameReviewMoveFeedbackButtonClicked.percent_reviewed = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8229.

```text
sification = 1;
  optional .chesscom.game_review.v2.GameReviewMoveFeedbackButton button_name = 3;
  optional int32 percent_reviewed = 5;
}

message GameReviewMovesMoveNodeClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClas
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05391"></a>
## FND-05391: message declaration: chesscom.game_review.v2.GameReviewMovesMoveNodeClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewMovesMoveNodeClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8269.

```text
e_review.v2.GameReviewMoveFeedbackButton button_name = 3;
  optional int32 percent_reviewed = 5;
}

message GameReviewMovesMoveNodeClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  op
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05392"></a>
## FND-05392: oneof declaration: chesscom.game_review.v2.GameReviewMovesMoveNodeClicked._user_or_opponent_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_or_opponent_move {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7207.

```text
result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05393"></a>
## FND-05393: chesscom.game_review.v2.GameReviewMovesMoveNodeClicked.user_or_opponent_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7240.

```text
s_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chessco
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05394"></a>
## FND-05394: oneof declaration: chesscom.game_review.v2.GameReviewMovesMoveNodeClicked._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05395"></a>
## FND-05395: chesscom.game_review.v2.GameReviewMovesMoveNodeClicked.result = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7335.

```text
 {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.gam
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05396"></a>
## FND-05396: chesscom.game_review.v2.GameReviewMovesMoveNodeClicked.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6869.

```text
nEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClassificationsExpandClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassifi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05397"></a>
## FND-05397: chesscom.game_review.v2.GameReviewMovesMoveNodeClicked.percent_reviewed = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8587.

```text
t = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 4;
}

message GameReviewMoveChangedClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05398"></a>
## FND-05398: message declaration: chesscom.game_review.v2.GameReviewMoveChangedClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewMoveChangedClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8627.

```text
ion_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 4;
}

message GameReviewMoveChangedClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  opti
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05399"></a>
## FND-05399: oneof declaration: chesscom.game_review.v2.GameReviewMoveChangedClicked._user_or_opponent_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_or_opponent_move {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7207.

```text
result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05400"></a>
## FND-05400: chesscom.game_review.v2.GameReviewMoveChangedClicked.user_or_opponent_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7240.

```text
s_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chessco
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05401"></a>
## FND-05401: oneof declaration: chesscom.game_review.v2.GameReviewMoveChangedClicked._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05402"></a>
## FND-05402: chesscom.game_review.v2.GameReviewMoveChangedClicked.result = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7642.

```text
creen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;
}

message GameReviewMoveFeedbackButtonClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_oppon
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05403"></a>
## FND-05403: chesscom.game_review.v2.GameReviewMoveChangedClicked.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6869.

```text
nEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClassificationsExpandClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassifi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05404"></a>
## FND-05404: chesscom.game_review.v2.GameReviewMoveChangedClicked.move_navigation_method = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewMoveNavigationMethod move_navigation_method = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8943.

```text
t = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional .chesscom.game_review.v2.GameReviewMoveNavigationMethod move_navigation_method = 3;
  optional int32 percent_reviewed = 5;
}

message GameReviewMoveChangedArrowKeyPressed {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chessco
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05405"></a>
## FND-05405: chesscom.game_review.v2.GameReviewMoveChangedClicked.percent_reviewed = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8229.

```text
sification = 1;
  optional .chesscom.game_review.v2.GameReviewMoveFeedbackButton button_name = 3;
  optional int32 percent_reviewed = 5;
}

message GameReviewMovesMoveNodeClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClas
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05406"></a>
## FND-05406: message declaration: chesscom.game_review.v2.GameReviewMoveChangedArrowKeyPressed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewMoveChangedArrowKeyPressed {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 9078.

```text
ameReviewMoveNavigationMethod move_navigation_method = 3;
  optional int32 percent_reviewed = 5;
}

message GameReviewMoveChangedArrowKeyPressed {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05407"></a>
## FND-05407: oneof declaration: chesscom.game_review.v2.GameReviewMoveChangedArrowKeyPressed._user_or_opponent_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_or_opponent_move {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7207.

```text
result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05408"></a>
## FND-05408: chesscom.game_review.v2.GameReviewMoveChangedArrowKeyPressed.user_or_opponent_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7240.

```text
s_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chessco
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05409"></a>
## FND-05409: oneof declaration: chesscom.game_review.v2.GameReviewMoveChangedArrowKeyPressed._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05410"></a>
## FND-05410: chesscom.game_review.v2.GameReviewMoveChangedArrowKeyPressed.result = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7642.

```text
creen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;
}

message GameReviewMoveFeedbackButtonClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_oppon
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05411"></a>
## FND-05411: chesscom.game_review.v2.GameReviewMoveChangedArrowKeyPressed.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6869.

```text
nEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClassificationsExpandClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassifi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05412"></a>
## FND-05412: chesscom.game_review.v2.GameReviewMoveChangedArrowKeyPressed.move_navigation_method = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewMoveNavigationMethod move_navigation_method = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8943.

```text
t = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional .chesscom.game_review.v2.GameReviewMoveNavigationMethod move_navigation_method = 3;
  optional int32 percent_reviewed = 5;
}

message GameReviewMoveChangedArrowKeyPressed {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chessco
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05413"></a>
## FND-05413: chesscom.game_review.v2.GameReviewMoveChangedArrowKeyPressed.percent_reviewed = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8229.

```text
sification = 1;
  optional .chesscom.game_review.v2.GameReviewMoveFeedbackButton button_name = 3;
  optional int32 percent_reviewed = 5;
}

message GameReviewMovesMoveNodeClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClas
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05414"></a>
## FND-05414: message declaration: chesscom.game_review.v2.GameReviewBackButtonClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewBackButtonClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 9537.

```text
ameReviewMoveNavigationMethod move_navigation_method = 3;
  optional int32 percent_reviewed = 5;
}

message GameReviewBackButtonClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.game_review.v2.GameReviewBackButtonWeb button_name = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewMovesEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05415"></a>
## FND-05415: oneof declaration: chesscom.game_review.v2.GameReviewBackButtonClicked._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05416"></a>
## FND-05416: chesscom.game_review.v2.GameReviewBackButtonClicked.result = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5109.

```text
_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;
}

message GameRev
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05417"></a>
## FND-05417: chesscom.game_review.v2.GameReviewBackButtonClicked.button_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewBackButtonWeb button_name = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 9655.

```text
BackButtonClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.game_review.v2.GameReviewBackButtonWeb button_name = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewMovesEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification =
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05418"></a>
## FND-05418: chesscom.game_review.v2.GameReviewBackButtonClicked.percent_reviewed = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6698.

```text
iew_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional int32 percent_reviewed = 3;
}

message GameReviewOverviewScreenEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClas
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05419"></a>
## FND-05419: message declaration: chesscom.game_review.v2.GameReviewMovesEvalGraphClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewMovesEvalGraphClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 9772.

```text
m.game_review.v2.GameReviewBackButtonWeb button_name = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewMovesEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewMovesMovesPlaybackToggled {
  oneof _result {
  .ches
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05420"></a>
## FND-05420: oneof declaration: chesscom.game_review.v2.GameReviewMovesEvalGraphClicked._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05421"></a>
## FND-05421: chesscom.game_review.v2.GameReviewMovesEvalGraphClicked.result = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5109.

```text
_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;
}

message GameRev
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05422"></a>
## FND-05422: chesscom.game_review.v2.GameReviewMovesEvalGraphClicked.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6869.

```text
nEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClassificationsExpandClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassifi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05423"></a>
## FND-05423: chesscom.game_review.v2.GameReviewMovesEvalGraphClicked.percent_reviewed = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6698.

```text
iew_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional int32 percent_reviewed = 3;
}

message GameReviewOverviewScreenEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClas
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05424"></a>
## FND-05424: message declaration: chesscom.game_review.v2.GameReviewMovesMovesPlaybackToggled

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewMovesMovesPlaybackToggled {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 10021.

```text
ion_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewMovesMovesPlaybackToggled {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool moves_playback_enabled = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewCoachAudioToggleMuteClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05425"></a>
## FND-05425: oneof declaration: chesscom.game_review.v2.GameReviewMovesMovesPlaybackToggled._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05426"></a>
## FND-05426: chesscom.game_review.v2.GameReviewMovesMovesPlaybackToggled.result = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5109.

```text
_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;
}

message GameRev
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05427"></a>
## FND-05427: chesscom.game_review.v2.GameReviewMovesMovesPlaybackToggled.moves_playback_enabled = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool moves_playback_enabled = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 10147.

```text
esPlaybackToggled {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool moves_playback_enabled = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewCoachAudioToggleMuteClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 5;
  }
  option
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05428"></a>
## FND-05428: chesscom.game_review.v2.GameReviewMovesMovesPlaybackToggled.percent_reviewed = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6698.

```text
iew_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional int32 percent_reviewed = 3;
}

message GameReviewOverviewScreenEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClas
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05429"></a>
## FND-05429: message declaration: chesscom.game_review.v2.GameReviewCoachAudioToggleMuteClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewCoachAudioToggleMuteClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 10231.

```text
sult = 2;
  }
  optional bool moves_playback_enabled = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewCoachAudioToggleMuteClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 5;
  }
  optional bool coach_speech_muted = 1;
  optional string coach_name = 2;
  optional int32 p
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05430"></a>
## FND-05430: oneof declaration: chesscom.game_review.v2.GameReviewCoachAudioToggleMuteClicked._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05431"></a>
## FND-05431: chesscom.game_review.v2.GameReviewCoachAudioToggleMuteClicked.result = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7335.

```text
 {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.gam
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05432"></a>
## FND-05432: oneof declaration: chesscom.game_review.v2.GameReviewCoachAudioToggleMuteClicked._game_review_screen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_review_screen {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6518.

```text
esscom.game_review.v2.GameReviewResult result = 1;
  }
}

message GameReviewSelfAnalysisClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional int32 percent_reviewed = 3;
}

message GameReviewOverviewScreenEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.Game
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05433"></a>
## FND-05433: chesscom.game_review.v2.GameReviewCoachAudioToggleMuteClicked.game_review_screen = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewScreen game_review_screen = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 10389.

```text
esult {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 5;
  }
  optional bool coach_speech_muted = 1;
  optional string coach_name = 2;
  optional int32 percent_reviewed = 4;
}

message GameReviewShowMovesToggleClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_oppo
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05434"></a>
## FND-05434: chesscom.game_review.v2.GameReviewCoachAudioToggleMuteClicked.coach_speech_muted = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool coach_speech_muted = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 10461.

```text
eof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 5;
  }
  optional bool coach_speech_muted = 1;
  optional string coach_name = 2;
  optional int32 percent_reviewed = 4;
}

message GameReviewShowMovesToggleClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameRevi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05435"></a>
## FND-05435: chesscom.game_review.v2.GameReviewCoachAudioToggleMuteClicked.coach_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coach_name = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 10501.

```text
me_review.v2.GameReviewScreen game_review_screen = 5;
  }
  optional bool coach_speech_muted = 1;
  optional string coach_name = 2;
  optional int32 percent_reviewed = 4;
}

message GameReviewShowMovesToggleClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .che
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05436"></a>
## FND-05436: chesscom.game_review.v2.GameReviewCoachAudioToggleMuteClicked.percent_reviewed = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8587.

```text
t = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 4;
}

message GameReviewMoveChangedClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05437"></a>
## FND-05437: message declaration: chesscom.game_review.v2.GameReviewShowMovesToggleClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewShowMovesToggleClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 10575.

```text
coach_speech_muted = 1;
  optional string coach_name = 2;
  optional int32 percent_reviewed = 4;
}

message GameReviewShowMovesToggleClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05438"></a>
## FND-05438: oneof declaration: chesscom.game_review.v2.GameReviewShowMovesToggleClicked._user_or_opponent_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_or_opponent_move {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7207.

```text
result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05439"></a>
## FND-05439: chesscom.game_review.v2.GameReviewShowMovesToggleClicked.user_or_opponent_move = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 10653.

```text
cent_reviewed = 4;
}

message GameReviewShowMovesToggleClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional .chesscom.game_review.v2.ShowMovesButtonState button_state = 2;
  opt
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05440"></a>
## FND-05440: oneof declaration: chesscom.game_review.v2.GameReviewShowMovesToggleClicked._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05441"></a>
## FND-05441: chesscom.game_review.v2.GameReviewShowMovesToggleClicked.result = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7642.

```text
creen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;
}

message GameReviewMoveFeedbackButtonClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_oppon
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05442"></a>
## FND-05442: chesscom.game_review.v2.GameReviewShowMovesToggleClicked.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6869.

```text
nEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClassificationsExpandClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassifi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05443"></a>
## FND-05443: chesscom.game_review.v2.GameReviewShowMovesToggleClicked.button_state = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.ShowMovesButtonState button_state = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 10895.

```text
t = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional .chesscom.game_review.v2.ShowMovesButtonState button_state = 2;
  optional int32 percent_reviewed = 5;
}

message GameReviewCoachVisualization {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewR
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05444"></a>
## FND-05444: chesscom.game_review.v2.GameReviewShowMovesToggleClicked.percent_reviewed = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8229.

```text
sification = 1;
  optional .chesscom.game_review.v2.GameReviewMoveFeedbackButton button_name = 3;
  optional int32 percent_reviewed = 5;
}

message GameReviewMovesMoveNodeClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClas
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05445"></a>
## FND-05445: message declaration: chesscom.game_review.v2.GameReviewCoachVisualization

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewCoachVisualization {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11010.

```text
com.game_review.v2.ShowMovesButtonState button_state = 2;
  optional int32 percent_reviewed = 5;
}

message GameReviewCoachVisualization {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  opti
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05446"></a>
## FND-05446: oneof declaration: chesscom.game_review.v2.GameReviewCoachVisualization._user_or_opponent_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_or_opponent_move {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7207.

```text
result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05447"></a>
## FND-05447: chesscom.game_review.v2.GameReviewCoachVisualization.user_or_opponent_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7240.

```text
s_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chessco
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05448"></a>
## FND-05448: oneof declaration: chesscom.game_review.v2.GameReviewCoachVisualization._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05449"></a>
## FND-05449: chesscom.game_review.v2.GameReviewCoachVisualization.result = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7335.

```text
 {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.gam
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05450"></a>
## FND-05450: chesscom.game_review.v2.GameReviewCoachVisualization.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6869.

```text
nEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClassificationsExpandClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassifi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05451"></a>
## FND-05451: chesscom.game_review.v2.GameReviewCoachVisualization.percent_reviewed = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8587.

```text
t = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 4;
}

message GameReviewMoveChangedClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05452"></a>
## FND-05452: message declaration: chesscom.game_review.v2.GameReviewCeacResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewCeacResponse {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11366.

```text
ion_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 4;
}

message GameReviewCeacResponse {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional bool is_user_game = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 4;
  optional bool ceac_response_result = 5
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05453"></a>
## FND-05453: oneof declaration: chesscom.game_review.v2.GameReviewCeacResponse._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05454"></a>
## FND-05454: chesscom.game_review.v2.GameReviewCeacResponse.result = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7335.

```text
 {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.gam
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05455"></a>
## FND-05455: chesscom.game_review.v2.GameReviewCeacResponse.is_user_game = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_user_game = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11479.

```text
eviewCeacResponse {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional bool is_user_game = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 4;
  optional bool ceac_response_result = 5;
}

message GameReviewCoachTextFeedback {
  oneof _user_feedback {
  string user_feedback = 2;
  }
  optional st
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05456"></a>
## FND-05456: chesscom.game_review.v2.GameReviewCeacResponse.game_type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7758.

```text
eview.v2.GameReviewResult result = 4;
  }
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;
}

message GameReviewMoveFeedbackButtonClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05457"></a>
## FND-05457: chesscom.game_review.v2.GameReviewCeacResponse.source = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewStartSource source = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11578.

```text
 optional bool is_user_game = 1;
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 2;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 4;
  optional bool ceac_response_result = 5;
}

message GameReviewCoachTextFeedback {
  oneof _user_feedback {
  string user_feedback = 2;
  }
  optional string celebrity_coach_text = 1;
  optional string game_link = 3;
  optional int32 move_number = 4;
 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05458"></a>
## FND-05458: chesscom.game_review.v2.GameReviewCeacResponse.ceac_response_result = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool ceac_response_result = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11648.

```text
ysisGameType game_type = 2;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 4;
  optional bool ceac_response_result = 5;
}

message GameReviewCoachTextFeedback {
  oneof _user_feedback {
  string user_feedback = 2;
  }
  optional string celebrity_coach_text = 1;
  optional string game_link = 3;
  optional int32 move_number = 4;
  optional string selected_coach_name = 5;
  optional string selected_c
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05459"></a>
## FND-05459: message declaration: chesscom.game_review.v2.GameReviewCoachTextFeedback

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewCoachTextFeedback {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11691.

```text
sscom.game_review.v2.GameReviewStartSource source = 4;
  optional bool ceac_response_result = 5;
}

message GameReviewCoachTextFeedback {
  oneof _user_feedback {
  string user_feedback = 2;
  }
  optional string celebrity_coach_text = 1;
  optional string game_link = 3;
  optional int32 move_number = 4;
  optional string selected_coach_name = 5;
  optional string selected_coach_id = 6;
  optional .chesscom.explanati
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05460"></a>
## FND-05460: oneof declaration: chesscom.game_review.v2.GameReviewCoachTextFeedback._user_feedback

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_feedback {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11731.

```text
ce source = 4;
  optional bool ceac_response_result = 5;
}

message GameReviewCoachTextFeedback {
  oneof _user_feedback {
  string user_feedback = 2;
  }
  optional string celebrity_coach_text = 1;
  optional string game_link = 3;
  optional int32 move_number = 4;
  optional string selected_coach_name = 5;
  optional string selected_coach_id = 6;
  optional .chesscom.explanation_engine.v1.MoveClassification move_cla
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05461"></a>
## FND-05461: chesscom.game_review.v2.GameReviewCoachTextFeedback.user_feedback = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_feedback = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11756.

```text
 bool ceac_response_result = 5;
}

message GameReviewCoachTextFeedback {
  oneof _user_feedback {
  string user_feedback = 2;
  }
  optional string celebrity_coach_text = 1;
  optional string game_link = 3;
  optional int32 move_number = 4;
  optional string selected_coach_name = 5;
  optional string selected_coach_id = 6;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 7;
  option
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05462"></a>
## FND-05462: chesscom.game_review.v2.GameReviewCoachTextFeedback.celebrity_coach_text = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string celebrity_coach_text = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11788.

```text
}

message GameReviewCoachTextFeedback {
  oneof _user_feedback {
  string user_feedback = 2;
  }
  optional string celebrity_coach_text = 1;
  optional string game_link = 3;
  optional int32 move_number = 4;
  optional string selected_coach_name = 5;
  optional string selected_coach_id = 6;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 7;
  optional string cee_version = 8;
  opt
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05463"></a>
## FND-05463: chesscom.game_review.v2.GameReviewCoachTextFeedback.game_link = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_link = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11832.

```text
neof _user_feedback {
  string user_feedback = 2;
  }
  optional string celebrity_coach_text = 1;
  optional string game_link = 3;
  optional int32 move_number = 4;
  optional string selected_coach_name = 5;
  optional string selected_coach_id = 6;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 7;
  optional string cee_version = 8;
  optional string engine_strength = 9;
}

message
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05464"></a>
## FND-05464: chesscom.game_review.v2.GameReviewCoachTextFeedback.move_number = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 move_number = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11865.

```text
er_feedback = 2;
  }
  optional string celebrity_coach_text = 1;
  optional string game_link = 3;
  optional int32 move_number = 4;
  optional string selected_coach_name = 5;
  optional string selected_coach_id = 6;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 7;
  optional string cee_version = 8;
  optional string engine_strength = 9;
}

message GameReviewCourseRecommendationVi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05465"></a>
## FND-05465: chesscom.game_review.v2.GameReviewCoachTextFeedback.selected_coach_name = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string selected_coach_name = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11899.

```text
ring celebrity_coach_text = 1;
  optional string game_link = 3;
  optional int32 move_number = 4;
  optional string selected_coach_name = 5;
  optional string selected_coach_id = 6;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 7;
  optional string cee_version = 8;
  optional string engine_strength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_na
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05466"></a>
## FND-05466: chesscom.game_review.v2.GameReviewCoachTextFeedback.selected_coach_id = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string selected_coach_id = 6;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11942.

```text
tring game_link = 3;
  optional int32 move_number = 4;
  optional string selected_coach_name = 5;
  optional string selected_coach_id = 6;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 7;
  optional string cee_version = 8;
  optional string engine_strength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05467"></a>
## FND-05467: chesscom.game_review.v2.GameReviewCoachTextFeedback.move_classification = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 7;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 11983.

```text
e_number = 4;
  optional string selected_coach_name = 5;
  optional string selected_coach_id = 6;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 7;
  optional string cee_version = 8;
  optional string engine_strength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameR
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05468"></a>
## FND-05468: chesscom.game_review.v2.GameReviewCoachTextFeedback.cee_version = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string cee_version = 8;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12070.

```text
ch_id = 6;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 7;
  optional string cee_version = 8;
  optional string engine_strength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicke
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05469"></a>
## FND-05469: chesscom.game_review.v2.GameReviewCoachTextFeedback.engine_strength = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string engine_strength = 9;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12105.

```text
lanation_engine.v1.MoveClassification move_classification = 7;
  optional string cee_version = 8;
  optional string engine_strength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name =
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05470"></a>
## FND-05470: message declaration: chesscom.game_review.v2.GameReviewCourseRecommendationViewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewCourseRecommendationViewed {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12145.

```text
ve_classification = 7;
  optional string cee_version = 8;
  optional string engine_strength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05471"></a>
## FND-05471: chesscom.game_review.v2.GameReviewCourseRecommendationViewed.course_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_name = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12194.

```text
ion = 8;
  optional string engine_strength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCour
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05472"></a>
## FND-05472: chesscom.game_review.v2.GameReviewCourseRecommendationViewed.author_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string author_name = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12229.

```text
trength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
  op
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05473"></a>
## FND-05473: chesscom.game_review.v2.GameReviewCourseRecommendationViewed.type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12264.

```text
ourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
  optional string opening_name = 4;
  o
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05474"></a>
## FND-05474: message declaration: chesscom.game_review.v2.GameReviewCourseRecommendationClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewCourseRecommendationClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12346.

```text
uthor_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
  optional string opening_name = 4;
  optional string fen = 5;
  optional string variation_preview_url = 6;
  optional st
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
