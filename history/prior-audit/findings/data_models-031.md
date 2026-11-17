# data_models — findings 3001–3100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-03275"></a>
## FND-03275: chesscom.explanation_engine.v1.RetryMiss.success_speech = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech success_speech = 8;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2422.

```text
.Speech attempt_speech = 6;
  optional .chesscom.explanation_engine.v1.Speech failure_speech = 7;
  optional .chesscom.explanation_engine.v1.Speech success_speech = 8;
  repeated .chesscom.chess.v1.Move success_moves = 9;
}

message CoachChoice {
  oneof _response_move {
  .chesscom.chess.v1.Move response_move = 3;
  }
  optional string button_text = 1;
  optional .chesscom.explanation_engine.v1.Speech response_speec
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03276"></a>
## FND-03276: chesscom.explanation_engine.v1.RetryMiss.success_moves = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Move success_moves = 9;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2492.

```text
.Speech failure_speech = 7;
  optional .chesscom.explanation_engine.v1.Speech success_speech = 8;
  repeated .chesscom.chess.v1.Move success_moves = 9;
}

message CoachChoice {
  oneof _response_move {
  .chesscom.chess.v1.Move response_move = 3;
  }
  optional string button_text = 1;
  optional .chesscom.explanation_engine.v1.Speech response_speech = 2;
}

message CoachChatDebugInfo {
  optional .chesscom.explanatio
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03277"></a>
## FND-03277: message declaration: chesscom.explanation_engine.v1.CoachChoice

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachChoice {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2547.

```text
ation_engine.v1.Speech success_speech = 8;
  repeated .chesscom.chess.v1.Move success_moves = 9;
}

message CoachChoice {
  oneof _response_move {
  .chesscom.chess.v1.Move response_move = 3;
  }
  optional string button_text = 1;
  optional .chesscom.explanation_engine.v1.Speech response_speech = 2;
}

message CoachChatDebugInfo {
  optional .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 1;
  op
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03278"></a>
## FND-03278: oneof declaration: chesscom.explanation_engine.v1.CoachChoice._response_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _response_move {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2571.

```text
uccess_speech = 8;
  repeated .chesscom.chess.v1.Move success_moves = 9;
}

message CoachChoice {
  oneof _response_move {
  .chesscom.chess.v1.Move response_move = 3;
  }
  optional string button_text = 1;
  optional .chesscom.explanation_engine.v1.Speech response_speech = 2;
}

message CoachChatDebugInfo {
  optional .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 1;
  optional .chesscom.explana
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03279"></a>
## FND-03279: chesscom.explanation_engine.v1.CoachChoice.response_move = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Move response_move = 3;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2596.

```text
ated .chesscom.chess.v1.Move success_moves = 9;
}

message CoachChoice {
  oneof _response_move {
  .chesscom.chess.v1.Move response_move = 3;
  }
  optional string button_text = 1;
  optional .chesscom.explanation_engine.v1.Speech response_speech = 2;
}

message CoachChatDebugInfo {
  optional .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 1;
  optional .chesscom.explanation_engine.v1.RetryMista
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03280"></a>
## FND-03280: chesscom.explanation_engine.v1.CoachChoice.button_text = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string button_text = 1;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2645.

```text


message CoachChoice {
  oneof _response_move {
  .chesscom.chess.v1.Move response_move = 3;
  }
  optional string button_text = 1;
  optional .chesscom.explanation_engine.v1.Speech response_speech = 2;
}

message CoachChatDebugInfo {
  optional .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 1;
  optional .chesscom.explanation_engine.v1.RetryMistakeDebugInfo retry_mistake_debug_info = 2;
  repea
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03281"></a>
## FND-03281: chesscom.explanation_engine.v1.CoachChoice.response_speech = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech response_speech = 2;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2680.

```text
sponse_move {
  .chesscom.chess.v1.Move response_move = 3;
  }
  optional string button_text = 1;
  optional .chesscom.explanation_engine.v1.Speech response_speech = 2;
}

message CoachChatDebugInfo {
  optional .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 1;
  optional .chesscom.explanation_engine.v1.RetryMistakeDebugInfo retry_mistake_debug_info = 2;
  repeated string used_botchat_triggers = 
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03282"></a>
## FND-03282: message declaration: chesscom.explanation_engine.v1.CoachChatDebugInfo

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachChatDebugInfo {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2752.

```text
l string button_text = 1;
  optional .chesscom.explanation_engine.v1.Speech response_speech = 2;
}

message CoachChatDebugInfo {
  optional .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 1;
  optional .chesscom.explanation_engine.v1.RetryMistakeDebugInfo retry_mistake_debug_info = 2;
  repeated string used_botchat_triggers = 3;
  repeated string used_board_events = 4;
  optional .chesscom.explana
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03283"></a>
## FND-03283: chesscom.explanation_engine.v1.CoachChatDebugInfo.speech_debug_info = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 1;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2783.

```text
ional .chesscom.explanation_engine.v1.Speech response_speech = 2;
}

message CoachChatDebugInfo {
  optional .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 1;
  optional .chesscom.explanation_engine.v1.RetryMistakeDebugInfo retry_mistake_debug_info = 2;
  repeated string used_botchat_triggers = 3;
  repeated string used_board_events = 4;
  optional .chesscom.explanation_engine.v1.FlipBoardMistake
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03284"></a>
## FND-03284: chesscom.explanation_engine.v1.CoachChatDebugInfo.retry_mistake_debug_info = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.RetryMistakeDebugInfo retry_mistake_debug_info = 2;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2865.

```text
ChatDebugInfo {
  optional .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 1;
  optional .chesscom.explanation_engine.v1.RetryMistakeDebugInfo retry_mistake_debug_info = 2;
  repeated string used_botchat_triggers = 3;
  repeated string used_board_events = 4;
  optional .chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo flip_board_mistake_debug_info = 5;
}

message RetryMistakeDebugInfo {
  
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03285"></a>
## FND-03285: chesscom.explanation_engine.v1.CoachChatDebugInfo.used_botchat_triggers = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string used_botchat_triggers = 3;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 2960.

```text
1;
  optional .chesscom.explanation_engine.v1.RetryMistakeDebugInfo retry_mistake_debug_info = 2;
  repeated string used_botchat_triggers = 3;
  repeated string used_board_events = 4;
  optional .chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo flip_board_mistake_debug_info = 5;
}

message RetryMistakeDebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03286"></a>
## FND-03286: chesscom.explanation_engine.v1.CoachChatDebugInfo.used_board_events = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string used_board_events = 4;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 3005.

```text
.RetryMistakeDebugInfo retry_mistake_debug_info = 2;
  repeated string used_botchat_triggers = 3;
  repeated string used_board_events = 4;
  optional .chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo flip_board_mistake_debug_info = 5;
}

message RetryMistakeDebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional bool player_is_winning = 2;
  optional int32
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03287"></a>
## FND-03287: chesscom.explanation_engine.v1.CoachChatDebugInfo.flip_board_mistake_debug_info = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo flip_board_mistake_debug_info = 5;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 3046.

```text
g_info = 2;
  repeated string used_botchat_triggers = 3;
  repeated string used_board_events = 4;
  optional .chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo flip_board_mistake_debug_info = 5;
}

message RetryMistakeDebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional bool player_is_winning = 2;
  optional int32 ply_until_cooldown = 3;
}

message FlipB
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03288"></a>
## FND-03288: message declaration: chesscom.explanation_engine.v1.RetryMistakeDebugInfo

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RetryMistakeDebugInfo {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 3151.

```text
nal .chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo flip_board_mistake_debug_info = 5;
}

message RetryMistakeDebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional bool player_is_winning = 2;
  optional int32 ply_until_cooldown = 3;
}

message FlipBoardMistakeDebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification 
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03289"></a>
## FND-03289: chesscom.explanation_engine.v1.RetryMistakeDebugInfo.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 3185.

```text
1.FlipBoardMistakeDebugInfo flip_board_mistake_debug_info = 5;
}

message RetryMistakeDebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional bool player_is_winning = 2;
  optional int32 ply_until_cooldown = 3;
}

message FlipBoardMistakeDebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 ply_until_fl
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03290"></a>
## FND-03290: chesscom.explanation_engine.v1.RetryMistakeDebugInfo.player_is_winning = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool player_is_winning = 2;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 3272.

```text
ebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional bool player_is_winning = 2;
  optional int32 ply_until_cooldown = 3;
}

message FlipBoardMistakeDebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 ply_until_flip_board_cooldown = 2;
}

```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03291"></a>
## FND-03291: chesscom.explanation_engine.v1.RetryMistakeDebugInfo.ply_until_cooldown = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 ply_until_cooldown = 3;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 3311.

```text
tion_engine.v1.MoveClassification move_classification = 1;
  optional bool player_is_winning = 2;
  optional int32 ply_until_cooldown = 3;
}

message FlipBoardMistakeDebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 ply_until_flip_board_cooldown = 2;
}

```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03292"></a>
## FND-03292: message declaration: chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FlipBoardMistakeDebugInfo {

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 3353.

```text
ssification = 1;
  optional bool player_is_winning = 2;
  optional int32 ply_until_cooldown = 3;
}

message FlipBoardMistakeDebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 ply_until_flip_board_cooldown = 2;
}

```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03293"></a>
## FND-03293: chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 3185.

```text
1.FlipBoardMistakeDebugInfo flip_board_mistake_debug_info = 5;
}

message RetryMistakeDebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional bool player_is_winning = 2;
  optional int32 ply_until_cooldown = 3;
}

message FlipBoardMistakeDebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 ply_until_fl
```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03294"></a>
## FND-03294: chesscom.explanation_engine.v1.FlipBoardMistakeDebugInfo.ply_until_flip_board_cooldown = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 ply_until_flip_board_cooldown = 2;

### Evidence

- **SRC-0366** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_chat.proto` — [preserved redacted evidence](../evidence/text/45f5a923cd2439b4a741a8fced600c23304b3e8fcea515d766d502ab1f5ca46c.proto)
  Character offset 3478.

```text
ebugInfo {
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 ply_until_flip_board_cooldown = 2;
}

```

**Source references:** SRC-0366, SRC-1337  
**URL references:** None independently associated  
**Related findings:** FND-03234, FND-03235, FND-03236

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03295"></a>
## FND-03295: message declaration: chesscom.explanation_engine.v1.GetCoachHintRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCoachHintRequest {

### Evidence

- **SRC-0367** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_hint.proto` — [preserved redacted evidence](../evidence/text/a6f6ebde4e86f47cf08797c3d2da517cb826e32a58554e9f1316c6f0da82e269.proto)
  Character offset 131.

```text
_engine/v1/feature_get_coach_hint.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetCoachHintRequest {
}

message GetCoachHintResponse {
  oneof _hint {
  .chesscom.explanation_engine.v1.CoachHint hint = 1;
  }
}

message CoachHint {
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _speech_debug_info {
  .chesscom.explanation_engine.v1.SpeechDebugInfo speec
```

**Source references:** SRC-0367, SRC-1338  
**URL references:** None independently associated  
**Related findings:** FND-03296, FND-03297

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03296"></a>
## FND-03296: message declaration: chesscom.explanation_engine.v1.GetCoachHintResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCoachHintResponse {

### Evidence

- **SRC-0367** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_hint.proto` — [preserved redacted evidence](../evidence/text/a6f6ebde4e86f47cf08797c3d2da517cb826e32a58554e9f1316c6f0da82e269.proto)
  Character offset 164.

```text
.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetCoachHintRequest {
}

message GetCoachHintResponse {
  oneof _hint {
  .chesscom.explanation_engine.v1.CoachHint hint = 1;
  }
}

message CoachHint {
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _speech_debug_info {
  .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 3;
  }
  optional 
```

**Source references:** SRC-0367, SRC-1338  
**URL references:** None independently associated  
**Related findings:** FND-03295, FND-03297

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03297"></a>
## FND-03297: oneof declaration: chesscom.explanation_engine.v1.GetCoachHintResponse._hint

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _hint {

### Evidence

- **SRC-0367** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_hint.proto` — [preserved redacted evidence](../evidence/text/a6f6ebde4e86f47cf08797c3d2da517cb826e32a58554e9f1316c6f0da82e269.proto)
  Character offset 197.

```text
 chesscom.explanation_engine.v1;

message GetCoachHintRequest {
}

message GetCoachHintResponse {
  oneof _hint {
  .chesscom.explanation_engine.v1.CoachHint hint = 1;
  }
}

message CoachHint {
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _speech_debug_info {
  .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 3;
  }
  optional .chesscom.chess.v1.Move move = 1;
```

**Source references:** SRC-0367, SRC-1338  
**URL references:** None independently associated  
**Related findings:** FND-03295, FND-03296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03298"></a>
## FND-03298: chesscom.explanation_engine.v1.GetCoachHintResponse.hint = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.CoachHint hint = 1;

### Evidence

- **SRC-0367** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_hint.proto` — [preserved redacted evidence](../evidence/text/a6f6ebde4e86f47cf08797c3d2da517cb826e32a58554e9f1316c6f0da82e269.proto)
  Character offset 213.

```text
ation_engine.v1;

message GetCoachHintRequest {
}

message GetCoachHintResponse {
  oneof _hint {
  .chesscom.explanation_engine.v1.CoachHint hint = 1;
  }
}

message CoachHint {
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _speech_debug_info {
  .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 3;
  }
  optional .chesscom.chess.v1.Move move = 1;
}

```

**Source references:** SRC-0367, SRC-1338  
**URL references:** None independently associated  
**Related findings:** FND-03295, FND-03296, FND-03297

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03299"></a>
## FND-03299: message declaration: chesscom.explanation_engine.v1.CoachHint

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachHint {

### Evidence

- **SRC-0367** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_hint.proto` — [preserved redacted evidence](../evidence/text/a6f6ebde4e86f47cf08797c3d2da517cb826e32a58554e9f1316c6f0da82e269.proto)
  Character offset 272.

```text
GetCoachHintResponse {
  oneof _hint {
  .chesscom.explanation_engine.v1.CoachHint hint = 1;
  }
}

message CoachHint {
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _speech_debug_info {
  .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 3;
  }
  optional .chesscom.chess.v1.Move move = 1;
}

```

**Source references:** SRC-0367, SRC-1338  
**URL references:** None independently associated  
**Related findings:** FND-03295, FND-03296, FND-03297

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03300"></a>
## FND-03300: oneof declaration: chesscom.explanation_engine.v1.CoachHint._speech

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _speech {

### Evidence

- **SRC-0367** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_hint.proto` — [preserved redacted evidence](../evidence/text/a6f6ebde4e86f47cf08797c3d2da517cb826e32a58554e9f1316c6f0da82e269.proto)
  Character offset 294.

```text

  oneof _hint {
  .chesscom.explanation_engine.v1.CoachHint hint = 1;
  }
}

message CoachHint {
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _speech_debug_info {
  .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 3;
  }
  optional .chesscom.chess.v1.Move move = 1;
}

```

**Source references:** SRC-0367, SRC-1338  
**URL references:** None independently associated  
**Related findings:** FND-03295, FND-03296, FND-03297

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03301"></a>
## FND-03301: chesscom.explanation_engine.v1.CoachHint.speech = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.Speech speech = 2;

### Evidence

- **SRC-0367** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_hint.proto` — [preserved redacted evidence](../evidence/text/a6f6ebde4e86f47cf08797c3d2da517cb826e32a58554e9f1316c6f0da82e269.proto)
  Character offset 312.

```text
 .chesscom.explanation_engine.v1.CoachHint hint = 1;
  }
}

message CoachHint {
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _speech_debug_info {
  .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 3;
  }
  optional .chesscom.chess.v1.Move move = 1;
}

```

**Source references:** SRC-0367, SRC-1338  
**URL references:** None independently associated  
**Related findings:** FND-03295, FND-03296, FND-03297

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03302"></a>
## FND-03302: oneof declaration: chesscom.explanation_engine.v1.CoachHint._speech_debug_info

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _speech_debug_info {

### Evidence

- **SRC-0367** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_hint.proto` — [preserved redacted evidence](../evidence/text/a6f6ebde4e86f47cf08797c3d2da517cb826e32a58554e9f1316c6f0da82e269.proto)
  Character offset 369.

```text
}

message CoachHint {
  oneof _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _speech_debug_info {
  .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 3;
  }
  optional .chesscom.chess.v1.Move move = 1;
}

```

**Source references:** SRC-0367, SRC-1338  
**URL references:** None independently associated  
**Related findings:** FND-03295, FND-03296, FND-03297

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03303"></a>
## FND-03303: chesscom.explanation_engine.v1.CoachHint.speech_debug_info = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 3;

### Evidence

- **SRC-0367** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_hint.proto` — [preserved redacted evidence](../evidence/text/a6f6ebde4e86f47cf08797c3d2da517cb826e32a58554e9f1316c6f0da82e269.proto)
  Character offset 398.

```text
f _speech {
  .chesscom.explanation_engine.v1.Speech speech = 2;
  }
  oneof _speech_debug_info {
  .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 3;
  }
  optional .chesscom.chess.v1.Move move = 1;
}

```

**Source references:** SRC-0367, SRC-1338  
**URL references:** None independently associated  
**Related findings:** FND-03295, FND-03296, FND-03297

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03304"></a>
## FND-03304: chesscom.explanation_engine.v1.CoachHint.move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move move = 1;

### Evidence

- **SRC-0367** `research/proto/chesscom/explanation_engine/v1/feature_get_coach_hint.proto` — [preserved redacted evidence](../evidence/text/a6f6ebde4e86f47cf08797c3d2da517cb826e32a58554e9f1316c6f0da82e269.proto)
  Character offset 475.

```text
_speech_debug_info {
  .chesscom.explanation_engine.v1.SpeechDebugInfo speech_debug_info = 3;
  }
  optional .chesscom.chess.v1.Move move = 1;
}

```

**Source references:** SRC-0367, SRC-1338  
**URL references:** None independently associated  
**Related findings:** FND-03295, FND-03296, FND-03297

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03305"></a>
## FND-03305: message declaration: chesscom.explanation_engine.v1.GetCompressedPositionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCompressedPositionRequest {

### Evidence

- **SRC-0368** `research/proto/chesscom/explanation_engine/v1/feature_get_compressed_position.proto` — [preserved redacted evidence](../evidence/text/43fa20ac176614cc1787f950c1158115861b3c1eb5b777121c992726a90f6479.proto)
  Character offset 140.

```text
1/feature_get_compressed_position.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetCompressedPositionRequest {
  oneof position_to_convert {
  .chesscom.chess.v1.Position position = 1;
  string fen = 2;
  }
}

message GetCompressedPositionResponse {
  optional bytes compressed_position = 1;
}

```

**Source references:** SRC-0368, SRC-1339  
**URL references:** None independently associated  
**Related findings:** FND-03306, FND-03307

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03306"></a>
## FND-03306: oneof declaration: chesscom.explanation_engine.v1.GetCompressedPositionRequest.position_to_convert

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof position_to_convert {

### Evidence

- **SRC-0368** `research/proto/chesscom/explanation_engine/v1/feature_get_compressed_position.proto` — [preserved redacted evidence](../evidence/text/43fa20ac176614cc1787f950c1158115861b3c1eb5b777121c992726a90f6479.proto)
  Character offset 181.

```text
/ syntax: proto3

package chesscom.explanation_engine.v1;

message GetCompressedPositionRequest {
  oneof position_to_convert {
  .chesscom.chess.v1.Position position = 1;
  string fen = 2;
  }
}

message GetCompressedPositionResponse {
  optional bytes compressed_position = 1;
}

```

**Source references:** SRC-0368, SRC-1339  
**URL references:** None independently associated  
**Related findings:** FND-03305, FND-03307

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03307"></a>
## FND-03307: chesscom.explanation_engine.v1.GetCompressedPositionRequest.position = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Position position = 1;

### Evidence

- **SRC-0368** `research/proto/chesscom/explanation_engine/v1/feature_get_compressed_position.proto` — [preserved redacted evidence](../evidence/text/43fa20ac176614cc1787f950c1158115861b3c1eb5b777121c992726a90f6479.proto)
  Character offset 211.

```text
scom.explanation_engine.v1;

message GetCompressedPositionRequest {
  oneof position_to_convert {
  .chesscom.chess.v1.Position position = 1;
  string fen = 2;
  }
}

message GetCompressedPositionResponse {
  optional bytes compressed_position = 1;
}

```

**Source references:** SRC-0368, SRC-1339  
**URL references:** None independently associated  
**Related findings:** FND-03305, FND-03306

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03308"></a>
## FND-03308: chesscom.explanation_engine.v1.GetCompressedPositionRequest.fen = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string fen = 2;

### Evidence

- **SRC-0368** `research/proto/chesscom/explanation_engine/v1/feature_get_compressed_position.proto` — [preserved redacted evidence](../evidence/text/43fa20ac176614cc1787f950c1158115861b3c1eb5b777121c992726a90f6479.proto)
  Character offset 255.

```text
ressedPositionRequest {
  oneof position_to_convert {
  .chesscom.chess.v1.Position position = 1;
  string fen = 2;
  }
}

message GetCompressedPositionResponse {
  optional bytes compressed_position = 1;
}

```

**Source references:** SRC-0368, SRC-1339  
**URL references:** None independently associated  
**Related findings:** FND-03305, FND-03306, FND-03307

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03309"></a>
## FND-03309: message declaration: chesscom.explanation_engine.v1.GetCompressedPositionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCompressedPositionResponse {

### Evidence

- **SRC-0368** `research/proto/chesscom/explanation_engine/v1/feature_get_compressed_position.proto` — [preserved redacted evidence](../evidence/text/43fa20ac176614cc1787f950c1158115861b3c1eb5b777121c992726a90f6479.proto)
  Character offset 278.

```text

  oneof position_to_convert {
  .chesscom.chess.v1.Position position = 1;
  string fen = 2;
  }
}

