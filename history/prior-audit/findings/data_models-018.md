# data_models — findings 1701–1800

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-01975"></a>
## FND-01975: oneof declaration: chesscom.courses.v1.CourseVariation._learning_level

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _learning_level {

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 232.

```text
neof _video_start {
  int32 video_start = 9;
  }
  oneof _video_end {
  int32 video_end = 10;
  }
  oneof _learning_level {
  uint32 learning_level = 12;
  }
  oneof _first_learned_at {
  .google.protobuf.Timestamp first_learned_at = 13;
  }
  oneof _last_reviewed_at {
  .google.protobuf.Timestamp last_reviewed_at = 14;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 15;
  }
  oneof _previ
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01976"></a>
## FND-01976: chesscom.courses.v1.CourseVariation.learning_level = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint32 learning_level = 12;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 258.

```text
2 video_start = 9;
  }
  oneof _video_end {
  int32 video_end = 10;
  }
  oneof _learning_level {
  uint32 learning_level = 12;
  }
  oneof _first_learned_at {
  .google.protobuf.Timestamp first_learned_at = 13;
  }
  oneof _last_reviewed_at {
  .google.protobuf.Timestamp last_reviewed_at = 14;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 15;
  }
  oneof _preview_position {
  .chesscom.
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01977"></a>
## FND-01977: oneof declaration: chesscom.courses.v1.CourseVariation._first_learned_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _first_learned_at {

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 292.

```text
deo_end {
  int32 video_end = 10;
  }
  oneof _learning_level {
  uint32 learning_level = 12;
  }
  oneof _first_learned_at {
  .google.protobuf.Timestamp first_learned_at = 13;
  }
  oneof _last_reviewed_at {
  .google.protobuf.Timestamp last_reviewed_at = 14;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 15;
  }
  oneof _preview_position {
  .chesscom.courses.v1.CoursePosition preview_
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01978"></a>
## FND-01978: chesscom.courses.v1.CourseVariation.first_learned_at = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp first_learned_at = 13;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 320.

```text
= 10;
  }
  oneof _learning_level {
  uint32 learning_level = 12;
  }
  oneof _first_learned_at {
  .google.protobuf.Timestamp first_learned_at = 13;
  }
  oneof _last_reviewed_at {
  .google.protobuf.Timestamp last_reviewed_at = 14;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 15;
  }
  oneof _preview_position {
  .chesscom.courses.v1.CoursePosition preview_position = 17;
  }
  optiona
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01979"></a>
## FND-01979: oneof declaration: chesscom.courses.v1.CourseVariation._last_reviewed_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_reviewed_at {

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 376.

