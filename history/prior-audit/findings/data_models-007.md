# data_models — findings 601–700

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-00875"></a>
## FND-00875: chesscom.ceac.v2.GameReviewResponse.failure = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.GameReviewResponseFailure failure = 3;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 939.

```text
meReviewResponseProgress progress = 1;
  .chesscom.ceac.v2.GameReviewResponseSuccess success = 2;
  .chesscom.ceac.v2.GameReviewResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message GameReviewResponseSuccess {
  optional .chesscom.explanation_engine.v1.GameReview game_review = 2;
  repeated string cee_c_api_calls = 100
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00876"></a>
## FND-00876: chesscom.ceac.v2.GameReviewResponse.heartbeat = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.Heartbeat heartbeat = 4;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 998.

```text
GameReviewResponseSuccess success = 2;
  .chesscom.ceac.v2.GameReviewResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message GameReviewResponseSuccess {
  optional .chesscom.explanation_engine.v1.GameReview game_review = 2;
  repeated string cee_c_api_calls = 100;
}

message GameReviewResponseProgress {
  optional float 
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00877"></a>
## FND-00877: chesscom.ceac.v2.GameReviewResponse.waiting_for_capacity = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 1043.

```text
sscom.ceac.v2.GameReviewResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message GameReviewResponseSuccess {
  optional .chesscom.explanation_engine.v1.GameReview game_review = 2;
  repeated string cee_c_api_calls = 100;
}

message GameReviewResponseProgress {
  optional float progress = 1;
}

message GameReviewResponseFa
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00878"></a>
## FND-00878: message declaration: chesscom.ceac.v2.GameReviewResponseSuccess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewResponseSuccess {

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 1113.

```text
v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message GameReviewResponseSuccess {
  optional .chesscom.explanation_engine.v1.GameReview game_review = 2;
  repeated string cee_c_api_calls = 100;
}

message GameReviewResponseProgress {
  optional float progress = 1;
}

message GameReviewResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_g
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00879"></a>
## FND-00879: chesscom.ceac.v2.GameReviewResponseSuccess.game_review = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.GameReview game_review = 2;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 1151.

```text
m.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message GameReviewResponseSuccess {
  optional .chesscom.explanation_engine.v1.GameReview game_review = 2;
  repeated string cee_c_api_calls = 100;
}

message GameReviewResponseProgress {
  optional float progress = 1;
}

message GameReviewResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.Gen
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00880"></a>
## FND-00880: chesscom.ceac.v2.GameReviewResponseSuccess.cee_c_api_calls = 100

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string cee_c_api_calls = 100;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 1222.

```text
ameReviewResponseSuccess {
  optional .chesscom.explanation_engine.v1.GameReview game_review = 2;
  repeated string cee_c_api_calls = 100;
}

message GameReviewResponseProgress {
  optional float progress = 1;
}

message GameReviewResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  option
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00881"></a>
## FND-00881: message declaration: chesscom.ceac.v2.GameReviewResponseProgress

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewResponseProgress {

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 1264.

```text
sscom.explanation_engine.v1.GameReview game_review = 2;
  repeated string cee_c_api_calls = 100;
}

message GameReviewResponseProgress {
  optional float progress = 1;
}

message GameReviewResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_
```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00882"></a>
## FND-00882: chesscom.ceac.v2.GameReviewResponseProgress.progress = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float progress = 1;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 1303.

```text
game_review = 2;
  repeated string cee_c_api_calls = 100;
}

message GameReviewResponseProgress {
  optional float progress = 1;
}

message GameReviewResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_error = 5;
}

```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00883"></a>
## FND-00883: message declaration: chesscom.ceac.v2.GameReviewResponseFailure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewResponseFailure {

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 1335.

```text
ng cee_c_api_calls = 100;
}

message GameReviewResponseProgress {
  optional float progress = 1;
}

message GameReviewResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_error = 5;
}

```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00884"></a>
## FND-00884: oneof declaration: chesscom.ceac.v2.GameReviewResponseFailure.error

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof error {

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 1373.

```text
ameReviewResponseProgress {
  optional float progress = 1;
}

message GameReviewResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_error = 5;
}

```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00885"></a>
## FND-00885: chesscom.ceac.v2.GameReviewResponseFailure.invalid_game_error = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 1389.

```text
eProgress {
  optional float progress = 1;
}

message GameReviewResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_error = 5;
}

```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00886"></a>
## FND-00886: chesscom.ceac.v2.GameReviewResponseFailure.general_error = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.GeneralError general_error = 4;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 1450.

```text
iewResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_error = 5;
}

```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00887"></a>
## FND-00887: chesscom.ceac.v2.GameReviewResponseFailure.reason = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string reason = 1;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 1506.

```text
.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_error = 5;
}

```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00888"></a>
## FND-00888: chesscom.ceac.v2.GameReviewResponseFailure.failure_error = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ceac.v2.FailureError failure_error = 5;

### Evidence

- **SRC-0233** `research/proto/chesscom/ceac/v2/game_review.proto` — [preserved redacted evidence](../evidence/text/c8f3d838115abd37c8dc241cfc87a38f8a7aeef43a1aa1b18388cf263ebb831d.proto)
  Character offset 1536.

```text
_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_error = 5;
}

```

**Source references:** SRC-0233, SRC-1204  
**URL references:** None independently associated  
**Related findings:** FND-00861, FND-00862, FND-00863

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00889"></a>
## FND-00889: message declaration: chesscom.ceac.v2.GameReviewOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewOptions {

### Evidence

- **SRC-0234** `research/proto/chesscom/ceac/v2/game_review_options.proto` — [preserved redacted evidence](../evidence/text/36d89fcc3cceedfb639e5687b45012816e4fc7c3babb08eb2fde41aa29afca93.proto)
  Character offset 100.

```text
// source: chesscom/ceac/v2/game_review_options.proto
// syntax: proto3

package chesscom.ceac.v2;

message GameReviewOptions {
  optional bool report_card_entitled = 1;
  optional bool include_train_takeaways = 2;
  optional bool can_access_locked_takeaways = 3;
}

```

**Source references:** SRC-0234, SRC-1205  
**URL references:** None independently associated  
**Related findings:** FND-00890, FND-00891

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00890"></a>
## FND-00890: chesscom.ceac.v2.GameReviewOptions.report_card_entitled = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool report_card_entitled = 1;

### Evidence

- **SRC-0234** `research/proto/chesscom/ceac/v2/game_review_options.proto` — [preserved redacted evidence](../evidence/text/36d89fcc3cceedfb639e5687b45012816e4fc7c3babb08eb2fde41aa29afca93.proto)
  Character offset 130.

```text
me_review_options.proto
// syntax: proto3

package chesscom.ceac.v2;

message GameReviewOptions {
  optional bool report_card_entitled = 1;
  optional bool include_train_takeaways = 2;
  optional bool can_access_locked_takeaways = 3;
}

```

**Source references:** SRC-0234, SRC-1205  
**URL references:** None independently associated  
**Related findings:** FND-00889, FND-00891

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00891"></a>
## FND-00891: chesscom.ceac.v2.GameReviewOptions.include_train_takeaways = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool include_train_takeaways = 2;

### Evidence

- **SRC-0234** `research/proto/chesscom/ceac/v2/game_review_options.proto` — [preserved redacted evidence](../evidence/text/36d89fcc3cceedfb639e5687b45012816e4fc7c3babb08eb2fde41aa29afca93.proto)
  Character offset 172.

```text

package chesscom.ceac.v2;

message GameReviewOptions {
  optional bool report_card_entitled = 1;
  optional bool include_train_takeaways = 2;
  optional bool can_access_locked_takeaways = 3;
}

```

**Source references:** SRC-0234, SRC-1205  
**URL references:** None independently associated  
**Related findings:** FND-00889, FND-00890

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00892"></a>
## FND-00892: chesscom.ceac.v2.GameReviewOptions.can_access_locked_takeaways = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool can_access_locked_takeaways = 3;

### Evidence

- **SRC-0234** `research/proto/chesscom/ceac/v2/game_review_options.proto` — [preserved redacted evidence](../evidence/text/36d89fcc3cceedfb639e5687b45012816e4fc7c3babb08eb2fde41aa29afca93.proto)
  Character offset 217.

```text
wOptions {
  optional bool report_card_entitled = 1;
  optional bool include_train_takeaways = 2;
  optional bool can_access_locked_takeaways = 3;
}

```

**Source references:** SRC-0234, SRC-1205  
**URL references:** None independently associated  
**Related findings:** FND-00889, FND-00890, FND-00891

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00893"></a>
## FND-00893: message declaration: chesscom.ceac.v2.Heartbeat

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Heartbeat {

### Evidence

- **SRC-0235** `research/proto/chesscom/ceac/v2/heartbeat.proto` — [preserved redacted evidence](../evidence/text/53389449021b87c74ef9b9f455f8d935288c184b5cd17060ead8011cfc78b373.proto)
  Character offset 90.

```text
// source: chesscom/ceac/v2/heartbeat.proto
// syntax: proto3

package chesscom.ceac.v2;

message Heartbeat {
}

```

**Source references:** SRC-0235, SRC-1206  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00894"></a>
## FND-00894: message declaration: chesscom.ceac.v2.RequestMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RequestMetadata {

### Evidence

- **SRC-0236** `research/proto/chesscom/ceac/v2/request_metadata.proto` — [preserved redacted evidence](../evidence/text/2ba131aa5dbf7b9e7dd2324e1ab880badf1781688cbd86433177d34611b2547f.proto)
  Character offset 97.

```text
// source: chesscom/ceac/v2/request_metadata.proto
// syntax: proto3

package chesscom.ceac.v2;

message RequestMetadata {
  optional .chesscom.ceac.v2.Client client = 1;
  optional .chesscom.ceac.v2.Product product = 2;
  optional .google.protobuf.Timestamp received_time = 3;
  optional bool debug_mode = 4;
}

message RequestOptions {
  optional int32 heartbeat_interval_seconds = 4;
  optional bool use_progress_u
```

**Source references:** SRC-0236, SRC-1207  
**URL references:** None independently associated  
**Related findings:** FND-00895, FND-00896

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00895"></a>
## FND-00895: chesscom.ceac.v2.RequestMetadata.client = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ceac.v2.Client client = 1;

### Evidence

- **SRC-0236** `research/proto/chesscom/ceac/v2/request_metadata.proto` — [preserved redacted evidence](../evidence/text/2ba131aa5dbf7b9e7dd2324e1ab880badf1781688cbd86433177d34611b2547f.proto)
  Character offset 125.

```text
v2/request_metadata.proto
// syntax: proto3

package chesscom.ceac.v2;

message RequestMetadata {
  optional .chesscom.ceac.v2.Client client = 1;
  optional .chesscom.ceac.v2.Product product = 2;
  optional .google.protobuf.Timestamp received_time = 3;
  optional bool debug_mode = 4;
}

message RequestOptions {
  optional int32 heartbeat_interval_seconds = 4;
  optional bool use_progress_updates = 5;
}

```

**Source references:** SRC-0236, SRC-1207  
**URL references:** None independently associated  
**Related findings:** FND-00894, FND-00896

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00896"></a>
## FND-00896: chesscom.ceac.v2.RequestMetadata.product = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ceac.v2.Product product = 2;

### Evidence

- **SRC-0236** `research/proto/chesscom/ceac/v2/request_metadata.proto` — [preserved redacted evidence](../evidence/text/2ba131aa5dbf7b9e7dd2324e1ab880badf1781688cbd86433177d34611b2547f.proto)
  Character offset 173.

```text
kage chesscom.ceac.v2;

message RequestMetadata {
  optional .chesscom.ceac.v2.Client client = 1;
  optional .chesscom.ceac.v2.Product product = 2;
  optional .google.protobuf.Timestamp received_time = 3;
  optional bool debug_mode = 4;
}

message RequestOptions {
  optional int32 heartbeat_interval_seconds = 4;
  optional bool use_progress_updates = 5;
}

```

**Source references:** SRC-0236, SRC-1207  
**URL references:** None independently associated  
**Related findings:** FND-00894, FND-00895

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00897"></a>
## FND-00897: chesscom.ceac.v2.RequestMetadata.received_time = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp received_time = 3;

### Evidence

- **SRC-0236** `research/proto/chesscom/ceac/v2/request_metadata.proto` — [preserved redacted evidence](../evidence/text/2ba131aa5dbf7b9e7dd2324e1ab880badf1781688cbd86433177d34611b2547f.proto)
  Character offset 223.

```text
  optional .chesscom.ceac.v2.Client client = 1;
  optional .chesscom.ceac.v2.Product product = 2;
  optional .google.protobuf.Timestamp received_time = 3;
  optional bool debug_mode = 4;
}

message RequestOptions {
  optional int32 heartbeat_interval_seconds = 4;
  optional bool use_progress_updates = 5;
}

```

**Source references:** SRC-0236, SRC-1207  
**URL references:** None independently associated  
**Related findings:** FND-00894, FND-00895, FND-00896

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00898"></a>
## FND-00898: chesscom.ceac.v2.RequestMetadata.debug_mode = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool debug_mode = 4;

### Evidence

- **SRC-0236** `research/proto/chesscom/ceac/v2/request_metadata.proto` — [preserved redacted evidence](../evidence/text/2ba131aa5dbf7b9e7dd2324e1ab880badf1781688cbd86433177d34611b2547f.proto)
  Character offset 280.

```text
l .chesscom.ceac.v2.Product product = 2;
  optional .google.protobuf.Timestamp received_time = 3;
  optional bool debug_mode = 4;
}

message RequestOptions {
  optional int32 heartbeat_interval_seconds = 4;
  optional bool use_progress_updates = 5;
}

```

**Source references:** SRC-0236, SRC-1207  
**URL references:** None independently associated  
**Related findings:** FND-00894, FND-00895, FND-00896

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00899"></a>
## FND-00899: message declaration: chesscom.ceac.v2.RequestOptions

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RequestOptions {

### Evidence

- **SRC-0236** `research/proto/chesscom/ceac/v2/request_metadata.proto` — [preserved redacted evidence](../evidence/text/2ba131aa5dbf7b9e7dd2324e1ab880badf1781688cbd86433177d34611b2547f.proto)
  Character offset 313.

```text
ct = 2;
  optional .google.protobuf.Timestamp received_time = 3;
  optional bool debug_mode = 4;
}

message RequestOptions {
  optional int32 heartbeat_interval_seconds = 4;
  optional bool use_progress_updates = 5;
}

```

**Source references:** SRC-0236, SRC-1207  
**URL references:** None independently associated  
**Related findings:** FND-00894, FND-00895, FND-00896

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00900"></a>
## FND-00900: chesscom.ceac.v2.RequestOptions.heartbeat_interval_seconds = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 heartbeat_interval_seconds = 4;

### Evidence

- **SRC-0236** `research/proto/chesscom/ceac/v2/request_metadata.proto` — [preserved redacted evidence](../evidence/text/2ba131aa5dbf7b9e7dd2324e1ab880badf1781688cbd86433177d34611b2547f.proto)
  Character offset 340.

```text
protobuf.Timestamp received_time = 3;
  optional bool debug_mode = 4;
}

message RequestOptions {
  optional int32 heartbeat_interval_seconds = 4;
  optional bool use_progress_updates = 5;
}

```

**Source references:** SRC-0236, SRC-1207  
**URL references:** None independently associated  
**Related findings:** FND-00894, FND-00895, FND-00896

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00901"></a>
## FND-00901: chesscom.ceac.v2.RequestOptions.use_progress_updates = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool use_progress_updates = 5;

### Evidence

- **SRC-0236** `research/proto/chesscom/ceac/v2/request_metadata.proto` — [preserved redacted evidence](../evidence/text/2ba131aa5dbf7b9e7dd2324e1ab880badf1781688cbd86433177d34611b2547f.proto)
  Character offset 389.

```text
bool debug_mode = 4;
}

message RequestOptions {
  optional int32 heartbeat_interval_seconds = 4;
  optional bool use_progress_updates = 5;
}

```

**Source references:** SRC-0236, SRC-1207  
**URL references:** None independently associated  
**Related findings:** FND-00894, FND-00895, FND-00896

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00902"></a>
## FND-00902: message declaration: chesscom.ceac.v2.RunSearchRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RunSearchRequest {

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 91.

```text
// source: chesscom/ceac/v2/run_search.proto
// syntax: proto3

package chesscom.ceac.v2;

message RunSearchRequest {
  optional .chesscom.explanation_engine.v1.NewGameRequest new_game_req = 1;
  optional .chesscom.explanation_engine.v1.RunSearchRequest run_search_req = 2;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional .chesscom.ceac.v2.RequestMetadata request_metadata = 4;
  optional .chesscom
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00903, FND-00904

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00903"></a>
## FND-00903: chesscom.ceac.v2.RunSearchRequest.new_game_req = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.NewGameRequest new_game_req = 1;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 120.

```text
ceac/v2/run_search.proto
// syntax: proto3

package chesscom.ceac.v2;

message RunSearchRequest {
  optional .chesscom.explanation_engine.v1.NewGameRequest new_game_req = 1;
  optional .chesscom.explanation_engine.v1.RunSearchRequest run_search_req = 2;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional .chesscom.ceac.v2.RequestMetadata request_metadata = 4;
  optional .chesscom.ceac.v2.RequestOptions reque
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00904"></a>
## FND-00904: chesscom.ceac.v2.RunSearchRequest.run_search_req = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.RunSearchRequest run_search_req = 2;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 196.

```text
ge RunSearchRequest {
  optional .chesscom.explanation_engine.v1.NewGameRequest new_game_req = 1;
  optional .chesscom.explanation_engine.v1.RunSearchRequest run_search_req = 2;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional .chesscom.ceac.v2.RequestMetadata request_metadata = 4;
  optional .chesscom.ceac.v2.RequestOptions request_options = 5;
  optional bool key_position_search = 6;
}

message RunSearc
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00905"></a>
## FND-00905: chesscom.ceac.v2.RunSearchRequest.engine = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.engine.v1.Engine engine = 3;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 276.

```text
new_game_req = 1;
  optional .chesscom.explanation_engine.v1.RunSearchRequest run_search_req = 2;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional .chesscom.ceac.v2.RequestMetadata request_metadata = 4;
  optional .chesscom.ceac.v2.RequestOptions request_options = 5;
  optional bool key_position_search = 6;
}

message RunSearchResponse {
  oneof result {
  .chesscom.ceac.v2.RunSearchResponseProgress progr
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00906"></a>
## FND-00906: chesscom.ceac.v2.RunSearchRequest.request_metadata = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ceac.v2.RequestMetadata request_metadata = 4;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 326.

```text
_engine.v1.RunSearchRequest run_search_req = 2;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional .chesscom.ceac.v2.RequestMetadata request_metadata = 4;
  optional .chesscom.ceac.v2.RequestOptions request_options = 5;
  optional bool key_position_search = 6;
}

message RunSearchResponse {
  oneof result {
  .chesscom.ceac.v2.RunSearchResponseProgress progress = 1;
  .chesscom.ceac.v2.RunSearchResponseSucc
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00907"></a>
## FND-00907: chesscom.ceac.v2.RunSearchRequest.request_options = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ceac.v2.RequestOptions request_options = 5;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 393.

```text
m.engine.v1.Engine engine = 3;
  optional .chesscom.ceac.v2.RequestMetadata request_metadata = 4;
  optional .chesscom.ceac.v2.RequestOptions request_options = 5;
  optional bool key_position_search = 6;
}

message RunSearchResponse {
  oneof result {
  .chesscom.ceac.v2.RunSearchResponseProgress progress = 1;
  .chesscom.ceac.v2.RunSearchResponseSuccess success = 2;
  .chesscom.ceac.v2.RunSearchResponseFailure failu
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00908"></a>
## FND-00908: chesscom.ceac.v2.RunSearchRequest.key_position_search = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool key_position_search = 6;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 458.

```text
stMetadata request_metadata = 4;
  optional .chesscom.ceac.v2.RequestOptions request_options = 5;
  optional bool key_position_search = 6;
}

message RunSearchResponse {
  oneof result {
  .chesscom.ceac.v2.RunSearchResponseProgress progress = 1;
  .chesscom.ceac.v2.RunSearchResponseSuccess success = 2;
  .chesscom.ceac.v2.RunSearchResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00909"></a>
## FND-00909: message declaration: chesscom.ceac.v2.RunSearchResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RunSearchResponse {

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 500.

```text
l .chesscom.ceac.v2.RequestOptions request_options = 5;
  optional bool key_position_search = 6;
}

message RunSearchResponse {
  oneof result {
  .chesscom.ceac.v2.RunSearchResponseProgress progress = 1;
  .chesscom.ceac.v2.RunSearchResponseSuccess success = 2;
  .chesscom.ceac.v2.RunSearchResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_cap
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00910"></a>
## FND-00910: oneof declaration: chesscom.ceac.v2.RunSearchResponse.result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof result {

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 530.

```text
ions request_options = 5;
  optional bool key_position_search = 6;
}

message RunSearchResponse {
  oneof result {
  .chesscom.ceac.v2.RunSearchResponseProgress progress = 1;
  .chesscom.ceac.v2.RunSearchResponseSuccess success = 2;
  .chesscom.ceac.v2.RunSearchResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message RunS
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00911"></a>
## FND-00911: chesscom.ceac.v2.RunSearchResponse.progress = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.RunSearchResponseProgress progress = 1;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 547.

```text
ons = 5;
  optional bool key_position_search = 6;
}

message RunSearchResponse {
  oneof result {
  .chesscom.ceac.v2.RunSearchResponseProgress progress = 1;
  .chesscom.ceac.v2.RunSearchResponseSuccess success = 2;
  .chesscom.ceac.v2.RunSearchResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message RunSearchResponseSucc
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00912"></a>
## FND-00912: chesscom.ceac.v2.RunSearchResponse.success = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.RunSearchResponseSuccess success = 2;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 607.

```text
 RunSearchResponse {
  oneof result {
  .chesscom.ceac.v2.RunSearchResponseProgress progress = 1;
  .chesscom.ceac.v2.RunSearchResponseSuccess success = 2;
  .chesscom.ceac.v2.RunSearchResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message RunSearchResponseSuccess {
  oneof _position_search_key {
  string position_searc
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00913"></a>
## FND-00913: chesscom.ceac.v2.RunSearchResponse.failure = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.RunSearchResponseFailure failure = 3;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 665.

```text
RunSearchResponseProgress progress = 1;
  .chesscom.ceac.v2.RunSearchResponseSuccess success = 2;
  .chesscom.ceac.v2.RunSearchResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message RunSearchResponseSuccess {
  oneof _position_search_key {
  string position_search_key = 2;
  }
  optional .chesscom.explanation_engine.v1.
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00914"></a>
## FND-00914: chesscom.ceac.v2.RunSearchResponse.heartbeat = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.Heartbeat heartbeat = 4;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 723.

```text
2.RunSearchResponseSuccess success = 2;
  .chesscom.ceac.v2.RunSearchResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message RunSearchResponseSuccess {
  oneof _position_search_key {
  string position_search_key = 2;
  }
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResp
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00915"></a>
## FND-00915: chesscom.ceac.v2.RunSearchResponse.waiting_for_capacity = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 768.

```text
esscom.ceac.v2.RunSearchResponseFailure failure = 3;
  .chesscom.ceac.v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message RunSearchResponseSuccess {
  oneof _position_search_key {
  string position_search_key = 2;
  }
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseProgress {
  optional .chesscom.explanati
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00916"></a>
## FND-00916: message declaration: chesscom.ceac.v2.RunSearchResponseSuccess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RunSearchResponseSuccess {

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 838.

```text
v2.Heartbeat heartbeat = 4;
  .chesscom.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message RunSearchResponseSuccess {
  oneof _position_search_key {
  string position_search_key = 2;
  }
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseProgress {
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchRes
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00917"></a>
## FND-00917: oneof declaration: chesscom.ceac.v2.RunSearchResponseSuccess._position_search_key

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _position_search_key {

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 875.

```text
om.ceac.v2.WaitingForCapacity waiting_for_capacity = 5;
  }
}

message RunSearchResponseSuccess {
  oneof _position_search_key {
  string position_search_key = 2;
  }
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseProgress {
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseFailure {
  oneof error {
  .che
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00918"></a>
## FND-00918: chesscom.ceac.v2.RunSearchResponseSuccess.position_search_key = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string position_search_key = 2;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 906.

```text
aiting_for_capacity = 5;
  }
}

message RunSearchResponseSuccess {
  oneof _position_search_key {
  string position_search_key = 2;
  }
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseProgress {
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError 
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00919"></a>
## FND-00919: chesscom.ceac.v2.RunSearchResponseSuccess.run_search = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 944.

```text
e RunSearchResponseSuccess {
  oneof _position_search_key {
  string position_search_key = 2;
  }
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseProgress {
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ce
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00920"></a>
## FND-00920: message declaration: chesscom.ceac.v2.RunSearchResponseProgress

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RunSearchResponseProgress {

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 1022.

```text
search_key = 2;
  }
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseProgress {
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  opti
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00921"></a>
## FND-00921: chesscom.ceac.v2.RunSearchResponseProgress.run_search = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 944.

```text
e RunSearchResponseSuccess {
  oneof _position_search_key {
  string position_search_key = 2;
  }
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseProgress {
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ce
```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00922"></a>
## FND-00922: message declaration: chesscom.ceac.v2.RunSearchResponseFailure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RunSearchResponseFailure {

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 1138.

```text
hResponseProgress {
  optional .chesscom.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_error = 5;
}

```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00923"></a>
## FND-00923: oneof declaration: chesscom.ceac.v2.RunSearchResponseFailure.error

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof error {

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 1175.

```text
com.explanation_engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_error = 5;
}

```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00924"></a>
## FND-00924: chesscom.ceac.v2.RunSearchResponseFailure.invalid_game_error = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 1191.

```text
engine.v1.RunSearchResponse run_search = 1;
}

message RunSearchResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_error = 5;
}

```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00925"></a>
## FND-00925: chesscom.ceac.v2.RunSearchResponseFailure.general_error = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.ceac.v2.GeneralError general_error = 4;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 1252.

```text
rchResponseFailure {
  oneof error {
  .chesscom.ceac.v2.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_error = 5;
}

```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00926"></a>
## FND-00926: chesscom.ceac.v2.RunSearchResponseFailure.reason = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string reason = 1;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 1308.

```text
.InvalidGameError invalid_game_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_error = 5;
}

```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00927"></a>
## FND-00927: chesscom.ceac.v2.RunSearchResponseFailure.failure_error = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ceac.v2.FailureError failure_error = 5;

### Evidence

- **SRC-0237** `research/proto/chesscom/ceac/v2/run_search.proto` — [preserved redacted evidence](../evidence/text/66e1d39e9ecb8ee9f7cb2d7bdf653b1a764882a9dbf0e19450ff3fe732cc926b.proto)
  Character offset 1338.

```text
_error = 3;
  .chesscom.ceac.v2.GeneralError general_error = 4;
  }
  optional string reason = 1;
  optional .chesscom.ceac.v2.FailureError failure_error = 5;
}

```

**Source references:** SRC-0237, SRC-1208  
**URL references:** None independently associated  
**Related findings:** FND-00902, FND-00903, FND-00904

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00928"></a>
## FND-00928: message declaration: chesscom.ceac.v2.WaitingForCapacity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message WaitingForCapacity {

### Evidence

- **SRC-0238** `research/proto/chesscom/ceac/v2/waiting_for_capacity.proto` — [preserved redacted evidence](../evidence/text/c488edd41ecdb6f2fd0cd7957402aeef04575c3d5028c008ea0dacb2f4b88e03.proto)
  Character offset 101.

```text
/ source: chesscom/ceac/v2/waiting_for_capacity.proto
// syntax: proto3

package chesscom.ceac.v2;

message WaitingForCapacity {
}

```

**Source references:** SRC-0238, SRC-1209  
**URL references:** None independently associated  
**Related findings:** None assigned

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00929"></a>
## FND-00929: message declaration: chesscom.cheat_metadata_storage.v1.GameCheatMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameCheatMetadata {

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 131.

```text
ata_storage/v1/cheat_metadata.proto
// syntax: proto3

package chesscom.cheat_metadata_storage.v1;

message GameCheatMetadata {
  optional string game_id = 1;
  optional .google.protobuf.Timestamp created_at = 2;
  optional .chesscom.cheat_metadata_storage.v1.CheatMetadata white_player_metadata = 3;
  optional .chesscom.cheat_metadata_storage.v1.CheatMetadata black_player_metadata = 4;
  optional string white_client 
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00930, FND-00931

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00930"></a>
## FND-00930: chesscom.cheat_metadata_storage.v1.GameCheatMetadata.game_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_id = 1;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 161.

```text
proto
// syntax: proto3

package chesscom.cheat_metadata_storage.v1;

message GameCheatMetadata {
  optional string game_id = 1;
  optional .google.protobuf.Timestamp created_at = 2;
  optional .chesscom.cheat_metadata_storage.v1.CheatMetadata white_player_metadata = 3;
  optional .chesscom.cheat_metadata_storage.v1.CheatMetadata black_player_metadata = 4;
  optional string white_client = 5;
  optional string black_c
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00931"></a>
## FND-00931: chesscom.cheat_metadata_storage.v1.GameCheatMetadata.created_at = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp created_at = 2;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 192.

```text
e chesscom.cheat_metadata_storage.v1;

message GameCheatMetadata {
  optional string game_id = 1;
  optional .google.protobuf.Timestamp created_at = 2;
  optional .chesscom.cheat_metadata_storage.v1.CheatMetadata white_player_metadata = 3;
  optional .chesscom.cheat_metadata_storage.v1.CheatMetadata black_player_metadata = 4;
  optional string white_client = 5;
  optional string black_client = 6;
  optional bool whit
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00932"></a>
## FND-00932: chesscom.cheat_metadata_storage.v1.GameCheatMetadata.white_player_metadata = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.cheat_metadata_storage.v1.CheatMetadata white_player_metadata = 3;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 246.

```text
atMetadata {
  optional string game_id = 1;
  optional .google.protobuf.Timestamp created_at = 2;
  optional .chesscom.cheat_metadata_storage.v1.CheatMetadata white_player_metadata = 3;
  optional .chesscom.cheat_metadata_storage.v1.CheatMetadata black_player_metadata = 4;
  optional string white_client = 5;
  optional string black_client = 6;
  optional bool white_moves_from_multiple_clients = 7;
  optional bool bla
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00933"></a>
## FND-00933: chesscom.cheat_metadata_storage.v1.GameCheatMetadata.black_player_metadata = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.cheat_metadata_storage.v1.CheatMetadata black_player_metadata = 4;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 334.

```text
d_at = 2;
  optional .chesscom.cheat_metadata_storage.v1.CheatMetadata white_player_metadata = 3;
  optional .chesscom.cheat_metadata_storage.v1.CheatMetadata black_player_metadata = 4;
  optional string white_client = 5;
  optional string black_client = 6;
  optional bool white_moves_from_multiple_clients = 7;
  optional bool black_moves_from_multiple_clients = 8;
}

message CheatMetadata {
  repeated uint32 move_ho
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00934"></a>
## FND-00934: chesscom.cheat_metadata_storage.v1.GameCheatMetadata.white_client = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string white_client = 5;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 422.

```text
data = 3;
  optional .chesscom.cheat_metadata_storage.v1.CheatMetadata black_player_metadata = 4;
  optional string white_client = 5;
  optional string black_client = 6;
  optional bool white_moves_from_multiple_clients = 7;
  optional bool black_moves_from_multiple_clients = 8;
}

message CheatMetadata {
  repeated uint32 move_hold_times = 1;
  repeated uint32 toggled_moves = 2;
  repeated uint32 bot_moves = 3;
  re
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00935"></a>
## FND-00935: chesscom.cheat_metadata_storage.v1.GameCheatMetadata.black_client = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string black_client = 6;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 458.

```text
_metadata_storage.v1.CheatMetadata black_player_metadata = 4;
  optional string white_client = 5;
  optional string black_client = 6;
  optional bool white_moves_from_multiple_clients = 7;
  optional bool black_moves_from_multiple_clients = 8;
}

message CheatMetadata {
  repeated uint32 move_hold_times = 1;
  repeated uint32 toggled_moves = 2;
  repeated uint32 bot_moves = 3;
  repeated uint32 change_of_heart_moves 
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00936"></a>
## FND-00936: chesscom.cheat_metadata_storage.v1.GameCheatMetadata.white_moves_from_multiple_clients = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool white_moves_from_multiple_clients = 7;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 494.

```text
lack_player_metadata = 4;
  optional string white_client = 5;
  optional string black_client = 6;
  optional bool white_moves_from_multiple_clients = 7;
  optional bool black_moves_from_multiple_clients = 8;
}

message CheatMetadata {
  repeated uint32 move_hold_times = 1;
  repeated uint32 toggled_moves = 2;
  repeated uint32 bot_moves = 3;
  repeated uint32 change_of_heart_moves = 4;
  repeated uint32 draw_offer_mo
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00937"></a>
## FND-00937: chesscom.cheat_metadata_storage.v1.GameCheatMetadata.black_moves_from_multiple_clients = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool black_moves_from_multiple_clients = 8;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 549.

```text
t = 5;
  optional string black_client = 6;
  optional bool white_moves_from_multiple_clients = 7;
  optional bool black_moves_from_multiple_clients = 8;
}

message CheatMetadata {
  repeated uint32 move_hold_times = 1;
  repeated uint32 toggled_moves = 2;
  repeated uint32 bot_moves = 3;
  repeated uint32 change_of_heart_moves = 4;
  repeated uint32 draw_offer_moves = 5;
  repeated int32 pointer_offsets = 6;
  repeat
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00938"></a>
## FND-00938: message declaration: chesscom.cheat_metadata_storage.v1.CheatMetadata

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CheatMetadata {

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 605.

```text
ol white_moves_from_multiple_clients = 7;
  optional bool black_moves_from_multiple_clients = 8;
}

message CheatMetadata {
  repeated uint32 move_hold_times = 1;
  repeated uint32 toggled_moves = 2;
  repeated uint32 bot_moves = 3;
  repeated uint32 change_of_heart_moves = 4;
  repeated uint32 draw_offer_moves = 5;
  repeated int32 pointer_offsets = 6;
  repeated uint32 not_user_generated_moves = 7;
  repeated uint3
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00939"></a>
## FND-00939: chesscom.cheat_metadata_storage.v1.CheatMetadata.move_hold_times = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 move_hold_times = 1;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 631.

```text
le_clients = 7;
  optional bool black_moves_from_multiple_clients = 8;
}

message CheatMetadata {
  repeated uint32 move_hold_times = 1;
  repeated uint32 toggled_moves = 2;
  repeated uint32 bot_moves = 3;
  repeated uint32 change_of_heart_moves = 4;
  repeated uint32 draw_offer_moves = 5;
  repeated int32 pointer_offsets = 6;
  repeated uint32 not_user_generated_moves = 7;
  repeated uint32 untrusted_event_moves = 
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00940"></a>
## FND-00940: chesscom.cheat_metadata_storage.v1.CheatMetadata.toggled_moves = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 toggled_moves = 2;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 670.

```text
oves_from_multiple_clients = 8;
}

message CheatMetadata {
  repeated uint32 move_hold_times = 1;
  repeated uint32 toggled_moves = 2;
  repeated uint32 bot_moves = 3;
  repeated uint32 change_of_heart_moves = 4;
  repeated uint32 draw_offer_moves = 5;
  repeated int32 pointer_offsets = 6;
  repeated uint32 not_user_generated_moves = 7;
  repeated uint32 untrusted_event_moves = 8;
  repeated uint32 blur_on_own_turn_m
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00941"></a>
## FND-00941: chesscom.cheat_metadata_storage.v1.CheatMetadata.bot_moves = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 bot_moves = 3;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 707.

```text
ssage CheatMetadata {
  repeated uint32 move_hold_times = 1;
  repeated uint32 toggled_moves = 2;
  repeated uint32 bot_moves = 3;
  repeated uint32 change_of_heart_moves = 4;
  repeated uint32 draw_offer_moves = 5;
  repeated int32 pointer_offsets = 6;
  repeated uint32 not_user_generated_moves = 7;
  repeated uint32 untrusted_event_moves = 8;
  repeated uint32 blur_on_own_turn_moves = 9;
  repeated uint32 blur_on_o
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00942"></a>
## FND-00942: chesscom.cheat_metadata_storage.v1.CheatMetadata.change_of_heart_moves = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 change_of_heart_moves = 4;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 740.

```text
uint32 move_hold_times = 1;
  repeated uint32 toggled_moves = 2;
  repeated uint32 bot_moves = 3;
  repeated uint32 change_of_heart_moves = 4;
  repeated uint32 draw_offer_moves = 5;
  repeated int32 pointer_offsets = 6;
  repeated uint32 not_user_generated_moves = 7;
  repeated uint32 untrusted_event_moves = 8;
  repeated uint32 blur_on_own_turn_moves = 9;
  repeated uint32 blur_on_opponent_turn_moves = 10;
  repeat
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00943"></a>
## FND-00943: chesscom.cheat_metadata_storage.v1.CheatMetadata.draw_offer_moves = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 draw_offer_moves = 5;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 785.

```text
 toggled_moves = 2;
  repeated uint32 bot_moves = 3;
  repeated uint32 change_of_heart_moves = 4;
  repeated uint32 draw_offer_moves = 5;
  repeated int32 pointer_offsets = 6;
  repeated uint32 not_user_generated_moves = 7;
  repeated uint32 untrusted_event_moves = 8;
  repeated uint32 blur_on_own_turn_moves = 9;
  repeated uint32 blur_on_opponent_turn_moves = 10;
  repeated uint32 focus_on_own_turn_moves = 11;
  rep
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00944"></a>
## FND-00944: chesscom.cheat_metadata_storage.v1.CheatMetadata.pointer_offsets = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated int32 pointer_offsets = 6;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 825.

```text
t_moves = 3;
  repeated uint32 change_of_heart_moves = 4;
  repeated uint32 draw_offer_moves = 5;
  repeated int32 pointer_offsets = 6;
  repeated uint32 not_user_generated_moves = 7;
  repeated uint32 untrusted_event_moves = 8;
  repeated uint32 blur_on_own_turn_moves = 9;
  repeated uint32 blur_on_opponent_turn_moves = 10;
  repeated uint32 focus_on_own_turn_moves = 11;
  repeated uint32 focus_on_opponent_turn_move
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00945"></a>
## FND-00945: chesscom.cheat_metadata_storage.v1.CheatMetadata.not_user_generated_moves = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 not_user_generated_moves = 7;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 863.

```text
of_heart_moves = 4;
  repeated uint32 draw_offer_moves = 5;
  repeated int32 pointer_offsets = 6;
  repeated uint32 not_user_generated_moves = 7;
  repeated uint32 untrusted_event_moves = 8;
  repeated uint32 blur_on_own_turn_moves = 9;
  repeated uint32 blur_on_opponent_turn_moves = 10;
  repeated uint32 focus_on_own_turn_moves = 11;
  repeated uint32 focus_on_opponent_turn_moves = 12;
  repeated int32 move_to_first
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00946"></a>
## FND-00946: chesscom.cheat_metadata_storage.v1.CheatMetadata.untrusted_event_moves = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 untrusted_event_moves = 8;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 911.

```text
_moves = 5;
  repeated int32 pointer_offsets = 6;
  repeated uint32 not_user_generated_moves = 7;
  repeated uint32 untrusted_event_moves = 8;
  repeated uint32 blur_on_own_turn_moves = 9;
  repeated uint32 blur_on_opponent_turn_moves = 10;
  repeated uint32 focus_on_own_turn_moves = 11;
  repeated uint32 focus_on_opponent_turn_moves = 12;
  repeated int32 move_to_first_blur_times = 13;
  repeated int32 last_focus_to
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00947"></a>
## FND-00947: chesscom.cheat_metadata_storage.v1.CheatMetadata.blur_on_own_turn_moves = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 blur_on_own_turn_moves = 9;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 956.

```text
= 6;
  repeated uint32 not_user_generated_moves = 7;
  repeated uint32 untrusted_event_moves = 8;
  repeated uint32 blur_on_own_turn_moves = 9;
  repeated uint32 blur_on_opponent_turn_moves = 10;
  repeated uint32 focus_on_own_turn_moves = 11;
  repeated uint32 focus_on_opponent_turn_moves = 12;
  repeated int32 move_to_first_blur_times = 13;
  repeated int32 last_focus_to_move_times = 14;
  repeated int32 total_blur
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00948"></a>
## FND-00948: chesscom.cheat_metadata_storage.v1.CheatMetadata.blur_on_opponent_turn_moves = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 blur_on_opponent_turn_moves = 10;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 1002.

```text
s = 7;
  repeated uint32 untrusted_event_moves = 8;
  repeated uint32 blur_on_own_turn_moves = 9;
  repeated uint32 blur_on_opponent_turn_moves = 10;
  repeated uint32 focus_on_own_turn_moves = 11;
  repeated uint32 focus_on_opponent_turn_moves = 12;
  repeated int32 move_to_first_blur_times = 13;
  repeated int32 last_focus_to_move_times = 14;
  repeated int32 total_blur_time = 15;
  repeated int32 total_focus_time 
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00949"></a>
## FND-00949: chesscom.cheat_metadata_storage.v1.CheatMetadata.focus_on_own_turn_moves = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 focus_on_own_turn_moves = 11;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 1054.

```text
  repeated uint32 blur_on_own_turn_moves = 9;
  repeated uint32 blur_on_opponent_turn_moves = 10;
  repeated uint32 focus_on_own_turn_moves = 11;
  repeated uint32 focus_on_opponent_turn_moves = 12;
  repeated int32 move_to_first_blur_times = 13;
  repeated int32 last_focus_to_move_times = 14;
  repeated int32 total_blur_time = 15;
  repeated int32 total_focus_time = 16;
  repeated int32 blur_counts = 17;
  repeated 
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00950"></a>
## FND-00950: chesscom.cheat_metadata_storage.v1.CheatMetadata.focus_on_opponent_turn_moves = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 focus_on_opponent_turn_moves = 12;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 1102.

```text
repeated uint32 blur_on_opponent_turn_moves = 10;
  repeated uint32 focus_on_own_turn_moves = 11;
  repeated uint32 focus_on_opponent_turn_moves = 12;
  repeated int32 move_to_first_blur_times = 13;
  repeated int32 last_focus_to_move_times = 14;
  repeated int32 total_blur_time = 15;
  repeated int32 total_focus_time = 16;
  repeated int32 blur_counts = 17;
  repeated uint32 external_board_moves = 18;
  repeated uin
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00951"></a>
## FND-00951: chesscom.cheat_metadata_storage.v1.CheatMetadata.move_to_first_blur_times = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated int32 move_to_first_blur_times = 13;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 1155.

```text
epeated uint32 focus_on_own_turn_moves = 11;
  repeated uint32 focus_on_opponent_turn_moves = 12;
  repeated int32 move_to_first_blur_times = 13;
  repeated int32 last_focus_to_move_times = 14;
  repeated int32 total_blur_time = 15;
  repeated int32 total_focus_time = 16;
  repeated int32 blur_counts = 17;
  repeated uint32 external_board_moves = 18;
  repeated uint32 premoves = 19;
  repeated uint32 screenshot_detec
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00952"></a>
## FND-00952: chesscom.cheat_metadata_storage.v1.CheatMetadata.last_focus_to_move_times = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated int32 last_focus_to_move_times = 14;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 1203.

```text
epeated uint32 focus_on_opponent_turn_moves = 12;
  repeated int32 move_to_first_blur_times = 13;
  repeated int32 last_focus_to_move_times = 14;
  repeated int32 total_blur_time = 15;
  repeated int32 total_focus_time = 16;
  repeated int32 blur_counts = 17;
  repeated uint32 external_board_moves = 18;
  repeated uint32 premoves = 19;
  repeated uint32 screenshot_detected_moves = 20;
  optional string browser_extens
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00953"></a>
## FND-00953: chesscom.cheat_metadata_storage.v1.CheatMetadata.total_blur_time = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated int32 total_blur_time = 15;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 1251.

```text
;
  repeated int32 move_to_first_blur_times = 13;
  repeated int32 last_focus_to_move_times = 14;
  repeated int32 total_blur_time = 15;
  repeated int32 total_focus_time = 16;
  repeated int32 blur_counts = 17;
  repeated uint32 external_board_moves = 18;
  repeated uint32 premoves = 19;
  repeated uint32 screenshot_detected_moves = 20;
  optional string browser_extension = 21;
  repeated int32 square_widths = 22;
}
```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00954"></a>
## FND-00954: chesscom.cheat_metadata_storage.v1.CheatMetadata.total_focus_time = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated int32 total_focus_time = 16;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 1290.

```text
imes = 13;
  repeated int32 last_focus_to_move_times = 14;
  repeated int32 total_blur_time = 15;
  repeated int32 total_focus_time = 16;
  repeated int32 blur_counts = 17;
  repeated uint32 external_board_moves = 18;
  repeated uint32 premoves = 19;
  repeated uint32 screenshot_detected_moves = 20;
  optional string browser_extension = 21;
  repeated int32 square_widths = 22;
}

```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00955"></a>
## FND-00955: chesscom.cheat_metadata_storage.v1.CheatMetadata.blur_counts = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated int32 blur_counts = 17;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 1330.

```text
o_move_times = 14;
  repeated int32 total_blur_time = 15;
  repeated int32 total_focus_time = 16;
  repeated int32 blur_counts = 17;
  repeated uint32 external_board_moves = 18;
  repeated uint32 premoves = 19;
  repeated uint32 screenshot_detected_moves = 20;
  optional string browser_extension = 21;
  repeated int32 square_widths = 22;
}

```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00956"></a>
## FND-00956: chesscom.cheat_metadata_storage.v1.CheatMetadata.external_board_moves = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 external_board_moves = 18;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 1365.

```text
 total_blur_time = 15;
  repeated int32 total_focus_time = 16;
  repeated int32 blur_counts = 17;
  repeated uint32 external_board_moves = 18;
  repeated uint32 premoves = 19;
  repeated uint32 screenshot_detected_moves = 20;
  optional string browser_extension = 21;
  repeated int32 square_widths = 22;
}

```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00957"></a>
## FND-00957: chesscom.cheat_metadata_storage.v1.CheatMetadata.premoves = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 premoves = 19;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 1410.

```text
_focus_time = 16;
  repeated int32 blur_counts = 17;
  repeated uint32 external_board_moves = 18;
  repeated uint32 premoves = 19;
  repeated uint32 screenshot_detected_moves = 20;
  optional string browser_extension = 21;
  repeated int32 square_widths = 22;
}

```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00958"></a>
## FND-00958: chesscom.cheat_metadata_storage.v1.CheatMetadata.screenshot_detected_moves = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated uint32 screenshot_detected_moves = 20;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 1443.

```text
2 blur_counts = 17;
  repeated uint32 external_board_moves = 18;
  repeated uint32 premoves = 19;
  repeated uint32 screenshot_detected_moves = 20;
  optional string browser_extension = 21;
  repeated int32 square_widths = 22;
}

```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00959"></a>
## FND-00959: chesscom.cheat_metadata_storage.v1.CheatMetadata.browser_extension = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string browser_extension = 21;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 1493.

```text
rd_moves = 18;
  repeated uint32 premoves = 19;
  repeated uint32 screenshot_detected_moves = 20;
  optional string browser_extension = 21;
  repeated int32 square_widths = 22;
}

```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00960"></a>
## FND-00960: chesscom.cheat_metadata_storage.v1.CheatMetadata.square_widths = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated int32 square_widths = 22;

### Evidence

- **SRC-0239** `research/proto/chesscom/cheat_metadata_storage/v1/cheat_metadata.proto` — [preserved redacted evidence](../evidence/text/f2c20deacbf209241ec60d0d9627821e8d2c7f5c1f3b1ed0f186beb5642c8631.proto)
  Character offset 1535.

```text
= 19;
  repeated uint32 screenshot_detected_moves = 20;
  optional string browser_extension = 21;
  repeated int32 square_widths = 22;
}

```

**Source references:** SRC-0239, SRC-1210  
**URL references:** None independently associated  
**Related findings:** FND-00929, FND-00930, FND-00931

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00961"></a>
## FND-00961: message declaration: chesscom.chess.v1.Arrow

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Arrow {

### Evidence

- **SRC-0240** `research/proto/chesscom/chess/v1/arrow.proto` — [preserved redacted evidence](../evidence/text/7ae30bfec7dd4dcedad1ebff56c4269be807ab39eb3831df693ef769229e5a9b.proto)
  Character offset 88.

```text
// source: chesscom/chess/v1/arrow.proto
// syntax: proto3

package chesscom.chess.v1;

message Arrow {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
}

message ArrowsAndSquares {
  repeated .chesscom.chess.v1.Arrow arrows = 1;
  repeated .chesscom.chess.v1.Square squares = 2;
}

```

**Source references:** SRC-0240, SRC-1211  
**URL references:** None independently associated  
**Related findings:** FND-00962, FND-00963

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00962"></a>
## FND-00962: chesscom.chess.v1.Arrow.from = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square from = 1;

### Evidence

- **SRC-0240** `research/proto/chesscom/chess/v1/arrow.proto` — [preserved redacted evidence](../evidence/text/7ae30bfec7dd4dcedad1ebff56c4269be807ab39eb3831df693ef769229e5a9b.proto)
  Character offset 106.

```text
rce: chesscom/chess/v1/arrow.proto
// syntax: proto3

package chesscom.chess.v1;

message Arrow {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
}

message ArrowsAndSquares {
  repeated .chesscom.chess.v1.Arrow arrows = 1;
  repeated .chesscom.chess.v1.Square squares = 2;
}

```

**Source references:** SRC-0240, SRC-1211  
**URL references:** None independently associated  
**Related findings:** FND-00961, FND-00963

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00963"></a>
## FND-00963: chesscom.chess.v1.Arrow.to = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square to = 2;

### Evidence

- **SRC-0240** `research/proto/chesscom/chess/v1/arrow.proto` — [preserved redacted evidence](../evidence/text/7ae30bfec7dd4dcedad1ebff56c4269be807ab39eb3831df693ef769229e5a9b.proto)
  Character offset 153.

```text
roto3

package chesscom.chess.v1;

message Arrow {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
}

message ArrowsAndSquares {
  repeated .chesscom.chess.v1.Arrow arrows = 1;
  repeated .chesscom.chess.v1.Square squares = 2;
}

```

**Source references:** SRC-0240, SRC-1211  
**URL references:** None independently associated  
**Related findings:** FND-00961, FND-00962

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00964"></a>
## FND-00964: message declaration: chesscom.chess.v1.ArrowsAndSquares

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ArrowsAndSquares {

### Evidence

- **SRC-0240** `research/proto/chesscom/chess/v1/arrow.proto` — [preserved redacted evidence](../evidence/text/7ae30bfec7dd4dcedad1ebff56c4269be807ab39eb3831df693ef769229e5a9b.proto)
  Character offset 199.

```text
ow {
  optional .chesscom.chess.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
}

message ArrowsAndSquares {
  repeated .chesscom.chess.v1.Arrow arrows = 1;
  repeated .chesscom.chess.v1.Square squares = 2;
}

```

**Source references:** SRC-0240, SRC-1211  
**URL references:** None independently associated  
**Related findings:** FND-00961, FND-00962, FND-00963

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00965"></a>
## FND-00965: chesscom.chess.v1.ArrowsAndSquares.arrows = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Arrow arrows = 1;

### Evidence

- **SRC-0240** `research/proto/chesscom/chess/v1/arrow.proto` — [preserved redacted evidence](../evidence/text/7ae30bfec7dd4dcedad1ebff56c4269be807ab39eb3831df693ef769229e5a9b.proto)
  Character offset 228.

```text
ss.v1.Square from = 1;
  optional .chesscom.chess.v1.Square to = 2;
}

message ArrowsAndSquares {
  repeated .chesscom.chess.v1.Arrow arrows = 1;
  repeated .chesscom.chess.v1.Square squares = 2;
}

```

**Source references:** SRC-0240, SRC-1211  
**URL references:** None independently associated  
**Related findings:** FND-00961, FND-00962, FND-00963

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00966"></a>
## FND-00966: chesscom.chess.v1.ArrowsAndSquares.squares = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Square squares = 2;

### Evidence

- **SRC-0240** `research/proto/chesscom/chess/v1/arrow.proto` — [preserved redacted evidence](../evidence/text/7ae30bfec7dd4dcedad1ebff56c4269be807ab39eb3831df693ef769229e5a9b.proto)
  Character offset 276.

```text
s.v1.Square to = 2;
}

message ArrowsAndSquares {
  repeated .chesscom.chess.v1.Arrow arrows = 1;
  repeated .chesscom.chess.v1.Square squares = 2;
}

```

**Source references:** SRC-0240, SRC-1211  
**URL references:** None independently associated  
**Related findings:** FND-00961, FND-00962, FND-00963

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-00967"></a>
## FND-00967: enum declaration: chesscom.chess.v1.MarkingColor

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MarkingColor {

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 97.

```text
// source: chesscom/chess/v1/board_markings.proto
// syntax: proto3

package chesscom.chess.v1;

enum MarkingColor {
  MARKING_COLOR_UNSPECIFIED = 0;
  MARKING_COLOR_RED = 1;
  MARKING_COLOR_BLUE = 2;
  MARKING_COLOR_GREEN = 3;
  MARKING_COLOR_ORANGE = 4;
}

message ArrowMarking {
  optional .chesscom.chess.v1.Arrow arrow = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message SquareMarking {
  optio
```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00968, FND-00969

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00968"></a>
## FND-00968: chesscom.chess.v1.MarkingColor.MARKING_COLOR_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MARKING_COLOR_UNSPECIFIED = 0;

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 119.

```text
/chess/v1/board_markings.proto
// syntax: proto3

package chesscom.chess.v1;

enum MarkingColor {
  MARKING_COLOR_UNSPECIFIED = 0;
  MARKING_COLOR_RED = 1;
  MARKING_COLOR_BLUE = 2;
  MARKING_COLOR_GREEN = 3;
  MARKING_COLOR_ORANGE = 4;
}

message ArrowMarking {
  optional .chesscom.chess.v1.Arrow arrow = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message SquareMarking {
  optional .chesscom.chess.v1
```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00969

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00969"></a>
## FND-00969: chesscom.chess.v1.MarkingColor.MARKING_COLOR_RED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MARKING_COLOR_RED = 1;

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 152.

```text
 syntax: proto3

package chesscom.chess.v1;

enum MarkingColor {
  MARKING_COLOR_UNSPECIFIED = 0;
  MARKING_COLOR_RED = 1;
  MARKING_COLOR_BLUE = 2;
  MARKING_COLOR_GREEN = 3;
  MARKING_COLOR_ORANGE = 4;
}

message ArrowMarking {
  optional .chesscom.chess.v1.Arrow arrow = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message SquareMarking {
  optional .chesscom.chess.v1.Square square = 1;
  optional .c
```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00968

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00970"></a>
## FND-00970: chesscom.chess.v1.MarkingColor.MARKING_COLOR_BLUE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MARKING_COLOR_BLUE = 2;

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 177.

```text
chesscom.chess.v1;

enum MarkingColor {
  MARKING_COLOR_UNSPECIFIED = 0;
  MARKING_COLOR_RED = 1;
  MARKING_COLOR_BLUE = 2;
  MARKING_COLOR_GREEN = 3;
  MARKING_COLOR_ORANGE = 4;
}

message ArrowMarking {
  optional .chesscom.chess.v1.Arrow arrow = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message SquareMarking {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.chess.v1.MarkingC
```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00968, FND-00969

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00971"></a>
## FND-00971: chesscom.chess.v1.MarkingColor.MARKING_COLOR_GREEN = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MARKING_COLOR_GREEN = 3;

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 203.

```text
arkingColor {
  MARKING_COLOR_UNSPECIFIED = 0;
  MARKING_COLOR_RED = 1;
  MARKING_COLOR_BLUE = 2;
  MARKING_COLOR_GREEN = 3;
  MARKING_COLOR_ORANGE = 4;
}

message ArrowMarking {
  optional .chesscom.chess.v1.Arrow arrow = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message SquareMarking {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message
```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00968, FND-00969

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00972"></a>
## FND-00972: chesscom.chess.v1.MarkingColor.MARKING_COLOR_ORANGE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MARKING_COLOR_ORANGE = 4;

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 230.

```text
OR_UNSPECIFIED = 0;
  MARKING_COLOR_RED = 1;
  MARKING_COLOR_BLUE = 2;
  MARKING_COLOR_GREEN = 3;
  MARKING_COLOR_ORANGE = 4;
}

message ArrowMarking {
  optional .chesscom.chess.v1.Arrow arrow = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message SquareMarking {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message BoardMarkings {
  repeated
```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00968, FND-00969

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00973"></a>
## FND-00973: message declaration: chesscom.chess.v1.ArrowMarking

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ArrowMarking {

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 259.

```text
_COLOR_RED = 1;
  MARKING_COLOR_BLUE = 2;
  MARKING_COLOR_GREEN = 3;
  MARKING_COLOR_ORANGE = 4;
}

message ArrowMarking {
  optional .chesscom.chess.v1.Arrow arrow = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message SquareMarking {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message BoardMarkings {
  repeated .chesscom.chess.v1.ArrowMark
```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00968, FND-00969

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-00974"></a>
## FND-00974: chesscom.chess.v1.ArrowMarking.arrow = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Arrow arrow = 1;

### Evidence

- **SRC-0241** `research/proto/chesscom/chess/v1/board_markings.proto` — [preserved redacted evidence](../evidence/text/5da3d766d3aec780e114cc51daa52f702ecbf8475795190cccc1a5d4d924475e.proto)
  Character offset 284.

```text
_COLOR_BLUE = 2;
  MARKING_COLOR_GREEN = 3;
  MARKING_COLOR_ORANGE = 4;
}

message ArrowMarking {
  optional .chesscom.chess.v1.Arrow arrow = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message SquareMarking {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.chess.v1.MarkingColor color = 2;
}

message BoardMarkings {
  repeated .chesscom.chess.v1.ArrowMarking arrows = 1;
  repeate
```

**Source references:** SRC-0241, SRC-1212  
**URL references:** None independently associated  
**Related findings:** FND-00967, FND-00968, FND-00969

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