message GetCompressedPositionResponse {
  optional bytes compressed_position = 1;
}

```

**Source references:** SRC-0368, SRC-1339  
**URL references:** None independently associated  
**Related findings:** FND-03305, FND-03306, FND-03307

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03310"></a>
## FND-03310: chesscom.explanation_engine.v1.GetCompressedPositionResponse.compressed_position = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bytes compressed_position = 1;

### Evidence

- **SRC-0368** `research/proto/chesscom/explanation_engine/v1/feature_get_compressed_position.proto` — [preserved redacted evidence](../evidence/text/43fa20ac176614cc1787f950c1158115861b3c1eb5b777121c992726a90f6479.proto)
  Character offset 320.

```text
.chess.v1.Position position = 1;
  string fen = 2;
  }
}

message GetCompressedPositionResponse {
  optional bytes compressed_position = 1;
}

```

**Source references:** SRC-0368, SRC-1339  
**URL references:** None independently associated  
**Related findings:** FND-03305, FND-03306, FND-03307

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03311"></a>
## FND-03311: message declaration: chesscom.explanation_engine.v1.GetErgonomicGameRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetErgonomicGameRequest {

### Evidence

- **SRC-0369** `research/proto/chesscom/explanation_engine/v1/feature_get_ergonomic_game.proto` — [preserved redacted evidence](../evidence/text/ab3ecb952e6b61917e36e74b78701622537bf01f027723a3eff4a22b9ff4b8d9.proto)
  Character offset 135.

```text
ine/v1/feature_get_ergonomic_game.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetErgonomicGameRequest {
  oneof game_to_convert {
  .chesscom.explanation_engine.v1.GameState game_state = 1;
  string pgn = 2;
  int32 starting_game_point = 3;
  }
}

message GetErgonomicGameResponse {
  optional .chesscom.chess.v1.Game game = 1;
}

```

**Source references:** SRC-0369, SRC-1340  
**URL references:** None independently associated  
**Related findings:** FND-03312, FND-03313

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03312"></a>
## FND-03312: oneof declaration: chesscom.explanation_engine.v1.GetErgonomicGameRequest.game_to_convert

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof game_to_convert {

### Evidence

- **SRC-0369** `research/proto/chesscom/explanation_engine/v1/feature_get_ergonomic_game.proto` — [preserved redacted evidence](../evidence/text/ab3ecb952e6b61917e36e74b78701622537bf01f027723a3eff4a22b9ff4b8d9.proto)
  Character offset 171.

```text
oto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetErgonomicGameRequest {
  oneof game_to_convert {
  .chesscom.explanation_engine.v1.GameState game_state = 1;
  string pgn = 2;
  int32 starting_game_point = 3;
  }
}

message GetErgonomicGameResponse {
  optional .chesscom.chess.v1.Game game = 1;
}

```

**Source references:** SRC-0369, SRC-1340  
**URL references:** None independently associated  
**Related findings:** FND-03311, FND-03313

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03313"></a>
## FND-03313: chesscom.explanation_engine.v1.GetErgonomicGameRequest.game_state = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.GameState game_state = 1;

### Evidence

- **SRC-0369** `research/proto/chesscom/explanation_engine/v1/feature_get_ergonomic_game.proto` — [preserved redacted evidence](../evidence/text/ab3ecb952e6b61917e36e74b78701622537bf01f027723a3eff4a22b9ff4b8d9.proto)
  Character offset 197.

```text
kage chesscom.explanation_engine.v1;

message GetErgonomicGameRequest {
  oneof game_to_convert {
  .chesscom.explanation_engine.v1.GameState game_state = 1;
  string pgn = 2;
  int32 starting_game_point = 3;
  }
}

message GetErgonomicGameResponse {
  optional .chesscom.chess.v1.Game game = 1;
}

```

**Source references:** SRC-0369, SRC-1340  
**URL references:** None independently associated  
**Related findings:** FND-03311, FND-03312

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03314"></a>
## FND-03314: chesscom.explanation_engine.v1.GetErgonomicGameRequest.pgn = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string pgn = 2;

### Evidence

- **SRC-0369** `research/proto/chesscom/explanation_engine/v1/feature_get_ergonomic_game.proto` — [preserved redacted evidence](../evidence/text/ab3ecb952e6b61917e36e74b78701622537bf01f027723a3eff4a22b9ff4b8d9.proto)
  Character offset 257.

```text
meRequest {
  oneof game_to_convert {
  .chesscom.explanation_engine.v1.GameState game_state = 1;
  string pgn = 2;
  int32 starting_game_point = 3;
  }
}

message GetErgonomicGameResponse {
  optional .chesscom.chess.v1.Game game = 1;
}

```

**Source references:** SRC-0369, SRC-1340  
**URL references:** None independently associated  
**Related findings:** FND-03311, FND-03312, FND-03313

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03315"></a>
## FND-03315: chesscom.explanation_engine.v1.GetErgonomicGameRequest.starting_game_point = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 starting_game_point = 3;

### Evidence

- **SRC-0369** `research/proto/chesscom/explanation_engine/v1/feature_get_ergonomic_game.proto` — [preserved redacted evidence](../evidence/text/ab3ecb952e6b61917e36e74b78701622537bf01f027723a3eff4a22b9ff4b8d9.proto)
  Character offset 275.

```text
f game_to_convert {
  .chesscom.explanation_engine.v1.GameState game_state = 1;
  string pgn = 2;
  int32 starting_game_point = 3;
  }
}

message GetErgonomicGameResponse {
  optional .chesscom.chess.v1.Game game = 1;
}

```

**Source references:** SRC-0369, SRC-1340  
**URL references:** None independently associated  
**Related findings:** FND-03311, FND-03312, FND-03313

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03316"></a>
## FND-03316: message declaration: chesscom.explanation_engine.v1.GetErgonomicGameResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetErgonomicGameResponse {

### Evidence

- **SRC-0369** `research/proto/chesscom/explanation_engine/v1/feature_get_ergonomic_game.proto` — [preserved redacted evidence](../evidence/text/ab3ecb952e6b61917e36e74b78701622537bf01f027723a3eff4a22b9ff4b8d9.proto)
  Character offset 313.

```text
ation_engine.v1.GameState game_state = 1;
  string pgn = 2;
  int32 starting_game_point = 3;
  }
}

message GetErgonomicGameResponse {
  optional .chesscom.chess.v1.Game game = 1;
}

