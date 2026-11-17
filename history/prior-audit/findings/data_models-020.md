# data_models — findings 1901–2000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-02175"></a>
## FND-02175: chesscom.courses.v1.StoreCourseTrainingProgressRequest.ply_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string ply_id = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1178.

```text
on lesson = 1;
  optional string training_id = 2;
}

message StoreCourseTrainingProgressRequest {
  optional string ply_id = 1;
  optional string san = 2;
  optional .chesscom.courses.v1.MoveTrainerTrainingMode training_mode = 3;
  optional string learning_session_id = 4;
  optional string training_id = 5;
}

message StoreCourseTrainingProgressResponse {
}

message StoreCourseVideoProgressRequest {
  optional string 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02176"></a>
## FND-02176: chesscom.courses.v1.StoreCourseTrainingProgressRequest.san = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string san = 2;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1208.

```text
ng training_id = 2;
}

message StoreCourseTrainingProgressRequest {
  optional string ply_id = 1;
  optional string san = 2;
  optional .chesscom.courses.v1.MoveTrainerTrainingMode training_mode = 3;
  optional string learning_session_id = 4;
  optional string training_id = 5;
}

message StoreCourseTrainingProgressResponse {
}

message StoreCourseVideoProgressRequest {
  optional string video_id = 1;
  optional strin
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02177"></a>
## FND-02177: chesscom.courses.v1.StoreCourseTrainingProgressRequest.training_mode = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.MoveTrainerTrainingMode training_mode = 3;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1235.

```text
age StoreCourseTrainingProgressRequest {
  optional string ply_id = 1;
  optional string san = 2;
  optional .chesscom.courses.v1.MoveTrainerTrainingMode training_mode = 3;
  optional string learning_session_id = 4;
  optional string training_id = 5;
}

message StoreCourseTrainingProgressResponse {
}

message StoreCourseVideoProgressRequest {
  optional string video_id = 1;
  optional string learning_session_id = 2;

```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02178"></a>
## FND-02178: chesscom.courses.v1.StoreCourseTrainingProgressRequest.learning_session_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string learning_session_id = 4;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1310.

```text
tional string san = 2;
  optional .chesscom.courses.v1.MoveTrainerTrainingMode training_mode = 3;
  optional string learning_session_id = 4;
  optional string training_id = 5;
}

message StoreCourseTrainingProgressResponse {
}

message StoreCourseVideoProgressRequest {
  optional string video_id = 1;
  optional string learning_session_id = 2;
  optional int32 position_in_seconds = 3;
  optional int32 watched_seconds 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02179"></a>
## FND-02179: chesscom.courses.v1.StoreCourseTrainingProgressRequest.training_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string training_id = 5;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1353.

```text
.courses.v1.MoveTrainerTrainingMode training_mode = 3;
  optional string learning_session_id = 4;
  optional string training_id = 5;
}

message StoreCourseTrainingProgressResponse {
}

message StoreCourseVideoProgressRequest {
  optional string video_id = 1;
  optional string learning_session_id = 2;
  optional int32 position_in_seconds = 3;
  optional int32 watched_seconds = 4;
}

message StoreCourseVideoProgressRes
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02180"></a>
## FND-02180: message declaration: chesscom.courses.v1.StoreCourseTrainingProgressResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StoreCourseTrainingProgressResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1389.

```text
training_mode = 3;
  optional string learning_session_id = 4;
  optional string training_id = 5;
}

message StoreCourseTrainingProgressResponse {
}

message StoreCourseVideoProgressRequest {
  optional string video_id = 1;
  optional string learning_session_id = 2;
  optional int32 position_in_seconds = 3;
  optional int32 watched_seconds = 4;
}

message StoreCourseVideoProgressResponse {
}

message GetCourseVideoPla
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02181"></a>
## FND-02181: message declaration: chesscom.courses.v1.StoreCourseVideoProgressRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StoreCourseVideoProgressRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1438.

```text
sion_id = 4;
  optional string training_id = 5;
}

message StoreCourseTrainingProgressResponse {
}

message StoreCourseVideoProgressRequest {
  optional string video_id = 1;
  optional string learning_session_id = 2;
  optional int32 position_in_seconds = 3;
  optional int32 watched_seconds = 4;
}

message StoreCourseVideoProgressResponse {
}

message GetCourseVideoPlaybackRequest {
  optional string video_id = 1;
}

```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02182"></a>
## FND-02182: chesscom.courses.v1.StoreCourseVideoProgressRequest.video_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string video_id = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1482.

```text
 5;
}

message StoreCourseTrainingProgressResponse {
}

message StoreCourseVideoProgressRequest {
  optional string video_id = 1;
  optional string learning_session_id = 2;
  optional int32 position_in_seconds = 3;
  optional int32 watched_seconds = 4;
}

message StoreCourseVideoProgressResponse {
}

message GetCourseVideoPlaybackRequest {
  optional string video_id = 1;
}

message GetCourseVideoPlaybackResponse {
  
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02183"></a>
## FND-02183: chesscom.courses.v1.StoreCourseVideoProgressRequest.learning_session_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string learning_session_id = 2;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 469.

```text
ningSessionResponse {
  optional .chesscom.courses.v1.CourseLearningSession learning_session = 1;
  optional string learning_session_id = 2;
  optional .chesscom.courses.v1.CourseLearningSessionProgress progress = 3;
}

message GetCourseTrainingForLearningRequest {
  optional string variation_id = 1;
  optional string learning_session_id = 2;
}

message GetCourseTrainingForLearningResponse {
  optional .chesscom.cour
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02184"></a>
## FND-02184: chesscom.courses.v1.StoreCourseVideoProgressRequest.position_in_seconds = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 position_in_seconds = 3;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1557.

```text
VideoProgressRequest {
  optional string video_id = 1;
  optional string learning_session_id = 2;
  optional int32 position_in_seconds = 3;
  optional int32 watched_seconds = 4;
}

message StoreCourseVideoProgressResponse {
}

message GetCourseVideoPlaybackRequest {
  optional string video_id = 1;
}

message GetCourseVideoPlaybackResponse {
  optional .chesscom.courses.v1.CourseVideoPlayback playback = 1;
}

message 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02185"></a>
## FND-02185: chesscom.courses.v1.StoreCourseVideoProgressRequest.watched_seconds = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 watched_seconds = 4;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1599.

```text
ideo_id = 1;
  optional string learning_session_id = 2;
  optional int32 position_in_seconds = 3;
  optional int32 watched_seconds = 4;
}

message StoreCourseVideoProgressResponse {
}

message GetCourseVideoPlaybackRequest {
  optional string video_id = 1;
}

message GetCourseVideoPlaybackResponse {
  optional .chesscom.courses.v1.CourseVideoPlayback playback = 1;
}

message FinalizeCourseTrainingRequest {
  optional
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02186"></a>
## FND-02186: message declaration: chesscom.courses.v1.StoreCourseVideoProgressResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StoreCourseVideoProgressResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1638.

```text
_session_id = 2;
  optional int32 position_in_seconds = 3;
  optional int32 watched_seconds = 4;
}

message StoreCourseVideoProgressResponse {
}

message GetCourseVideoPlaybackRequest {
  optional string video_id = 1;
}

message GetCourseVideoPlaybackResponse {
  optional .chesscom.courses.v1.CourseVideoPlayback playback = 1;
}

message FinalizeCourseTrainingRequest {
  optional string learning_session_id = 1;
  opti
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02187"></a>
## FND-02187: message declaration: chesscom.courses.v1.GetCourseVideoPlaybackRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseVideoPlaybackRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1684.

```text
seconds = 3;
  optional int32 watched_seconds = 4;
}

message StoreCourseVideoProgressResponse {
}

message GetCourseVideoPlaybackRequest {
  optional string video_id = 1;
}

message GetCourseVideoPlaybackResponse {
  optional .chesscom.courses.v1.CourseVideoPlayback playback = 1;
}

message FinalizeCourseTrainingRequest {
  optional string learning_session_id = 1;
  optional string training_id = 2;
}

message Finali
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02188"></a>
## FND-02188: chesscom.courses.v1.GetCourseVideoPlaybackRequest.video_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string video_id = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1482.

```text
 5;
}