```text
vel = 12;
  }
  oneof _first_learned_at {
  .google.protobuf.Timestamp first_learned_at = 13;
  }
  oneof _last_reviewed_at {
  .google.protobuf.Timestamp last_reviewed_at = 14;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 15;
  }
  oneof _preview_position {
  .chesscom.courses.v1.CoursePosition preview_position = 17;
  }
  optional string id = 1;
  optional string name = 2;
  optional 
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01980"></a>
## FND-01980: chesscom.courses.v1.CourseVariation.last_reviewed_at = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_reviewed_at = 14;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 404.

```text
_learned_at {
  .google.protobuf.Timestamp first_learned_at = 13;
  }
  oneof _last_reviewed_at {
  .google.protobuf.Timestamp last_reviewed_at = 14;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 15;
  }
  oneof _preview_position {
  .chesscom.courses.v1.CoursePosition preview_position = 17;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses.v1.CourseP
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01981"></a>
## FND-01981: oneof declaration: chesscom.courses.v1.CourseVariation._next_review_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _next_review_at {

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 460.

```text
_at = 13;
  }
  oneof _last_reviewed_at {
  .google.protobuf.Timestamp last_reviewed_at = 14;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 15;
  }
  oneof _preview_position {
  .chesscom.courses.v1.CoursePosition preview_position = 17;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses.v1.CoursePosition starting_position = 3;
  optional string move_tr
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01982"></a>
## FND-01982: chesscom.courses.v1.CourseVariation.next_review_at = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp next_review_at = 15;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 486.

```text
t_reviewed_at {
  .google.protobuf.Timestamp last_reviewed_at = 14;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 15;
  }
  oneof _preview_position {
  .chesscom.courses.v1.CoursePosition preview_position = 17;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses.v1.CoursePosition starting_position = 3;
  optional string move_trainer_id = 4;
  optional s
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01983"></a>
## FND-01983: oneof declaration: chesscom.courses.v1.CourseVariation._preview_position

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _preview_position {

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 540.

```text
ewed_at = 14;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 15;
  }
  oneof _preview_position {
  .chesscom.courses.v1.CoursePosition preview_position = 17;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses.v1.CoursePosition starting_position = 3;
  optional string move_trainer_id = 4;
  optional string chapter_id = 5;
  optional .chesscom.courses_com
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01984"></a>
## FND-01984: chesscom.courses.v1.CourseVariation.preview_position = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CoursePosition preview_position = 17;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 568.

```text
ext_review_at {
  .google.protobuf.Timestamp next_review_at = 15;
  }
  oneof _preview_position {
  .chesscom.courses.v1.CoursePosition preview_position = 17;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses.v1.CoursePosition starting_position = 3;
  optional string move_trainer_id = 4;
  optional string chapter_id = 5;
  optional .chesscom.courses_common.v1.CourseVariationType t
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01985"></a>
## FND-01985: chesscom.courses.v1.CourseVariation.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 633.

```text

  }
  oneof _preview_position {
  .chesscom.courses.v1.CoursePosition preview_position = 17;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses.v1.CoursePosition starting_position = 3;
  optional string move_trainer_id = 4;
  optional string chapter_id = 5;
  optional .chesscom.courses_common.v1.CourseVariationType type = 6;
  optional bool is_learned = 7;
  optional bool is_pause
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01986"></a>
## FND-01986: chesscom.courses.v1.CourseVariation.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 659.

```text
tion {
  .chesscom.courses.v1.CoursePosition preview_position = 17;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses.v1.CoursePosition starting_position = 3;
  optional string move_trainer_id = 4;
  optional string chapter_id = 5;
  optional .chesscom.courses_common.v1.CourseVariationType type = 6;
  optional bool is_learned = 7;
  optional bool is_paused = 8;
  optional .chessco
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01987"></a>
## FND-01987: chesscom.courses.v1.CourseVariation.starting_position = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CoursePosition starting_position = 3;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 687.

```text
1.CoursePosition preview_position = 17;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses.v1.CoursePosition starting_position = 3;
  optional string move_trainer_id = 4;
  optional string chapter_id = 5;
  optional .chesscom.courses_common.v1.CourseVariationType type = 6;
  optional bool is_learned = 7;
  optional bool is_paused = 8;
  optional .chesscom.courses.v1.VariationAccess
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01988"></a>
## FND-01988: chesscom.courses.v1.CourseVariation.move_trainer_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string move_trainer_id = 4;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 757.

```text
  optional string name = 2;
  optional .chesscom.courses.v1.CoursePosition starting_position = 3;
  optional string move_trainer_id = 4;
  optional string chapter_id = 5;
  optional .chesscom.courses_common.v1.CourseVariationType type = 6;
  optional bool is_learned = 7;
  optional bool is_paused = 8;
  optional .chesscom.courses.v1.VariationAccessType access_type = 11;
  optional uint32 move_count = 16;
  optional .
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01989"></a>
## FND-01989: chesscom.courses.v1.CourseVariation.chapter_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string chapter_id = 5;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 796.

```text
.chesscom.courses.v1.CoursePosition starting_position = 3;
  optional string move_trainer_id = 4;
  optional string chapter_id = 5;
  optional .chesscom.courses_common.v1.CourseVariationType type = 6;
  optional bool is_learned = 7;
  optional bool is_paused = 8;
  optional .chesscom.courses.v1.VariationAccessType access_type = 11;
  optional uint32 move_count = 16;
  optional .chesscom.chess.v1.Color learner_color =
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01990"></a>
## FND-01990: chesscom.courses.v1.CourseVariation.type = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseVariationType type = 6;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 830.

```text
n starting_position = 3;
  optional string move_trainer_id = 4;
  optional string chapter_id = 5;
  optional .chesscom.courses_common.v1.CourseVariationType type = 6;
  optional bool is_learned = 7;
  optional bool is_paused = 8;
  optional .chesscom.courses.v1.VariationAccessType access_type = 11;
  optional uint32 move_count = 16;
  optional .chesscom.chess.v1.Color learner_color = 18;
  optional string slug = 19;

```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01991"></a>
## FND-01991: chesscom.courses.v1.CourseVariation.is_learned = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_learned = 7;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 899.

```text
ional string chapter_id = 5;
  optional .chesscom.courses_common.v1.CourseVariationType type = 6;
  optional bool is_learned = 7;
  optional bool is_paused = 8;
  optional .chesscom.courses.v1.VariationAccessType access_type = 11;
  optional uint32 move_count = 16;
  optional .chesscom.chess.v1.Color learner_color = 18;
  optional string slug = 19;
}

```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01992"></a>
## FND-01992: chesscom.courses.v1.CourseVariation.is_paused = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_paused = 8;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 931.

```text
ptional .chesscom.courses_common.v1.CourseVariationType type = 6;
  optional bool is_learned = 7;
  optional bool is_paused = 8;
  optional .chesscom.courses.v1.VariationAccessType access_type = 11;
  optional uint32 move_count = 16;
  optional .chesscom.chess.v1.Color learner_color = 18;
  optional string slug = 19;
}

```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01993"></a>
## FND-01993: chesscom.courses.v1.CourseVariation.access_type = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.VariationAccessType access_type = 11;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 962.

```text
n.v1.CourseVariationType type = 6;
  optional bool is_learned = 7;
  optional bool is_paused = 8;
  optional .chesscom.courses.v1.VariationAccessType access_type = 11;
  optional uint32 move_count = 16;
  optional .chesscom.chess.v1.Color learner_color = 18;
  optional string slug = 19;
}

```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01994"></a>
## FND-01994: chesscom.courses.v1.CourseVariation.move_count = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 move_count = 16;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 1032.

```text
ptional bool is_paused = 8;
  optional .chesscom.courses.v1.VariationAccessType access_type = 11;
  optional uint32 move_count = 16;
  optional .chesscom.chess.v1.Color learner_color = 18;
  optional string slug = 19;
}

```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01995"></a>
## FND-01995: chesscom.courses.v1.CourseVariation.learner_color = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Color learner_color = 18;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 1067.

```text
nal .chesscom.courses.v1.VariationAccessType access_type = 11;
  optional uint32 move_count = 16;
  optional .chesscom.chess.v1.Color learner_color = 18;
  optional string slug = 19;
}

```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01996"></a>
## FND-01996: chesscom.courses.v1.CourseVariation.slug = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string slug = 19;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 1123.

```text
 = 11;
  optional uint32 move_count = 16;
  optional .chesscom.chess.v1.Color learner_color = 18;
  optional string slug = 19;
}

