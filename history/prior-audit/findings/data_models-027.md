# data_models — findings 2601–2700

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-02875"></a>
## FND-02875: chesscom.explanation_engine.v1.BotEngine.BOT_ENGINE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_ENGINE_UNSPECIFIED = 0;

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 672.

```text
O_CHESS = 13;
  BOT_PERSONALITY_DANNY = 14;
  BOT_PERSONALITY_UNLEASHED = 15;
}

enum BotEngine {
  BOT_ENGINE_UNSPECIFIED = 0;
  BOT_ENGINE_KOMODO = 1;
  BOT_ENGINE_TORCH = 2;
}

message BotTimeLimits {
  oneof _time_limit_ms {
  int32 time_limit_ms = 1;
  }
  oneof _time_left_ms {
  int32 time_left_ms = 2;
  }
  oneof _time_inc_ms {
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool ada
```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02876"></a>
## FND-02876: chesscom.explanation_engine.v1.BotEngine.BOT_ENGINE_KOMODO = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_ENGINE_KOMODO = 1;

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 702.

```text
Y_DANNY = 14;
  BOT_PERSONALITY_UNLEASHED = 15;
}

enum BotEngine {
  BOT_ENGINE_UNSPECIFIED = 0;
  BOT_ENGINE_KOMODO = 1;
  BOT_ENGINE_TORCH = 2;
}

message BotTimeLimits {
  oneof _time_limit_ms {
  int32 time_limit_ms = 1;
  }
  oneof _time_left_ms {
  int32 time_left_ms = 2;
  }
  oneof _time_inc_ms {
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _person
```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02877"></a>
## FND-02877: chesscom.explanation_engine.v1.BotEngine.BOT_ENGINE_TORCH = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BOT_ENGINE_TORCH = 2;

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 727.