message StoreCourseTrainingProgressResponse {
}

message StoreCourseVideoProgressRequest {
  optional string video_id = 1;
  optional string learning_session_id = 2;
  optional int32 position_in_seconds = 3;
  optional int32 watched_seconds = 4;
}

message StoreCourseVideoProgressResponse {
}

message GetCourseVideoPlaybackRequest {
  optional string video_id = 1;
}

message GetCourseVideoPlaybackResponse {
  
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02189"></a>
## FND-02189: message declaration: chesscom.courses.v1.GetCourseVideoPlaybackResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseVideoPlaybackResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1759.

```text
deoProgressResponse {
}

message GetCourseVideoPlaybackRequest {
  optional string video_id = 1;
}

message GetCourseVideoPlaybackResponse {
  optional .chesscom.courses.v1.CourseVideoPlayback playback = 1;
}

message FinalizeCourseTrainingRequest {
  optional string learning_session_id = 1;
  optional string training_id = 2;
}

message FinalizeCourseTrainingResponse {
  optional .chesscom.courses.v1.CourseLearningSe
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02190"></a>
## FND-02190: chesscom.courses.v1.GetCourseVideoPlaybackResponse.playback = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseVideoPlayback playback = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1802.

```text
ideoPlaybackRequest {
  optional string video_id = 1;
}

message GetCourseVideoPlaybackResponse {
  optional .chesscom.courses.v1.CourseVideoPlayback playback = 1;
}

message FinalizeCourseTrainingRequest {
  optional string learning_session_id = 1;
  optional string training_id = 2;
}

message FinalizeCourseTrainingResponse {
  optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;
}

message GetCourseS
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02191"></a>
## FND-02191: message declaration: chesscom.courses.v1.FinalizeCourseTrainingRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FinalizeCourseTrainingRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1869.

```text
tCourseVideoPlaybackResponse {
  optional .chesscom.courses.v1.CourseVideoPlayback playback = 1;
}

message FinalizeCourseTrainingRequest {
  optional string learning_session_id = 1;
  optional string training_id = 2;
}

message FinalizeCourseTrainingResponse {
  optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;
}

message GetCourseStatsRequest {
  optional string context_type = 1;
  optional string
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02192"></a>
## FND-02192: chesscom.courses.v1.FinalizeCourseTrainingRequest.learning_session_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string learning_session_id = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1911.

```text
.chesscom.courses.v1.CourseVideoPlayback playback = 1;
}

message FinalizeCourseTrainingRequest {
  optional string learning_session_id = 1;
  optional string training_id = 2;
}

message FinalizeCourseTrainingResponse {
  optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;
}