```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01997"></a>
## FND-01997: message declaration: chesscom.courses.v1.CourseVariationPly

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseVariationPly {

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 107.

```text
ce: chesscom/courses/v1/course_variation_ply.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseVariationPly {
  oneof _pre_comment {
  string pre_comment = 8;
  }
  oneof _post_comment {
  string post_comment = 9;
  }
  oneof _coach_speech {
  .chesscom.courses.v1.CourseCoachSpeech coach_speech = 11;
  }
  optional string id = 1;
  optional int32 move_number = 2;
  optional string san = 3;
  option
```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01998, FND-01999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01998"></a>
## FND-01998: oneof declaration: chesscom.courses.v1.CourseVariationPly._pre_comment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pre_comment {

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 138.

```text
variation_ply.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseVariationPly {
  oneof _pre_comment {
  string pre_comment = 8;
  }
  oneof _post_comment {
  string post_comment = 9;
  }
  oneof _coach_speech {
  .chesscom.courses.v1.CourseCoachSpeech coach_speech = 11;
  }
  optional string id = 1;
  optional int32 move_number = 2;
  optional string san = 3;
  optional .chesscom.courses.v1.CourseP
```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01999"></a>
## FND-01999: chesscom.courses.v1.CourseVariationPly.pre_comment = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string pre_comment = 8;

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 161.

```text
syntax: proto3

package chesscom.courses.v1;

message CourseVariationPly {
  oneof _pre_comment {
  string pre_comment = 8;
  }
  oneof _post_comment {
  string post_comment = 9;
  }
  oneof _coach_speech {
  .chesscom.courses.v1.CourseCoachSpeech coach_speech = 11;
  }
  optional string id = 1;
  optional int32 move_number = 2;
  optional string san = 3;
  optional .chesscom.courses.v1.CoursePosition position = 4;
 
```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02000"></a>
## FND-02000: oneof declaration: chesscom.courses.v1.CourseVariationPly._post_comment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _post_comment {

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 191.

```text
om.courses.v1;

message CourseVariationPly {
  oneof _pre_comment {
  string pre_comment = 8;
  }
  oneof _post_comment {
  string post_comment = 9;
  }
  oneof _coach_speech {
  .chesscom.courses.v1.CourseCoachSpeech coach_speech = 11;
  }
  optional string id = 1;
  optional int32 move_number = 2;
  optional string san = 3;
  optional .chesscom.courses.v1.CoursePosition position = 4;
  optional .chesscom.chess.v1.C
```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01998, FND-01999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02001"></a>
## FND-02001: chesscom.courses.v1.CourseVariationPly.post_comment = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string post_comment = 9;

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 215.

```text
CourseVariationPly {
  oneof _pre_comment {
  string pre_comment = 8;
  }
  oneof _post_comment {
  string post_comment = 9;
  }
  oneof _coach_speech {
  .chesscom.courses.v1.CourseCoachSpeech coach_speech = 11;
  }
  optional string id = 1;
  optional int32 move_number = 2;
  optional string san = 3;
  optional .chesscom.courses.v1.CoursePosition position = 4;
  optional .chesscom.chess.v1.Color color = 5;
  option
```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01998, FND-01999

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02002"></a>
## FND-02002: oneof declaration: chesscom.courses.v1.CourseVariationPly._coach_speech

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _coach_speech {

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 246.

```text
re_comment {
  string pre_comment = 8;
  }
  oneof _post_comment {
  string post_comment = 9;
  }
  oneof _coach_speech {
  .chesscom.courses.v1.CourseCoachSpeech coach_speech = 11;
  }
  optional string id = 1;
  optional int32 move_number = 2;
  optional string san = 3;
  optional .chesscom.courses.v1.CoursePosition position = 4;
  optional .chesscom.chess.v1.Color color = 5;
  optional bool is_learnable = 6;
  rep
```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01998, FND-01999

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02003"></a>
## FND-02003: chesscom.courses.v1.CourseVariationPly.coach_speech = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseCoachSpeech coach_speech = 11;

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 270.

```text
e_comment = 8;
  }
  oneof _post_comment {
  string post_comment = 9;
  }
  oneof _coach_speech {
  .chesscom.courses.v1.CourseCoachSpeech coach_speech = 11;
  }
  optional string id = 1;
  optional int32 move_number = 2;
  optional string san = 3;
  optional .chesscom.courses.v1.CoursePosition position = 4;
  optional .chesscom.chess.v1.Color color = 5;
  optional bool is_learnable = 6;
  repeated .chesscom.courses_
```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01998, FND-01999

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02004"></a>
## FND-02004: chesscom.courses.v1.CourseVariationPly.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 334.

```text
 = 9;
  }
  oneof _coach_speech {
  .chesscom.courses.v1.CourseCoachSpeech coach_speech = 11;
  }
  optional string id = 1;
  optional int32 move_number = 2;
  optional string san = 3;
  optional .chesscom.courses.v1.CoursePosition position = 4;
  optional .chesscom.chess.v1.Color color = 5;
  optional bool is_learnable = 6;
  repeated .chesscom.courses_common.v1.CourseVariationAlternativeMove alternative_moves = 7;

```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01998, FND-01999

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02005"></a>
## FND-02005: chesscom.courses.v1.CourseVariationPly.move_number = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 move_number = 2;

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 360.

```text
peech {
  .chesscom.courses.v1.CourseCoachSpeech coach_speech = 11;
  }
  optional string id = 1;
  optional int32 move_number = 2;
  optional string san = 3;
  optional .chesscom.courses.v1.CoursePosition position = 4;
  optional .chesscom.chess.v1.Color color = 5;
  optional bool is_learnable = 6;
  repeated .chesscom.courses_common.v1.CourseVariationAlternativeMove alternative_moves = 7;
  optional int32 ply_index
```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01998, FND-01999

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02006"></a>
## FND-02006: chesscom.courses.v1.CourseVariationPly.san = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string san = 3;

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 394.

```text
rseCoachSpeech coach_speech = 11;
  }
  optional string id = 1;
  optional int32 move_number = 2;
  optional string san = 3;
  optional .chesscom.courses.v1.CoursePosition position = 4;
  optional .chesscom.chess.v1.Color color = 5;
  optional bool is_learnable = 6;
  repeated .chesscom.courses_common.v1.CourseVariationAlternativeMove alternative_moves = 7;
  optional int32 ply_index = 10;
}

```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01998, FND-01999

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02007"></a>
## FND-02007: chesscom.courses.v1.CourseVariationPly.position = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CoursePosition position = 4;

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 421.

```text
 = 11;
  }
  optional string id = 1;
  optional int32 move_number = 2;
  optional string san = 3;
  optional .chesscom.courses.v1.CoursePosition position = 4;
  optional .chesscom.chess.v1.Color color = 5;
  optional bool is_learnable = 6;
  repeated .chesscom.courses_common.v1.CourseVariationAlternativeMove alternative_moves = 7;
  optional int32 ply_index = 10;
}

