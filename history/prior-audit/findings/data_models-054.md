# data_models — findings 5301–5400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-05575"></a>
## FND-05575: oneof declaration: chesscom.game_review.v2.GameReviewExplainMoveNavClicked._result

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

<a id="FND-05576"></a>
## FND-05576: chesscom.game_review.v2.GameReviewExplainMoveNavClicked.result = 3

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

<a id="FND-05577"></a>
## FND-05577: chesscom.game_review.v2.GameReviewExplainMoveNavClicked.move_classification = 1

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

<a id="FND-05578"></a>
## FND-05578: chesscom.game_review.v2.GameReviewExplainMoveNavClicked.percent_reviewed = 4

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

<a id="FND-05579"></a>
## FND-05579: chesscom.game_review.v2.GameReviewExplainMoveNavClicked.line_ply = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 line_ply = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 17200.

```text
tion_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 4;
  optional int32 line_ply = 5;
  optional .chesscom.game_review.v2.GameReviewMoveNavigationMethod move_navigation_method = 6;
}

message GameReviewShareButtonClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameRev
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05580"></a>
## FND-05580: chesscom.game_review.v2.GameReviewExplainMoveNavClicked.move_navigation_method = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewMoveNavigationMethod move_navigation_method = 6;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 17231.

```text
on move_classification = 1;
  optional int32 percent_reviewed = 4;
  optional int32 line_ply = 5;
  optional .chesscom.game_review.v2.GameReviewMoveNavigationMethod move_navigation_method = 6;
}

message GameReviewShareButtonClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  opt
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05581"></a>
## FND-05581: message declaration: chesscom.game_review.v2.GameReviewShareButtonClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewShareButtonClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 17327.

```text
;
  optional .chesscom.game_review.v2.GameReviewMoveNavigationMethod move_navigation_method = 6;
}

message GameReviewShareButtonClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.game_review.v2.GameReviewSharePlacement placement = 2;
}

message GameReviewShar
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05582"></a>
## FND-05582: oneof declaration: chesscom.game_review.v2.GameReviewShareButtonClicked._game_review_screen

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

<a id="FND-05583"></a>
## FND-05583: chesscom.game_review.v2.GameReviewShareButtonClicked.game_review_screen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6548.

```text
ewResult result = 1;
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
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05584"></a>
## FND-05584: oneof declaration: chesscom.game_review.v2.GameReviewShareButtonClicked._result

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

<a id="FND-05585"></a>
## FND-05585: chesscom.game_review.v2.GameReviewShareButtonClicked.result = 3

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

<a id="FND-05586"></a>
## FND-05586: chesscom.game_review.v2.GameReviewShareButtonClicked.placement = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewSharePlacement placement = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 17548.

```text
iew_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.game_review.v2.GameReviewSharePlacement placement = 2;
}

message GameReviewShareCompleted {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _destination {
  string destination = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameRevi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05587"></a>
## FND-05587: message declaration: chesscom.game_review.v2.GameReviewShareCompleted

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewShareCompleted {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 17625.

```text
sult result = 3;
  }
  optional .chesscom.game_review.v2.GameReviewSharePlacement placement = 2;
}