message GetCourseStatsRequest {
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseStats
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02193"></a>
## FND-02193: chesscom.courses.v1.FinalizeCourseTrainingRequest.training_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string training_id = 2;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 823.

```text
e GetCourseTrainingForLearningResponse {
  optional .chesscom.courses.v1.CourseLesson lesson = 1;
  optional string training_id = 2;
}

message GetCourseTrainingForReviewingRequest {
  optional string variation_id = 1;
  optional string learning_session_id = 2;
}

message GetCourseTrainingForReviewingResponse {
  optional .chesscom.courses.v1.CourseLesson lesson = 1;
  optional string training_id = 2;
}

message Stor
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02194"></a>
## FND-02194: message declaration: chesscom.courses.v1.FinalizeCourseTrainingResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FinalizeCourseTrainingResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1990.

```text
eTrainingRequest {
  optional string learning_session_id = 1;
  optional string training_id = 2;
}

message FinalizeCourseTrainingResponse {
  optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;
}

message GetCourseStatsRequest {
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseStatsResponse {
  optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02195"></a>
## FND-02195: chesscom.courses.v1.FinalizeCourseTrainingResponse.stats = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2033.

```text
ng_session_id = 1;
  optional string training_id = 2;
}

message FinalizeCourseTrainingResponse {
  optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;
}

message GetCourseStatsRequest {
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseStatsResponse {
  optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;
}

message GetCourseConfigurationRequest 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02196"></a>
## FND-02196: message declaration: chesscom.courses.v1.GetCourseStatsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseStatsRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2104.

```text
zeCourseTrainingResponse {
  optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;
}

message GetCourseStatsRequest {
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseStatsResponse {
  optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;
}

message GetCourseConfigurationRequest {
  oneof _course_slug {
  string course_slug = 3;
  }
  optional strin
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02197"></a>
## FND-02197: chesscom.courses.v1.GetCourseStatsRequest.context_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string context_type = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 277.

```text
n_id {
  string learning_session_id = 3;
  }
  oneof _course_slug {
  string course_slug = 4;
  }
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseLearningSessionResponse {
  optional .chesscom.courses.v1.CourseLearningSession learning_session = 1;
  optional string learning_session_id = 2;
  optional .chesscom.courses.v1.CourseLearningSessionProgress progress = 3;
}

message 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02198"></a>
## FND-02198: chesscom.courses.v1.GetCourseStatsRequest.context_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string context_id = 2;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 313.

```text
= 3;
  }
  oneof _course_slug {
  string course_slug = 4;
  }
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseLearningSessionResponse {
  optional .chesscom.courses.v1.CourseLearningSession learning_session = 1;
  optional string learning_session_id = 2;
  optional .chesscom.courses.v1.CourseLearningSessionProgress progress = 3;
}

message GetCourseTrainingForLearningRequest 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02199"></a>
## FND-02199: message declaration: chesscom.courses.v1.GetCourseStatsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseStatsResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2209.

```text
ge GetCourseStatsRequest {
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseStatsResponse {
  optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;
}

message GetCourseConfigurationRequest {
  oneof _course_slug {
  string course_slug = 3;
  }
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseConfigurationResponse {
  optio
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02200"></a>
## FND-02200: chesscom.courses.v1.GetCourseStatsResponse.stats = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2033.

```text
ng_session_id = 1;
  optional string training_id = 2;
}

message FinalizeCourseTrainingResponse {
  optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;
}

message GetCourseStatsRequest {
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseStatsResponse {
  optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;
}

message GetCourseConfigurationRequest 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02201"></a>
## FND-02201: message declaration: chesscom.courses.v1.GetCourseConfigurationRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseConfigurationRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2315.

```text
e GetCourseStatsResponse {
  optional .chesscom.courses.v1.CourseLearningSessionStats stats = 1;
}

message GetCourseConfigurationRequest {
  oneof _course_slug {
  string course_slug = 3;
  }
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseConfigurationResponse {
  optional .chesscom.courses.v1.CourseConfiguration configuration = 1;
  repeated .chesscom.api.v1.Language avail
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02202"></a>
## FND-02202: oneof declaration: chesscom.courses.v1.GetCourseConfigurationRequest._course_slug

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _course_slug {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 224.

```text
urseLearningSessionRequest {
  oneof _learning_session_id {
  string learning_session_id = 3;
  }
  oneof _course_slug {
  string course_slug = 4;
  }
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseLearningSessionResponse {
  optional .chesscom.courses.v1.CourseLearningSession learning_session = 1;
  optional string learning_session_id = 2;
  optional .chesscom.courses.v1.Co
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02203"></a>
## FND-02203: chesscom.courses.v1.GetCourseConfigurationRequest.course_slug = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string course_slug = 3;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2380.

```text
LearningSessionStats stats = 1;
}

message GetCourseConfigurationRequest {
  oneof _course_slug {
  string course_slug = 3;
  }
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseConfigurationResponse {
  optional .chesscom.courses.v1.CourseConfiguration configuration = 1;
  repeated .chesscom.api.v1.Language available_languages = 2;
}

message StoreCourseConfigurationRequest {

```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02204"></a>
## FND-02204: chesscom.courses.v1.GetCourseConfigurationRequest.context_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string context_type = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 277.

```text
n_id {
  string learning_session_id = 3;
  }
  oneof _course_slug {
  string course_slug = 4;
  }
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseLearningSessionResponse {
  optional .chesscom.courses.v1.CourseLearningSession learning_session = 1;
  optional string learning_session_id = 2;
  optional .chesscom.courses.v1.CourseLearningSessionProgress progress = 3;
}

message 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02205"></a>
## FND-02205: chesscom.courses.v1.GetCourseConfigurationRequest.context_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string context_id = 2;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 313.

```text
= 3;
  }
  oneof _course_slug {
  string course_slug = 4;
  }
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseLearningSessionResponse {
  optional .chesscom.courses.v1.CourseLearningSession learning_session = 1;
  optional string learning_session_id = 2;
  optional .chesscom.courses.v1.CourseLearningSessionProgress progress = 3;
}

message GetCourseTrainingForLearningRequest 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02206"></a>
## FND-02206: message declaration: chesscom.courses.v1.GetCourseConfigurationResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseConfigurationResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2481.

```text
tring course_slug = 3;
  }
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseConfigurationResponse {
  optional .chesscom.courses.v1.CourseConfiguration configuration = 1;
  repeated .chesscom.api.v1.Language available_languages = 2;
}

message StoreCourseConfigurationRequest {
  optional string context_type = 1;
  optional string context_id = 2;
  optional .chesscom.courses.v1
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02207"></a>
## FND-02207: chesscom.courses.v1.GetCourseConfigurationResponse.configuration = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseConfiguration configuration = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2524.

```text
g context_type = 1;
  optional string context_id = 2;
}

message GetCourseConfigurationResponse {
  optional .chesscom.courses.v1.CourseConfiguration configuration = 1;
  repeated .chesscom.api.v1.Language available_languages = 2;
}

message StoreCourseConfigurationRequest {
  optional string context_type = 1;
  optional string context_id = 2;
  optional .chesscom.courses.v1.CourseConfiguration configuration = 3;
}


```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02208"></a>
## FND-02208: chesscom.courses.v1.GetCourseConfigurationResponse.available_languages = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.api.v1.Language available_languages = 2;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2595.

```text
rseConfigurationResponse {
  optional .chesscom.courses.v1.CourseConfiguration configuration = 1;
  repeated .chesscom.api.v1.Language available_languages = 2;
}

message StoreCourseConfigurationRequest {
  optional string context_type = 1;
  optional string context_id = 2;
  optional .chesscom.courses.v1.CourseConfiguration configuration = 3;
}

message StoreCourseConfigurationResponse {
}

message DeleteCourseProgr
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02209"></a>
## FND-02209: message declaration: chesscom.courses.v1.StoreCourseConfigurationRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StoreCourseConfigurationRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2658.

```text
seConfiguration configuration = 1;
  repeated .chesscom.api.v1.Language available_languages = 2;
}

message StoreCourseConfigurationRequest {
  optional string context_type = 1;
  optional string context_id = 2;
  optional .chesscom.courses.v1.CourseConfiguration configuration = 3;
}

message StoreCourseConfigurationResponse {
}

message DeleteCourseProgressRequest {
  optional string course_id = 1;
}

message Delete
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02210"></a>
## FND-02210: chesscom.courses.v1.StoreCourseConfigurationRequest.context_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string context_type = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 277.

```text
n_id {
  string learning_session_id = 3;
  }
  oneof _course_slug {
  string course_slug = 4;
  }
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseLearningSessionResponse {
  optional .chesscom.courses.v1.CourseLearningSession learning_session = 1;
  optional string learning_session_id = 2;
  optional .chesscom.courses.v1.CourseLearningSessionProgress progress = 3;
}

message 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02211"></a>
## FND-02211: chesscom.courses.v1.StoreCourseConfigurationRequest.context_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string context_id = 2;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 313.

```text
= 3;
  }
  oneof _course_slug {
  string course_slug = 4;
  }
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseLearningSessionResponse {
  optional .chesscom.courses.v1.CourseLearningSession learning_session = 1;
  optional string learning_session_id = 2;
  optional .chesscom.courses.v1.CourseLearningSessionProgress progress = 3;
}

message GetCourseTrainingForLearningRequest 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02212"></a>
## FND-02212: chesscom.courses.v1.StoreCourseConfigurationRequest.configuration = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseConfiguration configuration = 3;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2772.

```text
ourseConfigurationRequest {
  optional string context_type = 1;
  optional string context_id = 2;
  optional .chesscom.courses.v1.CourseConfiguration configuration = 3;
}

message StoreCourseConfigurationResponse {
}

message DeleteCourseProgressRequest {
  optional string course_id = 1;
}

message DeleteCourseProgressResponse {
}

message ClaimPreviewRequest {
  optional string variation_id = 1;
}

message ClaimPrev
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02213"></a>
## FND-02213: message declaration: chesscom.courses.v1.StoreCourseConfigurationResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StoreCourseConfigurationResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2844.

```text
al string context_id = 2;
  optional .chesscom.courses.v1.CourseConfiguration configuration = 3;
}

message StoreCourseConfigurationResponse {
}

message DeleteCourseProgressRequest {
  optional string course_id = 1;
}

message DeleteCourseProgressResponse {
}

message ClaimPreviewRequest {
  optional string variation_id = 1;
}

message ClaimPreviewResponse {
}

message SetVariationPausedRequest {
  optional string v
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02214"></a>
## FND-02214: message declaration: chesscom.courses.v1.DeleteCourseProgressRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DeleteCourseProgressRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2890.

```text
.courses.v1.CourseConfiguration configuration = 3;
}

message StoreCourseConfigurationResponse {
}

message DeleteCourseProgressRequest {
  optional string course_id = 1;
}

message DeleteCourseProgressResponse {
}

message ClaimPreviewRequest {
  optional string variation_id = 1;
}

message ClaimPreviewResponse {
}

message SetVariationPausedRequest {
  optional string variation_id = 1;
}

message SetVariationPaused
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02215"></a>
## FND-02215: chesscom.courses.v1.DeleteCourseProgressRequest.course_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_id = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2930.

```text
ation = 3;
}

message StoreCourseConfigurationResponse {
}

message DeleteCourseProgressRequest {
  optional string course_id = 1;
}

message DeleteCourseProgressResponse {
}

message ClaimPreviewRequest {
  optional string variation_id = 1;
}

message ClaimPreviewResponse {
}

message SetVariationPausedRequest {
  optional string variation_id = 1;
}

message SetVariationPausedResponse {
}

message SetVariationUnpaus
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02216"></a>
## FND-02216: message declaration: chesscom.courses.v1.DeleteCourseProgressResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DeleteCourseProgressResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 2964.

```text
onfigurationResponse {
}

message DeleteCourseProgressRequest {
  optional string course_id = 1;
}

message DeleteCourseProgressResponse {
}

message ClaimPreviewRequest {
  optional string variation_id = 1;
}

message ClaimPreviewResponse {
}

message SetVariationPausedRequest {
  optional string variation_id = 1;
}

message SetVariationPausedResponse {
}

message SetVariationUnpausedRequest {
  optional string vari
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02217"></a>
## FND-02217: message declaration: chesscom.courses.v1.ClaimPreviewRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ClaimPreviewRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 3006.

```text
urseProgressRequest {
  optional string course_id = 1;
}

message DeleteCourseProgressResponse {
}

message ClaimPreviewRequest {
  optional string variation_id = 1;
}

message ClaimPreviewResponse {
}

message SetVariationPausedRequest {
  optional string variation_id = 1;
}

message SetVariationPausedResponse {
}

message SetVariationUnpausedRequest {
  optional string variation_id = 1;
}

message SetVariationUnpau
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02218"></a>
## FND-02218: chesscom.courses.v1.ClaimPreviewRequest.variation_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string variation_id = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 637.

```text
s.v1.CourseLearningSessionProgress progress = 3;
}

message GetCourseTrainingForLearningRequest {
  optional string variation_id = 1;
  optional string learning_session_id = 2;
}

message GetCourseTrainingForLearningResponse {
  optional .chesscom.courses.v1.CourseLesson lesson = 1;
  optional string training_id = 2;
}

message GetCourseTrainingForReviewingRequest {
  optional string variation_id = 1;
  optional stri
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02219"></a>
## FND-02219: message declaration: chesscom.courses.v1.ClaimPreviewResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ClaimPreviewResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 3075.

```text
eteCourseProgressResponse {
}

message ClaimPreviewRequest {
  optional string variation_id = 1;
}

message ClaimPreviewResponse {
}

message SetVariationPausedRequest {
  optional string variation_id = 1;
}

message SetVariationPausedResponse {
}

message SetVariationUnpausedRequest {
  optional string variation_id = 1;
}

message SetVariationUnpausedResponse {
}

```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02220"></a>
## FND-02220: message declaration: chesscom.courses.v1.SetVariationPausedRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetVariationPausedRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 3109.

```text
sage ClaimPreviewRequest {
  optional string variation_id = 1;
}

message ClaimPreviewResponse {
}

message SetVariationPausedRequest {
  optional string variation_id = 1;
}

message SetVariationPausedResponse {
}

message SetVariationUnpausedRequest {
  optional string variation_id = 1;
}

message SetVariationUnpausedResponse {
}

```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02221"></a>
## FND-02221: chesscom.courses.v1.SetVariationPausedRequest.variation_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string variation_id = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 637.

```text
s.v1.CourseLearningSessionProgress progress = 3;
}

message GetCourseTrainingForLearningRequest {
  optional string variation_id = 1;
  optional string learning_session_id = 2;
}

message GetCourseTrainingForLearningResponse {
  optional .chesscom.courses.v1.CourseLesson lesson = 1;
  optional string training_id = 2;
}

message GetCourseTrainingForReviewingRequest {
  optional string variation_id = 1;
  optional stri
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02222"></a>
## FND-02222: message declaration: chesscom.courses.v1.SetVariationPausedResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetVariationPausedResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 3184.

```text
laimPreviewResponse {
}

message SetVariationPausedRequest {
  optional string variation_id = 1;
}

message SetVariationPausedResponse {
}

message SetVariationUnpausedRequest {
  optional string variation_id = 1;
}

message SetVariationUnpausedResponse {
}

```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02223"></a>
## FND-02223: message declaration: chesscom.courses.v1.SetVariationUnpausedRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetVariationUnpausedRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 3224.

```text
ationPausedRequest {
  optional string variation_id = 1;
}

message SetVariationPausedResponse {
}

message SetVariationUnpausedRequest {
  optional string variation_id = 1;
}

message SetVariationUnpausedResponse {
}

```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02224"></a>
## FND-02224: chesscom.courses.v1.SetVariationUnpausedRequest.variation_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string variation_id = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 637.

```text
s.v1.CourseLearningSessionProgress progress = 3;
}

message GetCourseTrainingForLearningRequest {
  optional string variation_id = 1;
  optional string learning_session_id = 2;
}

message GetCourseTrainingForLearningResponse {
  optional .chesscom.courses.v1.CourseLesson lesson = 1;
  optional string training_id = 2;
}

message GetCourseTrainingForReviewingRequest {
  optional string variation_id = 1;
  optional stri
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02225"></a>
## FND-02225: message declaration: chesscom.courses.v1.SetVariationUnpausedResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetVariationUnpausedResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 3301.

```text
ionPausedResponse {
}

message SetVariationUnpausedRequest {
  optional string variation_id = 1;
}

message SetVariationUnpausedResponse {
}

```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02226"></a>
## FND-02226: message declaration: chesscom.courses.v1.GoalStep

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GoalStep {

### Evidence

- **SRC-0297** `research/proto/chesscom/courses/v1/goal_step.proto` — [preserved redacted evidence](../evidence/text/cbfc550c754d696dc2fe84a9689ed88d48fe5110d1d338b9183f74dbf313cf7f.proto)
  Character offset 96.

```text
// source: chesscom/courses/v1/goal_step.proto
// syntax: proto3

package chesscom.courses.v1;

message GoalStep {
  optional string type = 1;
  optional int32 completed_amount = 2;
  optional int32 total_amount = 3;
}

```

**Source references:** SRC-0297, SRC-1268  
**URL references:** None independently associated  
**Related findings:** FND-02227, FND-02228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02227"></a>
## FND-02227: chesscom.courses.v1.GoalStep.type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string type = 1;

### Evidence

- **SRC-0297** `research/proto/chesscom/courses/v1/goal_step.proto` — [preserved redacted evidence](../evidence/text/cbfc550c754d696dc2fe84a9689ed88d48fe5110d1d338b9183f74dbf313cf7f.proto)
  Character offset 117.

```text
om/courses/v1/goal_step.proto
// syntax: proto3

package chesscom.courses.v1;

message GoalStep {
  optional string type = 1;
  optional int32 completed_amount = 2;
  optional int32 total_amount = 3;
}

```

**Source references:** SRC-0297, SRC-1268  
**URL references:** None independently associated  
**Related findings:** FND-02226, FND-02228

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02228"></a>
## FND-02228: chesscom.courses.v1.GoalStep.completed_amount = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 completed_amount = 2;

### Evidence

- **SRC-0297** `research/proto/chesscom/courses/v1/goal_step.proto` — [preserved redacted evidence](../evidence/text/cbfc550c754d696dc2fe84a9689ed88d48fe5110d1d338b9183f74dbf313cf7f.proto)
  Character offset 145.

```text
o
// syntax: proto3

package chesscom.courses.v1;

message GoalStep {
  optional string type = 1;
  optional int32 completed_amount = 2;
  optional int32 total_amount = 3;
}

```

**Source references:** SRC-0297, SRC-1268  
**URL references:** None independently associated  
**Related findings:** FND-02226, FND-02227

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02229"></a>
## FND-02229: chesscom.courses.v1.GoalStep.total_amount = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 total_amount = 3;

### Evidence

- **SRC-0297** `research/proto/chesscom/courses/v1/goal_step.proto` — [preserved redacted evidence](../evidence/text/cbfc550c754d696dc2fe84a9689ed88d48fe5110d1d338b9183f74dbf313cf7f.proto)
  Character offset 184.

```text
ourses.v1;

message GoalStep {
  optional string type = 1;
  optional int32 completed_amount = 2;
  optional int32 total_amount = 3;
}

```

**Source references:** SRC-0297, SRC-1268  
**URL references:** None independently associated  
**Related findings:** FND-02226, FND-02227, FND-02228

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02230"></a>
## FND-02230: enum declaration: chesscom.courses.v1.GoalType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GoalType {

### Evidence

- **SRC-0298** `research/proto/chesscom/courses/v1/goal_type.proto` — [preserved redacted evidence](../evidence/text/9a2219042b9ef1a062f2e411897bcaae44cbe75c39d7e745424feaacb6424899.proto)
  Character offset 96.

```text
// source: chesscom/courses/v1/goal_type.proto
// syntax: proto3

package chesscom.courses.v1;

enum GoalType {
  GOAL_TYPE_UNSPECIFIED = 0;
  GOAL_TYPE_FTUE_CHECKLIST = 1;
}

```

**Source references:** SRC-0298, SRC-1269  
**URL references:** None independently associated  
**Related findings:** FND-02231, FND-02232

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02231"></a>
## FND-02231: chesscom.courses.v1.GoalType.GOAL_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GOAL_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0298** `research/proto/chesscom/courses/v1/goal_type.proto` — [preserved redacted evidence](../evidence/text/9a2219042b9ef1a062f2e411897bcaae44cbe75c39d7e745424feaacb6424899.proto)
  Character offset 114.

```text
sscom/courses/v1/goal_type.proto
// syntax: proto3

package chesscom.courses.v1;

enum GoalType {
  GOAL_TYPE_UNSPECIFIED = 0;
  GOAL_TYPE_FTUE_CHECKLIST = 1;
}

```

**Source references:** SRC-0298, SRC-1269  
**URL references:** None independently associated  
**Related findings:** FND-02230, FND-02232

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02232"></a>
## FND-02232: chesscom.courses.v1.GoalType.GOAL_TYPE_FTUE_CHECKLIST = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GOAL_TYPE_FTUE_CHECKLIST = 1;

### Evidence

- **SRC-0298** `research/proto/chesscom/courses/v1/goal_type.proto` — [preserved redacted evidence](../evidence/text/9a2219042b9ef1a062f2e411897bcaae44cbe75c39d7e745424feaacb6424899.proto)
  Character offset 143.

```text
oto
// syntax: proto3

package chesscom.courses.v1;

enum GoalType {
  GOAL_TYPE_UNSPECIFIED = 0;
  GOAL_TYPE_FTUE_CHECKLIST = 1;
}

```

**Source references:** SRC-0298, SRC-1269  
**URL references:** None independently associated  
**Related findings:** FND-02230, FND-02231

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02233"></a>
## FND-02233: enum declaration: chesscom.courses.v1.MoveTrainerTrainingMode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MoveTrainerTrainingMode {

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 99.

```text
// source: chesscom/courses/v1/move_trainer.proto
// syntax: proto3

package chesscom.courses.v1;

enum MoveTrainerTrainingMode {
  MOVE_TRAINER_TRAINING_MODE_UNSPECIFIED = 0;
  MOVE_TRAINER_TRAINING_MODE_LEARN = 1;
  MOVE_TRAINER_TRAINING_MODE_REVIEW = 2;
}

enum MoveTrainerTrainingResult {
  MOVE_TRAINER_TRAINING_RESULT_UNSPECIFIED = 0;
  MOVE_TRAINER_TRAINING_RESULT_PASS = 1;
  MOVE_TRAINER_TRAINING_RESULT_FAILED
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02234"></a>
## FND-02234: chesscom.courses.v1.MoveTrainerTrainingMode.MOVE_TRAINER_TRAINING_MODE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_TRAINER_TRAINING_MODE_UNSPECIFIED = 0;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 132.

```text
ove_trainer.proto
// syntax: proto3

package chesscom.courses.v1;

enum MoveTrainerTrainingMode {
  MOVE_TRAINER_TRAINING_MODE_UNSPECIFIED = 0;
  MOVE_TRAINER_TRAINING_MODE_LEARN = 1;
  MOVE_TRAINER_TRAINING_MODE_REVIEW = 2;
}

enum MoveTrainerTrainingResult {
  MOVE_TRAINER_TRAINING_RESULT_UNSPECIFIED = 0;
  MOVE_TRAINER_TRAINING_RESULT_PASS = 1;
  MOVE_TRAINER_TRAINING_RESULT_FAILED = 2;
}

enum AccessRightMode {
 
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02235"></a>
## FND-02235: chesscom.courses.v1.MoveTrainerTrainingMode.MOVE_TRAINER_TRAINING_MODE_LEARN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_TRAINER_TRAINING_MODE_LEARN = 1;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 178.

```text
hesscom.courses.v1;

enum MoveTrainerTrainingMode {
  MOVE_TRAINER_TRAINING_MODE_UNSPECIFIED = 0;
  MOVE_TRAINER_TRAINING_MODE_LEARN = 1;
  MOVE_TRAINER_TRAINING_MODE_REVIEW = 2;
}

enum MoveTrainerTrainingResult {
  MOVE_TRAINER_TRAINING_RESULT_UNSPECIFIED = 0;
  MOVE_TRAINER_TRAINING_RESULT_PASS = 1;
  MOVE_TRAINER_TRAINING_RESULT_FAILED = 2;
}

enum AccessRightMode {
  ACCESS_RIGHT_MODE_UNSPECIFIED = 0;
  ACCESS_R
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02236"></a>
## FND-02236: chesscom.courses.v1.MoveTrainerTrainingMode.MOVE_TRAINER_TRAINING_MODE_REVIEW = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_TRAINER_TRAINING_MODE_REVIEW = 2;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 218.

```text
iningMode {
  MOVE_TRAINER_TRAINING_MODE_UNSPECIFIED = 0;
  MOVE_TRAINER_TRAINING_MODE_LEARN = 1;
  MOVE_TRAINER_TRAINING_MODE_REVIEW = 2;
}

enum MoveTrainerTrainingResult {
  MOVE_TRAINER_TRAINING_RESULT_UNSPECIFIED = 0;
  MOVE_TRAINER_TRAINING_RESULT_PASS = 1;
  MOVE_TRAINER_TRAINING_RESULT_FAILED = 2;
}

enum AccessRightMode {
  ACCESS_RIGHT_MODE_UNSPECIFIED = 0;
  ACCESS_RIGHT_MODE_FULL = 1;
  ACCESS_RIGHT_MODE_
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02237"></a>
## FND-02237: enum declaration: chesscom.courses.v1.MoveTrainerTrainingResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MoveTrainerTrainingResult {

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 260.

```text
NSPECIFIED = 0;
  MOVE_TRAINER_TRAINING_MODE_LEARN = 1;
  MOVE_TRAINER_TRAINING_MODE_REVIEW = 2;
}

enum MoveTrainerTrainingResult {
  MOVE_TRAINER_TRAINING_RESULT_UNSPECIFIED = 0;
  MOVE_TRAINER_TRAINING_RESULT_PASS = 1;
  MOVE_TRAINER_TRAINING_RESULT_FAILED = 2;
}

enum AccessRightMode {
  ACCESS_RIGHT_MODE_UNSPECIFIED = 0;
  ACCESS_RIGHT_MODE_FULL = 1;
  ACCESS_RIGHT_MODE_PREVIEW = 2;
}

message MoveTrainer {
  on
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02238"></a>
## FND-02238: chesscom.courses.v1.MoveTrainerTrainingResult.MOVE_TRAINER_TRAINING_RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_TRAINER_TRAINING_RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 295.

```text
NING_MODE_LEARN = 1;
  MOVE_TRAINER_TRAINING_MODE_REVIEW = 2;
}

enum MoveTrainerTrainingResult {
  MOVE_TRAINER_TRAINING_RESULT_UNSPECIFIED = 0;
  MOVE_TRAINER_TRAINING_RESULT_PASS = 1;
  MOVE_TRAINER_TRAINING_RESULT_FAILED = 2;
}

enum AccessRightMode {
  ACCESS_RIGHT_MODE_UNSPECIFIED = 0;
  ACCESS_RIGHT_MODE_FULL = 1;
  ACCESS_RIGHT_MODE_PREVIEW = 2;
}

message MoveTrainer {
  oneof _course_game_aspect {
  .chessc
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02239"></a>
## FND-02239: chesscom.courses.v1.MoveTrainerTrainingResult.MOVE_TRAINER_TRAINING_RESULT_PASS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_TRAINER_TRAINING_RESULT_PASS = 1;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 343.

```text
E_REVIEW = 2;
}

enum MoveTrainerTrainingResult {
  MOVE_TRAINER_TRAINING_RESULT_UNSPECIFIED = 0;
  MOVE_TRAINER_TRAINING_RESULT_PASS = 1;
  MOVE_TRAINER_TRAINING_RESULT_FAILED = 2;
}

enum AccessRightMode {
  ACCESS_RIGHT_MODE_UNSPECIFIED = 0;
  ACCESS_RIGHT_MODE_FULL = 1;
  ACCESS_RIGHT_MODE_PREVIEW = 2;
}

message MoveTrainer {
  oneof _course_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspect course_gam
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02240"></a>
## FND-02240: chesscom.courses.v1.MoveTrainerTrainingResult.MOVE_TRAINER_TRAINING_RESULT_FAILED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOVE_TRAINER_TRAINING_RESULT_FAILED = 2;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 384.

```text
Result {
  MOVE_TRAINER_TRAINING_RESULT_UNSPECIFIED = 0;
  MOVE_TRAINER_TRAINING_RESULT_PASS = 1;
  MOVE_TRAINER_TRAINING_RESULT_FAILED = 2;
}

enum AccessRightMode {
  ACCESS_RIGHT_MODE_UNSPECIFIED = 0;
  ACCESS_RIGHT_MODE_FULL = 1;
  ACCESS_RIGHT_MODE_PREVIEW = 2;
}

message MoveTrainer {
  oneof _course_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspect course_game_aspect = 10;
  }
  oneof _coach {
  .ch
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02241"></a>
## FND-02241: enum declaration: chesscom.courses.v1.AccessRightMode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum AccessRightMode {

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 428.

```text
ECIFIED = 0;
  MOVE_TRAINER_TRAINING_RESULT_PASS = 1;
  MOVE_TRAINER_TRAINING_RESULT_FAILED = 2;
}

enum AccessRightMode {
  ACCESS_RIGHT_MODE_UNSPECIFIED = 0;
  ACCESS_RIGHT_MODE_FULL = 1;
  ACCESS_RIGHT_MODE_PREVIEW = 2;
}

message MoveTrainer {
  oneof _course_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspect course_game_aspect = 10;
  }
  oneof _coach {
  .chesscom.courses.v1.CourseCoach coach = 11;
  
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02242"></a>
## FND-02242: chesscom.courses.v1.AccessRightMode.ACCESS_RIGHT_MODE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ACCESS_RIGHT_MODE_UNSPECIFIED = 0;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 453.

```text
ER_TRAINING_RESULT_PASS = 1;
  MOVE_TRAINER_TRAINING_RESULT_FAILED = 2;
}

enum AccessRightMode {
  ACCESS_RIGHT_MODE_UNSPECIFIED = 0;
  ACCESS_RIGHT_MODE_FULL = 1;
  ACCESS_RIGHT_MODE_PREVIEW = 2;
}

message MoveTrainer {
  oneof _course_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspect course_game_aspect = 10;
  }
  oneof _coach {
  .chesscom.courses.v1.CourseCoach coach = 11;
  }
  oneof _learner_player
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02243"></a>
## FND-02243: chesscom.courses.v1.AccessRightMode.ACCESS_RIGHT_MODE_FULL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ACCESS_RIGHT_MODE_FULL = 1;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 490.

```text
RAINER_TRAINING_RESULT_FAILED = 2;
}

enum AccessRightMode {
  ACCESS_RIGHT_MODE_UNSPECIFIED = 0;
  ACCESS_RIGHT_MODE_FULL = 1;
  ACCESS_RIGHT_MODE_PREVIEW = 2;
}

message MoveTrainer {
  oneof _course_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspect course_game_aspect = 10;
  }
  oneof _coach {
  .chesscom.courses.v1.CourseCoach coach = 11;
  }
  oneof _learner_player {
  .chesscom.courses.v1.CourseLesso
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02244"></a>
## FND-02244: chesscom.courses.v1.AccessRightMode.ACCESS_RIGHT_MODE_PREVIEW = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ACCESS_RIGHT_MODE_PREVIEW = 2;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 520.

```text
= 2;
}

enum AccessRightMode {
  ACCESS_RIGHT_MODE_UNSPECIFIED = 0;
  ACCESS_RIGHT_MODE_FULL = 1;
  ACCESS_RIGHT_MODE_PREVIEW = 2;
}

message MoveTrainer {
  oneof _course_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspect course_game_aspect = 10;
  }
  oneof _coach {
  .chesscom.courses.v1.CourseCoach coach = 11;
  }
  oneof _learner_player {
  .chesscom.courses.v1.CourseLessonPlayer learner_player = 13;
 
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02245"></a>
## FND-02245: message declaration: chesscom.courses.v1.MoveTrainer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message MoveTrainer {

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 554.

```text
CCESS_RIGHT_MODE_UNSPECIFIED = 0;
  ACCESS_RIGHT_MODE_FULL = 1;
  ACCESS_RIGHT_MODE_PREVIEW = 2;
}

message MoveTrainer {
  oneof _course_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspect course_game_aspect = 10;
  }
  oneof _coach {
  .chesscom.courses.v1.CourseCoach coach = 11;
  }
  oneof _learner_player {
  .chesscom.courses.v1.CourseLessonPlayer learner_player = 13;
  }
  optional string id = 1;
  opt
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02246"></a>
## FND-02246: oneof declaration: chesscom.courses.v1.MoveTrainer._course_game_aspect

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _course_game_aspect {

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 578.

```text
FIED = 0;
  ACCESS_RIGHT_MODE_FULL = 1;
  ACCESS_RIGHT_MODE_PREVIEW = 2;
}

message MoveTrainer {
  oneof _course_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspect course_game_aspect = 10;
  }
  oneof _coach {
  .chesscom.courses.v1.CourseCoach coach = 11;
  }
  oneof _learner_player {
  .chesscom.courses.v1.CourseLessonPlayer learner_player = 13;
  }
  optional string id = 1;
  optional string name = 2;
 
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02247"></a>
## FND-02247: chesscom.courses.v1.MoveTrainer.course_game_aspect = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses_common.v1.CourseGameAspect course_game_aspect = 10;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 608.

```text
FULL = 1;
  ACCESS_RIGHT_MODE_PREVIEW = 2;
}

message MoveTrainer {
  oneof _course_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspect course_game_aspect = 10;
  }
  oneof _coach {
  .chesscom.courses.v1.CourseCoach coach = 11;
  }
  oneof _learner_player {
  .chesscom.courses.v1.CourseLessonPlayer learner_player = 13;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses_co
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02248"></a>
## FND-02248: oneof declaration: chesscom.courses.v1.MoveTrainer._coach

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _coach {

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 684.

```text
_course_game_aspect {
  .chesscom.courses_common.v1.CourseGameAspect course_game_aspect = 10;
  }
  oneof _coach {
  .chesscom.courses.v1.CourseCoach coach = 11;
  }
  oneof _learner_player {
  .chesscom.courses.v1.CourseLessonPlayer learner_player = 13;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  repeated .chesscom.courses.v1.CourseChapter c
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02249"></a>
## FND-02249: chesscom.courses.v1.MoveTrainer.coach = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseCoach coach = 11;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 701.

```text
ct {
  .chesscom.courses_common.v1.CourseGameAspect course_game_aspect = 10;
  }
  oneof _coach {
  .chesscom.courses.v1.CourseCoach coach = 11;
  }
  oneof _learner_player {
  .chesscom.courses.v1.CourseLessonPlayer learner_player = 13;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  repeated .chesscom.courses.v1.CourseChapter chapters = 4;
  re
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02250"></a>
## FND-02250: oneof declaration: chesscom.courses.v1.MoveTrainer._learner_player

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _learner_player {

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 752.

```text
 course_game_aspect = 10;
  }
  oneof _coach {
  .chesscom.courses.v1.CourseCoach coach = 11;
  }
  oneof _learner_player {
  .chesscom.courses.v1.CourseLessonPlayer learner_player = 13;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  repeated .chesscom.courses.v1.CourseChapter chapters = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02251"></a>
## FND-02251: chesscom.courses.v1.MoveTrainer.learner_player = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseLessonPlayer learner_player = 13;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 778.

```text
  }
  oneof _coach {
  .chesscom.courses.v1.CourseCoach coach = 11;
  }
  oneof _learner_player {
  .chesscom.courses.v1.CourseLessonPlayer learner_player = 13;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  repeated .chesscom.courses.v1.CourseChapter chapters = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional string slug 
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02252"></a>
## FND-02252: chesscom.courses.v1.MoveTrainer.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 845.

```text

  }
  oneof _learner_player {
  .chesscom.courses.v1.CourseLessonPlayer learner_player = 13;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  repeated .chesscom.courses.v1.CourseChapter chapters = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional string slug = 6;
  optional .chesscom.courses.v1.AccessRightMode access_right_m
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02253"></a>
## FND-02253: chesscom.courses.v1.MoveTrainer.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 871.

```text
er {
  .chesscom.courses.v1.CourseLessonPlayer learner_player = 13;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  repeated .chesscom.courses.v1.CourseChapter chapters = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional string slug = 6;
  optional .chesscom.courses.v1.AccessRightMode access_right_mode = 7;
  optional .chess
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02254"></a>
## FND-02254: chesscom.courses.v1.MoveTrainer.picture = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.Picture picture = 3;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 899.

```text
CourseLessonPlayer learner_player = 13;
  }
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  repeated .chesscom.courses.v1.CourseChapter chapters = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional string slug = 6;
  optional .chesscom.courses.v1.AccessRightMode access_right_mode = 7;
  optional .chesscom.courses.v1.CourseType co
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02255"></a>
## FND-02255: chesscom.courses.v1.MoveTrainer.chapters = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseChapter chapters = 4;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 959.

```text
g id = 1;
  optional string name = 2;
  optional .chesscom.courses_common.v1.Picture picture = 3;
  repeated .chesscom.courses.v1.CourseChapter chapters = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional string slug = 6;
  optional .chesscom.courses.v1.AccessRightMode access_right_mode = 7;
  optional .chesscom.courses.v1.CourseType course_type = 8;
  optional .chesscom.courses_common.v1.Course
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02256"></a>
## FND-02256: chesscom.courses.v1.MoveTrainer.authors = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseAuthor authors = 5;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 1019.

```text
ourses_common.v1.Picture picture = 3;
  repeated .chesscom.courses.v1.CourseChapter chapters = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional string slug = 6;
  optional .chesscom.courses.v1.AccessRightMode access_right_mode = 7;
  optional .chesscom.courses.v1.CourseType course_type = 8;
  optional .chesscom.courses_common.v1.CourseSource course_source = 9;
  optional .chesscom.courses.v1.Co
```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02257"></a>
## FND-02257: chesscom.courses.v1.MoveTrainer.slug = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string slug = 6;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 1077.

```text
.courses.v1.CourseChapter chapters = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional string slug = 6;
  optional .chesscom.courses.v1.AccessRightMode access_right_mode = 7;
  optional .chesscom.courses.v1.CourseType course_type = 8;
  optional .chesscom.courses_common.v1.CourseSource course_source = 9;
  optional .chesscom.courses.v1.CourseLessonPlayer author_player = 12;
}

```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02258"></a>
## FND-02258: chesscom.courses.v1.MoveTrainer.access_right_mode = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.AccessRightMode access_right_mode = 7;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 1105.

```text
apters = 4;
  repeated .chesscom.courses.v1.CourseAuthor authors = 5;
  optional string slug = 6;
  optional .chesscom.courses.v1.AccessRightMode access_right_mode = 7;
  optional .chesscom.courses.v1.CourseType course_type = 8;
  optional .chesscom.courses_common.v1.CourseSource course_source = 9;
  optional .chesscom.courses.v1.CourseLessonPlayer author_player = 12;
}

```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02259"></a>
## FND-02259: chesscom.courses.v1.MoveTrainer.course_type = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseType course_type = 8;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 1176.

```text
 optional string slug = 6;
  optional .chesscom.courses.v1.AccessRightMode access_right_mode = 7;
  optional .chesscom.courses.v1.CourseType course_type = 8;
  optional .chesscom.courses_common.v1.CourseSource course_source = 9;
  optional .chesscom.courses.v1.CourseLessonPlayer author_player = 12;
}

```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02260"></a>
## FND-02260: chesscom.courses.v1.MoveTrainer.course_source = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseSource course_source = 9;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 1236.

```text
ccessRightMode access_right_mode = 7;
  optional .chesscom.courses.v1.CourseType course_type = 8;
  optional .chesscom.courses_common.v1.CourseSource course_source = 9;
  optional .chesscom.courses.v1.CourseLessonPlayer author_player = 12;
}

```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02261"></a>
## FND-02261: chesscom.courses.v1.MoveTrainer.author_player = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseLessonPlayer author_player = 12;

### Evidence

- **SRC-0299** `research/proto/chesscom/courses/v1/move_trainer.proto` — [preserved redacted evidence](../evidence/text/f688ef6bb1e9e766b413edb370fafe4d43aae84f3a5c9f54e0db17a2d8cce8e6.proto)
  Character offset 1307.

```text
ourseType course_type = 8;
  optional .chesscom.courses_common.v1.CourseSource course_source = 9;
  optional .chesscom.courses.v1.CourseLessonPlayer author_player = 12;
}

```

**Source references:** SRC-0299, SRC-1270  
**URL references:** None independently associated  
**Related findings:** FND-02233, FND-02234, FND-02235

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02262"></a>
## FND-02262: message declaration: chesscom.courses.v1.Nag

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Nag {

### Evidence

- **SRC-0300** `research/proto/chesscom/courses/v1/nag.proto` — [preserved redacted evidence](../evidence/text/29a7ccf4e50e65aee679f79bee23cb01296e71c3caf44a54465c894abe3a1525.proto)
  Character offset 90.

```text
// source: chesscom/courses/v1/nag.proto
// syntax: proto3

package chesscom.courses.v1;

message Nag {
  optional string type = 1;
  optional int32 nag_id = 2;
}

```

**Source references:** SRC-0300, SRC-1271  
**URL references:** None independently associated  
**Related findings:** FND-02263, FND-02264

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02263"></a>
## FND-02263: chesscom.courses.v1.Nag.type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string type = 1;

### Evidence

- **SRC-0300** `research/proto/chesscom/courses/v1/nag.proto` — [preserved redacted evidence](../evidence/text/29a7ccf4e50e65aee679f79bee23cb01296e71c3caf44a54465c894abe3a1525.proto)
  Character offset 106.

```text
rce: chesscom/courses/v1/nag.proto
// syntax: proto3

package chesscom.courses.v1;

message Nag {
  optional string type = 1;
  optional int32 nag_id = 2;
}

```

**Source references:** SRC-0300, SRC-1271  
**URL references:** None independently associated  
**Related findings:** FND-02262, FND-02264

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02264"></a>
## FND-02264: chesscom.courses.v1.Nag.nag_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 nag_id = 2;

### Evidence

- **SRC-0300** `research/proto/chesscom/courses/v1/nag.proto` — [preserved redacted evidence](../evidence/text/29a7ccf4e50e65aee679f79bee23cb01296e71c3caf44a54465c894abe3a1525.proto)
  Character offset 134.

```text
.proto
// syntax: proto3

package chesscom.courses.v1;

message Nag {
  optional string type = 1;
  optional int32 nag_id = 2;
}

```

**Source references:** SRC-0300, SRC-1271  
**URL references:** None independently associated  
**Related findings:** FND-02262, FND-02263

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02265"></a>
## FND-02265: enum declaration: chesscom.courses.v1.OwnershipType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum OwnershipType {

### Evidence

- **SRC-0301** `research/proto/chesscom/courses/v1/ownership_type.proto` — [preserved redacted evidence](../evidence/text/367fb79b08dca40265ff5ce5e982e00307b68da76e157ab128b440b878286a96.proto)
  Character offset 101.

```text
/ source: chesscom/courses/v1/ownership_type.proto
// syntax: proto3

package chesscom.courses.v1;

enum OwnershipType {
  OWNERSHIP_TYPE_UNSPECIFIED = 0;
  OWNERSHIP_TYPE_ACQUIRED = 1;
  OWNERSHIP_TYPE_PREVIEW = 2;
  OWNERSHIP_TYPE_CLAIMED = 3;
  OWNERSHIP_TYPE_PURCHASED = 4;
}

```

**Source references:** SRC-0301, SRC-1272  
**URL references:** None independently associated  
**Related findings:** FND-02266, FND-02267

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02266"></a>
## FND-02266: chesscom.courses.v1.OwnershipType.OWNERSHIP_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

OWNERSHIP_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0301** `research/proto/chesscom/courses/v1/ownership_type.proto` — [preserved redacted evidence](../evidence/text/367fb79b08dca40265ff5ce5e982e00307b68da76e157ab128b440b878286a96.proto)
  Character offset 124.

```text
ses/v1/ownership_type.proto
// syntax: proto3

package chesscom.courses.v1;

enum OwnershipType {
  OWNERSHIP_TYPE_UNSPECIFIED = 0;
  OWNERSHIP_TYPE_ACQUIRED = 1;
  OWNERSHIP_TYPE_PREVIEW = 2;
  OWNERSHIP_TYPE_CLAIMED = 3;
  OWNERSHIP_TYPE_PURCHASED = 4;
}

```

**Source references:** SRC-0301, SRC-1272  
**URL references:** None independently associated  
**Related findings:** FND-02265, FND-02267

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02267"></a>
## FND-02267: chesscom.courses.v1.OwnershipType.OWNERSHIP_TYPE_ACQUIRED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

OWNERSHIP_TYPE_ACQUIRED = 1;

### Evidence

- **SRC-0301** `research/proto/chesscom/courses/v1/ownership_type.proto` — [preserved redacted evidence](../evidence/text/367fb79b08dca40265ff5ce5e982e00307b68da76e157ab128b440b878286a96.proto)
  Character offset 158.

```text
tax: proto3

package chesscom.courses.v1;

enum OwnershipType {
  OWNERSHIP_TYPE_UNSPECIFIED = 0;
  OWNERSHIP_TYPE_ACQUIRED = 1;
  OWNERSHIP_TYPE_PREVIEW = 2;
  OWNERSHIP_TYPE_CLAIMED = 3;
  OWNERSHIP_TYPE_PURCHASED = 4;
}

```

**Source references:** SRC-0301, SRC-1272  
**URL references:** None independently associated  
**Related findings:** FND-02265, FND-02266

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02268"></a>
## FND-02268: chesscom.courses.v1.OwnershipType.OWNERSHIP_TYPE_PREVIEW = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

OWNERSHIP_TYPE_PREVIEW = 2;

### Evidence

- **SRC-0301** `research/proto/chesscom/courses/v1/ownership_type.proto` — [preserved redacted evidence](../evidence/text/367fb79b08dca40265ff5ce5e982e00307b68da76e157ab128b440b878286a96.proto)
  Character offset 189.

```text
ourses.v1;

enum OwnershipType {
  OWNERSHIP_TYPE_UNSPECIFIED = 0;
  OWNERSHIP_TYPE_ACQUIRED = 1;
  OWNERSHIP_TYPE_PREVIEW = 2;
  OWNERSHIP_TYPE_CLAIMED = 3;
  OWNERSHIP_TYPE_PURCHASED = 4;
}

```

**Source references:** SRC-0301, SRC-1272  
**URL references:** None independently associated  
**Related findings:** FND-02265, FND-02266, FND-02267

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02269"></a>
## FND-02269: chesscom.courses.v1.OwnershipType.OWNERSHIP_TYPE_CLAIMED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

OWNERSHIP_TYPE_CLAIMED = 3;

### Evidence

- **SRC-0301** `research/proto/chesscom/courses/v1/ownership_type.proto` — [preserved redacted evidence](../evidence/text/367fb79b08dca40265ff5ce5e982e00307b68da76e157ab128b440b878286a96.proto)
  Character offset 219.

```text
 {
  OWNERSHIP_TYPE_UNSPECIFIED = 0;
  OWNERSHIP_TYPE_ACQUIRED = 1;
  OWNERSHIP_TYPE_PREVIEW = 2;
  OWNERSHIP_TYPE_CLAIMED = 3;
  OWNERSHIP_TYPE_PURCHASED = 4;
}

```

**Source references:** SRC-0301, SRC-1272  
**URL references:** None independently associated  
**Related findings:** FND-02265, FND-02266, FND-02267

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02270"></a>
## FND-02270: chesscom.courses.v1.OwnershipType.OWNERSHIP_TYPE_PURCHASED = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

OWNERSHIP_TYPE_PURCHASED = 4;

### Evidence

- **SRC-0301** `research/proto/chesscom/courses/v1/ownership_type.proto` — [preserved redacted evidence](../evidence/text/367fb79b08dca40265ff5ce5e982e00307b68da76e157ab128b440b878286a96.proto)
  Character offset 249.

```text
D = 0;
  OWNERSHIP_TYPE_ACQUIRED = 1;
  OWNERSHIP_TYPE_PREVIEW = 2;
  OWNERSHIP_TYPE_CLAIMED = 3;
  OWNERSHIP_TYPE_PURCHASED = 4;
}

```

**Source references:** SRC-0301, SRC-1272  
**URL references:** None independently associated  
**Related findings:** FND-02265, FND-02266, FND-02267

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02271"></a>
## FND-02271: message declaration: chesscom.courses.v1.PriceRange

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PriceRange {

### Evidence

- **SRC-0302** `research/proto/chesscom/courses/v1/price_range.proto` — [preserved redacted evidence](../evidence/text/c3fa835b83c2e08d6e41294be0da9cef8f808193f8e263c9ed9d43a950657eb6.proto)
  Character offset 98.

```text
// source: chesscom/courses/v1/price_range.proto
// syntax: proto3

package chesscom.courses.v1;

message PriceRange {
  optional int32 from = 1;
  optional int32 to = 2;
  optional bool with_video = 3;
}

```

**Source references:** SRC-0302, SRC-1273  
**URL references:** None independently associated  
**Related findings:** FND-02272, FND-02273

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02272"></a>
## FND-02272: chesscom.courses.v1.PriceRange.from = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 from = 1;

### Evidence

- **SRC-0302** `research/proto/chesscom/courses/v1/price_range.proto` — [preserved redacted evidence](../evidence/text/c3fa835b83c2e08d6e41294be0da9cef8f808193f8e263c9ed9d43a950657eb6.proto)
  Character offset 121.

```text
ourses/v1/price_range.proto
// syntax: proto3

package chesscom.courses.v1;

message PriceRange {
  optional int32 from = 1;
  optional int32 to = 2;
  optional bool with_video = 3;
}

```

**Source references:** SRC-0302, SRC-1273  
**URL references:** None independently associated  
**Related findings:** FND-02271, FND-02273

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02273"></a>
## FND-02273: chesscom.courses.v1.PriceRange.to = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 to = 2;

### Evidence

- **SRC-0302** `research/proto/chesscom/courses/v1/price_range.proto` — [preserved redacted evidence](../evidence/text/c3fa835b83c2e08d6e41294be0da9cef8f808193f8e263c9ed9d43a950657eb6.proto)
  Character offset 148.

```text

// syntax: proto3

package chesscom.courses.v1;

message PriceRange {
  optional int32 from = 1;
  optional int32 to = 2;
  optional bool with_video = 3;
}

```

**Source references:** SRC-0302, SRC-1273  
**URL references:** None independently associated  
**Related findings:** FND-02271, FND-02272

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02274"></a>
## FND-02274: chesscom.courses.v1.PriceRange.with_video = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool with_video = 3;

### Evidence

- **SRC-0302** `research/proto/chesscom/courses/v1/price_range.proto` — [preserved redacted evidence](../evidence/text/c3fa835b83c2e08d6e41294be0da9cef8f808193f8e263c9ed9d43a950657eb6.proto)
  Character offset 173.

```text
ge chesscom.courses.v1;

message PriceRange {
  optional int32 from = 1;
  optional int32 to = 2;
  optional bool with_video = 3;
}

```

**Source references:** SRC-0302, SRC-1273  
**URL references:** None independently associated  
**Related findings:** FND-02271, FND-02272, FND-02273

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