```

**Source references:** SRC-0369, SRC-1340  
**URL references:** None independently associated  
**Related findings:** FND-03311, FND-03312, FND-03313

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03317"></a>
## FND-03317: chesscom.explanation_engine.v1.GetErgonomicGameResponse.game = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Game game = 1;

### Evidence

- **SRC-0369** `research/proto/chesscom/explanation_engine/v1/feature_get_ergonomic_game.proto` — [preserved redacted evidence](../evidence/text/ab3ecb952e6b61917e36e74b78701622537bf01f027723a3eff4a22b9ff4b8d9.proto)
  Character offset 350.

```text
= 1;
  string pgn = 2;
  int32 starting_game_point = 3;
  }
}

message GetErgonomicGameResponse {
  optional .chesscom.chess.v1.Game game = 1;
}

```

**Source references:** SRC-0369, SRC-1340  
**URL references:** None independently associated  
**Related findings:** FND-03311, FND-03312, FND-03313

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03318"></a>
## FND-03318: message declaration: chesscom.explanation_engine.v1.GetErgonomicPositionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetErgonomicPositionRequest {

### Evidence

- **SRC-0370** `research/proto/chesscom/explanation_engine/v1/feature_get_ergonomic_position.proto` — [preserved redacted evidence](../evidence/text/b0995fb51e880e972a44e2360082610b6c1247efd68a03e7d657d4ba1d54cb5f.proto)
  Character offset 139.

```text
v1/feature_get_ergonomic_position.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetErgonomicPositionRequest {
  oneof position_to_convert {
  bytes compressed_position = 1;
  string fen = 2;
  }
}

message GetErgonomicPositionResponse {
  optional .chesscom.chess.v1.Position position = 1;
}

```

**Source references:** SRC-0370, SRC-1341  
**URL references:** None independently associated  
**Related findings:** FND-03319, FND-03320

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03319"></a>
## FND-03319: oneof declaration: chesscom.explanation_engine.v1.GetErgonomicPositionRequest.position_to_convert

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof position_to_convert {

### Evidence

- **SRC-0370** `research/proto/chesscom/explanation_engine/v1/feature_get_ergonomic_position.proto` — [preserved redacted evidence](../evidence/text/b0995fb51e880e972a44e2360082610b6c1247efd68a03e7d657d4ba1d54cb5f.proto)
  Character offset 179.

```text
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetErgonomicPositionRequest {
  oneof position_to_convert {
  bytes compressed_position = 1;
  string fen = 2;
  }
}

message GetErgonomicPositionResponse {
  optional .chesscom.chess.v1.Position position = 1;
}

```

**Source references:** SRC-0370, SRC-1341  
**URL references:** None independently associated  
**Related findings:** FND-03318, FND-03320

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03320"></a>
## FND-03320: chesscom.explanation_engine.v1.GetErgonomicPositionRequest.compressed_position = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bytes compressed_position = 1;

### Evidence

- **SRC-0370** `research/proto/chesscom/explanation_engine/v1/feature_get_ergonomic_position.proto` — [preserved redacted evidence](../evidence/text/b0995fb51e880e972a44e2360082610b6c1247efd68a03e7d657d4ba1d54cb5f.proto)
  Character offset 209.

```text
sscom.explanation_engine.v1;

message GetErgonomicPositionRequest {
  oneof position_to_convert {
  bytes compressed_position = 1;
  string fen = 2;
  }
}

message GetErgonomicPositionResponse {
  optional .chesscom.chess.v1.Position position = 1;
}

```

**Source references:** SRC-0370, SRC-1341  
**URL references:** None independently associated  
**Related findings:** FND-03318, FND-03319

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03321"></a>
## FND-03321: chesscom.explanation_engine.v1.GetErgonomicPositionRequest.fen = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string fen = 2;

### Evidence

- **SRC-0370** `research/proto/chesscom/explanation_engine/v1/feature_get_ergonomic_position.proto` — [preserved redacted evidence](../evidence/text/b0995fb51e880e972a44e2360082610b6c1247efd68a03e7d657d4ba1d54cb5f.proto)
  Character offset 242.

```text
sage GetErgonomicPositionRequest {
  oneof position_to_convert {
  bytes compressed_position = 1;
  string fen = 2;
  }
}

message GetErgonomicPositionResponse {
  optional .chesscom.chess.v1.Position position = 1;
}

```

**Source references:** SRC-0370, SRC-1341  
**URL references:** None independently associated  
**Related findings:** FND-03318, FND-03319, FND-03320

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03322"></a>
## FND-03322: message declaration: chesscom.explanation_engine.v1.GetErgonomicPositionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetErgonomicPositionResponse {

### Evidence

- **SRC-0370** `research/proto/chesscom/explanation_engine/v1/feature_get_ergonomic_position.proto` — [preserved redacted evidence](../evidence/text/b0995fb51e880e972a44e2360082610b6c1247efd68a03e7d657d4ba1d54cb5f.proto)
  Character offset 265.

```text
onRequest {
  oneof position_to_convert {
  bytes compressed_position = 1;
  string fen = 2;
  }
}

message GetErgonomicPositionResponse {
  optional .chesscom.chess.v1.Position position = 1;
}

```

**Source references:** SRC-0370, SRC-1341  
**URL references:** None independently associated  
**Related findings:** FND-03318, FND-03319, FND-03320

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03323"></a>
## FND-03323: chesscom.explanation_engine.v1.GetErgonomicPositionResponse.position = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Position position = 1;

### Evidence

- **SRC-0370** `research/proto/chesscom/explanation_engine/v1/feature_get_ergonomic_position.proto` — [preserved redacted evidence](../evidence/text/b0995fb51e880e972a44e2360082610b6c1247efd68a03e7d657d4ba1d54cb5f.proto)
  Character offset 306.

```text

  bytes compressed_position = 1;
  string fen = 2;
  }
}

message GetErgonomicPositionResponse {
  optional .chesscom.chess.v1.Position position = 1;
}

```

**Source references:** SRC-0370, SRC-1341  
**URL references:** None independently associated  
**Related findings:** FND-03318, FND-03319, FND-03320

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03324"></a>
## FND-03324: message declaration: chesscom.explanation_engine.v1.GetFenRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetFenRequest {

### Evidence

- **SRC-0371** `research/proto/chesscom/explanation_engine/v1/feature_get_fen.proto` — [preserved redacted evidence](../evidence/text/aa6072ee3a83f8d90da261be226252d18b3f984f84273b02fd010d4b906188b2.proto)
  Character offset 124.

```text
anation_engine/v1/feature_get_fen.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetFenRequest {
  oneof position_to_convert {
  .chesscom.chess.v1.Position position = 1;
  bytes compressed_position = 2;
  }
  oneof _fen_notation {
  .chesscom.explanation_engine.v1.FenNotation fen_notation = 3;
  }
}

message GetFenResponse {
  optional string fen = 1;
}

```

**Source references:** SRC-0371, SRC-1342  
**URL references:** None independently associated  
**Related findings:** FND-03325, FND-03326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03325"></a>
## FND-03325: oneof declaration: chesscom.explanation_engine.v1.GetFenRequest.position_to_convert

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof position_to_convert {

### Evidence

- **SRC-0371** `research/proto/chesscom/explanation_engine/v1/feature_get_fen.proto` — [preserved redacted evidence](../evidence/text/aa6072ee3a83f8d90da261be226252d18b3f984f84273b02fd010d4b906188b2.proto)
  Character offset 150.

```text
get_fen.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetFenRequest {
  oneof position_to_convert {
  .chesscom.chess.v1.Position position = 1;
  bytes compressed_position = 2;
  }
  oneof _fen_notation {
  .chesscom.explanation_engine.v1.FenNotation fen_notation = 3;
  }
}

message GetFenResponse {
  optional string fen = 1;
}

```

**Source references:** SRC-0371, SRC-1342  
**URL references:** None independently associated  
**Related findings:** FND-03324, FND-03326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03326"></a>
## FND-03326: chesscom.explanation_engine.v1.GetFenRequest.position = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Position position = 1;

### Evidence

- **SRC-0371** `research/proto/chesscom/explanation_engine/v1/feature_get_fen.proto` — [preserved redacted evidence](../evidence/text/aa6072ee3a83f8d90da261be226252d18b3f984f84273b02fd010d4b906188b2.proto)
  Character offset 180.

```text
3

package chesscom.explanation_engine.v1;

message GetFenRequest {
  oneof position_to_convert {
  .chesscom.chess.v1.Position position = 1;
  bytes compressed_position = 2;
  }
  oneof _fen_notation {
  .chesscom.explanation_engine.v1.FenNotation fen_notation = 3;
  }
}

message GetFenResponse {
  optional string fen = 1;
}

```

**Source references:** SRC-0371, SRC-1342  
**URL references:** None independently associated  
**Related findings:** FND-03324, FND-03325

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03327"></a>
## FND-03327: chesscom.explanation_engine.v1.GetFenRequest.compressed_position = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bytes compressed_position = 2;

### Evidence

- **SRC-0371** `research/proto/chesscom/explanation_engine/v1/feature_get_fen.proto` — [preserved redacted evidence](../evidence/text/aa6072ee3a83f8d90da261be226252d18b3f984f84273b02fd010d4b906188b2.proto)
  Character offset 224.

```text
message GetFenRequest {
  oneof position_to_convert {
  .chesscom.chess.v1.Position position = 1;
  bytes compressed_position = 2;
  }
  oneof _fen_notation {
  .chesscom.explanation_engine.v1.FenNotation fen_notation = 3;
  }
}

message GetFenResponse {
  optional string fen = 1;
}