```text
NALITY_UNLEASHED = 15;
}

enum BotEngine {
  BOT_ENGINE_UNSPECIFIED = 0;
  BOT_ENGINE_KOMODO = 1;
  BOT_ENGINE_TORCH = 2;
}

message BotTimeLimits {
  oneof _time_limit_ms {
  int32 time_limit_ms = 1;
  }
  oneof _time_left_ms {
  int32 time_left_ms = 2;
  }
  oneof _time_inc_ms {
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _personality {
  .chesscom.expla
```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02878"></a>
## FND-02878: message declaration: chesscom.explanation_engine.v1.BotTimeLimits

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotTimeLimits {

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 752.

```text

enum BotEngine {
  BOT_ENGINE_UNSPECIFIED = 0;
  BOT_ENGINE_KOMODO = 1;
  BOT_ENGINE_TORCH = 2;
}

message BotTimeLimits {
  oneof _time_limit_ms {
  int32 time_limit_ms = 1;
  }
  oneof _time_left_ms {
  int32 time_left_ms = 2;
  }
  oneof _time_inc_ms {
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _personality {
  .chesscom.explanation_engine.v1.BotPerso
```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02879"></a>
## FND-02879: oneof declaration: chesscom.explanation_engine.v1.BotTimeLimits._time_limit_ms

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_limit_ms {

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 778.

```text
GINE_UNSPECIFIED = 0;
  BOT_ENGINE_KOMODO = 1;
  BOT_ENGINE_TORCH = 2;
}

message BotTimeLimits {
  oneof _time_limit_ms {
  int32 time_limit_ms = 1;
  }
  oneof _time_left_ms {
  int32 time_left_ms = 2;
  }
  oneof _time_inc_ms {
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _personality {
  .chesscom.explanation_engine.v1.BotPersonality personality = 3;
  
```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02880"></a>
## FND-02880: chesscom.explanation_engine.v1.BotTimeLimits.time_limit_ms = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 time_limit_ms = 1;

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 803.

```text
OT_ENGINE_KOMODO = 1;
  BOT_ENGINE_TORCH = 2;
}

message BotTimeLimits {
  oneof _time_limit_ms {
  int32 time_limit_ms = 1;
  }
  oneof _time_left_ms {
  int32 time_left_ms = 2;
  }
  oneof _time_inc_ms {
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _personality {
  .chesscom.explanation_engine.v1.BotPersonality personality = 3;
  }
  oneof _book_path {
  
```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02881"></a>
## FND-02881: oneof declaration: chesscom.explanation_engine.v1.BotTimeLimits._time_left_ms

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_left_ms {

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 834.

```text
INE_TORCH = 2;
}

message BotTimeLimits {
  oneof _time_limit_ms {
  int32 time_limit_ms = 1;
  }
  oneof _time_left_ms {
  int32 time_left_ms = 2;
  }
  oneof _time_inc_ms {
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _personality {
  .chesscom.explanation_engine.v1.BotPersonality personality = 3;
  }
  oneof _book_path {
  string book_path = 4;
  }
  one
```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02882"></a>
## FND-02882: chesscom.explanation_engine.v1.BotTimeLimits.time_left_ms = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 time_left_ms = 2;

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 858.

```text
e BotTimeLimits {
  oneof _time_limit_ms {
  int32 time_limit_ms = 1;
  }
  oneof _time_left_ms {
  int32 time_left_ms = 2;
  }
  oneof _time_inc_ms {
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _personality {
  .chesscom.explanation_engine.v1.BotPersonality personality = 3;
  }
  oneof _book_path {
  string book_path = 4;
  }
  oneof _time_limits {
  .che
```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02883"></a>
## FND-02883: oneof declaration: chesscom.explanation_engine.v1.BotTimeLimits._time_inc_ms

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_inc_ms {

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 888.

```text
e_limit_ms {
  int32 time_limit_ms = 1;
  }
  oneof _time_left_ms {
  int32 time_left_ms = 2;
  }
  oneof _time_inc_ms {
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _personality {
  .chesscom.explanation_engine.v1.BotPersonality personality = 3;
  }
  oneof _book_path {
  string book_path = 4;
  }
  oneof _time_limits {
  .chesscom.explanation_engine.v1.Bo
```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02884"></a>
## FND-02884: chesscom.explanation_engine.v1.BotTimeLimits.time_inc_ms = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 time_inc_ms = 3;

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 911.

```text
me_limit_ms = 1;
  }
  oneof _time_left_ms {
  int32 time_left_ms = 2;
  }
  oneof _time_inc_ms {
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _personality {
  .chesscom.explanation_engine.v1.BotPersonality personality = 3;
  }
  oneof _book_path {
  string book_path = 4;
  }
  oneof _time_limits {
  .chesscom.explanation_engine.v1.BotTimeLimits time_limits
```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02885"></a>
## FND-02885: message declaration: chesscom.explanation_engine.v1.BotOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotOptions {

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 941.

```text
time_left_ms {
  int32 time_left_ms = 2;
  }
  oneof _time_inc_ms {
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _personality {
  .chesscom.explanation_engine.v1.BotPersonality personality = 3;
  }
  oneof _book_path {
  string book_path = 4;
  }
  oneof _time_limits {
  .chesscom.explanation_engine.v1.BotTimeLimits time_limits = 5;
  }
  oneof _artifact_id
```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02886"></a>
## FND-02886: oneof declaration: chesscom.explanation_engine.v1.BotOptions._adaptive

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _adaptive {

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 964.

```text
time_left_ms = 2;
  }
  oneof _time_inc_ms {
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _personality {
  .chesscom.explanation_engine.v1.BotPersonality personality = 3;
  }
  oneof _book_path {
  string book_path = 4;
  }
  oneof _time_limits {
  .chesscom.explanation_engine.v1.BotTimeLimits time_limits = 5;
  }
  oneof _artifact_id {
  string artifact_id
```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02887"></a>
## FND-02887: chesscom.explanation_engine.v1.BotOptions.adaptive = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool adaptive = 2;

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 984.

```text
}
  oneof _time_inc_ms {
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _personality {
  .chesscom.explanation_engine.v1.BotPersonality personality = 3;
  }
  oneof _book_path {
  string book_path = 4;
  }
  oneof _time_limits {
  .chesscom.explanation_engine.v1.BotTimeLimits time_limits = 5;
  }
  oneof _artifact_id {
  string artifact_id = 6;
  }
  optional
```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02888"></a>
## FND-02888: oneof declaration: chesscom.explanation_engine.v1.BotOptions._personality

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _personality {

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 1009.

```text
  int32 time_inc_ms = 3;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _personality {
  .chesscom.explanation_engine.v1.BotPersonality personality = 3;
  }
  oneof _book_path {
  string book_path = 4;
  }
  oneof _time_limits {
  .chesscom.explanation_engine.v1.BotTimeLimits time_limits = 5;
  }
  oneof _artifact_id {
  string artifact_id = 6;
  }
  optional int32 rating = 1;
}

```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02889"></a>
## FND-02889: chesscom.explanation_engine.v1.BotOptions.personality = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.BotPersonality personality = 3;

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 1032.

```text
;
  }
}

message BotOptions {
  oneof _adaptive {
  bool adaptive = 2;
  }
  oneof _personality {
  .chesscom.explanation_engine.v1.BotPersonality personality = 3;
  }
  oneof _book_path {
  string book_path = 4;
  }
  oneof _time_limits {
  .chesscom.explanation_engine.v1.BotTimeLimits time_limits = 5;
  }
  oneof _artifact_id {
  string artifact_id = 6;
  }
  optional int32 rating = 1;
}

```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02890"></a>
## FND-02890: oneof declaration: chesscom.explanation_engine.v1.BotOptions._book_path

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _book_path {

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 1102.

```text

  }
  oneof _personality {
  .chesscom.explanation_engine.v1.BotPersonality personality = 3;
  }
  oneof _book_path {
  string book_path = 4;
  }
  oneof _time_limits {
  .chesscom.explanation_engine.v1.BotTimeLimits time_limits = 5;
  }
  oneof _artifact_id {
  string artifact_id = 6;
  }
  optional int32 rating = 1;
}

```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02891"></a>
## FND-02891: chesscom.explanation_engine.v1.BotOptions.book_path = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string book_path = 4;

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 1123.

```text
lity {
  .chesscom.explanation_engine.v1.BotPersonality personality = 3;
  }
  oneof _book_path {
  string book_path = 4;
  }
  oneof _time_limits {
  .chesscom.explanation_engine.v1.BotTimeLimits time_limits = 5;
  }
  oneof _artifact_id {
  string artifact_id = 6;
  }
  optional int32 rating = 1;
}

```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02892"></a>
## FND-02892: oneof declaration: chesscom.explanation_engine.v1.BotOptions._time_limits

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_limits {

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 1151.

```text
on_engine.v1.BotPersonality personality = 3;
  }
  oneof _book_path {
  string book_path = 4;
  }
  oneof _time_limits {
  .chesscom.explanation_engine.v1.BotTimeLimits time_limits = 5;
  }
  oneof _artifact_id {
  string artifact_id = 6;
  }
  optional int32 rating = 1;
}

```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02893"></a>
## FND-02893: chesscom.explanation_engine.v1.BotOptions.time_limits = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.BotTimeLimits time_limits = 5;

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 1174.

```text
lity personality = 3;
  }
  oneof _book_path {
  string book_path = 4;
  }
  oneof _time_limits {
  .chesscom.explanation_engine.v1.BotTimeLimits time_limits = 5;
  }
  oneof _artifact_id {
  string artifact_id = 6;
  }
  optional int32 rating = 1;
}

```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02894"></a>
## FND-02894: oneof declaration: chesscom.explanation_engine.v1.BotOptions._artifact_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _artifact_id {

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 1243.

```text
;
  }
  oneof _time_limits {
  .chesscom.explanation_engine.v1.BotTimeLimits time_limits = 5;
  }
  oneof _artifact_id {
  string artifact_id = 6;
  }
  optional int32 rating = 1;
}

```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02895"></a>
## FND-02895: chesscom.explanation_engine.v1.BotOptions.artifact_id = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string artifact_id = 6;

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 1266.

```text
its {
  .chesscom.explanation_engine.v1.BotTimeLimits time_limits = 5;
  }
  oneof _artifact_id {
  string artifact_id = 6;
  }
  optional int32 rating = 1;
}

```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02896"></a>
## FND-02896: chesscom.explanation_engine.v1.BotOptions.rating = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 rating = 1;

### Evidence

- **SRC-0338** `research/proto/chesscom/explanation_engine/v1/bot.proto` — [preserved redacted evidence](../evidence/text/f170a23a8561c5b2f1f2da73f41a166ad39dcc916d1180ef1b8790a928df6140.proto)
  Character offset 1296.

```text
engine.v1.BotTimeLimits time_limits = 5;
  }
  oneof _artifact_id {
  string artifact_id = 6;
  }
  optional int32 rating = 1;
}

```

**Source references:** SRC-0338, SRC-1309  
**URL references:** None independently associated  
**Related findings:** FND-02857, FND-02858, FND-02859

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02897"></a>
## FND-02897: enum declaration: chesscom.explanation_engine.v1.PositionShape

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PositionShape {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 131.

```text
_engine/v1/bot_move_configuration.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum PositionShape {
  POSITION_SHAPE_UNSPECIFIED = 0;
  POSITION_SHAPE_PASSIVE = 1;
  POSITION_SHAPE_ACTIVE = 2;
  POSITION_SHAPE_CLOSED = 3;
  POSITION_SHAPE_OPEN = 4;
  POSITION_SHAPE_SEMI_OPEN = 5;
  POSITION_SHAPE_THREATENED = 6;
  POSITION_SHAPE_THREATENING = 7;
  POSITION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP =
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02898"></a>
## FND-02898: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

POSITION_SHAPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 154.

```text
figuration.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum PositionShape {
  POSITION_SHAPE_UNSPECIFIED = 0;
  POSITION_SHAPE_PASSIVE = 1;
  POSITION_SHAPE_ACTIVE = 2;
  POSITION_SHAPE_CLOSED = 3;
  POSITION_SHAPE_OPEN = 4;
  POSITION_SHAPE_SEMI_OPEN = 5;
  POSITION_SHAPE_THREATENED = 6;
  POSITION_SHAPE_THREATENING = 7;
  POSITION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP = 9;
}

enum ModelArch {
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02899"></a>
## FND-02899: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_PASSIVE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

POSITION_SHAPE_PASSIVE = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 188.

```text


package chesscom.explanation_engine.v1;

enum PositionShape {
  POSITION_SHAPE_UNSPECIFIED = 0;
  POSITION_SHAPE_PASSIVE = 1;
  POSITION_SHAPE_ACTIVE = 2;
  POSITION_SHAPE_CLOSED = 3;
  POSITION_SHAPE_OPEN = 4;
  POSITION_SHAPE_SEMI_OPEN = 5;
  POSITION_SHAPE_THREATENED = 6;
  POSITION_SHAPE_THREATENING = 7;
  POSITION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP = 9;
}

enum ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  M
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02900"></a>
## FND-02900: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_ACTIVE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

POSITION_SHAPE_ACTIVE = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 218.

```text
_engine.v1;

enum PositionShape {
  POSITION_SHAPE_UNSPECIFIED = 0;
  POSITION_SHAPE_PASSIVE = 1;
  POSITION_SHAPE_ACTIVE = 2;
  POSITION_SHAPE_CLOSED = 3;
  POSITION_SHAPE_OPEN = 4;
  POSITION_SHAPE_SEMI_OPEN = 5;
  POSITION_SHAPE_THREATENED = 6;
  POSITION_SHAPE_THREATENING = 7;
  POSITION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP = 9;
}

enum ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_A
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02901"></a>
## FND-02901: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_CLOSED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

POSITION_SHAPE_CLOSED = 3;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 247.

```text
pe {
  POSITION_SHAPE_UNSPECIFIED = 0;
  POSITION_SHAPE_PASSIVE = 1;
  POSITION_SHAPE_ACTIVE = 2;
  POSITION_SHAPE_CLOSED = 3;
  POSITION_SHAPE_OPEN = 4;
  POSITION_SHAPE_SEMI_OPEN = 5;
  POSITION_SHAPE_THREATENED = 6;
  POSITION_SHAPE_THREATENING = 7;
  POSITION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP = 9;
}

enum ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02902"></a>
## FND-02902: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_OPEN = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

POSITION_SHAPE_OPEN = 4;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 276.

```text
FIED = 0;
  POSITION_SHAPE_PASSIVE = 1;
  POSITION_SHAPE_ACTIVE = 2;
  POSITION_SHAPE_CLOSED = 3;
  POSITION_SHAPE_OPEN = 4;
  POSITION_SHAPE_SEMI_OPEN = 5;
  POSITION_SHAPE_THREATENED = 6;
  POSITION_SHAPE_THREATENING = 7;
  POSITION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP = 9;
}

enum ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_M
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02903"></a>
## FND-02903: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_SEMI_OPEN = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

POSITION_SHAPE_SEMI_OPEN = 5;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 303.

```text
PASSIVE = 1;
  POSITION_SHAPE_ACTIVE = 2;
  POSITION_SHAPE_CLOSED = 3;
  POSITION_SHAPE_OPEN = 4;
  POSITION_SHAPE_SEMI_OPEN = 5;
  POSITION_SHAPE_THREATENED = 6;
  POSITION_SHAPE_THREATENING = 7;
  POSITION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP = 9;
}

enum ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMov
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02904"></a>
## FND-02904: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_THREATENED = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

POSITION_SHAPE_THREATENED = 6;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 335.

```text
TIVE = 2;
  POSITION_SHAPE_CLOSED = 3;
  POSITION_SHAPE_OPEN = 4;
  POSITION_SHAPE_SEMI_OPEN = 5;
  POSITION_SHAPE_THREATENED = 6;
  POSITION_SHAPE_THREATENING = 7;
  POSITION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP = 9;
}

enum ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMoveConfiguration {
  oneof mode {

```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02905"></a>
## FND-02905: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_THREATENING = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

POSITION_SHAPE_THREATENING = 7;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 368.

```text
 = 3;
  POSITION_SHAPE_OPEN = 4;
  POSITION_SHAPE_SEMI_OPEN = 5;
  POSITION_SHAPE_THREATENED = 6;
  POSITION_SHAPE_THREATENING = 7;
  POSITION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP = 9;
}

enum ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMoveConfiguration {
  oneof mode {
  .chesscom.explanation_engine.v1
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02906"></a>
## FND-02906: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_CALM = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

POSITION_SHAPE_CALM = 8;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 402.

```text
 POSITION_SHAPE_SEMI_OPEN = 5;
  POSITION_SHAPE_THREATENED = 6;
  POSITION_SHAPE_THREATENING = 7;
  POSITION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP = 9;
}

enum ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMoveConfiguration {
  oneof mode {
  .chesscom.explanation_engine.v1.AdditiveConfig additive = 5;
  .c
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02907"></a>
## FND-02907: chesscom.explanation_engine.v1.PositionShape.POSITION_SHAPE_SHARP = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

POSITION_SHAPE_SHARP = 9;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 429.

```text
 5;
  POSITION_SHAPE_THREATENED = 6;
  POSITION_SHAPE_THREATENING = 7;
  POSITION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP = 9;
}

enum ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMoveConfiguration {
  oneof mode {
  .chesscom.explanation_engine.v1.AdditiveConfig additive = 5;
  .chesscom.explanation_engine.
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02908"></a>
## FND-02908: enum declaration: chesscom.explanation_engine.v1.ModelArch

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ModelArch {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 458.

```text
ED = 6;
  POSITION_SHAPE_THREATENING = 7;
  POSITION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP = 9;
}

enum ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMoveConfiguration {
  oneof mode {
  .chesscom.explanation_engine.v1.AdditiveConfig additive = 5;
  .chesscom.explanation_engine.v1.NnMultConfig nnmult = 6;
 
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02909"></a>
## FND-02909: chesscom.explanation_engine.v1.ModelArch.MODEL_ARCH_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MODEL_ARCH_UNSPECIFIED = 0;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 477.

```text
SHAPE_THREATENING = 7;
  POSITION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP = 9;
}

enum ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMoveConfiguration {
  oneof mode {
  .chesscom.explanation_engine.v1.AdditiveConfig additive = 5;
  .chesscom.explanation_engine.v1.NnMultConfig nnmult = 6;
  }
  optional strin
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02910"></a>
## FND-02910: chesscom.explanation_engine.v1.ModelArch.MODEL_ARCH_CHARM = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MODEL_ARCH_CHARM = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 507.

```text
ION_SHAPE_CALM = 8;
  POSITION_SHAPE_SHARP = 9;
}

enum ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMoveConfiguration {
  oneof mode {
  .chesscom.explanation_engine.v1.AdditiveConfig additive = 5;
  .chesscom.explanation_engine.v1.NnMultConfig nnmult = 6;
  }
  optional string id = 1;
  optional string na
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02911"></a>
## FND-02911: chesscom.explanation_engine.v1.ModelArch.MODEL_ARCH_CHARM_SMALL = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MODEL_ARCH_CHARM_SMALL = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 531.

```text
SITION_SHAPE_SHARP = 9;
}

enum ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMoveConfiguration {
  oneof mode {
  .chesscom.explanation_engine.v1.AdditiveConfig additive = 5;
  .chesscom.explanation_engine.v1.NnMultConfig nnmult = 6;
  }
  optional string id = 1;
  optional string name = 2;
  optional strin
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02912"></a>
## FND-02912: chesscom.explanation_engine.v1.ModelArch.MODEL_ARCH_MAIA = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MODEL_ARCH_MAIA = 3;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 561.

```text
m ModelArch {
  MODEL_ARCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMoveConfiguration {
  oneof mode {
  .chesscom.explanation_engine.v1.AdditiveConfig additive = 5;
  .chesscom.explanation_engine.v1.NnMultConfig nnmult = 6;
  }
  optional string id = 1;
  optional string name = 2;
  optional string version = 3;
  optional .che
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02913"></a>
## FND-02913: chesscom.explanation_engine.v1.ModelArch.MODEL_ARCH_MAIA3 = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MODEL_ARCH_MAIA3 = 4;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 584.

```text
RCH_UNSPECIFIED = 0;
  MODEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMoveConfiguration {
  oneof mode {
  .chesscom.explanation_engine.v1.AdditiveConfig additive = 5;
  .chesscom.explanation_engine.v1.NnMultConfig nnmult = 6;
  }
  optional string id = 1;
  optional string name = 2;
  optional string version = 3;
  optional .chesscom.explanation_engin
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02914"></a>
## FND-02914: message declaration: chesscom.explanation_engine.v1.BotMoveConfiguration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotMoveConfiguration {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 609.

```text
DEL_ARCH_CHARM = 1;
  MODEL_ARCH_CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMoveConfiguration {
  oneof mode {
  .chesscom.explanation_engine.v1.AdditiveConfig additive = 5;
  .chesscom.explanation_engine.v1.NnMultConfig nnmult = 6;
  }
  optional string id = 1;
  optional string name = 2;
  optional string version = 3;
  optional .chesscom.explanation_engine.v1.BotMoveSettings sett
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02915"></a>
## FND-02915: oneof declaration: chesscom.explanation_engine.v1.BotMoveConfiguration.mode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof mode {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 642.

```text
CHARM_SMALL = 2;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMoveConfiguration {
  oneof mode {
  .chesscom.explanation_engine.v1.AdditiveConfig additive = 5;
  .chesscom.explanation_engine.v1.NnMultConfig nnmult = 6;
  }
  optional string id = 1;
  optional string name = 2;
  optional string version = 3;
  optional .chesscom.explanation_engine.v1.BotMoveSettings settings = 4;
}

message BotMoveSetti
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02916"></a>
## FND-02916: chesscom.explanation_engine.v1.BotMoveConfiguration.additive = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.AdditiveConfig additive = 5;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 657.

```text
;
  MODEL_ARCH_MAIA = 3;
  MODEL_ARCH_MAIA3 = 4;
}

message BotMoveConfiguration {
  oneof mode {
  .chesscom.explanation_engine.v1.AdditiveConfig additive = 5;
  .chesscom.explanation_engine.v1.NnMultConfig nnmult = 6;
  }
  optional string id = 1;
  optional string name = 2;
  optional string version = 3;
  optional .chesscom.explanation_engine.v1.BotMoveSettings settings = 4;
}

message BotMoveSettings {
  oneof s
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02917"></a>
## FND-02917: chesscom.explanation_engine.v1.BotMoveConfiguration.nnmult = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.NnMultConfig nnmult = 6;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 720.

```text
MoveConfiguration {
  oneof mode {
  .chesscom.explanation_engine.v1.AdditiveConfig additive = 5;
  .chesscom.explanation_engine.v1.NnMultConfig nnmult = 6;
  }
  optional string id = 1;
  optional string name = 2;
  optional string version = 3;
  optional .chesscom.explanation_engine.v1.BotMoveSettings settings = 4;
}

message BotMoveSettings {
  oneof search_limit {
  int32 depth = 1;
  int64 nodes = 2;
  }
  oneof
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02918"></a>
## FND-02918: chesscom.explanation_engine.v1.BotMoveConfiguration.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 783.

```text
ne.v1.AdditiveConfig additive = 5;
  .chesscom.explanation_engine.v1.NnMultConfig nnmult = 6;
  }
  optional string id = 1;
  optional string name = 2;
  optional string version = 3;
  optional .chesscom.explanation_engine.v1.BotMoveSettings settings = 4;
}

message BotMoveSettings {
  oneof search_limit {
  int32 depth = 1;
  int64 nodes = 2;
  }
  oneof _book {
  .chesscom.explanation_engine.v1.BookMovesSettings bo
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02919"></a>
## FND-02919: chesscom.explanation_engine.v1.BotMoveConfiguration.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 809.

```text
ive = 5;
  .chesscom.explanation_engine.v1.NnMultConfig nnmult = 6;
  }
  optional string id = 1;
  optional string name = 2;
  optional string version = 3;
  optional .chesscom.explanation_engine.v1.BotMoveSettings settings = 4;
}

message BotMoveSettings {
  oneof search_limit {
  int32 depth = 1;
  int64 nodes = 2;
  }
  oneof _book {
  .chesscom.explanation_engine.v1.BookMovesSettings book = 3;
  }
  oneof _sampl
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02920"></a>
## FND-02920: chesscom.explanation_engine.v1.BotMoveConfiguration.version = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string version = 3;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 837.

```text
tion_engine.v1.NnMultConfig nnmult = 6;
  }
  optional string id = 1;
  optional string name = 2;
  optional string version = 3;
  optional .chesscom.explanation_engine.v1.BotMoveSettings settings = 4;
}

message BotMoveSettings {
  oneof search_limit {
  int32 depth = 1;
  int64 nodes = 2;
  }
  oneof _book {
  .chesscom.explanation_engine.v1.BookMovesSettings book = 3;
  }
  oneof _sampling {
  .chesscom.explanatio
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02921"></a>
## FND-02921: chesscom.explanation_engine.v1.BotMoveConfiguration.settings = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.BotMoveSettings settings = 4;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 868.

```text
ult = 6;
  }
  optional string id = 1;
  optional string name = 2;
  optional string version = 3;
  optional .chesscom.explanation_engine.v1.BotMoveSettings settings = 4;
}

message BotMoveSettings {
  oneof search_limit {
  int32 depth = 1;
  int64 nodes = 2;
  }
  oneof _book {
  .chesscom.explanation_engine.v1.BookMovesSettings book = 3;
  }
  oneof _sampling {
  .chesscom.explanation_engine.v1.SamplingSettings sa
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02922"></a>
## FND-02922: message declaration: chesscom.explanation_engine.v1.BotMoveSettings

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BotMoveSettings {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 942.

```text
nal string version = 3;
  optional .chesscom.explanation_engine.v1.BotMoveSettings settings = 4;
}

message BotMoveSettings {
  oneof search_limit {
  int32 depth = 1;
  int64 nodes = 2;
  }
  oneof _book {
  .chesscom.explanation_engine.v1.BookMovesSettings book = 3;
  }
  oneof _sampling {
  .chesscom.explanation_engine.v1.SamplingSettings sampling = 4;
  }
}

message AdditiveConfig {
  optional int32 n_top_moves =
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02923"></a>
## FND-02923: oneof declaration: chesscom.explanation_engine.v1.BotMoveSettings.search_limit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof search_limit {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 970.

```text
tional .chesscom.explanation_engine.v1.BotMoveSettings settings = 4;
}

message BotMoveSettings {
  oneof search_limit {
  int32 depth = 1;
  int64 nodes = 2;
  }
  oneof _book {
  .chesscom.explanation_engine.v1.BookMovesSettings book = 3;
  }
  oneof _sampling {
  .chesscom.explanation_engine.v1.SamplingSettings sampling = 4;
  }
}

message AdditiveConfig {
  optional int32 n_top_moves = 1;
  optional int32 n_bad_m
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02924"></a>
## FND-02924: chesscom.explanation_engine.v1.BotMoveSettings.depth = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 depth = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 993.

```text
ation_engine.v1.BotMoveSettings settings = 4;
}

message BotMoveSettings {
  oneof search_limit {
  int32 depth = 1;
  int64 nodes = 2;
  }
  oneof _book {
  .chesscom.explanation_engine.v1.BookMovesSettings book = 3;
  }
  oneof _sampling {
  .chesscom.explanation_engine.v1.SamplingSettings sampling = 4;
  }
}

message AdditiveConfig {
  optional int32 n_top_moves = 1;
  optional int32 n_bad_moves = 2;
  optional do
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02925"></a>
## FND-02925: chesscom.explanation_engine.v1.BotMoveSettings.nodes = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 nodes = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1012.

```text
MoveSettings settings = 4;
}

message BotMoveSettings {
  oneof search_limit {
  int32 depth = 1;
  int64 nodes = 2;
  }
  oneof _book {
  .chesscom.explanation_engine.v1.BookMovesSettings book = 3;
  }
  oneof _sampling {
  .chesscom.explanation_engine.v1.SamplingSettings sampling = 4;
  }
}

message AdditiveConfig {
  optional int32 n_top_moves = 1;
  optional int32 n_bad_moves = 2;
  optional double time_taken_mul
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02926"></a>
## FND-02926: oneof declaration: chesscom.explanation_engine.v1.BotMoveSettings._book

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _book {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1035.

```text
 4;
}

message BotMoveSettings {
  oneof search_limit {
  int32 depth = 1;
  int64 nodes = 2;
  }
  oneof _book {
  .chesscom.explanation_engine.v1.BookMovesSettings book = 3;
  }
  oneof _sampling {
  .chesscom.explanation_engine.v1.SamplingSettings sampling = 4;
  }
}

message AdditiveConfig {
  optional int32 n_top_moves = 1;
  optional int32 n_bad_moves = 2;
  optional double time_taken_multiplier = 3;
  repeated
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02927"></a>
## FND-02927: chesscom.explanation_engine.v1.BotMoveSettings.book = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.BookMovesSettings book = 3;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1051.

```text
otMoveSettings {
  oneof search_limit {
  int32 depth = 1;
  int64 nodes = 2;
  }
  oneof _book {
  .chesscom.explanation_engine.v1.BookMovesSettings book = 3;
  }
  oneof _sampling {
  .chesscom.explanation_engine.v1.SamplingSettings sampling = 4;
  }
}

message AdditiveConfig {
  optional int32 n_top_moves = 1;
  optional int32 n_bad_moves = 2;
  optional double time_taken_multiplier = 3;
  repeated .chesscom.expla
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02928"></a>
## FND-02928: oneof declaration: chesscom.explanation_engine.v1.BotMoveSettings._sampling

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _sampling {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1117.

```text
 nodes = 2;
  }
  oneof _book {
  .chesscom.explanation_engine.v1.BookMovesSettings book = 3;
  }
  oneof _sampling {
  .chesscom.explanation_engine.v1.SamplingSettings sampling = 4;
  }
}

message AdditiveConfig {
  optional int32 n_top_moves = 1;
  optional int32 n_bad_moves = 2;
  optional double time_taken_multiplier = 3;
  repeated .chesscom.explanation_engine.v1.AdditiveBehavior behaviors = 4;
}

message NnMult
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02929"></a>
## FND-02929: chesscom.explanation_engine.v1.BotMoveSettings.sampling = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.SamplingSettings sampling = 4;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1137.

```text
eof _book {
  .chesscom.explanation_engine.v1.BookMovesSettings book = 3;
  }
  oneof _sampling {
  .chesscom.explanation_engine.v1.SamplingSettings sampling = 4;
  }
}

message AdditiveConfig {
  optional int32 n_top_moves = 1;
  optional int32 n_bad_moves = 2;
  optional double time_taken_multiplier = 3;
  repeated .chesscom.explanation_engine.v1.AdditiveBehavior behaviors = 4;
}

message NnMultConfig {
  optional 
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02930"></a>
## FND-02930: message declaration: chesscom.explanation_engine.v1.AdditiveConfig

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AdditiveConfig {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1207.

```text
 3;
  }
  oneof _sampling {
  .chesscom.explanation_engine.v1.SamplingSettings sampling = 4;
  }
}

message AdditiveConfig {
  optional int32 n_top_moves = 1;
  optional int32 n_bad_moves = 2;
  optional double time_taken_multiplier = 3;
  repeated .chesscom.explanation_engine.v1.AdditiveBehavior behaviors = 4;
}

message NnMultConfig {
  optional int32 n_top_nn_candidates = 1;
  optional .chesscom.explanation_engine
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02931"></a>
## FND-02931: chesscom.explanation_engine.v1.AdditiveConfig.n_top_moves = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 n_top_moves = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1234.

```text

  .chesscom.explanation_engine.v1.SamplingSettings sampling = 4;
  }
}

message AdditiveConfig {
  optional int32 n_top_moves = 1;
  optional int32 n_bad_moves = 2;
  optional double time_taken_multiplier = 3;
  repeated .chesscom.explanation_engine.v1.AdditiveBehavior behaviors = 4;
}

message NnMultConfig {
  optional int32 n_top_nn_candidates = 1;
  optional .chesscom.explanation_engine.v1.NnConfig nn = 2;
  repe
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02932"></a>
## FND-02932: chesscom.explanation_engine.v1.AdditiveConfig.n_bad_moves = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 n_bad_moves = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1268.

```text
.SamplingSettings sampling = 4;
  }
}

message AdditiveConfig {
  optional int32 n_top_moves = 1;
  optional int32 n_bad_moves = 2;
  optional double time_taken_multiplier = 3;
  repeated .chesscom.explanation_engine.v1.AdditiveBehavior behaviors = 4;
}

message NnMultConfig {
  optional int32 n_top_nn_candidates = 1;
  optional .chesscom.explanation_engine.v1.NnConfig nn = 2;
  repeated .chesscom.explanation_engine.
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02933"></a>
## FND-02933: chesscom.explanation_engine.v1.AdditiveConfig.time_taken_multiplier = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double time_taken_multiplier = 3;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1302.

```text
}
}

message AdditiveConfig {
  optional int32 n_top_moves = 1;
  optional int32 n_bad_moves = 2;
  optional double time_taken_multiplier = 3;
  repeated .chesscom.explanation_engine.v1.AdditiveBehavior behaviors = 4;
}

message NnMultConfig {
  optional int32 n_top_nn_candidates = 1;
  optional .chesscom.explanation_engine.v1.NnConfig nn = 2;
  repeated .chesscom.explanation_engine.v1.NnMultBehavior behaviors = 3;
}
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02934"></a>
## FND-02934: chesscom.explanation_engine.v1.AdditiveConfig.behaviors = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.AdditiveBehavior behaviors = 4;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1347.

```text
2 n_top_moves = 1;
  optional int32 n_bad_moves = 2;
  optional double time_taken_multiplier = 3;
  repeated .chesscom.explanation_engine.v1.AdditiveBehavior behaviors = 4;
}

message NnMultConfig {
  optional int32 n_top_nn_candidates = 1;
  optional .chesscom.explanation_engine.v1.NnConfig nn = 2;
  repeated .chesscom.explanation_engine.v1.NnMultBehavior behaviors = 3;
}

message BookMovesSettings {
  optional stri
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02935"></a>
## FND-02935: message declaration: chesscom.explanation_engine.v1.NnMultConfig

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NnMultConfig {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1423.

```text
taken_multiplier = 3;
  repeated .chesscom.explanation_engine.v1.AdditiveBehavior behaviors = 4;
}

message NnMultConfig {
  optional int32 n_top_nn_candidates = 1;
  optional .chesscom.explanation_engine.v1.NnConfig nn = 2;
  repeated .chesscom.explanation_engine.v1.NnMultBehavior behaviors = 3;
}

message BookMovesSettings {
  optional string name = 1;
  optional int32 move_count = 2;
}

message SamplingSettings {

```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02936"></a>
## FND-02936: chesscom.explanation_engine.v1.NnMultConfig.n_top_nn_candidates = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 n_top_nn_candidates = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1448.

```text
epeated .chesscom.explanation_engine.v1.AdditiveBehavior behaviors = 4;
}

message NnMultConfig {
  optional int32 n_top_nn_candidates = 1;
  optional .chesscom.explanation_engine.v1.NnConfig nn = 2;
  repeated .chesscom.explanation_engine.v1.NnMultBehavior behaviors = 3;
}

message BookMovesSettings {
  optional string name = 1;
  optional int32 move_count = 2;
}

message SamplingSettings {
  optional double probabi
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02937"></a>
## FND-02937: chesscom.explanation_engine.v1.NnMultConfig.nn = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.NnConfig nn = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1490.

```text
ditiveBehavior behaviors = 4;
}

message NnMultConfig {
  optional int32 n_top_nn_candidates = 1;
  optional .chesscom.explanation_engine.v1.NnConfig nn = 2;
  repeated .chesscom.explanation_engine.v1.NnMultBehavior behaviors = 3;
}

message BookMovesSettings {
  optional string name = 1;
  optional int32 move_count = 2;
}

message SamplingSettings {
  optional double probability_threshold = 1;
}

message AdditiveBeh
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02938"></a>
## FND-02938: chesscom.explanation_engine.v1.NnMultConfig.behaviors = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.NnMultBehavior behaviors = 3;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1550.

```text
tional int32 n_top_nn_candidates = 1;
  optional .chesscom.explanation_engine.v1.NnConfig nn = 2;
  repeated .chesscom.explanation_engine.v1.NnMultBehavior behaviors = 3;
}

message BookMovesSettings {
  optional string name = 1;
  optional int32 move_count = 2;
}

message SamplingSettings {
  optional double probability_threshold = 1;
}

message AdditiveBehavior {
  oneof _max_eval_drop {
  .chesscom.explanation_eng
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02939"></a>
## FND-02939: message declaration: chesscom.explanation_engine.v1.BookMovesSettings

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BookMovesSettings {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1624.

```text
ine.v1.NnConfig nn = 2;
  repeated .chesscom.explanation_engine.v1.NnMultBehavior behaviors = 3;
}

message BookMovesSettings {
  optional string name = 1;
  optional int32 move_count = 2;
}

message SamplingSettings {
  optional double probability_threshold = 1;
}

message AdditiveBehavior {
  oneof _max_eval_drop {
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .ch
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02940"></a>
## FND-02940: chesscom.explanation_engine.v1.BookMovesSettings.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1654.

```text
ated .chesscom.explanation_engine.v1.NnMultBehavior behaviors = 3;
}

message BookMovesSettings {
  optional string name = 1;
  optional int32 move_count = 2;
}

message SamplingSettings {
  optional double probability_threshold = 1;
}

message AdditiveBehavior {
  oneof _max_eval_drop {
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.E
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02941"></a>
## FND-02941: chesscom.explanation_engine.v1.BookMovesSettings.move_count = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 move_count = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1682.

```text
ngine.v1.NnMultBehavior behaviors = 3;
}

message BookMovesSettings {
  optional string name = 1;
  optional int32 move_count = 2;
}

message SamplingSettings {
  optional double probability_threshold = 1;
}

message AdditiveBehavior {
  oneof _max_eval_drop {
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.EvalThreshold max_advantage =
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02942"></a>
## FND-02942: message declaration: chesscom.explanation_engine.v1.SamplingSettings

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SamplingSettings {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1716.

```text
= 3;
}

message BookMovesSettings {
  optional string name = 1;
  optional int32 move_count = 2;
}

message SamplingSettings {
  optional double probability_threshold = 1;
}

message AdditiveBehavior {
  oneof _max_eval_drop {
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.EvalThreshold max_advantage = 7;
  }
  oneof _legacy_bot {
  .c
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02943"></a>
## FND-02943: chesscom.explanation_engine.v1.SamplingSettings.probability_threshold = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double probability_threshold = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1745.

```text
ings {
  optional string name = 1;
  optional int32 move_count = 2;
}

message SamplingSettings {
  optional double probability_threshold = 1;
}

message AdditiveBehavior {
  oneof _max_eval_drop {
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.EvalThreshold max_advantage = 7;
  }
  oneof _legacy_bot {
  .chesscom.explanation_engine.v1
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02944"></a>
## FND-02944: message declaration: chesscom.explanation_engine.v1.AdditiveBehavior

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AdditiveBehavior {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1791.

```text
int32 move_count = 2;
}

message SamplingSettings {
  optional double probability_threshold = 1;
}

message AdditiveBehavior {
  oneof _max_eval_drop {
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.EvalThreshold max_advantage = 7;
  }
  oneof _legacy_bot {
  .chesscom.explanation_engine.v1.LegacyBot legacy_bot = 9;
  }
  oneof _nn {
 
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02945"></a>
## FND-02945: oneof declaration: chesscom.explanation_engine.v1.AdditiveBehavior._max_eval_drop

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_eval_drop {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1820.

```text
age SamplingSettings {
  optional double probability_threshold = 1;
}

message AdditiveBehavior {
  oneof _max_eval_drop {
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.EvalThreshold max_advantage = 7;
  }
  oneof _legacy_bot {
  .chesscom.explanation_engine.v1.LegacyBot legacy_bot = 9;
  }
  oneof _nn {
  .chesscom.explanation_engine
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02946"></a>
## FND-02946: chesscom.explanation_engine.v1.AdditiveBehavior.max_eval_drop = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1845.

```text
optional double probability_threshold = 1;
}

message AdditiveBehavior {
  oneof _max_eval_drop {
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.EvalThreshold max_advantage = 7;
  }
  oneof _legacy_bot {
  .chesscom.explanation_engine.v1.LegacyBot legacy_bot = 9;
  }
  oneof _nn {
  .chesscom.explanation_engine.v1.NnConfig nn = 10;
  }
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02947"></a>
## FND-02947: oneof declaration: chesscom.explanation_engine.v1.AdditiveBehavior._max_advantage

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_advantage {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1916.

```text
{
  oneof _max_eval_drop {
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.EvalThreshold max_advantage = 7;
  }
  oneof _legacy_bot {
  .chesscom.explanation_engine.v1.LegacyBot legacy_bot = 9;
  }
  oneof _nn {
  .chesscom.explanation_engine.v1.NnConfig nn = 10;
  }
  oneof _coherence {
  .chesscom.explanation_engine.v1.CoherenceConfig
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02948"></a>
## FND-02948: chesscom.explanation_engine.v1.AdditiveBehavior.max_advantage = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.EvalThreshold max_advantage = 7;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1941.

```text
{
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.EvalThreshold max_advantage = 7;
  }
  oneof _legacy_bot {
  .chesscom.explanation_engine.v1.LegacyBot legacy_bot = 9;
  }
  oneof _nn {
  .chesscom.explanation_engine.v1.NnConfig nn = 10;
  }
  oneof _coherence {
  .chesscom.explanation_engine.v1.CoherenceConfig coherence = 11;
  }
  op
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02949"></a>
## FND-02949: oneof declaration: chesscom.explanation_engine.v1.AdditiveBehavior._legacy_bot

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _legacy_bot {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2012.

```text
}
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.EvalThreshold max_advantage = 7;
  }
  oneof _legacy_bot {
  .chesscom.explanation_engine.v1.LegacyBot legacy_bot = 9;
  }
  oneof _nn {
  .chesscom.explanation_engine.v1.NnConfig nn = 10;
  }
  oneof _coherence {
  .chesscom.explanation_engine.v1.CoherenceConfig coherence = 11;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double 
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02950"></a>
## FND-02950: chesscom.explanation_engine.v1.AdditiveBehavior.legacy_bot = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.LegacyBot legacy_bot = 9;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2034.

```text
ge {
  .chesscom.explanation_engine.v1.EvalThreshold max_advantage = 7;
  }
  oneof _legacy_bot {
  .chesscom.explanation_engine.v1.LegacyBot legacy_bot = 9;
  }
  oneof _nn {
  .chesscom.explanation_engine.v1.NnConfig nn = 10;
  }
  oneof _coherence {
  .chesscom.explanation_engine.v1.CoherenceConfig coherence = 11;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02951"></a>
## FND-02951: oneof declaration: chesscom.explanation_engine.v1.AdditiveBehavior._nn

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _nn {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2098.

```text
ge = 7;
  }
  oneof _legacy_bot {
  .chesscom.explanation_engine.v1.LegacyBot legacy_bot = 9;
  }
  oneof _nn {
  .chesscom.explanation_engine.v1.NnConfig nn = 10;
  }
  oneof _coherence {
  .chesscom.explanation_engine.v1.CoherenceConfig coherence = 11;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 4;
  repeat
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02952"></a>
## FND-02952: chesscom.explanation_engine.v1.AdditiveBehavior.nn = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.NnConfig nn = 10;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2112.

```text
oneof _legacy_bot {
  .chesscom.explanation_engine.v1.LegacyBot legacy_bot = 9;
  }
  oneof _nn {
  .chesscom.explanation_engine.v1.NnConfig nn = 10;
  }
  oneof _coherence {
  .chesscom.explanation_engine.v1.CoherenceConfig coherence = 11;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 4;
  repeated .chesscom.e
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02953"></a>
## FND-02953: oneof declaration: chesscom.explanation_engine.v1.AdditiveBehavior._coherence

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _coherence {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2168.

```text
gacyBot legacy_bot = 9;
  }
  oneof _nn {
  .chesscom.explanation_engine.v1.NnConfig nn = 10;
  }
  oneof _coherence {
  .chesscom.explanation_engine.v1.CoherenceConfig coherence = 11;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 4;
  repeated .chesscom.explanation_engine.v1.PieceBonus piece_bonuses = 5;
  opt
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02954"></a>
## FND-02954: chesscom.explanation_engine.v1.AdditiveBehavior.coherence = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.explanation_engine.v1.CoherenceConfig coherence = 11;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2189.

```text
9;
  }
  oneof _nn {
  .chesscom.explanation_engine.v1.NnConfig nn = 10;
  }
  oneof _coherence {
  .chesscom.explanation_engine.v1.CoherenceConfig coherence = 11;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 4;
  repeated .chesscom.explanation_engine.v1.PieceBonus piece_bonuses = 5;
  optional .chesscom.expla
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02955"></a>
## FND-02955: chesscom.explanation_engine.v1.AdditiveBehavior.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1654.

```text
ated .chesscom.explanation_engine.v1.NnMultBehavior behaviors = 3;
}

message BookMovesSettings {
  optional string name = 1;
  optional int32 move_count = 2;
}

message SamplingSettings {
  optional double probability_threshold = 1;
}

message AdditiveBehavior {
  oneof _max_eval_drop {
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.E
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02956"></a>
## FND-02956: chesscom.explanation_engine.v1.AdditiveBehavior.enabled = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enabled = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2287.

```text
  .chesscom.explanation_engine.v1.CoherenceConfig coherence = 11;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 4;
  repeated .chesscom.explanation_engine.v1.PieceBonus piece_bonuses = 5;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 8;
}

message NnMultBehavior {
  oneof _max_eval
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02957"></a>
## FND-02957: chesscom.explanation_engine.v1.AdditiveBehavior.weight = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double weight = 3;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2316.

```text
e.v1.CoherenceConfig coherence = 11;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 4;
  repeated .chesscom.explanation_engine.v1.PieceBonus piece_bonuses = 5;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 8;
}

message NnMultBehavior {
  oneof _max_eval_drop {
  int32 max_eval_drop
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02958"></a>
## FND-02958: chesscom.explanation_engine.v1.AdditiveBehavior.rules = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.MatcherRule rules = 4;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2346.

```text
 = 11;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 4;
  repeated .chesscom.explanation_engine.v1.PieceBonus piece_bonuses = 5;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 8;
}

message NnMultBehavior {
  oneof _max_eval_drop {
  int32 max_eval_drop = 5;
  }
  oneof _max_advanta
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02959"></a>
## FND-02959: chesscom.explanation_engine.v1.AdditiveBehavior.piece_bonuses = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.PieceBonus piece_bonuses = 5;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2412.

```text
;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 4;
  repeated .chesscom.explanation_engine.v1.PieceBonus piece_bonuses = 5;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 8;
}

message NnMultBehavior {
  oneof _max_eval_drop {
  int32 max_eval_drop = 5;
  }
  oneof _max_advantage {
  int32 max_advantage = 6;
  }
  optional string name = 1;
  
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02960"></a>
## FND-02960: chesscom.explanation_engine.v1.AdditiveBehavior.context = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 8;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2485.

```text
1.MatcherRule rules = 4;
  repeated .chesscom.explanation_engine.v1.PieceBonus piece_bonuses = 5;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 8;
}

message NnMultBehavior {
  oneof _max_eval_drop {
  int32 max_eval_drop = 5;
  }
  oneof _max_advantage {
  int32 max_advantage = 6;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .ches
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02961"></a>
## FND-02961: message declaration: chesscom.explanation_engine.v1.NnMultBehavior

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NnMultBehavior {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2565.

```text
iece_bonuses = 5;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 8;
}

message NnMultBehavior {
  oneof _max_eval_drop {
  int32 max_eval_drop = 5;
  }
  oneof _max_advantage {
  int32 max_advantage = 6;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.NnMultRule rules = 4;
  optional .chesscom.explanatio
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02962"></a>
## FND-02962: oneof declaration: chesscom.explanation_engine.v1.NnMultBehavior._max_eval_drop

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_eval_drop {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1820.

```text
age SamplingSettings {
  optional double probability_threshold = 1;
}

message AdditiveBehavior {
  oneof _max_eval_drop {
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.EvalThreshold max_advantage = 7;
  }
  oneof _legacy_bot {
  .chesscom.explanation_engine.v1.LegacyBot legacy_bot = 9;
  }
  oneof _nn {
  .chesscom.explanation_engine
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02963"></a>
## FND-02963: chesscom.explanation_engine.v1.NnMultBehavior.max_eval_drop = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max_eval_drop = 5;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2617.

```text
ngine.v1.BotMoveBehaviorContext context = 8;
}

message NnMultBehavior {
  oneof _max_eval_drop {
  int32 max_eval_drop = 5;
  }
  oneof _max_advantage {
  int32 max_advantage = 6;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.NnMultRule rules = 4;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 7;
}

m
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02964"></a>
## FND-02964: oneof declaration: chesscom.explanation_engine.v1.NnMultBehavior._max_advantage

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_advantage {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1916.

```text
{
  oneof _max_eval_drop {
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.EvalThreshold max_advantage = 7;
  }
  oneof _legacy_bot {
  .chesscom.explanation_engine.v1.LegacyBot legacy_bot = 9;
  }
  oneof _nn {
  .chesscom.explanation_engine.v1.NnConfig nn = 10;
  }
  oneof _coherence {
  .chesscom.explanation_engine.v1.CoherenceConfig
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02965"></a>
## FND-02965: chesscom.explanation_engine.v1.NnMultBehavior.max_advantage = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max_advantage = 6;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2673.

```text
NnMultBehavior {
  oneof _max_eval_drop {
  int32 max_eval_drop = 5;
  }
  oneof _max_advantage {
  int32 max_advantage = 6;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.NnMultRule rules = 4;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 7;
}

message MatcherRule {
  oneof _weight {
  double weight =
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02966"></a>
## FND-02966: chesscom.explanation_engine.v1.NnMultBehavior.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 1654.

```text
ated .chesscom.explanation_engine.v1.NnMultBehavior behaviors = 3;
}

message BookMovesSettings {
  optional string name = 1;
  optional int32 move_count = 2;
}

message SamplingSettings {
  optional double probability_threshold = 1;
}

message AdditiveBehavior {
  oneof _max_eval_drop {
  .chesscom.explanation_engine.v1.EvalThreshold max_eval_drop = 6;
  }
  oneof _max_advantage {
  .chesscom.explanation_engine.v1.E
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02967"></a>
## FND-02967: chesscom.explanation_engine.v1.NnMultBehavior.enabled = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool enabled = 2;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2287.

```text
  .chesscom.explanation_engine.v1.CoherenceConfig coherence = 11;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 4;
  repeated .chesscom.explanation_engine.v1.PieceBonus piece_bonuses = 5;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 8;
}

message NnMultBehavior {
  oneof _max_eval
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02968"></a>
## FND-02968: chesscom.explanation_engine.v1.NnMultBehavior.weight = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double weight = 3;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2316.

```text
e.v1.CoherenceConfig coherence = 11;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.MatcherRule rules = 4;
  repeated .chesscom.explanation_engine.v1.PieceBonus piece_bonuses = 5;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 8;
}

message NnMultBehavior {
  oneof _max_eval_drop {
  int32 max_eval_drop
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02969"></a>
## FND-02969: chesscom.explanation_engine.v1.NnMultBehavior.rules = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.NnMultRule rules = 4;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2791.

```text
e = 6;
  }
  optional string name = 1;
  optional bool enabled = 2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.NnMultRule rules = 4;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 7;
}

message MatcherRule {
  oneof _weight {
  double weight = 4;
  }
  repeated .chesscom.explanation_engine.v1.Circumstance circumstances = 1;
  repeated .chesscom.explanation_en
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02970"></a>
## FND-02970: chesscom.explanation_engine.v1.NnMultBehavior.context = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 7;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2856.

```text
2;
  optional double weight = 3;
  repeated .chesscom.explanation_engine.v1.NnMultRule rules = 4;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 7;
}

message MatcherRule {
  oneof _weight {
  double weight = 4;
  }
  repeated .chesscom.explanation_engine.v1.Circumstance circumstances = 1;
  repeated .chesscom.explanation_engine.v1.AnalysisType tags = 2;
  repeated .chesscom.explanation_e
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02971"></a>
## FND-02971: message declaration: chesscom.explanation_engine.v1.MatcherRule

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MatcherRule {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2936.

```text
ltRule rules = 4;
  optional .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 7;
}

message MatcherRule {
  oneof _weight {
  double weight = 4;
  }
  repeated .chesscom.explanation_engine.v1.Circumstance circumstances = 1;
  repeated .chesscom.explanation_engine.v1.AnalysisType tags = 2;
  repeated .chesscom.explanation_engine.v1.MoveClassification move_classifications = 3;
}

message NnMultRule {
  
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02972"></a>
## FND-02972: oneof declaration: chesscom.explanation_engine.v1.MatcherRule._weight

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _weight {

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2960.

```text
onal .chesscom.explanation_engine.v1.BotMoveBehaviorContext context = 7;
}

message MatcherRule {
  oneof _weight {
  double weight = 4;
  }
  repeated .chesscom.explanation_engine.v1.Circumstance circumstances = 1;
  repeated .chesscom.explanation_engine.v1.AnalysisType tags = 2;
  repeated .chesscom.explanation_engine.v1.MoveClassification move_classifications = 3;
}

message NnMultRule {
  oneof body {
  .chesscom
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02973"></a>
## FND-02973: chesscom.explanation_engine.v1.MatcherRule.weight = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double weight = 4;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 2978.

```text
lanation_engine.v1.BotMoveBehaviorContext context = 7;
}

message MatcherRule {
  oneof _weight {
  double weight = 4;
  }
  repeated .chesscom.explanation_engine.v1.Circumstance circumstances = 1;
  repeated .chesscom.explanation_engine.v1.AnalysisType tags = 2;
  repeated .chesscom.explanation_engine.v1.MoveClassification move_classifications = 3;
}

message NnMultRule {
  oneof body {
  .chesscom.explanation_engin
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02974"></a>
## FND-02974: chesscom.explanation_engine.v1.MatcherRule.circumstances = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.Circumstance circumstances = 1;

### Evidence

- **SRC-0339** `research/proto/chesscom/explanation_engine/v1/bot_move_configuration.proto` — [preserved redacted evidence](../evidence/text/37de2a1a8b9bcb2189bfe0e57362ba0ac4d9a375a77ac7e47bdf8cf005d0b9e9.proto)
  Character offset 3003.

```text
eBehaviorContext context = 7;
}

message MatcherRule {
  oneof _weight {
  double weight = 4;
  }
  repeated .chesscom.explanation_engine.v1.Circumstance circumstances = 1;
  repeated .chesscom.explanation_engine.v1.AnalysisType tags = 2;
  repeated .chesscom.explanation_engine.v1.MoveClassification move_classifications = 3;
}

message NnMultRule {
  oneof body {
  .chesscom.explanation_engine.v1.PieceGate pieces = 1
```

**Source references:** SRC-0339, SRC-1310  
**URL references:** None independently associated  
**Related findings:** FND-02897, FND-02898, FND-02899

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
