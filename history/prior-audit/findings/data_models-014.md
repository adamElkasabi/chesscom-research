# data_models — findings 1301–1400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-01575"></a>
## FND-01575: chesscom.coaches.v2.CoachContextExtension.coach_locale = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coach_locale = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4871.

```text
 wrong_attempts = 3;
}

message CoachContextExtension {
  optional string coach_analytics_id = 1;
  optional string coach_locale = 2;
}

message PlayCoachRetryMissContextExtension {
  oneof _found_correct_move {
  bool found_correct_move = 2;
  }
  oneof _wrong_attempts {
  int32 wrong_attempts = 3;
  }
  optional string boardevent = 1;
}

message CoachAnimationShown {
  optional string animation_type = 1;
  optional
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01576"></a>
## FND-01576: message declaration: chesscom.coaches.v2.PlayCoachRetryMissContextExtension

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PlayCoachRetryMissContextExtension {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4908.

```text
ContextExtension {
  optional string coach_analytics_id = 1;
  optional string coach_locale = 2;
}

message PlayCoachRetryMissContextExtension {
  oneof _found_correct_move {
  bool found_correct_move = 2;
  }
  oneof _wrong_attempts {
  int32 wrong_attempts = 3;
  }
  optional string boardevent = 1;
}

message CoachAnimationShown {
  optional string animation_type = 1;
  optional string interface = 2;
}

message Gui
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01577"></a>
## FND-01577: oneof declaration: chesscom.coaches.v2.PlayCoachRetryMissContextExtension._found_correct_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _found_correct_move {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4955.

```text
ytics_id = 1;
  optional string coach_locale = 2;
}

message PlayCoachRetryMissContextExtension {
  oneof _found_correct_move {
  bool found_correct_move = 2;
  }
  oneof _wrong_attempts {
  int32 wrong_attempts = 3;
  }
  optional string boardevent = 1;
}

message CoachAnimationShown {
  optional string animation_type = 1;
  optional string interface = 2;
}

message GuidedCoachGameStarted {
  optional string script_
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01578"></a>
## FND-01578: chesscom.coaches.v2.PlayCoachRetryMissContextExtension.found_correct_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool found_correct_move = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4726.

```text
oice = 2;
}

message CoachFlipBoardExerciseCompleted {
  optional string boardevent = 1;
  optional bool found_correct_move = 2;
  optional int32 wrong_attempts = 3;
}

message CoachContextExtension {
  optional string coach_analytics_id = 1;
  optional string coach_locale = 2;
}