```

**Source references:** SRC-0371, SRC-1342  
**URL references:** None independently associated  
**Related findings:** FND-03324, FND-03325, FND-03326

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03328"></a>
## FND-03328: oneof declaration: chesscom.explanation_engine.v1.GetFenRequest._fen_notation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fen_notation {

### Evidence

- **SRC-0371** `research/proto/chesscom/explanation_engine/v1/feature_get_fen.proto` — [preserved redacted evidence](../evidence/text/aa6072ee3a83f8d90da261be226252d18b3f984f84273b02fd010d4b906188b2.proto)
  Character offset 261.

```text
ion_to_convert {
  .chesscom.chess.v1.Position position = 1;
  bytes compressed_position = 2;
  }
  oneof _fen_notation {
  .chesscom.explanation_engine.v1.FenNotation fen_notation = 3;
  }
}

message GetFenResponse {
  optional string fen = 1;
}

```

**Source references:** SRC-0371, SRC-1342  
**URL references:** None independently associated  
**Related findings:** FND-03324, FND-03325, FND-03326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03329"></a>
## FND-03329: chesscom.explanation_engine.v1.GetFenRequest.fen_notation = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.FenNotation fen_notation = 3;

### Evidence

- **SRC-0371** `research/proto/chesscom/explanation_engine/v1/feature_get_fen.proto` — [preserved redacted evidence](../evidence/text/aa6072ee3a83f8d90da261be226252d18b3f984f84273b02fd010d4b906188b2.proto)
  Character offset 285.

```text
scom.chess.v1.Position position = 1;
  bytes compressed_position = 2;
  }
  oneof _fen_notation {
  .chesscom.explanation_engine.v1.FenNotation fen_notation = 3;
  }
}

message GetFenResponse {
  optional string fen = 1;
}

```

**Source references:** SRC-0371, SRC-1342  
**URL references:** None independently associated  
**Related findings:** FND-03324, FND-03325, FND-03326

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03330"></a>
## FND-03330: message declaration: chesscom.explanation_engine.v1.GetFenResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetFenResponse {

### Evidence

- **SRC-0371** `research/proto/chesscom/explanation_engine/v1/feature_get_fen.proto` — [preserved redacted evidence](../evidence/text/aa6072ee3a83f8d90da261be226252d18b3f984f84273b02fd010d4b906188b2.proto)
  Character offset 354.

```text

  }
  oneof _fen_notation {
  .chesscom.explanation_engine.v1.FenNotation fen_notation = 3;
  }
}

message GetFenResponse {
  optional string fen = 1;
}

```

**Source references:** SRC-0371, SRC-1342  
**URL references:** None independently associated  
**Related findings:** FND-03324, FND-03325, FND-03326

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03331"></a>
## FND-03331: chesscom.explanation_engine.v1.GetFenResponse.fen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string fen = 1;

### Evidence

- **SRC-0371** `research/proto/chesscom/explanation_engine/v1/feature_get_fen.proto` — [preserved redacted evidence](../evidence/text/aa6072ee3a83f8d90da261be226252d18b3f984f84273b02fd010d4b906188b2.proto)
  Character offset 381.

```text
{
  .chesscom.explanation_engine.v1.FenNotation fen_notation = 3;
  }
}

message GetFenResponse {
  optional string fen = 1;
}

```

**Source references:** SRC-0371, SRC-1342  
**URL references:** None independently associated  
**Related findings:** FND-03324, FND-03325, FND-03326

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03332"></a>
## FND-03332: message declaration: chesscom.explanation_engine.v1.GetGameResultRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetGameResultRequest {

### Evidence

- **SRC-0372** `research/proto/chesscom/explanation_engine/v1/feature_get_game_result.proto` — [preserved redacted evidence](../evidence/text/155e9924d3bddf159d6ca0b5329f56a0482a3554bc6609e3abbcc1f877fedcad.proto)
  Character offset 132.

```text
engine/v1/feature_get_game_result.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetGameResultRequest {
}

message GetGameResultResponse {
  oneof _game_result {
  .chesscom.chess.v1.GameResult game_result = 1;
  }
}

```

**Source references:** SRC-0372, SRC-1343  
**URL references:** None independently associated  
**Related findings:** FND-03333, FND-03334

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03333"></a>
## FND-03333: message declaration: chesscom.explanation_engine.v1.GetGameResultResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetGameResultResponse {

### Evidence

- **SRC-0372** `research/proto/chesscom/explanation_engine/v1/feature_get_game_result.proto` — [preserved redacted evidence](../evidence/text/155e9924d3bddf159d6ca0b5329f56a0482a3554bc6609e3abbcc1f877fedcad.proto)
  Character offset 166.

```text
proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetGameResultRequest {
}

message GetGameResultResponse {
  oneof _game_result {
  .chesscom.chess.v1.GameResult game_result = 1;
  }
}

```

**Source references:** SRC-0372, SRC-1343  
**URL references:** None independently associated  
**Related findings:** FND-03332, FND-03334

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03334"></a>
## FND-03334: oneof declaration: chesscom.explanation_engine.v1.GetGameResultResponse._game_result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_result {

### Evidence

- **SRC-0372** `research/proto/chesscom/explanation_engine/v1/feature_get_game_result.proto` — [preserved redacted evidence](../evidence/text/155e9924d3bddf159d6ca0b5329f56a0482a3554bc6609e3abbcc1f877fedcad.proto)
  Character offset 200.

```text
hesscom.explanation_engine.v1;

message GetGameResultRequest {
}

message GetGameResultResponse {
  oneof _game_result {
  .chesscom.chess.v1.GameResult game_result = 1;
  }
}

```

**Source references:** SRC-0372, SRC-1343  
**URL references:** None independently associated  
**Related findings:** FND-03332, FND-03333

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03335"></a>
## FND-03335: chesscom.explanation_engine.v1.GetGameResultResponse.game_result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.GameResult game_result = 1;

### Evidence

- **SRC-0372** `research/proto/chesscom/explanation_engine/v1/feature_get_game_result.proto` — [preserved redacted evidence](../evidence/text/155e9924d3bddf159d6ca0b5329f56a0482a3554bc6609e3abbcc1f877fedcad.proto)
  Character offset 223.

```text
ine.v1;

message GetGameResultRequest {
}

message GetGameResultResponse {
  oneof _game_result {
  .chesscom.chess.v1.GameResult game_result = 1;
  }
}

```

**Source references:** SRC-0372, SRC-1343  
**URL references:** None independently associated  
**Related findings:** FND-03332, FND-03333, FND-03334

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03336"></a>
## FND-03336: message declaration: chesscom.explanation_engine.v1.GetGameStateRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetGameStateRequest {

### Evidence

- **SRC-0373** `research/proto/chesscom/explanation_engine/v1/feature_get_game_state.proto` — [preserved redacted evidence](../evidence/text/f266a624d6eec9c42b0bc12756a0f946b37bcc23b1ecc489c9c0f719e5781faf.proto)
  Character offset 131.

```text
_engine/v1/feature_get_game_state.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetGameStateRequest {
}

message GetGameStateResponse {
  optional .chesscom.explanation_engine.v1.GameState game_state = 1;
}

```

**Source references:** SRC-0373, SRC-1344  
**URL references:** None independently associated  
**Related findings:** FND-03337, FND-03338

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03337"></a>
## FND-03337: message declaration: chesscom.explanation_engine.v1.GetGameStateResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetGameStateResponse {

### Evidence

- **SRC-0373** `research/proto/chesscom/explanation_engine/v1/feature_get_game_state.proto` — [preserved redacted evidence](../evidence/text/f266a624d6eec9c42b0bc12756a0f946b37bcc23b1ecc489c9c0f719e5781faf.proto)
  Character offset 164.

```text
.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetGameStateRequest {
}

message GetGameStateResponse {
  optional .chesscom.explanation_engine.v1.GameState game_state = 1;
}

```

**Source references:** SRC-0373, SRC-1344  
**URL references:** None independently associated  
**Related findings:** FND-03336, FND-03338

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03338"></a>
## FND-03338: chesscom.explanation_engine.v1.GetGameStateResponse.game_state = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GameState game_state = 1;

### Evidence

- **SRC-0373** `research/proto/chesscom/explanation_engine/v1/feature_get_game_state.proto` — [preserved redacted evidence](../evidence/text/f266a624d6eec9c42b0bc12756a0f946b37bcc23b1ecc489c9c0f719e5781faf.proto)
  Character offset 197.

```text
 chesscom.explanation_engine.v1;

message GetGameStateRequest {
}

message GetGameStateResponse {
  optional .chesscom.explanation_engine.v1.GameState game_state = 1;
}

