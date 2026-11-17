# data_models — findings 10601–10700

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-10875"></a>
## FND-10875: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._unrated_attempt_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _unrated_attempt_count {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1691.

```text
32 rated_attempt_count = 4;
  }
  oneof _rated_passed_count {
  int32 rated_passed_count = 5;
  }
  oneof _unrated_attempt_count {
  int32 unrated_attempt_count = 6;
  }
  oneof _min_rating {
  int32 min_rating = 7;
  }
  oneof _min_rating_timestamp {
  .google.protobuf.Timestamp min_rating_timestamp = 8;
  }
  oneof _max_rating {
  int32 max_rating = 9;
  }
  oneof _max_rating_timestamp {
  .google.protobuf.Timestam
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10876"></a>
## FND-10876: chesscom.user_properties.v1.PuzzlesAttemptedProperty.unrated_attempt_count = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 unrated_attempt_count = 6;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1724.

```text
 oneof _rated_passed_count {
  int32 rated_passed_count = 5;
  }
  oneof _unrated_attempt_count {
  int32 unrated_attempt_count = 6;
  }
  oneof _min_rating {
  int32 min_rating = 7;
  }
  oneof _min_rating_timestamp {
  .google.protobuf.Timestamp min_rating_timestamp = 8;
  }
  oneof _max_rating {
  int32 max_rating = 9;
  }
  oneof _max_rating_timestamp {
  .google.protobuf.Timestamp max_rating_timestamp = 10;
  }

```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10877"></a>
## FND-10877: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._min_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _min_rating {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1763.

```text
ted_passed_count = 5;
  }
  oneof _unrated_attempt_count {
  int32 unrated_attempt_count = 6;
  }
  oneof _min_rating {
  int32 min_rating = 7;
  }
  oneof _min_rating_timestamp {
  .google.protobuf.Timestamp min_rating_timestamp = 8;
  }
  oneof _max_rating {
  int32 max_rating = 9;
  }
  oneof _max_rating_timestamp {
  .google.protobuf.Timestamp max_rating_timestamp = 10;
  }
  oneof _rated_longest_streak {
  int32
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10878"></a>
## FND-10878: chesscom.user_properties.v1.PuzzlesAttemptedProperty.min_rating = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 min_rating = 7;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1785.

```text
  }
  oneof _unrated_attempt_count {
  int32 unrated_attempt_count = 6;
  }
  oneof _min_rating {
  int32 min_rating = 7;
  }
  oneof _min_rating_timestamp {
  .google.protobuf.Timestamp min_rating_timestamp = 8;
  }
  oneof _max_rating {
  int32 max_rating = 9;
  }
  oneof _max_rating_timestamp {
  .google.protobuf.Timestamp max_rating_timestamp = 10;
  }
  oneof _rated_longest_streak {
  int32 rated_longest_streak 
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10879"></a>
## FND-10879: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._min_rating_timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _min_rating_timestamp {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1813.

```text
_count {
  int32 unrated_attempt_count = 6;
  }
  oneof _min_rating {
  int32 min_rating = 7;
  }
  oneof _min_rating_timestamp {
  .google.protobuf.Timestamp min_rating_timestamp = 8;
  }
  oneof _max_rating {
  int32 max_rating = 9;
  }
  oneof _max_rating_timestamp {
  .google.protobuf.Timestamp max_rating_timestamp = 10;
  }
  oneof _rated_longest_streak {
  int32 rated_longest_streak = 11;
  }
  oneof _rated_lon
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10880"></a>
## FND-10880: chesscom.user_properties.v1.PuzzlesAttemptedProperty.min_rating_timestamp = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp min_rating_timestamp = 8;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1845.

```text
_count = 6;
  }
  oneof _min_rating {
  int32 min_rating = 7;
  }
  oneof _min_rating_timestamp {
  .google.protobuf.Timestamp min_rating_timestamp = 8;
  }
  oneof _max_rating {
  int32 max_rating = 9;
  }
  oneof _max_rating_timestamp {
  .google.protobuf.Timestamp max_rating_timestamp = 10;
  }
  oneof _rated_longest_streak {
  int32 rated_longest_streak = 11;
  }
  oneof _rated_longest_streak_timestamp {
  .googl
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10881"></a>
## FND-10881: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._max_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_rating {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1904.

```text
7;
  }
  oneof _min_rating_timestamp {
  .google.protobuf.Timestamp min_rating_timestamp = 8;
  }
  oneof _max_rating {
  int32 max_rating = 9;
  }
  oneof _max_rating_timestamp {
  .google.protobuf.Timestamp max_rating_timestamp = 10;
  }
  oneof _rated_longest_streak {
  int32 rated_longest_streak = 11;
  }
  oneof _rated_longest_streak_timestamp {
  .google.protobuf.Timestamp rated_longest_streak_timestamp = 12;
 
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10882"></a>
## FND-10882: chesscom.user_properties.v1.PuzzlesAttemptedProperty.max_rating = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max_rating = 9;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1926.

```text
ting_timestamp {
  .google.protobuf.Timestamp min_rating_timestamp = 8;
  }
  oneof _max_rating {
  int32 max_rating = 9;
  }
  oneof _max_rating_timestamp {
  .google.protobuf.Timestamp max_rating_timestamp = 10;
  }
  oneof _rated_longest_streak {
  int32 rated_longest_streak = 11;
  }
  oneof _rated_longest_streak_timestamp {
  .google.protobuf.Timestamp rated_longest_streak_timestamp = 12;
  }
  oneof _rated_curr
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10883"></a>
## FND-10883: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._max_rating_timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_rating_timestamp {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1954.

```text
rotobuf.Timestamp min_rating_timestamp = 8;
  }
  oneof _max_rating {
  int32 max_rating = 9;
  }
  oneof _max_rating_timestamp {
  .google.protobuf.Timestamp max_rating_timestamp = 10;
  }
  oneof _rated_longest_streak {
  int32 rated_longest_streak = 11;
  }
  oneof _rated_longest_streak_timestamp {
  .google.protobuf.Timestamp rated_longest_streak_timestamp = 12;
  }
  oneof _rated_current_streak {
  int32 rated_c
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10884"></a>
## FND-10884: chesscom.user_properties.v1.PuzzlesAttemptedProperty.max_rating_timestamp = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp max_rating_timestamp = 10;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 1986.

```text
estamp = 8;
  }
  oneof _max_rating {
  int32 max_rating = 9;
  }
  oneof _max_rating_timestamp {
  .google.protobuf.Timestamp max_rating_timestamp = 10;
  }
  oneof _rated_longest_streak {
  int32 rated_longest_streak = 11;
  }
  oneof _rated_longest_streak_timestamp {
  .google.protobuf.Timestamp rated_longest_streak_timestamp = 12;
  }
  oneof _rated_current_streak {
  int32 rated_current_streak = 13;
  }
  oneof 
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10885"></a>
## FND-10885: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._rated_longest_streak

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rated_longest_streak {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2046.

```text
;
  }
  oneof _max_rating_timestamp {
  .google.protobuf.Timestamp max_rating_timestamp = 10;
  }
  oneof _rated_longest_streak {
  int32 rated_longest_streak = 11;
  }
  oneof _rated_longest_streak_timestamp {
  .google.protobuf.Timestamp rated_longest_streak_timestamp = 12;
  }
  oneof _rated_current_streak {
  int32 rated_current_streak = 13;
  }
  oneof _history_reset_last_timestamp {
  .google.protobuf.Timestamp
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10886"></a>
## FND-10886: chesscom.user_properties.v1.PuzzlesAttemptedProperty.rated_longest_streak = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rated_longest_streak = 11;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2078.

```text
amp {
  .google.protobuf.Timestamp max_rating_timestamp = 10;
  }
  oneof _rated_longest_streak {
  int32 rated_longest_streak = 11;
  }
  oneof _rated_longest_streak_timestamp {
  .google.protobuf.Timestamp rated_longest_streak_timestamp = 12;
  }
  oneof _rated_current_streak {
  int32 rated_current_streak = 13;
  }
  oneof _history_reset_last_timestamp {
  .google.protobuf.Timestamp history_reset_last_timestamp = 
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10887"></a>
## FND-10887: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._rated_longest_streak_timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rated_longest_streak_timestamp {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2117.

```text
rating_timestamp = 10;
  }
  oneof _rated_longest_streak {
  int32 rated_longest_streak = 11;
  }
  oneof _rated_longest_streak_timestamp {
  .google.protobuf.Timestamp rated_longest_streak_timestamp = 12;
  }
  oneof _rated_current_streak {
  int32 rated_current_streak = 13;
  }
  oneof _history_reset_last_timestamp {
  .google.protobuf.Timestamp history_reset_last_timestamp = 14;
  }
  oneof _shadow_rating {
  int3
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10888"></a>
## FND-10888: chesscom.user_properties.v1.PuzzlesAttemptedProperty.rated_longest_streak_timestamp = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp rated_longest_streak_timestamp = 12;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2159.

```text
longest_streak {
  int32 rated_longest_streak = 11;
  }
  oneof _rated_longest_streak_timestamp {
  .google.protobuf.Timestamp rated_longest_streak_timestamp = 12;
  }
  oneof _rated_current_streak {
  int32 rated_current_streak = 13;
  }
  oneof _history_reset_last_timestamp {
  .google.protobuf.Timestamp history_reset_last_timestamp = 14;
  }
  oneof _shadow_rating {
  int32 shadow_rating = 15;
  }
  oneof _min_sha
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10889"></a>
## FND-10889: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._rated_current_streak

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rated_current_streak {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2229.

```text
_longest_streak_timestamp {
  .google.protobuf.Timestamp rated_longest_streak_timestamp = 12;
  }
  oneof _rated_current_streak {
  int32 rated_current_streak = 13;
  }
  oneof _history_reset_last_timestamp {
  .google.protobuf.Timestamp history_reset_last_timestamp = 14;
  }
  oneof _shadow_rating {
  int32 shadow_rating = 15;
  }
  oneof _min_shadow_rating {
  int32 min_shadow_rating = 16;
  }
  oneof _min_shadow_r
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10890"></a>
## FND-10890: chesscom.user_properties.v1.PuzzlesAttemptedProperty.rated_current_streak = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rated_current_streak = 13;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2261.

```text
oogle.protobuf.Timestamp rated_longest_streak_timestamp = 12;
  }
  oneof _rated_current_streak {
  int32 rated_current_streak = 13;
  }
  oneof _history_reset_last_timestamp {
  .google.protobuf.Timestamp history_reset_last_timestamp = 14;
  }
  oneof _shadow_rating {
  int32 shadow_rating = 15;
  }
  oneof _min_shadow_rating {
  int32 min_shadow_rating = 16;
  }
  oneof _min_shadow_rating_timestamp {
  .google.prot
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10891"></a>
## FND-10891: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._history_reset_last_timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _history_reset_last_timestamp {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2300.

```text
streak_timestamp = 12;
  }
  oneof _rated_current_streak {
  int32 rated_current_streak = 13;
  }
  oneof _history_reset_last_timestamp {
  .google.protobuf.Timestamp history_reset_last_timestamp = 14;
  }
  oneof _shadow_rating {
  int32 shadow_rating = 15;
  }
  oneof _min_shadow_rating {
  int32 min_shadow_rating = 16;
  }
  oneof _min_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_shadow_rating_timest
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10892"></a>
## FND-10892: chesscom.user_properties.v1.PuzzlesAttemptedProperty.history_reset_last_timestamp = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp history_reset_last_timestamp = 14;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2340.

