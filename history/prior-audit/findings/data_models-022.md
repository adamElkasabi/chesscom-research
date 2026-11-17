# data_models — findings 2101–2200

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-02375"></a>
## FND-02375: chesscom.courses_common.v1.CourseChapterStats.quickstarter_variations = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 quickstarter_variations = 3;

### Evidence

- **SRC-0316** `research/proto/chesscom/courses_common/v1/course_chapter_stats.proto` — [preserved redacted evidence](../evidence/text/4641142454a7008c3c5b1c72b8c9e47a004ea12ce4ae9efc63572d227a9827cb.proto)
  Character offset 242.

```text
Stats {
  optional int32 trainable_variations = 1;
  optional int32 informational_variations = 2;
  optional int32 quickstarter_variations = 3;
  optional int32 alternative_variations = 4;
  optional int32 puzzles = 5;
  optional float average_training_depth = 6;
  optional int32 paid_video_minutes = 7;
}

```

**Source references:** SRC-0316, SRC-1287  
**URL references:** None independently associated  
**Related findings:** FND-02372, FND-02373, FND-02374

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02376"></a>
## FND-02376: chesscom.courses_common.v1.CourseChapterStats.alternative_variations = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 alternative_variations = 4;

### Evidence

- **SRC-0316** `research/proto/chesscom/courses_common/v1/course_chapter_stats.proto` — [preserved redacted evidence](../evidence/text/4641142454a7008c3c5b1c72b8c9e47a004ea12ce4ae9efc63572d227a9827cb.proto)
  Character offset 288.

```text
= 1;
  optional int32 informational_variations = 2;
  optional int32 quickstarter_variations = 3;
  optional int32 alternative_variations = 4;
  optional int32 puzzles = 5;
  optional float average_training_depth = 6;
  optional int32 paid_video_minutes = 7;
}

```

**Source references:** SRC-0316, SRC-1287  
**URL references:** None independently associated  
**Related findings:** FND-02372, FND-02373, FND-02374

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02377"></a>
## FND-02377: chesscom.courses_common.v1.CourseChapterStats.puzzles = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 puzzles = 5;

### Evidence

- **SRC-0316** `research/proto/chesscom/courses_common/v1/course_chapter_stats.proto` — [preserved redacted evidence](../evidence/text/4641142454a7008c3c5b1c72b8c9e47a004ea12ce4ae9efc63572d227a9827cb.proto)
  Character offset 333.

```text
s = 2;
  optional int32 quickstarter_variations = 3;
  optional int32 alternative_variations = 4;
  optional int32 puzzles = 5;
  optional float average_training_depth = 6;
  optional int32 paid_video_minutes = 7;
}

```

**Source references:** SRC-0316, SRC-1287  
**URL references:** None independently associated  
**Related findings:** FND-02372, FND-02373, FND-02374

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02378"></a>
## FND-02378: chesscom.courses_common.v1.CourseChapterStats.average_training_depth = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float average_training_depth = 6;

### Evidence

- **SRC-0316** `research/proto/chesscom/courses_common/v1/course_chapter_stats.proto` — [preserved redacted evidence](../evidence/text/4641142454a7008c3c5b1c72b8c9e47a004ea12ce4ae9efc63572d227a9827cb.proto)
  Character offset 363.

```text
tarter_variations = 3;
  optional int32 alternative_variations = 4;
  optional int32 puzzles = 5;
  optional float average_training_depth = 6;
  optional int32 paid_video_minutes = 7;
}

```

**Source references:** SRC-0316, SRC-1287  
**URL references:** None independently associated  
**Related findings:** FND-02372, FND-02373, FND-02374

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02379"></a>
## FND-02379: chesscom.courses_common.v1.CourseChapterStats.paid_video_minutes = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 paid_video_minutes = 7;

### Evidence

- **SRC-0316** `research/proto/chesscom/courses_common/v1/course_chapter_stats.proto` — [preserved redacted evidence](../evidence/text/4641142454a7008c3c5b1c72b8c9e47a004ea12ce4ae9efc63572d227a9827cb.proto)
  Character offset 408.

```text
native_variations = 4;
  optional int32 puzzles = 5;
  optional float average_training_depth = 6;
  optional int32 paid_video_minutes = 7;
}

```

