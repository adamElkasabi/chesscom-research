# data_models — findings 2201–2300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-02475"></a>
## FND-02475: chesscom.courses_common.v1.CourseVideoProvider.COURSE_VIDEO_PROVIDER_VIMEO = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_VIDEO_PROVIDER_VIMEO = 3;

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 256.

```text
ROVIDER_UNSPECIFIED = 0;
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
  optional .chesscom.courses_common.v1.CourseVideoProvider 
```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02472, FND-02473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02476"></a>
## FND-02476: message declaration: chesscom.courses_common.v1.CourseVideo

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseVideo {

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 292.

```text
DEO_PROVIDER_WISTIA = 1;
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
  optional .chesscom.courses_common.v1.CourseVideoProvider provider = 3;
  optional string prov
```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02472, FND-02473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02477"></a>
## FND-02477: oneof declaration: chesscom.courses_common.v1.CourseVideo._id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _id {

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 316.

```text

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
  optional .chesscom.courses_common.v1.CourseVideoProvider provider = 3;
  optional string provider_video_identifier = 
```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02472, FND-02473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02478"></a>
## FND-02478: chesscom.courses_common.v1.CourseVideo.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string id = 1;

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 330.

```text
O_PROVIDER_YOUTUBE = 2;
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
  optional .chesscom.courses_common.v1.CourseVideoProvider provider = 3;
  optional string provider_video_identifier = 4;
}

```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02472, FND-02473

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02479"></a>
## FND-02479: oneof declaration: chesscom.courses_common.v1.CourseVideo._thumbnail

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _thumbnail {

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 351.

```text
2;
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
  optional .chesscom.courses_common.v1.CourseVideoProvider provider = 3;
  optional string provider_video_identifier = 4;
}

```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02472, FND-02473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02480"></a>
## FND-02480: chesscom.courses_common.v1.CourseVideo.thumbnail = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses_common.v1.Picture thumbnail = 5;

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 372.

```text
VIDER_VIMEO = 3;
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
  optional .chesscom.courses_common.v1.CourseVideoProvider provider = 3;
  optional string provider_video_identifier = 4;
}

```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02472, FND-02473

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02481"></a>
## FND-02481: oneof declaration: chesscom.courses_common.v1.CourseVideo._duration_seconds

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _duration_seconds {

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 429.

```text
 string id = 1;
  }
  oneof _thumbnail {
  .chesscom.courses_common.v1.Picture thumbnail = 5;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 6;
  }
  optional string name = 2;
  optional .chesscom.courses_common.v1.CourseVideoProvider provider = 3;
  optional string provider_video_identifier = 4;
}

```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02472, FND-02473

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02482"></a>
## FND-02482: chesscom.courses_common.v1.CourseVideo.duration_seconds = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 duration_seconds = 6;

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 457.

```text
_thumbnail {
  .chesscom.courses_common.v1.Picture thumbnail = 5;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 6;
  }
  optional string name = 2;
  optional .chesscom.courses_common.v1.CourseVideoProvider provider = 3;
  optional string provider_video_identifier = 4;
}

```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02472, FND-02473

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02483"></a>
## FND-02483: chesscom.courses_common.v1.CourseVideo.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 491.

```text
ommon.v1.Picture thumbnail = 5;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 6;
  }
  optional string name = 2;
  optional .chesscom.courses_common.v1.CourseVideoProvider provider = 3;
  optional string provider_video_identifier = 4;
}

```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02472, FND-02473

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02484"></a>
## FND-02484: chesscom.courses_common.v1.CourseVideo.provider = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseVideoProvider provider = 3;

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 519.

```text
 5;
  }
  oneof _duration_seconds {
  int32 duration_seconds = 6;
  }
  optional string name = 2;
  optional .chesscom.courses_common.v1.CourseVideoProvider provider = 3;
  optional string provider_video_identifier = 4;
}

```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02472, FND-02473

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02485"></a>
## FND-02485: chesscom.courses_common.v1.CourseVideo.provider_video_identifier = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string provider_video_identifier = 4;

### Evidence

- **SRC-0328** `research/proto/chesscom/courses_common/v1/course_video.proto` — [preserved redacted evidence](../evidence/text/87aaf90d04df3bac0af979262be5552ed68445eca30a20fc057f7c51b7f3eb05.proto)
  Character offset 592.

```text
ptional string name = 2;
  optional .chesscom.courses_common.v1.CourseVideoProvider provider = 3;
  optional string provider_video_identifier = 4;
}

```

**Source references:** SRC-0328, SRC-1299  
**URL references:** None independently associated  
**Related findings:** FND-02471, FND-02472, FND-02473

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02486"></a>
## FND-02486: message declaration: chesscom.courses_common.v1.Picture

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Picture {

### Evidence

- **SRC-0329** `research/proto/chesscom/courses_common/v1/picture.proto` — [preserved redacted evidence](../evidence/text/a59721dcc6e7eda4fae1d86cd642e11e6d9155ab2dce12fd59508f9d8de5405f.proto)
  Character offset 108.

```text
e: chesscom/courses_common/v1/picture.proto
// syntax: proto3

package chesscom.courses_common.v1;

message Picture {
  oneof _preview_url {
  string preview_url = 2;
  }
  optional string url = 1;
}

```

**Source references:** SRC-0329, SRC-1300  
**URL references:** None independently associated  
**Related findings:** FND-02487, FND-02488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02487"></a>
## FND-02487: oneof declaration: chesscom.courses_common.v1.Picture._preview_url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _preview_url {

### Evidence

- **SRC-0329** `research/proto/chesscom/courses_common/v1/picture.proto` — [preserved redacted evidence](../evidence/text/a59721dcc6e7eda4fae1d86cd642e11e6d9155ab2dce12fd59508f9d8de5405f.proto)
  Character offset 128.

```text
common/v1/picture.proto
// syntax: proto3

package chesscom.courses_common.v1;

message Picture {
  oneof _preview_url {
  string preview_url = 2;
  }
  optional string url = 1;
}

```

**Source references:** SRC-0329, SRC-1300  
**URL references:** None independently associated  
**Related findings:** FND-02486, FND-02488

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02488"></a>
## FND-02488: chesscom.courses_common.v1.Picture.preview_url = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string preview_url = 2;

### Evidence

- **SRC-0329** `research/proto/chesscom/courses_common/v1/picture.proto` — [preserved redacted evidence](../evidence/text/a59721dcc6e7eda4fae1d86cd642e11e6d9155ab2dce12fd59508f9d8de5405f.proto)
  Character offset 151.

```text

// syntax: proto3

package chesscom.courses_common.v1;

message Picture {
  oneof _preview_url {
  string preview_url = 2;
  }
  optional string url = 1;
}

```

**Source references:** SRC-0329, SRC-1300  
**URL references:** None independently associated  
**Related findings:** FND-02486, FND-02487

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02489"></a>
## FND-02489: chesscom.courses_common.v1.Picture.url = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string url = 1;

### Evidence

- **SRC-0329** `research/proto/chesscom/courses_common/v1/picture.proto` — [preserved redacted evidence](../evidence/text/a59721dcc6e7eda4fae1d86cd642e11e6d9155ab2dce12fd59508f9d8de5405f.proto)
  Character offset 181.

```text
esscom.courses_common.v1;

message Picture {
  oneof _preview_url {
  string preview_url = 2;
  }
  optional string url = 1;
}

```

**Source references:** SRC-0329, SRC-1300  
**URL references:** None independently associated  
**Related findings:** FND-02486, FND-02487, FND-02488

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02490"></a>
## FND-02490: message declaration: chesscom.courses_common.v1.Range

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Range {

### Evidence

- **SRC-0330** `research/proto/chesscom/courses_common/v1/range.proto` — [preserved redacted evidence](../evidence/text/09c29c4eb82b611b04c814fce29c2b894201e170f71d86ccbcf3bb9ccd1defa4.proto)
  Character offset 106.

```text
rce: chesscom/courses_common/v1/range.proto
// syntax: proto3

package chesscom.courses_common.v1;

message Range {
  optional int32 from = 1;
  optional int32 to = 2;
}

```

**Source references:** SRC-0330, SRC-1301  
**URL references:** None independently associated  
**Related findings:** FND-02491, FND-02492

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02491"></a>
## FND-02491: chesscom.courses_common.v1.Range.from = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 from = 1;

### Evidence

- **SRC-0330** `research/proto/chesscom/courses_common/v1/range.proto` — [preserved redacted evidence](../evidence/text/09c29c4eb82b611b04c814fce29c2b894201e170f71d86ccbcf3bb9ccd1defa4.proto)
  Character offset 124.

```text
ses_common/v1/range.proto
// syntax: proto3

package chesscom.courses_common.v1;

message Range {
  optional int32 from = 1;
  optional int32 to = 2;
}

```

**Source references:** SRC-0330, SRC-1301  
**URL references:** None independently associated  
**Related findings:** FND-02490, FND-02492

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02492"></a>
## FND-02492: chesscom.courses_common.v1.Range.to = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 to = 2;

### Evidence

- **SRC-0330** `research/proto/chesscom/courses_common/v1/range.proto` — [preserved redacted evidence](../evidence/text/09c29c4eb82b611b04c814fce29c2b894201e170f71d86ccbcf3bb9ccd1defa4.proto)
  Character offset 151.

```text
/ syntax: proto3

package chesscom.courses_common.v1;

message Range {
  optional int32 from = 1;
  optional int32 to = 2;
}

```

**Source references:** SRC-0330, SRC-1301  
**URL references:** None independently associated  
**Related findings:** FND-02490, FND-02491

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02493"></a>
## FND-02493: enum declaration: chesscom.engine.v1.Engine

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Engine {

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 91.

```text
// source: chesscom/engine/v1/engine.proto
// syntax: proto3

package chesscom.engine.v1;

enum Engine {
  ENGINE_UNSPECIFIED = 0;
  ENGINE_SF12 = 1;
  ENGINE_SF15 = 2;
  ENGINE_SF15_NNUE = 3;
  ENGINE_SF15_1 = 4;
  ENGINE_SF15_1_NNUE = 5;
  ENGINE_SF16_NNUE = 6;
  ENGINE_SF9_FAIRPLAY_V1 = 7;
  ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HU
```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02494"></a>
## FND-02494: chesscom.engine.v1.Engine.ENGINE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_UNSPECIFIED = 0;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 107.

```text
ce: chesscom/engine/v1/engine.proto
// syntax: proto3

package chesscom.engine.v1;

enum Engine {
  ENGINE_UNSPECIFIED = 0;
  ENGINE_SF12 = 1;
  ENGINE_SF15 = 2;
  ENGINE_SF15_NNUE = 3;
  ENGINE_SF15_1 = 4;
  ENGINE_SF15_1_NNUE = 5;
  ENGINE_SF16_NNUE = 6;
  ENGINE_SF9_FAIRPLAY_V1 = 7;
  ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGI
```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02495"></a>
## FND-02495: chesscom.engine.v1.Engine.ENGINE_SF12 = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_SF12 = 1;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 133.

```text
ine.proto
// syntax: proto3

package chesscom.engine.v1;

enum Engine {
  ENGINE_UNSPECIFIED = 0;
  ENGINE_SF12 = 1;
  ENGINE_SF15 = 2;
  ENGINE_SF15_NNUE = 3;
  ENGINE_SF15_1 = 4;
  ENGINE_SF15_1_NNUE = 5;
  ENGINE_SF16_NNUE = 6;
  ENGINE_SF9_FAIRPLAY_V1 = 7;
  ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGIN
```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02496"></a>
## FND-02496: chesscom.engine.v1.Engine.ENGINE_SF15 = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_SF15 = 2;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 152.

```text
: proto3

package chesscom.engine.v1;

enum Engine {
  ENGINE_UNSPECIFIED = 0;
  ENGINE_SF12 = 1;
  ENGINE_SF15 = 2;
  ENGINE_SF15_NNUE = 3;
  ENGINE_SF15_1 = 4;
  ENGINE_SF15_1_NNUE = 5;
  ENGINE_SF16_NNUE = 6;
  ENGINE_SF9_FAIRPLAY_V1 = 7;
  ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGINE_SF19_NNUE = 14;
}
```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02497"></a>
## FND-02497: chesscom.engine.v1.Engine.ENGINE_SF15_NNUE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_SF15_NNUE = 3;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 171.

```text
hesscom.engine.v1;

enum Engine {
  ENGINE_UNSPECIFIED = 0;
  ENGINE_SF12 = 1;
  ENGINE_SF15 = 2;
  ENGINE_SF15_NNUE = 3;
  ENGINE_SF15_1 = 4;
  ENGINE_SF15_1_NNUE = 5;
  ENGINE_SF16_NNUE = 6;
  ENGINE_SF9_FAIRPLAY_V1 = 7;
  ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGINE_SF19_NNUE = 14;
}

```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02498"></a>
## FND-02498: chesscom.engine.v1.Engine.ENGINE_SF15_1 = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_SF15_1 = 4;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 195.

```text
 Engine {
  ENGINE_UNSPECIFIED = 0;
  ENGINE_SF12 = 1;
  ENGINE_SF15 = 2;
  ENGINE_SF15_NNUE = 3;
  ENGINE_SF15_1 = 4;
  ENGINE_SF15_1_NNUE = 5;
  ENGINE_SF16_NNUE = 6;
  ENGINE_SF9_FAIRPLAY_V1 = 7;
  ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGINE_SF19_NNUE = 14;
}

```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02499"></a>
## FND-02499: chesscom.engine.v1.Engine.ENGINE_SF15_1_NNUE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_SF15_1_NNUE = 5;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 216.

```text
SPECIFIED = 0;
  ENGINE_SF12 = 1;
  ENGINE_SF15 = 2;
  ENGINE_SF15_NNUE = 3;
  ENGINE_SF15_1 = 4;
  ENGINE_SF15_1_NNUE = 5;
  ENGINE_SF16_NNUE = 6;
  ENGINE_SF9_FAIRPLAY_V1 = 7;
  ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGINE_SF19_NNUE = 14;
}

```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02500"></a>
## FND-02500: chesscom.engine.v1.Engine.ENGINE_SF16_NNUE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_SF16_NNUE = 6;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 242.

```text
12 = 1;
  ENGINE_SF15 = 2;
  ENGINE_SF15_NNUE = 3;
  ENGINE_SF15_1 = 4;
  ENGINE_SF15_1_NNUE = 5;
  ENGINE_SF16_NNUE = 6;
  ENGINE_SF9_FAIRPLAY_V1 = 7;
  ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGINE_SF19_NNUE = 14;
}

```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02501"></a>
## FND-02501: chesscom.engine.v1.Engine.ENGINE_SF9_FAIRPLAY_V1 = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_SF9_FAIRPLAY_V1 = 7;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 266.

```text
2;
  ENGINE_SF15_NNUE = 3;
  ENGINE_SF15_1 = 4;
  ENGINE_SF15_1_NNUE = 5;
  ENGINE_SF16_NNUE = 6;
  ENGINE_SF9_FAIRPLAY_V1 = 7;
  ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGINE_SF19_NNUE = 14;
}

```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02502"></a>
## FND-02502: chesscom.engine.v1.Engine.ENGINE_DRAGON_3_3 = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_DRAGON_3_3 = 8;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 296.

```text
NGINE_SF15_1 = 4;
  ENGINE_SF15_1_NNUE = 5;
  ENGINE_SF16_NNUE = 6;
  ENGINE_SF9_FAIRPLAY_V1 = 7;
  ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGINE_SF19_NNUE = 14;
}

```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02503"></a>
## FND-02503: chesscom.engine.v1.Engine.ENGINE_KOMODO_3_3 = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_KOMODO_3_3 = 9;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 321.

```text
E_SF15_1_NNUE = 5;
  ENGINE_SF16_NNUE = 6;
  ENGINE_SF9_FAIRPLAY_V1 = 7;
  ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGINE_SF19_NNUE = 14;
}

```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02504"></a>
## FND-02504: chesscom.engine.v1.Engine.ENGINE_SF16_1_NNUE = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_SF16_1_NNUE = 10;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 346.

```text
NE_SF16_NNUE = 6;
  ENGINE_SF9_FAIRPLAY_V1 = 7;
  ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGINE_SF19_NNUE = 14;
}

```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02505"></a>
## FND-02505: chesscom.engine.v1.Engine.ENGINE_TORCH_3 = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_TORCH_3 = 11;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 373.

```text
SF9_FAIRPLAY_V1 = 7;
  ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGINE_SF19_NNUE = 14;
}

```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02506"></a>
## FND-02506: chesscom.engine.v1.Engine.ENGINE_TORCH_HUMAN = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_TORCH_HUMAN = 12;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 396.

```text
ENGINE_DRAGON_3_3 = 8;
  ENGINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGINE_SF19_NNUE = 14;
}

```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02507"></a>
## FND-02507: chesscom.engine.v1.Engine.ENGINE_SF18_NNUE = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_SF18_NNUE = 13;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 423.

```text
GINE_KOMODO_3_3 = 9;
  ENGINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGINE_SF19_NNUE = 14;
}

```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02508"></a>
## FND-02508: chesscom.engine.v1.Engine.ENGINE_SF19_NNUE = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ENGINE_SF19_NNUE = 14;

### Evidence

- **SRC-0331** `research/proto/chesscom/engine/v1/engine.proto` — [preserved redacted evidence](../evidence/text/2480569492b7d8f22a378b3fadc58c7666edfe9083321d9adb6ecef5411409aa.proto)
  Character offset 448.

```text
GINE_SF16_1_NNUE = 10;
  ENGINE_TORCH_3 = 11;
  ENGINE_TORCH_HUMAN = 12;
  ENGINE_SF18_NNUE = 13;
  ENGINE_SF19_NNUE = 14;
}

```

**Source references:** SRC-0331, SRC-1302  
**URL references:** None independently associated  
**Related findings:** FND-02493, FND-02494, FND-02495

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02509"></a>
## FND-02509: message declaration: chesscom.engine.v1.Evaluation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Evaluation {

### Evidence

- **SRC-0332** `research/proto/chesscom/engine/v1/evaluation.proto` — [preserved redacted evidence](../evidence/text/aff6ef3d194f500593d1a7aeeae9197c12698c24cc0a97b18ea30ef17ee0dcfa.proto)
  Character offset 95.

```text
// source: chesscom/engine/v1/evaluation.proto
// syntax: proto3

package chesscom.engine.v1;

message Evaluation {
  optional .chesscom.engine.v1.Score score = 1;
  repeated .chesscom.chess.v1.Move variation = 2;
}

```

**Source references:** SRC-0332, SRC-1303  
**URL references:** None independently associated  
**Related findings:** FND-02510, FND-02511

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02510"></a>
## FND-02510: chesscom.engine.v1.Evaluation.score = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.engine.v1.Score score = 1;

### Evidence

- **SRC-0332** `research/proto/chesscom/engine/v1/evaluation.proto` — [preserved redacted evidence](../evidence/text/aff6ef3d194f500593d1a7aeeae9197c12698c24cc0a97b18ea30ef17ee0dcfa.proto)
  Character offset 118.

```text
m/engine/v1/evaluation.proto
// syntax: proto3

package chesscom.engine.v1;

message Evaluation {
  optional .chesscom.engine.v1.Score score = 1;
  repeated .chesscom.chess.v1.Move variation = 2;
}

```

**Source references:** SRC-0332, SRC-1303  
**URL references:** None independently associated  
**Related findings:** FND-02509, FND-02511

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02511"></a>
## FND-02511: chesscom.engine.v1.Evaluation.variation = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.chess.v1.Move variation = 2;

### Evidence

- **SRC-0332** `research/proto/chesscom/engine/v1/evaluation.proto` — [preserved redacted evidence](../evidence/text/aff6ef3d194f500593d1a7aeeae9197c12698c24cc0a97b18ea30ef17ee0dcfa.proto)
  Character offset 166.

```text
package chesscom.engine.v1;

message Evaluation {
  optional .chesscom.engine.v1.Score score = 1;
  repeated .chesscom.chess.v1.Move variation = 2;
}

```

**Source references:** SRC-0332, SRC-1303  
**URL references:** None independently associated  
**Related findings:** FND-02509, FND-02510

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02512"></a>
## FND-02512: message declaration: chesscom.engine.v1.Score

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Score {

### Evidence

- **SRC-0333** `research/proto/chesscom/engine/v1/score.proto` — [preserved redacted evidence](../evidence/text/d1e0f97361f8d27b21eaaf65030e3540ec7c93bd9eb7f75f1904a222b96d75bd.proto)
  Character offset 90.

```text
// source: chesscom/engine/v1/score.proto
// syntax: proto3

package chesscom.engine.v1;

message Score {
  oneof _strength {
  .chesscom.engine.v1.Strength strength = 5;
  }
  optional .chesscom.chess.v1.Score score = 1;
  optional int32 depth = 2;
  optional int64 nodes = 6;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional int32 variation = 4;
}

```

**Source references:** SRC-0333, SRC-1304  
**URL references:** None independently associated  
**Related findings:** FND-02513, FND-02514

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02513"></a>
## FND-02513: oneof declaration: chesscom.engine.v1.Score._strength

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _strength {

### Evidence

- **SRC-0333** `research/proto/chesscom/engine/v1/score.proto` — [preserved redacted evidence](../evidence/text/d1e0f97361f8d27b21eaaf65030e3540ec7c93bd9eb7f75f1904a222b96d75bd.proto)
  Character offset 108.

```text
e: chesscom/engine/v1/score.proto
// syntax: proto3

package chesscom.engine.v1;

message Score {
  oneof _strength {
  .chesscom.engine.v1.Strength strength = 5;
  }
  optional .chesscom.chess.v1.Score score = 1;
  optional int32 depth = 2;
  optional int64 nodes = 6;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional int32 variation = 4;
}

```

**Source references:** SRC-0333, SRC-1304  
**URL references:** None independently associated  
**Related findings:** FND-02512, FND-02514

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02514"></a>
## FND-02514: chesscom.engine.v1.Score.strength = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.engine.v1.Strength strength = 5;

### Evidence

- **SRC-0333** `research/proto/chesscom/engine/v1/score.proto` — [preserved redacted evidence](../evidence/text/d1e0f97361f8d27b21eaaf65030e3540ec7c93bd9eb7f75f1904a222b96d75bd.proto)
  Character offset 128.

```text
1/score.proto
// syntax: proto3

package chesscom.engine.v1;

message Score {
  oneof _strength {
  .chesscom.engine.v1.Strength strength = 5;
  }
  optional .chesscom.chess.v1.Score score = 1;
  optional int32 depth = 2;
  optional int64 nodes = 6;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional int32 variation = 4;
}

```

**Source references:** SRC-0333, SRC-1304  
**URL references:** None independently associated  
**Related findings:** FND-02512, FND-02513

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02515"></a>
## FND-02515: chesscom.engine.v1.Score.score = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Score score = 1;

### Evidence

- **SRC-0333** `research/proto/chesscom/engine/v1/score.proto` — [preserved redacted evidence](../evidence/text/d1e0f97361f8d27b21eaaf65030e3540ec7c93bd9eb7f75f1904a222b96d75bd.proto)
  Character offset 177.

```text
.engine.v1;

message Score {
  oneof _strength {
  .chesscom.engine.v1.Strength strength = 5;
  }
  optional .chesscom.chess.v1.Score score = 1;
  optional int32 depth = 2;
  optional int64 nodes = 6;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional int32 variation = 4;
}

```

**Source references:** SRC-0333, SRC-1304  
**URL references:** None independently associated  
**Related findings:** FND-02512, FND-02513, FND-02514

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02516"></a>
## FND-02516: chesscom.engine.v1.Score.depth = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 depth = 2;

### Evidence

- **SRC-0333** `research/proto/chesscom/engine/v1/score.proto` — [preserved redacted evidence](../evidence/text/d1e0f97361f8d27b21eaaf65030e3540ec7c93bd9eb7f75f1904a222b96d75bd.proto)
  Character offset 224.

```text
{
  .chesscom.engine.v1.Strength strength = 5;
  }
  optional .chesscom.chess.v1.Score score = 1;
  optional int32 depth = 2;
  optional int64 nodes = 6;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional int32 variation = 4;
}

```

**Source references:** SRC-0333, SRC-1304  
**URL references:** None independently associated  
**Related findings:** FND-02512, FND-02513, FND-02514

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02517"></a>
## FND-02517: chesscom.engine.v1.Score.nodes = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 nodes = 6;

### Evidence

- **SRC-0333** `research/proto/chesscom/engine/v1/score.proto` — [preserved redacted evidence](../evidence/text/d1e0f97361f8d27b21eaaf65030e3540ec7c93bd9eb7f75f1904a222b96d75bd.proto)
  Character offset 252.

```text
ngth strength = 5;
  }
  optional .chesscom.chess.v1.Score score = 1;
  optional int32 depth = 2;
  optional int64 nodes = 6;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional int32 variation = 4;
}

```

**Source references:** SRC-0333, SRC-1304  
**URL references:** None independently associated  
**Related findings:** FND-02512, FND-02513, FND-02514

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02518"></a>
## FND-02518: chesscom.engine.v1.Score.engine = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.engine.v1.Engine engine = 3;

### Evidence

- **SRC-0333** `research/proto/chesscom/engine/v1/score.proto` — [preserved redacted evidence](../evidence/text/d1e0f97361f8d27b21eaaf65030e3540ec7c93bd9eb7f75f1904a222b96d75bd.proto)
  Character offset 280.

```text
ional .chesscom.chess.v1.Score score = 1;
  optional int32 depth = 2;
  optional int64 nodes = 6;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional int32 variation = 4;
}

```

**Source references:** SRC-0333, SRC-1304  
**URL references:** None independently associated  
**Related findings:** FND-02512, FND-02513, FND-02514

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02519"></a>
## FND-02519: chesscom.engine.v1.Score.variation = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 variation = 4;

### Evidence

- **SRC-0333** `research/proto/chesscom/engine/v1/score.proto` — [preserved redacted evidence](../evidence/text/d1e0f97361f8d27b21eaaf65030e3540ec7c93bd9eb7f75f1904a222b96d75bd.proto)
  Character offset 330.

```text
al int32 depth = 2;
  optional int64 nodes = 6;
  optional .chesscom.engine.v1.Engine engine = 3;
  optional int32 variation = 4;
}

```

**Source references:** SRC-0333, SRC-1304  
**URL references:** None independently associated  
**Related findings:** FND-02512, FND-02513, FND-02514

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02520"></a>
## FND-02520: enum declaration: chesscom.engine.v1.Strength

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Strength {

### Evidence

- **SRC-0334** `research/proto/chesscom/engine/v1/strength.proto` — [preserved redacted evidence](../evidence/text/f0ea702032bf270096aea4a69dc474d0d4f5e606859f45fd3430db4183ecf398.proto)
  Character offset 93.

```text
// source: chesscom/engine/v1/strength.proto
// syntax: proto3

package chesscom.engine.v1;

enum Strength {
  STRENGTH_UNSPECIFIED = 0;
  STRENGTH_FAST = 1;
  STRENGTH_STANDARD = 2;
  STRENGTH_DEEP = 3;
  STRENGTH_MAXIMUM = 4;
}

```

**Source references:** SRC-0334, SRC-1305  
**URL references:** None independently associated  
**Related findings:** FND-02521, FND-02522

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02521"></a>
## FND-02521: chesscom.engine.v1.Strength.STRENGTH_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STRENGTH_UNSPECIFIED = 0;

### Evidence

- **SRC-0334** `research/proto/chesscom/engine/v1/strength.proto` — [preserved redacted evidence](../evidence/text/f0ea702032bf270096aea4a69dc474d0d4f5e606859f45fd3430db4183ecf398.proto)
  Character offset 111.

```text
chesscom/engine/v1/strength.proto
// syntax: proto3

package chesscom.engine.v1;

enum Strength {
  STRENGTH_UNSPECIFIED = 0;
  STRENGTH_FAST = 1;
  STRENGTH_STANDARD = 2;
  STRENGTH_DEEP = 3;
  STRENGTH_MAXIMUM = 4;
}

```

**Source references:** SRC-0334, SRC-1305  
**URL references:** None independently associated  
**Related findings:** FND-02520, FND-02522

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02522"></a>
## FND-02522: chesscom.engine.v1.Strength.STRENGTH_FAST = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STRENGTH_FAST = 1;

### Evidence

- **SRC-0334** `research/proto/chesscom/engine/v1/strength.proto` — [preserved redacted evidence](../evidence/text/f0ea702032bf270096aea4a69dc474d0d4f5e606859f45fd3430db4183ecf398.proto)
  Character offset 139.

```text
proto
// syntax: proto3

package chesscom.engine.v1;

enum Strength {
  STRENGTH_UNSPECIFIED = 0;
  STRENGTH_FAST = 1;
  STRENGTH_STANDARD = 2;
  STRENGTH_DEEP = 3;
  STRENGTH_MAXIMUM = 4;
}

```

**Source references:** SRC-0334, SRC-1305  
**URL references:** None independently associated  
**Related findings:** FND-02520, FND-02521

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02523"></a>
## FND-02523: chesscom.engine.v1.Strength.STRENGTH_STANDARD = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STRENGTH_STANDARD = 2;

### Evidence

- **SRC-0334** `research/proto/chesscom/engine/v1/strength.proto` — [preserved redacted evidence](../evidence/text/f0ea702032bf270096aea4a69dc474d0d4f5e606859f45fd3430db4183ecf398.proto)
  Character offset 160.

```text
o3

package chesscom.engine.v1;

enum Strength {
  STRENGTH_UNSPECIFIED = 0;
  STRENGTH_FAST = 1;
  STRENGTH_STANDARD = 2;
  STRENGTH_DEEP = 3;
  STRENGTH_MAXIMUM = 4;
}

```

**Source references:** SRC-0334, SRC-1305  
**URL references:** None independently associated  
**Related findings:** FND-02520, FND-02521, FND-02522

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02524"></a>
## FND-02524: chesscom.engine.v1.Strength.STRENGTH_DEEP = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STRENGTH_DEEP = 3;

### Evidence

- **SRC-0334** `research/proto/chesscom/engine/v1/strength.proto` — [preserved redacted evidence](../evidence/text/f0ea702032bf270096aea4a69dc474d0d4f5e606859f45fd3430db4183ecf398.proto)
  Character offset 185.

```text
ne.v1;

enum Strength {
  STRENGTH_UNSPECIFIED = 0;
  STRENGTH_FAST = 1;
  STRENGTH_STANDARD = 2;
  STRENGTH_DEEP = 3;
  STRENGTH_MAXIMUM = 4;
}

```

**Source references:** SRC-0334, SRC-1305  
**URL references:** None independently associated  
**Related findings:** FND-02520, FND-02521, FND-02522

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02525"></a>
## FND-02525: chesscom.engine.v1.Strength.STRENGTH_MAXIMUM = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

STRENGTH_MAXIMUM = 4;

### Evidence

- **SRC-0334** `research/proto/chesscom/engine/v1/strength.proto` — [preserved redacted evidence](../evidence/text/f0ea702032bf270096aea4a69dc474d0d4f5e606859f45fd3430db4183ecf398.proto)
  Character offset 206.

```text
 {
  STRENGTH_UNSPECIFIED = 0;
  STRENGTH_FAST = 1;
  STRENGTH_STANDARD = 2;
  STRENGTH_DEEP = 3;
  STRENGTH_MAXIMUM = 4;
}

```

**Source references:** SRC-0334, SRC-1305  
**URL references:** None independently associated  
**Related findings:** FND-02520, FND-02521, FND-02522

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02526"></a>
## FND-02526: enum declaration: chesscom.explanation_engine.v1.AccuracyAlgorithm

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum AccuracyAlgorithm {

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 117.

```text
om/explanation_engine/v1/accuracy.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum AccuracyAlgorithm {
  ACCURACY_ALGORITHM_UNSPECIFIED = 0;
  ACCURACY_ALGORITHM_CAPS2 = 1;
}

message PieceTypeAccuracy {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double accuracy_score = 2;
}

message GamePhaseAccuracy {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional do
```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02527, FND-02528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02527"></a>
## FND-02527: chesscom.explanation_engine.v1.AccuracyAlgorithm.ACCURACY_ALGORITHM_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ACCURACY_ALGORITHM_UNSPECIFIED = 0;

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 144.

```text
curacy.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum AccuracyAlgorithm {
  ACCURACY_ALGORITHM_UNSPECIFIED = 0;
  ACCURACY_ALGORITHM_CAPS2 = 1;
}

message PieceTypeAccuracy {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double accuracy_score = 2;
}

message GamePhaseAccuracy {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional double accuracy_score = 2;
}

```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02528"></a>
## FND-02528: chesscom.explanation_engine.v1.AccuracyAlgorithm.ACCURACY_ALGORITHM_CAPS2 = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ACCURACY_ALGORITHM_CAPS2 = 1;

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 182.

```text
e chesscom.explanation_engine.v1;

enum AccuracyAlgorithm {
  ACCURACY_ALGORITHM_UNSPECIFIED = 0;
  ACCURACY_ALGORITHM_CAPS2 = 1;
}

message PieceTypeAccuracy {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double accuracy_score = 2;
}

message GamePhaseAccuracy {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional double accuracy_score = 2;
}

message ColorAccuracy {
  optional .c
```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02529"></a>
## FND-02529: message declaration: chesscom.explanation_engine.v1.PieceTypeAccuracy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PieceTypeAccuracy {

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 215.

```text


enum AccuracyAlgorithm {
  ACCURACY_ALGORITHM_UNSPECIFIED = 0;
  ACCURACY_ALGORITHM_CAPS2 = 1;
}

message PieceTypeAccuracy {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double accuracy_score = 2;
}

message GamePhaseAccuracy {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional double accuracy_score = 2;
}

message ColorAccuracy {
  optional .chesscom.chess.v1.Color color = 1;
```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02530"></a>
## FND-02530: chesscom.explanation_engine.v1.PieceTypeAccuracy.piece_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.PieceType piece_type = 1;

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 245.

```text
CCURACY_ALGORITHM_UNSPECIFIED = 0;
  ACCURACY_ALGORITHM_CAPS2 = 1;
}

message PieceTypeAccuracy {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double accuracy_score = 2;
}

message GamePhaseAccuracy {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional double accuracy_score = 2;
}

message ColorAccuracy {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanat
```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02531"></a>
## FND-02531: chesscom.explanation_engine.v1.PieceTypeAccuracy.accuracy_score = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double accuracy_score = 2;

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 301.

```text
CAPS2 = 1;
}

message PieceTypeAccuracy {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double accuracy_score = 2;
}

message GamePhaseAccuracy {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional double accuracy_score = 2;
}

message ColorAccuracy {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.PieceTypeAccuracy accuracy_by_piece_type =
```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02532"></a>
## FND-02532: message declaration: chesscom.explanation_engine.v1.GamePhaseAccuracy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GamePhaseAccuracy {

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 340.

```text
 {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double accuracy_score = 2;
}

message GamePhaseAccuracy {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional double accuracy_score = 2;
}

message ColorAccuracy {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.PieceTypeAccuracy accuracy_by_piece_type = 2;
  repeated .chesscom.explanation_en
```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02533"></a>
## FND-02533: chesscom.explanation_engine.v1.GamePhaseAccuracy.game_phase = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.GamePhase game_phase = 1;

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 370.

```text
v1.PieceType piece_type = 1;
  optional double accuracy_score = 2;
}

message GamePhaseAccuracy {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional double accuracy_score = 2;
}

message ColorAccuracy {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.PieceTypeAccuracy accuracy_by_piece_type = 2;
  repeated .chesscom.explanation_engine.v1.GamePhaseAccuracy accu
```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02534"></a>
## FND-02534: chesscom.explanation_engine.v1.GamePhaseAccuracy.accuracy_score = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double accuracy_score = 2;

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 301.

```text
CAPS2 = 1;
}

message PieceTypeAccuracy {
  optional .chesscom.chess.v1.PieceType piece_type = 1;
  optional double accuracy_score = 2;
}

message GamePhaseAccuracy {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional double accuracy_score = 2;
}

message ColorAccuracy {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.PieceTypeAccuracy accuracy_by_piece_type =
```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02535"></a>
## FND-02535: message declaration: chesscom.explanation_engine.v1.ColorAccuracy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ColorAccuracy {

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 465.

```text
 {
  optional .chesscom.chess.v1.GamePhase game_phase = 1;
  optional double accuracy_score = 2;
}

message ColorAccuracy {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.PieceTypeAccuracy accuracy_by_piece_type = 2;
  repeated .chesscom.explanation_engine.v1.GamePhaseAccuracy accuracy_by_game_phase = 3;
  optional double accuracy_overall = 4;
  optional double avg_centipawn
```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02536"></a>
## FND-02536: chesscom.explanation_engine.v1.ColorAccuracy.color = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Color color = 1;

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 491.

```text
ess.v1.GamePhase game_phase = 1;
  optional double accuracy_score = 2;
}

message ColorAccuracy {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.PieceTypeAccuracy accuracy_by_piece_type = 2;
  repeated .chesscom.explanation_engine.v1.GamePhaseAccuracy accuracy_by_game_phase = 3;
  optional double accuracy_overall = 4;
  optional double avg_centipawn_loss = 5;
}

message Vari
```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02537"></a>
## FND-02537: chesscom.explanation_engine.v1.ColorAccuracy.accuracy_by_piece_type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.PieceTypeAccuracy accuracy_by_piece_type = 2;

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 538.

```text
ble accuracy_score = 2;
}

message ColorAccuracy {
  optional .chesscom.chess.v1.Color color = 1;
  repeated .chesscom.explanation_engine.v1.PieceTypeAccuracy accuracy_by_piece_type = 2;
  repeated .chesscom.explanation_engine.v1.GamePhaseAccuracy accuracy_by_game_phase = 3;
  optional double accuracy_overall = 4;
  optional double avg_centipawn_loss = 5;
}

message VariationAccuracy {
  repeated .chesscom.explanatio
```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02538"></a>
## FND-02538: chesscom.explanation_engine.v1.ColorAccuracy.accuracy_by_game_phase = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.GamePhaseAccuracy accuracy_by_game_phase = 3;

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 627.

```text
lor = 1;
  repeated .chesscom.explanation_engine.v1.PieceTypeAccuracy accuracy_by_piece_type = 2;
  repeated .chesscom.explanation_engine.v1.GamePhaseAccuracy accuracy_by_game_phase = 3;
  optional double accuracy_overall = 4;
  optional double avg_centipawn_loss = 5;
}

message VariationAccuracy {
  repeated .chesscom.explanation_engine.v1.ColorAccuracy accuracy_by_color = 1;
}

```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02539"></a>
## FND-02539: chesscom.explanation_engine.v1.ColorAccuracy.accuracy_overall = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double accuracy_overall = 4;

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 716.

```text
ype = 2;
  repeated .chesscom.explanation_engine.v1.GamePhaseAccuracy accuracy_by_game_phase = 3;
  optional double accuracy_overall = 4;
  optional double avg_centipawn_loss = 5;
}

message VariationAccuracy {
  repeated .chesscom.explanation_engine.v1.ColorAccuracy accuracy_by_color = 1;
}

```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02540"></a>
## FND-02540: chesscom.explanation_engine.v1.ColorAccuracy.avg_centipawn_loss = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional double avg_centipawn_loss = 5;

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 756.

```text
n_engine.v1.GamePhaseAccuracy accuracy_by_game_phase = 3;
  optional double accuracy_overall = 4;
  optional double avg_centipawn_loss = 5;
}

message VariationAccuracy {
  repeated .chesscom.explanation_engine.v1.ColorAccuracy accuracy_by_color = 1;
}

```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02541"></a>
## FND-02541: message declaration: chesscom.explanation_engine.v1.VariationAccuracy

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message VariationAccuracy {

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 799.

```text
ame_phase = 3;
  optional double accuracy_overall = 4;
  optional double avg_centipawn_loss = 5;
}

message VariationAccuracy {
  repeated .chesscom.explanation_engine.v1.ColorAccuracy accuracy_by_color = 1;
}

```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02542"></a>
## FND-02542: chesscom.explanation_engine.v1.VariationAccuracy.accuracy_by_color = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.ColorAccuracy accuracy_by_color = 1;

### Evidence

- **SRC-0335** `research/proto/chesscom/explanation_engine/v1/accuracy.proto` — [preserved redacted evidence](../evidence/text/5d38bd8bef9cb9241bee82c028296b05a713c547ec59fda94b2050476123d958.proto)
  Character offset 829.

```text
le accuracy_overall = 4;
  optional double avg_centipawn_loss = 5;
}

message VariationAccuracy {
  repeated .chesscom.explanation_engine.v1.ColorAccuracy accuracy_by_color = 1;
}

```

**Source references:** SRC-0335, SRC-1306  
**URL references:** None independently associated  
**Related findings:** FND-02526, FND-02527, FND-02528

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02543"></a>
## FND-02543: enum declaration: chesscom.explanation_engine.v1.AnalysisType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum AnalysisType {

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 122.

```text
planation_engine/v1/analysis_type.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum AnalysisType {
  ANALYSIS_TYPE_UNSPECIFIED = 0;
  ANALYSIS_TYPE_STALEMATE = 1;
  ANALYSIS_TYPE_FIFTY_MOVE = 2;
  ANALYSIS_TYPE_REPETITION = 3;
  ANALYSIS_TYPE_INSUFFICIENT = 4;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE = 5;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE = 6;
  ANALYSIS_TYPE_IGNORES_THREAT = 7;
  ANALYSIS
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02544"></a>
## FND-02544: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 144.

```text
alysis_type.proto
// syntax: proto3

package chesscom.explanation_engine.v1;

enum AnalysisType {
  ANALYSIS_TYPE_UNSPECIFIED = 0;
  ANALYSIS_TYPE_STALEMATE = 1;
  ANALYSIS_TYPE_FIFTY_MOVE = 2;
  ANALYSIS_TYPE_REPETITION = 3;
  ANALYSIS_TYPE_INSUFFICIENT = 4;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE = 5;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE = 6;
  ANALYSIS_TYPE_IGNORES_THREAT = 7;
  ANALYSIS_TYPE_INDIRECT_SACRIFI
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02545"></a>
## FND-02545: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_STALEMATE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_STALEMATE = 1;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 177.

```text
o3

package chesscom.explanation_engine.v1;

enum AnalysisType {
  ANALYSIS_TYPE_UNSPECIFIED = 0;
  ANALYSIS_TYPE_STALEMATE = 1;
  ANALYSIS_TYPE_FIFTY_MOVE = 2;
  ANALYSIS_TYPE_REPETITION = 3;
  ANALYSIS_TYPE_INSUFFICIENT = 4;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE = 5;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE = 6;
  ANALYSIS_TYPE_IGNORES_THREAT = 7;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE = 8;
  ANALYSIS_TYPE_CHECKMATE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02546"></a>
## FND-02546: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FIFTY_MOVE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FIFTY_MOVE = 2;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 208.

```text
n_engine.v1;

enum AnalysisType {
  ANALYSIS_TYPE_UNSPECIFIED = 0;
  ANALYSIS_TYPE_STALEMATE = 1;
  ANALYSIS_TYPE_FIFTY_MOVE = 2;
  ANALYSIS_TYPE_REPETITION = 3;
  ANALYSIS_TYPE_INSUFFICIENT = 4;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE = 5;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE = 6;
  ANALYSIS_TYPE_IGNORES_THREAT = 7;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE = 8;
  ANALYSIS_TYPE_CHECKMATE = 9;
  ANALYSIS_TYPE_FORCES_MA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02547"></a>
## FND-02547: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_REPETITION = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_REPETITION = 3;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 240.

```text
{
  ANALYSIS_TYPE_UNSPECIFIED = 0;
  ANALYSIS_TYPE_STALEMATE = 1;
  ANALYSIS_TYPE_FIFTY_MOVE = 2;
  ANALYSIS_TYPE_REPETITION = 3;
  ANALYSIS_TYPE_INSUFFICIENT = 4;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE = 5;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE = 6;
  ANALYSIS_TYPE_IGNORES_THREAT = 7;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE = 8;
  ANALYSIS_TYPE_CHECKMATE = 9;
  ANALYSIS_TYPE_FORCES_MATE = 11;
  ANALYSIS_TYPE_KEYMOME
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02548"></a>
## FND-02548: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_INSUFFICIENT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_INSUFFICIENT = 4;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 272.

```text
0;
  ANALYSIS_TYPE_STALEMATE = 1;
  ANALYSIS_TYPE_FIFTY_MOVE = 2;
  ANALYSIS_TYPE_REPETITION = 3;
  ANALYSIS_TYPE_INSUFFICIENT = 4;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE = 5;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE = 6;
  ANALYSIS_TYPE_IGNORES_THREAT = 7;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE = 8;
  ANALYSIS_TYPE_CHECKMATE = 9;
  ANALYSIS_TYPE_FORCES_MATE = 11;
  ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE = 12;
  ANAL
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02549"></a>
## FND-02549: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE = 5;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 306.

```text
  ANALYSIS_TYPE_FIFTY_MOVE = 2;
  ANALYSIS_TYPE_REPETITION = 3;
  ANALYSIS_TYPE_INSUFFICIENT = 4;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE = 5;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE = 6;
  ANALYSIS_TYPE_IGNORES_THREAT = 7;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE = 8;
  ANALYSIS_TYPE_CHECKMATE = 9;
  ANALYSIS_TYPE_FORCES_MATE = 11;
  ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE = 12;
  ANALYSIS_TYPE_SLOWER_MATE = 14;
  ANAL
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02550"></a>
## FND-02550: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE = 6;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 352.

```text
E_REPETITION = 3;
  ANALYSIS_TYPE_INSUFFICIENT = 4;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE = 5;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE = 6;
  ANALYSIS_TYPE_IGNORES_THREAT = 7;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE = 8;
  ANALYSIS_TYPE_CHECKMATE = 9;
  ANALYSIS_TYPE_FORCES_MATE = 11;
  ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE = 12;
  ANALYSIS_TYPE_SLOWER_MATE = 14;
  ANALYSIS_TYPE_STILL_MATE = 15;
  ANALYSIS_TYPE_MAT
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02551"></a>
## FND-02551: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_IGNORES_THREAT = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_IGNORES_THREAT = 7;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 398.

```text
 = 4;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_CAPTURE = 5;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE = 6;
  ANALYSIS_TYPE_IGNORES_THREAT = 7;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE = 8;
  ANALYSIS_TYPE_CHECKMATE = 9;
  ANALYSIS_TYPE_FORCES_MATE = 11;
  ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE = 12;
  ANALYSIS_TYPE_SLOWER_MATE = 14;
  ANALYSIS_TYPE_STILL_MATE = 15;
  ANALYSIS_TYPE_MATE_THREAT = 16;
  ANALYSIS_TYPE_INTERESTING = 1
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02552"></a>
## FND-02552: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_INDIRECT_SACRIFICE = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_INDIRECT_SACRIFICE = 8;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 434.

```text
CE_CAPTURE = 5;
  ANALYSIS_TYPE_DIRECT_SACRIFICE_ENPRISE = 6;
  ANALYSIS_TYPE_IGNORES_THREAT = 7;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE = 8;
  ANALYSIS_TYPE_CHECKMATE = 9;
  ANALYSIS_TYPE_FORCES_MATE = 11;
  ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE = 12;
  ANALYSIS_TYPE_SLOWER_MATE = 14;
  ANALYSIS_TYPE_STILL_MATE = 15;
  ANALYSIS_TYPE_MATE_THREAT = 16;
  ANALYSIS_TYPE_INTERESTING = 17;
  ANALYSIS_TYPE_FREE_PIECE = 18;

```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02553"></a>
## FND-02553: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CHECKMATE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CHECKMATE = 9;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 474.

```text
ACRIFICE_ENPRISE = 6;
  ANALYSIS_TYPE_IGNORES_THREAT = 7;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE = 8;
  ANALYSIS_TYPE_CHECKMATE = 9;
  ANALYSIS_TYPE_FORCES_MATE = 11;
  ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE = 12;
  ANALYSIS_TYPE_SLOWER_MATE = 14;
  ANALYSIS_TYPE_STILL_MATE = 15;
  ANALYSIS_TYPE_MATE_THREAT = 16;
  ANALYSIS_TYPE_INTERESTING = 17;
  ANALYSIS_TYPE_FREE_PIECE = 18;
  ANALYSIS_TYPE_QUASI_FREE_PIECE = 19;
 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02554"></a>
## FND-02554: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORCES_MATE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FORCES_MATE = 11;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 505.

```text
S_TYPE_IGNORES_THREAT = 7;
  ANALYSIS_TYPE_INDIRECT_SACRIFICE = 8;
  ANALYSIS_TYPE_CHECKMATE = 9;
  ANALYSIS_TYPE_FORCES_MATE = 11;
  ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE = 12;
  ANALYSIS_TYPE_SLOWER_MATE = 14;
  ANALYSIS_TYPE_STILL_MATE = 15;
  ANALYSIS_TYPE_MATE_THREAT = 16;
  ANALYSIS_TYPE_INTERESTING = 17;
  ANALYSIS_TYPE_FREE_PIECE = 18;
  ANALYSIS_TYPE_QUASI_FREE_PIECE = 19;
  ANALYSIS_TYPE_DISCOVERED_ATTAC
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02555"></a>
## FND-02555: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE = 12;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 539.

```text
SIS_TYPE_INDIRECT_SACRIFICE = 8;
  ANALYSIS_TYPE_CHECKMATE = 9;
  ANALYSIS_TYPE_FORCES_MATE = 11;
  ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE = 12;
  ANALYSIS_TYPE_SLOWER_MATE = 14;
  ANALYSIS_TYPE_STILL_MATE = 15;
  ANALYSIS_TYPE_MATE_THREAT = 16;
  ANALYSIS_TYPE_INTERESTING = 17;
  ANALYSIS_TYPE_FREE_PIECE = 18;
  ANALYSIS_TYPE_QUASI_FREE_PIECE = 19;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK = 20;
  ANALYSIS_TYPE_FORK
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02556"></a>
## FND-02556: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_SLOWER_MATE = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_SLOWER_MATE = 14;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 588.

```text
CHECKMATE = 9;
  ANALYSIS_TYPE_FORCES_MATE = 11;
  ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE = 12;
  ANALYSIS_TYPE_SLOWER_MATE = 14;
  ANALYSIS_TYPE_STILL_MATE = 15;
  ANALYSIS_TYPE_MATE_THREAT = 16;
  ANALYSIS_TYPE_INTERESTING = 17;
  ANALYSIS_TYPE_FREE_PIECE = 18;
  ANALYSIS_TYPE_QUASI_FREE_PIECE = 19;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK = 20;
  ANALYSIS_TYPE_FORK_WITH_MATE = 21;
  ANALYSIS_TYPE_FORK = 22;
  ANA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02557"></a>
## FND-02557: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_STILL_MATE = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_STILL_MATE = 15;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 622.

```text
CES_MATE = 11;
  ANALYSIS_TYPE_KEYMOMENT_GOOD_FASTER_MATE = 12;
  ANALYSIS_TYPE_SLOWER_MATE = 14;
  ANALYSIS_TYPE_STILL_MATE = 15;
  ANALYSIS_TYPE_MATE_THREAT = 16;
  ANALYSIS_TYPE_INTERESTING = 17;
  ANALYSIS_TYPE_FREE_PIECE = 18;
  ANALYSIS_TYPE_QUASI_FREE_PIECE = 19;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK = 20;
  ANALYSIS_TYPE_FORK_WITH_MATE = 21;
  ANALYSIS_TYPE_FORK = 22;
  ANALYSIS_TYPE_MULTI_ATTACK = 23;
  AN
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02558"></a>
## FND-02558: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MATE_THREAT = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_MATE_THREAT = 16;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 655.

```text
YMOMENT_GOOD_FASTER_MATE = 12;
  ANALYSIS_TYPE_SLOWER_MATE = 14;
  ANALYSIS_TYPE_STILL_MATE = 15;
  ANALYSIS_TYPE_MATE_THREAT = 16;
  ANALYSIS_TYPE_INTERESTING = 17;
  ANALYSIS_TYPE_FREE_PIECE = 18;
  ANALYSIS_TYPE_QUASI_FREE_PIECE = 19;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK = 20;
  ANALYSIS_TYPE_FORK_WITH_MATE = 21;
  ANALYSIS_TYPE_FORK = 22;
  ANALYSIS_TYPE_MULTI_ATTACK = 23;
  ANALYSIS_TYPE_SKEWER = 24;
  ANALYS
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02559"></a>
## FND-02559: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_INTERESTING = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_INTERESTING = 17;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 689.

```text
NALYSIS_TYPE_SLOWER_MATE = 14;
  ANALYSIS_TYPE_STILL_MATE = 15;
  ANALYSIS_TYPE_MATE_THREAT = 16;
  ANALYSIS_TYPE_INTERESTING = 17;
  ANALYSIS_TYPE_FREE_PIECE = 18;
  ANALYSIS_TYPE_QUASI_FREE_PIECE = 19;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK = 20;
  ANALYSIS_TYPE_FORK_WITH_MATE = 21;
  ANALYSIS_TYPE_FORK = 22;
  ANALYSIS_TYPE_MULTI_ATTACK = 23;
  ANALYSIS_TYPE_SKEWER = 24;
  ANALYSIS_TYPE_DOUBLE_CHECK = 25;
  ANALY
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02560"></a>
## FND-02560: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FREE_PIECE = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FREE_PIECE = 18;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 723.

```text
NALYSIS_TYPE_STILL_MATE = 15;
  ANALYSIS_TYPE_MATE_THREAT = 16;
  ANALYSIS_TYPE_INTERESTING = 17;
  ANALYSIS_TYPE_FREE_PIECE = 18;
  ANALYSIS_TYPE_QUASI_FREE_PIECE = 19;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK = 20;
  ANALYSIS_TYPE_FORK_WITH_MATE = 21;
  ANALYSIS_TYPE_FORK = 22;
  ANALYSIS_TYPE_MULTI_ATTACK = 23;
  ANALYSIS_TYPE_SKEWER = 24;
  ANALYSIS_TYPE_DOUBLE_CHECK = 25;
  ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_T
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02561"></a>
## FND-02561: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_QUASI_FREE_PIECE = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_QUASI_FREE_PIECE = 19;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 756.

```text
NALYSIS_TYPE_MATE_THREAT = 16;
  ANALYSIS_TYPE_INTERESTING = 17;
  ANALYSIS_TYPE_FREE_PIECE = 18;
  ANALYSIS_TYPE_QUASI_FREE_PIECE = 19;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK = 20;
  ANALYSIS_TYPE_FORK_WITH_MATE = 21;
  ANALYSIS_TYPE_FORK = 22;
  ANALYSIS_TYPE_MULTI_ATTACK = 23;
  ANALYSIS_TYPE_SKEWER = 24;
  ANALYSIS_TYPE_DOUBLE_CHECK = 25;
  ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT = 26;
  ANALYSIS_TYPE_DISCO
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02562"></a>
## FND-02562: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK = 20;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 795.

```text
IS_TYPE_INTERESTING = 17;
  ANALYSIS_TYPE_FREE_PIECE = 18;
  ANALYSIS_TYPE_QUASI_FREE_PIECE = 19;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK = 20;
  ANALYSIS_TYPE_FORK_WITH_MATE = 21;
  ANALYSIS_TYPE_FORK = 22;
  ANALYSIS_TYPE_MULTI_ATTACK = 23;
  ANALYSIS_TYPE_SKEWER = 24;
  ANALYSIS_TYPE_DOUBLE_CHECK = 25;
  ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT = 26;
  ANALYSIS_TYPE_DISCOVERED_ATTACK = 27;
  ANALYSIS_TYPE_PROM
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02563"></a>
## FND-02563: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORK_WITH_MATE = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FORK_WITH_MATE = 21;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 841.

```text
_PIECE = 18;
  ANALYSIS_TYPE_QUASI_FREE_PIECE = 19;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK = 20;
  ANALYSIS_TYPE_FORK_WITH_MATE = 21;
  ANALYSIS_TYPE_FORK = 22;
  ANALYSIS_TYPE_MULTI_ATTACK = 23;
  ANALYSIS_TYPE_SKEWER = 24;
  ANALYSIS_TYPE_DOUBLE_CHECK = 25;
  ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT = 26;
  ANALYSIS_TYPE_DISCOVERED_ATTACK = 27;
  ANALYSIS_TYPE_PROMOTION = 28;
  ANALYSIS_TYPE_DISCOVERED_CHECK =
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02564"></a>
## FND-02564: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORK = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FORK = 22;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 878.

```text
EE_PIECE = 19;
  ANALYSIS_TYPE_DISCOVERED_ATTACK_CHECK = 20;
  ANALYSIS_TYPE_FORK_WITH_MATE = 21;
  ANALYSIS_TYPE_FORK = 22;
  ANALYSIS_TYPE_MULTI_ATTACK = 23;
  ANALYSIS_TYPE_SKEWER = 24;
  ANALYSIS_TYPE_DOUBLE_CHECK = 25;
  ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT = 26;
  ANALYSIS_TYPE_DISCOVERED_ATTACK = 27;
  ANALYSIS_TYPE_PROMOTION = 28;
  ANALYSIS_TYPE_DISCOVERED_CHECK = 29;
  ANALYSIS_TYPE_ATTACKS_TRAPPED_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02565"></a>
## FND-02565: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_MULTI_ATTACK = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_MULTI_ATTACK = 23;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 905.

```text
YPE_DISCOVERED_ATTACK_CHECK = 20;
  ANALYSIS_TYPE_FORK_WITH_MATE = 21;
  ANALYSIS_TYPE_FORK = 22;
  ANALYSIS_TYPE_MULTI_ATTACK = 23;
  ANALYSIS_TYPE_SKEWER = 24;
  ANALYSIS_TYPE_DOUBLE_CHECK = 25;
  ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT = 26;
  ANALYSIS_TYPE_DISCOVERED_ATTACK = 27;
  ANALYSIS_TYPE_PROMOTION = 28;
  ANALYSIS_TYPE_DISCOVERED_CHECK = 29;
  ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE = 30;
  ANALYSIS_TYPE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02566"></a>
## FND-02566: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_SKEWER = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_SKEWER = 24;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 940.

```text
 ANALYSIS_TYPE_FORK_WITH_MATE = 21;
  ANALYSIS_TYPE_FORK = 22;
  ANALYSIS_TYPE_MULTI_ATTACK = 23;
  ANALYSIS_TYPE_SKEWER = 24;
  ANALYSIS_TYPE_DOUBLE_CHECK = 25;
  ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT = 26;
  ANALYSIS_TYPE_DISCOVERED_ATTACK = 27;
  ANALYSIS_TYPE_PROMOTION = 28;
  ANALYSIS_TYPE_DISCOVERED_CHECK = 29;
  ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE = 30;
  ANALYSIS_TYPE_THREATENS_PINNED = 31;
  ANALYSIS_
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02567"></a>
## FND-02567: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DOUBLE_CHECK = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DOUBLE_CHECK = 25;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 969.

```text
 = 21;
  ANALYSIS_TYPE_FORK = 22;
  ANALYSIS_TYPE_MULTI_ATTACK = 23;
  ANALYSIS_TYPE_SKEWER = 24;
  ANALYSIS_TYPE_DOUBLE_CHECK = 25;
  ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT = 26;
  ANALYSIS_TYPE_DISCOVERED_ATTACK = 27;
  ANALYSIS_TYPE_PROMOTION = 28;
  ANALYSIS_TYPE_DISCOVERED_CHECK = 29;
  ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE = 30;
  ANALYSIS_TYPE_THREATENS_PINNED = 31;
  ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02568"></a>
## FND-02568: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT = 26;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1004.

```text
 ANALYSIS_TYPE_MULTI_ATTACK = 23;
  ANALYSIS_TYPE_SKEWER = 24;
  ANALYSIS_TYPE_DOUBLE_CHECK = 25;
  ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT = 26;
  ANALYSIS_TYPE_DISCOVERED_ATTACK = 27;
  ANALYSIS_TYPE_PROMOTION = 28;
  ANALYSIS_TYPE_DISCOVERED_CHECK = 29;
  ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE = 30;
  ANALYSIS_TYPE_THREATENS_PINNED = 31;
  ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS = 32;
  ANALYSIS_TYPE_FORCES_DO
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02569"></a>
## FND-02569: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DISCOVERED_ATTACK = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DISCOVERED_ATTACK = 27;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1057.

```text
WER = 24;
  ANALYSIS_TYPE_DOUBLE_CHECK = 25;
  ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT = 26;
  ANALYSIS_TYPE_DISCOVERED_ATTACK = 27;
  ANALYSIS_TYPE_PROMOTION = 28;
  ANALYSIS_TYPE_DISCOVERED_CHECK = 29;
  ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE = 30;
  ANALYSIS_TYPE_THREATENS_PINNED = 31;
  ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS = 32;
  ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS = 33;
  ANALYSIS_TYPE_FORCES_ISOLATED_PAW
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02570"></a>
## FND-02570: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_PROMOTION = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_PROMOTION = 28;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1097.

```text
 25;
  ANALYSIS_TYPE_CAPTURE_DEFENDS_EXPOSED_THREAT = 26;
  ANALYSIS_TYPE_DISCOVERED_ATTACK = 27;
  ANALYSIS_TYPE_PROMOTION = 28;
  ANALYSIS_TYPE_DISCOVERED_CHECK = 29;
  ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE = 30;
  ANALYSIS_TYPE_THREATENS_PINNED = 31;
  ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS = 32;
  ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS = 33;
  ANALYSIS_TYPE_FORCES_ISOLATED_PAWN = 34;
  ANALYSIS_TYPE_EQUAL_TRADE = 35
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02571"></a>
## FND-02571: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_DISCOVERED_CHECK = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_DISCOVERED_CHECK = 29;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1129.

```text
ENDS_EXPOSED_THREAT = 26;
  ANALYSIS_TYPE_DISCOVERED_ATTACK = 27;
  ANALYSIS_TYPE_PROMOTION = 28;
  ANALYSIS_TYPE_DISCOVERED_CHECK = 29;
  ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE = 30;
  ANALYSIS_TYPE_THREATENS_PINNED = 31;
  ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS = 32;
  ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS = 33;
  ANALYSIS_TYPE_FORCES_ISOLATED_PAWN = 34;
  ANALYSIS_TYPE_EQUAL_TRADE = 35;
  ANALYSIS_TYPE_IMMEDIATE_RECA
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02572"></a>
## FND-02572: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE = 30

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE = 30;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1168.

```text
PE_DISCOVERED_ATTACK = 27;
  ANALYSIS_TYPE_PROMOTION = 28;
  ANALYSIS_TYPE_DISCOVERED_CHECK = 29;
  ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE = 30;
  ANALYSIS_TYPE_THREATENS_PINNED = 31;
  ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS = 32;
  ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS = 33;
  ANALYSIS_TYPE_FORCES_ISOLATED_PAWN = 34;
  ANALYSIS_TYPE_EQUAL_TRADE = 35;
  ANALYSIS_TYPE_IMMEDIATE_RECAPTURE = 36;
  ANALYSIS_TYPE_OBVIOUS_REC
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02573"></a>
## FND-02573: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_THREATENS_PINNED = 31

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_THREATENS_PINNED = 31;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1212.

```text
ROMOTION = 28;
  ANALYSIS_TYPE_DISCOVERED_CHECK = 29;
  ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE = 30;
  ANALYSIS_TYPE_THREATENS_PINNED = 31;
  ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS = 32;
  ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS = 33;
  ANALYSIS_TYPE_FORCES_ISOLATED_PAWN = 34;
  ANALYSIS_TYPE_EQUAL_TRADE = 35;
  ANALYSIS_TYPE_IMMEDIATE_RECAPTURE = 36;
  ANALYSIS_TYPE_OBVIOUS_RECAPTURE = 37;
  ANALYSIS_TYPE_CAPTURES_CHECKE
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02574"></a>
## FND-02574: chesscom.explanation_engine.v1.AnalysisType.ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS = 32

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS = 32;

### Evidence

- **SRC-0336** `research/proto/chesscom/explanation_engine/v1/analysis_type.proto` — [preserved redacted evidence](../evidence/text/596a243661b7a24f0f3e61bcba101f1f4dce0a908fa6b339239223cf8f184825.proto)
  Character offset 1251.

```text
ED_CHECK = 29;
  ANALYSIS_TYPE_ATTACKS_TRAPPED_PIECE = 30;
  ANALYSIS_TYPE_THREATENS_PINNED = 31;
  ANALYSIS_TYPE_FORCES_DOUBLED_CASTLE_PAWNS = 32;
  ANALYSIS_TYPE_FORCES_DOUBLED_PAWNS = 33;
  ANALYSIS_TYPE_FORCES_ISOLATED_PAWN = 34;
  ANALYSIS_TYPE_EQUAL_TRADE = 35;
  ANALYSIS_TYPE_IMMEDIATE_RECAPTURE = 36;
  ANALYSIS_TYPE_OBVIOUS_RECAPTURE = 37;
  ANALYSIS_TYPE_CAPTURES_CHECKER = 38;
  ANALYSIS_TYPE_COUNTER_THREAT 
```

**Source references:** SRC-0336, SRC-1307  
**URL references:** None independently associated  
**Related findings:** FND-02543, FND-02544, FND-02545

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
