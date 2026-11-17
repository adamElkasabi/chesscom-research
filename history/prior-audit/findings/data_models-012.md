# data_models — findings 1101–1200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-01375"></a>
## FND-01375: chesscom.coaches.v2.GetCurrentCoachRequest.device_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string device_id = 1;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1275.

```text
tCoachRequest {
  oneof _locale_override {
  string locale_override = 2;
  }
  oneof _device_id {
  string device_id = 1;
  }
  oneof _bucketing_id {
  string bucketing_id = 3;
  }
  oneof _with_celebrity_coaches {
  bool with_celebrity_coaches = 4;
  }
}

message GetCurrentCoachResponse {
  optional .chesscom.coaches.v2.Coach current_coach = 1;
}

message GetCoachQuotaRequest {
}

message GetCoachQuotaResponse {
  o
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01376"></a>
## FND-01376: oneof declaration: chesscom.coaches.v2.GetCurrentCoachRequest._bucketing_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _bucketing_id {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1303.

```text
ale_override {
  string locale_override = 2;
  }
  oneof _device_id {
  string device_id = 1;
  }
  oneof _bucketing_id {
  string bucketing_id = 3;
  }
  oneof _with_celebrity_coaches {
  bool with_celebrity_coaches = 4;
  }
}

message GetCurrentCoachResponse {
  optional .chesscom.coaches.v2.Coach current_coach = 1;
}

message GetCoachQuotaRequest {
}

message GetCoachQuotaResponse {
  optional int32 remaining = 1;
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01377"></a>
## FND-01377: chesscom.coaches.v2.GetCurrentCoachRequest.bucketing_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string bucketing_id = 3;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1327.

```text
locale_override = 2;
  }
  oneof _device_id {
  string device_id = 1;
  }
  oneof _bucketing_id {
  string bucketing_id = 3;
  }
  oneof _with_celebrity_coaches {
  bool with_celebrity_coaches = 4;
  }
}

message GetCurrentCoachResponse {
  optional .chesscom.coaches.v2.Coach current_coach = 1;
}

message GetCoachQuotaRequest {
}

message GetCoachQuotaResponse {
  optional int32 remaining = 1;
}

message StartedGameA
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01378"></a>
## FND-01378: oneof declaration: chesscom.coaches.v2.GetCurrentCoachRequest._with_celebrity_coaches

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _with_celebrity_coaches {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 186.

```text
es.v2;

message ListCoachesRequest {
  oneof _locale_override {
  string locale_override = 1;
  }
  oneof _with_celebrity_coaches {
  bool with_celebrity_coaches = 2;
  }
}

message ListCoachesResponse {
  repeated .chesscom.coaches.v2.CoachCategory coach_categories = 1;
}

message ListOnboardingCoachesRequest {
  oneof _locale_override {
  string locale_override = 1;
  }
  oneof _with_celebrity_coaches {
  bool with
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01379"></a>
## FND-01379: chesscom.coaches.v2.GetCurrentCoachRequest.with_celebrity_coaches = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool with_celebrity_coaches = 4;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1392.

```text
= 1;
  }
  oneof _bucketing_id {
  string bucketing_id = 3;
  }
  oneof _with_celebrity_coaches {
  bool with_celebrity_coaches = 4;
  }
}

message GetCurrentCoachResponse {
  optional .chesscom.coaches.v2.Coach current_coach = 1;
}

message GetCoachQuotaRequest {
}

message GetCoachQuotaResponse {
  optional int32 remaining = 1;
}

message StartedGameAgainstCoachRequest {
  optional string game_token = 2;
}

message
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01380"></a>
## FND-01380: message declaration: chesscom.coaches.v2.GetCurrentCoachResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCurrentCoachResponse {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1432.

```text
g bucketing_id = 3;
  }
  oneof _with_celebrity_coaches {
  bool with_celebrity_coaches = 4;
  }
}

message GetCurrentCoachResponse {
  optional .chesscom.coaches.v2.Coach current_coach = 1;
}

message GetCoachQuotaRequest {
}

message GetCoachQuotaResponse {
  optional int32 remaining = 1;
}

message StartedGameAgainstCoachRequest {
  optional string game_token = 2;
}

message StartedGameAgainstCoachResponse {
}

me
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01381"></a>
## FND-01381: chesscom.coaches.v2.GetCurrentCoachResponse.current_coach = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.Coach current_coach = 1;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1100.

```text
ing locale_override = 2;
  }
  optional string coach_id = 1;
}

message SetCurrentCoachResponse {
  optional .chesscom.coaches.v2.Coach current_coach = 1;
}

message GetCurrentCoachRequest {
  oneof _locale_override {
  string locale_override = 2;
  }
  oneof _device_id {
  string device_id = 1;
  }
  oneof _bucketing_id {
  string bucketing_id = 3;
  }
  oneof _with_celebrity_coaches {
  bool with_celebrity_coaches 
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01382"></a>
## FND-01382: message declaration: chesscom.coaches.v2.GetCoachQuotaRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCoachQuotaRequest {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1526.

```text
 }
}

message GetCurrentCoachResponse {
  optional .chesscom.coaches.v2.Coach current_coach = 1;
}

message GetCoachQuotaRequest {
}

message GetCoachQuotaResponse {
  optional int32 remaining = 1;
}

message StartedGameAgainstCoachRequest {
  optional string game_token = 2;
}

message StartedGameAgainstCoachResponse {
}

message SetSettingsResponse {
}