```

**Source references:** SRC-0373, SRC-1344  
**URL references:** None independently associated  
**Related findings:** FND-03336, FND-03337

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03339"></a>
## FND-03339: enum declaration: chesscom.explanation_engine.v1.IllegalMoveCase

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum IllegalMoveCase {

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 145.

```text
ture_get_illegal_move_explanation.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum IllegalMoveCase {
  ILLEGAL_MOVE_CASE_UNSPECIFIED = 0;
  ILLEGAL_MOVE_CASE_IN_CHECK = 1;
  ILLEGAL_MOVE_CASE_PIECE_PINNED_TO_KING = 2;
  ILLEGAL_MOVE_CASE_PIECE_HAS_OTHER_LEGAL_MOVES = 3;
  ILLEGAL_MOVE_CASE_PIECE_HAS_NO_LEGAL_MOVES = 4;
  ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE = 5;
  ILLEGAL_MOVE_CASE_PAWN_HAS_N
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03340"></a>
## FND-03340: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ILLEGAL_MOVE_CASE_UNSPECIFIED = 0;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 170.

```text
lanation.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum IllegalMoveCase {
  ILLEGAL_MOVE_CASE_UNSPECIFIED = 0;
  ILLEGAL_MOVE_CASE_IN_CHECK = 1;
  ILLEGAL_MOVE_CASE_PIECE_PINNED_TO_KING = 2;
  ILLEGAL_MOVE_CASE_PIECE_HAS_OTHER_LEGAL_MOVES = 3;
  ILLEGAL_MOVE_CASE_PIECE_HAS_NO_LEGAL_MOVES = 4;
  ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE = 5;
  ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES = 6;
  ILLE
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03341"></a>
## FND-03341: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_IN_CHECK = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ILLEGAL_MOVE_CASE_IN_CHECK = 1;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 207.

```text
kage chesscom.explanation_engine.v1;

enum IllegalMoveCase {
  ILLEGAL_MOVE_CASE_UNSPECIFIED = 0;
  ILLEGAL_MOVE_CASE_IN_CHECK = 1;
  ILLEGAL_MOVE_CASE_PIECE_PINNED_TO_KING = 2;
  ILLEGAL_MOVE_CASE_PIECE_HAS_OTHER_LEGAL_MOVES = 3;
  ILLEGAL_MOVE_CASE_PIECE_HAS_NO_LEGAL_MOVES = 4;
  ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE = 5;
  ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES = 6;
  ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED = 7;

```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03342"></a>
## FND-03342: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_PIECE_PINNED_TO_KING = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ILLEGAL_MOVE_CASE_PIECE_PINNED_TO_KING = 2;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 241.

```text
1;

enum IllegalMoveCase {
  ILLEGAL_MOVE_CASE_UNSPECIFIED = 0;
  ILLEGAL_MOVE_CASE_IN_CHECK = 1;
  ILLEGAL_MOVE_CASE_PIECE_PINNED_TO_KING = 2;
  ILLEGAL_MOVE_CASE_PIECE_HAS_OTHER_LEGAL_MOVES = 3;
  ILLEGAL_MOVE_CASE_PIECE_HAS_NO_LEGAL_MOVES = 4;
  ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE = 5;
  ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES = 6;
  ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED = 7;
  ILLEGAL_MOVE_CASE_CASTLE_IN_CHEC
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03343"></a>
## FND-03343: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_PIECE_HAS_OTHER_LEGAL_MOVES = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ILLEGAL_MOVE_CASE_PIECE_HAS_OTHER_LEGAL_MOVES = 3;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 287.

```text
_UNSPECIFIED = 0;
  ILLEGAL_MOVE_CASE_IN_CHECK = 1;
  ILLEGAL_MOVE_CASE_PIECE_PINNED_TO_KING = 2;
  ILLEGAL_MOVE_CASE_PIECE_HAS_OTHER_LEGAL_MOVES = 3;
  ILLEGAL_MOVE_CASE_PIECE_HAS_NO_LEGAL_MOVES = 4;
  ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE = 5;
  ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES = 6;
  ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED = 7;
  ILLEGAL_MOVE_CASE_CASTLE_IN_CHECK = 8;
  ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHEC
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03344"></a>
## FND-03344: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_PIECE_HAS_NO_LEGAL_MOVES = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ILLEGAL_MOVE_CASE_PIECE_HAS_NO_LEGAL_MOVES = 4;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 340.

```text
 ILLEGAL_MOVE_CASE_PIECE_PINNED_TO_KING = 2;
  ILLEGAL_MOVE_CASE_PIECE_HAS_OTHER_LEGAL_MOVES = 3;
  ILLEGAL_MOVE_CASE_PIECE_HAS_NO_LEGAL_MOVES = 4;
  ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE = 5;
  ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES = 6;
  ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED = 7;
  ILLEGAL_MOVE_CASE_CASTLE_IN_CHECK = 8;
  ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHECK = 9;
}

enum IllegalMoveExplanationMode {
  ILLEGAL
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03345"></a>
## FND-03345: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE = 5;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 390.

```text
EGAL_MOVE_CASE_PIECE_HAS_OTHER_LEGAL_MOVES = 3;
  ILLEGAL_MOVE_CASE_PIECE_HAS_NO_LEGAL_MOVES = 4;
  ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE = 5;
  ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES = 6;
  ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED = 7;
  ILLEGAL_MOVE_CASE_CASTLE_IN_CHECK = 8;
  ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHECK = 9;
}

enum IllegalMoveExplanationMode {
  ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED = 0;
  ILLEGAL_
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03346"></a>
## FND-03346: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES = 6;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 437.

```text

  ILLEGAL_MOVE_CASE_PIECE_HAS_NO_LEGAL_MOVES = 4;
  ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE = 5;
  ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES = 6;
  ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED = 7;
  ILLEGAL_MOVE_CASE_CASTLE_IN_CHECK = 8;
  ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHECK = 9;
}

enum IllegalMoveExplanationMode {
  ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED = 0;
  ILLEGAL_MOVE_EXPLANATION_MODE_ALL = 1;
  ILLEGAL_MOVE_E
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03347"></a>
## FND-03347: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED = 7;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 486.

```text
;
  ILLEGAL_MOVE_CASE_PAWN_CAN_ONLY_CAPTURE = 5;
  ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES = 6;
  ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED = 7;
  ILLEGAL_MOVE_CASE_CASTLE_IN_CHECK = 8;
  ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHECK = 9;
}

enum IllegalMoveExplanationMode {
  ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED = 0;
  ILLEGAL_MOVE_EXPLANATION_MODE_ALL = 1;
  ILLEGAL_MOVE_EXPLANATION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MO
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03348"></a>
## FND-03348: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_CASTLE_IN_CHECK = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ILLEGAL_MOVE_CASE_CASTLE_IN_CHECK = 8;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 529.

```text
 = 5;
  ILLEGAL_MOVE_CASE_PAWN_HAS_NO_LEGAL_MOVES = 6;
  ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED = 7;
  ILLEGAL_MOVE_CASE_CASTLE_IN_CHECK = 8;
  ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHECK = 9;
}

enum IllegalMoveExplanationMode {
  ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED = 0;
  ILLEGAL_MOVE_EXPLANATION_MODE_ALL = 1;
  ILLEGAL_MOVE_EXPLANATION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MOVES = 2;
}

message GetIllegalMoveExplanati
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03349"></a>
## FND-03349: chesscom.explanation_engine.v1.IllegalMoveCase.ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHECK = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHECK = 9;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 570.

```text
AL_MOVES = 6;
  ILLEGAL_MOVE_CASE_CASTLE_KING_MOVED = 7;
  ILLEGAL_MOVE_CASE_CASTLE_IN_CHECK = 8;
  ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHECK = 9;
}

enum IllegalMoveExplanationMode {
  ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED = 0;
  ILLEGAL_MOVE_EXPLANATION_MODE_ALL = 1;
  ILLEGAL_MOVE_EXPLANATION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MOVES = 2;
}

message GetIllegalMoveExplanationRequest {
  optional .chesscom.chess.v1
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03350"></a>
## FND-03350: enum declaration: chesscom.explanation_engine.v1.IllegalMoveExplanationMode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum IllegalMoveExplanationMode {

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 617.

```text
OVED = 7;
  ILLEGAL_MOVE_CASE_CASTLE_IN_CHECK = 8;
  ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHECK = 9;
}

enum IllegalMoveExplanationMode {
  ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED = 0;
  ILLEGAL_MOVE_EXPLANATION_MODE_ALL = 1;
  ILLEGAL_MOVE_EXPLANATION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MOVES = 2;
}

message GetIllegalMoveExplanationRequest {
  optional .chesscom.chess.v1.Move attempted_move = 1;
}

message GetIllegal
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03351"></a>
## FND-03351: chesscom.explanation_engine.v1.IllegalMoveExplanationMode.ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED = 0;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 653.

```text
_IN_CHECK = 8;
  ILLEGAL_MOVE_CASE_CASTLE_THROUGH_CHECK = 9;
}

enum IllegalMoveExplanationMode {
  ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED = 0;
  ILLEGAL_MOVE_EXPLANATION_MODE_ALL = 1;
  ILLEGAL_MOVE_EXPLANATION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MOVES = 2;
}

message GetIllegalMoveExplanationRequest {
  optional .chesscom.chess.v1.Move attempted_move = 1;
}

message GetIllegalMoveExplanationResponse {
  oneof _i
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03352"></a>
## FND-03352: chesscom.explanation_engine.v1.IllegalMoveExplanationMode.ILLEGAL_MOVE_EXPLANATION_MODE_ALL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ILLEGAL_MOVE_EXPLANATION_MODE_ALL = 1;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 702.

```text
_CHECK = 9;
}

enum IllegalMoveExplanationMode {
  ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED = 0;
  ILLEGAL_MOVE_EXPLANATION_MODE_ALL = 1;
  ILLEGAL_MOVE_EXPLANATION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MOVES = 2;
}

message GetIllegalMoveExplanationRequest {
  optional .chesscom.chess.v1.Move attempted_move = 1;
}