message GameReviewShareCompleted {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _destination {
  string destination = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.game_review.v2.GameReviewShareP
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05588"></a>
## FND-05588: oneof declaration: chesscom.game_review.v2.GameReviewShareCompleted._game_review_screen

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

<a id="FND-05589"></a>
## FND-05589: chesscom.game_review.v2.GameReviewShareCompleted.game_review_screen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6548.

```text
ewResult result = 1;
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
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05590"></a>
## FND-05590: oneof declaration: chesscom.game_review.v2.GameReviewShareCompleted._destination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _destination {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 17764.

```text
eof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _destination {
  string destination = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.game_review.v2.GameReviewSharePlacement placement = 2;
}

message GameReviewSettingsClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen ga
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05591"></a>
## FND-05591: chesscom.game_review.v2.GameReviewShareCompleted.destination = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string destination = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 17787.

```text
 {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _destination {
  string destination = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.game_review.v2.GameReviewSharePlacement placement = 2;
}

message GameReviewSettingsClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05592"></a>
## FND-05592: oneof declaration: chesscom.game_review.v2.GameReviewShareCompleted._result

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

<a id="FND-05593"></a>
## FND-05593: chesscom.game_review.v2.GameReviewShareCompleted.result = 4

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

<a id="FND-05594"></a>
## FND-05594: chesscom.game_review.v2.GameReviewShareCompleted.placement = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewSharePlacement placement = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 17548.

```text
iew_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.game_review.v2.GameReviewSharePlacement placement = 2;
}

message GameReviewShareCompleted {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _destination {
  string destination = 3;
  }
  oneof _result {
  .chesscom.game_review.v2.GameRevi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05595"></a>
## FND-05595: message declaration: chesscom.game_review.v2.GameReviewSettingsClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewSettingsClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 17972.

```text
sult result = 4;
  }
  optional .chesscom.game_review.v2.GameReviewSharePlacement placement = 2;
}

message GameReviewSettingsClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
}

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05596"></a>
## FND-05596: oneof declaration: chesscom.game_review.v2.GameReviewSettingsClicked._game_review_screen

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

<a id="FND-05597"></a>
## FND-05597: chesscom.game_review.v2.GameReviewSettingsClicked.game_review_screen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6548.

```text
ewResult result = 1;
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
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05598"></a>
## FND-05598: oneof declaration: chesscom.game_review.v2.GameReviewSettingsClicked._result

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

<a id="FND-05599"></a>
## FND-05599: chesscom.game_review.v2.GameReviewSettingsClicked.result = 2

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

<a id="FND-05600"></a>
## FND-05600: enum declaration: chesscom.game_storage.v1.GameProvider

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameProvider {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 108.

```text
e: chesscom/game_storage/v1/game_stored.proto
// syntax: proto3

package chesscom.game_storage.v1;

enum GameProvider {
  GAME_PROVIDER_UNSPECIFIED = 0;
  GAME_PROVIDER_CHESS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05601"></a>
## FND-05601: chesscom.game_storage.v1.GameProvider.GAME_PROVIDER_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 130.

```text
ge/v1/game_stored.proto
// syntax: proto3

package chesscom.game_storage.v1;

enum GameProvider {
  GAME_PROVIDER_UNSPECIFIED = 0;
  GAME_PROVIDER_CHESS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DI
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05602"></a>
## FND-05602: chesscom.game_storage.v1.GameProvider.GAME_PROVIDER_CHESS_COM = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_CHESS_COM = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 163.

```text
: proto3

package chesscom.game_storage.v1;

enum GameProvider {
  GAME_PROVIDER_UNSPECIFIED = 0;
  GAME_PROVIDER_CHESS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05603"></a>
## FND-05603: chesscom.game_storage.v1.GameProvider.GAME_PROVIDER_CHESS_KID = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_CHESS_KID = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 194.

```text
_storage.v1;

enum GameProvider {
  GAME_PROVIDER_UNSPECIFIED = 0;
  GAME_PROVIDER_CHESS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_S
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05604"></a>
## FND-05604: chesscom.game_storage.v1.GameProvider.GAME_PROVIDER_FIDE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_FIDE = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 225.

```text
 {
  GAME_PROVIDER_UNSPECIFIED = 0;
  GAME_PROVIDER_CHESS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GA
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05605"></a>
## FND-05605: chesscom.game_storage.v1.GameProvider.GAME_PROVIDER_LICHESS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_LICHESS = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 251.

```text
FIED = 0;
  GAME_PROVIDER_CHESS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATC
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05606"></a>
## FND-05606: chesscom.game_storage.v1.GameProvider.GAME_PROVIDER_CHESSBASE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_CHESSBASE = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 280.

```text
SS_COM = 1;
  GAME_PROVIDER_CHESS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05607"></a>
## FND-05607: chesscom.game_storage.v1.GameProvider.GAME_PROVIDER_OFFLINE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_OFFLINE = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 311.

```text
SS_KID = 2;
  GAME_PROVIDER_FIDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05608"></a>
## FND-05608: chesscom.game_storage.v1.GameProvider.GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 340.

```text
IDE = 3;
  GAME_PROVIDER_LICHESS = 4;
  GAME_PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05609"></a>
## FND-05609: enum declaration: chesscom.game_storage.v1.GameOrigin

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameOrigin {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 385.

```text
PROVIDER_CHESSBASE = 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIG
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05610"></a>
## FND-05610: chesscom.game_storage.v1.GameOrigin.GAME_ORIGIN_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 405.

```text
 5;
  GAME_PROVIDER_OFFLINE = 6;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05611"></a>
## FND-05611: chesscom.game_storage.v1.GameOrigin.GAME_ORIGIN_DIRECT_CHALLENGE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_DIRECT_CHALLENGE = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 436.

```text
;
  GAME_PROVIDER_CHESS_COM_MASTER_GAMES = 7;
}

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 1
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05612"></a>
## FND-05612: chesscom.game_storage.v1.GameOrigin.GAME_ORIGIN_SEEK = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_SEEK = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 472.

```text
AMES = 7;
}

enum GameOrigin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05613"></a>
## FND-05613: chesscom.game_storage.v1.GameOrigin.GAME_ORIGIN_POOL_SEEK = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_POOL_SEEK = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 496.

```text
igin {
  GAME_ORIGIN_UNSPECIFIED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLAS
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05614"></a>
## FND-05614: chesscom.game_storage.v1.GameOrigin.GAME_ORIGIN_START_GAME = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_START_GAME = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 525.

```text
IED = 0;
  GAME_ORIGIN_DIRECT_CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLA
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05615"></a>
## FND-05615: chesscom.game_storage.v1.GameOrigin.GAME_ORIGIN_MATCH = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_MATCH = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 555.

```text
CHALLENGE = 1;
  GAME_ORIGIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BL
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05616"></a>
## FND-05616: chesscom.game_storage.v1.GameOrigin.GAME_ORIGIN_ARENA = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_ARENA = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 580.

```text
GIN_SEEK = 2;
  GAME_ORIGIN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAP
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05617"></a>
## FND-05617: chesscom.game_storage.v1.GameOrigin.GAME_ORIGIN_TOURNAMENT = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_TOURNAMENT = 7;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 605.

```text
IN_POOL_SEEK = 3;
  GAME_ORIGIN_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAIL
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05618"></a>
## FND-05618: chesscom.game_storage.v1.GameOrigin.GAME_ORIGIN_TEAM_MATCH = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_TEAM_MATCH = 8;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 635.

```text
N_START_GAME = 4;
  GAME_ORIGIN_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05619"></a>
## FND-05619: chesscom.game_storage.v1.GameOrigin.GAME_ORIGIN_COMPETITION = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_COMPETITION = 9;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 665.

```text
N_MATCH = 5;
  GAME_ORIGIN_ARENA = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05620"></a>
## FND-05620: chesscom.game_storage.v1.GameOrigin.GAME_ORIGIN_RECOMMENDED_MATCH = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_RECOMMENDED_MATCH = 10;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 696.

```text
A = 6;
  GAME_ORIGIN_TOURNAMENT = 7;
  GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_C
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05621"></a>
## FND-05621: chesscom.game_storage.v1.GameOrigin.GAME_ORIGIN_LEAGUE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_LEAGUE = 11;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 734.

```text
 GAME_ORIGIN_TEAM_MATCH = 8;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_U
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05622"></a>
## FND-05622: chesscom.game_storage.v1.GameOrigin.GAME_ORIGIN_SIMUL = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_ORIGIN_SIMUL = 12;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 761.

```text
;
  GAME_ORIGIN_COMPETITION = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05623"></a>
## FND-05623: enum declaration: chesscom.game_storage.v1.TimeClass

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TimeClass {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 788.

```text
 = 9;
  GAME_ORIGIN_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05624"></a>
## FND-05624: chesscom.game_storage.v1.TimeClass.TIME_CLASS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 807.

```text
_RECOMMENDED_MATCH = 10;
  GAME_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHE
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05625"></a>
## FND-05625: chesscom.game_storage.v1.TimeClass.TIME_CLASS_BULLET = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_BULLET = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 837.

```text
E_ORIGIN_LEAGUE = 11;
  GAME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATI
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05626"></a>
## FND-05626: chesscom.game_storage.v1.TimeClass.TIME_CLASS_BLITZ = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_BLITZ = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 862.

```text
AME_ORIGIN_SIMUL = 12;
}

enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05627"></a>
## FND-05627: chesscom.game_storage.v1.TimeClass.TIME_CLASS_RAPID = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_RAPID = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 886.

```text


enum TimeClass {
  TIME_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLAS
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05628"></a>
## FND-05628: chesscom.game_storage.v1.TimeClass.TIME_CLASS_DAILY = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_DAILY = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 910.

```text
E_CLASS_UNSPECIFIED = 0;
  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05629"></a>
## FND-05629: chesscom.game_storage.v1.TimeClass.TIME_CLASS_HYPER = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_HYPER = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 934.

```text

  TIME_CLASS_BULLET = 1;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHES
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05630"></a>
## FND-05630: chesscom.game_storage.v1.TimeClass.TIME_CLASS_CLASSICAL = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TIME_CLASS_CLASSICAL = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 958.

```text
;
  TIME_CLASS_BLITZ = 2;
  TIME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RA
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05631"></a>
## FND-05631: enum declaration: chesscom.game_storage.v1.RatingClass

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum RatingClass {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 987.

```text
IME_CLASS_RAPID = 3;
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05632"></a>
## FND-05632: chesscom.game_storage.v1.RatingClass.RATING_CLASS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1008.

```text
  TIME_CLASS_DAILY = 4;
  TIME_CLASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05633"></a>
## FND-05633: chesscom.game_storage.v1.RatingClass.RATING_CLASS_UNRATED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_UNRATED = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1040.

```text
LASS_HYPER = 5;
  TIME_CLASS_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05634"></a>
## FND-05634: chesscom.game_storage.v1.RatingClass.RATING_CLASS_CHESS_COM_CHESS_BULLET = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1068.

```text
_CLASSICAL = 6;
}

enum RatingClass {
  RATING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGO
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05635"></a>
## FND-05635: chesscom.game_storage.v1.RatingClass.RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1111.

```text
ING_CLASS_UNSPECIFIED = 0;
  RATING_CLASS_UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THRE
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05636"></a>
## FND-05636: chesscom.game_storage.v1.RatingClass.RATING_CLASS_CHESS_COM_CHESS_RAPID = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1153.

```text
UNRATED = 1;
  RATING_CLASS_CHESS_COM_CHESS_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZ
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05637"></a>
## FND-05637: chesscom.game_storage.v1.RatingClass.RATING_CLASS_CHESS_COM_CHESS_DAILY = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1195.

```text
S_BULLET = 2;
  RATING_CLASS_CHESS_COM_CHESS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STA
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05638"></a>
## FND-05638: chesscom.game_storage.v1.RatingClass.RATING_CLASS_CHESS_COM_CHESS960 = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS960 = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1237.

```text
SS_BLITZ = 3;
  RATING_CLASS_CHESS_COM_CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPI
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05639"></a>
## FND-05639: chesscom.game_storage.v1.RatingClass.RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1276.

```text
CHESS_RAPID = 4;
  RATING_CLASS_CHESS_COM_CHESS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05640"></a>
## FND-05640: chesscom.game_storage.v1.RatingClass.RATING_CLASS_CHESS_COM_BUGHOUSE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_BUGHOUSE = 8;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1321.

```text
SS_DAILY = 5;
  RATING_CLASS_CHESS_COM_CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CH
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05641"></a>
## FND-05641: chesscom.game_storage.v1.RatingClass.RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1360.

```text
CHESS960 = 6;
  RATING_CLASS_CHESS_COM_CHESS960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

enum Variant {
  VARIANT_U
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05642"></a>
## FND-05642: chesscom.game_storage.v1.RatingClass.RATING_CLASS_CHESS_COM_THREECHECK = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_THREECHECK = 10;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1404.

```text
960_DAILY = 7;
  RATING_CLASS_CHESS_COM_BUGHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIA
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05643"></a>
## FND-05643: chesscom.game_storage.v1.RatingClass.RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1446.

```text
GHOUSE = 8;
  RATING_CLASS_CHESS_COM_KINGOFTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;

```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05644"></a>
## FND-05644: chesscom.game_storage.v1.RatingClass.RATING_CLASS_FIDE_CHESS_STANDARD = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_FIDE_CHESS_STANDARD = 12;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1488.

```text
FTHEHILL = 9;
  RATING_CLASS_CHESS_COM_THREECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZY
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05645"></a>
## FND-05645: chesscom.game_storage.v1.RatingClass.RATING_CLASS_FIDE_CHESS_RAPID = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_FIDE_CHESS_RAPID = 13;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1529.

```text
REECHECK = 10;
  RATING_CLASS_CHESS_COM_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05646"></a>
## FND-05646: chesscom.game_storage.v1.RatingClass.RATING_CLASS_FIDE_CHESS_BLITZ = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_FIDE_CHESS_BLITZ = 14;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1567.

```text
M_CRAZYHOUSE = 11;
  RATING_CLASS_FIDE_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05647"></a>
## FND-05647: chesscom.game_storage.v1.RatingClass.RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1605.

```text
_CHESS_STANDARD = 12;
  RATING_CLASS_FIDE_CHESS_RAPID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {

```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05648"></a>
## FND-05648: enum declaration: chesscom.game_storage.v1.Variant

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Variant {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1654.

```text
APID = 13;
  RATING_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PU
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05649"></a>
## FND-05649: chesscom.game_storage.v1.Variant.VARIANT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1671.

```text
NG_CLASS_FIDE_CHESS_BLITZ = 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05650"></a>
## FND-05650: chesscom.game_storage.v1.Variant.VARIANT_CHESS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_CHESS = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1698.

```text
 14;
  RATING_CLASS_CHESS_COM_CHESS_ODDS_CHESS = 15;
}

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enu
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05651"></a>
## FND-05651: chesscom.game_storage.v1.Variant.VARIANT_CHESS_960 = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_CHESS_960 = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1719.

```text
HESS_COM_CHESS_ODDS_CHESS = 15;
}

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PL
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05652"></a>
## FND-05652: chesscom.game_storage.v1.Variant.VARIANT_BUGHOUSE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_BUGHOUSE = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1744.

```text
 = 15;
}

enum Variant {
  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED =
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05653"></a>
## FND-05653: chesscom.game_storage.v1.Variant.VARIANT_THREE_CHECK = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_THREE_CHECK = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1768.

```text

  VARIANT_UNSPECIFIED = 0;
  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05654"></a>
## FND-05654: chesscom.game_storage.v1.Variant.VARIANT_CRAZYHOUSE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_CRAZYHOUSE = 6;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1795.

```text

  VARIANT_CHESS = 1;
  VARIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW =
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05655"></a>
## FND-05655: chesscom.game_storage.v1.Variant.VARIANT_KING_OF_THE_HILL = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_KING_OF_THE_HILL = 7;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1821.

```text
RIANT_CHESS_960 = 2;
  VARIANT_BUGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE =
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05656"></a>
## FND-05656: chesscom.game_storage.v1.Variant.VARIANT_ODDS_CHESS = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_ODDS_CHESS = 8;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1853.

```text
UGHOUSE = 4;
  VARIANT_THREE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05657"></a>
## FND-05657: chesscom.game_storage.v1.Variant.VARIANT_HELP_CHESS = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VARIANT_HELP_CHESS = 9;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1879.

```text
EE_CHECK = 5;
  VARIANT_CRAZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PA
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05658"></a>
## FND-05658: enum declaration: chesscom.game_storage.v1.GamePrivacy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GamePrivacy {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1906.

```text
ZYHOUSE = 6;
  VARIANT_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum Gam
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05659"></a>
## FND-05659: chesscom.game_storage.v1.GamePrivacy.GAME_PRIVACY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PRIVACY_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1927.

```text
T_KING_OF_THE_HILL = 7;
  VARIANT_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum GameResult {
  GAME_RESU
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05660"></a>
## FND-05660: chesscom.game_storage.v1.GamePrivacy.GAME_PRIVACY_PUBLIC = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PRIVACY_PUBLIC = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1959.

```text
T_ODDS_CHESS = 8;
  VARIANT_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESUL
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05661"></a>
## FND-05661: chesscom.game_storage.v1.GamePrivacy.GAME_PRIVACY_PRIVATE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_PRIVACY_PRIVATE = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 1986.

```text
_HELP_CHESS = 9;
}

enum GamePrivacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;

```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05662"></a>
## FND-05662: enum declaration: chesscom.game_storage.v1.PlayerResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PlayerResult {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2015.

```text
Privacy {
  GAME_PRIVACY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHE
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05663"></a>
## FND-05663: chesscom.game_storage.v1.PlayerResult.PLAYER_RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2037.

```text
CY_UNSPECIFIED = 0;
  GAME_PRIVACY_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RES
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05664"></a>
## FND-05664: chesscom.game_storage.v1.PlayerResult.PLAYER_RESULT_WIN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_RESULT_WIN = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2070.

```text
Y_PUBLIC = 1;
  GAME_PRIVACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;

```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05665"></a>
## FND-05665: chesscom.game_storage.v1.PlayerResult.PLAYER_RESULT_DRAW = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_RESULT_DRAW = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2095.

```text
ACY_PRIVATE = 2;
}

enum PlayerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05666"></a>
## FND-05666: chesscom.game_storage.v1.PlayerResult.PLAYER_RESULT_LOSE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_RESULT_LOSE = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2121.

```text
layerResult {
  PLAYER_RESULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_R
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05667"></a>
## FND-05667: chesscom.game_storage.v1.PlayerResult.PLAYER_RESULT_ABORT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_RESULT_ABORT = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2147.

```text
ULT_UNSPECIFIED = 0;
  PLAYER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05668"></a>
## FND-05668: chesscom.game_storage.v1.PlayerResult.PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2174.

```text
ER_RESULT_WIN = 1;
  PLAYER_RESULT_DRAW = 2;
  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_RE
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05669"></a>
## FND-05669: enum declaration: chesscom.game_storage.v1.GameResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameResult {

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2218.

```text

  PLAYER_RESULT_LOSE = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMAT
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05670"></a>
## FND-05670: chesscom.game_storage.v1.GameResult.GAME_RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2238.

```text
E = 3;
  PLAYER_RESULT_ABORT = 4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05671"></a>
## FND-05671: chesscom.game_storage.v1.GameResult.GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2269.

```text
4;
  PLAYER_RESULT_BUGHOUSE_PARTNER_LOSE = 5;
}

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL 
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05672"></a>
## FND-05672: chesscom.game_storage.v1.GameResult.GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2308.

```text
E = 5;
}

enum GameResult {
  GAME_RESULT_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_I
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05673"></a>
## FND-05673: chesscom.game_storage.v1.GameResult.GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2349.

```text
_UNSPECIFIED = 0;
  GAME_RESULT_WIN_LOSE_BY_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_D
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05674"></a>
## FND-05674: chesscom.game_storage.v1.GameResult.GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;

### Evidence

- **SRC-0455** `research/proto/chesscom/game_storage/v1/game_stored.proto` — [preserved redacted evidence](../evidence/text/1be0149c3b468e713fbfd7c053accb9df08e3b9f622af257a146b19c18b35290.proto)
  Character offset 2392.

```text
_TIMEOUT = 1;
  GAME_RESULT_WIN_LOSE_BY_CHECKMATE = 2;
  GAME_RESULT_WIN_LOSE_BY_RESIGNATION = 3;
  GAME_RESULT_WIN_LOSE_BY_ABANDONMENT = 4;
  GAME_RESULT_DRAW_BY_AGREEMENT = 5;
  GAME_RESULT_DRAW_BY_REPETITION = 6;
  GAME_RESULT_DRAW_BY_STALEMATE = 7;
  GAME_RESULT_DRAW_BY_INSUFFICIENT_MATERIAL = 8;
  GAME_RESULT_DRAW_BY_TIMEOUT_VS_INSUFFICIENT_MATERIAL = 9;
  GAME_RESULT_DRAW_BY_50_MOVE_RULE = 10;
  GAME_RESULT_WIN
```

**Source references:** SRC-0455, SRC-1426  
**URL references:** None independently associated  
**Related findings:** FND-05600, FND-05601, FND-05602

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