```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01998, FND-01999

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02008"></a>
## FND-02008: chesscom.courses.v1.CourseVariationPly.color = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Color color = 5;

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 482.

```text
mber = 2;
  optional string san = 3;
  optional .chesscom.courses.v1.CoursePosition position = 4;
  optional .chesscom.chess.v1.Color color = 5;
  optional bool is_learnable = 6;
  repeated .chesscom.courses_common.v1.CourseVariationAlternativeMove alternative_moves = 7;
  optional int32 ply_index = 10;
}

```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01998, FND-01999

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02009"></a>
## FND-02009: chesscom.courses.v1.CourseVariationPly.is_learnable = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_learnable = 6;

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 529.

```text
 .chesscom.courses.v1.CoursePosition position = 4;
  optional .chesscom.chess.v1.Color color = 5;
  optional bool is_learnable = 6;
  repeated .chesscom.courses_common.v1.CourseVariationAlternativeMove alternative_moves = 7;
  optional int32 ply_index = 10;
}

```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01998, FND-01999

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02010"></a>
## FND-02010: chesscom.courses.v1.CourseVariationPly.alternative_moves = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses_common.v1.CourseVariationAlternativeMove alternative_moves = 7;

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 563.

```text
on position = 4;
  optional .chesscom.chess.v1.Color color = 5;
  optional bool is_learnable = 6;
  repeated .chesscom.courses_common.v1.CourseVariationAlternativeMove alternative_moves = 7;
  optional int32 ply_index = 10;
}

```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01998, FND-01999

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02011"></a>
## FND-02011: chesscom.courses.v1.CourseVariationPly.ply_index = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 ply_index = 10;

### Evidence

- **SRC-0288** `research/proto/chesscom/courses/v1/course_variation_ply.proto` — [preserved redacted evidence](../evidence/text/9240b2b8769f21f0b4dcc855ccc7178bd8770fce3aae5e65249d63ba21d3c317.proto)
  Character offset 656.

```text
= 6;
  repeated .chesscom.courses_common.v1.CourseVariationAlternativeMove alternative_moves = 7;
  optional int32 ply_index = 10;
}

```

**Source references:** SRC-0288, SRC-1259  
**URL references:** None independently associated  
**Related findings:** FND-01997, FND-01998, FND-01999

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02012"></a>
## FND-02012: message declaration: chesscom.courses.v1.CourseVideoPlayback

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseVideoPlayback {

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 108.

```text
e: chesscom/courses/v1/course_video_playback.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseVideoPlayback {
  oneof _hls_url {
  string hls_url = 1;
  }
  oneof _thumbnail_url {
  string thumbnail_url = 4;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 5;
  }
  repeated .chesscom.courses.v1.CourseVideoPlaybackFile files = 2;
  repeated .chesscom.courses.v1.CourseVideoTextTrack text_t
```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02013, FND-02014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02013"></a>
## FND-02013: oneof declaration: chesscom.courses.v1.CourseVideoPlayback._hls_url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _hls_url {

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 140.

```text
deo_playback.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseVideoPlayback {
  oneof _hls_url {
  string hls_url = 1;
  }
  oneof _thumbnail_url {
  string thumbnail_url = 4;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 5;
  }
  repeated .chesscom.courses.v1.CourseVideoPlaybackFile files = 2;
  repeated .chesscom.courses.v1.CourseVideoTextTrack text_tracks = 3;
}

message CourseVide
```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02014"></a>
## FND-02014: chesscom.courses.v1.CourseVideoPlayback.hls_url = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string hls_url = 1;

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 159.

```text
// syntax: proto3

package chesscom.courses.v1;

message CourseVideoPlayback {
  oneof _hls_url {
  string hls_url = 1;
  }
  oneof _thumbnail_url {
  string thumbnail_url = 4;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 5;
  }
  repeated .chesscom.courses.v1.CourseVideoPlaybackFile files = 2;
  repeated .chesscom.courses.v1.CourseVideoTextTrack text_tracks = 3;
}

message CourseVideoPlaybackFile {
  o
```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02015"></a>
## FND-02015: oneof declaration: chesscom.courses.v1.CourseVideoPlayback._thumbnail_url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _thumbnail_url {

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 185.

```text
 chesscom.courses.v1;

message CourseVideoPlayback {
  oneof _hls_url {
  string hls_url = 1;
  }
  oneof _thumbnail_url {
  string thumbnail_url = 4;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 5;
  }
  repeated .chesscom.courses.v1.CourseVideoPlaybackFile files = 2;
  repeated .chesscom.courses.v1.CourseVideoTextTrack text_tracks = 3;
}

message CourseVideoPlaybackFile {
  oneof _file_size {
  int64 
```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02016"></a>
## FND-02016: chesscom.courses.v1.CourseVideoPlayback.thumbnail_url = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string thumbnail_url = 4;

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 210.

```text
ssage CourseVideoPlayback {
  oneof _hls_url {
  string hls_url = 1;
  }
  oneof _thumbnail_url {
  string thumbnail_url = 4;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 5;
  }
  repeated .chesscom.courses.v1.CourseVideoPlaybackFile files = 2;
  repeated .chesscom.courses.v1.CourseVideoTextTrack text_tracks = 3;
}

message CourseVideoPlaybackFile {
  oneof _file_size {
  int64 file_size = 4;
  }
  opti
```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02017"></a>
## FND-02017: oneof declaration: chesscom.courses.v1.CourseVideoPlayback._duration_seconds

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _duration_seconds {

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 242.

```text
eof _hls_url {
  string hls_url = 1;
  }
  oneof _thumbnail_url {
  string thumbnail_url = 4;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 5;
  }
  repeated .chesscom.courses.v1.CourseVideoPlaybackFile files = 2;
  repeated .chesscom.courses.v1.CourseVideoTextTrack text_tracks = 3;
}

message CourseVideoPlaybackFile {
  oneof _file_size {
  int64 file_size = 4;
  }
  optional string url = 1;
  optional 
```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02018"></a>
## FND-02018: chesscom.courses.v1.CourseVideoPlayback.duration_seconds = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 duration_seconds = 5;

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 270.

```text
url = 1;
  }
  oneof _thumbnail_url {
  string thumbnail_url = 4;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 5;
  }
  repeated .chesscom.courses.v1.CourseVideoPlaybackFile files = 2;
  repeated .chesscom.courses.v1.CourseVideoTextTrack text_tracks = 3;
}

message CourseVideoPlaybackFile {
  oneof _file_size {
  int64 file_size = 4;
  }
  optional string url = 1;
  optional int32 width = 2;
  optional 
```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02019"></a>
## FND-02019: chesscom.courses.v1.CourseVideoPlayback.files = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseVideoPlaybackFile files = 2;

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 304.

```text
l {
  string thumbnail_url = 4;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 5;
  }
  repeated .chesscom.courses.v1.CourseVideoPlaybackFile files = 2;
  repeated .chesscom.courses.v1.CourseVideoTextTrack text_tracks = 3;
}

message CourseVideoPlaybackFile {
  oneof _file_size {
  int64 file_size = 4;
  }
  optional string url = 1;
  optional int32 width = 2;
  optional int32 height = 3;
}

message Cours
```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02020"></a>
## FND-02020: chesscom.courses.v1.CourseVideoPlayback.text_tracks = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseVideoTextTrack text_tracks = 3;

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 371.

```text
nt32 duration_seconds = 5;
  }
  repeated .chesscom.courses.v1.CourseVideoPlaybackFile files = 2;
  repeated .chesscom.courses.v1.CourseVideoTextTrack text_tracks = 3;
}

message CourseVideoPlaybackFile {
  oneof _file_size {
  int64 file_size = 4;
  }
  optional string url = 1;
  optional int32 width = 2;
  optional int32 height = 3;
}

message CourseVideoTextTrack {
  oneof _label {
  string label = 2;
  }
  option
```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02021"></a>
## FND-02021: message declaration: chesscom.courses.v1.CourseVideoPlaybackFile

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseVideoPlaybackFile {

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 442.

```text
deoPlaybackFile files = 2;
  repeated .chesscom.courses.v1.CourseVideoTextTrack text_tracks = 3;
}

message CourseVideoPlaybackFile {
  oneof _file_size {
  int64 file_size = 4;
  }
  optional string url = 1;
  optional int32 width = 2;
  optional int32 height = 3;
}

message CourseVideoTextTrack {
  oneof _label {
  string label = 2;
  }
  optional string language = 1;
  optional string url = 3;
}

```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02022"></a>
## FND-02022: oneof declaration: chesscom.courses.v1.CourseVideoPlaybackFile._file_size

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _file_size {

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 478.

```text
d .chesscom.courses.v1.CourseVideoTextTrack text_tracks = 3;
}