```text
d_current_streak {
  int32 rated_current_streak = 13;
  }
  oneof _history_reset_last_timestamp {
  .google.protobuf.Timestamp history_reset_last_timestamp = 14;
  }
  oneof _shadow_rating {
  int32 shadow_rating = 15;
  }
  oneof _min_shadow_rating {
  int32 min_shadow_rating = 16;
  }
  oneof _min_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_shadow_rating_timestamp = 17;
  }
  oneof _max_shadow_rating
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10893"></a>
## FND-10893: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._shadow_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _shadow_rating {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2408.

```text
istory_reset_last_timestamp {
  .google.protobuf.Timestamp history_reset_last_timestamp = 14;
  }
  oneof _shadow_rating {
  int32 shadow_rating = 15;
  }
  oneof _min_shadow_rating {
  int32 min_shadow_rating = 16;
  }
  oneof _min_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_shadow_rating_timestamp = 17;
  }
  oneof _max_shadow_rating {
  int32 max_shadow_rating = 18;
  }
  oneof _max_shadow_rating_ti
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10894"></a>
## FND-10894: chesscom.user_properties.v1.PuzzlesAttemptedProperty.shadow_rating = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 shadow_rating = 15;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2433.

```text
mp {
  .google.protobuf.Timestamp history_reset_last_timestamp = 14;
  }
  oneof _shadow_rating {
  int32 shadow_rating = 15;
  }
  oneof _min_shadow_rating {
  int32 min_shadow_rating = 16;
  }
  oneof _min_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_shadow_rating_timestamp = 17;
  }
  oneof _max_shadow_rating {
  int32 max_shadow_rating = 18;
  }
  oneof _max_shadow_rating_timestamp {
  .google.proto
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10895"></a>
## FND-10895: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._min_shadow_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _min_shadow_rating {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2465.

```text
p history_reset_last_timestamp = 14;
  }
  oneof _shadow_rating {
  int32 shadow_rating = 15;
  }
  oneof _min_shadow_rating {
  int32 min_shadow_rating = 16;
  }
  oneof _min_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_shadow_rating_timestamp = 17;
  }
  oneof _max_shadow_rating {
  int32 max_shadow_rating = 18;
  }
  oneof _max_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_shadow_rating_
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10896"></a>
## FND-10896: chesscom.user_properties.v1.PuzzlesAttemptedProperty.min_shadow_rating = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 min_shadow_rating = 16;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2494.

