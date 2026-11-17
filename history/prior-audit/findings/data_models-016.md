# data_models — findings 1501–1600

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-01775"></a>
## FND-01775: chesscom.courses.v1.CourseLearningSessionProgress.total_learning_session_variations_by_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseVariationTypeCount total_learning_session_variations_by_type = 1;

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 897.

```text
peCount total_learning_session_variations_by_type = 6;
}

message CourseLearningSessionProgress {
  repeated .chesscom.courses.v1.CourseVariationTypeCount total_learning_session_variations_by_type = 1;
}

message CourseVariationTypeCount {
  optional .chesscom.courses_common.v1.CourseVariationType type = 1;
  optional int32 count = 2;
}

```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01776"></a>
## FND-01776: message declaration: chesscom.courses.v1.CourseVariationTypeCount

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseVariationTypeCount {

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 1002.

```text
ted .chesscom.courses.v1.CourseVariationTypeCount total_learning_session_variations_by_type = 1;
}

message CourseVariationTypeCount {
  optional .chesscom.courses_common.v1.CourseVariationType type = 1;
  optional int32 count = 2;
}

```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01777"></a>
## FND-01777: chesscom.courses.v1.CourseVariationTypeCount.type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseVariationType type = 1;

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 1039.

```text
ionTypeCount total_learning_session_variations_by_type = 1;
}

message CourseVariationTypeCount {
  optional .chesscom.courses_common.v1.CourseVariationType type = 1;
  optional int32 count = 2;
}

```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01778"></a>
## FND-01778: chesscom.courses.v1.CourseVariationTypeCount.count = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 count = 2;

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 1108.

```text
e CourseVariationTypeCount {
  optional .chesscom.courses_common.v1.CourseVariationType type = 1;
  optional int32 count = 2;
}

```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01779"></a>
## FND-01779: message declaration: chesscom.courses.v1.CourseLesson

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseLesson {

### Evidence

- **SRC-0275** `research/proto/chesscom/courses/v1/course_lesson.proto` — [preserved redacted evidence](../evidence/text/5f236d84060b966b7f36099753be1f4f3dbc22dc7fe59102d21a40dddd01c37d.proto)
  Character offset 100.

```text
// source: chesscom/courses/v1/course_lesson.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseLesson {
  oneof _video_section {
  .chesscom.courses_common.v1.Range video_section = 6;
  }
  oneof _user_video_position {
  int32 user_video_position = 7;
  }
  optional .chesscom.courses.v1.CourseVariation variation = 1;
  optional .chesscom.courses.v1.CourseLessonPlayer white_player = 2;
  optional .c
```

**Source references:** SRC-0275, SRC-1246  
**URL references:** None independently associated  
**Related findings:** FND-01780, FND-01781

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01780"></a>
## FND-01780: oneof declaration: chesscom.courses.v1.CourseLesson._video_section

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _video_section {

### Evidence

- **SRC-0275** `research/proto/chesscom/courses/v1/course_lesson.proto` — [preserved redacted evidence](../evidence/text/5f236d84060b966b7f36099753be1f4f3dbc22dc7fe59102d21a40dddd01c37d.proto)
  Character offset 125.

```text
es/v1/course_lesson.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseLesson {
  oneof _video_section {
  .chesscom.courses_common.v1.Range video_section = 6;
  }
  oneof _user_video_position {
  int32 user_video_position = 7;
  }
  optional .chesscom.courses.v1.CourseVariation variation = 1;
  optional .chesscom.courses.v1.CourseLessonPlayer white_player = 2;
  optional .chesscom.courses.v1.Course
```

**Source references:** SRC-0275, SRC-1246  
**URL references:** None independently associated  
**Related findings:** FND-01779, FND-01781

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01781"></a>
## FND-01781: chesscom.courses.v1.CourseLesson.video_section = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses_common.v1.Range video_section = 6;

### Evidence

- **SRC-0275** `research/proto/chesscom/courses/v1/course_lesson.proto` — [preserved redacted evidence](../evidence/text/5f236d84060b966b7f36099753be1f4f3dbc22dc7fe59102d21a40dddd01c37d.proto)
  Character offset 150.

```text

// syntax: proto3

package chesscom.courses.v1;

message CourseLesson {
  oneof _video_section {
  .chesscom.courses_common.v1.Range video_section = 6;
  }
  oneof _user_video_position {
  int32 user_video_position = 7;
  }
  optional .chesscom.courses.v1.CourseVariation variation = 1;
  optional .chesscom.courses.v1.CourseLessonPlayer white_player = 2;
  optional .chesscom.courses.v1.CourseLessonPlayer black_player
```

**Source references:** SRC-0275, SRC-1246  
**URL references:** None independently associated  
**Related findings:** FND-01779, FND-01780

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01782"></a>
## FND-01782: oneof declaration: chesscom.courses.v1.CourseLesson._user_video_position

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_video_position {

### Evidence

- **SRC-0275** `research/proto/chesscom/courses/v1/course_lesson.proto` — [preserved redacted evidence](../evidence/text/5f236d84060b966b7f36099753be1f4f3dbc22dc7fe59102d21a40dddd01c37d.proto)
  Character offset 209.

```text
ourseLesson {
  oneof _video_section {
  .chesscom.courses_common.v1.Range video_section = 6;
  }
  oneof _user_video_position {
  int32 user_video_position = 7;
  }
  optional .chesscom.courses.v1.CourseVariation variation = 1;
  optional .chesscom.courses.v1.CourseLessonPlayer white_player = 2;
  optional .chesscom.courses.v1.CourseLessonPlayer black_player = 3;
  repeated .chesscom.courses.v1.CourseVariationPly pl
```

**Source references:** SRC-0275, SRC-1246  
**URL references:** None independently associated  
**Related findings:** FND-01779, FND-01780, FND-01781

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01783"></a>
## FND-01783: chesscom.courses.v1.CourseLesson.user_video_position = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 user_video_position = 7;

### Evidence

- **SRC-0275** `research/proto/chesscom/courses/v1/course_lesson.proto` — [preserved redacted evidence](../evidence/text/5f236d84060b966b7f36099753be1f4f3dbc22dc7fe59102d21a40dddd01c37d.proto)
  Character offset 240.

```text
ction {
  .chesscom.courses_common.v1.Range video_section = 6;
  }
  oneof _user_video_position {
  int32 user_video_position = 7;
  }
  optional .chesscom.courses.v1.CourseVariation variation = 1;
  optional .chesscom.courses.v1.CourseLessonPlayer white_player = 2;
  optional .chesscom.courses.v1.CourseLessonPlayer black_player = 3;
  repeated .chesscom.courses.v1.CourseVariationPly plies = 4;
  optional .chesscom.c
```

**Source references:** SRC-0275, SRC-1246  
**URL references:** None independently associated  
**Related findings:** FND-01779, FND-01780, FND-01781

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01784"></a>
## FND-01784: chesscom.courses.v1.CourseLesson.variation = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseVariation variation = 1;

### Evidence

- **SRC-0275** `research/proto/chesscom/courses/v1/course_lesson.proto` — [preserved redacted evidence](../evidence/text/5f236d84060b966b7f36099753be1f4f3dbc22dc7fe59102d21a40dddd01c37d.proto)
  Character offset 277.

```text
.Range video_section = 6;
  }
  oneof _user_video_position {
  int32 user_video_position = 7;
  }
  optional .chesscom.courses.v1.CourseVariation variation = 1;
  optional .chesscom.courses.v1.CourseLessonPlayer white_player = 2;
  optional .chesscom.courses.v1.CourseLessonPlayer black_player = 3;
  repeated .chesscom.courses.v1.CourseVariationPly plies = 4;
  optional .chesscom.courses.v1.CourseConfiguration setting
```

**Source references:** SRC-0275, SRC-1246  
**URL references:** None independently associated  
**Related findings:** FND-01779, FND-01780, FND-01781

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01785"></a>
## FND-01785: chesscom.courses.v1.CourseLesson.white_player = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseLessonPlayer white_player = 2;

### Evidence

- **SRC-0275** `research/proto/chesscom/courses/v1/course_lesson.proto` — [preserved redacted evidence](../evidence/text/5f236d84060b966b7f36099753be1f4f3dbc22dc7fe59102d21a40dddd01c37d.proto)
  Character offset 340.

```text
int32 user_video_position = 7;
  }
  optional .chesscom.courses.v1.CourseVariation variation = 1;
  optional .chesscom.courses.v1.CourseLessonPlayer white_player = 2;
  optional .chesscom.courses.v1.CourseLessonPlayer black_player = 3;
  repeated .chesscom.courses.v1.CourseVariationPly plies = 4;
  optional .chesscom.courses.v1.CourseConfiguration settings = 5;
  optional .chesscom.chess.v1.Color first_learnable_move
```

**Source references:** SRC-0275, SRC-1246  
**URL references:** None independently associated  
**Related findings:** FND-01779, FND-01780, FND-01781

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01786"></a>
## FND-01786: chesscom.courses.v1.CourseLesson.black_player = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseLessonPlayer black_player = 3;

### Evidence

- **SRC-0275** `research/proto/chesscom/courses/v1/course_lesson.proto` — [preserved redacted evidence](../evidence/text/5f236d84060b966b7f36099753be1f4f3dbc22dc7fe59102d21a40dddd01c37d.proto)
  Character offset 409.

```text
urseVariation variation = 1;
  optional .chesscom.courses.v1.CourseLessonPlayer white_player = 2;
  optional .chesscom.courses.v1.CourseLessonPlayer black_player = 3;
  repeated .chesscom.courses.v1.CourseVariationPly plies = 4;
  optional .chesscom.courses.v1.CourseConfiguration settings = 5;
  optional .chesscom.chess.v1.Color first_learnable_move_color = 8;
  optional int32 initial_ply_offset = 9;
}

```

**Source references:** SRC-0275, SRC-1246  
**URL references:** None independently associated  
**Related findings:** FND-01779, FND-01780, FND-01781

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01787"></a>
## FND-01787: chesscom.courses.v1.CourseLesson.plies = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseVariationPly plies = 4;

### Evidence

- **SRC-0275** `research/proto/chesscom/courses/v1/course_lesson.proto` — [preserved redacted evidence](../evidence/text/5f236d84060b966b7f36099753be1f4f3dbc22dc7fe59102d21a40dddd01c37d.proto)
  Character offset 478.

```text
ssonPlayer white_player = 2;
  optional .chesscom.courses.v1.CourseLessonPlayer black_player = 3;
  repeated .chesscom.courses.v1.CourseVariationPly plies = 4;
  optional .chesscom.courses.v1.CourseConfiguration settings = 5;
  optional .chesscom.chess.v1.Color first_learnable_move_color = 8;
  optional int32 initial_ply_offset = 9;
}

```

**Source references:** SRC-0275, SRC-1246  
**URL references:** None independently associated  
**Related findings:** FND-01779, FND-01780, FND-01781

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01788"></a>
## FND-01788: chesscom.courses.v1.CourseLesson.settings = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseConfiguration settings = 5;

### Evidence

- **SRC-0275** `research/proto/chesscom/courses/v1/course_lesson.proto` — [preserved redacted evidence](../evidence/text/5f236d84060b966b7f36099753be1f4f3dbc22dc7fe59102d21a40dddd01c37d.proto)
  Character offset 540.

```text
ourseLessonPlayer black_player = 3;
  repeated .chesscom.courses.v1.CourseVariationPly plies = 4;
  optional .chesscom.courses.v1.CourseConfiguration settings = 5;
  optional .chesscom.chess.v1.Color first_learnable_move_color = 8;
  optional int32 initial_ply_offset = 9;
}

```

**Source references:** SRC-0275, SRC-1246  
**URL references:** None independently associated  
**Related findings:** FND-01779, FND-01780, FND-01781

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01789"></a>
## FND-01789: chesscom.courses.v1.CourseLesson.first_learnable_move_color = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Color first_learnable_move_color = 8;

### Evidence

- **SRC-0275** `research/proto/chesscom/courses/v1/course_lesson.proto` — [preserved redacted evidence](../evidence/text/5f236d84060b966b7f36099753be1f4f3dbc22dc7fe59102d21a40dddd01c37d.proto)
  Character offset 606.

```text
1.CourseVariationPly plies = 4;
  optional .chesscom.courses.v1.CourseConfiguration settings = 5;
  optional .chesscom.chess.v1.Color first_learnable_move_color = 8;
  optional int32 initial_ply_offset = 9;
}

```

**Source references:** SRC-0275, SRC-1246  
**URL references:** None independently associated  
**Related findings:** FND-01779, FND-01780, FND-01781

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01790"></a>
## FND-01790: chesscom.courses.v1.CourseLesson.initial_ply_offset = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 initial_ply_offset = 9;

### Evidence

- **SRC-0275** `research/proto/chesscom/courses/v1/course_lesson.proto` — [preserved redacted evidence](../evidence/text/5f236d84060b966b7f36099753be1f4f3dbc22dc7fe59102d21a40dddd01c37d.proto)
  Character offset 674.

```text
seConfiguration settings = 5;
  optional .chesscom.chess.v1.Color first_learnable_move_color = 8;
  optional int32 initial_ply_offset = 9;
}

```

**Source references:** SRC-0275, SRC-1246  
**URL references:** None independently associated  
**Related findings:** FND-01779, FND-01780, FND-01781

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01791"></a>
## FND-01791: message declaration: chesscom.courses.v1.CourseLessonPlayer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseLessonPlayer {

### Evidence

- **SRC-0276** `research/proto/chesscom/courses/v1/course_lesson_player.proto` — [preserved redacted evidence](../evidence/text/f699293a856ad4254f8b8811800295e098830b39d0895c19e5a8a781f192e611.proto)
  Character offset 107.

```text
ce: chesscom/courses/v1/course_lesson_player.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseLessonPlayer {
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 2;
  }
  optional string name = 1;
  optional bool is_author = 3;
}

```

**Source references:** SRC-0276, SRC-1247  
**URL references:** None independently associated  
**Related findings:** FND-01792, FND-01793

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01792"></a>
## FND-01792: oneof declaration: chesscom.courses.v1.CourseLessonPlayer._picture

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _picture {

### Evidence

- **SRC-0276** `research/proto/chesscom/courses/v1/course_lesson_player.proto` — [preserved redacted evidence](../evidence/text/f699293a856ad4254f8b8811800295e098830b39d0895c19e5a8a781f192e611.proto)
  Character offset 138.

```text
lesson_player.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseLessonPlayer {
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 2;
  }
  optional string name = 1;
  optional bool is_author = 3;
}

```

**Source references:** SRC-0276, SRC-1247  
**URL references:** None independently associated  
**Related findings:** FND-01791, FND-01793

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01793"></a>
## FND-01793: chesscom.courses.v1.CourseLessonPlayer.picture = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses_common.v1.Picture picture = 2;

### Evidence

- **SRC-0276** `research/proto/chesscom/courses/v1/course_lesson_player.proto` — [preserved redacted evidence](../evidence/text/f699293a856ad4254f8b8811800295e098830b39d0895c19e5a8a781f192e611.proto)
  Character offset 157.

```text

// syntax: proto3

package chesscom.courses.v1;

message CourseLessonPlayer {
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 2;
  }
  optional string name = 1;
  optional bool is_author = 3;
}

```

**Source references:** SRC-0276, SRC-1247  
**URL references:** None independently associated  
**Related findings:** FND-01791, FND-01792

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01794"></a>
## FND-01794: chesscom.courses.v1.CourseLessonPlayer.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0276** `research/proto/chesscom/courses/v1/course_lesson_player.proto` — [preserved redacted evidence](../evidence/text/f699293a856ad4254f8b8811800295e098830b39d0895c19e5a8a781f192e611.proto)
  Character offset 212.

```text
ge CourseLessonPlayer {
  oneof _picture {
  .chesscom.courses_common.v1.Picture picture = 2;
  }
  optional string name = 1;
  optional bool is_author = 3;
}

```

**Source references:** SRC-0276, SRC-1247  
**URL references:** None independently associated  
**Related findings:** FND-01791, FND-01792, FND-01793

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01795"></a>
## FND-01795: chesscom.courses.v1.CourseLessonPlayer.is_author = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_author = 3;

### Evidence

- **SRC-0276** `research/proto/chesscom/courses/v1/course_lesson_player.proto` — [preserved redacted evidence](../evidence/text/f699293a856ad4254f8b8811800295e098830b39d0895c19e5a8a781f192e611.proto)
  Character offset 240.

```text
eof _picture {
  .chesscom.courses_common.v1.Picture picture = 2;
  }
  optional string name = 1;
  optional bool is_author = 3;
}

```

**Source references:** SRC-0276, SRC-1247  
**URL references:** None independently associated  
**Related findings:** FND-01791, FND-01792, FND-01793

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01796"></a>
## FND-01796: message declaration: chesscom.courses.v1.CoursePosition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoursePosition {

### Evidence

- **SRC-0277** `research/proto/chesscom/courses/v1/course_position.proto` — [preserved redacted evidence](../evidence/text/9eb2e7359dcf0b9cd5a70e3274ca132e63861cfe2af5a60f9819e31ad2ace384.proto)
  Character offset 102.

```text
 source: chesscom/courses/v1/course_position.proto
// syntax: proto3

package chesscom.courses.v1;

message CoursePosition {
  optional string fen = 1;
  repeated .chesscom.courses_common.v1.CourseDrawingSquare highlights = 2;
  repeated .chesscom.courses_common.v1.CourseDrawingArrow arrows = 3;
  repeated .chesscom.courses.v1.Nag nags = 4;
}

```

**Source references:** SRC-0277, SRC-1248  
**URL references:** None independently associated  
**Related findings:** FND-01797, FND-01798

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01797"></a>
## FND-01797: chesscom.courses.v1.CoursePosition.fen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string fen = 1;

### Evidence

- **SRC-0277** `research/proto/chesscom/courses/v1/course_position.proto` — [preserved redacted evidence](../evidence/text/9eb2e7359dcf0b9cd5a70e3274ca132e63861cfe2af5a60f9819e31ad2ace384.proto)
  Character offset 129.

```text
1/course_position.proto
// syntax: proto3

package chesscom.courses.v1;

message CoursePosition {
  optional string fen = 1;
  repeated .chesscom.courses_common.v1.CourseDrawingSquare highlights = 2;
  repeated .chesscom.courses_common.v1.CourseDrawingArrow arrows = 3;
  repeated .chesscom.courses.v1.Nag nags = 4;
}

```

**Source references:** SRC-0277, SRC-1248  
**URL references:** None independently associated  
**Related findings:** FND-01796, FND-01798

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01798"></a>
## FND-01798: chesscom.courses.v1.CoursePosition.highlights = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses_common.v1.CourseDrawingSquare highlights = 2;

### Evidence

- **SRC-0277** `research/proto/chesscom/courses/v1/course_position.proto` — [preserved redacted evidence](../evidence/text/9eb2e7359dcf0b9cd5a70e3274ca132e63861cfe2af5a60f9819e31ad2ace384.proto)
  Character offset 156.

```text
syntax: proto3

package chesscom.courses.v1;

message CoursePosition {
  optional string fen = 1;
  repeated .chesscom.courses_common.v1.CourseDrawingSquare highlights = 2;
  repeated .chesscom.courses_common.v1.CourseDrawingArrow arrows = 3;
  repeated .chesscom.courses.v1.Nag nags = 4;
}

```

**Source references:** SRC-0277, SRC-1248  
**URL references:** None independently associated  
**Related findings:** FND-01796, FND-01797

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01799"></a>
## FND-01799: chesscom.courses.v1.CoursePosition.arrows = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses_common.v1.CourseDrawingArrow arrows = 3;

### Evidence

- **SRC-0277** `research/proto/chesscom/courses/v1/course_position.proto` — [preserved redacted evidence](../evidence/text/9eb2e7359dcf0b9cd5a70e3274ca132e63861cfe2af5a60f9819e31ad2ace384.proto)
  Character offset 231.

```text
tional string fen = 1;
  repeated .chesscom.courses_common.v1.CourseDrawingSquare highlights = 2;
  repeated .chesscom.courses_common.v1.CourseDrawingArrow arrows = 3;
  repeated .chesscom.courses.v1.Nag nags = 4;
}

```

**Source references:** SRC-0277, SRC-1248  
**URL references:** None independently associated  
**Related findings:** FND-01796, FND-01797, FND-01798

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01800"></a>
## FND-01800: chesscom.courses.v1.CoursePosition.nags = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.Nag nags = 4;

### Evidence

- **SRC-0277** `research/proto/chesscom/courses/v1/course_position.proto` — [preserved redacted evidence](../evidence/text/9eb2e7359dcf0b9cd5a70e3274ca132e63861cfe2af5a60f9819e31ad2ace384.proto)
  Character offset 301.

```text
awingSquare highlights = 2;
  repeated .chesscom.courses_common.v1.CourseDrawingArrow arrows = 3;
  repeated .chesscom.courses.v1.Nag nags = 4;
}

```

**Source references:** SRC-0277, SRC-1248  
**URL references:** None independently associated  
**Related findings:** FND-01796, FND-01797, FND-01798

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01801"></a>
## FND-01801: message declaration: chesscom.courses.v1.CourseProduct

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseProduct {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 101.

```text
/ source: chesscom/courses/v1/course_product.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseProduct {
  oneof _video {
  .chesscom.courses_common.v1.CourseVideo video = 13;
  }
  oneof _move_trainer_sku {
  string move_trainer_sku = 15;
  }
  oneof _video_sku {
  string video_sku = 16;
  }
  oneof _move_trainer_price {
  .chesscom.courses_common.v1.CoursePrice move_trainer_price = 17;
  }
  oneo
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01802"></a>
## FND-01802: oneof declaration: chesscom.courses.v1.CourseProduct._video

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _video {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 127.

```text
/v1/course_product.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseProduct {
  oneof _video {
  .chesscom.courses_common.v1.CourseVideo video = 13;
  }
  oneof _move_trainer_sku {
  string move_trainer_sku = 15;
  }
  oneof _video_sku {
  string video_sku = 16;
  }
  oneof _move_trainer_price {
  .chesscom.courses_common.v1.CoursePrice move_trainer_price = 17;
  }
  oneof _video_price {
  .chessc
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01803"></a>
## FND-01803: chesscom.courses.v1.CourseProduct.video = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses_common.v1.CourseVideo video = 13;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 144.

```text
t.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseProduct {
  oneof _video {
  .chesscom.courses_common.v1.CourseVideo video = 13;
  }
  oneof _move_trainer_sku {
  string move_trainer_sku = 15;
  }
  oneof _video_sku {
  string video_sku = 16;
  }
  oneof _move_trainer_price {
  .chesscom.courses_common.v1.CoursePrice move_trainer_price = 17;
  }
  oneof _video_price {
  .chesscom.courses_common
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01804"></a>
## FND-01804: oneof declaration: chesscom.courses.v1.CourseProduct._move_trainer_sku

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _move_trainer_sku {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 202.

```text
essage CourseProduct {
  oneof _video {
  .chesscom.courses_common.v1.CourseVideo video = 13;
  }
  oneof _move_trainer_sku {
  string move_trainer_sku = 15;
  }
  oneof _video_sku {
  string video_sku = 16;
  }
  oneof _move_trainer_price {
  .chesscom.courses_common.v1.CoursePrice move_trainer_price = 17;
  }
  oneof _video_price {
  .chesscom.courses_common.v1.CoursePrice video_price = 18;
  }
  oneof _move_traine
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01805"></a>
## FND-01805: chesscom.courses.v1.CourseProduct.move_trainer_sku = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string move_trainer_sku = 15;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 230.

```text
of _video {
  .chesscom.courses_common.v1.CourseVideo video = 13;
  }
  oneof _move_trainer_sku {
  string move_trainer_sku = 15;
  }
  oneof _video_sku {
  string video_sku = 16;
  }
  oneof _move_trainer_price {
  .chesscom.courses_common.v1.CoursePrice move_trainer_price = 17;
  }
  oneof _video_price {
  .chesscom.courses_common.v1.CoursePrice video_price = 18;
  }
  oneof _move_trainer_purchase_date {
  .google.
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01806"></a>
## FND-01806: oneof declaration: chesscom.courses.v1.CourseProduct._video_sku

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _video_sku {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 266.

```text
on.v1.CourseVideo video = 13;
  }
  oneof _move_trainer_sku {
  string move_trainer_sku = 15;
  }
  oneof _video_sku {
  string video_sku = 16;
  }
  oneof _move_trainer_price {
  .chesscom.courses_common.v1.CoursePrice move_trainer_price = 17;
  }
  oneof _video_price {
  .chesscom.courses_common.v1.CoursePrice video_price = 18;
  }
  oneof _move_trainer_purchase_date {
  .google.protobuf.Timestamp move_trainer_purc
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01807"></a>
## FND-01807: chesscom.courses.v1.CourseProduct.video_sku = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string video_sku = 16;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 287.

```text
eo = 13;
  }
  oneof _move_trainer_sku {
  string move_trainer_sku = 15;
  }
  oneof _video_sku {
  string video_sku = 16;
  }
  oneof _move_trainer_price {
  .chesscom.courses_common.v1.CoursePrice move_trainer_price = 17;
  }
  oneof _video_price {
  .chesscom.courses_common.v1.CoursePrice video_price = 18;
  }
  oneof _move_trainer_purchase_date {
  .google.protobuf.Timestamp move_trainer_purchase_date = 19;
  }
 
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01808"></a>
## FND-01808: oneof declaration: chesscom.courses.v1.CourseProduct._move_trainer_price

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _move_trainer_price {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 316.

```text
ainer_sku {
  string move_trainer_sku = 15;
  }
  oneof _video_sku {
  string video_sku = 16;
  }
  oneof _move_trainer_price {
  .chesscom.courses_common.v1.CoursePrice move_trainer_price = 17;
  }
  oneof _video_price {
  .chesscom.courses_common.v1.CoursePrice video_price = 18;
  }
  oneof _move_trainer_purchase_date {
  .google.protobuf.Timestamp move_trainer_purchase_date = 19;
  }
  oneof _video_purchase_date {
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01809"></a>
## FND-01809: chesscom.courses.v1.CourseProduct.move_trainer_price = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses_common.v1.CoursePrice move_trainer_price = 17;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 346.

```text
ner_sku = 15;
  }
  oneof _video_sku {
  string video_sku = 16;
  }
  oneof _move_trainer_price {
  .chesscom.courses_common.v1.CoursePrice move_trainer_price = 17;
  }
  oneof _video_price {
  .chesscom.courses_common.v1.CoursePrice video_price = 18;
  }
  oneof _move_trainer_purchase_date {
  .google.protobuf.Timestamp move_trainer_purchase_date = 19;
  }
  oneof _video_purchase_date {
  .google.protobuf.Timestamp 
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01810"></a>
## FND-01810: oneof declaration: chesscom.courses.v1.CourseProduct._video_price

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _video_price {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 417.

```text
neof _move_trainer_price {
  .chesscom.courses_common.v1.CoursePrice move_trainer_price = 17;
  }
  oneof _video_price {
  .chesscom.courses_common.v1.CoursePrice video_price = 18;
  }
  oneof _move_trainer_purchase_date {
  .google.protobuf.Timestamp move_trainer_purchase_date = 19;
  }
  oneof _video_purchase_date {
  .google.protobuf.Timestamp video_purchase_date = 20;
  }
  oneof _video_hours_count {
  int32 vide
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01811"></a>
## FND-01811: chesscom.courses.v1.CourseProduct.video_price = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses_common.v1.CoursePrice video_price = 18;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 440.

```text
e {
  .chesscom.courses_common.v1.CoursePrice move_trainer_price = 17;
  }
  oneof _video_price {
  .chesscom.courses_common.v1.CoursePrice video_price = 18;
  }
  oneof _move_trainer_purchase_date {
  .google.protobuf.Timestamp move_trainer_purchase_date = 19;
  }
  oneof _video_purchase_date {
  .google.protobuf.Timestamp video_purchase_date = 20;
  }
  oneof _video_hours_count {
  int32 video_hours_count = 23;
  }
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01812"></a>
## FND-01812: oneof declaration: chesscom.courses.v1.CourseProduct._move_trainer_purchase_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _move_trainer_purchase_date {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 504.

```text
 = 17;
  }
  oneof _video_price {
  .chesscom.courses_common.v1.CoursePrice video_price = 18;
  }
  oneof _move_trainer_purchase_date {
  .google.protobuf.Timestamp move_trainer_purchase_date = 19;
  }
  oneof _video_purchase_date {
  .google.protobuf.Timestamp video_purchase_date = 20;
  }
  oneof _video_hours_count {
  int32 video_hours_count = 23;
  }
  oneof _is_deleted {
  bool is_deleted = 26;
  }
  oneof _free
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01813"></a>
## FND-01813: chesscom.courses.v1.CourseProduct.move_trainer_purchase_date = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp move_trainer_purchase_date = 19;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 542.

```text
hesscom.courses_common.v1.CoursePrice video_price = 18;
  }
  oneof _move_trainer_purchase_date {
  .google.protobuf.Timestamp move_trainer_purchase_date = 19;
  }
  oneof _video_purchase_date {
  .google.protobuf.Timestamp video_purchase_date = 20;
  }
  oneof _video_hours_count {
  int32 video_hours_count = 23;
  }
  oneof _is_deleted {
  bool is_deleted = 26;
  }
  oneof _free_video_minutes {
  int32 free_video_mi
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01814"></a>
## FND-01814: oneof declaration: chesscom.courses.v1.CourseProduct._video_purchase_date

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _video_purchase_date {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 608.

```text
f _move_trainer_purchase_date {
  .google.protobuf.Timestamp move_trainer_purchase_date = 19;
  }
  oneof _video_purchase_date {
  .google.protobuf.Timestamp video_purchase_date = 20;
  }
  oneof _video_hours_count {
  int32 video_hours_count = 23;
  }
  oneof _is_deleted {
  bool is_deleted = 26;
  }
  oneof _free_video_minutes {
  int32 free_video_minutes = 27;
  }
  oneof _user_access_grant {
  .chesscom.courses.v
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01815"></a>
## FND-01815: chesscom.courses.v1.CourseProduct.video_purchase_date = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp video_purchase_date = 20;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 639.

```text

  .google.protobuf.Timestamp move_trainer_purchase_date = 19;
  }
  oneof _video_purchase_date {
  .google.protobuf.Timestamp video_purchase_date = 20;
  }
  oneof _video_hours_count {
  int32 video_hours_count = 23;
  }
  oneof _is_deleted {
  bool is_deleted = 26;
  }
  oneof _free_video_minutes {
  int32 free_video_minutes = 27;
  }
  oneof _user_access_grant {
  .chesscom.courses.v1.UserAccessGrant user_access_g
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01816"></a>
## FND-01816: oneof declaration: chesscom.courses.v1.CourseProduct._video_hours_count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _video_hours_count {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 698.

```text
19;
  }
  oneof _video_purchase_date {
  .google.protobuf.Timestamp video_purchase_date = 20;
  }
  oneof _video_hours_count {
  int32 video_hours_count = 23;
  }
  oneof _is_deleted {
  bool is_deleted = 26;
  }
  oneof _free_video_minutes {
  int32 free_video_minutes = 27;
  }
  oneof _user_access_grant {
  .chesscom.courses.v1.UserAccessGrant user_access_grant = 29;
  }
  oneof _best_for {
  .chesscom.courses_comm
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01817"></a>
## FND-01817: chesscom.courses.v1.CourseProduct.video_hours_count = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 video_hours_count = 23;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 727.

```text
se_date {
  .google.protobuf.Timestamp video_purchase_date = 20;
  }
  oneof _video_hours_count {
  int32 video_hours_count = 23;
  }
  oneof _is_deleted {
  bool is_deleted = 26;
  }
  oneof _free_video_minutes {
  int32 free_video_minutes = 27;
  }
  oneof _user_access_grant {
  .chesscom.courses.v1.UserAccessGrant user_access_grant = 29;
  }
  oneof _best_for {
  .chesscom.courses_common.v1.CourseTargetLevel best_
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01818"></a>
## FND-01818: oneof declaration: chesscom.courses.v1.CourseProduct._is_deleted

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_deleted {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 763.

```text
mp video_purchase_date = 20;
  }
  oneof _video_hours_count {
  int32 video_hours_count = 23;
  }
  oneof _is_deleted {
  bool is_deleted = 26;
  }
  oneof _free_video_minutes {
  int32 free_video_minutes = 27;
  }
  oneof _user_access_grant {
  .chesscom.courses.v1.UserAccessGrant user_access_grant = 29;
  }
  oneof _best_for {
  .chesscom.courses_common.v1.CourseTargetLevel best_for = 30;
  }
  oneof _canonical_lin
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01819"></a>
## FND-01819: chesscom.courses.v1.CourseProduct.is_deleted = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_deleted = 26;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 785.

```text
 = 20;
  }
  oneof _video_hours_count {
  int32 video_hours_count = 23;
  }
  oneof _is_deleted {
  bool is_deleted = 26;
  }
  oneof _free_video_minutes {
  int32 free_video_minutes = 27;
  }
  oneof _user_access_grant {
  .chesscom.courses.v1.UserAccessGrant user_access_grant = 29;
  }
  oneof _best_for {
  .chesscom.courses_common.v1.CourseTargetLevel best_for = 30;
  }
  oneof _canonical_line {
  .chesscom.course
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01820"></a>
## FND-01820: oneof declaration: chesscom.courses.v1.CourseProduct._free_video_minutes

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _free_video_minutes {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 813.

```text
urs_count {
  int32 video_hours_count = 23;
  }
  oneof _is_deleted {
  bool is_deleted = 26;
  }
  oneof _free_video_minutes {
  int32 free_video_minutes = 27;
  }
  oneof _user_access_grant {
  .chesscom.courses.v1.UserAccessGrant user_access_grant = 29;
  }
  oneof _best_for {
  .chesscom.courses_common.v1.CourseTargetLevel best_for = 30;
  }
  oneof _canonical_line {
  .chesscom.courses.v1.CourseCanonicalLine can
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01821"></a>
## FND-01821: chesscom.courses.v1.CourseProduct.free_video_minutes = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 free_video_minutes = 27;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 843.

```text
s_count = 23;
  }
  oneof _is_deleted {
  bool is_deleted = 26;
  }
  oneof _free_video_minutes {
  int32 free_video_minutes = 27;
  }
  oneof _user_access_grant {
  .chesscom.courses.v1.UserAccessGrant user_access_grant = 29;
  }
  oneof _best_for {
  .chesscom.courses_common.v1.CourseTargetLevel best_for = 30;
  }
  oneof _canonical_line {
  .chesscom.courses.v1.CourseCanonicalLine canonical_line = 32;
  }
  oneof 
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01822"></a>
## FND-01822: oneof declaration: chesscom.courses.v1.CourseProduct._user_access_grant

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_access_grant {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 880.

```text
 {
  bool is_deleted = 26;
  }
  oneof _free_video_minutes {
  int32 free_video_minutes = 27;
  }
  oneof _user_access_grant {
  .chesscom.courses.v1.UserAccessGrant user_access_grant = 29;
  }
  oneof _best_for {
  .chesscom.courses_common.v1.CourseTargetLevel best_for = 30;
  }
  oneof _canonical_line {
  .chesscom.courses.v1.CourseCanonicalLine canonical_line = 32;
  }
  oneof _first_coach_comment {
  .chesscom.co
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01823"></a>
## FND-01823: chesscom.courses.v1.CourseProduct.user_access_grant = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.UserAccessGrant user_access_grant = 29;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 909.

```text
}
  oneof _free_video_minutes {
  int32 free_video_minutes = 27;
  }
  oneof _user_access_grant {
  .chesscom.courses.v1.UserAccessGrant user_access_grant = 29;
  }
  oneof _best_for {
  .chesscom.courses_common.v1.CourseTargetLevel best_for = 30;
  }
  oneof _canonical_line {
  .chesscom.courses.v1.CourseCanonicalLine canonical_line = 32;
  }
  oneof _first_coach_comment {
  .chesscom.courses.v1.CourseCoachComment f
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01824"></a>
## FND-01824: oneof declaration: chesscom.courses.v1.CourseProduct._best_for

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _best_for {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 976.

```text
}
  oneof _user_access_grant {
  .chesscom.courses.v1.UserAccessGrant user_access_grant = 29;
  }
  oneof _best_for {
  .chesscom.courses_common.v1.CourseTargetLevel best_for = 30;
  }
  oneof _canonical_line {
  .chesscom.courses.v1.CourseCanonicalLine canonical_line = 32;
  }
  oneof _first_coach_comment {
  .chesscom.courses.v1.CourseCoachComment first_coach_comment = 34;
  }
  oneof _board_preview {
  .chesscom.c
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01825"></a>
## FND-01825: chesscom.courses.v1.CourseProduct.best_for = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses_common.v1.CourseTargetLevel best_for = 30;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 996.

```text
ss_grant {
  .chesscom.courses.v1.UserAccessGrant user_access_grant = 29;
  }
  oneof _best_for {
  .chesscom.courses_common.v1.CourseTargetLevel best_for = 30;
  }
  oneof _canonical_line {
  .chesscom.courses.v1.CourseCanonicalLine canonical_line = 32;
  }
  oneof _first_coach_comment {
  .chesscom.courses.v1.CourseCoachComment first_coach_comment = 34;
  }
  oneof _board_preview {
  .chesscom.courses_common.v1.Cou
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01826"></a>
## FND-01826: oneof declaration: chesscom.courses.v1.CourseProduct._canonical_line

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _canonical_line {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1063.

```text
 = 29;
  }
  oneof _best_for {
  .chesscom.courses_common.v1.CourseTargetLevel best_for = 30;
  }
  oneof _canonical_line {
  .chesscom.courses.v1.CourseCanonicalLine canonical_line = 32;
  }
  oneof _first_coach_comment {
  .chesscom.courses.v1.CourseCoachComment first_coach_comment = 34;
  }
  oneof _board_preview {
  .chesscom.courses_common.v1.CourseBoardPreview board_preview = 35;
  }
  optional string id = 1;
 
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01827"></a>
## FND-01827: chesscom.courses.v1.CourseProduct.canonical_line = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseCanonicalLine canonical_line = 32;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1089.

```text
or {
  .chesscom.courses_common.v1.CourseTargetLevel best_for = 30;
  }
  oneof _canonical_line {
  .chesscom.courses.v1.CourseCanonicalLine canonical_line = 32;
  }
  oneof _first_coach_comment {
  .chesscom.courses.v1.CourseCoachComment first_coach_comment = 34;
  }
  oneof _board_preview {
  .chesscom.courses_common.v1.CourseBoardPreview board_preview = 35;
  }
  optional string id = 1;
  optional string name = 2;
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01828"></a>
## FND-01828: oneof declaration: chesscom.courses.v1.CourseProduct._first_coach_comment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _first_coach_comment {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1157.

```text
  }
  oneof _canonical_line {
  .chesscom.courses.v1.CourseCanonicalLine canonical_line = 32;
  }
  oneof _first_coach_comment {
  .chesscom.courses.v1.CourseCoachComment first_coach_comment = 34;
  }
  oneof _board_preview {
  .chesscom.courses_common.v1.CourseBoardPreview board_preview = 35;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional string short_descript
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01829"></a>
## FND-01829: chesscom.courses.v1.CourseProduct.first_coach_comment = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseCoachComment first_coach_comment = 34;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1188.

```text
 .chesscom.courses.v1.CourseCanonicalLine canonical_line = 32;
  }
  oneof _first_coach_comment {
  .chesscom.courses.v1.CourseCoachComment first_coach_comment = 34;
  }
  oneof _board_preview {
  .chesscom.courses_common.v1.CourseBoardPreview board_preview = 35;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional string short_description = 4;
  optional .chesscom.c
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01830"></a>
## FND-01830: oneof declaration: chesscom.courses.v1.CourseProduct._board_preview

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_preview {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1260.

```text
of _first_coach_comment {
  .chesscom.courses.v1.CourseCoachComment first_coach_comment = 34;
  }
  oneof _board_preview {
  .chesscom.courses_common.v1.CourseBoardPreview board_preview = 35;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional string short_description = 4;
  optional .chesscom.courses_common.v1.Picture square_picture = 5;
  optional .chesscom.course
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01831"></a>
## FND-01831: chesscom.courses.v1.CourseProduct.board_preview = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses_common.v1.CourseBoardPreview board_preview = 35;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1285.

```text

  .chesscom.courses.v1.CourseCoachComment first_coach_comment = 34;
  }
  oneof _board_preview {
  .chesscom.courses_common.v1.CourseBoardPreview board_preview = 35;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional string short_description = 4;
  optional .chesscom.courses_common.v1.Picture square_picture = 5;
  optional .chesscom.courses_common.v1.Picture recta
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01832"></a>
## FND-01832: chesscom.courses.v1.CourseProduct.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1358.

```text
  oneof _board_preview {
  .chesscom.courses_common.v1.CourseBoardPreview board_preview = 35;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional string short_description = 4;
  optional .chesscom.courses_common.v1.Picture square_picture = 5;
  optional .chesscom.courses_common.v1.Picture rectangular_picture = 6;
  optional .chesscom.courses_common.v1.CourseRating r
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01833"></a>
## FND-01833: chesscom.courses.v1.CourseProduct.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1384.

```text
 .chesscom.courses_common.v1.CourseBoardPreview board_preview = 35;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional string short_description = 4;
  optional .chesscom.courses_common.v1.Picture square_picture = 5;
  optional .chesscom.courses_common.v1.Picture rectangular_picture = 6;
  optional .chesscom.courses_common.v1.CourseRating rating = 7;
  optional .che
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01834"></a>
## FND-01834: chesscom.courses.v1.CourseProduct.description = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string description = 3;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1412.

```text
.CourseBoardPreview board_preview = 35;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional string short_description = 4;
  optional .chesscom.courses_common.v1.Picture square_picture = 5;
  optional .chesscom.courses_common.v1.Picture rectangular_picture = 6;
  optional .chesscom.courses_common.v1.CourseRating rating = 7;
  optional .chesscom.courses_common.v1.Rang
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01835"></a>
## FND-01835: chesscom.courses.v1.CourseProduct.short_description = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string short_description = 4;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1447.

```text
 35;
  }
  optional string id = 1;
  optional string name = 2;
  optional string description = 3;
  optional string short_description = 4;
  optional .chesscom.courses_common.v1.Picture square_picture = 5;
  optional .chesscom.courses_common.v1.Picture rectangular_picture = 6;
  optional .chesscom.courses_common.v1.CourseRating rating = 7;
  optional .chesscom.courses_common.v1.Range recommended_level_range = 8;
  op
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01836"></a>
## FND-01836: chesscom.courses.v1.CourseProduct.square_picture = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.Picture square_picture = 5;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1488.

```text
onal string name = 2;
  optional string description = 3;
  optional string short_description = 4;
  optional .chesscom.courses_common.v1.Picture square_picture = 5;
  optional .chesscom.courses_common.v1.Picture rectangular_picture = 6;
  optional .chesscom.courses_common.v1.CourseRating rating = 7;
  optional .chesscom.courses_common.v1.Range recommended_level_range = 8;
  optional .chesscom.courses_common.v1.Course
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01837"></a>
## FND-01837: chesscom.courses.v1.CourseProduct.rectangular_picture = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.Picture rectangular_picture = 6;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1555.

```text
 string short_description = 4;
  optional .chesscom.courses_common.v1.Picture square_picture = 5;
  optional .chesscom.courses_common.v1.Picture rectangular_picture = 6;
  optional .chesscom.courses_common.v1.CourseRating rating = 7;
  optional .chesscom.courses_common.v1.Range recommended_level_range = 8;
  optional .chesscom.courses_common.v1.CourseGameAspect game_aspect = 9;
  repeated .chesscom.chess.v1.Color col
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01838"></a>
## FND-01838: chesscom.courses.v1.CourseProduct.rating = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseRating rating = 7;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1627.

```text
cture square_picture = 5;
  optional .chesscom.courses_common.v1.Picture rectangular_picture = 6;
  optional .chesscom.courses_common.v1.CourseRating rating = 7;
  optional .chesscom.courses_common.v1.Range recommended_level_range = 8;
  optional .chesscom.courses_common.v1.CourseGameAspect game_aspect = 9;
  repeated .chesscom.chess.v1.Color color = 10;
  optional .google.protobuf.Timestamp release_date = 11;
  repe
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01839"></a>
## FND-01839: chesscom.courses.v1.CourseProduct.recommended_level_range = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.Range recommended_level_range = 8;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1691.

```text
.Picture rectangular_picture = 6;
  optional .chesscom.courses_common.v1.CourseRating rating = 7;
  optional .chesscom.courses_common.v1.Range recommended_level_range = 8;
  optional .chesscom.courses_common.v1.CourseGameAspect game_aspect = 9;
  repeated .chesscom.chess.v1.Color color = 10;
  optional .google.protobuf.Timestamp release_date = 11;
  repeated .chesscom.courses.v1.CourseAuthor authors = 12;
  optional 
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01840"></a>
## FND-01840: chesscom.courses.v1.CourseProduct.game_aspect = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseGameAspect game_aspect = 9;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1765.

```text
ourseRating rating = 7;
  optional .chesscom.courses_common.v1.Range recommended_level_range = 8;
  optional .chesscom.courses_common.v1.CourseGameAspect game_aspect = 9;
  repeated .chesscom.chess.v1.Color color = 10;
  optional .google.protobuf.Timestamp release_date = 11;
  repeated .chesscom.courses.v1.CourseAuthor authors = 12;
  optional string slug = 14;
  repeated string move_trainer_ids = 21;
  optional int3
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01841"></a>
## FND-01841: chesscom.courses.v1.CourseProduct.color = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Color color = 10;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1838.

```text
mmended_level_range = 8;
  optional .chesscom.courses_common.v1.CourseGameAspect game_aspect = 9;
  repeated .chesscom.chess.v1.Color color = 10;
  optional .google.protobuf.Timestamp release_date = 11;
  repeated .chesscom.courses.v1.CourseAuthor authors = 12;
  optional string slug = 14;
  repeated string move_trainer_ids = 21;
  optional int32 variation_count = 22;
  optional bool is_diamond_exclusive = 24;
  repe
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01842"></a>
## FND-01842: chesscom.courses.v1.CourseProduct.release_date = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp release_date = 11;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1886.

```text
urses_common.v1.CourseGameAspect game_aspect = 9;
  repeated .chesscom.chess.v1.Color color = 10;
  optional .google.protobuf.Timestamp release_date = 11;
  repeated .chesscom.courses.v1.CourseAuthor authors = 12;
  optional string slug = 14;
  repeated string move_trainer_ids = 21;
  optional int32 variation_count = 22;
  optional bool is_diamond_exclusive = 24;
  repeated .chesscom.api.v1.Language language = 25;
  
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01843"></a>
## FND-01843: chesscom.courses.v1.CourseProduct.authors = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseAuthor authors = 12;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 1943.

```text
ted .chesscom.chess.v1.Color color = 10;
  optional .google.protobuf.Timestamp release_date = 11;
  repeated .chesscom.courses.v1.CourseAuthor authors = 12;
  optional string slug = 14;
  repeated string move_trainer_ids = 21;
  optional int32 variation_count = 22;
  optional bool is_diamond_exclusive = 24;
  repeated .chesscom.api.v1.Language language = 25;
  optional .chesscom.courses_common.v1.CourseSource course_
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01844"></a>
## FND-01844: chesscom.courses.v1.CourseProduct.slug = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string slug = 14;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 2002.

```text
.protobuf.Timestamp release_date = 11;
  repeated .chesscom.courses.v1.CourseAuthor authors = 12;
  optional string slug = 14;
  repeated string move_trainer_ids = 21;
  optional int32 variation_count = 22;
  optional bool is_diamond_exclusive = 24;
  repeated .chesscom.api.v1.Language language = 25;
  optional .chesscom.courses_common.v1.CourseSource course_source = 28;
  repeated .chesscom.courses.v1.CourseCustomTa
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01845"></a>
## FND-01845: chesscom.courses.v1.CourseProduct.move_trainer_ids = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string move_trainer_ids = 21;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 2031.

```text
ate = 11;
  repeated .chesscom.courses.v1.CourseAuthor authors = 12;
  optional string slug = 14;
  repeated string move_trainer_ids = 21;
  optional int32 variation_count = 22;
  optional bool is_diamond_exclusive = 24;
  repeated .chesscom.api.v1.Language language = 25;
  optional .chesscom.courses_common.v1.CourseSource course_source = 28;
  repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 31;
  
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01846"></a>
## FND-01846: chesscom.courses.v1.CourseProduct.variation_count = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 variation_count = 22;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 2072.

```text
.CourseAuthor authors = 12;
  optional string slug = 14;
  repeated string move_trainer_ids = 21;
  optional int32 variation_count = 22;
  optional bool is_diamond_exclusive = 24;
  repeated .chesscom.api.v1.Language language = 25;
  optional .chesscom.courses_common.v1.CourseSource course_source = 28;
  repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 31;
  optional bool is_recommended = 33;
}

mes
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01847"></a>
## FND-01847: chesscom.courses.v1.CourseProduct.is_diamond_exclusive = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_diamond_exclusive = 24;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 2111.

```text
string slug = 14;
  repeated string move_trainer_ids = 21;
  optional int32 variation_count = 22;
  optional bool is_diamond_exclusive = 24;
  repeated .chesscom.api.v1.Language language = 25;
  optional .chesscom.courses_common.v1.CourseSource course_source = 28;
  repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 31;
  optional bool is_recommended = 33;
}

message CourseProductList {
  repeated .ch
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01848"></a>
## FND-01848: chesscom.courses.v1.CourseProduct.language = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.api.v1.Language language = 25;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 2154.

```text
ainer_ids = 21;
  optional int32 variation_count = 22;
  optional bool is_diamond_exclusive = 24;
  repeated .chesscom.api.v1.Language language = 25;
  optional .chesscom.courses_common.v1.CourseSource course_source = 28;
  repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 31;
  optional bool is_recommended = 33;
}

message CourseProductList {
  repeated .chesscom.courses.v1.CourseProduct course_list
```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01849"></a>
## FND-01849: chesscom.courses.v1.CourseProduct.course_source = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseSource course_source = 28;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 2206.

```text
2;
  optional bool is_diamond_exclusive = 24;
  repeated .chesscom.api.v1.Language language = 25;
  optional .chesscom.courses_common.v1.CourseSource course_source = 28;
  repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 31;
  optional bool is_recommended = 33;
}

message CourseProductList {
  repeated .chesscom.courses.v1.CourseProduct course_list = 1;
}

```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01850"></a>
## FND-01850: chesscom.courses.v1.CourseProduct.course_custom_tags = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 31;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 2278.

```text
1.Language language = 25;
  optional .chesscom.courses_common.v1.CourseSource course_source = 28;
  repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 31;
  optional bool is_recommended = 33;
}

message CourseProductList {
  repeated .chesscom.courses.v1.CourseProduct course_list = 1;
}

```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01851"></a>
## FND-01851: chesscom.courses.v1.CourseProduct.is_recommended = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_recommended = 33;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 2351.

```text
urce course_source = 28;
  repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 31;
  optional bool is_recommended = 33;
}

message CourseProductList {
  repeated .chesscom.courses.v1.CourseProduct course_list = 1;
}

```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01852"></a>
## FND-01852: message declaration: chesscom.courses.v1.CourseProductList

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseProductList {

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 2389.

```text
hesscom.courses.v1.CourseCustomTag course_custom_tags = 31;
  optional bool is_recommended = 33;
}

message CourseProductList {
  repeated .chesscom.courses.v1.CourseProduct course_list = 1;
}

```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01853"></a>
## FND-01853: chesscom.courses.v1.CourseProductList.course_list = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseProduct course_list = 1;

### Evidence

- **SRC-0278** `research/proto/chesscom/courses/v1/course_product.proto` — [preserved redacted evidence](../evidence/text/6cd3b6e5989a1ecf5118d9f7561dd9bdc5f1d1b2465b17777e7ffaee0e7ace53.proto)
  Character offset 2419.

```text
mTag course_custom_tags = 31;
  optional bool is_recommended = 33;
}

message CourseProductList {
  repeated .chesscom.courses.v1.CourseProduct course_list = 1;
}

```

**Source references:** SRC-0278, SRC-1249  
**URL references:** None independently associated  
**Related findings:** FND-01801, FND-01802, FND-01803

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01854"></a>
## FND-01854: message declaration: chesscom.courses.v1.GetCourseProductBySKURequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseProductBySKURequest {

### Evidence

- **SRC-0279** `research/proto/chesscom/courses/v1/course_product_by_sku_service.proto` — [preserved redacted evidence](../evidence/text/80a5fe8318c122e22e4f8c99261311b33a58d278c1be3380ef9f59e9a7d25ff0.proto)
  Character offset 116.

```text
com/courses/v1/course_product_by_sku_service.proto
// syntax: proto3

package chesscom.courses.v1;

message GetCourseProductBySKURequest {
  oneof _locale {
  string locale = 2;
  }
  optional string sku = 1;
}

message GetCourseProductBySKUResponse {
  optional .chesscom.courses.v1.CourseProduct product = 1;
}

```

**Source references:** SRC-0279, SRC-1250  
**URL references:** None independently associated  
**Related findings:** FND-01855, FND-01856

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01855"></a>
## FND-01855: oneof declaration: chesscom.courses.v1.GetCourseProductBySKURequest._locale

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _locale {

### Evidence

- **SRC-0279** `research/proto/chesscom/courses/v1/course_product_by_sku_service.proto` — [preserved redacted evidence](../evidence/text/80a5fe8318c122e22e4f8c99261311b33a58d278c1be3380ef9f59e9a7d25ff0.proto)
  Character offset 157.

```text
ice.proto
// syntax: proto3

package chesscom.courses.v1;

message GetCourseProductBySKURequest {
  oneof _locale {
  string locale = 2;
  }
  optional string sku = 1;
}

message GetCourseProductBySKUResponse {
  optional .chesscom.courses.v1.CourseProduct product = 1;
}

```

**Source references:** SRC-0279, SRC-1250  
**URL references:** None independently associated  
**Related findings:** FND-01854, FND-01856

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01856"></a>
## FND-01856: chesscom.courses.v1.GetCourseProductBySKURequest.locale = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string locale = 2;

### Evidence

- **SRC-0279** `research/proto/chesscom/courses/v1/course_product_by_sku_service.proto` — [preserved redacted evidence](../evidence/text/80a5fe8318c122e22e4f8c99261311b33a58d278c1be3380ef9f59e9a7d25ff0.proto)
  Character offset 175.

```text
x: proto3

package chesscom.courses.v1;

message GetCourseProductBySKURequest {
  oneof _locale {
  string locale = 2;
  }
  optional string sku = 1;
}

message GetCourseProductBySKUResponse {
  optional .chesscom.courses.v1.CourseProduct product = 1;
}

```

**Source references:** SRC-0279, SRC-1250  
**URL references:** None independently associated  
**Related findings:** FND-01854, FND-01855

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01857"></a>
## FND-01857: chesscom.courses.v1.GetCourseProductBySKURequest.sku = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string sku = 1;

### Evidence

- **SRC-0279** `research/proto/chesscom/courses/v1/course_product_by_sku_service.proto` — [preserved redacted evidence](../evidence/text/80a5fe8318c122e22e4f8c99261311b33a58d278c1be3380ef9f59e9a7d25ff0.proto)
  Character offset 200.

```text
om.courses.v1;

message GetCourseProductBySKURequest {
  oneof _locale {
  string locale = 2;
  }
  optional string sku = 1;
}

message GetCourseProductBySKUResponse {
  optional .chesscom.courses.v1.CourseProduct product = 1;
}

```

**Source references:** SRC-0279, SRC-1250  
**URL references:** None independently associated  
**Related findings:** FND-01854, FND-01855, FND-01856

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01858"></a>
## FND-01858: message declaration: chesscom.courses.v1.GetCourseProductBySKUResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseProductBySKUResponse {

### Evidence

- **SRC-0279** `research/proto/chesscom/courses/v1/course_product_by_sku_service.proto` — [preserved redacted evidence](../evidence/text/80a5fe8318c122e22e4f8c99261311b33a58d278c1be3380ef9f59e9a7d25ff0.proto)
  Character offset 228.

```text
ourseProductBySKURequest {
  oneof _locale {
  string locale = 2;
  }
  optional string sku = 1;
}

message GetCourseProductBySKUResponse {
  optional .chesscom.courses.v1.CourseProduct product = 1;
}

```

**Source references:** SRC-0279, SRC-1250  
**URL references:** None independently associated  
**Related findings:** FND-01854, FND-01855, FND-01856

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01859"></a>
## FND-01859: chesscom.courses.v1.GetCourseProductBySKUResponse.product = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseProduct product = 1;

### Evidence

- **SRC-0279** `research/proto/chesscom/courses/v1/course_product_by_sku_service.proto` — [preserved redacted evidence](../evidence/text/80a5fe8318c122e22e4f8c99261311b33a58d278c1be3380ef9f59e9a7d25ff0.proto)
  Character offset 270.

```text
 {
  string locale = 2;
  }
  optional string sku = 1;
}

message GetCourseProductBySKUResponse {
  optional .chesscom.courses.v1.CourseProduct product = 1;
}

```

**Source references:** SRC-0279, SRC-1250  
**URL references:** None independently associated  
**Related findings:** FND-01854, FND-01855, FND-01856

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01860"></a>
## FND-01860: message declaration: chesscom.courses.v1.CourseProductDetails

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseProductDetails {

### Evidence

- **SRC-0280** `research/proto/chesscom/courses/v1/course_product_details.proto` — [preserved redacted evidence](../evidence/text/90a48fd2df84495c8a8877b234331f58c3a19642db2cf0af9be13688679465cc.proto)
  Character offset 109.

```text
: chesscom/courses/v1/course_product_details.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseProductDetails {
  optional .chesscom.courses.v1.CourseProduct product = 1;
  repeated .chesscom.courses.v1.CourseChapterDetails chapters = 2;
  repeated .chesscom.courses_common.v1.CourseProductReview reviews = 3;
  optional string default_move_trainer_id = 4;
}

```

**Source references:** SRC-0280, SRC-1251  
**URL references:** None independently associated  
**Related findings:** FND-01861, FND-01862

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01861"></a>
## FND-01861: chesscom.courses.v1.CourseProductDetails.product = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseProduct product = 1;

### Evidence

- **SRC-0280** `research/proto/chesscom/courses/v1/course_product_details.proto` — [preserved redacted evidence](../evidence/text/90a48fd2df84495c8a8877b234331f58c3a19642db2cf0af9be13688679465cc.proto)
  Character offset 142.

```text
uct_details.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseProductDetails {
  optional .chesscom.courses.v1.CourseProduct product = 1;
  repeated .chesscom.courses.v1.CourseChapterDetails chapters = 2;
  repeated .chesscom.courses_common.v1.CourseProductReview reviews = 3;
  optional string default_move_trainer_id = 4;
}

```

**Source references:** SRC-0280, SRC-1251  
**URL references:** None independently associated  
**Related findings:** FND-01860, FND-01862

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01862"></a>
## FND-01862: chesscom.courses.v1.CourseProductDetails.chapters = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseChapterDetails chapters = 2;

### Evidence

- **SRC-0280** `research/proto/chesscom/courses/v1/course_product_details.proto` — [preserved redacted evidence](../evidence/text/90a48fd2df84495c8a8877b234331f58c3a19642db2cf0af9be13688679465cc.proto)
  Character offset 201.

```text
es.v1;

message CourseProductDetails {
  optional .chesscom.courses.v1.CourseProduct product = 1;
  repeated .chesscom.courses.v1.CourseChapterDetails chapters = 2;
  repeated .chesscom.courses_common.v1.CourseProductReview reviews = 3;
  optional string default_move_trainer_id = 4;
}

```

**Source references:** SRC-0280, SRC-1251  
**URL references:** None independently associated  
**Related findings:** FND-01860, FND-01861

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01863"></a>
## FND-01863: chesscom.courses.v1.CourseProductDetails.reviews = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses_common.v1.CourseProductReview reviews = 3;

### Evidence

- **SRC-0280** `research/proto/chesscom/courses/v1/course_product_details.proto` — [preserved redacted evidence](../evidence/text/90a48fd2df84495c8a8877b234331f58c3a19642db2cf0af9be13688679465cc.proto)
  Character offset 268.

```text
.v1.CourseProduct product = 1;
  repeated .chesscom.courses.v1.CourseChapterDetails chapters = 2;
  repeated .chesscom.courses_common.v1.CourseProductReview reviews = 3;
  optional string default_move_trainer_id = 4;
}

```

**Source references:** SRC-0280, SRC-1251  
**URL references:** None independently associated  
**Related findings:** FND-01860, FND-01861, FND-01862

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01864"></a>
## FND-01864: chesscom.courses.v1.CourseProductDetails.default_move_trainer_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string default_move_trainer_id = 4;

### Evidence

- **SRC-0280** `research/proto/chesscom/courses/v1/course_product_details.proto` — [preserved redacted evidence](../evidence/text/90a48fd2df84495c8a8877b234331f58c3a19642db2cf0af9be13688679465cc.proto)
  Character offset 340.

```text
pterDetails chapters = 2;
  repeated .chesscom.courses_common.v1.CourseProductReview reviews = 3;
  optional string default_move_trainer_id = 4;
}

```

**Source references:** SRC-0280, SRC-1251  
**URL references:** None independently associated  
**Related findings:** FND-01860, FND-01861, FND-01862

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01865"></a>
## FND-01865: message declaration: chesscom.courses.v1.GetCourseProductBySlugRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseProductBySlugRequest {

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 117.

```text
om/courses/v1/course_product_details_service.proto
// syntax: proto3

package chesscom.courses.v1;

message GetCourseProductBySlugRequest {
  optional string slug = 1;
  optional string country_code = 2;
}

message GetCourseProductBySlugResponse {
  optional .chesscom.courses.v1.CourseProductDetails details = 1;
}

message ClaimCourseProductRequest {
  optional string product_id = 1;
}

message ClaimCourseProductResp
```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01866, FND-01867

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01866"></a>
## FND-01866: chesscom.courses.v1.GetCourseProductBySlugRequest.slug = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string slug = 1;

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 159.

```text
ce.proto
// syntax: proto3

package chesscom.courses.v1;

message GetCourseProductBySlugRequest {
  optional string slug = 1;
  optional string country_code = 2;
}

message GetCourseProductBySlugResponse {
  optional .chesscom.courses.v1.CourseProductDetails details = 1;
}

message ClaimCourseProductRequest {
  optional string product_id = 1;
}

message ClaimCourseProductResponse {
  optional string default_move_trai
```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01867

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01867"></a>
## FND-01867: chesscom.courses.v1.GetCourseProductBySlugRequest.country_code = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string country_code = 2;

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 187.

```text
package chesscom.courses.v1;

message GetCourseProductBySlugRequest {
  optional string slug = 1;
  optional string country_code = 2;
}

message GetCourseProductBySlugResponse {
  optional .chesscom.courses.v1.CourseProductDetails details = 1;
}

message ClaimCourseProductRequest {
  optional string product_id = 1;
}

message ClaimCourseProductResponse {
  optional string default_move_trainer_id = 1;
}

message GetDe
```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01868"></a>
## FND-01868: message declaration: chesscom.courses.v1.GetCourseProductBySlugResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseProductBySlugResponse {

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 224.

```text
 GetCourseProductBySlugRequest {
  optional string slug = 1;
  optional string country_code = 2;
}

message GetCourseProductBySlugResponse {
  optional .chesscom.courses.v1.CourseProductDetails details = 1;
}

message ClaimCourseProductRequest {
  optional string product_id = 1;
}

message ClaimCourseProductResponse {
  optional string default_move_trainer_id = 1;
}

message GetDefaultMoveTrainerIdByProductIdRequest 
```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866, FND-01867

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01869"></a>
## FND-01869: chesscom.courses.v1.GetCourseProductBySlugResponse.details = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseProductDetails details = 1;

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 267.

```text
 string slug = 1;
  optional string country_code = 2;
}

message GetCourseProductBySlugResponse {
  optional .chesscom.courses.v1.CourseProductDetails details = 1;
}

message ClaimCourseProductRequest {
  optional string product_id = 1;
}

message ClaimCourseProductResponse {
  optional string default_move_trainer_id = 1;
}

message GetDefaultMoveTrainerIdByProductIdRequest {
  optional string product_id = 1;
}

mess
```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866, FND-01867

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01870"></a>
## FND-01870: message declaration: chesscom.courses.v1.ClaimCourseProductRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ClaimCourseProductRequest {

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 334.

```text
tCourseProductBySlugResponse {
  optional .chesscom.courses.v1.CourseProductDetails details = 1;
}

message ClaimCourseProductRequest {
  optional string product_id = 1;
}

message ClaimCourseProductResponse {
  optional string default_move_trainer_id = 1;
}

message GetDefaultMoveTrainerIdByProductIdRequest {
  optional string product_id = 1;
}

message GetDefaultMoveTrainerIdByProductIdResponse {
  optional string 
```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866, FND-01867

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01871"></a>
## FND-01871: chesscom.courses.v1.ClaimCourseProductRequest.product_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string product_id = 1;

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 372.

```text
nal .chesscom.courses.v1.CourseProductDetails details = 1;
}

message ClaimCourseProductRequest {
  optional string product_id = 1;
}

message ClaimCourseProductResponse {
  optional string default_move_trainer_id = 1;
}

message GetDefaultMoveTrainerIdByProductIdRequest {
  optional string product_id = 1;
}

message GetDefaultMoveTrainerIdByProductIdResponse {
  optional string default_move_trainer_id = 1;
  optiona
```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866, FND-01867

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01872"></a>
## FND-01872: message declaration: chesscom.courses.v1.ClaimCourseProductResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ClaimCourseProductResponse {

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 407.

```text
uctDetails details = 1;
}

message ClaimCourseProductRequest {
  optional string product_id = 1;
}

message ClaimCourseProductResponse {
  optional string default_move_trainer_id = 1;
}

message GetDefaultMoveTrainerIdByProductIdRequest {
  optional string product_id = 1;
}

message GetDefaultMoveTrainerIdByProductIdResponse {
  optional string default_move_trainer_id = 1;
  optional bool is_course_owned = 2;
  optio
```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866, FND-01867

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01873"></a>
## FND-01873: chesscom.courses.v1.ClaimCourseProductResponse.default_move_trainer_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string default_move_trainer_id = 1;

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 446.

```text
mCourseProductRequest {
  optional string product_id = 1;
}

message ClaimCourseProductResponse {
  optional string default_move_trainer_id = 1;
}

message GetDefaultMoveTrainerIdByProductIdRequest {
  optional string product_id = 1;
}

message GetDefaultMoveTrainerIdByProductIdResponse {
  optional string default_move_trainer_id = 1;
  optional bool is_course_owned = 2;
  optional bool is_video_owned = 3;
}

message
```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866, FND-01867

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01874"></a>
## FND-01874: message declaration: chesscom.courses.v1.GetDefaultMoveTrainerIdByProductIdRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetDefaultMoveTrainerIdByProductIdRequest {

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 494.

```text
t_id = 1;
}

message ClaimCourseProductResponse {
  optional string default_move_trainer_id = 1;
}

message GetDefaultMoveTrainerIdByProductIdRequest {
  optional string product_id = 1;
}

message GetDefaultMoveTrainerIdByProductIdResponse {
  optional string default_move_trainer_id = 1;
  optional bool is_course_owned = 2;
  optional bool is_video_owned = 3;
}

message SetCourseActiveRequest {
  optional string cour
```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866, FND-01867

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