message CourseVideoPlaybackFile {
  oneof _file_size {
  int64 file_size = 4;
  }
  optional string url = 1;
  optional int32 width = 2;
  optional int32 height = 3;
}

message CourseVideoTextTrack {
  oneof _label {
  string label = 2;
  }
  optional string language = 1;
  optional string url = 3;
}

```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02023"></a>
## FND-02023: chesscom.courses.v1.CourseVideoPlaybackFile.file_size = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int64 file_size = 4;

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 499.

```text
1.CourseVideoTextTrack text_tracks = 3;
}

message CourseVideoPlaybackFile {
  oneof _file_size {
  int64 file_size = 4;
  }
  optional string url = 1;
  optional int32 width = 2;
  optional int32 height = 3;
}

message CourseVideoTextTrack {
  oneof _label {
  string label = 2;
  }
  optional string language = 1;
  optional string url = 3;
}

```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02024"></a>
## FND-02024: chesscom.courses.v1.CourseVideoPlaybackFile.url = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string url = 1;

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 526.

```text
_tracks = 3;
}

message CourseVideoPlaybackFile {
  oneof _file_size {
  int64 file_size = 4;
  }
  optional string url = 1;
  optional int32 width = 2;
  optional int32 height = 3;
}

message CourseVideoTextTrack {
  oneof _label {
  string label = 2;
  }
  optional string language = 1;
  optional string url = 3;
}

```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02025"></a>
## FND-02025: chesscom.courses.v1.CourseVideoPlaybackFile.width = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 width = 2;

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 553.

```text
rseVideoPlaybackFile {
  oneof _file_size {
  int64 file_size = 4;
  }
  optional string url = 1;
  optional int32 width = 2;
  optional int32 height = 3;
}

message CourseVideoTextTrack {
  oneof _label {
  string label = 2;
  }
  optional string language = 1;
  optional string url = 3;
}

```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02026"></a>
## FND-02026: chesscom.courses.v1.CourseVideoPlaybackFile.height = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 height = 3;

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 581.

```text
of _file_size {
  int64 file_size = 4;
  }
  optional string url = 1;
  optional int32 width = 2;
  optional int32 height = 3;
}

message CourseVideoTextTrack {
  oneof _label {
  string label = 2;
  }
  optional string language = 1;
  optional string url = 3;
}

```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02027"></a>
## FND-02027: message declaration: chesscom.courses.v1.CourseVideoTextTrack

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseVideoTextTrack {

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 611.

```text
ize = 4;
  }
  optional string url = 1;
  optional int32 width = 2;
  optional int32 height = 3;
}

message CourseVideoTextTrack {
  oneof _label {
  string label = 2;
  }
  optional string language = 1;
  optional string url = 3;
}

```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02028"></a>
## FND-02028: oneof declaration: chesscom.courses.v1.CourseVideoTextTrack._label

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _label {

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 644.

```text
l = 1;
  optional int32 width = 2;
  optional int32 height = 3;
}

message CourseVideoTextTrack {
  oneof _label {
  string label = 2;
  }
  optional string language = 1;
  optional string url = 3;
}

```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02029"></a>
## FND-02029: chesscom.courses.v1.CourseVideoTextTrack.label = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string label = 2;

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 661.

```text
 int32 width = 2;
  optional int32 height = 3;
}

message CourseVideoTextTrack {
  oneof _label {
  string label = 2;
  }
  optional string language = 1;
  optional string url = 3;
}