**Source references:** SRC-0316, SRC-1287  
**URL references:** None independently associated  
**Related findings:** FND-02372, FND-02373, FND-02374

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02380"></a>
## FND-02380: enum declaration: chesscom.courses_common.v1.CourseCoachAvatar

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseCoachAvatar {

### Evidence

- **SRC-0317** `research/proto/chesscom/courses_common/v1/course_coach_avatar.proto` — [preserved redacted evidence](../evidence/text/89f5dd3b2d7f7649db829b67064f57ae32f076baca30e10d4160895f0d24c68a.proto)
  Character offset 120.

```text
courses_common/v1/course_coach_avatar.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum CourseCoachAvatar {
  COURSE_COACH_AVATAR_UNSPECIFIED = 0;
  COURSE_COACH_AVATAR_DAVID = 1;
  COURSE_COACH_AVATAR_MAE = 2;
  COURSE_COACH_AVATAR_DANTE = 3;
  COURSE_COACH_AVATAR_NADIA = 4;
}

```

**Source references:** SRC-0317, SRC-1288  
**URL references:** None independently associated  
**Related findings:** FND-02381, FND-02382

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02381"></a>
## FND-02381: chesscom.courses_common.v1.CourseCoachAvatar.COURSE_COACH_AVATAR_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_COACH_AVATAR_UNSPECIFIED = 0;

### Evidence

- **SRC-0317** `research/proto/chesscom/courses_common/v1/course_coach_avatar.proto` — [preserved redacted evidence](../evidence/text/89f5dd3b2d7f7649db829b67064f57ae32f076baca30e10d4160895f0d24c68a.proto)
  Character offset 147.

```text
ach_avatar.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum CourseCoachAvatar {
  COURSE_COACH_AVATAR_UNSPECIFIED = 0;
  COURSE_COACH_AVATAR_DAVID = 1;
  COURSE_COACH_AVATAR_MAE = 2;
  COURSE_COACH_AVATAR_DANTE = 3;
  COURSE_COACH_AVATAR_NADIA = 4;
}

```

**Source references:** SRC-0317, SRC-1288  
**URL references:** None independently associated  
**Related findings:** FND-02380, FND-02382

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02382"></a>
## FND-02382: chesscom.courses_common.v1.CourseCoachAvatar.COURSE_COACH_AVATAR_DAVID = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_COACH_AVATAR_DAVID = 1;

### Evidence

- **SRC-0317** `research/proto/chesscom/courses_common/v1/course_coach_avatar.proto` — [preserved redacted evidence](../evidence/text/89f5dd3b2d7f7649db829b67064f57ae32f076baca30e10d4160895f0d24c68a.proto)
  Character offset 186.

```text
kage chesscom.courses_common.v1;

enum CourseCoachAvatar {
  COURSE_COACH_AVATAR_UNSPECIFIED = 0;
  COURSE_COACH_AVATAR_DAVID = 1;
  COURSE_COACH_AVATAR_MAE = 2;
  COURSE_COACH_AVATAR_DANTE = 3;
  COURSE_COACH_AVATAR_NADIA = 4;
}

```

**Source references:** SRC-0317, SRC-1288  
**URL references:** None independently associated  
**Related findings:** FND-02380, FND-02381

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02383"></a>
## FND-02383: chesscom.courses_common.v1.CourseCoachAvatar.COURSE_COACH_AVATAR_MAE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_COACH_AVATAR_MAE = 2;

### Evidence

- **SRC-0317** `research/proto/chesscom/courses_common/v1/course_coach_avatar.proto` — [preserved redacted evidence](../evidence/text/89f5dd3b2d7f7649db829b67064f57ae32f076baca30e10d4160895f0d24c68a.proto)
  Character offset 219.

```text

enum CourseCoachAvatar {
  COURSE_COACH_AVATAR_UNSPECIFIED = 0;
  COURSE_COACH_AVATAR_DAVID = 1;
  COURSE_COACH_AVATAR_MAE = 2;
  COURSE_COACH_AVATAR_DANTE = 3;
  COURSE_COACH_AVATAR_NADIA = 4;
}

```

**Source references:** SRC-0317, SRC-1288  
**URL references:** None independently associated  
**Related findings:** FND-02380, FND-02381, FND-02382

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02384"></a>
## FND-02384: chesscom.courses_common.v1.CourseCoachAvatar.COURSE_COACH_AVATAR_DANTE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_COACH_AVATAR_DANTE = 3;

### Evidence

- **SRC-0317** `research/proto/chesscom/courses_common/v1/course_coach_avatar.proto` — [preserved redacted evidence](../evidence/text/89f5dd3b2d7f7649db829b67064f57ae32f076baca30e10d4160895f0d24c68a.proto)
  Character offset 250.

```text
RSE_COACH_AVATAR_UNSPECIFIED = 0;
  COURSE_COACH_AVATAR_DAVID = 1;
  COURSE_COACH_AVATAR_MAE = 2;
  COURSE_COACH_AVATAR_DANTE = 3;
  COURSE_COACH_AVATAR_NADIA = 4;
}

```

**Source references:** SRC-0317, SRC-1288  
**URL references:** None independently associated  
**Related findings:** FND-02380, FND-02381, FND-02382

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02385"></a>
## FND-02385: chesscom.courses_common.v1.CourseCoachAvatar.COURSE_COACH_AVATAR_NADIA = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_COACH_AVATAR_NADIA = 4;

### Evidence

- **SRC-0317** `research/proto/chesscom/courses_common/v1/course_coach_avatar.proto` — [preserved redacted evidence](../evidence/text/89f5dd3b2d7f7649db829b67064f57ae32f076baca30e10d4160895f0d24c68a.proto)
  Character offset 283.

```text

  COURSE_COACH_AVATAR_DAVID = 1;
  COURSE_COACH_AVATAR_MAE = 2;
  COURSE_COACH_AVATAR_DANTE = 3;
  COURSE_COACH_AVATAR_NADIA = 4;
}

```

**Source references:** SRC-0317, SRC-1288  
**URL references:** None independently associated  
**Related findings:** FND-02380, FND-02381, FND-02382

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02386"></a>
## FND-02386: enum declaration: chesscom.courses_common.v1.CourseDrawingArrowType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseDrawingArrowType {

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 116.

```text
com/courses_common/v1/course_drawings.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum CourseDrawingArrowType {
  COURSE_DRAWING_ARROW_TYPE_UNSPECIFIED = 0;
  COURSE_DRAWING_ARROW_TYPE_PRIMARY = 1;
  COURSE_DRAWING_ARROW_TYPE_SECONDARY = 2;
  COURSE_DRAWING_ARROW_TYPE_TERTIARY = 3;
  COURSE_DRAWING_ARROW_TYPE_QUATERNARY = 4;
}

enum CourseDrawingSquareType {
  COURSE_DRAWING_SQUARE_TYPE_UNSPECIFIED 
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02387, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02387"></a>
## FND-02387: chesscom.courses_common.v1.CourseDrawingArrowType.COURSE_DRAWING_ARROW_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_DRAWING_ARROW_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 148.

```text
wings.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum CourseDrawingArrowType {
  COURSE_DRAWING_ARROW_TYPE_UNSPECIFIED = 0;
  COURSE_DRAWING_ARROW_TYPE_PRIMARY = 1;
  COURSE_DRAWING_ARROW_TYPE_SECONDARY = 2;
  COURSE_DRAWING_ARROW_TYPE_TERTIARY = 3;
  COURSE_DRAWING_ARROW_TYPE_QUATERNARY = 4;
}

enum CourseDrawingSquareType {
  COURSE_DRAWING_SQUARE_TYPE_UNSPECIFIED = 0;
  COURSE_DRAWING_SQUARE_TYP
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02388"></a>
## FND-02388: chesscom.courses_common.v1.CourseDrawingArrowType.COURSE_DRAWING_ARROW_TYPE_PRIMARY = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_DRAWING_ARROW_TYPE_PRIMARY = 1;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 193.

```text
om.courses_common.v1;

enum CourseDrawingArrowType {
  COURSE_DRAWING_ARROW_TYPE_UNSPECIFIED = 0;
  COURSE_DRAWING_ARROW_TYPE_PRIMARY = 1;
  COURSE_DRAWING_ARROW_TYPE_SECONDARY = 2;
  COURSE_DRAWING_ARROW_TYPE_TERTIARY = 3;
  COURSE_DRAWING_ARROW_TYPE_QUATERNARY = 4;
}

enum CourseDrawingSquareType {
  COURSE_DRAWING_SQUARE_TYPE_UNSPECIFIED = 0;
  COURSE_DRAWING_SQUARE_TYPE_PRIMARY = 1;
  COURSE_DRAWING_SQUARE_TYPE_S
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02389"></a>
## FND-02389: chesscom.courses_common.v1.CourseDrawingArrowType.COURSE_DRAWING_ARROW_TYPE_SECONDARY = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_DRAWING_ARROW_TYPE_SECONDARY = 2;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 234.

```text
ArrowType {
  COURSE_DRAWING_ARROW_TYPE_UNSPECIFIED = 0;
  COURSE_DRAWING_ARROW_TYPE_PRIMARY = 1;
  COURSE_DRAWING_ARROW_TYPE_SECONDARY = 2;
  COURSE_DRAWING_ARROW_TYPE_TERTIARY = 3;
  COURSE_DRAWING_ARROW_TYPE_QUATERNARY = 4;
}

enum CourseDrawingSquareType {
  COURSE_DRAWING_SQUARE_TYPE_UNSPECIFIED = 0;
  COURSE_DRAWING_SQUARE_TYPE_PRIMARY = 1;
  COURSE_DRAWING_SQUARE_TYPE_SECONDARY = 2;
  COURSE_DRAWING_SQUARE_TYP
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02390"></a>
## FND-02390: chesscom.courses_common.v1.CourseDrawingArrowType.COURSE_DRAWING_ARROW_TYPE_TERTIARY = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_DRAWING_ARROW_TYPE_TERTIARY = 3;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 277.

```text
PECIFIED = 0;
  COURSE_DRAWING_ARROW_TYPE_PRIMARY = 1;
  COURSE_DRAWING_ARROW_TYPE_SECONDARY = 2;
  COURSE_DRAWING_ARROW_TYPE_TERTIARY = 3;
  COURSE_DRAWING_ARROW_TYPE_QUATERNARY = 4;
}

enum CourseDrawingSquareType {
  COURSE_DRAWING_SQUARE_TYPE_UNSPECIFIED = 0;
  COURSE_DRAWING_SQUARE_TYPE_PRIMARY = 1;
  COURSE_DRAWING_SQUARE_TYPE_SECONDARY = 2;
  COURSE_DRAWING_SQUARE_TYPE_TERTIARY = 3;
  COURSE_DRAWING_SQUARE_TYP
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02391"></a>
## FND-02391: chesscom.courses_common.v1.CourseDrawingArrowType.COURSE_DRAWING_ARROW_TYPE_QUATERNARY = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_DRAWING_ARROW_TYPE_QUATERNARY = 4;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 319.

```text
PRIMARY = 1;
  COURSE_DRAWING_ARROW_TYPE_SECONDARY = 2;
  COURSE_DRAWING_ARROW_TYPE_TERTIARY = 3;
  COURSE_DRAWING_ARROW_TYPE_QUATERNARY = 4;
}

enum CourseDrawingSquareType {
  COURSE_DRAWING_SQUARE_TYPE_UNSPECIFIED = 0;
  COURSE_DRAWING_SQUARE_TYPE_PRIMARY = 1;
  COURSE_DRAWING_SQUARE_TYPE_SECONDARY = 2;
  COURSE_DRAWING_SQUARE_TYPE_TERTIARY = 3;
  COURSE_DRAWING_SQUARE_TYPE_QUATERNARY = 4;
}

message CourseDrawing
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02392"></a>
## FND-02392: enum declaration: chesscom.courses_common.v1.CourseDrawingSquareType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseDrawingSquareType {

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 364.

```text
NDARY = 2;
  COURSE_DRAWING_ARROW_TYPE_TERTIARY = 3;
  COURSE_DRAWING_ARROW_TYPE_QUATERNARY = 4;
}

enum CourseDrawingSquareType {
  COURSE_DRAWING_SQUARE_TYPE_UNSPECIFIED = 0;
  COURSE_DRAWING_SQUARE_TYPE_PRIMARY = 1;
  COURSE_DRAWING_SQUARE_TYPE_SECONDARY = 2;
  COURSE_DRAWING_SQUARE_TYPE_TERTIARY = 3;
  COURSE_DRAWING_SQUARE_TYPE_QUATERNARY = 4;
}

message CourseDrawingArrow {
  optional .chesscom.chess.v1.Square 
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02393"></a>
## FND-02393: chesscom.courses_common.v1.CourseDrawingSquareType.COURSE_DRAWING_SQUARE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_DRAWING_SQUARE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 397.

```text
_TYPE_TERTIARY = 3;
  COURSE_DRAWING_ARROW_TYPE_QUATERNARY = 4;
}

enum CourseDrawingSquareType {
  COURSE_DRAWING_SQUARE_TYPE_UNSPECIFIED = 0;
  COURSE_DRAWING_SQUARE_TYPE_PRIMARY = 1;
  COURSE_DRAWING_SQUARE_TYPE_SECONDARY = 2;
  COURSE_DRAWING_SQUARE_TYPE_TERTIARY = 3;
  COURSE_DRAWING_SQUARE_TYPE_QUATERNARY = 4;
}

message CourseDrawingArrow {
  optional .chesscom.chess.v1.Square square_from = 1;
  optional .ches
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02394"></a>
## FND-02394: chesscom.courses_common.v1.CourseDrawingSquareType.COURSE_DRAWING_SQUARE_TYPE_PRIMARY = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_DRAWING_SQUARE_TYPE_PRIMARY = 1;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 443.

```text
E_QUATERNARY = 4;
}

enum CourseDrawingSquareType {
  COURSE_DRAWING_SQUARE_TYPE_UNSPECIFIED = 0;
  COURSE_DRAWING_SQUARE_TYPE_PRIMARY = 1;
  COURSE_DRAWING_SQUARE_TYPE_SECONDARY = 2;
  COURSE_DRAWING_SQUARE_TYPE_TERTIARY = 3;
  COURSE_DRAWING_SQUARE_TYPE_QUATERNARY = 4;
}

message CourseDrawingArrow {
  optional .chesscom.chess.v1.Square square_from = 1;
  optional .chesscom.chess.v1.Square square_to = 2;
  optional
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02395"></a>
## FND-02395: chesscom.courses_common.v1.CourseDrawingSquareType.COURSE_DRAWING_SQUARE_TYPE_SECONDARY = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_DRAWING_SQUARE_TYPE_SECONDARY = 2;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 485.

```text
areType {
  COURSE_DRAWING_SQUARE_TYPE_UNSPECIFIED = 0;
  COURSE_DRAWING_SQUARE_TYPE_PRIMARY = 1;
  COURSE_DRAWING_SQUARE_TYPE_SECONDARY = 2;
  COURSE_DRAWING_SQUARE_TYPE_TERTIARY = 3;
  COURSE_DRAWING_SQUARE_TYPE_QUATERNARY = 4;
}

message CourseDrawingArrow {
  optional .chesscom.chess.v1.Square square_from = 1;
  optional .chesscom.chess.v1.Square square_to = 2;
  optional .chesscom.courses_common.v1.CourseDrawing
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02396"></a>
## FND-02396: chesscom.courses_common.v1.CourseDrawingSquareType.COURSE_DRAWING_SQUARE_TYPE_TERTIARY = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_DRAWING_SQUARE_TYPE_TERTIARY = 3;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 529.

```text
CIFIED = 0;
  COURSE_DRAWING_SQUARE_TYPE_PRIMARY = 1;
  COURSE_DRAWING_SQUARE_TYPE_SECONDARY = 2;
  COURSE_DRAWING_SQUARE_TYPE_TERTIARY = 3;
  COURSE_DRAWING_SQUARE_TYPE_QUATERNARY = 4;
}

message CourseDrawingArrow {
  optional .chesscom.chess.v1.Square square_from = 1;
  optional .chesscom.chess.v1.Square square_to = 2;
  optional .chesscom.courses_common.v1.CourseDrawingArrowType type = 3;
}

message CourseDrawing
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02397"></a>
## FND-02397: chesscom.courses_common.v1.CourseDrawingSquareType.COURSE_DRAWING_SQUARE_TYPE_QUATERNARY = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_DRAWING_SQUARE_TYPE_QUATERNARY = 4;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 572.

```text
IMARY = 1;
  COURSE_DRAWING_SQUARE_TYPE_SECONDARY = 2;
  COURSE_DRAWING_SQUARE_TYPE_TERTIARY = 3;
  COURSE_DRAWING_SQUARE_TYPE_QUATERNARY = 4;
}

message CourseDrawingArrow {
  optional .chesscom.chess.v1.Square square_from = 1;
  optional .chesscom.chess.v1.Square square_to = 2;
  optional .chesscom.courses_common.v1.CourseDrawingArrowType type = 3;
}

message CourseDrawingSquare {
  optional .chesscom.chess.v1.Squa
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02398"></a>
## FND-02398: message declaration: chesscom.courses_common.v1.CourseDrawingArrow

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseDrawingArrow {

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 618.

```text
ARY = 2;
  COURSE_DRAWING_SQUARE_TYPE_TERTIARY = 3;
  COURSE_DRAWING_SQUARE_TYPE_QUATERNARY = 4;
}

message CourseDrawingArrow {
  optional .chesscom.chess.v1.Square square_from = 1;
  optional .chesscom.chess.v1.Square square_to = 2;
  optional .chesscom.courses_common.v1.CourseDrawingArrowType type = 3;
}

message CourseDrawingSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.courses_co
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02399"></a>
## FND-02399: chesscom.courses_common.v1.CourseDrawingArrow.square_from = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square square_from = 1;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 649.

```text
E_TYPE_TERTIARY = 3;
  COURSE_DRAWING_SQUARE_TYPE_QUATERNARY = 4;
}

message CourseDrawingArrow {
  optional .chesscom.chess.v1.Square square_from = 1;
  optional .chesscom.chess.v1.Square square_to = 2;
  optional .chesscom.courses_common.v1.CourseDrawingArrowType type = 3;
}

message CourseDrawingSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.courses_common.v1.CourseDrawingSquareType
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02400"></a>
## FND-02400: chesscom.courses_common.v1.CourseDrawingArrow.square_to = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square square_to = 2;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 703.

```text
ERNARY = 4;
}

message CourseDrawingArrow {
  optional .chesscom.chess.v1.Square square_from = 1;
  optional .chesscom.chess.v1.Square square_to = 2;
  optional .chesscom.courses_common.v1.CourseDrawingArrowType type = 3;
}

message CourseDrawingSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.courses_common.v1.CourseDrawingSquareType type = 2;
}

message CourseSubvariationDrawing {
  op
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02401"></a>
## FND-02401: chesscom.courses_common.v1.CourseDrawingArrow.type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseDrawingArrowType type = 3;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 755.

```text
al .chesscom.chess.v1.Square square_from = 1;
  optional .chesscom.chess.v1.Square square_to = 2;
  optional .chesscom.courses_common.v1.CourseDrawingArrowType type = 3;
}

message CourseDrawingSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.courses_common.v1.CourseDrawingSquareType type = 2;
}

message CourseSubvariationDrawing {
  optional string branch_fen = 1;
  optional string bran
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02402"></a>
## FND-02402: message declaration: chesscom.courses_common.v1.CourseDrawingSquare

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseDrawingSquare {

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 828.

```text
v1.Square square_to = 2;
  optional .chesscom.courses_common.v1.CourseDrawingArrowType type = 3;
}

message CourseDrawingSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.courses_common.v1.CourseDrawingSquareType type = 2;
}

message CourseSubvariationDrawing {
  optional string branch_fen = 1;
  optional string branch_move = 2;
  optional string position_fen = 3;
  repeated .chesscom.cou
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02403"></a>
## FND-02403: chesscom.courses_common.v1.CourseDrawingSquare.square = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Square square = 1;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 860.

```text
nal .chesscom.courses_common.v1.CourseDrawingArrowType type = 3;
}

message CourseDrawingSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.courses_common.v1.CourseDrawingSquareType type = 2;
}

message CourseSubvariationDrawing {
  optional string branch_fen = 1;
  optional string branch_move = 2;
  optional string position_fen = 3;
  repeated .chesscom.courses_common.v1.CourseDrawingSqua
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02404"></a>
## FND-02404: chesscom.courses_common.v1.CourseDrawingSquare.type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseDrawingSquareType type = 2;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 909.

```text
wType type = 3;
}

message CourseDrawingSquare {
  optional .chesscom.chess.v1.Square square = 1;
  optional .chesscom.courses_common.v1.CourseDrawingSquareType type = 2;
}

message CourseSubvariationDrawing {
  optional string branch_fen = 1;
  optional string branch_move = 2;
  optional string position_fen = 3;
  repeated .chesscom.courses_common.v1.CourseDrawingSquare drawing_squares = 4;
  repeated .chesscom.cour
```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02405"></a>
## FND-02405: message declaration: chesscom.courses_common.v1.CourseSubvariationDrawing

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseSubvariationDrawing {

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 983.

```text
s.v1.Square square = 1;
  optional .chesscom.courses_common.v1.CourseDrawingSquareType type = 2;
}

message CourseSubvariationDrawing {
  optional string branch_fen = 1;
  optional string branch_move = 2;
  optional string position_fen = 3;
  repeated .chesscom.courses_common.v1.CourseDrawingSquare drawing_squares = 4;
  repeated .chesscom.courses_common.v1.CourseDrawingArrow drawing_arrows = 5;
}

```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02406"></a>
## FND-02406: chesscom.courses_common.v1.CourseSubvariationDrawing.branch_fen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string branch_fen = 1;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 1021.

```text
esscom.courses_common.v1.CourseDrawingSquareType type = 2;
}

message CourseSubvariationDrawing {
  optional string branch_fen = 1;
  optional string branch_move = 2;
  optional string position_fen = 3;
  repeated .chesscom.courses_common.v1.CourseDrawingSquare drawing_squares = 4;
  repeated .chesscom.courses_common.v1.CourseDrawingArrow drawing_arrows = 5;
}

```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02407"></a>
## FND-02407: chesscom.courses_common.v1.CourseSubvariationDrawing.branch_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string branch_move = 2;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 1055.

```text
wingSquareType type = 2;
}

message CourseSubvariationDrawing {
  optional string branch_fen = 1;
  optional string branch_move = 2;
  optional string position_fen = 3;
  repeated .chesscom.courses_common.v1.CourseDrawingSquare drawing_squares = 4;
  repeated .chesscom.courses_common.v1.CourseDrawingArrow drawing_arrows = 5;
}

```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02408"></a>
## FND-02408: chesscom.courses_common.v1.CourseSubvariationDrawing.position_fen = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string position_fen = 3;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 1090.

```text
 CourseSubvariationDrawing {
  optional string branch_fen = 1;
  optional string branch_move = 2;
  optional string position_fen = 3;
  repeated .chesscom.courses_common.v1.CourseDrawingSquare drawing_squares = 4;
  repeated .chesscom.courses_common.v1.CourseDrawingArrow drawing_arrows = 5;
}

```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02409"></a>
## FND-02409: chesscom.courses_common.v1.CourseSubvariationDrawing.drawing_squares = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses_common.v1.CourseDrawingSquare drawing_squares = 4;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 1126.

```text
nal string branch_fen = 1;
  optional string branch_move = 2;
  optional string position_fen = 3;
  repeated .chesscom.courses_common.v1.CourseDrawingSquare drawing_squares = 4;
  repeated .chesscom.courses_common.v1.CourseDrawingArrow drawing_arrows = 5;
}

```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02410"></a>
## FND-02410: chesscom.courses_common.v1.CourseSubvariationDrawing.drawing_arrows = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses_common.v1.CourseDrawingArrow drawing_arrows = 5;

### Evidence

- **SRC-0318** `research/proto/chesscom/courses_common/v1/course_drawings.proto` — [preserved redacted evidence](../evidence/text/d753549edbca4050ceb3ddc8e7cccf910ebcc18004f2c383e7e394d2f0c26186.proto)
  Character offset 1206.

```text
position_fen = 3;
  repeated .chesscom.courses_common.v1.CourseDrawingSquare drawing_squares = 4;
  repeated .chesscom.courses_common.v1.CourseDrawingArrow drawing_arrows = 5;
}

```

**Source references:** SRC-0318, SRC-1289  
**URL references:** None independently associated  
**Related findings:** FND-02386, FND-02387, FND-02388

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02411"></a>
## FND-02411: enum declaration: chesscom.courses_common.v1.CourseGameAspectType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseGameAspectType {

### Evidence

- **SRC-0319** `research/proto/chesscom/courses_common/v1/course_game_aspect.proto` — [preserved redacted evidence](../evidence/text/a0aa119b9ce4b72e7a56481ef682e47fcf451978c8ddde775100ea36a85846e2.proto)
  Character offset 119.

```text
/courses_common/v1/course_game_aspect.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum CourseGameAspectType {
  COURSE_GAME_ASPECT_TYPE_UNSPECIFIED = 0;
  COURSE_GAME_ASPECT_TYPE_OPENING = 1;
  COURSE_GAME_ASPECT_TYPE_TACTICS = 2;
  COURSE_GAME_ASPECT_TYPE_STRATEGY = 3;
  COURSE_GAME_ASPECT_TYPE_ENDGAME = 4;
}

message CourseGameAspect {
  oneof _secondary_game_aspect {
  .chesscom.courses_common.v1
```

**Source references:** SRC-0319, SRC-1290  
**URL references:** None independently associated  
**Related findings:** FND-02412, FND-02413

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02412"></a>
## FND-02412: chesscom.courses_common.v1.CourseGameAspectType.COURSE_GAME_ASPECT_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_GAME_ASPECT_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0319** `research/proto/chesscom/courses_common/v1/course_game_aspect.proto` — [preserved redacted evidence](../evidence/text/a0aa119b9ce4b72e7a56481ef682e47fcf451978c8ddde775100ea36a85846e2.proto)
  Character offset 149.

```text
_aspect.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum CourseGameAspectType {
  COURSE_GAME_ASPECT_TYPE_UNSPECIFIED = 0;
  COURSE_GAME_ASPECT_TYPE_OPENING = 1;
  COURSE_GAME_ASPECT_TYPE_TACTICS = 2;
  COURSE_GAME_ASPECT_TYPE_STRATEGY = 3;
  COURSE_GAME_ASPECT_TYPE_ENDGAME = 4;
}

message CourseGameAspect {
  oneof _secondary_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspectType secondar
```

**Source references:** SRC-0319, SRC-1290  
**URL references:** None independently associated  
**Related findings:** FND-02411, FND-02413

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02413"></a>
## FND-02413: chesscom.courses_common.v1.CourseGameAspectType.COURSE_GAME_ASPECT_TYPE_OPENING = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_GAME_ASPECT_TYPE_OPENING = 1;

### Evidence

- **SRC-0319** `research/proto/chesscom/courses_common/v1/course_game_aspect.proto` — [preserved redacted evidence](../evidence/text/a0aa119b9ce4b72e7a56481ef682e47fcf451978c8ddde775100ea36a85846e2.proto)
  Character offset 192.

```text
esscom.courses_common.v1;

enum CourseGameAspectType {
  COURSE_GAME_ASPECT_TYPE_UNSPECIFIED = 0;
  COURSE_GAME_ASPECT_TYPE_OPENING = 1;
  COURSE_GAME_ASPECT_TYPE_TACTICS = 2;
  COURSE_GAME_ASPECT_TYPE_STRATEGY = 3;
  COURSE_GAME_ASPECT_TYPE_ENDGAME = 4;
}

message CourseGameAspect {
  oneof _secondary_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspectType secondary_game_aspect = 2;
  }
  optional .chesscom
```

**Source references:** SRC-0319, SRC-1290  
**URL references:** None independently associated  
**Related findings:** FND-02411, FND-02412

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02414"></a>
## FND-02414: chesscom.courses_common.v1.CourseGameAspectType.COURSE_GAME_ASPECT_TYPE_TACTICS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_GAME_ASPECT_TYPE_TACTICS = 2;

### Evidence

- **SRC-0319** `research/proto/chesscom/courses_common/v1/course_game_aspect.proto` — [preserved redacted evidence](../evidence/text/a0aa119b9ce4b72e7a56481ef682e47fcf451978c8ddde775100ea36a85846e2.proto)
  Character offset 231.

```text
ameAspectType {
  COURSE_GAME_ASPECT_TYPE_UNSPECIFIED = 0;
  COURSE_GAME_ASPECT_TYPE_OPENING = 1;
  COURSE_GAME_ASPECT_TYPE_TACTICS = 2;
  COURSE_GAME_ASPECT_TYPE_STRATEGY = 3;
  COURSE_GAME_ASPECT_TYPE_ENDGAME = 4;
}

message CourseGameAspect {
  oneof _secondary_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspectType secondary_game_aspect = 2;
  }
  optional .chesscom.courses_common.v1.CourseGameAspectType
```

**Source references:** SRC-0319, SRC-1290  
**URL references:** None independently associated  
**Related findings:** FND-02411, FND-02412, FND-02413

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02415"></a>
## FND-02415: chesscom.courses_common.v1.CourseGameAspectType.COURSE_GAME_ASPECT_TYPE_STRATEGY = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_GAME_ASPECT_TYPE_STRATEGY = 3;

### Evidence

- **SRC-0319** `research/proto/chesscom/courses_common/v1/course_game_aspect.proto` — [preserved redacted evidence](../evidence/text/a0aa119b9ce4b72e7a56481ef682e47fcf451978c8ddde775100ea36a85846e2.proto)
  Character offset 270.

```text
PE_UNSPECIFIED = 0;
  COURSE_GAME_ASPECT_TYPE_OPENING = 1;
  COURSE_GAME_ASPECT_TYPE_TACTICS = 2;
  COURSE_GAME_ASPECT_TYPE_STRATEGY = 3;
  COURSE_GAME_ASPECT_TYPE_ENDGAME = 4;
}

message CourseGameAspect {
  oneof _secondary_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspectType secondary_game_aspect = 2;
  }
  optional .chesscom.courses_common.v1.CourseGameAspectType main_game_aspect = 1;
}

```

**Source references:** SRC-0319, SRC-1290  
**URL references:** None independently associated  
**Related findings:** FND-02411, FND-02412, FND-02413

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02416"></a>
## FND-02416: chesscom.courses_common.v1.CourseGameAspectType.COURSE_GAME_ASPECT_TYPE_ENDGAME = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_GAME_ASPECT_TYPE_ENDGAME = 4;

### Evidence

- **SRC-0319** `research/proto/chesscom/courses_common/v1/course_game_aspect.proto` — [preserved redacted evidence](../evidence/text/a0aa119b9ce4b72e7a56481ef682e47fcf451978c8ddde775100ea36a85846e2.proto)
  Character offset 310.

```text
_TYPE_OPENING = 1;
  COURSE_GAME_ASPECT_TYPE_TACTICS = 2;
  COURSE_GAME_ASPECT_TYPE_STRATEGY = 3;
  COURSE_GAME_ASPECT_TYPE_ENDGAME = 4;
}

message CourseGameAspect {
  oneof _secondary_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspectType secondary_game_aspect = 2;
  }
  optional .chesscom.courses_common.v1.CourseGameAspectType main_game_aspect = 1;
}

```

**Source references:** SRC-0319, SRC-1290  
**URL references:** None independently associated  
**Related findings:** FND-02411, FND-02412, FND-02413

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02417"></a>
## FND-02417: message declaration: chesscom.courses_common.v1.CourseGameAspect

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseGameAspect {

### Evidence

- **SRC-0319** `research/proto/chesscom/courses_common/v1/course_game_aspect.proto` — [preserved redacted evidence](../evidence/text/a0aa119b9ce4b72e7a56481ef682e47fcf451978c8ddde775100ea36a85846e2.proto)
  Character offset 350.

```text
TYPE_TACTICS = 2;
  COURSE_GAME_ASPECT_TYPE_STRATEGY = 3;
  COURSE_GAME_ASPECT_TYPE_ENDGAME = 4;
}

message CourseGameAspect {
  oneof _secondary_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspectType secondary_game_aspect = 2;
  }
  optional .chesscom.courses_common.v1.CourseGameAspectType main_game_aspect = 1;
}

```

**Source references:** SRC-0319, SRC-1290  
**URL references:** None independently associated  
**Related findings:** FND-02411, FND-02412, FND-02413

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02418"></a>
## FND-02418: oneof declaration: chesscom.courses_common.v1.CourseGameAspect._secondary_game_aspect

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _secondary_game_aspect {

### Evidence

- **SRC-0319** `research/proto/chesscom/courses_common/v1/course_game_aspect.proto` — [preserved redacted evidence](../evidence/text/a0aa119b9ce4b72e7a56481ef682e47fcf451978c8ddde775100ea36a85846e2.proto)
  Character offset 379.

```text
ME_ASPECT_TYPE_STRATEGY = 3;
  COURSE_GAME_ASPECT_TYPE_ENDGAME = 4;
}

message CourseGameAspect {
  oneof _secondary_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspectType secondary_game_aspect = 2;
  }
  optional .chesscom.courses_common.v1.CourseGameAspectType main_game_aspect = 1;
}

```

**Source references:** SRC-0319, SRC-1290  
**URL references:** None independently associated  
**Related findings:** FND-02411, FND-02412, FND-02413

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02419"></a>
## FND-02419: chesscom.courses_common.v1.CourseGameAspect.secondary_game_aspect = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses_common.v1.CourseGameAspectType secondary_game_aspect = 2;

### Evidence

- **SRC-0319** `research/proto/chesscom/courses_common/v1/course_game_aspect.proto` — [preserved redacted evidence](../evidence/text/a0aa119b9ce4b72e7a56481ef682e47fcf451978c8ddde775100ea36a85846e2.proto)
  Character offset 412.

```text
URSE_GAME_ASPECT_TYPE_ENDGAME = 4;
}

message CourseGameAspect {
  oneof _secondary_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspectType secondary_game_aspect = 2;
  }
  optional .chesscom.courses_common.v1.CourseGameAspectType main_game_aspect = 1;
}

```

**Source references:** SRC-0319, SRC-1290  
**URL references:** None independently associated  
**Related findings:** FND-02411, FND-02412, FND-02413

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02420"></a>
## FND-02420: chesscom.courses_common.v1.CourseGameAspect.main_game_aspect = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseGameAspectType main_game_aspect = 1;

### Evidence

- **SRC-0319** `research/proto/chesscom/courses_common/v1/course_game_aspect.proto` — [preserved redacted evidence](../evidence/text/a0aa119b9ce4b72e7a56481ef682e47fcf451978c8ddde775100ea36a85846e2.proto)
  Character offset 494.

```text
y_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspectType secondary_game_aspect = 2;
  }
  optional .chesscom.courses_common.v1.CourseGameAspectType main_game_aspect = 1;
}

```

**Source references:** SRC-0319, SRC-1290  
**URL references:** None independently associated  
**Related findings:** FND-02411, FND-02412, FND-02413

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02421"></a>
## FND-02421: message declaration: chesscom.courses_common.v1.CoursePrice

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoursePrice {

### Evidence

- **SRC-0320** `research/proto/chesscom/courses_common/v1/course_price.proto` — [preserved redacted evidence](../evidence/text/bf7db4e7b7d81d25f9187495c4332a10db69dc11f3924fe6f7e0c23190c3b0e3.proto)
  Character offset 113.

```text
esscom/courses_common/v1/course_price.proto
// syntax: proto3

package chesscom.courses_common.v1;

message CoursePrice {
  oneof _discounted {
  .chesscom.api.v1.Money discounted = 3;
  }
  optional .chesscom.api.v1.Money original = 2;
  optional .chesscom.api.v1.Money diamond = 4;
}

```

**Source references:** SRC-0320, SRC-1291  
**URL references:** None independently associated  
**Related findings:** FND-02422, FND-02423

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02422"></a>
## FND-02422: oneof declaration: chesscom.courses_common.v1.CoursePrice._discounted

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _discounted {

### Evidence

- **SRC-0320** `research/proto/chesscom/courses_common/v1/course_price.proto` — [preserved redacted evidence](../evidence/text/bf7db4e7b7d81d25f9187495c4332a10db69dc11f3924fe6f7e0c23190c3b0e3.proto)
  Character offset 137.

```text
/course_price.proto
// syntax: proto3

package chesscom.courses_common.v1;

message CoursePrice {
  oneof _discounted {
  .chesscom.api.v1.Money discounted = 3;
  }
  optional .chesscom.api.v1.Money original = 2;
  optional .chesscom.api.v1.Money diamond = 4;
}

```

**Source references:** SRC-0320, SRC-1291  
**URL references:** None independently associated  
**Related findings:** FND-02421, FND-02423

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02423"></a>
## FND-02423: chesscom.courses_common.v1.CoursePrice.discounted = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.Money discounted = 3;

### Evidence

- **SRC-0320** `research/proto/chesscom/courses_common/v1/course_price.proto` — [preserved redacted evidence](../evidence/text/bf7db4e7b7d81d25f9187495c4332a10db69dc11f3924fe6f7e0c23190c3b0e3.proto)
  Character offset 159.

```text
 syntax: proto3

package chesscom.courses_common.v1;

message CoursePrice {
  oneof _discounted {
  .chesscom.api.v1.Money discounted = 3;
  }
  optional .chesscom.api.v1.Money original = 2;
  optional .chesscom.api.v1.Money diamond = 4;
}

```

**Source references:** SRC-0320, SRC-1291  
**URL references:** None independently associated  
**Related findings:** FND-02421, FND-02422

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02424"></a>
## FND-02424: chesscom.courses_common.v1.CoursePrice.original = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money original = 2;

### Evidence

- **SRC-0320** `research/proto/chesscom/courses_common/v1/course_price.proto` — [preserved redacted evidence](../evidence/text/bf7db4e7b7d81d25f9187495c4332a10db69dc11f3924fe6f7e0c23190c3b0e3.proto)
  Character offset 204.

```text
mon.v1;

message CoursePrice {
  oneof _discounted {
  .chesscom.api.v1.Money discounted = 3;
  }
  optional .chesscom.api.v1.Money original = 2;
  optional .chesscom.api.v1.Money diamond = 4;
}

```

**Source references:** SRC-0320, SRC-1291  
**URL references:** None independently associated  
**Related findings:** FND-02421, FND-02422, FND-02423

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02425"></a>
## FND-02425: chesscom.courses_common.v1.CoursePrice.diamond = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money diamond = 4;

### Evidence

- **SRC-0320** `research/proto/chesscom/courses_common/v1/course_price.proto` — [preserved redacted evidence](../evidence/text/bf7db4e7b7d81d25f9187495c4332a10db69dc11f3924fe6f7e0c23190c3b0e3.proto)
  Character offset 252.

```text
ed {
  .chesscom.api.v1.Money discounted = 3;
  }
  optional .chesscom.api.v1.Money original = 2;
  optional .chesscom.api.v1.Money diamond = 4;
}

```

**Source references:** SRC-0320, SRC-1291  
**URL references:** None independently associated  
**Related findings:** FND-02421, FND-02422, FND-02423

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02426"></a>
## FND-02426: message declaration: chesscom.courses_common.v1.CourseProductReview

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseProductReview {

### Evidence

- **SRC-0321** `research/proto/chesscom/courses_common/v1/course_product_review.proto` — [preserved redacted evidence](../evidence/text/4864a15aa1a4ebc598889d8ec7588dbd99e3645cefb8ac19c2b724a65a3e875d.proto)
  Character offset 122.

```text
urses_common/v1/course_product_review.proto
// syntax: proto3

package chesscom.courses_common.v1;

message CourseProductReview {
  optional string id = 1;
  optional float rating = 2;
  optional string title = 3;
  optional string text = 4;
  optional .chesscom.courses_common.v1.CourseReviewAuthor user = 5;
  optional .google.protobuf.Timestamp published_at = 6;
}

```

**Source references:** SRC-0321, SRC-1292  
**URL references:** None independently associated  
**Related findings:** FND-02427, FND-02428

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02427"></a>
## FND-02427: chesscom.courses_common.v1.CourseProductReview.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0321** `research/proto/chesscom/courses_common/v1/course_product_review.proto` — [preserved redacted evidence](../evidence/text/4864a15aa1a4ebc598889d8ec7588dbd99e3645cefb8ac19c2b724a65a3e875d.proto)
  Character offset 154.

```text
eview.proto
// syntax: proto3

package chesscom.courses_common.v1;

message CourseProductReview {
  optional string id = 1;
  optional float rating = 2;
  optional string title = 3;
  optional string text = 4;
  optional .chesscom.courses_common.v1.CourseReviewAuthor user = 5;
  optional .google.protobuf.Timestamp published_at = 6;
}

```

**Source references:** SRC-0321, SRC-1292  
**URL references:** None independently associated  
**Related findings:** FND-02426, FND-02428

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02428"></a>
## FND-02428: chesscom.courses_common.v1.CourseProductReview.rating = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float rating = 2;

### Evidence

- **SRC-0321** `research/proto/chesscom/courses_common/v1/course_product_review.proto` — [preserved redacted evidence](../evidence/text/4864a15aa1a4ebc598889d8ec7588dbd99e3645cefb8ac19c2b724a65a3e875d.proto)
  Character offset 180.

```text
to3

package chesscom.courses_common.v1;

message CourseProductReview {
  optional string id = 1;
  optional float rating = 2;
  optional string title = 3;
  optional string text = 4;
  optional .chesscom.courses_common.v1.CourseReviewAuthor user = 5;
  optional .google.protobuf.Timestamp published_at = 6;
}

```

**Source references:** SRC-0321, SRC-1292  
**URL references:** None independently associated  
**Related findings:** FND-02426, FND-02427

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02429"></a>
## FND-02429: chesscom.courses_common.v1.CourseProductReview.title = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string title = 3;

### Evidence

- **SRC-0321** `research/proto/chesscom/courses_common/v1/course_product_review.proto` — [preserved redacted evidence](../evidence/text/4864a15aa1a4ebc598889d8ec7588dbd99e3645cefb8ac19c2b724a65a3e875d.proto)
  Character offset 209.

```text
_common.v1;

message CourseProductReview {
  optional string id = 1;
  optional float rating = 2;
  optional string title = 3;
  optional string text = 4;
  optional .chesscom.courses_common.v1.CourseReviewAuthor user = 5;
  optional .google.protobuf.Timestamp published_at = 6;
}

```

**Source references:** SRC-0321, SRC-1292  
**URL references:** None independently associated  
**Related findings:** FND-02426, FND-02427, FND-02428

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02430"></a>
## FND-02430: chesscom.courses_common.v1.CourseProductReview.text = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string text = 4;

### Evidence

- **SRC-0321** `research/proto/chesscom/courses_common/v1/course_product_review.proto` — [preserved redacted evidence](../evidence/text/4864a15aa1a4ebc598889d8ec7588dbd99e3645cefb8ac19c2b724a65a3e875d.proto)
  Character offset 238.

```text
oductReview {
  optional string id = 1;
  optional float rating = 2;
  optional string title = 3;
  optional string text = 4;
  optional .chesscom.courses_common.v1.CourseReviewAuthor user = 5;
  optional .google.protobuf.Timestamp published_at = 6;
}

```

**Source references:** SRC-0321, SRC-1292  
**URL references:** None independently associated  
**Related findings:** FND-02426, FND-02427, FND-02428

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02431"></a>
## FND-02431: chesscom.courses_common.v1.CourseProductReview.user = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseReviewAuthor user = 5;

### Evidence

- **SRC-0321** `research/proto/chesscom/courses_common/v1/course_product_review.proto` — [preserved redacted evidence](../evidence/text/4864a15aa1a4ebc598889d8ec7588dbd99e3645cefb8ac19c2b724a65a3e875d.proto)
  Character offset 266.

```text
ing id = 1;
  optional float rating = 2;
  optional string title = 3;
  optional string text = 4;
  optional .chesscom.courses_common.v1.CourseReviewAuthor user = 5;
  optional .google.protobuf.Timestamp published_at = 6;
}

```

**Source references:** SRC-0321, SRC-1292  
**URL references:** None independently associated  
**Related findings:** FND-02426, FND-02427, FND-02428

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02432"></a>
## FND-02432: chesscom.courses_common.v1.CourseProductReview.published_at = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp published_at = 6;

### Evidence

- **SRC-0321** `research/proto/chesscom/courses_common/v1/course_product_review.proto` — [preserved redacted evidence](../evidence/text/4864a15aa1a4ebc598889d8ec7588dbd99e3645cefb8ac19c2b724a65a3e875d.proto)
  Character offset 334.

```text
;
  optional string text = 4;
  optional .chesscom.courses_common.v1.CourseReviewAuthor user = 5;
  optional .google.protobuf.Timestamp published_at = 6;
}

```

**Source references:** SRC-0321, SRC-1292  
**URL references:** None independently associated  
**Related findings:** FND-02426, FND-02427, FND-02428

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02433"></a>
## FND-02433: message declaration: chesscom.courses_common.v1.CourseRating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseRating {

### Evidence

- **SRC-0322** `research/proto/chesscom/courses_common/v1/course_rating.proto` — [preserved redacted evidence](../evidence/text/a16078ffb84300f13bedac02f07ef0679805b5efed078684a7ff97f337601737.proto)
  Character offset 114.

```text
sscom/courses_common/v1/course_rating.proto
// syntax: proto3

package chesscom.courses_common.v1;

message CourseRating {
  optional float average = 1;
  optional int32 amount = 2;
}

```

**Source references:** SRC-0322, SRC-1293  
**URL references:** None independently associated  
**Related findings:** FND-02434, FND-02435

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02434"></a>
## FND-02434: chesscom.courses_common.v1.CourseRating.average = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float average = 1;

### Evidence

- **SRC-0322** `research/proto/chesscom/courses_common/v1/course_rating.proto` — [preserved redacted evidence](../evidence/text/a16078ffb84300f13bedac02f07ef0679805b5efed078684a7ff97f337601737.proto)
  Character offset 139.

```text
ourse_rating.proto
// syntax: proto3

package chesscom.courses_common.v1;

message CourseRating {
  optional float average = 1;
  optional int32 amount = 2;
}

```

**Source references:** SRC-0322, SRC-1293  
**URL references:** None independently associated  
**Related findings:** FND-02433, FND-02435

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02435"></a>
## FND-02435: chesscom.courses_common.v1.CourseRating.amount = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 amount = 2;

### Evidence

- **SRC-0322** `research/proto/chesscom/courses_common/v1/course_rating.proto` — [preserved redacted evidence](../evidence/text/a16078ffb84300f13bedac02f07ef0679805b5efed078684a7ff97f337601737.proto)
  Character offset 169.

```text
proto3

package chesscom.courses_common.v1;

message CourseRating {
  optional float average = 1;
  optional int32 amount = 2;
}

```

**Source references:** SRC-0322, SRC-1293  
**URL references:** None independently associated  
**Related findings:** FND-02433, FND-02434

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02436"></a>
## FND-02436: enum declaration: chesscom.courses_common.v1.UserSourceType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum UserSourceType {

### Evidence

- **SRC-0323** `research/proto/chesscom/courses_common/v1/course_review_author.proto` — [preserved redacted evidence](../evidence/text/50662a82e3ccf70be2020515c46cd4a1474257591c6c6d1424a94323059aa93e.proto)
  Character offset 121.

```text
ourses_common/v1/course_review_author.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum UserSourceType {
  USER_SOURCE_TYPE_UNSPECIFIED = 0;
  USER_SOURCE_TYPE_CHESSCOM = 1;
  USER_SOURCE_TYPE_CHESSABLE = 2;
}

message CourseReviewAuthor {
  optional .chesscom.courses_common.v1.UserSource source = 1;
  optional string display_name = 2;
  optional .chesscom.courses_common.v1.Picture avatar = 3;
}

mes
```

**Source references:** SRC-0323, SRC-1294  
**URL references:** None independently associated  
**Related findings:** FND-02437, FND-02438

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02437"></a>
## FND-02437: chesscom.courses_common.v1.UserSourceType.USER_SOURCE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_SOURCE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0323** `research/proto/chesscom/courses_common/v1/course_review_author.proto` — [preserved redacted evidence](../evidence/text/50662a82e3ccf70be2020515c46cd4a1474257591c6c6d1424a94323059aa93e.proto)
  Character offset 145.

```text
review_author.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum UserSourceType {
  USER_SOURCE_TYPE_UNSPECIFIED = 0;
  USER_SOURCE_TYPE_CHESSCOM = 1;
  USER_SOURCE_TYPE_CHESSABLE = 2;
}

message CourseReviewAuthor {
  optional .chesscom.courses_common.v1.UserSource source = 1;
  optional string display_name = 2;
  optional .chesscom.courses_common.v1.Picture avatar = 3;
}

message UserSource {
  opti
```

**Source references:** SRC-0323, SRC-1294  
**URL references:** None independently associated  
**Related findings:** FND-02436, FND-02438

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02438"></a>
## FND-02438: chesscom.courses_common.v1.UserSourceType.USER_SOURCE_TYPE_CHESSCOM = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_SOURCE_TYPE_CHESSCOM = 1;

### Evidence

- **SRC-0323** `research/proto/chesscom/courses_common/v1/course_review_author.proto` — [preserved redacted evidence](../evidence/text/50662a82e3ccf70be2020515c46cd4a1474257591c6c6d1424a94323059aa93e.proto)
  Character offset 181.

```text
3

package chesscom.courses_common.v1;

enum UserSourceType {
  USER_SOURCE_TYPE_UNSPECIFIED = 0;
  USER_SOURCE_TYPE_CHESSCOM = 1;
  USER_SOURCE_TYPE_CHESSABLE = 2;
}

message CourseReviewAuthor {
  optional .chesscom.courses_common.v1.UserSource source = 1;
  optional string display_name = 2;
  optional .chesscom.courses_common.v1.Picture avatar = 3;
}

message UserSource {
  optional string id = 1;
  optional .ches
```

**Source references:** SRC-0323, SRC-1294  
**URL references:** None independently associated  
**Related findings:** FND-02436, FND-02437

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02439"></a>
## FND-02439: chesscom.courses_common.v1.UserSourceType.USER_SOURCE_TYPE_CHESSABLE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

USER_SOURCE_TYPE_CHESSABLE = 2;

### Evidence

- **SRC-0323** `research/proto/chesscom/courses_common/v1/course_review_author.proto` — [preserved redacted evidence](../evidence/text/50662a82e3ccf70be2020515c46cd4a1474257591c6c6d1424a94323059aa93e.proto)
  Character offset 214.

```text
n.v1;

enum UserSourceType {
  USER_SOURCE_TYPE_UNSPECIFIED = 0;
  USER_SOURCE_TYPE_CHESSCOM = 1;
  USER_SOURCE_TYPE_CHESSABLE = 2;
}

message CourseReviewAuthor {
  optional .chesscom.courses_common.v1.UserSource source = 1;
  optional string display_name = 2;
  optional .chesscom.courses_common.v1.Picture avatar = 3;
}

message UserSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.UserSource
```

**Source references:** SRC-0323, SRC-1294  
**URL references:** None independently associated  
**Related findings:** FND-02436, FND-02437, FND-02438

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02440"></a>
## FND-02440: message declaration: chesscom.courses_common.v1.CourseReviewAuthor

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseReviewAuthor {

### Evidence

- **SRC-0323** `research/proto/chesscom/courses_common/v1/course_review_author.proto` — [preserved redacted evidence](../evidence/text/50662a82e3ccf70be2020515c46cd4a1474257591c6c6d1424a94323059aa93e.proto)
  Character offset 249.

```text
_SOURCE_TYPE_UNSPECIFIED = 0;
  USER_SOURCE_TYPE_CHESSCOM = 1;
  USER_SOURCE_TYPE_CHESSABLE = 2;
}

message CourseReviewAuthor {
  optional .chesscom.courses_common.v1.UserSource source = 1;
  optional string display_name = 2;
  optional .chesscom.courses_common.v1.Picture avatar = 3;
}

message UserSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.UserSourceType type = 2;
}

```

**Source references:** SRC-0323, SRC-1294  
**URL references:** None independently associated  
**Related findings:** FND-02436, FND-02437, FND-02438

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02441"></a>
## FND-02441: chesscom.courses_common.v1.CourseReviewAuthor.source = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.UserSource source = 1;

### Evidence

- **SRC-0323** `research/proto/chesscom/courses_common/v1/course_review_author.proto` — [preserved redacted evidence](../evidence/text/50662a82e3ccf70be2020515c46cd4a1474257591c6c6d1424a94323059aa93e.proto)
  Character offset 280.

```text
 USER_SOURCE_TYPE_CHESSCOM = 1;
  USER_SOURCE_TYPE_CHESSABLE = 2;
}

message CourseReviewAuthor {
  optional .chesscom.courses_common.v1.UserSource source = 1;
  optional string display_name = 2;
  optional .chesscom.courses_common.v1.Picture avatar = 3;
}

message UserSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.UserSourceType type = 2;
}

```

**Source references:** SRC-0323, SRC-1294  
**URL references:** None independently associated  
**Related findings:** FND-02436, FND-02437, FND-02438

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02442"></a>
## FND-02442: chesscom.courses_common.v1.CourseReviewAuthor.display_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string display_name = 2;

### Evidence

- **SRC-0323** `research/proto/chesscom/courses_common/v1/course_review_author.proto` — [preserved redacted evidence](../evidence/text/50662a82e3ccf70be2020515c46cd4a1474257591c6c6d1424a94323059aa93e.proto)
  Character offset 342.

```text
 2;
}

message CourseReviewAuthor {
  optional .chesscom.courses_common.v1.UserSource source = 1;
  optional string display_name = 2;
  optional .chesscom.courses_common.v1.Picture avatar = 3;
}

message UserSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.UserSourceType type = 2;
}

```

**Source references:** SRC-0323, SRC-1294  
**URL references:** None independently associated  
**Related findings:** FND-02436, FND-02437, FND-02438

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02443"></a>
## FND-02443: chesscom.courses_common.v1.CourseReviewAuthor.avatar = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.Picture avatar = 3;

### Evidence

- **SRC-0323** `research/proto/chesscom/courses_common/v1/course_review_author.proto` — [preserved redacted evidence](../evidence/text/50662a82e3ccf70be2020515c46cd4a1474257591c6c6d1424a94323059aa93e.proto)
  Character offset 378.

```text
  optional .chesscom.courses_common.v1.UserSource source = 1;
  optional string display_name = 2;
  optional .chesscom.courses_common.v1.Picture avatar = 3;
}

message UserSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.UserSourceType type = 2;
}

```

**Source references:** SRC-0323, SRC-1294  
**URL references:** None independently associated  
**Related findings:** FND-02436, FND-02437, FND-02438

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02444"></a>
## FND-02444: message declaration: chesscom.courses_common.v1.UserSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserSource {

### Evidence

- **SRC-0323** `research/proto/chesscom/courses_common/v1/course_review_author.proto` — [preserved redacted evidence](../evidence/text/50662a82e3ccf70be2020515c46cd4a1474257591c6c6d1424a94323059aa93e.proto)
  Character offset 438.

```text
;
  optional string display_name = 2;
  optional .chesscom.courses_common.v1.Picture avatar = 3;
}

message UserSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.UserSourceType type = 2;
}

```

**Source references:** SRC-0323, SRC-1294  
**URL references:** None independently associated  
**Related findings:** FND-02436, FND-02437, FND-02438

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02445"></a>
## FND-02445: chesscom.courses_common.v1.UserSource.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0323** `research/proto/chesscom/courses_common/v1/course_review_author.proto` — [preserved redacted evidence](../evidence/text/50662a82e3ccf70be2020515c46cd4a1474257591c6c6d1424a94323059aa93e.proto)
  Character offset 461.

```text
play_name = 2;
  optional .chesscom.courses_common.v1.Picture avatar = 3;
}

message UserSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.UserSourceType type = 2;
}

```

**Source references:** SRC-0323, SRC-1294  
**URL references:** None independently associated  
**Related findings:** FND-02436, FND-02437, FND-02438

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02446"></a>
## FND-02446: chesscom.courses_common.v1.UserSource.type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.UserSourceType type = 2;

### Evidence

- **SRC-0323** `research/proto/chesscom/courses_common/v1/course_review_author.proto` — [preserved redacted evidence](../evidence/text/50662a82e3ccf70be2020515c46cd4a1474257591c6c6d1424a94323059aa93e.proto)
  Character offset 487.

```text
.chesscom.courses_common.v1.Picture avatar = 3;
}

message UserSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.UserSourceType type = 2;
}

```

**Source references:** SRC-0323, SRC-1294  
**URL references:** None independently associated  
**Related findings:** FND-02436, FND-02437, FND-02438

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02447"></a>
## FND-02447: enum declaration: chesscom.courses_common.v1.SourceType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SourceType {

### Evidence

- **SRC-0324** `research/proto/chesscom/courses_common/v1/course_source.proto` — [preserved redacted evidence](../evidence/text/39ae21dbae9cfa9966611a85ddc0c21ad262fc2fdaa2f22f6ef83bf8a5c93609.proto)
  Character offset 114.

```text
sscom/courses_common/v1/course_source.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum SourceType {
  SOURCE_TYPE_UNSPECIFIED = 0;
  SOURCE_TYPE_CHESSABLE = 1;
}

message CourseSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.SourceType type = 2;
}

```

**Source references:** SRC-0324, SRC-1295  
**URL references:** None independently associated  
**Related findings:** FND-02448, FND-02449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02448"></a>
## FND-02448: chesscom.courses_common.v1.SourceType.SOURCE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SOURCE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0324** `research/proto/chesscom/courses_common/v1/course_source.proto` — [preserved redacted evidence](../evidence/text/39ae21dbae9cfa9966611a85ddc0c21ad262fc2fdaa2f22f6ef83bf8a5c93609.proto)
  Character offset 134.

```text
/v1/course_source.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum SourceType {
  SOURCE_TYPE_UNSPECIFIED = 0;
  SOURCE_TYPE_CHESSABLE = 1;
}

message CourseSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.SourceType type = 2;
}

```

**Source references:** SRC-0324, SRC-1295  
**URL references:** None independently associated  
**Related findings:** FND-02447, FND-02449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02449"></a>
## FND-02449: chesscom.courses_common.v1.SourceType.SOURCE_TYPE_CHESSABLE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SOURCE_TYPE_CHESSABLE = 1;

### Evidence

- **SRC-0324** `research/proto/chesscom/courses_common/v1/course_source.proto` — [preserved redacted evidence](../evidence/text/39ae21dbae9cfa9966611a85ddc0c21ad262fc2fdaa2f22f6ef83bf8a5c93609.proto)
  Character offset 165.

```text
ax: proto3

package chesscom.courses_common.v1;

enum SourceType {
  SOURCE_TYPE_UNSPECIFIED = 0;
  SOURCE_TYPE_CHESSABLE = 1;
}

message CourseSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.SourceType type = 2;
}

```

**Source references:** SRC-0324, SRC-1295  
**URL references:** None independently associated  
**Related findings:** FND-02447, FND-02448

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02450"></a>
## FND-02450: message declaration: chesscom.courses_common.v1.CourseSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseSource {

### Evidence

- **SRC-0324** `research/proto/chesscom/courses_common/v1/course_source.proto` — [preserved redacted evidence](../evidence/text/39ae21dbae9cfa9966611a85ddc0c21ad262fc2fdaa2f22f6ef83bf8a5c93609.proto)
  Character offset 195.

```text
ourses_common.v1;

enum SourceType {
  SOURCE_TYPE_UNSPECIFIED = 0;
  SOURCE_TYPE_CHESSABLE = 1;
}

message CourseSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.SourceType type = 2;
}

```

**Source references:** SRC-0324, SRC-1295  
**URL references:** None independently associated  
**Related findings:** FND-02447, FND-02448, FND-02449

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02451"></a>
## FND-02451: chesscom.courses_common.v1.CourseSource.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0324** `research/proto/chesscom/courses_common/v1/course_source.proto` — [preserved redacted evidence](../evidence/text/39ae21dbae9cfa9966611a85ddc0c21ad262fc2fdaa2f22f6ef83bf8a5c93609.proto)
  Character offset 220.

```text
ourceType {
  SOURCE_TYPE_UNSPECIFIED = 0;
  SOURCE_TYPE_CHESSABLE = 1;
}

message CourseSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.SourceType type = 2;
}

```

**Source references:** SRC-0324, SRC-1295  
**URL references:** None independently associated  
**Related findings:** FND-02447, FND-02448, FND-02449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02452"></a>
## FND-02452: chesscom.courses_common.v1.CourseSource.type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.SourceType type = 2;

### Evidence

- **SRC-0324** `research/proto/chesscom/courses_common/v1/course_source.proto` — [preserved redacted evidence](../evidence/text/39ae21dbae9cfa9966611a85ddc0c21ad262fc2fdaa2f22f6ef83bf8a5c93609.proto)
  Character offset 246.

```text
UNSPECIFIED = 0;
  SOURCE_TYPE_CHESSABLE = 1;
}

message CourseSource {
  optional string id = 1;
  optional .chesscom.courses_common.v1.SourceType type = 2;
}

```

**Source references:** SRC-0324, SRC-1295  
**URL references:** None independently associated  
**Related findings:** FND-02447, FND-02448, FND-02449

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02453"></a>
## FND-02453: enum declaration: chesscom.courses_common.v1.CourseTargetLevel

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseTargetLevel {

### Evidence

- **SRC-0325** `research/proto/chesscom/courses_common/v1/course_target_level.proto` — [preserved redacted evidence](../evidence/text/f4c98a8f0811555b4d57e3474a5a194ba5842545044adb1deb3ba3ab3d98b708.proto)
  Character offset 120.

```text
courses_common/v1/course_target_level.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum CourseTargetLevel {
  COURSE_TARGET_LEVEL_UNSPECIFIED = 0;
  COURSE_TARGET_LEVEL_NOVICE = 1;
  COURSE_TARGET_LEVEL_BEGINNER = 2;
  COURSE_TARGET_LEVEL_INTERMEDIATE = 3;
  COURSE_TARGET_LEVEL_ADVANCED = 4;
  COURSE_TARGET_LEVEL_MASTER = 5;
  COURSE_TARGET_LEVEL_EXPERT = 6;
}

```

**Source references:** SRC-0325, SRC-1296  
**URL references:** None independently associated  
**Related findings:** FND-02454, FND-02455

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02454"></a>
## FND-02454: chesscom.courses_common.v1.CourseTargetLevel.COURSE_TARGET_LEVEL_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TARGET_LEVEL_UNSPECIFIED = 0;

### Evidence

- **SRC-0325** `research/proto/chesscom/courses_common/v1/course_target_level.proto` — [preserved redacted evidence](../evidence/text/f4c98a8f0811555b4d57e3474a5a194ba5842545044adb1deb3ba3ab3d98b708.proto)
  Character offset 147.

```text
rget_level.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum CourseTargetLevel {
  COURSE_TARGET_LEVEL_UNSPECIFIED = 0;
  COURSE_TARGET_LEVEL_NOVICE = 1;
  COURSE_TARGET_LEVEL_BEGINNER = 2;
  COURSE_TARGET_LEVEL_INTERMEDIATE = 3;
  COURSE_TARGET_LEVEL_ADVANCED = 4;
  COURSE_TARGET_LEVEL_MASTER = 5;
  COURSE_TARGET_LEVEL_EXPERT = 6;
}

```

**Source references:** SRC-0325, SRC-1296  
**URL references:** None independently associated  
**Related findings:** FND-02453, FND-02455

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02455"></a>
## FND-02455: chesscom.courses_common.v1.CourseTargetLevel.COURSE_TARGET_LEVEL_NOVICE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TARGET_LEVEL_NOVICE = 1;

### Evidence

- **SRC-0325** `research/proto/chesscom/courses_common/v1/course_target_level.proto` — [preserved redacted evidence](../evidence/text/f4c98a8f0811555b4d57e3474a5a194ba5842545044adb1deb3ba3ab3d98b708.proto)
  Character offset 186.

```text
kage chesscom.courses_common.v1;

enum CourseTargetLevel {
  COURSE_TARGET_LEVEL_UNSPECIFIED = 0;
  COURSE_TARGET_LEVEL_NOVICE = 1;
  COURSE_TARGET_LEVEL_BEGINNER = 2;
  COURSE_TARGET_LEVEL_INTERMEDIATE = 3;
  COURSE_TARGET_LEVEL_ADVANCED = 4;
  COURSE_TARGET_LEVEL_MASTER = 5;
  COURSE_TARGET_LEVEL_EXPERT = 6;
}

```

**Source references:** SRC-0325, SRC-1296  
**URL references:** None independently associated  
**Related findings:** FND-02453, FND-02454

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02456"></a>
## FND-02456: chesscom.courses_common.v1.CourseTargetLevel.COURSE_TARGET_LEVEL_BEGINNER = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TARGET_LEVEL_BEGINNER = 2;

### Evidence

- **SRC-0325** `research/proto/chesscom/courses_common/v1/course_target_level.proto` — [preserved redacted evidence](../evidence/text/f4c98a8f0811555b4d57e3474a5a194ba5842545044adb1deb3ba3ab3d98b708.proto)
  Character offset 220.

```text
enum CourseTargetLevel {
  COURSE_TARGET_LEVEL_UNSPECIFIED = 0;
  COURSE_TARGET_LEVEL_NOVICE = 1;
  COURSE_TARGET_LEVEL_BEGINNER = 2;
  COURSE_TARGET_LEVEL_INTERMEDIATE = 3;
  COURSE_TARGET_LEVEL_ADVANCED = 4;
  COURSE_TARGET_LEVEL_MASTER = 5;
  COURSE_TARGET_LEVEL_EXPERT = 6;
}

```

**Source references:** SRC-0325, SRC-1296  
**URL references:** None independently associated  
**Related findings:** FND-02453, FND-02454, FND-02455

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02457"></a>
## FND-02457: chesscom.courses_common.v1.CourseTargetLevel.COURSE_TARGET_LEVEL_INTERMEDIATE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TARGET_LEVEL_INTERMEDIATE = 3;

### Evidence

- **SRC-0325** `research/proto/chesscom/courses_common/v1/course_target_level.proto` — [preserved redacted evidence](../evidence/text/f4c98a8f0811555b4d57e3474a5a194ba5842545044adb1deb3ba3ab3d98b708.proto)
  Character offset 256.

```text
RGET_LEVEL_UNSPECIFIED = 0;
  COURSE_TARGET_LEVEL_NOVICE = 1;
  COURSE_TARGET_LEVEL_BEGINNER = 2;
  COURSE_TARGET_LEVEL_INTERMEDIATE = 3;
  COURSE_TARGET_LEVEL_ADVANCED = 4;
  COURSE_TARGET_LEVEL_MASTER = 5;
  COURSE_TARGET_LEVEL_EXPERT = 6;
}

```

**Source references:** SRC-0325, SRC-1296  
**URL references:** None independently associated  
**Related findings:** FND-02453, FND-02454, FND-02455

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02458"></a>
## FND-02458: chesscom.courses_common.v1.CourseTargetLevel.COURSE_TARGET_LEVEL_ADVANCED = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TARGET_LEVEL_ADVANCED = 4;

### Evidence

- **SRC-0325** `research/proto/chesscom/courses_common/v1/course_target_level.proto` — [preserved redacted evidence](../evidence/text/f4c98a8f0811555b4d57e3474a5a194ba5842545044adb1deb3ba3ab3d98b708.proto)
  Character offset 296.

```text
GET_LEVEL_NOVICE = 1;
  COURSE_TARGET_LEVEL_BEGINNER = 2;
  COURSE_TARGET_LEVEL_INTERMEDIATE = 3;
  COURSE_TARGET_LEVEL_ADVANCED = 4;
  COURSE_TARGET_LEVEL_MASTER = 5;
  COURSE_TARGET_LEVEL_EXPERT = 6;
}

```

**Source references:** SRC-0325, SRC-1296  
**URL references:** None independently associated  
**Related findings:** FND-02453, FND-02454, FND-02455

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02459"></a>
## FND-02459: chesscom.courses_common.v1.CourseTargetLevel.COURSE_TARGET_LEVEL_MASTER = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TARGET_LEVEL_MASTER = 5;

### Evidence

- **SRC-0325** `research/proto/chesscom/courses_common/v1/course_target_level.proto` — [preserved redacted evidence](../evidence/text/f4c98a8f0811555b4d57e3474a5a194ba5842545044adb1deb3ba3ab3d98b708.proto)
  Character offset 332.

```text
T_LEVEL_BEGINNER = 2;
  COURSE_TARGET_LEVEL_INTERMEDIATE = 3;
  COURSE_TARGET_LEVEL_ADVANCED = 4;
  COURSE_TARGET_LEVEL_MASTER = 5;
  COURSE_TARGET_LEVEL_EXPERT = 6;
}

```

**Source references:** SRC-0325, SRC-1296  
**URL references:** None independently associated  
**Related findings:** FND-02453, FND-02454, FND-02455

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02460"></a>
## FND-02460: chesscom.courses_common.v1.CourseTargetLevel.COURSE_TARGET_LEVEL_EXPERT = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TARGET_LEVEL_EXPERT = 6;

### Evidence

- **SRC-0325** `research/proto/chesscom/courses_common/v1/course_target_level.proto` — [preserved redacted evidence](../evidence/text/f4c98a8f0811555b4d57e3474a5a194ba5842545044adb1deb3ba3ab3d98b708.proto)
  Character offset 366.

```text
GET_LEVEL_INTERMEDIATE = 3;
  COURSE_TARGET_LEVEL_ADVANCED = 4;
  COURSE_TARGET_LEVEL_MASTER = 5;
  COURSE_TARGET_LEVEL_EXPERT = 6;
}

```

**Source references:** SRC-0325, SRC-1296  
**URL references:** None independently associated  
**Related findings:** FND-02453, FND-02454, FND-02455

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02461"></a>
## FND-02461: message declaration: chesscom.courses_common.v1.CourseVariationAlternativeMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseVariationAlternativeMove {

### Evidence

- **SRC-0326** `research/proto/chesscom/courses_common/v1/course_variation_alternative_move.proto` — [preserved redacted evidence](../evidence/text/c0a3bfd33b239137ee75a07359b5fd7dff8f4a0a19d73adda36fce3842cc1569.proto)
  Character offset 134.

```text
/v1/course_variation_alternative_move.proto
// syntax: proto3

package chesscom.courses_common.v1;

message CourseVariationAlternativeMove {
  optional string san = 1;
  optional string fen = 2;
}

```

**Source references:** SRC-0326, SRC-1297  
**URL references:** None independently associated  
**Related findings:** FND-02462, FND-02463

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02462"></a>
## FND-02462: chesscom.courses_common.v1.CourseVariationAlternativeMove.san = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string san = 1;

### Evidence

- **SRC-0326** `research/proto/chesscom/courses_common/v1/course_variation_alternative_move.proto` — [preserved redacted evidence](../evidence/text/c0a3bfd33b239137ee75a07359b5fd7dff8f4a0a19d73adda36fce3842cc1569.proto)
  Character offset 177.

```text

// syntax: proto3

package chesscom.courses_common.v1;

message CourseVariationAlternativeMove {
  optional string san = 1;
  optional string fen = 2;
}

```

**Source references:** SRC-0326, SRC-1297  
**URL references:** None independently associated  
**Related findings:** FND-02461, FND-02463

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02463"></a>
## FND-02463: chesscom.courses_common.v1.CourseVariationAlternativeMove.fen = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string fen = 2;

### Evidence

- **SRC-0326** `research/proto/chesscom/courses_common/v1/course_variation_alternative_move.proto` — [preserved redacted evidence](../evidence/text/c0a3bfd33b239137ee75a07359b5fd7dff8f4a0a19d73adda36fce3842cc1569.proto)
  Character offset 204.

```text
 chesscom.courses_common.v1;

message CourseVariationAlternativeMove {
  optional string san = 1;
  optional string fen = 2;
}

```

**Source references:** SRC-0326, SRC-1297  
**URL references:** None independently associated  
**Related findings:** FND-02461, FND-02462

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02464"></a>
## FND-02464: enum declaration: chesscom.courses_common.v1.CourseVariationType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseVariationType {

### Evidence

- **SRC-0327** `research/proto/chesscom/courses_common/v1/course_variation_type.proto` — [preserved redacted evidence](../evidence/text/48b8e6f57be85f3cc93d9e8b9454c30e2314c60c00b81e3b762307a2b92f8fd7.proto)
  Character offset 122.

```text
urses_common/v1/course_variation_type.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum CourseVariationType {
  COURSE_VARIATION_TYPE_UNSPECIFIED = 0;
  COURSE_VARIATION_TYPE_INFORMATIONAL = 1;
  COURSE_VARIATION_TYPE_ALTERNATIVE = 2;
  COURSE_VARIATION_TYPE_REFERENCE = 3;
  COURSE_VARIATION_TYPE_PUZZLE = 4;
  COURSE_VARIATION_TYPE_LESSON = 5;
}

```

**Source references:** SRC-0327, SRC-1298  
**URL references:** None independently associated  
**Related findings:** FND-02465, FND-02466

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02465"></a>
## FND-02465: chesscom.courses_common.v1.CourseVariationType.COURSE_VARIATION_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_VARIATION_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0327** `research/proto/chesscom/courses_common/v1/course_variation_type.proto` — [preserved redacted evidence](../evidence/text/48b8e6f57be85f3cc93d9e8b9454c30e2314c60c00b81e3b762307a2b92f8fd7.proto)
  Character offset 151.

```text
ion_type.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum CourseVariationType {
  COURSE_VARIATION_TYPE_UNSPECIFIED = 0;
  COURSE_VARIATION_TYPE_INFORMATIONAL = 1;
  COURSE_VARIATION_TYPE_ALTERNATIVE = 2;
  COURSE_VARIATION_TYPE_REFERENCE = 3;
  COURSE_VARIATION_TYPE_PUZZLE = 4;
  COURSE_VARIATION_TYPE_LESSON = 5;
}

```

**Source references:** SRC-0327, SRC-1298  
**URL references:** None independently associated  
**Related findings:** FND-02464, FND-02466

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02466"></a>
## FND-02466: chesscom.courses_common.v1.CourseVariationType.COURSE_VARIATION_TYPE_INFORMATIONAL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_VARIATION_TYPE_INFORMATIONAL = 1;

### Evidence

- **SRC-0327** `research/proto/chesscom/courses_common/v1/course_variation_type.proto` — [preserved redacted evidence](../evidence/text/48b8e6f57be85f3cc93d9e8b9454c30e2314c60c00b81e3b762307a2b92f8fd7.proto)
  Character offset 192.

```text
 chesscom.courses_common.v1;

enum CourseVariationType {
  COURSE_VARIATION_TYPE_UNSPECIFIED = 0;
  COURSE_VARIATION_TYPE_INFORMATIONAL = 1;
  COURSE_VARIATION_TYPE_ALTERNATIVE = 2;
  COURSE_VARIATION_TYPE_REFERENCE = 3;
  COURSE_VARIATION_TYPE_PUZZLE = 4;
  COURSE_VARIATION_TYPE_LESSON = 5;
}

```

**Source references:** SRC-0327, SRC-1298  
**URL references:** None independently associated  
**Related findings:** FND-02464, FND-02465

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02467"></a>
## FND-02467: chesscom.courses_common.v1.CourseVariationType.COURSE_VARIATION_TYPE_ALTERNATIVE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_VARIATION_TYPE_ALTERNATIVE = 2;

### Evidence

- **SRC-0327** `research/proto/chesscom/courses_common/v1/course_variation_type.proto` — [preserved redacted evidence](../evidence/text/48b8e6f57be85f3cc93d9e8b9454c30e2314c60c00b81e3b762307a2b92f8fd7.proto)
  Character offset 235.

```text
riationType {
  COURSE_VARIATION_TYPE_UNSPECIFIED = 0;
  COURSE_VARIATION_TYPE_INFORMATIONAL = 1;
  COURSE_VARIATION_TYPE_ALTERNATIVE = 2;
  COURSE_VARIATION_TYPE_REFERENCE = 3;
  COURSE_VARIATION_TYPE_PUZZLE = 4;
  COURSE_VARIATION_TYPE_LESSON = 5;
}

```

**Source references:** SRC-0327, SRC-1298  
**URL references:** None independently associated  
**Related findings:** FND-02464, FND-02465, FND-02466

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02468"></a>
## FND-02468: chesscom.courses_common.v1.CourseVariationType.COURSE_VARIATION_TYPE_REFERENCE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_VARIATION_TYPE_REFERENCE = 3;

### Evidence

- **SRC-0327** `research/proto/chesscom/courses_common/v1/course_variation_type.proto` — [preserved redacted evidence](../evidence/text/48b8e6f57be85f3cc93d9e8b9454c30e2314c60c00b81e3b762307a2b92f8fd7.proto)
  Character offset 276.

```text
PECIFIED = 0;
  COURSE_VARIATION_TYPE_INFORMATIONAL = 1;
  COURSE_VARIATION_TYPE_ALTERNATIVE = 2;
  COURSE_VARIATION_TYPE_REFERENCE = 3;
  COURSE_VARIATION_TYPE_PUZZLE = 4;
  COURSE_VARIATION_TYPE_LESSON = 5;
}

```

**Source references:** SRC-0327, SRC-1298  
**URL references:** None independently associated  
**Related findings:** FND-02464, FND-02465, FND-02466

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02469"></a>
## FND-02469: chesscom.courses_common.v1.CourseVariationType.COURSE_VARIATION_TYPE_PUZZLE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_VARIATION_TYPE_PUZZLE = 4;

### Evidence

- **SRC-0327** `research/proto/chesscom/courses_common/v1/course_variation_type.proto` — [preserved redacted evidence](../evidence/text/48b8e6f57be85f3cc93d9e8b9454c30e2314c60c00b81e3b762307a2b92f8fd7.proto)
  Character offset 315.

```text
NFORMATIONAL = 1;
  COURSE_VARIATION_TYPE_ALTERNATIVE = 2;
  COURSE_VARIATION_TYPE_REFERENCE = 3;
  COURSE_VARIATION_TYPE_PUZZLE = 4;
  COURSE_VARIATION_TYPE_LESSON = 5;
}

```

**Source references:** SRC-0327, SRC-1298  
**URL references:** None independently associated  
**Related findings:** FND-02464, FND-02465, FND-02466

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02470"></a>
## FND-02470: chesscom.courses_common.v1.CourseVariationType.COURSE_VARIATION_TYPE_LESSON = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_VARIATION_TYPE_LESSON = 5;

### Evidence

- **SRC-0327** `research/proto/chesscom/courses_common/v1/course_variation_type.proto` — [preserved redacted evidence](../evidence/text/48b8e6f57be85f3cc93d9e8b9454c30e2314c60c00b81e3b762307a2b92f8fd7.proto)
  Character offset 351.

```text
_TYPE_ALTERNATIVE = 2;
  COURSE_VARIATION_TYPE_REFERENCE = 3;
  COURSE_VARIATION_TYPE_PUZZLE = 4;
  COURSE_VARIATION_TYPE_LESSON = 5;
}

```

**Source references:** SRC-0327, SRC-1298  
**URL references:** None independently associated  
**Related findings:** FND-02464, FND-02465, FND-02466

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02471"></a>
## FND-02471: enum declaration: chesscom.courses_common.v1.CourseVideoProvider

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseVideoProvider {

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 113.

```text
esscom/courses_common/v1/course_video.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum CourseVideoProvider {
  COURSE_VIDEO_PROVIDER_UNSPECIFIED = 0;
  COURSE_VIDEO_PROVIDER_WISTIA = 1;
  COURSE_VIDEO_PROVIDER_YOUTUBE = 2;
  COURSE_VIDEO_PROVIDER_VIMEO = 3;
}

message CourseVideo {
  oneof _id {
  string id = 1;
  }
  oneof _thumbnail {
  .chesscom.courses_common.v1.Picture thumbnail = 5;
  }
  oneo
```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02472, FND-02473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02472"></a>
## FND-02472: chesscom.courses_common.v1.CourseVideoProvider.COURSE_VIDEO_PROVIDER_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_VIDEO_PROVIDER_UNSPECIFIED = 0;

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 142.

```text
se_video.proto
// syntax: proto3

package chesscom.courses_common.v1;

enum CourseVideoProvider {
  COURSE_VIDEO_PROVIDER_UNSPECIFIED = 0;
  COURSE_VIDEO_PROVIDER_WISTIA = 1;
  COURSE_VIDEO_PROVIDER_YOUTUBE = 2;
  COURSE_VIDEO_PROVIDER_VIMEO = 3;
}

message CourseVideo {
  oneof _id {
  string id = 1;
  }
  oneof _thumbnail {
  .chesscom.courses_common.v1.Picture thumbnail = 5;
  }
  oneof _duration_seconds {
  int32
```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02473"></a>
## FND-02473: chesscom.courses_common.v1.CourseVideoProvider.COURSE_VIDEO_PROVIDER_WISTIA = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_VIDEO_PROVIDER_WISTIA = 1;

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 183.

```text
 chesscom.courses_common.v1;

enum CourseVideoProvider {
  COURSE_VIDEO_PROVIDER_UNSPECIFIED = 0;
  COURSE_VIDEO_PROVIDER_WISTIA = 1;
  COURSE_VIDEO_PROVIDER_YOUTUBE = 2;
  COURSE_VIDEO_PROVIDER_VIMEO = 3;
}

message CourseVideo {
  oneof _id {
  string id = 1;
  }
  oneof _thumbnail {
  .chesscom.courses_common.v1.Picture thumbnail = 5;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 6;
  }
  optional str
```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02472

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02474"></a>
## FND-02474: chesscom.courses_common.v1.CourseVideoProvider.COURSE_VIDEO_PROVIDER_YOUTUBE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_VIDEO_PROVIDER_YOUTUBE = 2;

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 219.

```text
ourseVideoProvider {
  COURSE_VIDEO_PROVIDER_UNSPECIFIED = 0;
  COURSE_VIDEO_PROVIDER_WISTIA = 1;
  COURSE_VIDEO_PROVIDER_YOUTUBE = 2;
  COURSE_VIDEO_PROVIDER_VIMEO = 3;
}

message CourseVideo {
  oneof _id {
  string id = 1;
  }
  oneof _thumbnail {
  .chesscom.courses_common.v1.Picture thumbnail = 5;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 6;
  }
  optional string name = 2;
  optional .chesscom.c
```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02472, FND-02473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