message SetSettingsRequest {
  oneof _enable_motivational {
  b
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01383"></a>
## FND-01383: message declaration: chesscom.coaches.v2.GetCoachQuotaResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCoachQuotaResponse {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1560.

```text
nse {
  optional .chesscom.coaches.v2.Coach current_coach = 1;
}

message GetCoachQuotaRequest {
}

message GetCoachQuotaResponse {
  optional int32 remaining = 1;
}

message StartedGameAgainstCoachRequest {
  optional string game_token = 2;
}

message StartedGameAgainstCoachResponse {
}

message SetSettingsResponse {
}

message SetSettingsRequest {
  oneof _enable_motivational {
  bool enable_motivational = 1;
  }
 
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01384"></a>
## FND-01384: chesscom.coaches.v2.GetCoachQuotaResponse.remaining = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 remaining = 1;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1594.

```text
.v2.Coach current_coach = 1;
}

message GetCoachQuotaRequest {
}

message GetCoachQuotaResponse {
  optional int32 remaining = 1;
}

message StartedGameAgainstCoachRequest {
  optional string game_token = 2;
}

message StartedGameAgainstCoachResponse {
}

message SetSettingsResponse {
}

message SetSettingsRequest {
  oneof _enable_motivational {
  bool enable_motivational = 1;
  }
  oneof _enable_voice {
  bool enab
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01385"></a>
## FND-01385: message declaration: chesscom.coaches.v2.StartedGameAgainstCoachRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StartedGameAgainstCoachRequest {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1627.

```text
essage GetCoachQuotaRequest {
}

message GetCoachQuotaResponse {
  optional int32 remaining = 1;
}

message StartedGameAgainstCoachRequest {
  optional string game_token = 2;
}

message StartedGameAgainstCoachResponse {
}

message SetSettingsResponse {
}

message SetSettingsRequest {
  oneof _enable_motivational {
  bool enable_motivational = 1;
  }
  oneof _enable_voice {
  bool enable_voice = 2;
  }
  oneof _enable
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01386"></a>
## FND-01386: chesscom.coaches.v2.StartedGameAgainstCoachRequest.game_token = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_token = 2;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1670.

```text
tCoachQuotaResponse {
  optional int32 remaining = 1;
}

message StartedGameAgainstCoachRequest {
  optional string game_token = 2;
}

message StartedGameAgainstCoachResponse {
}

message SetSettingsResponse {
}

message SetSettingsRequest {
  oneof _enable_motivational {
  bool enable_motivational = 1;
  }
  oneof _enable_voice {
  bool enable_voice = 2;
  }
  oneof _enable_reminders {
  bool enable_reminders = 3;
 
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01387"></a>
## FND-01387: message declaration: chesscom.coaches.v2.StartedGameAgainstCoachResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StartedGameAgainstCoachResponse {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1705.

```text
t32 remaining = 1;
}

message StartedGameAgainstCoachRequest {
  optional string game_token = 2;
}

message StartedGameAgainstCoachResponse {
}

message SetSettingsResponse {
}

message SetSettingsRequest {
  oneof _enable_motivational {
  bool enable_motivational = 1;
  }
  oneof _enable_voice {
  bool enable_voice = 2;
  }
  oneof _enable_reminders {
  bool enable_reminders = 3;
  }
  oneof _puzzle_goals {
  bool p
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01388"></a>
## FND-01388: message declaration: chesscom.coaches.v2.SetSettingsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetSettingsResponse {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1750.

```text
nstCoachRequest {
  optional string game_token = 2;
}

message StartedGameAgainstCoachResponse {
}

message SetSettingsResponse {
}

message SetSettingsRequest {
  oneof _enable_motivational {
  bool enable_motivational = 1;
  }
  oneof _enable_voice {
  bool enable_voice = 2;
  }
  oneof _enable_reminders {
  bool enable_reminders = 3;
  }
  oneof _puzzle_goals {
  bool puzzle_goals = 4;
  }
  oneof _puzzle_mistake_
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01389"></a>
## FND-01389: message declaration: chesscom.coaches.v2.SetSettingsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetSettingsRequest {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1783.

```text
ng game_token = 2;
}

message StartedGameAgainstCoachResponse {
}

message SetSettingsResponse {
}

message SetSettingsRequest {
  oneof _enable_motivational {
  bool enable_motivational = 1;
  }
  oneof _enable_voice {
  bool enable_voice = 2;
  }
  oneof _enable_reminders {
  bool enable_reminders = 3;
  }
  oneof _puzzle_goals {
  bool puzzle_goals = 4;
  }
  oneof _puzzle_mistake_feedback {
  bool puzzle_mistake_
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01390"></a>
## FND-01390: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._enable_motivational

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _enable_motivational {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1814.

```text
tartedGameAgainstCoachResponse {
}

message SetSettingsResponse {
}

message SetSettingsRequest {
  oneof _enable_motivational {
  bool enable_motivational = 1;
  }
  oneof _enable_voice {
  bool enable_voice = 2;
  }
  oneof _enable_reminders {
  bool enable_reminders = 3;
  }
  oneof _puzzle_goals {
  bool puzzle_goals = 4;
  }
  oneof _puzzle_mistake_feedback {
  bool puzzle_mistake_feedback = 5;
  }
  oneof _puzz
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01391"></a>
## FND-01391: chesscom.coaches.v2.SetSettingsRequest.enable_motivational = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool enable_motivational = 1;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1845.

```text
{
}

message SetSettingsResponse {
}

message SetSettingsRequest {
  oneof _enable_motivational {
  bool enable_motivational = 1;
  }
  oneof _enable_voice {
  bool enable_voice = 2;
  }
  oneof _enable_reminders {
  bool enable_reminders = 3;
  }
  oneof _puzzle_goals {
  bool puzzle_goals = 4;
  }
  oneof _puzzle_mistake_feedback {
  bool puzzle_mistake_feedback = 5;
  }
  oneof _puzzle_hints {
  bool puzzle_hints 
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01392"></a>
## FND-01392: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._enable_voice

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _enable_voice {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1881.

```text


message SetSettingsRequest {
  oneof _enable_motivational {
  bool enable_motivational = 1;
  }
  oneof _enable_voice {
  bool enable_voice = 2;
  }
  oneof _enable_reminders {
  bool enable_reminders = 3;
  }
  oneof _puzzle_goals {
  bool puzzle_goals = 4;
  }
  oneof _puzzle_mistake_feedback {
  bool puzzle_mistake_feedback = 5;
  }
  oneof _puzzle_hints {
  bool puzzle_hints = 6;
  }
  oneof _voice_speed {
  .c
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01393"></a>
## FND-01393: chesscom.coaches.v2.SetSettingsRequest.enable_voice = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool enable_voice = 2;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1905.

```text
uest {
  oneof _enable_motivational {
  bool enable_motivational = 1;
  }
  oneof _enable_voice {
  bool enable_voice = 2;
  }
  oneof _enable_reminders {
  bool enable_reminders = 3;
  }
  oneof _puzzle_goals {
  bool puzzle_goals = 4;
  }
  oneof _puzzle_mistake_feedback {
  bool puzzle_mistake_feedback = 5;
  }
  oneof _puzzle_hints {
  bool puzzle_hints = 6;
  }
  oneof _voice_speed {
  .chesscom.coaches.v2.Coach
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01394"></a>
## FND-01394: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._enable_reminders

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _enable_reminders {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1934.

```text
tional {
  bool enable_motivational = 1;
  }
  oneof _enable_voice {
  bool enable_voice = 2;
  }
  oneof _enable_reminders {
  bool enable_reminders = 3;
  }
  oneof _puzzle_goals {
  bool puzzle_goals = 4;
  }
  oneof _puzzle_mistake_feedback {
  bool puzzle_mistake_feedback = 5;
  }
  oneof _puzzle_hints {
  bool puzzle_hints = 6;
  }
  oneof _voice_speed {
  .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
 
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01395"></a>
## FND-01395: chesscom.coaches.v2.SetSettingsRequest.enable_reminders = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool enable_reminders = 3;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1962.

```text
ational = 1;
  }
  oneof _enable_voice {
  bool enable_voice = 2;
  }
  oneof _enable_reminders {
  bool enable_reminders = 3;
  }
  oneof _puzzle_goals {
  bool puzzle_goals = 4;
  }
  oneof _puzzle_mistake_feedback {
  bool puzzle_mistake_feedback = 5;
  }
  oneof _puzzle_hints {
  bool puzzle_hints = 6;
  }
  oneof _voice_speed {
  .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  }
  oneof _show_coach_avata
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01396"></a>
## FND-01396: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._puzzle_goals

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzle_goals {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 1995.

```text
voice {
  bool enable_voice = 2;
  }
  oneof _enable_reminders {
  bool enable_reminders = 3;
  }
  oneof _puzzle_goals {
  bool puzzle_goals = 4;
  }
  oneof _puzzle_mistake_feedback {
  bool puzzle_mistake_feedback = 5;
  }
  oneof _puzzle_hints {
  bool puzzle_hints = 6;
  }
  oneof _voice_speed {
  .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  }
  oneof _show_coach_avatar_game_review {
  bool show_coach
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01397"></a>
## FND-01397: chesscom.coaches.v2.SetSettingsRequest.puzzle_goals = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool puzzle_goals = 4;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2019.

```text
ice = 2;
  }
  oneof _enable_reminders {
  bool enable_reminders = 3;
  }
  oneof _puzzle_goals {
  bool puzzle_goals = 4;
  }
  oneof _puzzle_mistake_feedback {
  bool puzzle_mistake_feedback = 5;
  }
  oneof _puzzle_hints {
  bool puzzle_hints = 6;
  }
  oneof _voice_speed {
  .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  }
  oneof _show_coach_avatar_game_review {
  bool show_coach_avatar_game_review = 8;
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01398"></a>
## FND-01398: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._puzzle_mistake_feedback

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzle_mistake_feedback {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2048.

```text
reminders {
  bool enable_reminders = 3;
  }
  oneof _puzzle_goals {
  bool puzzle_goals = 4;
  }
  oneof _puzzle_mistake_feedback {
  bool puzzle_mistake_feedback = 5;
  }
  oneof _puzzle_hints {
  bool puzzle_hints = 6;
  }
  oneof _voice_speed {
  .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  }
  oneof _show_coach_avatar_game_review {
  bool show_coach_avatar_game_review = 8;
  }
  oneof _enable_auto_sav
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01399"></a>
## FND-01399: chesscom.coaches.v2.SetSettingsRequest.puzzle_mistake_feedback = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool puzzle_mistake_feedback = 5;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2083.

```text
 = 3;
  }
  oneof _puzzle_goals {
  bool puzzle_goals = 4;
  }
  oneof _puzzle_mistake_feedback {
  bool puzzle_mistake_feedback = 5;
  }
  oneof _puzzle_hints {
  bool puzzle_hints = 6;
  }
  oneof _voice_speed {
  .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  }
  oneof _show_coach_avatar_game_review {
  bool show_coach_avatar_game_review = 8;
  }
  oneof _enable_auto_save_coach_games {
  bool enable_auto_
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01400"></a>
## FND-01400: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._puzzle_hints

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzle_hints {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2123.

```text
 puzzle_goals = 4;
  }
  oneof _puzzle_mistake_feedback {
  bool puzzle_mistake_feedback = 5;
  }
  oneof _puzzle_hints {
  bool puzzle_hints = 6;
  }
  oneof _voice_speed {
  .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  }
  oneof _show_coach_avatar_game_review {
  bool show_coach_avatar_game_review = 8;
  }
  oneof _enable_auto_save_coach_games {
  bool enable_auto_save_coach_games = 9;
  }
  oneof _enabl
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01401"></a>
## FND-01401: chesscom.coaches.v2.SetSettingsRequest.puzzle_hints = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool puzzle_hints = 6;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2147.

```text
 oneof _puzzle_mistake_feedback {
  bool puzzle_mistake_feedback = 5;
  }
  oneof _puzzle_hints {
  bool puzzle_hints = 6;
  }
  oneof _voice_speed {
  .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  }
  oneof _show_coach_avatar_game_review {
  bool show_coach_avatar_game_review = 8;
  }
  oneof _enable_auto_save_coach_games {
  bool enable_auto_save_coach_games = 9;
  }
  oneof _enable_evaluation_bar {
  boo
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01402"></a>
## FND-01402: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._voice_speed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _voice_speed {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2176.

```text
ck {
  bool puzzle_mistake_feedback = 5;
  }
  oneof _puzzle_hints {
  bool puzzle_hints = 6;
  }
  oneof _voice_speed {
  .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  }
  oneof _show_coach_avatar_game_review {
  bool show_coach_avatar_game_review = 8;
  }
  oneof _enable_auto_save_coach_games {
  bool enable_auto_save_coach_games = 9;
  }
  oneof _enable_evaluation_bar {
  bool enable_evaluation_bar = 10;
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01403"></a>
## FND-01403: chesscom.coaches.v2.SetSettingsRequest.voice_speed = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2199.

```text
ake_feedback = 5;
  }
  oneof _puzzle_hints {
  bool puzzle_hints = 6;
  }
  oneof _voice_speed {
  .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  }
  oneof _show_coach_avatar_game_review {
  bool show_coach_avatar_game_review = 8;
  }
  oneof _enable_auto_save_coach_games {
  bool enable_auto_save_coach_games = 9;
  }
  oneof _enable_evaluation_bar {
  bool enable_evaluation_bar = 10;
  }
  oneof _enable_su
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01404"></a>
## FND-01404: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._show_coach_avatar_game_review

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _show_coach_avatar_game_review {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2259.

```text
hints = 6;
  }
  oneof _voice_speed {
  .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  }
  oneof _show_coach_avatar_game_review {
  bool show_coach_avatar_game_review = 8;
  }
  oneof _enable_auto_save_coach_games {
  bool enable_auto_save_coach_games = 9;
  }
  oneof _enable_evaluation_bar {
  bool enable_evaluation_bar = 10;
  }
  oneof _enable_suggestion_arrows {
  bool enable_suggestion_arrows = 11;
  }

```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01405"></a>
## FND-01405: chesscom.coaches.v2.SetSettingsRequest.show_coach_avatar_game_review = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool show_coach_avatar_game_review = 8;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2300.

```text
chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  }
  oneof _show_coach_avatar_game_review {
  bool show_coach_avatar_game_review = 8;
  }
  oneof _enable_auto_save_coach_games {
  bool enable_auto_save_coach_games = 9;
  }
  oneof _enable_evaluation_bar {
  bool enable_evaluation_bar = 10;
  }
  oneof _enable_suggestion_arrows {
  bool enable_suggestion_arrows = 11;
  }
  oneof _enable_threat_arrows {
  bool en
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01406"></a>
## FND-01406: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._enable_auto_save_coach_games

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _enable_auto_save_coach_games {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2346.

```text
d = 7;
  }
  oneof _show_coach_avatar_game_review {
  bool show_coach_avatar_game_review = 8;
  }
  oneof _enable_auto_save_coach_games {
  bool enable_auto_save_coach_games = 9;
  }
  oneof _enable_evaluation_bar {
  bool enable_evaluation_bar = 10;
  }
  oneof _enable_suggestion_arrows {
  bool enable_suggestion_arrows = 11;
  }
  oneof _enable_threat_arrows {
  bool enable_threat_arrows = 12;
  }
  oneof _enable_s
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01407"></a>
## FND-01407: chesscom.coaches.v2.SetSettingsRequest.enable_auto_save_coach_games = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool enable_auto_save_coach_games = 9;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2386.

```text
me_review {
  bool show_coach_avatar_game_review = 8;
  }
  oneof _enable_auto_save_coach_games {
  bool enable_auto_save_coach_games = 9;
  }
  oneof _enable_evaluation_bar {
  bool enable_evaluation_bar = 10;
  }
  oneof _enable_suggestion_arrows {
  bool enable_suggestion_arrows = 11;
  }
  oneof _enable_threat_arrows {
  bool enable_threat_arrows = 12;
  }
  oneof _enable_skills {
  bool enable_skills = 13;
  }
 
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01408"></a>
## FND-01408: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._enable_evaluation_bar

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _enable_evaluation_bar {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2431.

```text
iew = 8;
  }
  oneof _enable_auto_save_coach_games {
  bool enable_auto_save_coach_games = 9;
  }
  oneof _enable_evaluation_bar {
  bool enable_evaluation_bar = 10;
  }
  oneof _enable_suggestion_arrows {
  bool enable_suggestion_arrows = 11;
  }
  oneof _enable_threat_arrows {
  bool enable_threat_arrows = 12;
  }
  oneof _enable_skills {
  bool enable_skills = 13;
  }
  oneof _enable_teach_legal_moves {
  bool ena
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01409"></a>
## FND-01409: chesscom.coaches.v2.SetSettingsRequest.enable_evaluation_bar = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool enable_evaluation_bar = 10;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2464.

```text
_save_coach_games {
  bool enable_auto_save_coach_games = 9;
  }
  oneof _enable_evaluation_bar {
  bool enable_evaluation_bar = 10;
  }
  oneof _enable_suggestion_arrows {
  bool enable_suggestion_arrows = 11;
  }
  oneof _enable_threat_arrows {
  bool enable_threat_arrows = 12;
  }
  oneof _enable_skills {
  bool enable_skills = 13;
  }
  oneof _enable_teach_legal_moves {
  bool enable_teach_legal_moves = 14;
  }
}
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01410"></a>
## FND-01410: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._enable_suggestion_arrows

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _enable_suggestion_arrows {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2503.

```text
save_coach_games = 9;
  }
  oneof _enable_evaluation_bar {
  bool enable_evaluation_bar = 10;
  }
  oneof _enable_suggestion_arrows {
  bool enable_suggestion_arrows = 11;
  }
  oneof _enable_threat_arrows {
  bool enable_threat_arrows = 12;
  }
  oneof _enable_skills {
  bool enable_skills = 13;
  }
  oneof _enable_teach_legal_moves {
  bool enable_teach_legal_moves = 14;
  }
}

message GetSettingsRequest {
}

messa
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01411"></a>
## FND-01411: chesscom.coaches.v2.SetSettingsRequest.enable_suggestion_arrows = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool enable_suggestion_arrows = 11;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2539.

```text
nable_evaluation_bar {
  bool enable_evaluation_bar = 10;
  }
  oneof _enable_suggestion_arrows {
  bool enable_suggestion_arrows = 11;
  }
  oneof _enable_threat_arrows {
  bool enable_threat_arrows = 12;
  }
  oneof _enable_skills {
  bool enable_skills = 13;
  }
  oneof _enable_teach_legal_moves {
  bool enable_teach_legal_moves = 14;
  }
}

message GetSettingsRequest {
}

message GetSettingsResponse {
  optional 
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01412"></a>
## FND-01412: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._enable_threat_arrows

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _enable_threat_arrows {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2581.

```text
ation_bar = 10;
  }
  oneof _enable_suggestion_arrows {
  bool enable_suggestion_arrows = 11;
  }
  oneof _enable_threat_arrows {
  bool enable_threat_arrows = 12;
  }
  oneof _enable_skills {
  bool enable_skills = 13;
  }
  oneof _enable_teach_legal_moves {
  bool enable_teach_legal_moves = 14;
  }
}

message GetSettingsRequest {
}

message GetSettingsResponse {
  optional bool enable_motivational = 1;
  optional b
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01413"></a>
## FND-01413: chesscom.coaches.v2.SetSettingsRequest.enable_threat_arrows = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool enable_threat_arrows = 12;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2613.

```text
ble_suggestion_arrows {
  bool enable_suggestion_arrows = 11;
  }
  oneof _enable_threat_arrows {
  bool enable_threat_arrows = 12;
  }
  oneof _enable_skills {
  bool enable_skills = 13;
  }
  oneof _enable_teach_legal_moves {
  bool enable_teach_legal_moves = 14;
  }
}

message GetSettingsRequest {
}

message GetSettingsResponse {
  optional bool enable_motivational = 1;
  optional bool enable_voice = 2;
  optional
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01414"></a>
## FND-01414: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._enable_skills

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _enable_skills {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2651.

```text
suggestion_arrows = 11;
  }
  oneof _enable_threat_arrows {
  bool enable_threat_arrows = 12;
  }
  oneof _enable_skills {
  bool enable_skills = 13;
  }
  oneof _enable_teach_legal_moves {
  bool enable_teach_legal_moves = 14;
  }
}

message GetSettingsRequest {
}

message GetSettingsResponse {
  optional bool enable_motivational = 1;
  optional bool enable_voice = 2;
  optional bool enable_reminders = 3;
  optional
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01415"></a>
## FND-01415: chesscom.coaches.v2.SetSettingsRequest.enable_skills = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool enable_skills = 13;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2676.

```text
 }
  oneof _enable_threat_arrows {
  bool enable_threat_arrows = 12;
  }
  oneof _enable_skills {
  bool enable_skills = 13;
  }
  oneof _enable_teach_legal_moves {
  bool enable_teach_legal_moves = 14;
  }
}

message GetSettingsRequest {
}

message GetSettingsResponse {
  optional bool enable_motivational = 1;
  optional bool enable_voice = 2;
  optional bool enable_reminders = 3;
  optional bool enable_puzzle_goals
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01416"></a>
## FND-01416: oneof declaration: chesscom.coaches.v2.SetSettingsRequest._enable_teach_legal_moves

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _enable_teach_legal_moves {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2707.

```text
s {
  bool enable_threat_arrows = 12;
  }
  oneof _enable_skills {
  bool enable_skills = 13;
  }
  oneof _enable_teach_legal_moves {
  bool enable_teach_legal_moves = 14;
  }
}

message GetSettingsRequest {
}

message GetSettingsResponse {
  optional bool enable_motivational = 1;
  optional bool enable_voice = 2;
  optional bool enable_reminders = 3;
  optional bool enable_puzzle_goals = 4;
  optional bool enable_pu
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01417"></a>
## FND-01417: chesscom.coaches.v2.SetSettingsRequest.enable_teach_legal_moves = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool enable_teach_legal_moves = 14;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2743.

```text
;
  }
  oneof _enable_skills {
  bool enable_skills = 13;
  }
  oneof _enable_teach_legal_moves {
  bool enable_teach_legal_moves = 14;
  }
}

message GetSettingsRequest {
}

message GetSettingsResponse {
  optional bool enable_motivational = 1;
  optional bool enable_voice = 2;
  optional bool enable_reminders = 3;
  optional bool enable_puzzle_goals = 4;
  optional bool enable_puzzle_mistake_feedback = 5;
  optiona
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01418"></a>
## FND-01418: message declaration: chesscom.coaches.v2.GetSettingsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSettingsRequest {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2786.

```text
e_skills = 13;
  }
  oneof _enable_teach_legal_moves {
  bool enable_teach_legal_moves = 14;
  }
}

message GetSettingsRequest {
}

message GetSettingsResponse {
  optional bool enable_motivational = 1;
  optional bool enable_voice = 2;
  optional bool enable_reminders = 3;
  optional bool enable_puzzle_goals = 4;
  optional bool enable_puzzle_mistake_feedback = 5;
  optional bool enable_puzzle_hints = 6;
  optional 
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01419"></a>
## FND-01419: message declaration: chesscom.coaches.v2.GetSettingsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSettingsResponse {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2818.

```text
le_teach_legal_moves {
  bool enable_teach_legal_moves = 14;
  }
}

message GetSettingsRequest {
}

message GetSettingsResponse {
  optional bool enable_motivational = 1;
  optional bool enable_voice = 2;
  optional bool enable_reminders = 3;
  optional bool enable_puzzle_goals = 4;
  optional bool enable_puzzle_mistake_feedback = 5;
  optional bool enable_puzzle_hints = 6;
  optional .chesscom.coaches.v2.CoachVoiceS
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01420"></a>
## FND-01420: chesscom.coaches.v2.GetSettingsResponse.enable_motivational = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_motivational = 1;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2850.

```text
able_teach_legal_moves = 14;
  }
}

message GetSettingsRequest {
}

message GetSettingsResponse {
  optional bool enable_motivational = 1;
  optional bool enable_voice = 2;
  optional bool enable_reminders = 3;
  optional bool enable_puzzle_goals = 4;
  optional bool enable_puzzle_mistake_feedback = 5;
  optional bool enable_puzzle_hints = 6;
  optional .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  optional
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01421"></a>
## FND-01421: chesscom.coaches.v2.GetSettingsResponse.enable_voice = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_voice = 2;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2891.

```text
ge GetSettingsRequest {
}

message GetSettingsResponse {
  optional bool enable_motivational = 1;
  optional bool enable_voice = 2;
  optional bool enable_reminders = 3;
  optional bool enable_puzzle_goals = 4;
  optional bool enable_puzzle_mistake_feedback = 5;
  optional bool enable_puzzle_hints = 6;
  optional .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  optional bool show_coach_avatar_game_review = 8;

```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01422"></a>
## FND-01422: chesscom.coaches.v2.GetSettingsResponse.enable_reminders = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_reminders = 3;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2925.

```text
 GetSettingsResponse {
  optional bool enable_motivational = 1;
  optional bool enable_voice = 2;
  optional bool enable_reminders = 3;
  optional bool enable_puzzle_goals = 4;
  optional bool enable_puzzle_mistake_feedback = 5;
  optional bool enable_puzzle_hints = 6;
  optional .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  optional bool show_coach_avatar_game_review = 8;
  optional bool enable_auto_save_c
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01423"></a>
## FND-01423: chesscom.coaches.v2.GetSettingsResponse.enable_puzzle_goals = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_puzzle_goals = 4;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 2963.

```text
 enable_motivational = 1;
  optional bool enable_voice = 2;
  optional bool enable_reminders = 3;
  optional bool enable_puzzle_goals = 4;
  optional bool enable_puzzle_mistake_feedback = 5;
  optional bool enable_puzzle_hints = 6;
  optional .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  optional bool show_coach_avatar_game_review = 8;
  optional bool enable_auto_save_coach_games = 9;
  optional bool enable
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01424"></a>
## FND-01424: chesscom.coaches.v2.GetSettingsResponse.enable_puzzle_mistake_feedback = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_puzzle_mistake_feedback = 5;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3004.

```text
 enable_voice = 2;
  optional bool enable_reminders = 3;
  optional bool enable_puzzle_goals = 4;
  optional bool enable_puzzle_mistake_feedback = 5;
  optional bool enable_puzzle_hints = 6;
  optional .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  optional bool show_coach_avatar_game_review = 8;
  optional bool enable_auto_save_coach_games = 9;
  optional bool enable_evaluation_bar = 10;
  optional bool ena
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01425"></a>
## FND-01425: chesscom.coaches.v2.GetSettingsResponse.enable_puzzle_hints = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_puzzle_hints = 6;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3056.

```text
= 3;
  optional bool enable_puzzle_goals = 4;
  optional bool enable_puzzle_mistake_feedback = 5;
  optional bool enable_puzzle_hints = 6;
  optional .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  optional bool show_coach_avatar_game_review = 8;
  optional bool enable_auto_save_coach_games = 9;
  optional bool enable_evaluation_bar = 10;
  optional bool enable_suggestion_arrows = 11;
  optional bool enable_t
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01426"></a>
## FND-01426: chesscom.coaches.v2.GetSettingsResponse.voice_speed = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3097.

```text
= 4;
  optional bool enable_puzzle_mistake_feedback = 5;
  optional bool enable_puzzle_hints = 6;
  optional .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  optional bool show_coach_avatar_game_review = 8;
  optional bool enable_auto_save_coach_games = 9;
  optional bool enable_evaluation_bar = 10;
  optional bool enable_suggestion_arrows = 11;
  optional bool enable_threat_arrows = 12;
  optional bool enable
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01427"></a>
## FND-01427: chesscom.coaches.v2.GetSettingsResponse.show_coach_avatar_game_review = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool show_coach_avatar_game_review = 8;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3162.

```text
al bool enable_puzzle_hints = 6;
  optional .chesscom.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  optional bool show_coach_avatar_game_review = 8;
  optional bool enable_auto_save_coach_games = 9;
  optional bool enable_evaluation_bar = 10;
  optional bool enable_suggestion_arrows = 11;
  optional bool enable_threat_arrows = 12;
  optional bool enable_skills = 13;
  optional bool enable_teach_legal_moves = 14;
}

m
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01428"></a>
## FND-01428: chesscom.coaches.v2.GetSettingsResponse.enable_auto_save_coach_games = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_auto_save_coach_games = 9;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3213.

```text
om.coaches.v2.CoachVoiceSpeed voice_speed = 7;
  optional bool show_coach_avatar_game_review = 8;
  optional bool enable_auto_save_coach_games = 9;
  optional bool enable_evaluation_bar = 10;
  optional bool enable_suggestion_arrows = 11;
  optional bool enable_threat_arrows = 12;
  optional bool enable_skills = 13;
  optional bool enable_teach_legal_moves = 14;
}

message SaveCoachGameRequest {
  oneof _game_uuid {

```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01429"></a>
## FND-01429: chesscom.coaches.v2.GetSettingsResponse.enable_evaluation_bar = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_evaluation_bar = 10;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3263.

```text
ptional bool show_coach_avatar_game_review = 8;
  optional bool enable_auto_save_coach_games = 9;
  optional bool enable_evaluation_bar = 10;
  optional bool enable_suggestion_arrows = 11;
  optional bool enable_threat_arrows = 12;
  optional bool enable_skills = 13;
  optional bool enable_teach_legal_moves = 14;
}

message SaveCoachGameRequest {
  oneof _game_uuid {
  string game_uuid = 12;
  }
  optional .chesscom.
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01430"></a>
## FND-01430: chesscom.coaches.v2.GetSettingsResponse.enable_suggestion_arrows = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_suggestion_arrows = 11;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3307.

```text
 8;
  optional bool enable_auto_save_coach_games = 9;
  optional bool enable_evaluation_bar = 10;
  optional bool enable_suggestion_arrows = 11;
  optional bool enable_threat_arrows = 12;
  optional bool enable_skills = 13;
  optional bool enable_teach_legal_moves = 14;
}

message SaveCoachGameRequest {
  oneof _game_uuid {
  string game_uuid = 12;
  }
  optional .chesscom.computer.v1.UserColor user_position = 1;
  o
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01431"></a>
## FND-01431: chesscom.coaches.v2.GetSettingsResponse.enable_threat_arrows = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_threat_arrows = 12;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3354.

```text
s = 9;
  optional bool enable_evaluation_bar = 10;
  optional bool enable_suggestion_arrows = 11;
  optional bool enable_threat_arrows = 12;
  optional bool enable_skills = 13;
  optional bool enable_teach_legal_moves = 14;
}

message SaveCoachGameRequest {
  oneof _game_uuid {
  string game_uuid = 12;
  }
  optional .chesscom.computer.v1.UserColor user_position = 1;
  optional string coach_id = 2;
  optional int32 c
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01432"></a>
## FND-01432: chesscom.coaches.v2.GetSettingsResponse.enable_skills = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_skills = 13;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3397.

```text
r = 10;
  optional bool enable_suggestion_arrows = 11;
  optional bool enable_threat_arrows = 12;
  optional bool enable_skills = 13;
  optional bool enable_teach_legal_moves = 14;
}

message SaveCoachGameRequest {
  oneof _game_uuid {
  string game_uuid = 12;
  }
  optional .chesscom.computer.v1.UserColor user_position = 1;
  optional string coach_id = 2;
  optional int32 coach_rating = 3;
  optional .chesscom.game_
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01433"></a>
## FND-01433: chesscom.coaches.v2.GetSettingsResponse.enable_teach_legal_moves = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enable_teach_legal_moves = 14;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3433.

```text
stion_arrows = 11;
  optional bool enable_threat_arrows = 12;
  optional bool enable_skills = 13;
  optional bool enable_teach_legal_moves = 14;
}

message SaveCoachGameRequest {
  oneof _game_uuid {
  string game_uuid = 12;
  }
  optional .chesscom.computer.v1.UserColor user_position = 1;
  optional string coach_id = 2;
  optional int32 coach_rating = 3;
  optional .chesscom.game_storage.v2.PlayerResult coach_result
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01434"></a>
## FND-01434: message declaration: chesscom.coaches.v2.SaveCoachGameRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SaveCoachGameRequest {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3481.

```text
_arrows = 12;
  optional bool enable_skills = 13;
  optional bool enable_teach_legal_moves = 14;
}

message SaveCoachGameRequest {
  oneof _game_uuid {
  string game_uuid = 12;
  }
  optional .chesscom.computer.v1.UserColor user_position = 1;
  optional string coach_id = 2;
  optional int32 coach_rating = 3;
  optional .chesscom.game_storage.v2.PlayerResult coach_result = 4;
  optional .chesscom.game_storage.v2.Playe
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01435"></a>
## FND-01435: oneof declaration: chesscom.coaches.v2.SaveCoachGameRequest._game_uuid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_uuid {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3514.

```text
ble_skills = 13;
  optional bool enable_teach_legal_moves = 14;
}

message SaveCoachGameRequest {
  oneof _game_uuid {
  string game_uuid = 12;
  }
  optional .chesscom.computer.v1.UserColor user_position = 1;
  optional string coach_id = 2;
  optional int32 coach_rating = 3;
  optional .chesscom.game_storage.v2.PlayerResult coach_result = 4;
  optional .chesscom.game_storage.v2.PlayerResult user_result = 5;
  option
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01436"></a>
## FND-01436: chesscom.coaches.v2.SaveCoachGameRequest.game_uuid = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string game_uuid = 12;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3535.

```text
tional bool enable_teach_legal_moves = 14;
}

message SaveCoachGameRequest {
  oneof _game_uuid {
  string game_uuid = 12;
  }
  optional .chesscom.computer.v1.UserColor user_position = 1;
  optional string coach_id = 2;
  optional int32 coach_rating = 3;
  optional .chesscom.game_storage.v2.PlayerResult coach_result = 4;
  optional .chesscom.game_storage.v2.PlayerResult user_result = 5;
  optional string initial_fen
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01437"></a>
## FND-01437: chesscom.coaches.v2.SaveCoachGameRequest.user_position = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.computer.v1.UserColor user_position = 1;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3564.

```text
l_moves = 14;
}

message SaveCoachGameRequest {
  oneof _game_uuid {
  string game_uuid = 12;
  }
  optional .chesscom.computer.v1.UserColor user_position = 1;
  optional string coach_id = 2;
  optional int32 coach_rating = 3;
  optional .chesscom.game_storage.v2.PlayerResult coach_result = 4;
  optional .chesscom.game_storage.v2.PlayerResult user_result = 5;
  optional string initial_fen = 6;
  optional string final
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01438"></a>
## FND-01438: chesscom.coaches.v2.SaveCoachGameRequest.coach_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coach_id = 2;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3626.

```text
uuid {
  string game_uuid = 12;
  }
  optional .chesscom.computer.v1.UserColor user_position = 1;
  optional string coach_id = 2;
  optional int32 coach_rating = 3;
  optional .chesscom.game_storage.v2.PlayerResult coach_result = 4;
  optional .chesscom.game_storage.v2.PlayerResult user_result = 5;
  optional string initial_fen = 6;
  optional string final_fen = 7;
  optional .google.protobuf.Timestamp game_start_tim
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01439"></a>
## FND-01439: chesscom.coaches.v2.SaveCoachGameRequest.coach_rating = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 coach_rating = 3;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3658.

```text
  }
  optional .chesscom.computer.v1.UserColor user_position = 1;
  optional string coach_id = 2;
  optional int32 coach_rating = 3;
  optional .chesscom.game_storage.v2.PlayerResult coach_result = 4;
  optional .chesscom.game_storage.v2.PlayerResult user_result = 5;
  optional string initial_fen = 6;
  optional string final_fen = 7;
  optional .google.protobuf.Timestamp game_start_time = 8;
  optional .google.protob
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01440"></a>
## FND-01440: chesscom.coaches.v2.SaveCoachGameRequest.coach_result = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.PlayerResult coach_result = 4;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3693.

```text
1.UserColor user_position = 1;
  optional string coach_id = 2;
  optional int32 coach_rating = 3;
  optional .chesscom.game_storage.v2.PlayerResult coach_result = 4;
  optional .chesscom.game_storage.v2.PlayerResult user_result = 5;
  optional string initial_fen = 6;
  optional string final_fen = 7;
  optional .google.protobuf.Timestamp game_start_time = 8;
  optional .google.protobuf.Timestamp game_end_time = 9;
  o
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01441"></a>
## FND-01441: chesscom.coaches.v2.SaveCoachGameRequest.user_result = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.PlayerResult user_result = 5;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3761.

```text
ional int32 coach_rating = 3;
  optional .chesscom.game_storage.v2.PlayerResult coach_result = 4;
  optional .chesscom.game_storage.v2.PlayerResult user_result = 5;
  optional string initial_fen = 6;
  optional string final_fen = 7;
  optional .google.protobuf.Timestamp game_start_time = 8;
  optional .google.protobuf.Timestamp game_end_time = 9;
  optional string move_text = 10;
  optional .chesscom.game_storage.v2.
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01442"></a>
## FND-01442: chesscom.coaches.v2.SaveCoachGameRequest.initial_fen = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string initial_fen = 6;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3828.

```text
PlayerResult coach_result = 4;
  optional .chesscom.game_storage.v2.PlayerResult user_result = 5;
  optional string initial_fen = 6;
  optional string final_fen = 7;
  optional .google.protobuf.Timestamp game_start_time = 8;
  optional .google.protobuf.Timestamp game_end_time = 9;
  optional string move_text = 10;
  optional .chesscom.game_storage.v2.GameResult game_result = 11;
  optional bool finish_vs_coach = 13;

```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01443"></a>
## FND-01443: chesscom.coaches.v2.SaveCoachGameRequest.final_fen = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string final_fen = 7;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3863.

```text
tional .chesscom.game_storage.v2.PlayerResult user_result = 5;
  optional string initial_fen = 6;
  optional string final_fen = 7;
  optional .google.protobuf.Timestamp game_start_time = 8;
  optional .google.protobuf.Timestamp game_end_time = 9;
  optional string move_text = 10;
  optional .chesscom.game_storage.v2.GameResult game_result = 11;
  optional bool finish_vs_coach = 13;
}

message HideCoachGameRequest {
 
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01444"></a>
## FND-01444: chesscom.coaches.v2.SaveCoachGameRequest.game_start_time = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp game_start_time = 8;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3896.

```text
PlayerResult user_result = 5;
  optional string initial_fen = 6;
  optional string final_fen = 7;
  optional .google.protobuf.Timestamp game_start_time = 8;
  optional .google.protobuf.Timestamp game_end_time = 9;
  optional string move_text = 10;
  optional .chesscom.game_storage.v2.GameResult game_result = 11;
  optional bool finish_vs_coach = 13;
}

message HideCoachGameRequest {
  optional uint64 game_id = 1;
}


```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01445"></a>
## FND-01445: chesscom.coaches.v2.SaveCoachGameRequest.game_end_time = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp game_end_time = 9;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 3955.

```text
 = 6;
  optional string final_fen = 7;
  optional .google.protobuf.Timestamp game_start_time = 8;
  optional .google.protobuf.Timestamp game_end_time = 9;
  optional string move_text = 10;
  optional .chesscom.game_storage.v2.GameResult game_result = 11;
  optional bool finish_vs_coach = 13;
}

message HideCoachGameRequest {
  optional uint64 game_id = 1;
}

message HideCoachGameResponse {
}

message SaveCoachGameRes
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01446"></a>
## FND-01446: chesscom.coaches.v2.SaveCoachGameRequest.move_text = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string move_text = 10;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 4012.

```text
.protobuf.Timestamp game_start_time = 8;
  optional .google.protobuf.Timestamp game_end_time = 9;
  optional string move_text = 10;
  optional .chesscom.game_storage.v2.GameResult game_result = 11;
  optional bool finish_vs_coach = 13;
}

message HideCoachGameRequest {
  optional uint64 game_id = 1;
}

message HideCoachGameResponse {
}

message SaveCoachGameResponse {
  optional uint64 game_id = 1;
  optional string 
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01447"></a>
## FND-01447: chesscom.coaches.v2.SaveCoachGameRequest.game_result = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_storage.v2.GameResult game_result = 11;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 4046.

```text
e = 8;
  optional .google.protobuf.Timestamp game_end_time = 9;
  optional string move_text = 10;
  optional .chesscom.game_storage.v2.GameResult game_result = 11;
  optional bool finish_vs_coach = 13;
}

message HideCoachGameRequest {
  optional uint64 game_id = 1;
}

message HideCoachGameResponse {
}

message SaveCoachGameResponse {
  optional uint64 game_id = 1;
  optional string game_uuid = 2;
}

message GetCoach
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01448"></a>
## FND-01448: chesscom.coaches.v2.SaveCoachGameRequest.finish_vs_coach = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool finish_vs_coach = 13;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 4112.

```text
optional string move_text = 10;
  optional .chesscom.game_storage.v2.GameResult game_result = 11;
  optional bool finish_vs_coach = 13;
}

message HideCoachGameRequest {
  optional uint64 game_id = 1;
}

message HideCoachGameResponse {
}

message SaveCoachGameResponse {
  optional uint64 game_id = 1;
  optional string game_uuid = 2;
}

message GetCoachSpeechRequest {
  optional string coach_id = 1;
  optional .chessc
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01449"></a>
## FND-01449: message declaration: chesscom.coaches.v2.HideCoachGameRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message HideCoachGameRequest {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 4151.

```text
nal .chesscom.game_storage.v2.GameResult game_result = 11;
  optional bool finish_vs_coach = 13;
}

message HideCoachGameRequest {
  optional uint64 game_id = 1;
}

message HideCoachGameResponse {
}

message SaveCoachGameResponse {
  optional uint64 game_id = 1;
  optional string game_uuid = 2;
}

message GetCoachSpeechRequest {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachContext context = 2;
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01450"></a>
## FND-01450: chesscom.coaches.v2.HideCoachGameRequest.game_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint64 game_id = 1;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 4184.

```text
eResult game_result = 11;
  optional bool finish_vs_coach = 13;
}

message HideCoachGameRequest {
  optional uint64 game_id = 1;
}

message HideCoachGameResponse {
}

message SaveCoachGameResponse {
  optional uint64 game_id = 1;
  optional string game_uuid = 2;
}

message GetCoachSpeechRequest {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachContext context = 2;
}

message GetCoachSpeechRespons
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01451"></a>
## FND-01451: message declaration: chesscom.coaches.v2.HideCoachGameResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message HideCoachGameResponse {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 4216.

```text
onal bool finish_vs_coach = 13;
}

message HideCoachGameRequest {
  optional uint64 game_id = 1;
}

message HideCoachGameResponse {
}

message SaveCoachGameResponse {
  optional uint64 game_id = 1;
  optional string game_uuid = 2;
}

message GetCoachSpeechRequest {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachContext context = 2;
}

message GetCoachSpeechResponse {
  repeated .chesscom.coaches
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01452"></a>
## FND-01452: message declaration: chesscom.coaches.v2.SaveCoachGameResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SaveCoachGameResponse {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 4251.

```text
message HideCoachGameRequest {
  optional uint64 game_id = 1;
}

message HideCoachGameResponse {
}

message SaveCoachGameResponse {
  optional uint64 game_id = 1;
  optional string game_uuid = 2;
}

message GetCoachSpeechRequest {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachContext context = 2;
}

message GetCoachSpeechResponse {
  repeated .chesscom.coaches.v2.SpeechString speech = 1;
}

```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01453"></a>
## FND-01453: chesscom.coaches.v2.SaveCoachGameResponse.game_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint64 game_id = 1;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 4184.

```text
eResult game_result = 11;
  optional bool finish_vs_coach = 13;
}

message HideCoachGameRequest {
  optional uint64 game_id = 1;
}

message HideCoachGameResponse {
}

message SaveCoachGameResponse {
  optional uint64 game_id = 1;
  optional string game_uuid = 2;
}

message GetCoachSpeechRequest {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachContext context = 2;
}

message GetCoachSpeechRespons
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01454"></a>
## FND-01454: chesscom.coaches.v2.SaveCoachGameResponse.game_uuid = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_uuid = 2;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 4316.

```text
message HideCoachGameResponse {
}

message SaveCoachGameResponse {
  optional uint64 game_id = 1;
  optional string game_uuid = 2;
}

message GetCoachSpeechRequest {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachContext context = 2;
}

message GetCoachSpeechResponse {
  repeated .chesscom.coaches.v2.SpeechString speech = 1;
}

```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01455"></a>
## FND-01455: message declaration: chesscom.coaches.v2.GetCoachSpeechRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCoachSpeechRequest {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 4350.

```text

message SaveCoachGameResponse {
  optional uint64 game_id = 1;
  optional string game_uuid = 2;
}

message GetCoachSpeechRequest {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachContext context = 2;
}

message GetCoachSpeechResponse {
  repeated .chesscom.coaches.v2.SpeechString speech = 1;
}

```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01456"></a>
## FND-01456: chesscom.coaches.v2.GetCoachSpeechRequest.coach_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coach_id = 1;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 676.

```text

  repeated .chesscom.coaches.v2.CoachCategory coach_categories = 1;
}

message GetCoachRequest {
  optional string coach_id = 1;
}

message GetCoachResponse {
  optional .chesscom.coaches.v2.Coach coach = 1;
}

message GetCoachesRequest {
  repeated string coach_ids = 1;
}

message GetCoachesResponse {
  repeated .chesscom.coaches.v2.Coach coaches = 1;
}

message SetCurrentCoachRequest {
  oneof _locale_override {
 
```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01457"></a>
## FND-01457: chesscom.coaches.v2.GetCoachSpeechRequest.context = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.coaches.v2.CoachContext context = 2;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 4416.

```text
optional string game_uuid = 2;
}

message GetCoachSpeechRequest {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachContext context = 2;
}

message GetCoachSpeechResponse {
  repeated .chesscom.coaches.v2.SpeechString speech = 1;
}

```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01458"></a>
## FND-01458: message declaration: chesscom.coaches.v2.GetCoachSpeechResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCoachSpeechResponse {

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 4475.

```text
uest {
  optional string coach_id = 1;
  optional .chesscom.coaches.v2.CoachContext context = 2;
}

message GetCoachSpeechResponse {
  repeated .chesscom.coaches.v2.SpeechString speech = 1;
}

```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01459"></a>
## FND-01459: chesscom.coaches.v2.GetCoachSpeechResponse.speech = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.coaches.v2.SpeechString speech = 1;

### Evidence

- **SRC-0258** `research/proto/chesscom/coaches/v2/service.proto` — [preserved redacted evidence](../evidence/text/4e553d74fee37f8bb524d1ab53e51b68f737af36b14ab0f4ac5722e8538d0316.proto)
  Character offset 4510.

```text
 1;
  optional .chesscom.coaches.v2.CoachContext context = 2;
}

message GetCoachSpeechResponse {
  repeated .chesscom.coaches.v2.SpeechString speech = 1;
}

```

**Source references:** SRC-0258, SRC-1229  
**URL references:** None independently associated  
**Related findings:** FND-01343, FND-01344, FND-01345

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01460"></a>
## FND-01460: enum declaration: chesscom.coaches.v2.CoachSwitchSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CoachSwitchSource {

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 100.

```text
// source: chesscom/coaches/v2/user_activity.proto
// syntax: proto3

package chesscom.coaches.v2;

enum CoachSwitchSource {
  COACH_SWITCH_SOURCE_UNSPECIFIED = 0;
  COACH_SWITCH_SOURCE_SETTINGS = 1;
  COACH_SWITCH_SOURCE_GAME_REVIEW = 2;
  COACH_SWITCH_SOURCE_PLAY_COACH = 3;
  COACH_SWITCH_SOURCE_DAILY_PUZZLE = 4;
  COACH_SWITCH_SOURCE_PUZZLES_ROOT = 5;
  COACH_SWITCH_SOURCE_PUZZLE = 6;
  COACH_SWITCH_SOURCE_LESSONS
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01461"></a>
## FND-01461: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_UNSPECIFIED = 0;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 127.

```text
/v2/user_activity.proto
// syntax: proto3

package chesscom.coaches.v2;

enum CoachSwitchSource {
  COACH_SWITCH_SOURCE_UNSPECIFIED = 0;
  COACH_SWITCH_SOURCE_SETTINGS = 1;
  COACH_SWITCH_SOURCE_GAME_REVIEW = 2;
  COACH_SWITCH_SOURCE_PLAY_COACH = 3;
  COACH_SWITCH_SOURCE_DAILY_PUZZLE = 4;
  COACH_SWITCH_SOURCE_PUZZLES_ROOT = 5;
  COACH_SWITCH_SOURCE_PUZZLE = 6;
  COACH_SWITCH_SOURCE_LESSONS_ROOT = 7;
  COACH_SWITCH_S
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01462"></a>
## FND-01462: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_SETTINGS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_SETTINGS = 1;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 166.

```text
o3

package chesscom.coaches.v2;

enum CoachSwitchSource {
  COACH_SWITCH_SOURCE_UNSPECIFIED = 0;
  COACH_SWITCH_SOURCE_SETTINGS = 1;
  COACH_SWITCH_SOURCE_GAME_REVIEW = 2;
  COACH_SWITCH_SOURCE_PLAY_COACH = 3;
  COACH_SWITCH_SOURCE_DAILY_PUZZLE = 4;
  COACH_SWITCH_SOURCE_PUZZLES_ROOT = 5;
  COACH_SWITCH_SOURCE_PUZZLE = 6;
  COACH_SWITCH_SOURCE_LESSONS_ROOT = 7;
  COACH_SWITCH_SOURCE_LESSON = 8;
  COACH_SWITCH_SOURCE
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01463"></a>
## FND-01463: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_GAME_REVIEW = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_GAME_REVIEW = 2;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 202.

```text
um CoachSwitchSource {
  COACH_SWITCH_SOURCE_UNSPECIFIED = 0;
  COACH_SWITCH_SOURCE_SETTINGS = 1;
  COACH_SWITCH_SOURCE_GAME_REVIEW = 2;
  COACH_SWITCH_SOURCE_PLAY_COACH = 3;
  COACH_SWITCH_SOURCE_DAILY_PUZZLE = 4;
  COACH_SWITCH_SOURCE_PUZZLES_ROOT = 5;
  COACH_SWITCH_SOURCE_PUZZLE = 6;
  COACH_SWITCH_SOURCE_LESSONS_ROOT = 7;
  COACH_SWITCH_SOURCE_LESSON = 8;
  COACH_SWITCH_SOURCE_COACH_GAME_SETUP = 9;
  COACH_SWITC
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01464"></a>
## FND-01464: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_PLAY_COACH = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_PLAY_COACH = 3;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 241.

```text
OURCE_UNSPECIFIED = 0;
  COACH_SWITCH_SOURCE_SETTINGS = 1;
  COACH_SWITCH_SOURCE_GAME_REVIEW = 2;
  COACH_SWITCH_SOURCE_PLAY_COACH = 3;
  COACH_SWITCH_SOURCE_DAILY_PUZZLE = 4;
  COACH_SWITCH_SOURCE_PUZZLES_ROOT = 5;
  COACH_SWITCH_SOURCE_PUZZLE = 6;
  COACH_SWITCH_SOURCE_LESSONS_ROOT = 7;
  COACH_SWITCH_SOURCE_LESSON = 8;
  COACH_SWITCH_SOURCE_COACH_GAME_SETUP = 9;
  COACH_SWITCH_SOURCE_LEARN_ROOT = 10;
  COACH_SWITC
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01465"></a>
## FND-01465: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_DAILY_PUZZLE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_DAILY_PUZZLE = 4;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 279.

```text
SOURCE_SETTINGS = 1;
  COACH_SWITCH_SOURCE_GAME_REVIEW = 2;
  COACH_SWITCH_SOURCE_PLAY_COACH = 3;
  COACH_SWITCH_SOURCE_DAILY_PUZZLE = 4;
  COACH_SWITCH_SOURCE_PUZZLES_ROOT = 5;
  COACH_SWITCH_SOURCE_PUZZLE = 6;
  COACH_SWITCH_SOURCE_LESSONS_ROOT = 7;
  COACH_SWITCH_SOURCE_LESSON = 8;
  COACH_SWITCH_SOURCE_COACH_GAME_SETUP = 9;
  COACH_SWITCH_SOURCE_LEARN_ROOT = 10;
  COACH_SWITCH_SOURCE_DEEPLINK = 11;
  COACH_SWITCH
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01466"></a>
## FND-01466: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_PUZZLES_ROOT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_PUZZLES_ROOT = 5;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 319.

```text
CE_GAME_REVIEW = 2;
  COACH_SWITCH_SOURCE_PLAY_COACH = 3;
  COACH_SWITCH_SOURCE_DAILY_PUZZLE = 4;
  COACH_SWITCH_SOURCE_PUZZLES_ROOT = 5;
  COACH_SWITCH_SOURCE_PUZZLE = 6;
  COACH_SWITCH_SOURCE_LESSONS_ROOT = 7;
  COACH_SWITCH_SOURCE_LESSON = 8;
  COACH_SWITCH_SOURCE_COACH_GAME_SETUP = 9;
  COACH_SWITCH_SOURCE_LEARN_ROOT = 10;
  COACH_SWITCH_SOURCE_DEEPLINK = 11;
  COACH_SWITCH_SOURCE_WELCOME_MODAL = 12;
  COACH_SWIT
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01467"></a>
## FND-01467: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_PUZZLE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_PUZZLE = 6;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 359.

```text
E_PLAY_COACH = 3;
  COACH_SWITCH_SOURCE_DAILY_PUZZLE = 4;
  COACH_SWITCH_SOURCE_PUZZLES_ROOT = 5;
  COACH_SWITCH_SOURCE_PUZZLE = 6;
  COACH_SWITCH_SOURCE_LESSONS_ROOT = 7;
  COACH_SWITCH_SOURCE_LESSON = 8;
  COACH_SWITCH_SOURCE_COACH_GAME_SETUP = 9;
  COACH_SWITCH_SOURCE_LEARN_ROOT = 10;
  COACH_SWITCH_SOURCE_DEEPLINK = 11;
  COACH_SWITCH_SOURCE_WELCOME_MODAL = 12;
  COACH_SWITCH_SOURCE_ONBOARDING = 13;
  COACH_SWITC
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01468"></a>
## FND-01468: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_LESSONS_ROOT = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_LESSONS_ROOT = 7;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 393.

```text
OURCE_DAILY_PUZZLE = 4;
  COACH_SWITCH_SOURCE_PUZZLES_ROOT = 5;
  COACH_SWITCH_SOURCE_PUZZLE = 6;
  COACH_SWITCH_SOURCE_LESSONS_ROOT = 7;
  COACH_SWITCH_SOURCE_LESSON = 8;
  COACH_SWITCH_SOURCE_COACH_GAME_SETUP = 9;
  COACH_SWITCH_SOURCE_LEARN_ROOT = 10;
  COACH_SWITCH_SOURCE_DEEPLINK = 11;
  COACH_SWITCH_SOURCE_WELCOME_MODAL = 12;
  COACH_SWITCH_SOURCE_ONBOARDING = 13;
  COACH_SWITCH_SOURCE_HOME = 14;
  COACH_SWITCH
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01469"></a>
## FND-01469: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_LESSON = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_LESSON = 8;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 433.

```text
OURCE_PUZZLES_ROOT = 5;
  COACH_SWITCH_SOURCE_PUZZLE = 6;
  COACH_SWITCH_SOURCE_LESSONS_ROOT = 7;
  COACH_SWITCH_SOURCE_LESSON = 8;
  COACH_SWITCH_SOURCE_COACH_GAME_SETUP = 9;
  COACH_SWITCH_SOURCE_LEARN_ROOT = 10;
  COACH_SWITCH_SOURCE_DEEPLINK = 11;
  COACH_SWITCH_SOURCE_WELCOME_MODAL = 12;
  COACH_SWITCH_SOURCE_ONBOARDING = 13;
  COACH_SWITCH_SOURCE_HOME = 14;
  COACH_SWITCH_SOURCE_TRAIN = 15;
}

enum CoachTagline
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01470"></a>
## FND-01470: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_COACH_GAME_SETUP = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_COACH_GAME_SETUP = 9;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 467.

```text
ITCH_SOURCE_PUZZLE = 6;
  COACH_SWITCH_SOURCE_LESSONS_ROOT = 7;
  COACH_SWITCH_SOURCE_LESSON = 8;
  COACH_SWITCH_SOURCE_COACH_GAME_SETUP = 9;
  COACH_SWITCH_SOURCE_LEARN_ROOT = 10;
  COACH_SWITCH_SOURCE_DEEPLINK = 11;
  COACH_SWITCH_SOURCE_WELCOME_MODAL = 12;
  COACH_SWITCH_SOURCE_ONBOARDING = 13;
  COACH_SWITCH_SOURCE_HOME = 14;
  COACH_SWITCH_SOURCE_TRAIN = 15;
}

enum CoachTaglineUi {
  COACH_TAGLINE_UI_UNSPECIFIE
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01471"></a>
## FND-01471: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_LEARN_ROOT = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_LEARN_ROOT = 10;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 511.

```text
E_LESSONS_ROOT = 7;
  COACH_SWITCH_SOURCE_LESSON = 8;
  COACH_SWITCH_SOURCE_COACH_GAME_SETUP = 9;
  COACH_SWITCH_SOURCE_LEARN_ROOT = 10;
  COACH_SWITCH_SOURCE_DEEPLINK = 11;
  COACH_SWITCH_SOURCE_WELCOME_MODAL = 12;
  COACH_SWITCH_SOURCE_ONBOARDING = 13;
  COACH_SWITCH_SOURCE_HOME = 14;
  COACH_SWITCH_SOURCE_TRAIN = 15;
}

enum CoachTaglineUi {
  COACH_TAGLINE_UI_UNSPECIFIED = 0;
  COACH_TAGLINE_UI_CHOOSE_COACH_MODAL
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01472"></a>
## FND-01472: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_DEEPLINK = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_DEEPLINK = 11;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 550.

```text
CE_LESSON = 8;
  COACH_SWITCH_SOURCE_COACH_GAME_SETUP = 9;
  COACH_SWITCH_SOURCE_LEARN_ROOT = 10;
  COACH_SWITCH_SOURCE_DEEPLINK = 11;
  COACH_SWITCH_SOURCE_WELCOME_MODAL = 12;
  COACH_SWITCH_SOURCE_ONBOARDING = 13;
  COACH_SWITCH_SOURCE_HOME = 14;
  COACH_SWITCH_SOURCE_TRAIN = 15;
}

enum CoachTaglineUi {
  COACH_TAGLINE_UI_UNSPECIFIED = 0;
  COACH_TAGLINE_UI_CHOOSE_COACH_MODAL = 1;
  COACH_TAGLINE_UI_SIGNUP_CHOOSE_
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01473"></a>
## FND-01473: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_WELCOME_MODAL = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_WELCOME_MODAL = 12;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 587.

```text
COACH_GAME_SETUP = 9;
  COACH_SWITCH_SOURCE_LEARN_ROOT = 10;
  COACH_SWITCH_SOURCE_DEEPLINK = 11;
  COACH_SWITCH_SOURCE_WELCOME_MODAL = 12;
  COACH_SWITCH_SOURCE_ONBOARDING = 13;
  COACH_SWITCH_SOURCE_HOME = 14;
  COACH_SWITCH_SOURCE_TRAIN = 15;
}

enum CoachTaglineUi {
  COACH_TAGLINE_UI_UNSPECIFIED = 0;
  COACH_TAGLINE_UI_CHOOSE_COACH_MODAL = 1;
  COACH_TAGLINE_UI_SIGNUP_CHOOSE_COACH_STEP = 2;
  COACH_TAGLINE_UI_SE
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01474"></a>
## FND-01474: chesscom.coaches.v2.CoachSwitchSource.COACH_SWITCH_SOURCE_ONBOARDING = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COACH_SWITCH_SOURCE_ONBOARDING = 13;

### Evidence

- **SRC-0259** `research/proto/chesscom/coaches/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/40b049ca8e741655a8d876511548d9b62278f6a252d02f56321fe65bf5e97358.proto)
  Character offset 629.

```text
E_LEARN_ROOT = 10;
  COACH_SWITCH_SOURCE_DEEPLINK = 11;
  COACH_SWITCH_SOURCE_WELCOME_MODAL = 12;
  COACH_SWITCH_SOURCE_ONBOARDING = 13;
  COACH_SWITCH_SOURCE_HOME = 14;
  COACH_SWITCH_SOURCE_TRAIN = 15;
}

enum CoachTaglineUi {
  COACH_TAGLINE_UI_UNSPECIFIED = 0;
  COACH_TAGLINE_UI_CHOOSE_COACH_MODAL = 1;
  COACH_TAGLINE_UI_SIGNUP_CHOOSE_COACH_STEP = 2;
  COACH_TAGLINE_UI_SELECT_COACH_SETTINGS = 3;
}

enum PlayCoach
```

**Source references:** SRC-0259, SRC-1230  
**URL references:** None independently associated  
**Related findings:** FND-01460, FND-01461, FND-01462

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