message PlayCoachRetryMissContextExtension {
  oneof _found_correct_move {
  bool found_correct_move = 2;
  }
  oneof _wrong_attempts {
  
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01579"></a>
## FND-01579: oneof declaration: chesscom.coaches.v2.PlayCoachRetryMissContextExtension._wrong_attempts

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _wrong_attempts {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 5020.

```text
CoachRetryMissContextExtension {
  oneof _found_correct_move {
  bool found_correct_move = 2;
  }
  oneof _wrong_attempts {
  int32 wrong_attempts = 3;
  }
  optional string boardevent = 1;
}

message CoachAnimationShown {
  optional string animation_type = 1;
  optional string interface = 2;
}

message GuidedCoachGameStarted {
  optional string script_id = 1;
  optional .chesscom.coaches.v2.GuidedCoachGameSource sou
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01580"></a>
## FND-01580: chesscom.coaches.v2.PlayCoachRetryMissContextExtension.wrong_attempts = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 wrong_attempts = 3;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4766.

```text
iseCompleted {
  optional string boardevent = 1;
  optional bool found_correct_move = 2;
  optional int32 wrong_attempts = 3;
}

message CoachContextExtension {
  optional string coach_analytics_id = 1;
  optional string coach_locale = 2;
}

message PlayCoachRetryMissContextExtension {
  oneof _found_correct_move {
  bool found_correct_move = 2;
  }
  oneof _wrong_attempts {
  int32 wrong_attempts = 3;
  }
  optional
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01581"></a>
## FND-01581: chesscom.coaches.v2.PlayCoachRetryMissContextExtension.boardevent = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string boardevent = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 4148.

```text
CoachSignUpModalCTATapped {
}

message CoachSettingsOpened {
}

message CoachCouldWarnOfMistake {
  optional string boardevent = 1;
  optional int32 cooldown_counter = 2;
}

message CoachWarnedOfMistake {
  optional string boardevent = 1;
}

message CoachMistakeWarningAnswered {
  optional string boardevent = 1;
  optional .chesscom.coaches.v2.CoachMistakeWarningChoice choice = 2;
}

message CoachFlipBoardOffered {
 
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01582"></a>
## FND-01582: message declaration: chesscom.coaches.v2.CoachAnimationShown

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachAnimationShown {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 5113.

```text

  }
  oneof _wrong_attempts {
  int32 wrong_attempts = 3;
  }
  optional string boardevent = 1;
}

message CoachAnimationShown {
  optional string animation_type = 1;
  optional string interface = 2;
}

message GuidedCoachGameStarted {
  optional string script_id = 1;
  optional .chesscom.coaches.v2.GuidedCoachGameSource source = 2;
}

message GuidedCoachGameResigned {
  optional string script_id = 1;
  optional int
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01583"></a>
## FND-01583: chesscom.coaches.v2.CoachAnimationShown.animation_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string animation_type = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 5145.

```text
 int32 wrong_attempts = 3;
  }
  optional string boardevent = 1;
}

message CoachAnimationShown {
  optional string animation_type = 1;
  optional string interface = 2;
}

message GuidedCoachGameStarted {
  optional string script_id = 1;
  optional .chesscom.coaches.v2.GuidedCoachGameSource source = 2;
}

message GuidedCoachGameResigned {
  optional string script_id = 1;
  optional int32 ply_index = 2;
}

message Gui
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01584"></a>
## FND-01584: chesscom.coaches.v2.CoachAnimationShown.interface = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string interface = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 5183.

```text
nal string boardevent = 1;
}

message CoachAnimationShown {
  optional string animation_type = 1;
  optional string interface = 2;
}

message GuidedCoachGameStarted {
  optional string script_id = 1;
  optional .chesscom.coaches.v2.GuidedCoachGameSource source = 2;
}

message GuidedCoachGameResigned {
  optional string script_id = 1;
  optional int32 ply_index = 2;
}

message GuidedCoachGameCompleted {
  optional str
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01585"></a>
## FND-01585: message declaration: chesscom.coaches.v2.GuidedCoachGameStarted

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GuidedCoachGameStarted {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 5217.

```text
age CoachAnimationShown {
  optional string animation_type = 1;
  optional string interface = 2;
}

message GuidedCoachGameStarted {
  optional string script_id = 1;
  optional .chesscom.coaches.v2.GuidedCoachGameSource source = 2;
}

message GuidedCoachGameResigned {
  optional string script_id = 1;
  optional int32 ply_index = 2;
}

message GuidedCoachGameCompleted {
  optional string script_id = 1;
}

```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01586"></a>
## FND-01586: chesscom.coaches.v2.GuidedCoachGameStarted.script_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string script_id = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 5252.

```text
l string animation_type = 1;
  optional string interface = 2;
}

message GuidedCoachGameStarted {
  optional string script_id = 1;
  optional .chesscom.coaches.v2.GuidedCoachGameSource source = 2;
}

message GuidedCoachGameResigned {
  optional string script_id = 1;
  optional int32 ply_index = 2;
}

message GuidedCoachGameCompleted {
  optional string script_id = 1;
}

```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01587"></a>
## FND-01587: chesscom.coaches.v2.GuidedCoachGameStarted.source = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.GuidedCoachGameSource source = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 5285.

```text
tional string interface = 2;
}

message GuidedCoachGameStarted {
  optional string script_id = 1;
  optional .chesscom.coaches.v2.GuidedCoachGameSource source = 2;
}

message GuidedCoachGameResigned {
  optional string script_id = 1;
  optional int32 ply_index = 2;
}

message GuidedCoachGameCompleted {
  optional string script_id = 1;
}

```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01588"></a>
## FND-01588: message declaration: chesscom.coaches.v2.GuidedCoachGameResigned

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GuidedCoachGameResigned {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 5352.

```text
optional string script_id = 1;
  optional .chesscom.coaches.v2.GuidedCoachGameSource source = 2;
}

message GuidedCoachGameResigned {
  optional string script_id = 1;
  optional int32 ply_index = 2;
}

message GuidedCoachGameCompleted {
  optional string script_id = 1;
}

```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01589"></a>
## FND-01589: chesscom.coaches.v2.GuidedCoachGameResigned.script_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string script_id = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 5252.

```text
l string animation_type = 1;
  optional string interface = 2;
}

message GuidedCoachGameStarted {
  optional string script_id = 1;
  optional .chesscom.coaches.v2.GuidedCoachGameSource source = 2;
}

message GuidedCoachGameResigned {
  optional string script_id = 1;
  optional int32 ply_index = 2;
}

message GuidedCoachGameCompleted {
  optional string script_id = 1;
}

```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01590"></a>
## FND-01590: chesscom.coaches.v2.GuidedCoachGameResigned.ply_index = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 ply_index = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 5421.

```text
CoachGameSource source = 2;
}

message GuidedCoachGameResigned {
  optional string script_id = 1;
  optional int32 ply_index = 2;
}

message GuidedCoachGameCompleted {
  optional string script_id = 1;
}

```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01591"></a>
## FND-01591: message declaration: chesscom.coaches.v2.GuidedCoachGameCompleted

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GuidedCoachGameCompleted {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 5454.

```text
ssage GuidedCoachGameResigned {
  optional string script_id = 1;
  optional int32 ply_index = 2;
}

message GuidedCoachGameCompleted {
  optional string script_id = 1;
}

```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01592"></a>
## FND-01592: chesscom.coaches.v2.GuidedCoachGameCompleted.script_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string script_id = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 5252.

```text
l string animation_type = 1;
  optional string interface = 2;
}

message GuidedCoachGameStarted {
  optional string script_id = 1;
  optional .chesscom.coaches.v2.GuidedCoachGameSource source = 2;
}

message GuidedCoachGameResigned {
  optional string script_id = 1;
  optional int32 ply_index = 2;
}

message GuidedCoachGameCompleted {
  optional string script_id = 1;
}

```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01593"></a>
## FND-01593: enum declaration: chesscom.computer.v1.UserColor

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum UserColor {

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 102.

```text
 source: chesscom/computer/v1/computer_game.proto
// syntax: proto3

package chesscom.computer.v1;

enum UserColor {
  USER_COLOR_UNSPECIFIED = 0;
  USER_COLOR_WHITE = 1;
  USER_COLOR_BLACK = 2;
}

enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  A
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01594"></a>
## FND-01594: chesscom.computer.v1.UserColor.USER_COLOR_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_COLOR_UNSPECIFIED = 0;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 121.

```text
omputer/v1/computer_game.proto
// syntax: proto3

package chesscom.computer.v1;

enum UserColor {
  USER_COLOR_UNSPECIFIED = 0;
  USER_COLOR_WHITE = 1;
  USER_COLOR_BLACK = 2;
}

enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATUR
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01595"></a>
## FND-01595: chesscom.computer.v1.UserColor.USER_COLOR_WHITE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_COLOR_WHITE = 1;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 151.

```text

// syntax: proto3

package chesscom.computer.v1;

enum UserColor {
  USER_COLOR_UNSPECIFIED = 0;
  USER_COLOR_WHITE = 1;
  USER_COLOR_BLACK = 2;
}

enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FE
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01596"></a>
## FND-01596: chesscom.computer.v1.UserColor.USER_COLOR_BLACK = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_COLOR_BLACK = 2;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 175.

```text
age chesscom.computer.v1;

enum UserColor {
  USER_COLOR_UNSPECIFIED = 0;
  USER_COLOR_WHITE = 1;
  USER_COLOR_BLACK = 2;
}

enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  AS
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01597"></a>
## FND-01597: enum declaration: chesscom.computer.v1.GameMode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameMode {

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 200.

```text


enum UserColor {
  USER_COLOR_UNSPECIFIED = 0;
  USER_COLOR_WHITE = 1;
  USER_COLOR_BLACK = 2;
}

enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01598"></a>
## FND-01598: chesscom.computer.v1.GameMode.GAME_MODE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_MODE_UNSPECIFIED = 0;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 218.

```text

  USER_COLOR_UNSPECIFIED = 0;
  USER_COLOR_WHITE = 1;
  USER_COLOR_BLACK = 2;
}

enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_G
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01599"></a>
## FND-01599: chesscom.computer.v1.GameMode.GAME_MODE_CHALLENGE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_MODE_CHALLENGE = 1;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 247.

```text
;
  USER_COLOR_WHITE = 1;
  USER_COLOR_BLACK = 2;
}

enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  AS
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01600"></a>
## FND-01600: chesscom.computer.v1.GameMode.GAME_MODE_FRIENDLY = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_MODE_FRIENDLY = 2;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 274.

```text
 USER_COLOR_BLACK = 2;
}

enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUAT
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01601"></a>
## FND-01601: chesscom.computer.v1.GameMode.GAME_MODE_ASSISTED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_MODE_ASSISTED = 3;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 300.

```text
enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_F
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01602"></a>
## FND-01602: chesscom.computer.v1.GameMode.GAME_MODE_CUSTOM = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_MODE_CUSTOM = 4;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 326.

```text
E_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSIS
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01603"></a>
## FND-01603: enum declaration: chesscom.computer.v1.AssistedGameFeature

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum AssistedGameFeature {

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 351.

```text
_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTI
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01604"></a>
## FND-01604: chesscom.computer.v1.AssistedGameFeature.ASSISTED_GAME_FEATURE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 380.

```text
ODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEAT
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01605"></a>
## FND-01605: chesscom.computer.v1.AssistedGameFeature.ASSISTED_GAME_FEATURE_CHAT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_CHAT = 1;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 421.

```text
3;
  GAME_MODE_CUSTOM = 4;
}

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

message AssistedGam
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01606"></a>
## FND-01606: chesscom.computer.v1.AssistedGameFeature.ASSISTED_GAME_FEATURE_ANALYSIS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_ANALYSIS = 2;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 455.

```text
 AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

message AssistedGameFeatures {
  optional bool chat =
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01607"></a>
## FND-01607: chesscom.computer.v1.AssistedGameFeature.ASSISTED_GAME_FEATURE_HINTS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_HINTS = 3;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 493.

```text
_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

message AssistedGameFeatures {
  optional bool chat = 1;
  optional bool analysis = 2;
  op
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01608"></a>
## FND-01608: chesscom.computer.v1.AssistedGameFeature.ASSISTED_GAME_FEATURE_THREATS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_THREATS = 4;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 528.

```text
D_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

message AssistedGameFeatures {
  optional bool chat = 1;
  optional bool analysis = 2;
  optional bool hints = 3;
  optional b
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01609"></a>
## FND-01609: chesscom.computer.v1.AssistedGameFeature.ASSISTED_GAME_FEATURE_EVALUATION = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_EVALUATION = 5;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 565.

```text
AME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

message AssistedGameFeatures {
  optional bool chat = 1;
  optional bool analysis = 2;
  optional bool hints = 3;
  optional bool threats = 4;
}

message CustomMod
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01610"></a>
## FND-01610: chesscom.computer.v1.AssistedGameFeature.ASSISTED_GAME_FEATURE_ENGINE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_ENGINE = 6;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 605.

```text
E_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

message AssistedGameFeatures {
  optional bool chat = 1;
  optional bool analysis = 2;
  optional bool hints = 3;
  optional bool threats = 4;
}

message CustomModeConfiguration {
  optional .chesscom.ga
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01611"></a>
## FND-01611: chesscom.computer.v1.AssistedGameFeature.ASSISTED_GAME_FEATURE_SUGGESTIONS = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 641.

```text
_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

message AssistedGameFeatures {
  optional bool chat = 1;
  optional bool analysis = 2;
  optional bool hints = 3;
  optional bool threats = 4;
}

message CustomModeConfiguration {
  optional .chesscom.game_storage.v1.Variant game_type = 1;
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01612"></a>
## FND-01612: chesscom.computer.v1.AssistedGameFeature.ASSISTED_GAME_FEATURE_TAKEBACKS = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_TAKEBACKS = 8;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 682.

```text
TURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

message AssistedGameFeatures {
  optional bool chat = 1;
  optional bool analysis = 2;
  optional bool hints = 3;
  optional bool threats = 4;
}

message CustomModeConfiguration {
  optional .chesscom.game_storage.v1.Variant game_type = 1;
  optional int32 base_time_ms = 2;
  opt
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01613"></a>
## FND-01613: message declaration: chesscom.computer.v1.AssistedGameFeatures

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AssistedGameFeatures {

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 722.

```text
TURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

message AssistedGameFeatures {
  optional bool chat = 1;
  optional bool analysis = 2;
  optional bool hints = 3;
  optional bool threats = 4;
}

message CustomModeConfiguration {
  optional .chesscom.game_storage.v1.Variant game_type = 1;
  optional int32 base_time_ms = 2;
  optional int32 time_increment_ms = 3;
  rep
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01614"></a>
## FND-01614: chesscom.computer.v1.AssistedGameFeatures.chat = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool chat = 1;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 755.

```text
FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

message AssistedGameFeatures {
  optional bool chat = 1;
  optional bool analysis = 2;
  optional bool hints = 3;
  optional bool threats = 4;
}

message CustomModeConfiguration {
  optional .chesscom.game_storage.v1.Variant game_type = 1;
  optional int32 base_time_ms = 2;
  optional int32 time_increment_ms = 3;
  repeated .chesscom.computer.v1.Assis
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01615"></a>
## FND-01615: chesscom.computer.v1.AssistedGameFeatures.analysis = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool analysis = 2;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 781.

```text
 ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

message AssistedGameFeatures {
  optional bool chat = 1;
  optional bool analysis = 2;
  optional bool hints = 3;
  optional bool threats = 4;
}

message CustomModeConfiguration {
  optional .chesscom.game_storage.v1.Variant game_type = 1;
  optional int32 base_time_ms = 2;
  optional int32 time_increment_ms = 3;
  repeated .chesscom.computer.v1.AssistedGameFeature assisted_ga
```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01616"></a>
## FND-01616: chesscom.computer.v1.AssistedGameFeatures.hints = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool hints = 3;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 811.

```text
KS = 8;
}

message AssistedGameFeatures {
  optional bool chat = 1;
  optional bool analysis = 2;
  optional bool hints = 3;
  optional bool threats = 4;
}

message CustomModeConfiguration {
  optional .chesscom.game_storage.v1.Variant game_type = 1;
  optional int32 base_time_ms = 2;
  optional int32 time_increment_ms = 3;
  repeated .chesscom.computer.v1.AssistedGameFeature assisted_game_features = 4;
}

```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01617"></a>
## FND-01617: chesscom.computer.v1.AssistedGameFeatures.threats = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool threats = 4;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 838.

```text
GameFeatures {
  optional bool chat = 1;
  optional bool analysis = 2;
  optional bool hints = 3;
  optional bool threats = 4;
}

message CustomModeConfiguration {
  optional .chesscom.game_storage.v1.Variant game_type = 1;
  optional int32 base_time_ms = 2;
  optional int32 time_increment_ms = 3;
  repeated .chesscom.computer.v1.AssistedGameFeature assisted_game_features = 4;
}

```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01618"></a>
## FND-01618: message declaration: chesscom.computer.v1.CustomModeConfiguration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CustomModeConfiguration {

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 868.

```text
 chat = 1;
  optional bool analysis = 2;
  optional bool hints = 3;
  optional bool threats = 4;
}

message CustomModeConfiguration {
  optional .chesscom.game_storage.v1.Variant game_type = 1;
  optional int32 base_time_ms = 2;
  optional int32 time_increment_ms = 3;
  repeated .chesscom.computer.v1.AssistedGameFeature assisted_game_features = 4;
}

```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01619"></a>
## FND-01619: chesscom.computer.v1.CustomModeConfiguration.game_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v1.Variant game_type = 1;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 904.

```text
= 2;
  optional bool hints = 3;
  optional bool threats = 4;
}

message CustomModeConfiguration {
  optional .chesscom.game_storage.v1.Variant game_type = 1;
  optional int32 base_time_ms = 2;
  optional int32 time_increment_ms = 3;
  repeated .chesscom.computer.v1.AssistedGameFeature assisted_game_features = 4;
}

```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01620"></a>
## FND-01620: chesscom.computer.v1.CustomModeConfiguration.base_time_ms = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 base_time_ms = 2;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 964.

```text

}

message CustomModeConfiguration {
  optional .chesscom.game_storage.v1.Variant game_type = 1;
  optional int32 base_time_ms = 2;
  optional int32 time_increment_ms = 3;
  repeated .chesscom.computer.v1.AssistedGameFeature assisted_game_features = 4;
}

```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01621"></a>
## FND-01621: chesscom.computer.v1.CustomModeConfiguration.time_increment_ms = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 time_increment_ms = 3;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 999.

```text
 {
  optional .chesscom.game_storage.v1.Variant game_type = 1;
  optional int32 base_time_ms = 2;
  optional int32 time_increment_ms = 3;
  repeated .chesscom.computer.v1.AssistedGameFeature assisted_game_features = 4;
}

```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01622"></a>
## FND-01622: chesscom.computer.v1.CustomModeConfiguration.assisted_game_features = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.computer.v1.AssistedGameFeature assisted_game_features = 4;

### Evidence

- **SRC-0260** `research/proto/chesscom/computer/v1/computer_game.proto` — [preserved redacted evidence](../evidence/text/06af6d3462c3cdaeb1a42ab65f35aca4a3c36acc7a00aaaf04bc455e6f873447.proto)
  Character offset 1039.

```text
Variant game_type = 1;
  optional int32 base_time_ms = 2;
  optional int32 time_increment_ms = 3;
  repeated .chesscom.computer.v1.AssistedGameFeature assisted_game_features = 4;
}

```

**Source references:** SRC-0260, SRC-1231  
**URL references:** None independently associated  
**Related findings:** FND-01593, FND-01594, FND-01595

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01623"></a>
## FND-01623: enum declaration: chesscom.computer.v2.AssistedGameFeature

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum AssistedGameFeature {

### Evidence

- **SRC-0261** `research/proto/chesscom/computer/v2/assisted_game_feature.proto` — [preserved redacted evidence](../evidence/text/5d8aee74efe62ecb71c8c416264e8e7273dc4f05c08b8b8ebff39aab78847ae9.proto)
  Character offset 110.

```text
 chesscom/computer/v2/assisted_game_feature.proto
// syntax: proto3

package chesscom.computer.v2;

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTI
```

**Source references:** SRC-0261, SRC-1232  
**URL references:** None independently associated  
**Related findings:** FND-01624, FND-01625

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01624"></a>
## FND-01624: chesscom.computer.v2.AssistedGameFeature.ASSISTED_GAME_FEATURE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;

### Evidence

- **SRC-0261** `research/proto/chesscom/computer/v2/assisted_game_feature.proto` — [preserved redacted evidence](../evidence/text/5d8aee74efe62ecb71c8c416264e8e7273dc4f05c08b8b8ebff39aab78847ae9.proto)
  Character offset 139.

```text
d_game_feature.proto
// syntax: proto3

package chesscom.computer.v2;

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEAT
```

**Source references:** SRC-0261, SRC-1232  
**URL references:** None independently associated  
**Related findings:** FND-01623, FND-01625

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01625"></a>
## FND-01625: chesscom.computer.v2.AssistedGameFeature.ASSISTED_GAME_FEATURE_CHAT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_CHAT = 1;

### Evidence

- **SRC-0261** `research/proto/chesscom/computer/v2/assisted_game_feature.proto` — [preserved redacted evidence](../evidence/text/5d8aee74efe62ecb71c8c416264e8e7273dc4f05c08b8b8ebff39aab78847ae9.proto)
  Character offset 180.

```text
ackage chesscom.computer.v2;

enum AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

```

**Source references:** SRC-0261, SRC-1232  
**URL references:** None independently associated  
**Related findings:** FND-01623, FND-01624

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01626"></a>
## FND-01626: chesscom.computer.v2.AssistedGameFeature.ASSISTED_GAME_FEATURE_ANALYSIS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_ANALYSIS = 2;

### Evidence

- **SRC-0261** `research/proto/chesscom/computer/v2/assisted_game_feature.proto` — [preserved redacted evidence](../evidence/text/5d8aee74efe62ecb71c8c416264e8e7273dc4f05c08b8b8ebff39aab78847ae9.proto)
  Character offset 214.

```text
 AssistedGameFeature {
  ASSISTED_GAME_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

```

**Source references:** SRC-0261, SRC-1232  
**URL references:** None independently associated  
**Related findings:** FND-01623, FND-01624, FND-01625

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01627"></a>
## FND-01627: chesscom.computer.v2.AssistedGameFeature.ASSISTED_GAME_FEATURE_HINTS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_HINTS = 3;

### Evidence

- **SRC-0261** `research/proto/chesscom/computer/v2/assisted_game_feature.proto` — [preserved redacted evidence](../evidence/text/5d8aee74efe62ecb71c8c416264e8e7273dc4f05c08b8b8ebff39aab78847ae9.proto)
  Character offset 252.

```text
_FEATURE_UNSPECIFIED = 0;
  ASSISTED_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

```

**Source references:** SRC-0261, SRC-1232  
**URL references:** None independently associated  
**Related findings:** FND-01623, FND-01624, FND-01625

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01628"></a>
## FND-01628: chesscom.computer.v2.AssistedGameFeature.ASSISTED_GAME_FEATURE_THREATS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_THREATS = 4;

### Evidence

- **SRC-0261** `research/proto/chesscom/computer/v2/assisted_game_feature.proto` — [preserved redacted evidence](../evidence/text/5d8aee74efe62ecb71c8c416264e8e7273dc4f05c08b8b8ebff39aab78847ae9.proto)
  Character offset 287.

```text
D_GAME_FEATURE_CHAT = 1;
  ASSISTED_GAME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

```

**Source references:** SRC-0261, SRC-1232  
**URL references:** None independently associated  
**Related findings:** FND-01623, FND-01624, FND-01625

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01629"></a>
## FND-01629: chesscom.computer.v2.AssistedGameFeature.ASSISTED_GAME_FEATURE_EVALUATION = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_EVALUATION = 5;

### Evidence

- **SRC-0261** `research/proto/chesscom/computer/v2/assisted_game_feature.proto` — [preserved redacted evidence](../evidence/text/5d8aee74efe62ecb71c8c416264e8e7273dc4f05c08b8b8ebff39aab78847ae9.proto)
  Character offset 324.

```text
AME_FEATURE_ANALYSIS = 2;
  ASSISTED_GAME_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

```

**Source references:** SRC-0261, SRC-1232  
**URL references:** None independently associated  
**Related findings:** FND-01623, FND-01624, FND-01625

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01630"></a>
## FND-01630: chesscom.computer.v2.AssistedGameFeature.ASSISTED_GAME_FEATURE_ENGINE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_ENGINE = 6;

### Evidence

- **SRC-0261** `research/proto/chesscom/computer/v2/assisted_game_feature.proto` — [preserved redacted evidence](../evidence/text/5d8aee74efe62ecb71c8c416264e8e7273dc4f05c08b8b8ebff39aab78847ae9.proto)
  Character offset 364.

```text
E_FEATURE_HINTS = 3;
  ASSISTED_GAME_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

```

**Source references:** SRC-0261, SRC-1232  
**URL references:** None independently associated  
**Related findings:** FND-01623, FND-01624, FND-01625

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01631"></a>
## FND-01631: chesscom.computer.v2.AssistedGameFeature.ASSISTED_GAME_FEATURE_SUGGESTIONS = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;

### Evidence

- **SRC-0261** `research/proto/chesscom/computer/v2/assisted_game_feature.proto` — [preserved redacted evidence](../evidence/text/5d8aee74efe62ecb71c8c416264e8e7273dc4f05c08b8b8ebff39aab78847ae9.proto)
  Character offset 400.

```text
_FEATURE_THREATS = 4;
  ASSISTED_GAME_FEATURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

```

**Source references:** SRC-0261, SRC-1232  
**URL references:** None independently associated  
**Related findings:** FND-01623, FND-01624, FND-01625

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01632"></a>
## FND-01632: chesscom.computer.v2.AssistedGameFeature.ASSISTED_GAME_FEATURE_TAKEBACKS = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ASSISTED_GAME_FEATURE_TAKEBACKS = 8;

### Evidence

- **SRC-0261** `research/proto/chesscom/computer/v2/assisted_game_feature.proto` — [preserved redacted evidence](../evidence/text/5d8aee74efe62ecb71c8c416264e8e7273dc4f05c08b8b8ebff39aab78847ae9.proto)
  Character offset 441.

```text
TURE_EVALUATION = 5;
  ASSISTED_GAME_FEATURE_ENGINE = 6;
  ASSISTED_GAME_FEATURE_SUGGESTIONS = 7;
  ASSISTED_GAME_FEATURE_TAKEBACKS = 8;
}

```

**Source references:** SRC-0261, SRC-1232  
**URL references:** None independently associated  
**Related findings:** FND-01623, FND-01624, FND-01625

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01633"></a>
## FND-01633: enum declaration: chesscom.computer.v2.GameMode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameMode {

### Evidence

- **SRC-0262** `research/proto/chesscom/computer/v2/game_mode.proto` — [preserved redacted evidence](../evidence/text/04c0c88b8a2177dea4557a89cd4ef2aedb8019296cd91c3f803ee52ecb22cd27.proto)
  Character offset 98.

```text
// source: chesscom/computer/v2/game_mode.proto
// syntax: proto3

package chesscom.computer.v2;

enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

```

**Source references:** SRC-0262, SRC-1233  
**URL references:** None independently associated  
**Related findings:** FND-01634, FND-01635

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01634"></a>
## FND-01634: chesscom.computer.v2.GameMode.GAME_MODE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_MODE_UNSPECIFIED = 0;

### Evidence

- **SRC-0262** `research/proto/chesscom/computer/v2/game_mode.proto` — [preserved redacted evidence](../evidence/text/04c0c88b8a2177dea4557a89cd4ef2aedb8019296cd91c3f803ee52ecb22cd27.proto)
  Character offset 116.

```text
com/computer/v2/game_mode.proto
// syntax: proto3

package chesscom.computer.v2;

enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

```

**Source references:** SRC-0262, SRC-1233  
**URL references:** None independently associated  
**Related findings:** FND-01633, FND-01635

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01635"></a>
## FND-01635: chesscom.computer.v2.GameMode.GAME_MODE_CHALLENGE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_MODE_CHALLENGE = 1;

### Evidence

- **SRC-0262** `research/proto/chesscom/computer/v2/game_mode.proto` — [preserved redacted evidence](../evidence/text/04c0c88b8a2177dea4557a89cd4ef2aedb8019296cd91c3f803ee52ecb22cd27.proto)
  Character offset 145.

```text
to
// syntax: proto3

package chesscom.computer.v2;

enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

```

**Source references:** SRC-0262, SRC-1233  
**URL references:** None independently associated  
**Related findings:** FND-01633, FND-01634

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01636"></a>
## FND-01636: chesscom.computer.v2.GameMode.GAME_MODE_FRIENDLY = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_MODE_FRIENDLY = 2;

### Evidence

- **SRC-0262** `research/proto/chesscom/computer/v2/game_mode.proto` — [preserved redacted evidence](../evidence/text/04c0c88b8a2177dea4557a89cd4ef2aedb8019296cd91c3f803ee52ecb22cd27.proto)
  Character offset 172.

```text
ge chesscom.computer.v2;

enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

```

**Source references:** SRC-0262, SRC-1233  
**URL references:** None independently associated  
**Related findings:** FND-01633, FND-01634, FND-01635

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01637"></a>
## FND-01637: chesscom.computer.v2.GameMode.GAME_MODE_ASSISTED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_MODE_ASSISTED = 3;

### Evidence

- **SRC-0262** `research/proto/chesscom/computer/v2/game_mode.proto` — [preserved redacted evidence](../evidence/text/04c0c88b8a2177dea4557a89cd4ef2aedb8019296cd91c3f803ee52ecb22cd27.proto)
  Character offset 198.

```text
enum GameMode {
  GAME_MODE_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

```

**Source references:** SRC-0262, SRC-1233  
**URL references:** None independently associated  
**Related findings:** FND-01633, FND-01634, FND-01635

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01638"></a>
## FND-01638: chesscom.computer.v2.GameMode.GAME_MODE_CUSTOM = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_MODE_CUSTOM = 4;

### Evidence

- **SRC-0262** `research/proto/chesscom/computer/v2/game_mode.proto` — [preserved redacted evidence](../evidence/text/04c0c88b8a2177dea4557a89cd4ef2aedb8019296cd91c3f803ee52ecb22cd27.proto)
  Character offset 224.

```text
E_UNSPECIFIED = 0;
  GAME_MODE_CHALLENGE = 1;
  GAME_MODE_FRIENDLY = 2;
  GAME_MODE_ASSISTED = 3;
  GAME_MODE_CUSTOM = 4;
}

```

**Source references:** SRC-0262, SRC-1233  
**URL references:** None independently associated  
**Related findings:** FND-01633, FND-01634, FND-01635

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01639"></a>
## FND-01639: message declaration: chesscom.courses.v1.SetConfigurableUserFlagRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetConfigurableUserFlagRequest {

### Evidence

- **SRC-0263** `research/proto/chesscom/courses/v1/configurable_user_flag_service.proto` — [preserved redacted evidence](../evidence/text/565bbf518f3d961535fe255b6c3fd6d83595e4a96c1539786f1e9404aa413cbd.proto)
  Character offset 117.

```text
om/courses/v1/configurable_user_flag_service.proto
// syntax: proto3

package chesscom.courses.v1;

message SetConfigurableUserFlagRequest {
  optional .chesscom.courses.v1.UserFlag user_flag = 1;
}

message SetConfigurableUserFlagResponse {
}

```

**Source references:** SRC-0263, SRC-1234  
**URL references:** None independently associated  
**Related findings:** FND-01640, FND-01641

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01640"></a>
## FND-01640: chesscom.courses.v1.SetConfigurableUserFlagRequest.user_flag = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.UserFlag user_flag = 1;

### Evidence

- **SRC-0263** `research/proto/chesscom/courses/v1/configurable_user_flag_service.proto` — [preserved redacted evidence](../evidence/text/565bbf518f3d961535fe255b6c3fd6d83595e4a96c1539786f1e9404aa413cbd.proto)
  Character offset 160.

```text
e.proto
// syntax: proto3

package chesscom.courses.v1;

message SetConfigurableUserFlagRequest {
  optional .chesscom.courses.v1.UserFlag user_flag = 1;
}

message SetConfigurableUserFlagResponse {
}

```

**Source references:** SRC-0263, SRC-1234  
**URL references:** None independently associated  
**Related findings:** FND-01639, FND-01641

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01641"></a>
## FND-01641: message declaration: chesscom.courses.v1.SetConfigurableUserFlagResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetConfigurableUserFlagResponse {

### Evidence

- **SRC-0263** `research/proto/chesscom/courses/v1/configurable_user_flag_service.proto` — [preserved redacted evidence](../evidence/text/565bbf518f3d961535fe255b6c3fd6d83595e4a96c1539786f1e9404aa413cbd.proto)
  Character offset 217.

```text
message SetConfigurableUserFlagRequest {
  optional .chesscom.courses.v1.UserFlag user_flag = 1;
}

message SetConfigurableUserFlagResponse {
}

```

**Source references:** SRC-0263, SRC-1234  
**URL references:** None independently associated  
**Related findings:** FND-01639, FND-01640

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01642"></a>
## FND-01642: message declaration: chesscom.courses.v1.Course

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Course {

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 93.

```text
// source: chesscom/courses/v1/course.proto
// syntax: proto3

package chesscom.courses.v1;

message Course {
  oneof _canonical_line {
  .chesscom.courses.v1.CourseCanonicalLine canonical_line = 13;
  }
  optional string id = 1;
  optional string title = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional .chesscom.courses.v1.CourseUserLearningInformation user_learning_information = 4;
 
```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01643, FND-01644

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01643"></a>
## FND-01643: oneof declaration: chesscom.courses.v1.Course._canonical_line

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _canonical_line {

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 112.

```text
hesscom/courses/v1/course.proto
// syntax: proto3

package chesscom.courses.v1;

message Course {
  oneof _canonical_line {
  .chesscom.courses.v1.CourseCanonicalLine canonical_line = 13;
  }
  optional string id = 1;
  optional string title = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional .chesscom.courses.v1.CourseUserLearningInformation user_learning_information = 4;
  repeated .chesscom
```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01644

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01644"></a>
## FND-01644: chesscom.courses.v1.Course.canonical_line = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseCanonicalLine canonical_line = 13;

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 138.

```text
proto
// syntax: proto3

package chesscom.courses.v1;

message Course {
  oneof _canonical_line {
  .chesscom.courses.v1.CourseCanonicalLine canonical_line = 13;
  }
  optional string id = 1;
  optional string title = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional .chesscom.courses.v1.CourseUserLearningInformation user_learning_information = 4;
  repeated .chesscom.courses.v1.CourseAuthor a
```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01643

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01645"></a>
## FND-01645: chesscom.courses.v1.Course.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 206.

```text
e {
  oneof _canonical_line {
  .chesscom.courses.v1.CourseCanonicalLine canonical_line = 13;
  }
  optional string id = 1;
  optional string title = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional .chesscom.courses.v1.CourseUserLearningInformation user_learning_information = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional int32 total_variation_amount = 6;
  optional 
```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01643, FND-01644

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01646"></a>
## FND-01646: chesscom.courses.v1.Course.title = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string title = 2;

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 232.

```text
e {
  .chesscom.courses.v1.CourseCanonicalLine canonical_line = 13;
  }
  optional string id = 1;
  optional string title = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional .chesscom.courses.v1.CourseUserLearningInformation user_learning_information = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional int32 total_variation_amount = 6;
  optional bool is_diamond_exclusive 
```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01643, FND-01644

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01647"></a>
## FND-01647: chesscom.courses.v1.Course.picture = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.Picture picture = 3;

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 261.

```text
urseCanonicalLine canonical_line = 13;
  }
  optional string id = 1;
  optional string title = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional .chesscom.courses.v1.CourseUserLearningInformation user_learning_information = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional int32 total_variation_amount = 6;
  optional bool is_diamond_exclusive = 7;
  optional .chesscom.cou
```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01643, FND-01644

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01648"></a>
## FND-01648: chesscom.courses.v1.Course.user_learning_information = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseUserLearningInformation user_learning_information = 4;

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 321.

```text
 id = 1;
  optional string title = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional .chesscom.courses.v1.CourseUserLearningInformation user_learning_information = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional int32 total_variation_amount = 6;
  optional bool is_diamond_exclusive = 7;
  optional .chesscom.courses.v1.OwnershipType ownership_type = 8;
  optional string 
```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01643, FND-01644

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01649"></a>
## FND-01649: chesscom.courses.v1.Course.authors = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseAuthor authors = 5;

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 414.

```text
= 3;
  optional .chesscom.courses.v1.CourseUserLearningInformation user_learning_information = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional int32 total_variation_amount = 6;
  optional bool is_diamond_exclusive = 7;
  optional .chesscom.courses.v1.OwnershipType ownership_type = 8;
  optional string slug = 9;
  optional .chesscom.courses_common.v1.CourseSource course_source = 10;
  optional 
```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01643, FND-01644

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01650"></a>
## FND-01650: chesscom.courses.v1.Course.total_variation_amount = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 total_variation_amount = 6;

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 472.

```text
ormation user_learning_information = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional int32 total_variation_amount = 6;
  optional bool is_diamond_exclusive = 7;
  optional .chesscom.courses.v1.OwnershipType ownership_type = 8;
  optional string slug = 9;
  optional .chesscom.courses_common.v1.CourseSource course_source = 10;
  optional bool is_tutorial = 11;
  optional .chesscom.courses.v1.Use
```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01643, FND-01644

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01651"></a>
## FND-01651: chesscom.courses.v1.Course.is_diamond_exclusive = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_diamond_exclusive = 7;

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 517.

```text
eated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional int32 total_variation_amount = 6;
  optional bool is_diamond_exclusive = 7;
  optional .chesscom.courses.v1.OwnershipType ownership_type = 8;
  optional string slug = 9;
  optional .chesscom.courses_common.v1.CourseSource course_source = 10;
  optional bool is_tutorial = 11;
  optional .chesscom.courses.v1.UserAccessGrant user_access_grant = 12;
}

```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01643, FND-01644

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01652"></a>
## FND-01652: chesscom.courses.v1.Course.ownership_type = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.OwnershipType ownership_type = 8;

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 559.

```text
thors = 5;
  optional int32 total_variation_amount = 6;
  optional bool is_diamond_exclusive = 7;
  optional .chesscom.courses.v1.OwnershipType ownership_type = 8;
  optional string slug = 9;
  optional .chesscom.courses_common.v1.CourseSource course_source = 10;
  optional bool is_tutorial = 11;
  optional .chesscom.courses.v1.UserAccessGrant user_access_grant = 12;
}

```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01643, FND-01644

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01653"></a>
## FND-01653: chesscom.courses.v1.Course.slug = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string slug = 9;

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 625.

```text
 bool is_diamond_exclusive = 7;
  optional .chesscom.courses.v1.OwnershipType ownership_type = 8;
  optional string slug = 9;
  optional .chesscom.courses_common.v1.CourseSource course_source = 10;
  optional bool is_tutorial = 11;
  optional .chesscom.courses.v1.UserAccessGrant user_access_grant = 12;
}

```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01643, FND-01644

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01654"></a>
## FND-01654: chesscom.courses.v1.Course.course_source = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseSource course_source = 10;

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 653.

```text
 7;
  optional .chesscom.courses.v1.OwnershipType ownership_type = 8;
  optional string slug = 9;
  optional .chesscom.courses_common.v1.CourseSource course_source = 10;
  optional bool is_tutorial = 11;
  optional .chesscom.courses.v1.UserAccessGrant user_access_grant = 12;
}

```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01643, FND-01644

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01655"></a>
## FND-01655: chesscom.courses.v1.Course.is_tutorial = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_tutorial = 11;

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 725.

```text
optional string slug = 9;
  optional .chesscom.courses_common.v1.CourseSource course_source = 10;
  optional bool is_tutorial = 11;
  optional .chesscom.courses.v1.UserAccessGrant user_access_grant = 12;
}

```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01643, FND-01644

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01656"></a>
## FND-01656: chesscom.courses.v1.Course.user_access_grant = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.UserAccessGrant user_access_grant = 12;

### Evidence

- **SRC-0264** `research/proto/chesscom/courses/v1/course.proto` — [preserved redacted evidence](../evidence/text/4f8ae90ac0607b347fb134b60526518805751d11ec83ebaa052dbae6b7a094b8.proto)
  Character offset 759.

```text
al .chesscom.courses_common.v1.CourseSource course_source = 10;
  optional bool is_tutorial = 11;
  optional .chesscom.courses.v1.UserAccessGrant user_access_grant = 12;
}

```

**Source references:** SRC-0264, SRC-1235  
**URL references:** None independently associated  
**Related findings:** FND-01642, FND-01643, FND-01644

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01657"></a>
## FND-01657: enum declaration: chesscom.courses.v1.CourseAuthorType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseAuthorType {

### Evidence

- **SRC-0265** `research/proto/chesscom/courses/v1/course_author.proto` — [preserved redacted evidence](../evidence/text/9ab437fe769ae4e51e6abcd12a8cfb430f14100b2188982580e7efa98a31c725.proto)
  Character offset 100.

```text
// source: chesscom/courses/v1/course_author.proto
// syntax: proto3

package chesscom.courses.v1;

enum CourseAuthorType {
  COURSE_AUTHOR_TYPE_UNSPECIFIED = 0;
  COURSE_AUTHOR_TYPE_MAIN = 1;
  COURSE_AUTHOR_TYPE_COAUTHOR = 2;
  COURSE_AUTHOR_TYPE_ENDORSER = 3;
  COURSE_AUTHOR_TYPE_PRESENTER = 4;
}

message CourseAuthor {
  oneof _chess_title {
  string chess_title = 2;
  }
  oneof _picture {
  .chesscom.courses_com
```

**Source references:** SRC-0265, SRC-1236  
**URL references:** None independently associated  
**Related findings:** FND-01658, FND-01659

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01658"></a>
## FND-01658: chesscom.courses.v1.CourseAuthorType.COURSE_AUTHOR_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_AUTHOR_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0265** `research/proto/chesscom/courses/v1/course_author.proto` — [preserved redacted evidence](../evidence/text/9ab437fe769ae4e51e6abcd12a8cfb430f14100b2188982580e7efa98a31c725.proto)
  Character offset 126.

```text
s/v1/course_author.proto
// syntax: proto3

package chesscom.courses.v1;

enum CourseAuthorType {
  COURSE_AUTHOR_TYPE_UNSPECIFIED = 0;
  COURSE_AUTHOR_TYPE_MAIN = 1;
  COURSE_AUTHOR_TYPE_COAUTHOR = 2;
  COURSE_AUTHOR_TYPE_ENDORSER = 3;
  COURSE_AUTHOR_TYPE_PRESENTER = 4;
}

message CourseAuthor {
  oneof _chess_title {
  string chess_title = 2;
  }
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 3
```

**Source references:** SRC-0265, SRC-1236  
**URL references:** None independently associated  
**Related findings:** FND-01657, FND-01659

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01659"></a>
## FND-01659: chesscom.courses.v1.CourseAuthorType.COURSE_AUTHOR_TYPE_MAIN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_AUTHOR_TYPE_MAIN = 1;

### Evidence

- **SRC-0265** `research/proto/chesscom/courses/v1/course_author.proto` — [preserved redacted evidence](../evidence/text/9ab437fe769ae4e51e6abcd12a8cfb430f14100b2188982580e7efa98a31c725.proto)
  Character offset 164.

```text
oto3

package chesscom.courses.v1;

enum CourseAuthorType {
  COURSE_AUTHOR_TYPE_UNSPECIFIED = 0;
  COURSE_AUTHOR_TYPE_MAIN = 1;
  COURSE_AUTHOR_TYPE_COAUTHOR = 2;
  COURSE_AUTHOR_TYPE_ENDORSER = 3;
  COURSE_AUTHOR_TYPE_PRESENTER = 4;
}

message CourseAuthor {
  oneof _chess_title {
  string chess_title = 2;
  }
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 3;
  }
  optional string name = 1;
  op
```

**Source references:** SRC-0265, SRC-1236  
**URL references:** None independently associated  
**Related findings:** FND-01657, FND-01658

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01660"></a>
## FND-01660: chesscom.courses.v1.CourseAuthorType.COURSE_AUTHOR_TYPE_COAUTHOR = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_AUTHOR_TYPE_COAUTHOR = 2;

### Evidence

- **SRC-0265** `research/proto/chesscom/courses/v1/course_author.proto` — [preserved redacted evidence](../evidence/text/9ab437fe769ae4e51e6abcd12a8cfb430f14100b2188982580e7efa98a31c725.proto)
  Character offset 195.

```text
v1;

enum CourseAuthorType {
  COURSE_AUTHOR_TYPE_UNSPECIFIED = 0;
  COURSE_AUTHOR_TYPE_MAIN = 1;
  COURSE_AUTHOR_TYPE_COAUTHOR = 2;
  COURSE_AUTHOR_TYPE_ENDORSER = 3;
  COURSE_AUTHOR_TYPE_PRESENTER = 4;
}

message CourseAuthor {
  oneof _chess_title {
  string chess_title = 2;
  }
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 3;
  }
  optional string name = 1;
  optional .chesscom.courses.v1.Cou
```

**Source references:** SRC-0265, SRC-1236  
**URL references:** None independently associated  
**Related findings:** FND-01657, FND-01658, FND-01659

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01661"></a>
## FND-01661: chesscom.courses.v1.CourseAuthorType.COURSE_AUTHOR_TYPE_ENDORSER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_AUTHOR_TYPE_ENDORSER = 3;

### Evidence

- **SRC-0265** `research/proto/chesscom/courses/v1/course_author.proto` — [preserved redacted evidence](../evidence/text/9ab437fe769ae4e51e6abcd12a8cfb430f14100b2188982580e7efa98a31c725.proto)
  Character offset 230.

```text
SE_AUTHOR_TYPE_UNSPECIFIED = 0;
  COURSE_AUTHOR_TYPE_MAIN = 1;
  COURSE_AUTHOR_TYPE_COAUTHOR = 2;
  COURSE_AUTHOR_TYPE_ENDORSER = 3;
  COURSE_AUTHOR_TYPE_PRESENTER = 4;
}

message CourseAuthor {
  oneof _chess_title {
  string chess_title = 2;
  }
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 3;
  }
  optional string name = 1;
  optional .chesscom.courses.v1.CourseAuthorType type = 4;
}

```

**Source references:** SRC-0265, SRC-1236  
**URL references:** None independently associated  
**Related findings:** FND-01657, FND-01658, FND-01659

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01662"></a>
## FND-01662: chesscom.courses.v1.CourseAuthorType.COURSE_AUTHOR_TYPE_PRESENTER = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_AUTHOR_TYPE_PRESENTER = 4;

### Evidence

- **SRC-0265** `research/proto/chesscom/courses/v1/course_author.proto` — [preserved redacted evidence](../evidence/text/9ab437fe769ae4e51e6abcd12a8cfb430f14100b2188982580e7efa98a31c725.proto)
  Character offset 265.

```text
OURSE_AUTHOR_TYPE_MAIN = 1;
  COURSE_AUTHOR_TYPE_COAUTHOR = 2;
  COURSE_AUTHOR_TYPE_ENDORSER = 3;
  COURSE_AUTHOR_TYPE_PRESENTER = 4;
}

message CourseAuthor {
  oneof _chess_title {
  string chess_title = 2;
  }
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 3;
  }
  optional string name = 1;
  optional .chesscom.courses.v1.CourseAuthorType type = 4;
}

```

**Source references:** SRC-0265, SRC-1236  
**URL references:** None independently associated  
**Related findings:** FND-01657, FND-01658, FND-01659

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01663"></a>
## FND-01663: message declaration: chesscom.courses.v1.CourseAuthor

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseAuthor {

### Evidence

- **SRC-0265** `research/proto/chesscom/courses/v1/course_author.proto` — [preserved redacted evidence](../evidence/text/9ab437fe769ae4e51e6abcd12a8cfb430f14100b2188982580e7efa98a31c725.proto)
  Character offset 302.

```text
AUTHOR_TYPE_COAUTHOR = 2;
  COURSE_AUTHOR_TYPE_ENDORSER = 3;
  COURSE_AUTHOR_TYPE_PRESENTER = 4;
}

message CourseAuthor {
  oneof _chess_title {
  string chess_title = 2;
  }
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 3;
  }
  optional string name = 1;
  optional .chesscom.courses.v1.CourseAuthorType type = 4;
}

```

**Source references:** SRC-0265, SRC-1236  
**URL references:** None independently associated  
**Related findings:** FND-01657, FND-01658, FND-01659

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01664"></a>
## FND-01664: oneof declaration: chesscom.courses.v1.CourseAuthor._chess_title

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _chess_title {

### Evidence

- **SRC-0265** `research/proto/chesscom/courses/v1/course_author.proto` — [preserved redacted evidence](../evidence/text/9ab437fe769ae4e51e6abcd12a8cfb430f14100b2188982580e7efa98a31c725.proto)
  Character offset 327.

```text

  COURSE_AUTHOR_TYPE_ENDORSER = 3;
  COURSE_AUTHOR_TYPE_PRESENTER = 4;
}

message CourseAuthor {
  oneof _chess_title {
  string chess_title = 2;
  }
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 3;
  }
  optional string name = 1;
  optional .chesscom.courses.v1.CourseAuthorType type = 4;
}

```

**Source references:** SRC-0265, SRC-1236  
**URL references:** None independently associated  
**Related findings:** FND-01657, FND-01658, FND-01659

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01665"></a>
## FND-01665: chesscom.courses.v1.CourseAuthor.chess_title = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string chess_title = 2;

### Evidence

- **SRC-0265** `research/proto/chesscom/courses/v1/course_author.proto` — [preserved redacted evidence](../evidence/text/9ab437fe769ae4e51e6abcd12a8cfb430f14100b2188982580e7efa98a31c725.proto)
  Character offset 350.

```text
NDORSER = 3;
  COURSE_AUTHOR_TYPE_PRESENTER = 4;
}

message CourseAuthor {
  oneof _chess_title {
  string chess_title = 2;
  }
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 3;
  }
  optional string name = 1;
  optional .chesscom.courses.v1.CourseAuthorType type = 4;
}

```

**Source references:** SRC-0265, SRC-1236  
**URL references:** None independently associated  
**Related findings:** FND-01657, FND-01658, FND-01659

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01666"></a>
## FND-01666: oneof declaration: chesscom.courses.v1.CourseAuthor._picture

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _picture {

### Evidence

- **SRC-0265** `research/proto/chesscom/courses/v1/course_author.proto` — [preserved redacted evidence](../evidence/text/9ab437fe769ae4e51e6abcd12a8cfb430f14100b2188982580e7efa98a31c725.proto)
  Character offset 380.

```text
YPE_PRESENTER = 4;
}

message CourseAuthor {
  oneof _chess_title {
  string chess_title = 2;
  }
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 3;
  }
  optional string name = 1;
  optional .chesscom.courses.v1.CourseAuthorType type = 4;
}

```

**Source references:** SRC-0265, SRC-1236  
**URL references:** None independently associated  
**Related findings:** FND-01657, FND-01658, FND-01659

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01667"></a>
## FND-01667: chesscom.courses.v1.CourseAuthor.picture = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses_common.v1.Picture picture = 3;

### Evidence

- **SRC-0265** `research/proto/chesscom/courses/v1/course_author.proto` — [preserved redacted evidence](../evidence/text/9ab437fe769ae4e51e6abcd12a8cfb430f14100b2188982580e7efa98a31c725.proto)
  Character offset 399.

```text
}

message CourseAuthor {
  oneof _chess_title {
  string chess_title = 2;
  }
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 3;
  }
  optional string name = 1;
  optional .chesscom.courses.v1.CourseAuthorType type = 4;
}

```

**Source references:** SRC-0265, SRC-1236  
**URL references:** None independently associated  
**Related findings:** FND-01657, FND-01658, FND-01659

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01668"></a>
## FND-01668: chesscom.courses.v1.CourseAuthor.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0265** `research/proto/chesscom/courses/v1/course_author.proto` — [preserved redacted evidence](../evidence/text/9ab437fe769ae4e51e6abcd12a8cfb430f14100b2188982580e7efa98a31c725.proto)
  Character offset 454.

```text
ng chess_title = 2;
  }
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 3;
  }
  optional string name = 1;
  optional .chesscom.courses.v1.CourseAuthorType type = 4;
}

```

**Source references:** SRC-0265, SRC-1236  
**URL references:** None independently associated  
**Related findings:** FND-01657, FND-01658, FND-01659

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01669"></a>
## FND-01669: chesscom.courses.v1.CourseAuthor.type = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseAuthorType type = 4;

### Evidence

- **SRC-0265** `research/proto/chesscom/courses/v1/course_author.proto` — [preserved redacted evidence](../evidence/text/9ab437fe769ae4e51e6abcd12a8cfb430f14100b2188982580e7efa98a31c725.proto)
  Character offset 482.

```text
eof _picture {
  .chesscom.courses_common.v1.Picture picture = 3;
  }
  optional string name = 1;
  optional .chesscom.courses.v1.CourseAuthorType type = 4;
}

```

**Source references:** SRC-0265, SRC-1236  
**URL references:** None independently associated  
**Related findings:** FND-01657, FND-01658, FND-01659

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01670"></a>
## FND-01670: message declaration: chesscom.courses.v1.CourseCanonicalLine

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseCanonicalLine {

### Evidence

- **SRC-0266** `research/proto/chesscom/courses/v1/course_canonical_line.proto` — [preserved redacted evidence](../evidence/text/5388b49d53caa858a82e05a5207883e662d47c65b7a1e2cf919376c54393d826.proto)
  Character offset 108.

```text
e: chesscom/courses/v1/course_canonical_line.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseCanonicalLine {
  repeated string moves = 1;
}

```

**Source references:** SRC-0266, SRC-1237  
**URL references:** None independently associated  
**Related findings:** FND-01671

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01671"></a>
## FND-01671: chesscom.courses.v1.CourseCanonicalLine.moves = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string moves = 1;

### Evidence

- **SRC-0266** `research/proto/chesscom/courses/v1/course_canonical_line.proto` — [preserved redacted evidence](../evidence/text/5388b49d53caa858a82e05a5207883e662d47c65b7a1e2cf919376c54393d826.proto)
  Character offset 140.

```text
nonical_line.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseCanonicalLine {
  repeated string moves = 1;
}

```

**Source references:** SRC-0266, SRC-1237  
**URL references:** None independently associated  
**Related findings:** FND-01670

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01672"></a>
## FND-01672: message declaration: chesscom.courses.v1.CourseChapter

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseChapter {

### Evidence

- **SRC-0267** `research/proto/chesscom/courses/v1/course_chapter.proto` — [preserved redacted evidence](../evidence/text/ee405a9161cc794693ce5b9505e13d025201dcfc1227ce009872e1022de0c742.proto)
  Character offset 101.

```text
/ source: chesscom/courses/v1/course_chapter.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseChapter {
  oneof _video {
  .chesscom.courses_common.v1.CourseVideo video = 3;
  }
  oneof _user_video_position {
  int32 user_video_position = 4;
  }
  optional string id = 1;
  optional string name = 2;
}

```

**Source references:** SRC-0267, SRC-1238  
**URL references:** None independently associated  
**Related findings:** FND-01673, FND-01674

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01673"></a>
## FND-01673: oneof declaration: chesscom.courses.v1.CourseChapter._video

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _video {

### Evidence

- **SRC-0267** `research/proto/chesscom/courses/v1/course_chapter.proto` — [preserved redacted evidence](../evidence/text/ee405a9161cc794693ce5b9505e13d025201dcfc1227ce009872e1022de0c742.proto)
  Character offset 127.

```text
/v1/course_chapter.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseChapter {
  oneof _video {
  .chesscom.courses_common.v1.CourseVideo video = 3;
  }
  oneof _user_video_position {
  int32 user_video_position = 4;
  }
  optional string id = 1;
  optional string name = 2;
}

```

**Source references:** SRC-0267, SRC-1238  
**URL references:** None independently associated  
**Related findings:** FND-01672, FND-01674

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01674"></a>
## FND-01674: chesscom.courses.v1.CourseChapter.video = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses_common.v1.CourseVideo video = 3;

### Evidence

- **SRC-0267** `research/proto/chesscom/courses/v1/course_chapter.proto` — [preserved redacted evidence](../evidence/text/ee405a9161cc794693ce5b9505e13d025201dcfc1227ce009872e1022de0c742.proto)
  Character offset 144.

```text
r.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseChapter {
  oneof _video {
  .chesscom.courses_common.v1.CourseVideo video = 3;
  }
  oneof _user_video_position {
  int32 user_video_position = 4;
  }
  optional string id = 1;
  optional string name = 2;
}

```

**Source references:** SRC-0267, SRC-1238  
**URL references:** None independently associated  
**Related findings:** FND-01672, FND-01673

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