```text
p = 14;
  }
  oneof _shadow_rating {
  int32 shadow_rating = 15;
  }
  oneof _min_shadow_rating {
  int32 min_shadow_rating = 16;
  }
  oneof _min_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_shadow_rating_timestamp = 17;
  }
  oneof _max_shadow_rating {
  int32 max_shadow_rating = 18;
  }
  oneof _max_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_shadow_rating_timestamp = 19;
  }
  oneof _
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10897"></a>
## FND-10897: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._min_shadow_rating_timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _min_shadow_rating_timestamp {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2530.

```text

  int32 shadow_rating = 15;
  }
  oneof _min_shadow_rating {
  int32 min_shadow_rating = 16;
  }
  oneof _min_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_shadow_rating_timestamp = 17;
  }
  oneof _max_shadow_rating {
  int32 max_shadow_rating = 18;
  }
  oneof _max_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_shadow_rating_timestamp = 19;
  }
  oneof _boosted_shadow_rating {
  int32 boos
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10898"></a>
## FND-10898: chesscom.user_properties.v1.PuzzlesAttemptedProperty.min_shadow_rating_timestamp = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp min_shadow_rating_timestamp = 17;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2569.

```text
f _min_shadow_rating {
  int32 min_shadow_rating = 16;
  }
  oneof _min_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_shadow_rating_timestamp = 17;
  }
  oneof _max_shadow_rating {
  int32 max_shadow_rating = 18;
  }
  oneof _max_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_shadow_rating_timestamp = 19;
  }
  oneof _boosted_shadow_rating {
  int32 boosted_shadow_rating = 20;
  }
  oneof _mi
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10899"></a>
## FND-10899: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._max_shadow_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_shadow_rating {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2636.

```text
_min_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_shadow_rating_timestamp = 17;
  }
  oneof _max_shadow_rating {
  int32 max_shadow_rating = 18;
  }
  oneof _max_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_shadow_rating_timestamp = 19;
  }
  oneof _boosted_shadow_rating {
  int32 boosted_shadow_rating = 20;
  }
  oneof _min_boosted_shadow_rating {
  int32 min_boosted_shadow_rating = 21;
 
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10900"></a>
## FND-10900: chesscom.user_properties.v1.PuzzlesAttemptedProperty.max_shadow_rating = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max_shadow_rating = 18;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2665.

```text
{
  .google.protobuf.Timestamp min_shadow_rating_timestamp = 17;
  }
  oneof _max_shadow_rating {
  int32 max_shadow_rating = 18;
  }
  oneof _max_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_shadow_rating_timestamp = 19;
  }
  oneof _boosted_shadow_rating {
  int32 boosted_shadow_rating = 20;
  }
  oneof _min_boosted_shadow_rating {
  int32 min_boosted_shadow_rating = 21;
  }
  oneof _min_boosted_shado
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10901"></a>
## FND-10901: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._max_shadow_rating_timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_shadow_rating_timestamp {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2701.

```text
hadow_rating_timestamp = 17;
  }
  oneof _max_shadow_rating {
  int32 max_shadow_rating = 18;
  }
  oneof _max_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_shadow_rating_timestamp = 19;
  }
  oneof _boosted_shadow_rating {
  int32 boosted_shadow_rating = 20;
  }
  oneof _min_boosted_shadow_rating {
  int32 min_boosted_shadow_rating = 21;
  }
  oneof _min_boosted_shadow_rating_timestamp {
  .google.proto
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10902"></a>
## FND-10902: chesscom.user_properties.v1.PuzzlesAttemptedProperty.max_shadow_rating_timestamp = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp max_shadow_rating_timestamp = 19;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2740.

```text
f _max_shadow_rating {
  int32 max_shadow_rating = 18;
  }
  oneof _max_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_shadow_rating_timestamp = 19;
  }
  oneof _boosted_shadow_rating {
  int32 boosted_shadow_rating = 20;
  }
  oneof _min_boosted_shadow_rating {
  int32 min_boosted_shadow_rating = 21;
  }
  oneof _min_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_boosted_shadow_rating
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10903"></a>
## FND-10903: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._boosted_shadow_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _boosted_shadow_rating {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2807.

```text
_max_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_shadow_rating_timestamp = 19;
  }
  oneof _boosted_shadow_rating {
  int32 boosted_shadow_rating = 20;
  }
  oneof _min_boosted_shadow_rating {
  int32 min_boosted_shadow_rating = 21;
  }
  oneof _min_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_boosted_shadow_rating_timestamp = 22;
  }
  oneof _max_boosted_shadow_rating {
  int32 m
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10904"></a>
## FND-10904: chesscom.user_properties.v1.PuzzlesAttemptedProperty.boosted_shadow_rating = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 boosted_shadow_rating = 20;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2840.

```text
.google.protobuf.Timestamp max_shadow_rating_timestamp = 19;
  }
  oneof _boosted_shadow_rating {
  int32 boosted_shadow_rating = 20;
  }
  oneof _min_boosted_shadow_rating {
  int32 min_boosted_shadow_rating = 21;
  }
  oneof _min_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_boosted_shadow_rating_timestamp = 22;
  }
  oneof _max_boosted_shadow_rating {
  int32 max_boosted_shadow_rating = 23;
  
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10905"></a>
## FND-10905: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._min_boosted_shadow_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _min_boosted_shadow_rating {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2880.

```text
ting_timestamp = 19;
  }
  oneof _boosted_shadow_rating {
  int32 boosted_shadow_rating = 20;
  }
  oneof _min_boosted_shadow_rating {
  int32 min_boosted_shadow_rating = 21;
  }
  oneof _min_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_boosted_shadow_rating_timestamp = 22;
  }
  oneof _max_boosted_shadow_rating {
  int32 max_boosted_shadow_rating = 23;
  }
  oneof _max_boosted_shadow_rating_tim
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10906"></a>
## FND-10906: chesscom.user_properties.v1.PuzzlesAttemptedProperty.min_boosted_shadow_rating = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 min_boosted_shadow_rating = 21;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2917.

```text
sted_shadow_rating {
  int32 boosted_shadow_rating = 20;
  }
  oneof _min_boosted_shadow_rating {
  int32 min_boosted_shadow_rating = 21;
  }
  oneof _min_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_boosted_shadow_rating_timestamp = 22;
  }
  oneof _max_boosted_shadow_rating {
  int32 max_boosted_shadow_rating = 23;
  }
  oneof _max_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10907"></a>
## FND-10907: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._min_boosted_shadow_rating_timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _min_boosted_shadow_rating_timestamp {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 2961.

```text
rating = 20;
  }
  oneof _min_boosted_shadow_rating {
  int32 min_boosted_shadow_rating = 21;
  }
  oneof _min_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_boosted_shadow_rating_timestamp = 22;
  }
  oneof _max_boosted_shadow_rating {
  int32 max_boosted_shadow_rating = 23;
  }
  oneof _max_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_boosted_shadow_rating_timestamp = 24;
 
```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10908"></a>
## FND-10908: chesscom.user_properties.v1.PuzzlesAttemptedProperty.min_boosted_shadow_rating_timestamp = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp min_boosted_shadow_rating_timestamp = 22;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 3008.

```text
ting {
  int32 min_boosted_shadow_rating = 21;
  }
  oneof _min_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp min_boosted_shadow_rating_timestamp = 22;
  }
  oneof _max_boosted_shadow_rating {
  int32 max_boosted_shadow_rating = 23;
  }
  oneof _max_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_boosted_shadow_rating_timestamp = 24;
  }
}

```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10909"></a>
## FND-10909: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._max_boosted_shadow_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_boosted_shadow_rating {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 3083.

```text
dow_rating_timestamp {
  .google.protobuf.Timestamp min_boosted_shadow_rating_timestamp = 22;
  }
  oneof _max_boosted_shadow_rating {
  int32 max_boosted_shadow_rating = 23;
  }
  oneof _max_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_boosted_shadow_rating_timestamp = 24;
  }
}

```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10910"></a>
## FND-10910: chesscom.user_properties.v1.PuzzlesAttemptedProperty.max_boosted_shadow_rating = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 max_boosted_shadow_rating = 23;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 3120.

```text
obuf.Timestamp min_boosted_shadow_rating_timestamp = 22;
  }
  oneof _max_boosted_shadow_rating {
  int32 max_boosted_shadow_rating = 23;
  }
  oneof _max_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_boosted_shadow_rating_timestamp = 24;
  }
}

