# data_models — findings 8101–8200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-08375"></a>
## FND-08375: message declaration: chesscom.skills.v1.GetSkillsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSkillsResponse {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1222.

```text
e {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

message GetSkillsRequest {
}

message GetSkillsResponse {
  repeated .chesscom.skills.v1.SkillView skill_items = 1;
  optional bool has_mastered_all = 2;
}

message GetSkillsPositionsRequest {
  optional string game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
}

message GetSkillsPositionsResponse {
  oneof
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08376"></a>
## FND-08376: chesscom.skills.v1.GetSkillsResponse.skill_items = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.skills.v1.SkillView skill_items = 1;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1252.

```text
s.v1.EligibilityError error = 1;
  }
}

message GetSkillsRequest {
}

message GetSkillsResponse {
  repeated .chesscom.skills.v1.SkillView skill_items = 1;
  optional bool has_mastered_all = 2;
}

message GetSkillsPositionsRequest {
  optional string game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
}

message GetSkillsPositionsResponse {
  oneof result {
  .chesscom.skills.v
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08377"></a>
## FND-08377: chesscom.skills.v1.GetSkillsResponse.has_mastered_all = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool has_mastered_all = 2;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1310.

```text
equest {
}

message GetSkillsResponse {
  repeated .chesscom.skills.v1.SkillView skill_items = 1;
  optional bool has_mastered_all = 2;
}

message GetSkillsPositionsRequest {
  optional string game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
}

message GetSkillsPositionsResponse {
  oneof result {
  .chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsSuccess suc
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08378"></a>
## FND-08378: message declaration: chesscom.skills.v1.GetSkillsPositionsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSkillsPositionsRequest {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1349.

```text

  repeated .chesscom.skills.v1.SkillView skill_items = 1;
  optional bool has_mastered_all = 2;
}

message GetSkillsPositionsRequest {
  optional string game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
}

message GetSkillsPositionsResponse {
  oneof result {
  .chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsSuccess success = 1;
  .chesscom.skills.v1.GetSkil
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08379"></a>
## FND-08379: chesscom.skills.v1.GetSkillsPositionsRequest.game_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_id = 1;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 311.

```text
nput = 3;
  .chesscom.skills.v1.GainSkillPointsRequest.GameReviewInput game_review_input = 4;
  }
  optional string game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
  message CoachInput {
  optional .chesscom.chess.v1.Color player_color = 1;
  }
  message GameReviewInput {
  }
}

message GainSkillPointsResponse {
  oneof result {
  .chesscom.skills.v1.GainSkillPointsResponse
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08380"></a>
## FND-08380: chesscom.skills.v1.GetSkillsPositionsRequest.skill_positions = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 342.

```text
.GainSkillPointsRequest.GameReviewInput game_review_input = 4;
  }
  optional string game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
  message CoachInput {
  optional .chesscom.chess.v1.Color player_color = 1;
  }
  message GameReviewInput {
  }
}

message GainSkillPointsResponse {
  oneof result {
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess success
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08381"></a>
## FND-08381: message declaration: chesscom.skills.v1.GetSkillsPositionsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSkillsPositionsResponse {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1498.

```text
ring game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
}

message GetSkillsPositionsResponse {
  oneof result {
  .chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsSuccess success = 1;
  .chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsFailure failure = 2;
  }
  message GetSkillsPositionsSuccess {
  repeated .chesscom.explanation_engine.v1.Skill
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08382"></a>
## FND-08382: oneof declaration: chesscom.skills.v1.GetSkillsPositionsResponse.result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof result {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 571.

```text
.Color player_color = 1;
  }
  message GameReviewInput {
  }
}

message GainSkillPointsResponse {
  oneof result {
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess success = 1;
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsFailure failure = 2;
  }
  message GainSkillPointsSuccess {
  repeated .chesscom.explanation_engine.v1.Skill skills_unlocked = 1;
  repeated .chesscom.skills.v1.S
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08383"></a>
## FND-08383: chesscom.skills.v1.GetSkillsPositionsResponse.success = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsSuccess success = 1;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1554.

```text
e.v1.SkillsPosition skill_positions = 2;
}

message GetSkillsPositionsResponse {
  oneof result {
  .chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsSuccess success = 1;
  .chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsFailure failure = 2;
  }
  message GetSkillsPositionsSuccess {
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 1;
  }
  message GetSkillsPo
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08384"></a>
## FND-08384: chesscom.skills.v1.GetSkillsPositionsResponse.failure = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsFailure failure = 2;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1642.

```text
 result {
  .chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsSuccess success = 1;
  .chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsFailure failure = 2;
  }
  message GetSkillsPositionsSuccess {
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 1;
  }
  message GetSkillsPositionsFailure {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

messa
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08385"></a>
## FND-08385: message declaration: chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsSuccess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSkillsPositionsSuccess {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1734.

```text
 = 1;
  .chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsFailure failure = 2;
  }
  message GetSkillsPositionsSuccess {
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 1;
  }
  message GetSkillsPositionsFailure {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

message GetConfigRequest {
  oneof _version {
  string version = 1;
  }
}

message GetConfigRespo
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08386"></a>
## FND-08386: chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsSuccess.skill_positions = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 1;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1772.

```text
ositionsResponse.GetSkillsPositionsFailure failure = 2;
  }
  message GetSkillsPositionsSuccess {
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 1;
  }
  message GetSkillsPositionsFailure {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

message GetConfigRequest {
  oneof _version {
  string version = 1;
  }
}

message GetConfigResponse {
  oneof _skill_configuration {
 
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08387"></a>
## FND-08387: message declaration: chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsFailure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSkillsPositionsFailure {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1855.

```text
tionsSuccess {
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 1;
  }
  message GetSkillsPositionsFailure {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

message GetConfigRequest {
  oneof _version {
  string version = 1;
  }
}

message GetConfigResponse {
  oneof _skill_configuration {
  .chesscom.skills.v1.SkillConfiguration skill_configuration = 3;
  }
  oneof _skill
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08388"></a>
## FND-08388: chesscom.skills.v1.GetSkillsPositionsResponse.GetSkillsPositionsFailure.error = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.skills.v1.EligibilityError error = 1;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1128.

```text
ed_all = 4;
  optional bool is_first_ever_skill_point = 5;
  }
  message GainSkillPointsFailure {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

message GetSkillsRequest {
}

message GetSkillsResponse {
  repeated .chesscom.skills.v1.SkillView skill_items = 1;
  optional bool has_mastered_all = 2;
}

message GetSkillsPositionsRequest {
  optional string game_id = 1;
  repeated .chesscom.explanation
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08389"></a>
## FND-08389: message declaration: chesscom.skills.v1.GetConfigRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetConfigRequest {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1957.

```text
ssage GetSkillsPositionsFailure {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

message GetConfigRequest {
  oneof _version {
  string version = 1;
  }
}

message GetConfigResponse {
  oneof _skill_configuration {
  .chesscom.skills.v1.SkillConfiguration skill_configuration = 3;
  }
  oneof _skill_category_configuration {
  .chesscom.skills.v1.SkillCategoryConfiguration skill_category_configuratio
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08390"></a>
## FND-08390: oneof declaration: chesscom.skills.v1.GetConfigRequest._version

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _version {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1986.

```text
re {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

message GetConfigRequest {
  oneof _version {
  string version = 1;
  }
}

message GetConfigResponse {
  oneof _skill_configuration {
  .chesscom.skills.v1.SkillConfiguration skill_configuration = 3;
  }
  oneof _skill_category_configuration {
  .chesscom.skills.v1.SkillCategoryConfiguration skill_category_configuration = 4;
  }
  optional .chessc
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08391"></a>
## FND-08391: chesscom.skills.v1.GetConfigRequest.version = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string version = 1;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2005.

```text
esscom.skills.v1.EligibilityError error = 1;
  }
}

message GetConfigRequest {
  oneof _version {
  string version = 1;
  }
}

message GetConfigResponse {
  oneof _skill_configuration {
  .chesscom.skills.v1.SkillConfiguration skill_configuration = 3;
  }
  oneof _skill_category_configuration {
  .chesscom.skills.v1.SkillCategoryConfiguration skill_category_configuration = 4;
  }
  optional .chesscom.skills.v1.GetCon
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08392"></a>
## FND-08392: message declaration: chesscom.skills.v1.GetConfigResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetConfigResponse {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2032.

```text
yError error = 1;
  }
}

message GetConfigRequest {
  oneof _version {
  string version = 1;
  }
}

message GetConfigResponse {
  oneof _skill_configuration {
  .chesscom.skills.v1.SkillConfiguration skill_configuration = 3;
  }
  oneof _skill_category_configuration {
  .chesscom.skills.v1.SkillCategoryConfiguration skill_category_configuration = 4;
  }
  optional .chesscom.skills.v1.GetConfigResponse.Status status =
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08393"></a>
## FND-08393: oneof declaration: chesscom.skills.v1.GetConfigResponse._skill_configuration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _skill_configuration {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2062.

```text
ge GetConfigRequest {
  oneof _version {
  string version = 1;
  }
}

message GetConfigResponse {
  oneof _skill_configuration {
  .chesscom.skills.v1.SkillConfiguration skill_configuration = 3;
  }
  oneof _skill_category_configuration {
  .chesscom.skills.v1.SkillCategoryConfiguration skill_category_configuration = 4;
  }
  optional .chesscom.skills.v1.GetConfigResponse.Status status = 1;
  optional string version 
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08394"></a>
## FND-08394: chesscom.skills.v1.GetConfigResponse.skill_configuration = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.skills.v1.SkillConfiguration skill_configuration = 3;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2093.

```text
version {
  string version = 1;
  }
}

message GetConfigResponse {
  oneof _skill_configuration {
  .chesscom.skills.v1.SkillConfiguration skill_configuration = 3;
  }
  oneof _skill_category_configuration {
  .chesscom.skills.v1.SkillCategoryConfiguration skill_category_configuration = 4;
  }
  optional .chesscom.skills.v1.GetConfigResponse.Status status = 1;
  optional string version = 2;
  enum Status {
    STATUS
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08395"></a>
## FND-08395: oneof declaration: chesscom.skills.v1.GetConfigResponse._skill_category_configuration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _skill_category_configuration {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2163.

```text
neof _skill_configuration {
  .chesscom.skills.v1.SkillConfiguration skill_configuration = 3;
  }
  oneof _skill_category_configuration {
  .chesscom.skills.v1.SkillCategoryConfiguration skill_category_configuration = 4;
  }
  optional .chesscom.skills.v1.GetConfigResponse.Status status = 1;
  optional string version = 2;
  enum Status {
    STATUS_UNSPECIFIED = 0;
    STATUS_NEW_VERSION_AVAILABLE = 1;
    STATUS_UP_
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08396"></a>
## FND-08396: chesscom.skills.v1.GetConfigResponse.skill_category_configuration = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.skills.v1.SkillCategoryConfiguration skill_category_configuration = 4;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2203.

```text
skills.v1.SkillConfiguration skill_configuration = 3;
  }
  oneof _skill_category_configuration {
  .chesscom.skills.v1.SkillCategoryConfiguration skill_category_configuration = 4;
  }
  optional .chesscom.skills.v1.GetConfigResponse.Status status = 1;
  optional string version = 2;
  enum Status {
    STATUS_UNSPECIFIED = 0;
    STATUS_NEW_VERSION_AVAILABLE = 1;
    STATUS_UP_TO_DATE = 2;
  }
}

message ResetSkillsR
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08397"></a>
## FND-08397: chesscom.skills.v1.GetConfigResponse.status = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.skills.v1.GetConfigResponse.Status status = 1;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2290.

```text
guration {
  .chesscom.skills.v1.SkillCategoryConfiguration skill_category_configuration = 4;
  }
  optional .chesscom.skills.v1.GetConfigResponse.Status status = 1;
  optional string version = 2;
  enum Status {
    STATUS_UNSPECIFIED = 0;
    STATUS_NEW_VERSION_AVAILABLE = 1;
    STATUS_UP_TO_DATE = 2;
  }
}

message ResetSkillsRequest {
}

message ResetSkillsResponse {
}

```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08398"></a>
## FND-08398: chesscom.skills.v1.GetConfigResponse.version = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string version = 2;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2358.

```text
tegory_configuration = 4;
  }
  optional .chesscom.skills.v1.GetConfigResponse.Status status = 1;
  optional string version = 2;
  enum Status {
    STATUS_UNSPECIFIED = 0;
    STATUS_NEW_VERSION_AVAILABLE = 1;
    STATUS_UP_TO_DATE = 2;
  }
}

message ResetSkillsRequest {
}

message ResetSkillsResponse {
}

```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08399"></a>
## FND-08399: enum declaration: chesscom.skills.v1.GetConfigResponse.Status

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Status {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2389.

```text
 optional .chesscom.skills.v1.GetConfigResponse.Status status = 1;
  optional string version = 2;
  enum Status {
    STATUS_UNSPECIFIED = 0;
    STATUS_NEW_VERSION_AVAILABLE = 1;
    STATUS_UP_TO_DATE = 2;
  }
}

message ResetSkillsRequest {
}

message ResetSkillsResponse {
}

```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08400"></a>
## FND-08400: chesscom.skills.v1.GetConfigResponse.Status.STATUS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_UNSPECIFIED = 0;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2407.

```text
m.skills.v1.GetConfigResponse.Status status = 1;
  optional string version = 2;
  enum Status {
    STATUS_UNSPECIFIED = 0;
    STATUS_NEW_VERSION_AVAILABLE = 1;
    STATUS_UP_TO_DATE = 2;
  }
}

message ResetSkillsRequest {
}

message ResetSkillsResponse {
}

```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08401"></a>
## FND-08401: chesscom.skills.v1.GetConfigResponse.Status.STATUS_NEW_VERSION_AVAILABLE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_NEW_VERSION_AVAILABLE = 1;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2435.

```text
e.Status status = 1;
  optional string version = 2;
  enum Status {
    STATUS_UNSPECIFIED = 0;
    STATUS_NEW_VERSION_AVAILABLE = 1;
    STATUS_UP_TO_DATE = 2;
  }
}

message ResetSkillsRequest {
}

message ResetSkillsResponse {
}

```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08402"></a>
## FND-08402: chesscom.skills.v1.GetConfigResponse.Status.STATUS_UP_TO_DATE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STATUS_UP_TO_DATE = 2;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2473.

```text
 version = 2;
  enum Status {
    STATUS_UNSPECIFIED = 0;
    STATUS_NEW_VERSION_AVAILABLE = 1;
    STATUS_UP_TO_DATE = 2;
  }
}

message ResetSkillsRequest {
}

message ResetSkillsResponse {
}

```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08403"></a>
## FND-08403: message declaration: chesscom.skills.v1.ResetSkillsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ResetSkillsRequest {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2503.

```text
    STATUS_UNSPECIFIED = 0;
    STATUS_NEW_VERSION_AVAILABLE = 1;
    STATUS_UP_TO_DATE = 2;
  }
}

message ResetSkillsRequest {
}

message ResetSkillsResponse {
}

```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08404"></a>
## FND-08404: message declaration: chesscom.skills.v1.ResetSkillsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ResetSkillsResponse {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 2535.

```text
STATUS_NEW_VERSION_AVAILABLE = 1;
    STATUS_UP_TO_DATE = 2;
  }
}

message ResetSkillsRequest {
}

message ResetSkillsResponse {
}

```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08405"></a>
## FND-08405: enum declaration: chesscom.skills.v1.SkillStatus

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SkillStatus {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 98.

```text
// source: chesscom/skills/v1/user_activity.proto
// syntax: proto3

package chesscom.skills.v1;

enum SkillStatus {
  SKILL_STATUS_UNSPECIFIED = 0;
  SKILL_STATUS_UNLOCKED = 1;
  SKILL_STATUS_LOCKED = 2;
  SKILL_STATUS_MASTERED = 3;
}

enum SkillSettingsNewState {
  SKILL_SETTINGS_NEW_STATE_UNSPECIFIED = 0;
  SKILL_SETTINGS_NEW_STATE_ON = 1;
  SKILL_SETTINGS_NEW_STATE_OFF = 2;
}

enum SkillSettingsEntryPoint {
  S
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08406"></a>
## FND-08406: chesscom.skills.v1.SkillStatus.SKILL_STATUS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_STATUS_UNSPECIFIED = 0;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 119.

```text
/skills/v1/user_activity.proto
// syntax: proto3

package chesscom.skills.v1;

enum SkillStatus {
  SKILL_STATUS_UNSPECIFIED = 0;
  SKILL_STATUS_UNLOCKED = 1;
  SKILL_STATUS_LOCKED = 2;
  SKILL_STATUS_MASTERED = 3;
}

enum SkillSettingsNewState {
  SKILL_SETTINGS_NEW_STATE_UNSPECIFIED = 0;
  SKILL_SETTINGS_NEW_STATE_ON = 1;
  SKILL_SETTINGS_NEW_STATE_OFF = 2;
}

enum SkillSettingsEntryPoint {
  SKILL_SETTINGS_ENTRY_P
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08407"></a>
## FND-08407: chesscom.skills.v1.SkillStatus.SKILL_STATUS_UNLOCKED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_STATUS_UNLOCKED = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 151.

```text
/ syntax: proto3

package chesscom.skills.v1;

enum SkillStatus {
  SKILL_STATUS_UNSPECIFIED = 0;
  SKILL_STATUS_UNLOCKED = 1;
  SKILL_STATUS_LOCKED = 2;
  SKILL_STATUS_MASTERED = 3;
}

enum SkillSettingsNewState {
  SKILL_SETTINGS_NEW_STATE_UNSPECIFIED = 0;
  SKILL_SETTINGS_NEW_STATE_ON = 1;
  SKILL_SETTINGS_NEW_STATE_OFF = 2;
}

enum SkillSettingsEntryPoint {
  SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED = 0;
  SKILL_SE
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08408"></a>
## FND-08408: chesscom.skills.v1.SkillStatus.SKILL_STATUS_LOCKED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_STATUS_LOCKED = 2;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 180.

```text
sscom.skills.v1;

enum SkillStatus {
  SKILL_STATUS_UNSPECIFIED = 0;
  SKILL_STATUS_UNLOCKED = 1;
  SKILL_STATUS_LOCKED = 2;
  SKILL_STATUS_MASTERED = 3;
}

enum SkillSettingsNewState {
  SKILL_SETTINGS_NEW_STATE_UNSPECIFIED = 0;
  SKILL_SETTINGS_NEW_STATE_ON = 1;
  SKILL_SETTINGS_NEW_STATE_OFF = 2;
}

enum SkillSettingsEntryPoint {
  SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED = 0;
  SKILL_SETTINGS_ENTRY_POINT_COACH_SETT
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08409"></a>
## FND-08409: chesscom.skills.v1.SkillStatus.SKILL_STATUS_MASTERED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_STATUS_MASTERED = 3;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 207.

```text
lStatus {
  SKILL_STATUS_UNSPECIFIED = 0;
  SKILL_STATUS_UNLOCKED = 1;
  SKILL_STATUS_LOCKED = 2;
  SKILL_STATUS_MASTERED = 3;
}

enum SkillSettingsNewState {
  SKILL_SETTINGS_NEW_STATE_UNSPECIFIED = 0;
  SKILL_SETTINGS_NEW_STATE_ON = 1;
  SKILL_SETTINGS_NEW_STATE_OFF = 2;
}

enum SkillSettingsEntryPoint {
  SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED = 0;
  SKILL_SETTINGS_ENTRY_POINT_COACH_SETTINGS = 1;
  SKILL_SETTINGS_
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08410"></a>
## FND-08410: enum declaration: chesscom.skills.v1.SkillSettingsNewState

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SkillSettingsNewState {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 237.

```text
CIFIED = 0;
  SKILL_STATUS_UNLOCKED = 1;
  SKILL_STATUS_LOCKED = 2;
  SKILL_STATUS_MASTERED = 3;
}

enum SkillSettingsNewState {
  SKILL_SETTINGS_NEW_STATE_UNSPECIFIED = 0;
  SKILL_SETTINGS_NEW_STATE_ON = 1;
  SKILL_SETTINGS_NEW_STATE_OFF = 2;
}

enum SkillSettingsEntryPoint {
  SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED = 0;
  SKILL_SETTINGS_ENTRY_POINT_COACH_SETTINGS = 1;
  SKILL_SETTINGS_ENTRY_POINT_GAME_REVIEW_SETTIN
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08411"></a>
## FND-08411: chesscom.skills.v1.SkillSettingsNewState.SKILL_SETTINGS_NEW_STATE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_SETTINGS_NEW_STATE_UNSPECIFIED = 0;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 268.

```text
CKED = 1;
  SKILL_STATUS_LOCKED = 2;
  SKILL_STATUS_MASTERED = 3;
}

enum SkillSettingsNewState {
  SKILL_SETTINGS_NEW_STATE_UNSPECIFIED = 0;
  SKILL_SETTINGS_NEW_STATE_ON = 1;
  SKILL_SETTINGS_NEW_STATE_OFF = 2;
}

enum SkillSettingsEntryPoint {
  SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED = 0;
  SKILL_SETTINGS_ENTRY_POINT_COACH_SETTINGS = 1;
  SKILL_SETTINGS_ENTRY_POINT_GAME_REVIEW_SETTINGS = 2;
  SKILL_SETTINGS_ENTRY_
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08412"></a>
## FND-08412: chesscom.skills.v1.SkillSettingsNewState.SKILL_SETTINGS_NEW_STATE_ON = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_SETTINGS_NEW_STATE_ON = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 312.

```text
_STATUS_MASTERED = 3;
}

enum SkillSettingsNewState {
  SKILL_SETTINGS_NEW_STATE_UNSPECIFIED = 0;
  SKILL_SETTINGS_NEW_STATE_ON = 1;
  SKILL_SETTINGS_NEW_STATE_OFF = 2;
}

enum SkillSettingsEntryPoint {
  SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED = 0;
  SKILL_SETTINGS_ENTRY_POINT_COACH_SETTINGS = 1;
  SKILL_SETTINGS_ENTRY_POINT_GAME_REVIEW_SETTINGS = 2;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_START_SETTINGS = 3;
  SKILL
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08413"></a>
## FND-08413: chesscom.skills.v1.SkillSettingsNewState.SKILL_SETTINGS_NEW_STATE_OFF = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_SETTINGS_NEW_STATE_OFF = 2;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 347.

```text
SettingsNewState {
  SKILL_SETTINGS_NEW_STATE_UNSPECIFIED = 0;
  SKILL_SETTINGS_NEW_STATE_ON = 1;
  SKILL_SETTINGS_NEW_STATE_OFF = 2;
}

enum SkillSettingsEntryPoint {
  SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED = 0;
  SKILL_SETTINGS_ENTRY_POINT_COACH_SETTINGS = 1;
  SKILL_SETTINGS_ENTRY_POINT_GAME_REVIEW_SETTINGS = 2;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_START_SETTINGS = 3;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_SE
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08414"></a>
## FND-08414: enum declaration: chesscom.skills.v1.SkillSettingsEntryPoint

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SkillSettingsEntryPoint {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 384.

```text
EW_STATE_UNSPECIFIED = 0;
  SKILL_SETTINGS_NEW_STATE_ON = 1;
  SKILL_SETTINGS_NEW_STATE_OFF = 2;
}

enum SkillSettingsEntryPoint {
  SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED = 0;
  SKILL_SETTINGS_ENTRY_POINT_COACH_SETTINGS = 1;
  SKILL_SETTINGS_ENTRY_POINT_GAME_REVIEW_SETTINGS = 2;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_START_SETTINGS = 3;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_SETTINGS = 4;
}

message SkillContextEx
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08415"></a>
## FND-08415: chesscom.skills.v1.SkillSettingsEntryPoint.SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED = 0;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 417.

```text
_SETTINGS_NEW_STATE_ON = 1;
  SKILL_SETTINGS_NEW_STATE_OFF = 2;
}

enum SkillSettingsEntryPoint {
  SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED = 0;
  SKILL_SETTINGS_ENTRY_POINT_COACH_SETTINGS = 1;
  SKILL_SETTINGS_ENTRY_POINT_GAME_REVIEW_SETTINGS = 2;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_START_SETTINGS = 3;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_SETTINGS = 4;
}

message SkillContextExtension {
  optional .chesscom.ex
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08416"></a>
## FND-08416: chesscom.skills.v1.SkillSettingsEntryPoint.SKILL_SETTINGS_ENTRY_POINT_COACH_SETTINGS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_SETTINGS_ENTRY_POINT_COACH_SETTINGS = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 463.

```text
EW_STATE_OFF = 2;
}

enum SkillSettingsEntryPoint {
  SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED = 0;
  SKILL_SETTINGS_ENTRY_POINT_COACH_SETTINGS = 1;
  SKILL_SETTINGS_ENTRY_POINT_GAME_REVIEW_SETTINGS = 2;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_START_SETTINGS = 3;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_SETTINGS = 4;
}

message SkillContextExtension {
  optional .chesscom.explanation_engine.v1.Skill skill_id = 1;
  opti
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08417"></a>
## FND-08417: chesscom.skills.v1.SkillSettingsEntryPoint.SKILL_SETTINGS_ENTRY_POINT_GAME_REVIEW_SETTINGS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_SETTINGS_ENTRY_POINT_GAME_REVIEW_SETTINGS = 2;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 512.

```text
 {
  SKILL_SETTINGS_ENTRY_POINT_UNSPECIFIED = 0;
  SKILL_SETTINGS_ENTRY_POINT_COACH_SETTINGS = 1;
  SKILL_SETTINGS_ENTRY_POINT_GAME_REVIEW_SETTINGS = 2;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_START_SETTINGS = 3;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_SETTINGS = 4;
}

message SkillContextExtension {
  optional .chesscom.explanation_engine.v1.Skill skill_id = 1;
  optional string skill_name = 2;
  optional .chesscom.
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08418"></a>
## FND-08418: chesscom.skills.v1.SkillSettingsEntryPoint.SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_START_SETTINGS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_START_SETTINGS = 3;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 567.

```text
L_SETTINGS_ENTRY_POINT_COACH_SETTINGS = 1;
  SKILL_SETTINGS_ENTRY_POINT_GAME_REVIEW_SETTINGS = 2;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_START_SETTINGS = 3;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_SETTINGS = 4;
}

message SkillContextExtension {
  optional .chesscom.explanation_engine.v1.Skill skill_id = 1;
  optional string skill_name = 2;
  optional .chesscom.skills.v1.SkillCategory skill_category = 3;
  optional 
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08419"></a>
## FND-08419: chesscom.skills.v1.SkillSettingsEntryPoint.SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_SETTINGS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_SETTINGS = 4;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 627.

```text
ENTRY_POINT_GAME_REVIEW_SETTINGS = 2;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_START_SETTINGS = 3;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_SETTINGS = 4;
}

message SkillContextExtension {
  optional .chesscom.explanation_engine.v1.Skill skill_id = 1;
  optional string skill_name = 2;
  optional .chesscom.skills.v1.SkillCategory skill_category = 3;
  optional .chesscom.skills.v1.SkillStatus skill_status = 4;
  optional
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08420"></a>
## FND-08420: message declaration: chesscom.skills.v1.SkillContextExtension

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillContextExtension {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 682.

```text
ENTRY_POINT_COACH_GAME_START_SETTINGS = 3;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_SETTINGS = 4;
}

message SkillContextExtension {
  optional .chesscom.explanation_engine.v1.Skill skill_id = 1;
  optional string skill_name = 2;
  optional .chesscom.skills.v1.SkillCategory skill_category = 3;
  optional .chesscom.skills.v1.SkillStatus skill_status = 4;
  optional uint32 points_current = 5;
  optional uint32 points_ne
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08421"></a>
## FND-08421: chesscom.skills.v1.SkillContextExtension.skill_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Skill skill_id = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 716.

```text
NGS = 3;
  SKILL_SETTINGS_ENTRY_POINT_COACH_GAME_SETTINGS = 4;
}

message SkillContextExtension {
  optional .chesscom.explanation_engine.v1.Skill skill_id = 1;
  optional string skill_name = 2;
  optional .chesscom.skills.v1.SkillCategory skill_category = 3;
  optional .chesscom.skills.v1.SkillStatus skill_status = 4;
  optional uint32 points_current = 5;
  optional uint32 points_needed_to_master = 6;
}

message Ski
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08422"></a>
## FND-08422: chesscom.skills.v1.SkillContextExtension.skill_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string skill_name = 2;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 779.

```text
}

message SkillContextExtension {
  optional .chesscom.explanation_engine.v1.Skill skill_id = 1;
  optional string skill_name = 2;
  optional .chesscom.skills.v1.SkillCategory skill_category = 3;
  optional .chesscom.skills.v1.SkillStatus skill_status = 4;
  optional uint32 points_current = 5;
  optional uint32 points_needed_to_master = 6;
}

message SkillSettingsContextExtension {
  optional .chesscom.skills.v1.Ski
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08423"></a>
## FND-08423: chesscom.skills.v1.SkillContextExtension.skill_category = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.skills.v1.SkillCategory skill_category = 3;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 813.

```text

  optional .chesscom.explanation_engine.v1.Skill skill_id = 1;
  optional string skill_name = 2;
  optional .chesscom.skills.v1.SkillCategory skill_category = 3;
  optional .chesscom.skills.v1.SkillStatus skill_status = 4;
  optional uint32 points_current = 5;
  optional uint32 points_needed_to_master = 6;
}

message SkillSettingsContextExtension {
  optional .chesscom.skills.v1.SkillSettingsNewState new_state = 1;

```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08424"></a>
## FND-08424: chesscom.skills.v1.SkillContextExtension.skill_status = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.skills.v1.SkillStatus skill_status = 4;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 878.

```text
 optional string skill_name = 2;
  optional .chesscom.skills.v1.SkillCategory skill_category = 3;
  optional .chesscom.skills.v1.SkillStatus skill_status = 4;
  optional uint32 points_current = 5;
  optional uint32 points_needed_to_master = 6;
}

message SkillSettingsContextExtension {
  optional .chesscom.skills.v1.SkillSettingsNewState new_state = 1;
  optional .chesscom.skills.v1.SkillSettingsEntryPoint entry_poin
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08425"></a>
## FND-08425: chesscom.skills.v1.SkillContextExtension.points_current = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 points_current = 5;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 939.

```text
v1.SkillCategory skill_category = 3;
  optional .chesscom.skills.v1.SkillStatus skill_status = 4;
  optional uint32 points_current = 5;
  optional uint32 points_needed_to_master = 6;
}

message SkillSettingsContextExtension {
  optional .chesscom.skills.v1.SkillSettingsNewState new_state = 1;
  optional .chesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08426"></a>
## FND-08426: chesscom.skills.v1.SkillContextExtension.points_needed_to_master = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 points_needed_to_master = 6;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 977.

```text
 optional .chesscom.skills.v1.SkillStatus skill_status = 4;
  optional uint32 points_current = 5;
  optional uint32 points_needed_to_master = 6;
}

message SkillSettingsContextExtension {
  optional .chesscom.skills.v1.SkillSettingsNewState new_state = 1;
  optional .chesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08427"></a>
## FND-08427: message declaration: chesscom.skills.v1.SkillSettingsContextExtension

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillSettingsContextExtension {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1025.

```text
status = 4;
  optional uint32 points_current = 5;
  optional uint32 points_needed_to_master = 6;
}

message SkillSettingsContextExtension {
  optional .chesscom.skills.v1.SkillSettingsNewState new_state = 1;
  optional .chesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIn
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08428"></a>
## FND-08428: chesscom.skills.v1.SkillSettingsContextExtension.new_state = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.skills.v1.SkillSettingsNewState new_state = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1067.

```text
nt = 5;
  optional uint32 points_needed_to_master = 6;
}

message SkillSettingsContextExtension {
  optional .chesscom.skills.v1.SkillSettingsNewState new_state = 1;
  optional .chesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .che
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08429"></a>
## FND-08429: chesscom.skills.v1.SkillSettingsContextExtension.entry_point = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1135.

```text
illSettingsContextExtension {
  optional .chesscom.skills.v1.SkillSettingsNewState new_state = 1;
  optional .chesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skil
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08430"></a>
## FND-08430: message declaration: chesscom.skills.v1.SkillPointAnimationViewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillPointAnimationViewed {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1208.

```text
sNewState new_state = 1;
  optional .chesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.F
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08431"></a>
## FND-08431: oneof declaration: chesscom.skills.v1.SkillPointAnimationViewed._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1246.

```text
hesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skill
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08432"></a>
## FND-08432: chesscom.skills.v1.SkillPointAnimationViewed.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1264.

```text
SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  on
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08433"></a>
## FND-08433: message declaration: chesscom.skills.v1.SkillPointsIntroScreenViewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillPointsIntroScreenViewed {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1324.

```text
ntAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel fun
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08434"></a>
## FND-08434: oneof declaration: chesscom.skills.v1.SkillPointsIntroScreenViewed._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1246.

```text
hesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skill
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08435"></a>
## FND-08435: chesscom.skills.v1.SkillPointsIntroScreenViewed.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1264.

```text
SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  on
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08436"></a>
## FND-08436: message declaration: chesscom.skills.v1.SkillsButtonClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillsButtonClicked {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1443.

```text
IntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillCategoryViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;

```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08437"></a>
## FND-08437: oneof declaration: chesscom.skills.v1.SkillsButtonClicked._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1246.

```text
hesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skill
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08438"></a>
## FND-08438: chesscom.skills.v1.SkillsButtonClicked.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1264.

```text
SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  on
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08439"></a>
## FND-08439: message declaration: chesscom.skills.v1.SkillsListViewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillsListViewed {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1553.

```text
illsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillCategoryViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillIntroFullScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funne
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08440"></a>
## FND-08440: oneof declaration: chesscom.skills.v1.SkillsListViewed._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1246.

```text
hesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skill
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08441"></a>
## FND-08441: chesscom.skills.v1.SkillsListViewed.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1264.

```text
SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  on
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08442"></a>
## FND-08442: message declaration: chesscom.skills.v1.SkillCategoryViewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillCategoryViewed {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1660.

```text
 SkillsListViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillCategoryViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillIntroFullScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillRowClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08443"></a>
## FND-08443: oneof declaration: chesscom.skills.v1.SkillCategoryViewed._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1246.

```text
hesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skill
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08444"></a>
## FND-08444: chesscom.skills.v1.SkillCategoryViewed.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1264.

```text
SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  on
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08445"></a>
## FND-08445: message declaration: chesscom.skills.v1.SkillIntroFullScreenViewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillIntroFullScreenViewed {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1770.

```text
illCategoryViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillIntroFullScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillRowClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillDefinitionModalViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08446"></a>
## FND-08446: oneof declaration: chesscom.skills.v1.SkillIntroFullScreenViewed._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1246.

```text
hesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skill
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08447"></a>
## FND-08447: chesscom.skills.v1.SkillIntroFullScreenViewed.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1264.

```text
SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  on
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08448"></a>
## FND-08448: message declaration: chesscom.skills.v1.SkillRowClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillRowClicked {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1887.

```text
oFullScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillRowClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillDefinitionModalViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillMasteryModalViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel fu
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08449"></a>
## FND-08449: oneof declaration: chesscom.skills.v1.SkillRowClicked._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1246.

```text
hesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skill
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08450"></a>
## FND-08450: chesscom.skills.v1.SkillRowClicked.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1264.

```text
SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  on
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08451"></a>
## FND-08451: message declaration: chesscom.skills.v1.SkillDefinitionModalViewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillDefinitionModalViewed {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1993.

```text
e SkillRowClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillDefinitionModalViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillMasteryModalViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillUnlockModalViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Fu
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08452"></a>
## FND-08452: oneof declaration: chesscom.skills.v1.SkillDefinitionModalViewed._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1246.

```text
hesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skill
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08453"></a>
## FND-08453: chesscom.skills.v1.SkillDefinitionModalViewed.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1264.

```text
SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  on
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08454"></a>
## FND-08454: message declaration: chesscom.skills.v1.SkillMasteryModalViewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillMasteryModalViewed {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 2110.

```text
nitionModalViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillMasteryModalViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillUnlockModalViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillMasteryShareButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08455"></a>
## FND-08455: oneof declaration: chesscom.skills.v1.SkillMasteryModalViewed._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1246.

```text
hesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skill
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08456"></a>
## FND-08456: chesscom.skills.v1.SkillMasteryModalViewed.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1264.

```text
SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  on
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08457"></a>
## FND-08457: message declaration: chesscom.skills.v1.SkillUnlockModalViewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillUnlockModalViewed {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 2224.

```text
asteryModalViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillUnlockModalViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillMasteryShareButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message AllSkillsMasteredScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.ev
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08458"></a>
## FND-08458: oneof declaration: chesscom.skills.v1.SkillUnlockModalViewed._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1246.

```text
hesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skill
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08459"></a>
## FND-08459: chesscom.skills.v1.SkillUnlockModalViewed.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1264.

```text
SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  on
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08460"></a>
## FND-08460: message declaration: chesscom.skills.v1.SkillMasteryShareButtonClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillMasteryShareButtonClicked {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 2337.

```text
UnlockModalViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillMasteryShareButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message AllSkillsMasteredScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message AllSkillsMasteredShareButtonClicked {
  oneof _funnel {
  .chesscom.pro
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08461"></a>
## FND-08461: oneof declaration: chesscom.skills.v1.SkillMasteryShareButtonClicked._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1246.

```text
hesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skill
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08462"></a>
## FND-08462: chesscom.skills.v1.SkillMasteryShareButtonClicked.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1264.

```text
SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  on
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08463"></a>
## FND-08463: message declaration: chesscom.skills.v1.AllSkillsMasteredScreenViewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AllSkillsMasteredScreenViewed {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 2458.

```text
hareButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message AllSkillsMasteredScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message AllSkillsMasteredShareButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsSettingToggleClicked {
}

```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08464"></a>
## FND-08464: oneof declaration: chesscom.skills.v1.AllSkillsMasteredScreenViewed._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1246.

```text
hesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skill
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08465"></a>
## FND-08465: chesscom.skills.v1.AllSkillsMasteredScreenViewed.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1264.

```text
SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  on
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08466"></a>
## FND-08466: message declaration: chesscom.skills.v1.AllSkillsMasteredShareButtonClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AllSkillsMasteredShareButtonClicked {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 2578.

```text
teredScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message AllSkillsMasteredShareButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsSettingToggleClicked {
}

```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08467"></a>
## FND-08467: oneof declaration: chesscom.skills.v1.AllSkillsMasteredShareButtonClicked._funnel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _funnel {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1246.

```text
hesscom.skills.v1.SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message Skill
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08468"></a>
## FND-08468: chesscom.skills.v1.AllSkillsMasteredShareButtonClicked.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 1264.

```text
SkillSettingsEntryPoint entry_point = 2;
}

message SkillPointAnimationViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillPointsIntroScreenViewed {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsListViewed {
  on
```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08469"></a>
## FND-08469: message declaration: chesscom.skills.v1.SkillsSettingToggleClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillsSettingToggleClicked {

### Evidence

- **SRC-0559** `research/proto/chesscom/skills/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/9fd30b446b2542cc46dafd24bd3e2062fdd39c3dafc9ef3fb514f7d1d5a2ce0a.proto)
  Character offset 2704.

```text
hareButtonClicked {
  oneof _funnel {
  .chesscom.proto_options.events.v1.Funnel funnel = 1;
  }
}

message SkillsSettingToggleClicked {
}

```

**Source references:** SRC-0559, SRC-1530  
**URL references:** None independently associated  
**Related findings:** FND-08405, FND-08406, FND-08407

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08470"></a>
## FND-08470: enum declaration: chesscom.stats.v1.AdvancedStatExampleOutcome

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum AdvancedStatExampleOutcome {

### Evidence

- **SRC-0560** `research/proto/chesscom/stats/v1/advanced_stat_example.proto` — [preserved redacted evidence](../evidence/text/285641f778a6368c055c2c43fb0019f71e97dbb3b996c67bb58cf12a3149de11.proto)
  Character offset 104.

```text
ource: chesscom/stats/v1/advanced_stat_example.proto
// syntax: proto3

package chesscom.stats.v1;

enum AdvancedStatExampleOutcome {
  ADVANCED_STAT_EXAMPLE_OUTCOME_UNSPECIFIED = 0;
  ADVANCED_STAT_EXAMPLE_OUTCOME_GOOD = 1;
  ADVANCED_STAT_EXAMPLE_OUTCOME_BAD = 2;
}

message AdvancedStatExample {
  optional .chesscom.stats.v1.AdvancedStatType stat = 1;
  optional .chesscom.stats.v1.AdvancedStatExampleOutcome outcome
```

**Source references:** SRC-0560, SRC-1531  
**URL references:** None independently associated  
**Related findings:** FND-08471, FND-08472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08471"></a>
## FND-08471: chesscom.stats.v1.AdvancedStatExampleOutcome.ADVANCED_STAT_EXAMPLE_OUTCOME_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_EXAMPLE_OUTCOME_UNSPECIFIED = 0;

### Evidence

- **SRC-0560** `research/proto/chesscom/stats/v1/advanced_stat_example.proto` — [preserved redacted evidence](../evidence/text/285641f778a6368c055c2c43fb0019f71e97dbb3b996c67bb58cf12a3149de11.proto)
  Character offset 140.

```text
at_example.proto
// syntax: proto3

package chesscom.stats.v1;

enum AdvancedStatExampleOutcome {
  ADVANCED_STAT_EXAMPLE_OUTCOME_UNSPECIFIED = 0;
  ADVANCED_STAT_EXAMPLE_OUTCOME_GOOD = 1;
  ADVANCED_STAT_EXAMPLE_OUTCOME_BAD = 2;
}

message AdvancedStatExample {
  optional .chesscom.stats.v1.AdvancedStatType stat = 1;
  optional .chesscom.stats.v1.AdvancedStatExampleOutcome outcome = 2;
  optional int32 ply = 3;
  op
```

**Source references:** SRC-0560, SRC-1531  
**URL references:** None independently associated  
**Related findings:** FND-08470, FND-08472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08472"></a>
## FND-08472: chesscom.stats.v1.AdvancedStatExampleOutcome.ADVANCED_STAT_EXAMPLE_OUTCOME_GOOD = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_EXAMPLE_OUTCOME_GOOD = 1;

### Evidence

- **SRC-0560** `research/proto/chesscom/stats/v1/advanced_stat_example.proto` — [preserved redacted evidence](../evidence/text/285641f778a6368c055c2c43fb0019f71e97dbb3b996c67bb58cf12a3149de11.proto)
  Character offset 189.

```text
com.stats.v1;

enum AdvancedStatExampleOutcome {
  ADVANCED_STAT_EXAMPLE_OUTCOME_UNSPECIFIED = 0;
  ADVANCED_STAT_EXAMPLE_OUTCOME_GOOD = 1;
  ADVANCED_STAT_EXAMPLE_OUTCOME_BAD = 2;
}

message AdvancedStatExample {
  optional .chesscom.stats.v1.AdvancedStatType stat = 1;
  optional .chesscom.stats.v1.AdvancedStatExampleOutcome outcome = 2;
  optional int32 ply = 3;
  optional string san = 4;
}

```

**Source references:** SRC-0560, SRC-1531  
**URL references:** None independently associated  
**Related findings:** FND-08470, FND-08471

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08473"></a>
## FND-08473: chesscom.stats.v1.AdvancedStatExampleOutcome.ADVANCED_STAT_EXAMPLE_OUTCOME_BAD = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ADVANCED_STAT_EXAMPLE_OUTCOME_BAD = 2;

### Evidence

- **SRC-0560** `research/proto/chesscom/stats/v1/advanced_stat_example.proto` — [preserved redacted evidence](../evidence/text/285641f778a6368c055c2c43fb0019f71e97dbb3b996c67bb58cf12a3149de11.proto)
  Character offset 231.

```text
come {
  ADVANCED_STAT_EXAMPLE_OUTCOME_UNSPECIFIED = 0;
  ADVANCED_STAT_EXAMPLE_OUTCOME_GOOD = 1;
  ADVANCED_STAT_EXAMPLE_OUTCOME_BAD = 2;
}

message AdvancedStatExample {
  optional .chesscom.stats.v1.AdvancedStatType stat = 1;
  optional .chesscom.stats.v1.AdvancedStatExampleOutcome outcome = 2;
  optional int32 ply = 3;
  optional string san = 4;
}

```

**Source references:** SRC-0560, SRC-1531  
**URL references:** None independently associated  
**Related findings:** FND-08470, FND-08471, FND-08472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08474"></a>
## FND-08474: message declaration: chesscom.stats.v1.AdvancedStatExample

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AdvancedStatExample {

### Evidence

- **SRC-0560** `research/proto/chesscom/stats/v1/advanced_stat_example.proto` — [preserved redacted evidence](../evidence/text/285641f778a6368c055c2c43fb0019f71e97dbb3b996c67bb58cf12a3149de11.proto)
  Character offset 273.

```text
PECIFIED = 0;
  ADVANCED_STAT_EXAMPLE_OUTCOME_GOOD = 1;
  ADVANCED_STAT_EXAMPLE_OUTCOME_BAD = 2;
}

message AdvancedStatExample {
  optional .chesscom.stats.v1.AdvancedStatType stat = 1;
  optional .chesscom.stats.v1.AdvancedStatExampleOutcome outcome = 2;
  optional int32 ply = 3;
  optional string san = 4;
}

```

**Source references:** SRC-0560, SRC-1531  
**URL references:** None independently associated  
**Related findings:** FND-08470, FND-08471, FND-08472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