```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02030"></a>
## FND-02030: chesscom.courses.v1.CourseVideoTextTrack.language = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string language = 1;

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 685.

```text
onal int32 height = 3;
}

message CourseVideoTextTrack {
  oneof _label {
  string label = 2;
  }
  optional string language = 1;
  optional string url = 3;
}

```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02031"></a>
## FND-02031: chesscom.courses.v1.CourseVideoTextTrack.url = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string url = 3;

### Evidence

- **SRC-0289** `research/proto/chesscom/courses/v1/course_video_playback.proto` — [preserved redacted evidence](../evidence/text/0cdab03c2a8682c1f10fdfeff8032368d23aa827513960bc7a7837d3f1a9ec0b.proto)
  Character offset 717.

```text
e CourseVideoTextTrack {
  oneof _label {
  string label = 2;
  }
  optional string language = 1;
  optional string url = 3;
}

```

**Source references:** SRC-0289, SRC-1260  
**URL references:** None independently associated  
**Related findings:** FND-02012, FND-02013, FND-02014

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02032"></a>
## FND-02032: message declaration: chesscom.courses.v1.AuthenticateForCoursesWithCookieRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AuthenticateForCoursesWithCookieRequest {

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 117.

```text
om/courses/v1/courses_authentication_service.proto
// syntax: proto3

package chesscom.courses.v1;

message AuthenticateForCoursesWithCookieRequest {
  optional string provider_name = 1;
  optional string cookie_name = 2;
}

message AuthenticateForCoursesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02033, FND-02034

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02033"></a>
## FND-02033: chesscom.courses.v1.AuthenticateForCoursesWithCookieRequest.provider_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string provider_name = 1;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 169.

```text
/ syntax: proto3

package chesscom.courses.v1;

message AuthenticateForCoursesWithCookieRequest {
  optional string provider_name = 1;
  optional string cookie_name = 2;
}

message AuthenticateForCoursesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCou
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02034"></a>
## FND-02034: chesscom.courses.v1.AuthenticateForCoursesWithCookieRequest.cookie_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string cookie_name = 2;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 206.

```text
urses.v1;

message AuthenticateForCoursesWithCookieRequest {
  optional string provider_name = 1;
  optional string cookie_name = 2;
}

message AuthenticateForCoursesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provi
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02035"></a>
## FND-02035: message declaration: chesscom.courses.v1.AuthenticateForCoursesWithCookieResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AuthenticateForCoursesWithCookieResponse {

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 242.

```text
ursesWithCookieRequest {
  optional string provider_name = 1;
  optional string cookie_name = 2;
}

message AuthenticateForCoursesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redi
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02036"></a>
## FND-02036: chesscom.courses.v1.AuthenticateForCoursesWithCookieResponse.access_token = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string access_token = 1;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 295.

```text
ame = 1;
  optional string cookie_name = 2;
}

message AuthenticateForCoursesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesRespons
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02037"></a>
## FND-02037: chesscom.courses.v1.AuthenticateForCoursesWithCookieResponse.refresh_token = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string refresh_token = 2;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 331.

```text
me = 2;
}

message AuthenticateForCoursesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

me
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02038"></a>
## FND-02038: chesscom.courses.v1.AuthenticateForCoursesWithCookieResponse.expires_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp expires_at = 3;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 368.

```text
rsesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

message AuthenticateForCoursesRequest {
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02039"></a>
## FND-02039: chesscom.courses.v1.AuthenticateForCoursesWithCookieResponse.expires_in_seconds = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 expires_in_seconds = 4;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 422.

```text
n = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

message AuthenticateForCoursesRequest {
  optional string provider_name = 1;
  optional strin
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02040"></a>
## FND-02040: message declaration: chesscom.courses.v1.GetOAuthURLForCoursesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetOAuthURLForCoursesRequest {

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 464.

```text
;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

message AuthenticateForCoursesRequest {
  optional string provider_name = 1;
  optional string code = 2;
  optional string redirect_uri
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02041"></a>
## FND-02041: chesscom.courses.v1.GetOAuthURLForCoursesRequest.provider_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string provider_name = 1;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 169.

```text
/ syntax: proto3

package chesscom.courses.v1;

message AuthenticateForCoursesWithCookieRequest {
  optional string provider_name = 1;
  optional string cookie_name = 2;
}

message AuthenticateForCoursesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCou
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02042"></a>
## FND-02042: chesscom.courses.v1.GetOAuthURLForCoursesRequest.redirect_uri = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string redirect_uri = 2;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 542.

```text
es_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

message AuthenticateForCoursesRequest {
  optional string provider_name = 1;
  optional string code = 2;
  optional string redirect_uri = 3;
  optional string state = 4;
}

message AuthenticateForCoursesResponse {
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02043"></a>
## FND-02043: message declaration: chesscom.courses.v1.GetOAuthURLForCoursesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetOAuthURLForCoursesResponse {

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 579.

```text
hURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

message AuthenticateForCoursesRequest {
  optional string provider_name = 1;
  optional string code = 2;
  optional string redirect_uri = 3;
  optional string state = 4;
}

message AuthenticateForCoursesResponse {
  optional string access_token = 1;

```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02044"></a>
## FND-02044: chesscom.courses.v1.GetOAuthURLForCoursesResponse.url = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string url = 1;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 621.

```text
provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

message AuthenticateForCoursesRequest {
  optional string provider_name = 1;
  optional string code = 2;
  optional string redirect_uri = 3;
  optional string state = 4;
}

message AuthenticateForCoursesResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  opt
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02045"></a>
## FND-02045: message declaration: chesscom.courses.v1.AuthenticateForCoursesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AuthenticateForCoursesRequest {

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 649.

```text
l string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

message AuthenticateForCoursesRequest {
  optional string provider_name = 1;
  optional string code = 2;
  optional string redirect_uri = 3;
  optional string state = 4;
}

message AuthenticateForCoursesResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Times
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02046"></a>
## FND-02046: chesscom.courses.v1.AuthenticateForCoursesRequest.provider_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string provider_name = 1;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 169.

```text
/ syntax: proto3

package chesscom.courses.v1;

message AuthenticateForCoursesWithCookieRequest {
  optional string provider_name = 1;
  optional string cookie_name = 2;
}

message AuthenticateForCoursesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCou
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02047"></a>
## FND-02047: chesscom.courses.v1.AuthenticateForCoursesRequest.code = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string code = 2;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 728.

```text
l string url = 1;
}

message AuthenticateForCoursesRequest {
  optional string provider_name = 1;
  optional string code = 2;
  optional string redirect_uri = 3;
  optional string state = 4;
}

message AuthenticateForCoursesResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message Refres
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02048"></a>
## FND-02048: chesscom.courses.v1.AuthenticateForCoursesRequest.redirect_uri = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string redirect_uri = 3;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 756.

```text
 AuthenticateForCoursesRequest {
  optional string provider_name = 1;
  optional string code = 2;
  optional string redirect_uri = 3;
  optional string state = 4;
}

message AuthenticateForCoursesResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message RefreshTokenForCoursesRequest {
  
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02049"></a>
## FND-02049: chesscom.courses.v1.AuthenticateForCoursesRequest.state = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string state = 4;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 792.

```text
ptional string provider_name = 1;
  optional string code = 2;
  optional string redirect_uri = 3;
  optional string state = 4;
}

message AuthenticateForCoursesResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message RefreshTokenForCoursesRequest {
  optional string refresh_token = 1;
}
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02050"></a>
## FND-02050: message declaration: chesscom.courses.v1.AuthenticateForCoursesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AuthenticateForCoursesResponse {

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 822.

```text
 1;
  optional string code = 2;
  optional string redirect_uri = 3;
  optional string state = 4;
}

message AuthenticateForCoursesResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message RefreshTokenForCoursesRequest {
  optional string refresh_token = 1;
}

message RefreshTokenForCours
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02051"></a>
## FND-02051: chesscom.courses.v1.AuthenticateForCoursesResponse.access_token = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string access_token = 1;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 295.

```text
ame = 1;
  optional string cookie_name = 2;
}

message AuthenticateForCoursesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesRespons
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02052"></a>
## FND-02052: chesscom.courses.v1.AuthenticateForCoursesResponse.refresh_token = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string refresh_token = 2;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 331.

```text
me = 2;
}

message AuthenticateForCoursesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

me
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02053"></a>
## FND-02053: chesscom.courses.v1.AuthenticateForCoursesResponse.expires_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp expires_at = 3;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 368.

```text
rsesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

message AuthenticateForCoursesRequest {
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02054"></a>
## FND-02054: chesscom.courses.v1.AuthenticateForCoursesResponse.expires_in_seconds = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 expires_in_seconds = 4;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 422.

```text
n = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

message AuthenticateForCoursesRequest {
  optional string provider_name = 1;
  optional strin
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02055"></a>
## FND-02055: message declaration: chesscom.courses.v1.RefreshTokenForCoursesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RefreshTokenForCoursesRequest {

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 1034.

```text
;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message RefreshTokenForCoursesRequest {
  optional string refresh_token = 1;
}

message RefreshTokenForCoursesResponse {
  oneof _refresh_token {
  string refresh_token = 2;
  }
  optional string access_token = 1;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message 
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02056"></a>
## FND-02056: chesscom.courses.v1.RefreshTokenForCoursesRequest.refresh_token = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string refresh_token = 1;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 1076.

```text
pires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message RefreshTokenForCoursesRequest {
  optional string refresh_token = 1;
}

message RefreshTokenForCoursesResponse {
  oneof _refresh_token {
  string refresh_token = 2;
  }
  optional string access_token = 1;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetUserInfoForCoursesRequest {
}

message 
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02057"></a>
## FND-02057: message declaration: chesscom.courses.v1.RefreshTokenForCoursesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RefreshTokenForCoursesResponse {

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 1114.

```text
_in_seconds = 4;
}

message RefreshTokenForCoursesRequest {
  optional string refresh_token = 1;
}

message RefreshTokenForCoursesResponse {
  oneof _refresh_token {
  string refresh_token = 2;
  }
  optional string access_token = 1;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetUserInfoForCoursesRequest {
}

message GetUserInfoForCoursesResponse {
  opti
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02058"></a>
## FND-02058: oneof declaration: chesscom.courses.v1.RefreshTokenForCoursesResponse._refresh_token

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _refresh_token {

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 1157.

```text
CoursesRequest {
  optional string refresh_token = 1;
}

message RefreshTokenForCoursesResponse {
  oneof _refresh_token {
  string refresh_token = 2;
  }
  optional string access_token = 1;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetUserInfoForCoursesRequest {
}

message GetUserInfoForCoursesResponse {
  optional string id = 1;
  optional string usern
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02059"></a>
## FND-02059: chesscom.courses.v1.RefreshTokenForCoursesResponse.refresh_token = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string refresh_token = 2;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 340.

```text


message AuthenticateForCoursesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

message Aut
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02060"></a>
## FND-02060: chesscom.courses.v1.RefreshTokenForCoursesResponse.access_token = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string access_token = 1;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 295.

```text
ame = 1;
  optional string cookie_name = 2;
}

message AuthenticateForCoursesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesRespons
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02061"></a>
## FND-02061: chesscom.courses.v1.RefreshTokenForCoursesResponse.expires_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp expires_at = 3;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 368.

```text
rsesWithCookieResponse {
  optional string access_token = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

message AuthenticateForCoursesRequest {
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02062"></a>
## FND-02062: chesscom.courses.v1.RefreshTokenForCoursesResponse.expires_in_seconds = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 expires_in_seconds = 4;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 422.

```text
n = 1;
  optional string refresh_token = 2;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetOAuthURLForCoursesRequest {
  optional string provider_name = 1;
  optional string redirect_uri = 2;
}

message GetOAuthURLForCoursesResponse {
  optional string url = 1;
}

message AuthenticateForCoursesRequest {
  optional string provider_name = 1;
  optional strin
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02063"></a>
## FND-02063: message declaration: chesscom.courses.v1.GetUserInfoForCoursesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserInfoForCoursesRequest {

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 1346.

```text
;
  optional .google.protobuf.Timestamp expires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetUserInfoForCoursesRequest {
}

message GetUserInfoForCoursesResponse {
  optional string id = 1;
  optional string username = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional string provider = 4;
  repeated .chesscom.courses.v1.UserFlag flags = 5;
  repeated .chesscom.courses.v1.User
```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02064"></a>
## FND-02064: message declaration: chesscom.courses.v1.GetUserInfoForCoursesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserInfoForCoursesResponse {

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 1388.

```text
pires_at = 3;
  optional int64 expires_in_seconds = 4;
}

message GetUserInfoForCoursesRequest {
}

message GetUserInfoForCoursesResponse {
  optional string id = 1;
  optional string username = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional string provider = 4;
  repeated .chesscom.courses.v1.UserFlag flags = 5;
  repeated .chesscom.courses.v1.UserGoal user_goal = 6;
}

```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02065"></a>
## FND-02065: chesscom.courses.v1.GetUserInfoForCoursesResponse.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 1430.

```text
seconds = 4;
}

message GetUserInfoForCoursesRequest {
}

message GetUserInfoForCoursesResponse {
  optional string id = 1;
  optional string username = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional string provider = 4;
  repeated .chesscom.courses.v1.UserFlag flags = 5;
  repeated .chesscom.courses.v1.UserGoal user_goal = 6;
}

```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02066"></a>
## FND-02066: chesscom.courses.v1.GetUserInfoForCoursesResponse.username = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string username = 2;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 1456.

```text
tUserInfoForCoursesRequest {
}

message GetUserInfoForCoursesResponse {
  optional string id = 1;
  optional string username = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional string provider = 4;
  repeated .chesscom.courses.v1.UserFlag flags = 5;
  repeated .chesscom.courses.v1.UserGoal user_goal = 6;
}

```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02067"></a>
## FND-02067: chesscom.courses.v1.GetUserInfoForCoursesResponse.picture = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.Picture picture = 3;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 1488.

```text
message GetUserInfoForCoursesResponse {
  optional string id = 1;
  optional string username = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional string provider = 4;
  repeated .chesscom.courses.v1.UserFlag flags = 5;
  repeated .chesscom.courses.v1.UserGoal user_goal = 6;
}

```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02068"></a>
## FND-02068: chesscom.courses.v1.GetUserInfoForCoursesResponse.provider = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string provider = 4;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 1548.

```text
 = 1;
  optional string username = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional string provider = 4;
  repeated .chesscom.courses.v1.UserFlag flags = 5;
  repeated .chesscom.courses.v1.UserGoal user_goal = 6;
}

```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02069"></a>
## FND-02069: chesscom.courses.v1.GetUserInfoForCoursesResponse.flags = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.UserFlag flags = 5;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 1580.

```text
 = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  optional string provider = 4;
  repeated .chesscom.courses.v1.UserFlag flags = 5;
  repeated .chesscom.courses.v1.UserGoal user_goal = 6;
}

```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02070"></a>
## FND-02070: chesscom.courses.v1.GetUserInfoForCoursesResponse.user_goal = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.UserGoal user_goal = 6;

### Evidence

- **SRC-0290** `research/proto/chesscom/courses/v1/courses_authentication_service.proto` — [preserved redacted evidence](../evidence/text/8e5914f77d3fa0f6dbe583e2eb391505cd74270bacd710011e60542f5320a8c5.proto)
  Character offset 1632.

```text
 picture = 3;
  optional string provider = 4;
  repeated .chesscom.courses.v1.UserFlag flags = 5;
  repeated .chesscom.courses.v1.UserGoal user_goal = 6;
}

```

**Source references:** SRC-0290, SRC-1261  
**URL references:** None independently associated  
**Related findings:** FND-02032, FND-02033, FND-02034

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02071"></a>
## FND-02071: message declaration: chesscom.courses.v1.GetCourseListRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseListRequest {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 112.

```text
hesscom/courses/v1/courses_dashboard_service.proto
// syntax: proto3

package chesscom.courses.v1;

message GetCourseListRequest {
}

message GetCourseListResponse {
  repeated .chesscom.courses.v1.Course course_list = 1;
}

message SetCourseInactiveRequest {
  optional string course_id = 1;
}

message SetCourseInactiveResponse {
}

message SetCoursePausedRequest {
  optional string course_id = 1;
}

message SetCours
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02072, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02072"></a>
## FND-02072: message declaration: chesscom.courses.v1.GetCourseListResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseListResponse {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 146.

```text
rd_service.proto
// syntax: proto3

package chesscom.courses.v1;

message GetCourseListRequest {
}

message GetCourseListResponse {
  repeated .chesscom.courses.v1.Course course_list = 1;
}

message SetCourseInactiveRequest {
  optional string course_id = 1;
}

message SetCourseInactiveResponse {
}

message SetCoursePausedRequest {
  optional string course_id = 1;
}

message SetCoursePausedResponse {
}

message SetCo
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02073"></a>
## FND-02073: chesscom.courses.v1.GetCourseListResponse.course_list = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.Course course_list = 1;

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 180.

```text


package chesscom.courses.v1;

message GetCourseListRequest {
}

message GetCourseListResponse {
  repeated .chesscom.courses.v1.Course course_list = 1;
}

message SetCourseInactiveRequest {
  optional string course_id = 1;
}

message SetCourseInactiveResponse {
}

message SetCoursePausedRequest {
  optional string course_id = 1;
}

message SetCoursePausedResponse {
}

message SetCourseUnpausedRequest {
  optional s
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02074"></a>
## FND-02074: message declaration: chesscom.courses.v1.SetCourseInactiveRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetCourseInactiveRequest {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 237.

```text
est {
}

message GetCourseListResponse {
  repeated .chesscom.courses.v1.Course course_list = 1;
}

message SetCourseInactiveRequest {
  optional string course_id = 1;
}

message SetCourseInactiveResponse {
}

message SetCoursePausedRequest {
  optional string course_id = 1;
}

message SetCoursePausedResponse {
}

message SetCourseUnpausedRequest {
  optional string course_id = 1;
}

message SetCourseUnpausedResponse
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