```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10911"></a>
## FND-10911: oneof declaration: chesscom.user_properties.v1.PuzzlesAttemptedProperty._max_boosted_shadow_rating_timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _max_boosted_shadow_rating_timestamp {

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 3164.

```text
estamp = 22;
  }
  oneof _max_boosted_shadow_rating {
  int32 max_boosted_shadow_rating = 23;
  }
  oneof _max_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_boosted_shadow_rating_timestamp = 24;
  }
}

```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10912"></a>
## FND-10912: chesscom.user_properties.v1.PuzzlesAttemptedProperty.max_boosted_shadow_rating_timestamp = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp max_boosted_shadow_rating_timestamp = 24;

### Evidence

- **SRC-0624** `research/proto/chesscom/user_properties/v1/properties_puzzles_attempted.proto` — [preserved redacted evidence](../evidence/text/c3c59a6f7bf9544e01c19a58d8620bb4ac1acfd5acf3a937e3cf3da9a91302c2.proto)
  Character offset 3211.

```text
ting {
  int32 max_boosted_shadow_rating = 23;
  }
  oneof _max_boosted_shadow_rating_timestamp {
  .google.protobuf.Timestamp max_boosted_shadow_rating_timestamp = 24;
  }
}

```

**Source references:** SRC-0624, SRC-1595  
**URL references:** None independently associated  
**Related findings:** FND-10838, FND-10839, FND-10840

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10913"></a>
## FND-10913: enum declaration: chesscom.user_properties.v1.RatingsPropertyDefinition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum RatingsPropertyDefinition {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 121.

```text
ser_properties/v1/properties_ratings.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum RatingsPropertyDefinition {
  RATING_PROPERTY_UNSPECIFIED = 0;
  RATING_CHESS_BLITZ = 1;
  RATING_CHESS_BULLET = 2;
  RATING_CHESS_DAILY = 3;
  RATING_CHESS_RAPID = 4;
  RATING_CHESS960_BLITZ = 5;
  RATING_CHESS960_BULLET = 6;
  RATING_CHESS960_DAILY = 7;
  RATING_CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RAT
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10914"></a>
## FND-10914: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_PROPERTY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_PROPERTY_UNSPECIFIED = 0;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 156.

```text
s.proto
// syntax: proto3

package chesscom.user_properties.v1;

enum RatingsPropertyDefinition {
  RATING_PROPERTY_UNSPECIFIED = 0;
  RATING_CHESS_BLITZ = 1;
  RATING_CHESS_BULLET = 2;
  RATING_CHESS_DAILY = 3;
  RATING_CHESS_RAPID = 4;
  RATING_CHESS960_BLITZ = 5;
  RATING_CHESS960_BULLET = 6;
  RATING_CHESS960_DAILY = 7;
  RATING_CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFT
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10915"></a>
## FND-10915: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_CHESS_BLITZ = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CHESS_BLITZ = 1;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 191.

```text
chesscom.user_properties.v1;

enum RatingsPropertyDefinition {
  RATING_PROPERTY_UNSPECIFIED = 0;
  RATING_CHESS_BLITZ = 1;
  RATING_CHESS_BULLET = 2;
  RATING_CHESS_DAILY = 3;
  RATING_CHESS_RAPID = 4;
  RATING_CHESS960_BLITZ = 5;
  RATING_CHESS960_BULLET = 6;
  RATING_CHESS960_DAILY = 7;
  RATING_CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 1
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10916"></a>
## FND-10916: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_CHESS_BULLET = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CHESS_BULLET = 2;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 217.

```text
1;

enum RatingsPropertyDefinition {
  RATING_PROPERTY_UNSPECIFIED = 0;
  RATING_CHESS_BLITZ = 1;
  RATING_CHESS_BULLET = 2;
  RATING_CHESS_DAILY = 3;
  RATING_CHESS_RAPID = 4;
  RATING_CHESS960_BLITZ = 5;
  RATING_CHESS960_BULLET = 6;
  RATING_CHESS960_DAILY = 7;
  RATING_CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 1
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10917"></a>
## FND-10917: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_CHESS_DAILY = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CHESS_DAILY = 3;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 244.

```text
inition {
  RATING_PROPERTY_UNSPECIFIED = 0;
  RATING_CHESS_BLITZ = 1;
  RATING_CHESS_BULLET = 2;
  RATING_CHESS_DAILY = 3;
  RATING_CHESS_RAPID = 4;
  RATING_CHESS960_BLITZ = 5;
  RATING_CHESS960_BULLET = 6;
  RATING_CHESS960_DAILY = 7;
  RATING_CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RAT
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10918"></a>
## FND-10918: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_CHESS_RAPID = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CHESS_RAPID = 4;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 270.

```text
Y_UNSPECIFIED = 0;
  RATING_CHESS_BLITZ = 1;
  RATING_CHESS_BULLET = 2;
  RATING_CHESS_DAILY = 3;
  RATING_CHESS_RAPID = 4;
  RATING_CHESS960_BLITZ = 5;
  RATING_CHESS960_BULLET = 6;
  RATING_CHESS960_DAILY = 7;
  RATING_CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
 
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10919"></a>
## FND-10919: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_CHESS960_BLITZ = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CHESS960_BLITZ = 5;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 296.

```text
G_CHESS_BLITZ = 1;
  RATING_CHESS_BULLET = 2;
  RATING_CHESS_DAILY = 3;
  RATING_CHESS_RAPID = 4;
  RATING_CHESS960_BLITZ = 5;
  RATING_CHESS960_BULLET = 6;
  RATING_CHESS960_DAILY = 7;
  RATING_CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10920"></a>
## FND-10920: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_CHESS960_BULLET = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CHESS960_BULLET = 6;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 325.

```text
HESS_BULLET = 2;
  RATING_CHESS_DAILY = 3;
  RATING_CHESS_RAPID = 4;
  RATING_CHESS960_BLITZ = 5;
  RATING_CHESS960_BULLET = 6;
  RATING_CHESS960_DAILY = 7;
  RATING_CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD =
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10921"></a>
## FND-10921: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_CHESS960_DAILY = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CHESS960_DAILY = 7;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 355.

```text
S_DAILY = 3;
  RATING_CHESS_RAPID = 4;
  RATING_CHESS960_BLITZ = 5;
  RATING_CHESS960_BULLET = 6;
  RATING_CHESS960_DAILY = 7;
  RATING_CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD =
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10922"></a>
## FND-10922: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_CHESS960_RAPID = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CHESS960_RAPID = 8;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 384.

```text
APID = 4;
  RATING_CHESS960_BLITZ = 5;
  RATING_CHESS960_BULLET = 6;
  RATING_CHESS960_DAILY = 7;
  RATING_CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RA
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10923"></a>
## FND-10923: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_CRAZYHOUSE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CRAZYHOUSE = 9;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 413.

```text
LITZ = 5;
  RATING_CHESS960_BULLET = 6;
  RATING_CHESS960_DAILY = 7;
  RATING_CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

messa
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10924"></a>
## FND-10924: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_BUGHOUSE = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_BUGHOUSE = 10;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 438.

```text
60_BULLET = 6;
  RATING_CHESS960_DAILY = 7;
  RATING_CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  on
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10925"></a>
## FND-10925: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_KINGOFTHEHILL = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_KINGOFTHEHILL = 11;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 462.

```text
CHESS960_DAILY = 7;
  RATING_CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  oneof _rating_chess_blitz 
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10926"></a>
## FND-10926: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_ODDSCHESS = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_ODDSCHESS = 12;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 491.

```text
CHESS960_RAPID = 8;
  RATING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  oneof _rating_chess_blitz {
  int32 rating_chess_blitz 
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10927"></a>
## FND-10927: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_THREECHECK = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_THREECHECK = 13;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 516.

```text
ING_CRAZYHOUSE = 9;
  RATING_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  oneof _rating_chess_blitz {
  int32 rating_chess_blitz = 1;
  }
  oneof _rating_
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10928"></a>
## FND-10928: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_ONE = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_ONE = 14;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 542.

```text
NG_BUGHOUSE = 10;
  RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  oneof _rating_chess_blitz {
  int32 rating_chess_blitz = 1;
  }
  oneof _rating_chess_bullet {
  int32 rat
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10929"></a>
## FND-10929: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_CHESS_BLITZ_RD = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CHESS_BLITZ_RD = 15;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 561.

```text
 RATING_KINGOFTHEHILL = 11;
  RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  oneof _rating_chess_blitz {
  int32 rating_chess_blitz = 1;
  }
  oneof _rating_chess_bullet {
  int32 rating_chess_bullet = 
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10930"></a>
## FND-10930: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_CHESS_BULLET_RD = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CHESS_BULLET_RD = 16;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 591.

```text
RATING_ODDSCHESS = 12;
  RATING_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  oneof _rating_chess_blitz {
  int32 rating_chess_blitz = 1;
  }
  oneof _rating_chess_bullet {
  int32 rating_chess_bullet = 2;
  }
  oneof _rating_chess_d
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10931"></a>
## FND-10931: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_CHESS_DAILY_RD = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CHESS_DAILY_RD = 17;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 622.

```text
_THREECHECK = 13;
  RATING_ONE = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  oneof _rating_chess_blitz {
  int32 rating_chess_blitz = 1;
  }
  oneof _rating_chess_bullet {
  int32 rating_chess_bullet = 2;
  }
  oneof _rating_chess_daily {
  int32 rating_chess_dai
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10932"></a>
## FND-10932: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_CHESS_RAPID_RD = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_CHESS_RAPID_RD = 18;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 652.

```text
 = 14;
  RATING_CHESS_BLITZ_RD = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  oneof _rating_chess_blitz {
  int32 rating_chess_blitz = 1;
  }
  oneof _rating_chess_bullet {
  int32 rating_chess_bullet = 2;
  }
  oneof _rating_chess_daily {
  int32 rating_chess_daily = 3;
  }
  oneof _rating_ch
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10933"></a>
## FND-10933: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_BEST = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_BEST = 19;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 682.

```text
 = 15;
  RATING_CHESS_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  oneof _rating_chess_blitz {
  int32 rating_chess_blitz = 1;
  }
  oneof _rating_chess_bullet {
  int32 rating_chess_bullet = 2;
  }
  oneof _rating_chess_daily {
  int32 rating_chess_daily = 3;
  }
  oneof _rating_chess_rapid {
  int32 rating_che
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10934"></a>
## FND-10934: chesscom.user_properties.v1.RatingsPropertyDefinition.RATING_BEST_TYPE = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RATING_BEST_TYPE = 20;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 702.

```text
S_BULLET_RD = 16;
  RATING_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  oneof _rating_chess_blitz {
  int32 rating_chess_blitz = 1;
  }
  oneof _rating_chess_bullet {
  int32 rating_chess_bullet = 2;
  }
  oneof _rating_chess_daily {
  int32 rating_chess_daily = 3;
  }
  oneof _rating_chess_rapid {
  int32 rating_chess_rapid = 4;
  }
  
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10935"></a>
## FND-10935: message declaration: chesscom.user_properties.v1.RatingsProperty

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RatingsProperty {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 728.

```text
_CHESS_DAILY_RD = 17;
  RATING_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  oneof _rating_chess_blitz {
  int32 rating_chess_blitz = 1;
  }
  oneof _rating_chess_bullet {
  int32 rating_chess_bullet = 2;
  }
  oneof _rating_chess_daily {
  int32 rating_chess_daily = 3;
  }
  oneof _rating_chess_rapid {
  int32 rating_chess_rapid = 4;
  }
  oneof _rating_chess960_bli
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10936"></a>
## FND-10936: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_chess_blitz

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_chess_blitz {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 756.

```text
NG_CHESS_RAPID_RD = 18;
  RATING_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  oneof _rating_chess_blitz {
  int32 rating_chess_blitz = 1;
  }
  oneof _rating_chess_bullet {
  int32 rating_chess_bullet = 2;
  }
  oneof _rating_chess_daily {
  int32 rating_chess_daily = 3;
  }
  oneof _rating_chess_rapid {
  int32 rating_chess_rapid = 4;
  }
  oneof _rating_chess960_blitz {
  int32 rating_chess960
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10937"></a>
## FND-10937: chesscom.user_properties.v1.RatingsProperty.rating_chess_blitz = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_chess_blitz = 1;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 786.

```text
NG_BEST = 19;
  RATING_BEST_TYPE = 20;
}

message RatingsProperty {
  oneof _rating_chess_blitz {
  int32 rating_chess_blitz = 1;
  }
  oneof _rating_chess_bullet {
  int32 rating_chess_bullet = 2;
  }
  oneof _rating_chess_daily {
  int32 rating_chess_daily = 3;
  }
  oneof _rating_chess_rapid {
  int32 rating_chess_rapid = 4;
  }
  oneof _rating_chess960_blitz {
  int32 rating_chess960_blitz = 5;
  }
  oneof _ratin
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10938"></a>
## FND-10938: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_chess_bullet

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_chess_bullet {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 822.

```text
0;
}

message RatingsProperty {
  oneof _rating_chess_blitz {
  int32 rating_chess_blitz = 1;
  }
  oneof _rating_chess_bullet {
  int32 rating_chess_bullet = 2;
  }
  oneof _rating_chess_daily {
  int32 rating_chess_daily = 3;
  }
  oneof _rating_chess_rapid {
  int32 rating_chess_rapid = 4;
  }
  oneof _rating_chess960_blitz {
  int32 rating_chess960_blitz = 5;
  }
  oneof _rating_chess960_bullet {
  int32 rating_c
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10939"></a>
## FND-10939: chesscom.user_properties.v1.RatingsProperty.rating_chess_bullet = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_chess_bullet = 2;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 853.

```text

  oneof _rating_chess_blitz {
  int32 rating_chess_blitz = 1;
  }
  oneof _rating_chess_bullet {
  int32 rating_chess_bullet = 2;
  }
  oneof _rating_chess_daily {
  int32 rating_chess_daily = 3;
  }
  oneof _rating_chess_rapid {
  int32 rating_chess_rapid = 4;
  }
  oneof _rating_chess960_blitz {
  int32 rating_chess960_blitz = 5;
  }
  oneof _rating_chess960_bullet {
  int32 rating_chess960_bullet = 6;
  }
  oneof
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10940"></a>
## FND-10940: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_chess_daily

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_chess_daily {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 890.

```text
2 rating_chess_blitz = 1;
  }
  oneof _rating_chess_bullet {
  int32 rating_chess_bullet = 2;
  }
  oneof _rating_chess_daily {
  int32 rating_chess_daily = 3;
  }
  oneof _rating_chess_rapid {
  int32 rating_chess_rapid = 4;
  }
  oneof _rating_chess960_blitz {
  int32 rating_chess960_blitz = 5;
  }
  oneof _rating_chess960_bullet {
  int32 rating_chess960_bullet = 6;
  }
  oneof _rating_chess960_daily {
  int32 rat
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10941"></a>
## FND-10941: chesscom.user_properties.v1.RatingsProperty.rating_chess_daily = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_chess_daily = 3;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 920.

```text
  oneof _rating_chess_bullet {
  int32 rating_chess_bullet = 2;
  }
  oneof _rating_chess_daily {
  int32 rating_chess_daily = 3;
  }
  oneof _rating_chess_rapid {
  int32 rating_chess_rapid = 4;
  }
  oneof _rating_chess960_blitz {
  int32 rating_chess960_blitz = 5;
  }
  oneof _rating_chess960_bullet {
  int32 rating_chess960_bullet = 6;
  }
  oneof _rating_chess960_daily {
  int32 rating_chess960_daily = 7;
  }
  
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10942"></a>
## FND-10942: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_chess_rapid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_chess_rapid {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 956.

```text
32 rating_chess_bullet = 2;
  }
  oneof _rating_chess_daily {
  int32 rating_chess_daily = 3;
  }
  oneof _rating_chess_rapid {
  int32 rating_chess_rapid = 4;
  }
  oneof _rating_chess960_blitz {
  int32 rating_chess960_blitz = 5;
  }
  oneof _rating_chess960_bullet {
  int32 rating_chess960_bullet = 6;
  }
  oneof _rating_chess960_daily {
  int32 rating_chess960_daily = 7;
  }
  oneof _rating_chess960_rapid {
  int
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10943"></a>
## FND-10943: chesscom.user_properties.v1.RatingsProperty.rating_chess_rapid = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_chess_rapid = 4;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 986.

```text
}
  oneof _rating_chess_daily {
  int32 rating_chess_daily = 3;
  }
  oneof _rating_chess_rapid {
  int32 rating_chess_rapid = 4;
  }
  oneof _rating_chess960_blitz {
  int32 rating_chess960_blitz = 5;
  }
  oneof _rating_chess960_bullet {
  int32 rating_chess960_bullet = 6;
  }
  oneof _rating_chess960_daily {
  int32 rating_chess960_daily = 7;
  }
  oneof _rating_chess960_rapid {
  int32 rating_chess960_rapid = 8;

```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10944"></a>
## FND-10944: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_chess960_blitz

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_chess960_blitz {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1022.

```text
t32 rating_chess_daily = 3;
  }
  oneof _rating_chess_rapid {
  int32 rating_chess_rapid = 4;
  }
  oneof _rating_chess960_blitz {
  int32 rating_chess960_blitz = 5;
  }
  oneof _rating_chess960_bullet {
  int32 rating_chess960_bullet = 6;
  }
  oneof _rating_chess960_daily {
  int32 rating_chess960_daily = 7;
  }
  oneof _rating_chess960_rapid {
  int32 rating_chess960_rapid = 8;
  }
  oneof _rating_crazyhouse {
  i
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10945"></a>
## FND-10945: chesscom.user_properties.v1.RatingsProperty.rating_chess960_blitz = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_chess960_blitz = 5;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1055.

```text
 oneof _rating_chess_rapid {
  int32 rating_chess_rapid = 4;
  }
  oneof _rating_chess960_blitz {
  int32 rating_chess960_blitz = 5;
  }
  oneof _rating_chess960_bullet {
  int32 rating_chess960_bullet = 6;
  }
  oneof _rating_chess960_daily {
  int32 rating_chess960_daily = 7;
  }
  oneof _rating_chess960_rapid {
  int32 rating_chess960_rapid = 8;
  }
  oneof _rating_crazyhouse {
  int32 rating_crazyhouse = 9;
  }
 
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10946"></a>
## FND-10946: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_chess960_bullet

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_chess960_bullet {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1094.

```text
ting_chess_rapid = 4;
  }
  oneof _rating_chess960_blitz {
  int32 rating_chess960_blitz = 5;
  }
  oneof _rating_chess960_bullet {
  int32 rating_chess960_bullet = 6;
  }
  oneof _rating_chess960_daily {
  int32 rating_chess960_daily = 7;
  }
  oneof _rating_chess960_rapid {
  int32 rating_chess960_rapid = 8;
  }
  oneof _rating_crazyhouse {
  int32 rating_crazyhouse = 9;
  }
  oneof _rating_bughouse {
  int32 ratin
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10947"></a>
## FND-10947: chesscom.user_properties.v1.RatingsProperty.rating_chess960_bullet = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_chess960_bullet = 6;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1128.

```text
_rating_chess960_blitz {
  int32 rating_chess960_blitz = 5;
  }
  oneof _rating_chess960_bullet {
  int32 rating_chess960_bullet = 6;
  }
  oneof _rating_chess960_daily {
  int32 rating_chess960_daily = 7;
  }
  oneof _rating_chess960_rapid {
  int32 rating_chess960_rapid = 8;
  }
  oneof _rating_crazyhouse {
  int32 rating_crazyhouse = 9;
  }
  oneof _rating_bughouse {
  int32 rating_bughouse = 10;
  }
  oneof _rati
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10948"></a>
## FND-10948: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_chess960_daily

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_chess960_daily {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1168.

```text
chess960_blitz = 5;
  }
  oneof _rating_chess960_bullet {
  int32 rating_chess960_bullet = 6;
  }
  oneof _rating_chess960_daily {
  int32 rating_chess960_daily = 7;
  }
  oneof _rating_chess960_rapid {
  int32 rating_chess960_rapid = 8;
  }
  oneof _rating_crazyhouse {
  int32 rating_crazyhouse = 9;
  }
  oneof _rating_bughouse {
  int32 rating_bughouse = 10;
  }
  oneof _rating_kingofthehill {
  int32 rating_kingof
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10949"></a>
## FND-10949: chesscom.user_properties.v1.RatingsProperty.rating_chess960_daily = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_chess960_daily = 7;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1201.

```text
rating_chess960_bullet {
  int32 rating_chess960_bullet = 6;
  }
  oneof _rating_chess960_daily {
  int32 rating_chess960_daily = 7;
  }
  oneof _rating_chess960_rapid {
  int32 rating_chess960_rapid = 8;
  }
  oneof _rating_crazyhouse {
  int32 rating_crazyhouse = 9;
  }
  oneof _rating_bughouse {
  int32 rating_bughouse = 10;
  }
  oneof _rating_kingofthehill {
  int32 rating_kingofthehill = 11;
  }
  oneof _rating
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10950"></a>
## FND-10950: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_chess960_rapid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_chess960_rapid {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1240.

```text
_chess960_bullet = 6;
  }
  oneof _rating_chess960_daily {
  int32 rating_chess960_daily = 7;
  }
  oneof _rating_chess960_rapid {
  int32 rating_chess960_rapid = 8;
  }
  oneof _rating_crazyhouse {
  int32 rating_crazyhouse = 9;
  }
  oneof _rating_bughouse {
  int32 rating_bughouse = 10;
  }
  oneof _rating_kingofthehill {
  int32 rating_kingofthehill = 11;
  }
  oneof _rating_oddschess {
  int32 rating_oddschess =
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10951"></a>
## FND-10951: chesscom.user_properties.v1.RatingsProperty.rating_chess960_rapid = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_chess960_rapid = 8;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1273.

```text
 _rating_chess960_daily {
  int32 rating_chess960_daily = 7;
  }
  oneof _rating_chess960_rapid {
  int32 rating_chess960_rapid = 8;
  }
  oneof _rating_crazyhouse {
  int32 rating_crazyhouse = 9;
  }
  oneof _rating_bughouse {
  int32 rating_bughouse = 10;
  }
  oneof _rating_kingofthehill {
  int32 rating_kingofthehill = 11;
  }
  oneof _rating_oddschess {
  int32 rating_oddschess = 12;
  }
  oneof _rating_threeche
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10952"></a>
## FND-10952: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_crazyhouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_crazyhouse {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1312.

```text
g_chess960_daily = 7;
  }
  oneof _rating_chess960_rapid {
  int32 rating_chess960_rapid = 8;
  }
  oneof _rating_crazyhouse {
  int32 rating_crazyhouse = 9;
  }
  oneof _rating_bughouse {
  int32 rating_bughouse = 10;
  }
  oneof _rating_kingofthehill {
  int32 rating_kingofthehill = 11;
  }
  oneof _rating_oddschess {
  int32 rating_oddschess = 12;
  }
  oneof _rating_threecheck {
  int32 rating_threecheck = 13;
  
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10953"></a>
## FND-10953: chesscom.user_properties.v1.RatingsProperty.rating_crazyhouse = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_crazyhouse = 9;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1341.

```text
neof _rating_chess960_rapid {
  int32 rating_chess960_rapid = 8;
  }
  oneof _rating_crazyhouse {
  int32 rating_crazyhouse = 9;
  }
  oneof _rating_bughouse {
  int32 rating_bughouse = 10;
  }
  oneof _rating_kingofthehill {
  int32 rating_kingofthehill = 11;
  }
  oneof _rating_oddschess {
  int32 rating_oddschess = 12;
  }
  oneof _rating_threecheck {
  int32 rating_threecheck = 13;
  }
  oneof _rating_one {
  int
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10954"></a>
## FND-10954: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_bughouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_bughouse {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1376.

```text
32 rating_chess960_rapid = 8;
  }
  oneof _rating_crazyhouse {
  int32 rating_crazyhouse = 9;
  }
  oneof _rating_bughouse {
  int32 rating_bughouse = 10;
  }
  oneof _rating_kingofthehill {
  int32 rating_kingofthehill = 11;
  }
  oneof _rating_oddschess {
  int32 rating_oddschess = 12;
  }
  oneof _rating_threecheck {
  int32 rating_threecheck = 13;
  }
  oneof _rating_one {
  int32 rating_one = 14;
  }
  oneof _ra
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10955"></a>
## FND-10955: chesscom.user_properties.v1.RatingsProperty.rating_bughouse = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_bughouse = 10;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1403.

```text
8;
  }
  oneof _rating_crazyhouse {
  int32 rating_crazyhouse = 9;
  }
  oneof _rating_bughouse {
  int32 rating_bughouse = 10;
  }
  oneof _rating_kingofthehill {
  int32 rating_kingofthehill = 11;
  }
  oneof _rating_oddschess {
  int32 rating_oddschess = 12;
  }
  oneof _rating_threecheck {
  int32 rating_threecheck = 13;
  }
  oneof _rating_one {
  int32 rating_one = 14;
  }
  oneof _rating_chess_blitz_rd {
  dou
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10956"></a>
## FND-10956: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_kingofthehill

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_kingofthehill {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1437.

```text
{
  int32 rating_crazyhouse = 9;
  }
  oneof _rating_bughouse {
  int32 rating_bughouse = 10;
  }
  oneof _rating_kingofthehill {
  int32 rating_kingofthehill = 11;
  }
  oneof _rating_oddschess {
  int32 rating_oddschess = 12;
  }
  oneof _rating_threecheck {
  int32 rating_threecheck = 13;
  }
  oneof _rating_one {
  int32 rating_one = 14;
  }
  oneof _rating_chess_blitz_rd {
  double rating_chess_blitz_rd = 15;
  
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10957"></a>
## FND-10957: chesscom.user_properties.v1.RatingsProperty.rating_kingofthehill = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_kingofthehill = 11;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1469.

```text

  }
  oneof _rating_bughouse {
  int32 rating_bughouse = 10;
  }
  oneof _rating_kingofthehill {
  int32 rating_kingofthehill = 11;
  }
  oneof _rating_oddschess {
  int32 rating_oddschess = 12;
  }
  oneof _rating_threecheck {
  int32 rating_threecheck = 13;
  }
  oneof _rating_one {
  int32 rating_one = 14;
  }
  oneof _rating_chess_blitz_rd {
  double rating_chess_blitz_rd = 15;
  }
  oneof _rating_chess_bullet_r
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10958"></a>
## FND-10958: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_oddschess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_oddschess {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1508.

```text
 rating_bughouse = 10;
  }
  oneof _rating_kingofthehill {
  int32 rating_kingofthehill = 11;
  }
  oneof _rating_oddschess {
  int32 rating_oddschess = 12;
  }
  oneof _rating_threecheck {
  int32 rating_threecheck = 13;
  }
  oneof _rating_one {
  int32 rating_one = 14;
  }
  oneof _rating_chess_blitz_rd {
  double rating_chess_blitz_rd = 15;
  }
  oneof _rating_chess_bullet_rd {
  double rating_chess_bullet_rd = 1
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10959"></a>
## FND-10959: chesscom.user_properties.v1.RatingsProperty.rating_oddschess = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_oddschess = 12;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1536.

```text
 oneof _rating_kingofthehill {
  int32 rating_kingofthehill = 11;
  }
  oneof _rating_oddschess {
  int32 rating_oddschess = 12;
  }
  oneof _rating_threecheck {
  int32 rating_threecheck = 13;
  }
  oneof _rating_one {
  int32 rating_one = 14;
  }
  oneof _rating_chess_blitz_rd {
  double rating_chess_blitz_rd = 15;
  }
  oneof _rating_chess_bullet_rd {
  double rating_chess_bullet_rd = 16;
  }
  oneof _rating_chess
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10960"></a>
## FND-10960: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_threecheck

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_threecheck {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1571.

```text
t32 rating_kingofthehill = 11;
  }
  oneof _rating_oddschess {
  int32 rating_oddschess = 12;
  }
  oneof _rating_threecheck {
  int32 rating_threecheck = 13;
  }
  oneof _rating_one {
  int32 rating_one = 14;
  }
  oneof _rating_chess_blitz_rd {
  double rating_chess_blitz_rd = 15;
  }
  oneof _rating_chess_bullet_rd {
  double rating_chess_bullet_rd = 16;
  }
  oneof _rating_chess_daily_rd {
  double rating_chess_d
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10961"></a>
## FND-10961: chesscom.user_properties.v1.RatingsProperty.rating_threecheck = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_threecheck = 13;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1600.

```text
;
  }
  oneof _rating_oddschess {
  int32 rating_oddschess = 12;
  }
  oneof _rating_threecheck {
  int32 rating_threecheck = 13;
  }
  oneof _rating_one {
  int32 rating_one = 14;
  }
  oneof _rating_chess_blitz_rd {
  double rating_chess_blitz_rd = 15;
  }
  oneof _rating_chess_bullet_rd {
  double rating_chess_bullet_rd = 16;
  }
  oneof _rating_chess_daily_rd {
  double rating_chess_daily_rd = 17;
  }
  oneof _ra
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10962"></a>
## FND-10962: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_one

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_one {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1636.

```text
int32 rating_oddschess = 12;
  }
  oneof _rating_threecheck {
  int32 rating_threecheck = 13;
  }
  oneof _rating_one {
  int32 rating_one = 14;
  }
  oneof _rating_chess_blitz_rd {
  double rating_chess_blitz_rd = 15;
  }
  oneof _rating_chess_bullet_rd {
  double rating_chess_bullet_rd = 16;
  }
  oneof _rating_chess_daily_rd {
  double rating_chess_daily_rd = 17;
  }
  oneof _rating_chess_rapid_rd {
  double ratin
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10963"></a>
## FND-10963: chesscom.user_properties.v1.RatingsProperty.rating_one = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_one = 14;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1658.

```text
 = 12;
  }
  oneof _rating_threecheck {
  int32 rating_threecheck = 13;
  }
  oneof _rating_one {
  int32 rating_one = 14;
  }
  oneof _rating_chess_blitz_rd {
  double rating_chess_blitz_rd = 15;
  }
  oneof _rating_chess_bullet_rd {
  double rating_chess_bullet_rd = 16;
  }
  oneof _rating_chess_daily_rd {
  double rating_chess_daily_rd = 17;
  }
  oneof _rating_chess_rapid_rd {
  double rating_chess_rapid_rd = 18;
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10964"></a>
## FND-10964: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_chess_blitz_rd

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_chess_blitz_rd {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1687.

```text
reecheck {
  int32 rating_threecheck = 13;
  }
  oneof _rating_one {
  int32 rating_one = 14;
  }
  oneof _rating_chess_blitz_rd {
  double rating_chess_blitz_rd = 15;
  }
  oneof _rating_chess_bullet_rd {
  double rating_chess_bullet_rd = 16;
  }
  oneof _rating_chess_daily_rd {
  double rating_chess_daily_rd = 17;
  }
  oneof _rating_chess_rapid_rd {
  double rating_chess_rapid_rd = 18;
  }
  oneof _rating_best {
 
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10965"></a>
## FND-10965: chesscom.user_properties.v1.RatingsProperty.rating_chess_blitz_rd = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double rating_chess_blitz_rd = 15;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1720.

```text
eck = 13;
  }
  oneof _rating_one {
  int32 rating_one = 14;
  }
  oneof _rating_chess_blitz_rd {
  double rating_chess_blitz_rd = 15;
  }
  oneof _rating_chess_bullet_rd {
  double rating_chess_bullet_rd = 16;
  }
  oneof _rating_chess_daily_rd {
  double rating_chess_daily_rd = 17;
  }
  oneof _rating_chess_rapid_rd {
  double rating_chess_rapid_rd = 18;
  }
  oneof _rating_best {
  int32 rating_best = 19;
  }
  on
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10966"></a>
## FND-10966: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_chess_bullet_rd

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_chess_bullet_rd {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1761.

```text
32 rating_one = 14;
  }
  oneof _rating_chess_blitz_rd {
  double rating_chess_blitz_rd = 15;
  }
  oneof _rating_chess_bullet_rd {
  double rating_chess_bullet_rd = 16;
  }
  oneof _rating_chess_daily_rd {
  double rating_chess_daily_rd = 17;
  }
  oneof _rating_chess_rapid_rd {
  double rating_chess_rapid_rd = 18;
  }
  oneof _rating_best {
  int32 rating_best = 19;
  }
  oneof _rating_best_type {
  string rating_b
```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10967"></a>
## FND-10967: chesscom.user_properties.v1.RatingsProperty.rating_chess_bullet_rd = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double rating_chess_bullet_rd = 16;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1795.

```text
ating_chess_blitz_rd {
  double rating_chess_blitz_rd = 15;
  }
  oneof _rating_chess_bullet_rd {
  double rating_chess_bullet_rd = 16;
  }
  oneof _rating_chess_daily_rd {
  double rating_chess_daily_rd = 17;
  }
  oneof _rating_chess_rapid_rd {
  double rating_chess_rapid_rd = 18;
  }
  oneof _rating_best {
  int32 rating_best = 19;
  }
  oneof _rating_best_type {
  string rating_best_type = 20;
  }
}

```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10968"></a>
## FND-10968: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_chess_daily_rd

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_chess_daily_rd {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1837.

```text
ss_blitz_rd = 15;
  }
  oneof _rating_chess_bullet_rd {
  double rating_chess_bullet_rd = 16;
  }
  oneof _rating_chess_daily_rd {
  double rating_chess_daily_rd = 17;
  }
  oneof _rating_chess_rapid_rd {
  double rating_chess_rapid_rd = 18;
  }
  oneof _rating_best {
  int32 rating_best = 19;
  }
  oneof _rating_best_type {
  string rating_best_type = 20;
  }
}

```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10969"></a>
## FND-10969: chesscom.user_properties.v1.RatingsProperty.rating_chess_daily_rd = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double rating_chess_daily_rd = 17;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1870.

```text
ting_chess_bullet_rd {
  double rating_chess_bullet_rd = 16;
  }
  oneof _rating_chess_daily_rd {
  double rating_chess_daily_rd = 17;
  }
  oneof _rating_chess_rapid_rd {
  double rating_chess_rapid_rd = 18;
  }
  oneof _rating_best {
  int32 rating_best = 19;
  }
  oneof _rating_best_type {
  string rating_best_type = 20;
  }
}

```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10970"></a>
## FND-10970: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_chess_rapid_rd

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_chess_rapid_rd {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1911.

```text
ess_bullet_rd = 16;
  }
  oneof _rating_chess_daily_rd {
  double rating_chess_daily_rd = 17;
  }
  oneof _rating_chess_rapid_rd {
  double rating_chess_rapid_rd = 18;
  }
  oneof _rating_best {
  int32 rating_best = 19;
  }
  oneof _rating_best_type {
  string rating_best_type = 20;
  }
}

```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10971"></a>
## FND-10971: chesscom.user_properties.v1.RatingsProperty.rating_chess_rapid_rd = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

double rating_chess_rapid_rd = 18;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1944.

```text
rating_chess_daily_rd {
  double rating_chess_daily_rd = 17;
  }
  oneof _rating_chess_rapid_rd {
  double rating_chess_rapid_rd = 18;
  }
  oneof _rating_best {
  int32 rating_best = 19;
  }
  oneof _rating_best_type {
  string rating_best_type = 20;
  }
}

```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10972"></a>
## FND-10972: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_best

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_best {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 1985.

```text
hess_daily_rd = 17;
  }
  oneof _rating_chess_rapid_rd {
  double rating_chess_rapid_rd = 18;
  }
  oneof _rating_best {
  int32 rating_best = 19;
  }
  oneof _rating_best_type {
  string rating_best_type = 20;
  }
}

```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-10973"></a>
## FND-10973: chesscom.user_properties.v1.RatingsProperty.rating_best = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating_best = 19;

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 2008.

```text

  oneof _rating_chess_rapid_rd {
  double rating_chess_rapid_rd = 18;
  }
  oneof _rating_best {
  int32 rating_best = 19;
  }
  oneof _rating_best_type {
  string rating_best_type = 20;
  }
}

```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-10974"></a>
## FND-10974: oneof declaration: chesscom.user_properties.v1.RatingsProperty._rating_best_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating_best_type {

### Evidence

- **SRC-0625** `research/proto/chesscom/user_properties/v1/properties_ratings.proto` — [preserved redacted evidence](../evidence/text/670f2464d8b43775a3b30684d658d0a60f90b71e6c4a86e90b2f53c114230f0e.proto)
  Character offset 2038.

```text
d {
  double rating_chess_rapid_rd = 18;
  }
  oneof _rating_best {
  int32 rating_best = 19;
  }
  oneof _rating_best_type {
  string rating_best_type = 20;
  }
}

```

**Source references:** SRC-0625, SRC-1596  
**URL references:** None independently associated  
**Related findings:** FND-10913, FND-10914, FND-10915

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