message GetIllegalMoveExplanationResponse {
  oneof _illegal_move_case {
  .chesscom.explanation_engine
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03353"></a>
## FND-03353: chesscom.explanation_engine.v1.IllegalMoveExplanationMode.ILLEGAL_MOVE_EXPLANATION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MOVES = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ILLEGAL_MOVE_EXPLANATION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MOVES = 2;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 743.

```text
nMode {
  ILLEGAL_MOVE_EXPLANATION_MODE_UNSPECIFIED = 0;
  ILLEGAL_MOVE_EXPLANATION_MODE_ALL = 1;
  ILLEGAL_MOVE_EXPLANATION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MOVES = 2;
}

message GetIllegalMoveExplanationRequest {
  optional .chesscom.chess.v1.Move attempted_move = 1;
}

message GetIllegalMoveExplanationResponse {
  oneof _illegal_move_case {
  .chesscom.explanation_engine.v1.IllegalMoveCase illegal_move_case = 1
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03354"></a>
## FND-03354: message declaration: chesscom.explanation_engine.v1.GetIllegalMoveExplanationRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetIllegalMoveExplanationRequest {

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 818.

```text
LANATION_MODE_ALL = 1;
  ILLEGAL_MOVE_EXPLANATION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MOVES = 2;
}

message GetIllegalMoveExplanationRequest {
  optional .chesscom.chess.v1.Move attempted_move = 1;
}

message GetIllegalMoveExplanationResponse {
  oneof _illegal_move_case {
  .chesscom.explanation_engine.v1.IllegalMoveCase illegal_move_case = 1;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 2;
  optio
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03355"></a>
## FND-03355: chesscom.explanation_engine.v1.GetIllegalMoveExplanationRequest.attempted_move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move attempted_move = 1;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 863.

```text
TION_MODE_SUPPRESS_PIECE_HAS_OTHER_LEGAL_MOVES = 2;
}

message GetIllegalMoveExplanationRequest {
  optional .chesscom.chess.v1.Move attempted_move = 1;
}

message GetIllegalMoveExplanationResponse {
  oneof _illegal_move_case {
  .chesscom.explanation_engine.v1.IllegalMoveCase illegal_move_case = 1;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 2;
  optional .chesscom.chess.v1.BoardMarkings board_ma
```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03356"></a>
## FND-03356: message declaration: chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetIllegalMoveExplanationResponse {

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 919.

```text
essage GetIllegalMoveExplanationRequest {
  optional .chesscom.chess.v1.Move attempted_move = 1;
}

message GetIllegalMoveExplanationResponse {
  oneof _illegal_move_case {
  .chesscom.explanation_engine.v1.IllegalMoveCase illegal_move_case = 1;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 2;
  optional .chesscom.chess.v1.BoardMarkings board_markings = 3;
}

```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03357"></a>
## FND-03357: oneof declaration: chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse._illegal_move_case

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _illegal_move_case {

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 965.

```text
tional .chesscom.chess.v1.Move attempted_move = 1;
}

message GetIllegalMoveExplanationResponse {
  oneof _illegal_move_case {
  .chesscom.explanation_engine.v1.IllegalMoveCase illegal_move_case = 1;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 2;
  optional .chesscom.chess.v1.BoardMarkings board_markings = 3;
}

```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03358"></a>
## FND-03358: chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse.illegal_move_case = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.IllegalMoveCase illegal_move_case = 1;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 994.

```text
e attempted_move = 1;
}

message GetIllegalMoveExplanationResponse {
  oneof _illegal_move_case {
  .chesscom.explanation_engine.v1.IllegalMoveCase illegal_move_case = 1;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 2;
  optional .chesscom.chess.v1.BoardMarkings board_markings = 3;
}

```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03359"></a>
## FND-03359: chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse.speech = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Speech speech = 2;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 1071.

```text
_illegal_move_case {
  .chesscom.explanation_engine.v1.IllegalMoveCase illegal_move_case = 1;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 2;
  optional .chesscom.chess.v1.BoardMarkings board_markings = 3;
}

```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03360"></a>
## FND-03360: chesscom.explanation_engine.v1.GetIllegalMoveExplanationResponse.board_markings = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.BoardMarkings board_markings = 3;

### Evidence

- **SRC-0374** `research/proto/chesscom/explanation_engine/v1/feature_get_illegal_move_explanation.proto` — [preserved redacted evidence](../evidence/text/76fc54267f871aa8e81b6981b5ea399f231f3989f1ca7f34480056bb87bffccb.proto)
  Character offset 1133.

```text
MoveCase illegal_move_case = 1;
  }
  optional .chesscom.explanation_engine.v1.Speech speech = 2;
  optional .chesscom.chess.v1.BoardMarkings board_markings = 3;
}

```

**Source references:** SRC-0374, SRC-1345  
**URL references:** None independently associated  
**Related findings:** FND-03339, FND-03340, FND-03341

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03361"></a>
## FND-03361: message declaration: chesscom.explanation_engine.v1.GetMoveDetailsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetMoveDetailsRequest {

### Evidence

- **SRC-0375** `research/proto/chesscom/explanation_engine/v1/feature_get_move_details.proto` — [preserved redacted evidence](../evidence/text/0967671b5e17dc858e4ba5df0bba4dd890426dbde153ac92548d890605f492e5.proto)
  Character offset 133.

```text
ngine/v1/feature_get_move_details.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetMoveDetailsRequest {
  oneof _move_notation {
  .chesscom.chess.v1.MoveNotation move_notation = 1;
  }
}

message GetMoveDetailsResponse {
  optional .chesscom.explanation_engine.v1.MoveDetails move = 1;
}

```

**Source references:** SRC-0375, SRC-1346  
**URL references:** None independently associated  
**Related findings:** FND-03362, FND-03363

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03362"></a>
## FND-03362: oneof declaration: chesscom.explanation_engine.v1.GetMoveDetailsRequest._move_notation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _move_notation {

### Evidence

- **SRC-0375** `research/proto/chesscom/explanation_engine/v1/feature_get_move_details.proto` — [preserved redacted evidence](../evidence/text/0967671b5e17dc858e4ba5df0bba4dd890426dbde153ac92548d890605f492e5.proto)
  Character offset 167.

```text
proto
// syntax: proto3

package chesscom.explanation_engine.v1;

message GetMoveDetailsRequest {
  oneof _move_notation {
  .chesscom.chess.v1.MoveNotation move_notation = 1;
  }
}

message GetMoveDetailsResponse {
  optional .chesscom.explanation_engine.v1.MoveDetails move = 1;
}

```

**Source references:** SRC-0375, SRC-1346  
**URL references:** None independently associated  
**Related findings:** FND-03361, FND-03363

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03363"></a>
## FND-03363: chesscom.explanation_engine.v1.GetMoveDetailsRequest.move_notation = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.MoveNotation move_notation = 1;

### Evidence

- **SRC-0375** `research/proto/chesscom/explanation_engine/v1/feature_get_move_details.proto` — [preserved redacted evidence](../evidence/text/0967671b5e17dc858e4ba5df0bba4dd890426dbde153ac92548d890605f492e5.proto)
  Character offset 192.

```text
package chesscom.explanation_engine.v1;

message GetMoveDetailsRequest {
  oneof _move_notation {
  .chesscom.chess.v1.MoveNotation move_notation = 1;
  }
}

message GetMoveDetailsResponse {
  optional .chesscom.explanation_engine.v1.MoveDetails move = 1;
}

```

**Source references:** SRC-0375, SRC-1346  
**URL references:** None independently associated  
**Related findings:** FND-03361, FND-03362

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03364"></a>
## FND-03364: message declaration: chesscom.explanation_engine.v1.GetMoveDetailsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetMoveDetailsResponse {

### Evidence

- **SRC-0375** `research/proto/chesscom/explanation_engine/v1/feature_get_move_details.proto` — [preserved redacted evidence](../evidence/text/0967671b5e17dc858e4ba5df0bba4dd890426dbde153ac92548d890605f492e5.proto)
  Character offset 250.

```text
tailsRequest {
  oneof _move_notation {
  .chesscom.chess.v1.MoveNotation move_notation = 1;
  }
}

message GetMoveDetailsResponse {
  optional .chesscom.explanation_engine.v1.MoveDetails move = 1;
}

```

**Source references:** SRC-0375, SRC-1346  
**URL references:** None independently associated  
**Related findings:** FND-03361, FND-03362, FND-03363

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03365"></a>
## FND-03365: chesscom.explanation_engine.v1.GetMoveDetailsResponse.move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveDetails move = 1;

### Evidence

- **SRC-0375** `research/proto/chesscom/explanation_engine/v1/feature_get_move_details.proto` — [preserved redacted evidence](../evidence/text/0967671b5e17dc858e4ba5df0bba4dd890426dbde153ac92548d890605f492e5.proto)
  Character offset 285.

```text
on {
  .chesscom.chess.v1.MoveNotation move_notation = 1;
  }
}

message GetMoveDetailsResponse {
  optional .chesscom.explanation_engine.v1.MoveDetails move = 1;
}

```

**Source references:** SRC-0375, SRC-1346  
**URL references:** None independently associated  
**Related findings:** FND-03361, FND-03362, FND-03363

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03366"></a>
## FND-03366: enum declaration: chesscom.explanation_engine.v1.NonChessTextType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum NonChessTextType {

### Evidence

- **SRC-0376** `research/proto/chesscom/explanation_engine/v1/feature_get_non_chess_text.proto` — [preserved redacted evidence](../evidence/text/3ad4537c412cfce227f138beb38b45dd56ac328a0e4ded762d94a730deb42c8b.proto)
  Character offset 135.

```text
ine/v1/feature_get_non_chess_text.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum NonChessTextType {
  NON_CHESS_TEXT_TYPE_UNSPECIFIED = 0;
  NON_CHESS_TEXT_TYPE_UNDO_MOVE_LEGAL = 1;
  NON_CHESS_TEXT_TYPE_UNDO_MOVE_ILLEGAL = 2;
  NON_CHESS_TEXT_TYPE_RESUME_GAME = 3;
  NON_CHESS_TEXT_TYPE_SWITCHED_COACH = 4;
}

message GetNonChessTextRequest {
  optional .chesscom.explanation_engine.v1.NonChessT
```

**Source references:** SRC-0376, SRC-1347  
**URL references:** None independently associated  
**Related findings:** FND-03367, FND-03368

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03367"></a>
## FND-03367: chesscom.explanation_engine.v1.NonChessTextType.NON_CHESS_TEXT_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NON_CHESS_TEXT_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0376** `research/proto/chesscom/explanation_engine/v1/feature_get_non_chess_text.proto` — [preserved redacted evidence](../evidence/text/3ad4537c412cfce227f138beb38b45dd56ac328a0e4ded762d94a730deb42c8b.proto)
  Character offset 161.

```text
ss_text.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum NonChessTextType {
  NON_CHESS_TEXT_TYPE_UNSPECIFIED = 0;
  NON_CHESS_TEXT_TYPE_UNDO_MOVE_LEGAL = 1;
  NON_CHESS_TEXT_TYPE_UNDO_MOVE_ILLEGAL = 2;
  NON_CHESS_TEXT_TYPE_RESUME_GAME = 3;
  NON_CHESS_TEXT_TYPE_SWITCHED_COACH = 4;
}

message GetNonChessTextRequest {
  optional .chesscom.explanation_engine.v1.NonChessTextType type = 1;
}

messa
```

**Source references:** SRC-0376, SRC-1347  
**URL references:** None independently associated  
**Related findings:** FND-03366, FND-03368

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03368"></a>
## FND-03368: chesscom.explanation_engine.v1.NonChessTextType.NON_CHESS_TEXT_TYPE_UNDO_MOVE_LEGAL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NON_CHESS_TEXT_TYPE_UNDO_MOVE_LEGAL = 1;

### Evidence

- **SRC-0376** `research/proto/chesscom/explanation_engine/v1/feature_get_non_chess_text.proto` — [preserved redacted evidence](../evidence/text/3ad4537c412cfce227f138beb38b45dd56ac328a0e4ded762d94a730deb42c8b.proto)
  Character offset 200.

```text
e chesscom.explanation_engine.v1;

enum NonChessTextType {
  NON_CHESS_TEXT_TYPE_UNSPECIFIED = 0;
  NON_CHESS_TEXT_TYPE_UNDO_MOVE_LEGAL = 1;
  NON_CHESS_TEXT_TYPE_UNDO_MOVE_ILLEGAL = 2;
  NON_CHESS_TEXT_TYPE_RESUME_GAME = 3;
  NON_CHESS_TEXT_TYPE_SWITCHED_COACH = 4;
}

message GetNonChessTextRequest {
  optional .chesscom.explanation_engine.v1.NonChessTextType type = 1;
}

message GetNonChessTextResponse {
  optional
```

**Source references:** SRC-0376, SRC-1347  
**URL references:** None independently associated  
**Related findings:** FND-03366, FND-03367

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03369"></a>
## FND-03369: chesscom.explanation_engine.v1.NonChessTextType.NON_CHESS_TEXT_TYPE_UNDO_MOVE_ILLEGAL = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NON_CHESS_TEXT_TYPE_UNDO_MOVE_ILLEGAL = 2;

### Evidence

- **SRC-0376** `research/proto/chesscom/explanation_engine/v1/feature_get_non_chess_text.proto` — [preserved redacted evidence](../evidence/text/3ad4537c412cfce227f138beb38b45dd56ac328a0e4ded762d94a730deb42c8b.proto)
  Character offset 243.

```text
ChessTextType {
  NON_CHESS_TEXT_TYPE_UNSPECIFIED = 0;
  NON_CHESS_TEXT_TYPE_UNDO_MOVE_LEGAL = 1;
  NON_CHESS_TEXT_TYPE_UNDO_MOVE_ILLEGAL = 2;
  NON_CHESS_TEXT_TYPE_RESUME_GAME = 3;
  NON_CHESS_TEXT_TYPE_SWITCHED_COACH = 4;
}

message GetNonChessTextRequest {
  optional .chesscom.explanation_engine.v1.NonChessTextType type = 1;
}

message GetNonChessTextResponse {
  optional .chesscom.explanation_engine.v1.Speech spe
```

**Source references:** SRC-0376, SRC-1347  
**URL references:** None independently associated  
**Related findings:** FND-03366, FND-03367, FND-03368

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03370"></a>
## FND-03370: chesscom.explanation_engine.v1.NonChessTextType.NON_CHESS_TEXT_TYPE_RESUME_GAME = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NON_CHESS_TEXT_TYPE_RESUME_GAME = 3;

### Evidence

- **SRC-0376** `research/proto/chesscom/explanation_engine/v1/feature_get_non_chess_text.proto` — [preserved redacted evidence](../evidence/text/3ad4537c412cfce227f138beb38b45dd56ac328a0e4ded762d94a730deb42c8b.proto)
  Character offset 288.

```text
FIED = 0;
  NON_CHESS_TEXT_TYPE_UNDO_MOVE_LEGAL = 1;
  NON_CHESS_TEXT_TYPE_UNDO_MOVE_ILLEGAL = 2;
  NON_CHESS_TEXT_TYPE_RESUME_GAME = 3;
  NON_CHESS_TEXT_TYPE_SWITCHED_COACH = 4;
}

message GetNonChessTextRequest {
  optional .chesscom.explanation_engine.v1.NonChessTextType type = 1;
}

message GetNonChessTextResponse {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

```

**Source references:** SRC-0376, SRC-1347  
**URL references:** None independently associated  
**Related findings:** FND-03366, FND-03367, FND-03368

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03371"></a>
## FND-03371: chesscom.explanation_engine.v1.NonChessTextType.NON_CHESS_TEXT_TYPE_SWITCHED_COACH = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

NON_CHESS_TEXT_TYPE_SWITCHED_COACH = 4;

### Evidence

- **SRC-0376** `research/proto/chesscom/explanation_engine/v1/feature_get_non_chess_text.proto` — [preserved redacted evidence](../evidence/text/3ad4537c412cfce227f138beb38b45dd56ac328a0e4ded762d94a730deb42c8b.proto)
  Character offset 327.

```text
VE_LEGAL = 1;
  NON_CHESS_TEXT_TYPE_UNDO_MOVE_ILLEGAL = 2;
  NON_CHESS_TEXT_TYPE_RESUME_GAME = 3;
  NON_CHESS_TEXT_TYPE_SWITCHED_COACH = 4;
}

message GetNonChessTextRequest {
  optional .chesscom.explanation_engine.v1.NonChessTextType type = 1;
}

message GetNonChessTextResponse {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

```

**Source references:** SRC-0376, SRC-1347  
**URL references:** None independently associated  
**Related findings:** FND-03366, FND-03367, FND-03368

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03372"></a>
## FND-03372: message declaration: chesscom.explanation_engine.v1.GetNonChessTextRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetNonChessTextRequest {

### Evidence

- **SRC-0376** `research/proto/chesscom/explanation_engine/v1/feature_get_non_chess_text.proto` — [preserved redacted evidence](../evidence/text/3ad4537c412cfce227f138beb38b45dd56ac328a0e4ded762d94a730deb42c8b.proto)
  Character offset 370.

```text
VE_ILLEGAL = 2;
  NON_CHESS_TEXT_TYPE_RESUME_GAME = 3;
  NON_CHESS_TEXT_TYPE_SWITCHED_COACH = 4;
}

message GetNonChessTextRequest {
  optional .chesscom.explanation_engine.v1.NonChessTextType type = 1;
}

message GetNonChessTextResponse {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

```

**Source references:** SRC-0376, SRC-1347  
**URL references:** None independently associated  
**Related findings:** FND-03366, FND-03367, FND-03368

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-03373"></a>
## FND-03373: chesscom.explanation_engine.v1.GetNonChessTextRequest.type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.NonChessTextType type = 1;

### Evidence

- **SRC-0376** `research/proto/chesscom/explanation_engine/v1/feature_get_non_chess_text.proto` — [preserved redacted evidence](../evidence/text/3ad4537c412cfce227f138beb38b45dd56ac328a0e4ded762d94a730deb42c8b.proto)
  Character offset 405.

```text
PE_RESUME_GAME = 3;
  NON_CHESS_TEXT_TYPE_SWITCHED_COACH = 4;
}

message GetNonChessTextRequest {
  optional .chesscom.explanation_engine.v1.NonChessTextType type = 1;
}

message GetNonChessTextResponse {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

```

**Source references:** SRC-0376, SRC-1347  
**URL references:** None independently associated  
**Related findings:** FND-03366, FND-03367, FND-03368

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-03374"></a>
## FND-03374: message declaration: chesscom.explanation_engine.v1.GetNonChessTextResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetNonChessTextResponse {

### Evidence

- **SRC-0376** `research/proto/chesscom/explanation_engine/v1/feature_get_non_chess_text.proto` — [preserved redacted evidence](../evidence/text/3ad4537c412cfce227f138beb38b45dd56ac328a0e4ded762d94a730deb42c8b.proto)
  Character offset 476.

```text
e GetNonChessTextRequest {
  optional .chesscom.explanation_engine.v1.NonChessTextType type = 1;
}

message GetNonChessTextResponse {
  optional .chesscom.explanation_engine.v1.Speech speech = 1;
}

```

**Source references:** SRC-0376, SRC-1347  
**URL references:** None independently associated  
**Related findings:** FND-03366, FND-03367, FND-03368

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
