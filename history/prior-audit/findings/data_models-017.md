# data_models — findings 1601–1700

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-01875"></a>
## FND-01875: chesscom.courses.v1.GetDefaultMoveTrainerIdByProductIdRequest.product_id = 1

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

<a id="FND-01876"></a>
## FND-01876: message declaration: chesscom.courses.v1.GetDefaultMoveTrainerIdByProductIdResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetDefaultMoveTrainerIdByProductIdResponse {

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 583.

```text
id = 1;
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
  optional string course_id = 1;
}

message SetCourseActiveResponse {
}

```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866, FND-01867

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01877"></a>
## FND-01877: chesscom.courses.v1.GetDefaultMoveTrainerIdByProductIdResponse.default_move_trainer_id = 1

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

<a id="FND-01878"></a>
## FND-01878: chesscom.courses.v1.GetDefaultMoveTrainerIdByProductIdResponse.is_course_owned = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_course_owned = 2;

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 685.

```text
ssage GetDefaultMoveTrainerIdByProductIdResponse {
  optional string default_move_trainer_id = 1;
  optional bool is_course_owned = 2;
  optional bool is_video_owned = 3;
}

message SetCourseActiveRequest {
  optional string course_id = 1;
}

message SetCourseActiveResponse {
}

```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866, FND-01867

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01879"></a>
## FND-01879: chesscom.courses.v1.GetDefaultMoveTrainerIdByProductIdResponse.is_video_owned = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_video_owned = 3;

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 722.

```text
tIdResponse {
  optional string default_move_trainer_id = 1;
  optional bool is_course_owned = 2;
  optional bool is_video_owned = 3;
}

message SetCourseActiveRequest {
  optional string course_id = 1;
}

message SetCourseActiveResponse {
}

```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866, FND-01867

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01880"></a>
## FND-01880: message declaration: chesscom.courses.v1.SetCourseActiveRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetCourseActiveRequest {

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 759.

```text
lt_move_trainer_id = 1;
  optional bool is_course_owned = 2;
  optional bool is_video_owned = 3;
}

message SetCourseActiveRequest {
  optional string course_id = 1;
}

message SetCourseActiveResponse {
}

```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866, FND-01867

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01881"></a>
## FND-01881: chesscom.courses.v1.SetCourseActiveRequest.course_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_id = 1;

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 794.

```text
bool is_course_owned = 2;
  optional bool is_video_owned = 3;
}

message SetCourseActiveRequest {
  optional string course_id = 1;
}

message SetCourseActiveResponse {
}

```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866, FND-01867

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01882"></a>
## FND-01882: message declaration: chesscom.courses.v1.SetCourseActiveResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetCourseActiveResponse {

### Evidence

- **SRC-0281** `research/proto/chesscom/courses/v1/course_product_details_service.proto` — [preserved redacted evidence](../evidence/text/e331f8bcb5f93359e6b74de3698e49db94b7b937262158fa14303b9615e04132.proto)
  Character offset 828.

```text
al bool is_video_owned = 3;
}

message SetCourseActiveRequest {
  optional string course_id = 1;
}

message SetCourseActiveResponse {
}

```

**Source references:** SRC-0281, SRC-1252  
**URL references:** None independently associated  
**Related findings:** FND-01865, FND-01866, FND-01867

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01883"></a>
## FND-01883: enum declaration: chesscom.courses.v1.RecommendationReason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum RecommendationReason {

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 108.

```text
e: chesscom/courses/v1/course_recommendation.proto
// syntax: proto3

package chesscom.courses.v1;

enum RecommendationReason {
  RECOMMENDATION_REASON_UNSPECIFIED = 0;
  RECOMMENDATION_REASON_LAST_BOOK_MOVE = 1;
  RECOMMENDATION_REASON_FIRST_MISTAKE = 2;
}

message CourseRecommendation {
  optional string coach_text = 1;
  optional string variation_preview_url = 2;
  optional string course_name = 3;
  optional strin
```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01884, FND-01885

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01884"></a>
## FND-01884: chesscom.courses.v1.RecommendationReason.RECOMMENDATION_REASON_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RECOMMENDATION_REASON_UNSPECIFIED = 0;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 138.

```text
recommendation.proto
// syntax: proto3

package chesscom.courses.v1;

enum RecommendationReason {
  RECOMMENDATION_REASON_UNSPECIFIED = 0;
  RECOMMENDATION_REASON_LAST_BOOK_MOVE = 1;
  RECOMMENDATION_REASON_FIRST_MISTAKE = 2;
}

message CourseRecommendation {
  optional string coach_text = 1;
  optional string variation_preview_url = 2;
  optional string course_name = 3;
  optional string author_name = 4;
  optional 
```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01885

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01885"></a>
## FND-01885: chesscom.courses.v1.RecommendationReason.RECOMMENDATION_REASON_LAST_BOOK_MOVE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RECOMMENDATION_REASON_LAST_BOOK_MOVE = 1;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 179.

```text
ackage chesscom.courses.v1;

enum RecommendationReason {
  RECOMMENDATION_REASON_UNSPECIFIED = 0;
  RECOMMENDATION_REASON_LAST_BOOK_MOVE = 1;
  RECOMMENDATION_REASON_FIRST_MISTAKE = 2;
}

message CourseRecommendation {
  optional string coach_text = 1;
  optional string variation_preview_url = 2;
  optional string course_name = 3;
  optional string author_name = 4;
  optional string course_id = 5;
  optional string c
```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01886"></a>
## FND-01886: chesscom.courses.v1.RecommendationReason.RECOMMENDATION_REASON_FIRST_MISTAKE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

RECOMMENDATION_REASON_FIRST_MISTAKE = 2;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 223.

```text
tionReason {
  RECOMMENDATION_REASON_UNSPECIFIED = 0;
  RECOMMENDATION_REASON_LAST_BOOK_MOVE = 1;
  RECOMMENDATION_REASON_FIRST_MISTAKE = 2;
}

message CourseRecommendation {
  optional string coach_text = 1;
  optional string variation_preview_url = 2;
  optional string course_name = 3;
  optional string author_name = 4;
  optional string course_id = 5;
  optional string course_url = 6;
  optional string cover_image
```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01887"></a>
## FND-01887: message declaration: chesscom.courses.v1.CourseRecommendation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseRecommendation {

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 267.

```text
FIED = 0;
  RECOMMENDATION_REASON_LAST_BOOK_MOVE = 1;
  RECOMMENDATION_REASON_FIRST_MISTAKE = 2;
}

message CourseRecommendation {
  optional string coach_text = 1;
  optional string variation_preview_url = 2;
  optional string course_name = 3;
  optional string author_name = 4;
  optional string course_id = 5;
  optional string course_url = 6;
  optional string cover_image_url = 7;
  optional float rating = 8;
  opt
```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01888"></a>
## FND-01888: chesscom.courses.v1.CourseRecommendation.coach_text = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coach_text = 1;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 300.

```text
_LAST_BOOK_MOVE = 1;
  RECOMMENDATION_REASON_FIRST_MISTAKE = 2;
}

message CourseRecommendation {
  optional string coach_text = 1;
  optional string variation_preview_url = 2;
  optional string course_name = 3;
  optional string author_name = 4;
  optional string course_id = 5;
  optional string course_url = 6;
  optional string cover_image_url = 7;
  optional float rating = 8;
  optional int32 review_count = 9;
  o
```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01889"></a>
## FND-01889: chesscom.courses.v1.CourseRecommendation.variation_preview_url = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string variation_preview_url = 2;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 334.

```text
ION_REASON_FIRST_MISTAKE = 2;
}

message CourseRecommendation {
  optional string coach_text = 1;
  optional string variation_preview_url = 2;
  optional string course_name = 3;
  optional string author_name = 4;
  optional string course_id = 5;
  optional string course_url = 6;
  optional string cover_image_url = 7;
  optional float rating = 8;
  optional int32 review_count = 9;
  optional string short_description =
```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01890"></a>
## FND-01890: chesscom.courses.v1.CourseRecommendation.course_name = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_name = 3;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 379.

```text
seRecommendation {
  optional string coach_text = 1;
  optional string variation_preview_url = 2;
  optional string course_name = 3;
  optional string author_name = 4;
  optional string course_id = 5;
  optional string course_url = 6;
  optional string cover_image_url = 7;
  optional float rating = 8;
  optional int32 review_count = 9;
  optional string short_description = 10;
}

message CourseSummary {
  optional st
```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01891"></a>
## FND-01891: chesscom.courses.v1.CourseRecommendation.author_name = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string author_name = 4;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 414.

```text
g coach_text = 1;
  optional string variation_preview_url = 2;
  optional string course_name = 3;
  optional string author_name = 4;
  optional string course_id = 5;
  optional string course_url = 6;
  optional string cover_image_url = 7;
  optional float rating = 8;
  optional int32 review_count = 9;
  optional string short_description = 10;
}

message CourseSummary {
  optional string variation_preview_url = 1;
  o
```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01892"></a>
## FND-01892: chesscom.courses.v1.CourseRecommendation.course_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_id = 5;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 449.

```text
 variation_preview_url = 2;
  optional string course_name = 3;
  optional string author_name = 4;
  optional string course_id = 5;
  optional string course_url = 6;
  optional string cover_image_url = 7;
  optional float rating = 8;
  optional int32 review_count = 9;
  optional string short_description = 10;
}

message CourseSummary {
  optional string variation_preview_url = 1;
  optional string course_name = 2;
  o
```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01893"></a>
## FND-01893: chesscom.courses.v1.CourseRecommendation.course_url = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_url = 6;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 482.

```text
ional string course_name = 3;
  optional string author_name = 4;
  optional string course_id = 5;
  optional string course_url = 6;
  optional string cover_image_url = 7;
  optional float rating = 8;
  optional int32 review_count = 9;
  optional string short_description = 10;
}

message CourseSummary {
  optional string variation_preview_url = 1;
  optional string course_name = 2;
  optional string author_name = 3;
 
```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01894"></a>
## FND-01894: chesscom.courses.v1.CourseRecommendation.cover_image_url = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string cover_image_url = 7;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 516.

```text
tional string author_name = 4;
  optional string course_id = 5;
  optional string course_url = 6;
  optional string cover_image_url = 7;
  optional float rating = 8;
  optional int32 review_count = 9;
  optional string short_description = 10;
}

message CourseSummary {
  optional string variation_preview_url = 1;
  optional string course_name = 2;
  optional string author_name = 3;
  optional float rating = 4;
  opti
```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01895"></a>
## FND-01895: chesscom.courses.v1.CourseRecommendation.rating = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float rating = 8;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 555.

```text
al string course_id = 5;
  optional string course_url = 6;
  optional string cover_image_url = 7;
  optional float rating = 8;
  optional int32 review_count = 9;
  optional string short_description = 10;
}

message CourseSummary {
  optional string variation_preview_url = 1;
  optional string course_name = 2;
  optional string author_name = 3;
  optional float rating = 4;
  optional int32 num_reviews = 5;
  optional 
```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01896"></a>
## FND-01896: chesscom.courses.v1.CourseRecommendation.review_count = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 review_count = 9;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 584.

```text
tional string course_url = 6;
  optional string cover_image_url = 7;
  optional float rating = 8;
  optional int32 review_count = 9;
  optional string short_description = 10;
}

message CourseSummary {
  optional string variation_preview_url = 1;
  optional string course_name = 2;
  optional string author_name = 3;
  optional float rating = 4;
  optional int32 num_reviews = 5;
  optional string thumbnail_url = 6;
}

```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01897"></a>
## FND-01897: chesscom.courses.v1.CourseRecommendation.short_description = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string short_description = 10;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 619.

```text
ional string cover_image_url = 7;
  optional float rating = 8;
  optional int32 review_count = 9;
  optional string short_description = 10;
}

message CourseSummary {
  optional string variation_preview_url = 1;
  optional string course_name = 2;
  optional string author_name = 3;
  optional float rating = 4;
  optional int32 num_reviews = 5;
  optional string thumbnail_url = 6;
}

```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01898"></a>
## FND-01898: message declaration: chesscom.courses.v1.CourseSummary

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseSummary {

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 662.

```text
l float rating = 8;
  optional int32 review_count = 9;
  optional string short_description = 10;
}

message CourseSummary {
  optional string variation_preview_url = 1;
  optional string course_name = 2;
  optional string author_name = 3;
  optional float rating = 4;
  optional int32 num_reviews = 5;
  optional string thumbnail_url = 6;
}

```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01899"></a>
## FND-01899: chesscom.courses.v1.CourseSummary.variation_preview_url = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string variation_preview_url = 1;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 688.

```text
onal int32 review_count = 9;
  optional string short_description = 10;
}

message CourseSummary {
  optional string variation_preview_url = 1;
  optional string course_name = 2;
  optional string author_name = 3;
  optional float rating = 4;
  optional int32 num_reviews = 5;
  optional string thumbnail_url = 6;
}

```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01900"></a>
## FND-01900: chesscom.courses.v1.CourseSummary.course_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_name = 2;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 733.

```text
g short_description = 10;
}

message CourseSummary {
  optional string variation_preview_url = 1;
  optional string course_name = 2;
  optional string author_name = 3;
  optional float rating = 4;
  optional int32 num_reviews = 5;
  optional string thumbnail_url = 6;
}

```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01901"></a>
## FND-01901: chesscom.courses.v1.CourseSummary.author_name = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string author_name = 3;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 768.

```text
e CourseSummary {
  optional string variation_preview_url = 1;
  optional string course_name = 2;
  optional string author_name = 3;
  optional float rating = 4;
  optional int32 num_reviews = 5;
  optional string thumbnail_url = 6;
}

```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01902"></a>
## FND-01902: chesscom.courses.v1.CourseSummary.rating = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float rating = 4;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 803.

```text
 variation_preview_url = 1;
  optional string course_name = 2;
  optional string author_name = 3;
  optional float rating = 4;
  optional int32 num_reviews = 5;
  optional string thumbnail_url = 6;
}

```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01903"></a>
## FND-01903: chesscom.courses.v1.CourseSummary.num_reviews = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 num_reviews = 5;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 832.

```text
 optional string course_name = 2;
  optional string author_name = 3;
  optional float rating = 4;
  optional int32 num_reviews = 5;
  optional string thumbnail_url = 6;
}

```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01904"></a>
## FND-01904: chesscom.courses.v1.CourseSummary.thumbnail_url = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string thumbnail_url = 6;

### Evidence

- **SRC-0282** `research/proto/chesscom/courses/v1/course_recommendation.proto` — [preserved redacted evidence](../evidence/text/e3b40d50ca95149d1010c9467b3593a32bbd31c94659f6c528a5d437a8992e70.proto)
  Character offset 866.

```text
  optional string author_name = 3;
  optional float rating = 4;
  optional int32 num_reviews = 5;
  optional string thumbnail_url = 6;
}

```

**Source references:** SRC-0282, SRC-1253  
**URL references:** None independently associated  
**Related findings:** FND-01883, FND-01884, FND-01885

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01905"></a>
## FND-01905: message declaration: chesscom.courses.v1.GetCourseRecommendationForPositionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseRecommendationForPositionRequest {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 116.

```text
com/courses/v1/course_recommendation_service.proto
// syntax: proto3

package chesscom.courses.v1;

message GetCourseRecommendationForPositionRequest {
  oneof _rating {
  int32 rating = 1;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 2;
  }
  oneof _eco_code {
  string eco_code = 6;
  }
  optional string fen = 3;
  optional .chesscom.courses.v1.RecommendationReason reason = 4;
  optional string user_id = 
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01906"></a>
## FND-01906: oneof declaration: chesscom.courses.v1.GetCourseRecommendationForPositionRequest._rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 170.

```text
syntax: proto3

package chesscom.courses.v1;

message GetCourseRecommendationForPositionRequest {
  oneof _rating {
  int32 rating = 1;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 2;
  }
  oneof _eco_code {
  string eco_code = 6;
  }
  optional string fen = 3;
  optional .chesscom.courses.v1.RecommendationReason reason = 4;
  optional string user_id = 5;
}

message GetCourseRecommendationForPositionRespon
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01907"></a>
## FND-01907: chesscom.courses.v1.GetCourseRecommendationForPositionRequest.rating = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating = 1;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 188.

```text
ckage chesscom.courses.v1;

message GetCourseRecommendationForPositionRequest {
  oneof _rating {
  int32 rating = 1;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 2;
  }
  oneof _eco_code {
  string eco_code = 6;
  }
  optional string fen = 3;
  optional .chesscom.courses.v1.RecommendationReason reason = 4;
  optional string user_id = 5;
}

message GetCourseRecommendationForPositionResponse {
  oneof _cour
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01908"></a>
## FND-01908: oneof declaration: chesscom.courses.v1.GetCourseRecommendationForPositionRequest._color

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _color {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 212.

```text
1;

message GetCourseRecommendationForPositionRequest {
  oneof _rating {
  int32 rating = 1;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 2;
  }
  oneof _eco_code {
  string eco_code = 6;
  }
  optional string fen = 3;
  optional .chesscom.courses.v1.RecommendationReason reason = 4;
  optional string user_id = 5;
}

message GetCourseRecommendationForPositionResponse {
  oneof _course {
  .chesscom.courses
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01909"></a>
## FND-01909: chesscom.courses.v1.GetCourseRecommendationForPositionRequest.color = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Color color = 2;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 229.

```text
urseRecommendationForPositionRequest {
  oneof _rating {
  int32 rating = 1;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 2;
  }
  oneof _eco_code {
  string eco_code = 6;
  }
  optional string fen = 3;
  optional .chesscom.courses.v1.RecommendationReason reason = 4;
  optional string user_id = 5;
}

message GetCourseRecommendationForPositionResponse {
  oneof _course {
  .chesscom.courses.v1.CourseRecomme
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01910"></a>
## FND-01910: oneof declaration: chesscom.courses.v1.GetCourseRecommendationForPositionRequest._eco_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _eco_code {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 271.

```text
neof _rating {
  int32 rating = 1;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 2;
  }
  oneof _eco_code {
  string eco_code = 6;
  }
  optional string fen = 3;
  optional .chesscom.courses.v1.RecommendationReason reason = 4;
  optional string user_id = 5;
}

message GetCourseRecommendationForPositionResponse {
  oneof _course {
  .chesscom.courses.v1.CourseRecommendation course = 1;
  }
}

message GetCour
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01911"></a>
## FND-01911: chesscom.courses.v1.GetCourseRecommendationForPositionRequest.eco_code = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string eco_code = 6;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 291.

```text
32 rating = 1;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 2;
  }
  oneof _eco_code {
  string eco_code = 6;
  }
  optional string fen = 3;
  optional .chesscom.courses.v1.RecommendationReason reason = 4;
  optional string user_id = 5;
}

message GetCourseRecommendationForPositionResponse {
  oneof _course {
  .chesscom.courses.v1.CourseRecommendation course = 1;
  }
}

message GetCoursesForPositionReques
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01912"></a>
## FND-01912: chesscom.courses.v1.GetCourseRecommendationForPositionRequest.fen = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string fen = 3;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 318.

```text
_color {
  .chesscom.chess.v1.Color color = 2;
  }
  oneof _eco_code {
  string eco_code = 6;
  }
  optional string fen = 3;
  optional .chesscom.courses.v1.RecommendationReason reason = 4;
  optional string user_id = 5;
}

message GetCourseRecommendationForPositionResponse {
  oneof _course {
  .chesscom.courses.v1.CourseRecommendation course = 1;
  }
}

message GetCoursesForPositionRequest {
  oneof _color {
  .che
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01913"></a>
## FND-01913: chesscom.courses.v1.GetCourseRecommendationForPositionRequest.reason = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.RecommendationReason reason = 4;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 345.

```text
v1.Color color = 2;
  }
  oneof _eco_code {
  string eco_code = 6;
  }
  optional string fen = 3;
  optional .chesscom.courses.v1.RecommendationReason reason = 4;
  optional string user_id = 5;
}

message GetCourseRecommendationForPositionResponse {
  oneof _course {
  .chesscom.courses.v1.CourseRecommendation course = 1;
  }
}

message GetCoursesForPositionRequest {
  oneof _color {
  .chesscom.chess.v1.Color color 
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01914"></a>
## FND-01914: chesscom.courses.v1.GetCourseRecommendationForPositionRequest.user_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_id = 5;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 410.

```text
;
  }
  optional string fen = 3;
  optional .chesscom.courses.v1.RecommendationReason reason = 4;
  optional string user_id = 5;
}

message GetCourseRecommendationForPositionResponse {
  oneof _course {
  .chesscom.courses.v1.CourseRecommendation course = 1;
  }
}

message GetCoursesForPositionRequest {
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  optional string fen = 1;
  optional string user_id = 2
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01915"></a>
## FND-01915: message declaration: chesscom.courses.v1.GetCourseRecommendationForPositionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseRecommendationForPositionResponse {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 442.

```text

  optional .chesscom.courses.v1.RecommendationReason reason = 4;
  optional string user_id = 5;
}

message GetCourseRecommendationForPositionResponse {
  oneof _course {
  .chesscom.courses.v1.CourseRecommendation course = 1;
  }
}

message GetCoursesForPositionRequest {
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  optional string fen = 1;
  optional string user_id = 2;
}

message GetCoursesForPositi
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01916"></a>
## FND-01916: oneof declaration: chesscom.courses.v1.GetCourseRecommendationForPositionResponse._course

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _course {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 497.

```text
eason = 4;
  optional string user_id = 5;
}

message GetCourseRecommendationForPositionResponse {
  oneof _course {
  .chesscom.courses.v1.CourseRecommendation course = 1;
  }
}

message GetCoursesForPositionRequest {
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  optional string fen = 1;
  optional string user_id = 2;
}

message GetCoursesForPositionResponse {
  repeated .chesscom.courses.v1.CourseSumm
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01917"></a>
## FND-01917: chesscom.courses.v1.GetCourseRecommendationForPositionResponse.course = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseRecommendation course = 1;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 515.

```text
nal string user_id = 5;
}

message GetCourseRecommendationForPositionResponse {
  oneof _course {
  .chesscom.courses.v1.CourseRecommendation course = 1;
  }
}

message GetCoursesForPositionRequest {
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  optional string fen = 1;
  optional string user_id = 2;
}

message GetCoursesForPositionResponse {
  repeated .chesscom.courses.v1.CourseSummary courses = 1;
}
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01918"></a>
## FND-01918: message declaration: chesscom.courses.v1.GetCoursesForPositionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCoursesForPositionRequest {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 576.

```text
PositionResponse {
  oneof _course {
  .chesscom.courses.v1.CourseRecommendation course = 1;
  }
}

message GetCoursesForPositionRequest {
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  optional string fen = 1;
  optional string user_id = 2;
}

message GetCoursesForPositionResponse {
  repeated .chesscom.courses.v1.CourseSummary courses = 1;
}

message GetUserCourseRecommendationsRequest {
  oneof _limi
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01919"></a>
## FND-01919: oneof declaration: chesscom.courses.v1.GetCoursesForPositionRequest._color

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _color {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 212.

```text
1;

message GetCourseRecommendationForPositionRequest {
  oneof _rating {
  int32 rating = 1;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 2;
  }
  oneof _eco_code {
  string eco_code = 6;
  }
  optional string fen = 3;
  optional .chesscom.courses.v1.RecommendationReason reason = 4;
  optional string user_id = 5;
}

message GetCourseRecommendationForPositionResponse {
  oneof _course {
  .chesscom.courses
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01920"></a>
## FND-01920: chesscom.courses.v1.GetCoursesForPositionRequest.color = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Color color = 3;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 634.

```text
1.CourseRecommendation course = 1;
  }
}

message GetCoursesForPositionRequest {
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  optional string fen = 1;
  optional string user_id = 2;
}

message GetCoursesForPositionResponse {
  repeated .chesscom.courses.v1.CourseSummary courses = 1;
}

message GetUserCourseRecommendationsRequest {
  oneof _limit {
  int32 limit = 3;
  }
  optional string user_id = 1;

```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01921"></a>
## FND-01921: chesscom.courses.v1.GetCoursesForPositionRequest.fen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string fen = 1;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 676.

```text
message GetCoursesForPositionRequest {
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  optional string fen = 1;
  optional string user_id = 2;
}

message GetCoursesForPositionResponse {
  repeated .chesscom.courses.v1.CourseSummary courses = 1;
}

message GetUserCourseRecommendationsRequest {
  oneof _limit {
  int32 limit = 3;
  }
  optional string user_id = 1;
  optional .chesscom.courses.v1.Recommenda
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01922"></a>
## FND-01922: chesscom.courses.v1.GetCoursesForPositionRequest.user_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_id = 2;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 703.

```text
onRequest {
  oneof _color {
  .chesscom.chess.v1.Color color = 3;
  }
  optional string fen = 1;
  optional string user_id = 2;
}

message GetCoursesForPositionResponse {
  repeated .chesscom.courses.v1.CourseSummary courses = 1;
}

message GetUserCourseRecommendationsRequest {
  oneof _limit {
  int32 limit = 3;
  }
  optional string user_id = 1;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint =
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01923"></a>
## FND-01923: message declaration: chesscom.courses.v1.GetCoursesForPositionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCoursesForPositionResponse {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 735.

```text
chesscom.chess.v1.Color color = 3;
  }
  optional string fen = 1;
  optional string user_id = 2;
}

message GetCoursesForPositionResponse {
  repeated .chesscom.courses.v1.CourseSummary courses = 1;
}

message GetUserCourseRecommendationsRequest {
  oneof _limit {
  int32 limit = 3;
  }
  optional string user_id = 1;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 2;
}

message GetUserCourseReco
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01924"></a>
## FND-01924: chesscom.courses.v1.GetCoursesForPositionResponse.courses = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseSummary courses = 1;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 777.

```text
ptional string fen = 1;
  optional string user_id = 2;
}

message GetCoursesForPositionResponse {
  repeated .chesscom.courses.v1.CourseSummary courses = 1;
}

message GetUserCourseRecommendationsRequest {
  oneof _limit {
  int32 limit = 3;
  }
  optional string user_id = 1;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 2;
}

message GetUserCourseRecommendationsResponse {
  oneof _set_id {
  
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01925"></a>
## FND-01925: message declaration: chesscom.courses.v1.GetUserCourseRecommendationsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserCourseRecommendationsRequest {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 837.

```text
ssage GetCoursesForPositionResponse {
  repeated .chesscom.courses.v1.CourseSummary courses = 1;
}

message GetUserCourseRecommendationsRequest {
  oneof _limit {
  int32 limit = 3;
  }
  optional string user_id = 1;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 2;
}

message GetUserCourseRecommendationsResponse {
  oneof _set_id {
  string set_id = 1;
  }
  repeated .chesscom.courses.v1.Recom
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01926"></a>
## FND-01926: oneof declaration: chesscom.courses.v1.GetUserCourseRecommendationsRequest._limit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _limit {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 885.

```text
 .chesscom.courses.v1.CourseSummary courses = 1;
}

message GetUserCourseRecommendationsRequest {
  oneof _limit {
  int32 limit = 3;
  }
  optional string user_id = 1;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 2;
}

message GetUserCourseRecommendationsResponse {
  oneof _set_id {
  string set_id = 1;
  }
  repeated .chesscom.courses.v1.RecommendedCourse courses = 2;
  optional bool is_fal
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01927"></a>
## FND-01927: chesscom.courses.v1.GetUserCourseRecommendationsRequest.limit = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 limit = 3;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 902.

```text
s.v1.CourseSummary courses = 1;
}

message GetUserCourseRecommendationsRequest {
  oneof _limit {
  int32 limit = 3;
  }
  optional string user_id = 1;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 2;
}

message GetUserCourseRecommendationsResponse {
  oneof _set_id {
  string set_id = 1;
  }
  repeated .chesscom.courses.v1.RecommendedCourse courses = 2;
  optional bool is_fallback = 3;
}

mes
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01928"></a>
## FND-01928: chesscom.courses.v1.GetUserCourseRecommendationsRequest.user_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_id = 1;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 925.

```text
ses = 1;
}

message GetUserCourseRecommendationsRequest {
  oneof _limit {
  int32 limit = 3;
  }
  optional string user_id = 1;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 2;
}

message GetUserCourseRecommendationsResponse {
  oneof _set_id {
  string set_id = 1;
  }
  repeated .chesscom.courses.v1.RecommendedCourse courses = 2;
  optional bool is_fallback = 3;
}

message ReportRecommendati
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01929"></a>
## FND-01929: chesscom.courses.v1.GetUserCourseRecommendationsRequest.touchpoint = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 2;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 956.

```text
seRecommendationsRequest {
  oneof _limit {
  int32 limit = 3;
  }
  optional string user_id = 1;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 2;
}

message GetUserCourseRecommendationsResponse {
  oneof _set_id {
  string set_id = 1;
  }
  repeated .chesscom.courses.v1.RecommendedCourse courses = 2;
  optional bool is_fallback = 3;
}

message ReportRecommendationImpressionRequest {
  oneof _
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01930"></a>
## FND-01930: message declaration: chesscom.courses.v1.GetUserCourseRecommendationsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetUserCourseRecommendationsResponse {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 1030.

```text
nal string user_id = 1;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 2;
}

message GetUserCourseRecommendationsResponse {
  oneof _set_id {
  string set_id = 1;
  }
  repeated .chesscom.courses.v1.RecommendedCourse courses = 2;
  optional bool is_fallback = 3;
}

message ReportRecommendationImpressionRequest {
  oneof _set_id {
  string set_id = 2;
  }
  oneof _is_fallback {
  bool is_fallbac
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01931"></a>
## FND-01931: oneof declaration: chesscom.courses.v1.GetUserCourseRecommendationsResponse._set_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _set_id {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 1079.

```text
ses.v1.RecommendationTouchpoint touchpoint = 2;
}

message GetUserCourseRecommendationsResponse {
  oneof _set_id {
  string set_id = 1;
  }
  repeated .chesscom.courses.v1.RecommendedCourse courses = 2;
  optional bool is_fallback = 3;
}

message ReportRecommendationImpressionRequest {
  oneof _set_id {
  string set_id = 2;
  }
  oneof _is_fallback {
  bool is_fallback = 5;
  }
  optional string user_id = 1;
  repea
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01932"></a>
## FND-01932: chesscom.courses.v1.GetUserCourseRecommendationsResponse.set_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string set_id = 1;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 1097.

```text
ionTouchpoint touchpoint = 2;
}

message GetUserCourseRecommendationsResponse {
  oneof _set_id {
  string set_id = 1;
  }
  repeated .chesscom.courses.v1.RecommendedCourse courses = 2;
  optional bool is_fallback = 3;
}

message ReportRecommendationImpressionRequest {
  oneof _set_id {
  string set_id = 2;
  }
  oneof _is_fallback {
  bool is_fallback = 5;
  }
  optional string user_id = 1;
  repeated string course_
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01933"></a>
## FND-01933: chesscom.courses.v1.GetUserCourseRecommendationsResponse.courses = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.RecommendedCourse courses = 2;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 1122.

```text
= 2;
}

message GetUserCourseRecommendationsResponse {
  oneof _set_id {
  string set_id = 1;
  }
  repeated .chesscom.courses.v1.RecommendedCourse courses = 2;
  optional bool is_fallback = 3;
}

message ReportRecommendationImpressionRequest {
  oneof _set_id {
  string set_id = 2;
  }
  oneof _is_fallback {
  bool is_fallback = 5;
  }
  optional string user_id = 1;
  repeated string course_ids = 3;
  optional .ches
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01934"></a>
## FND-01934: chesscom.courses.v1.GetUserCourseRecommendationsResponse.is_fallback = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_fallback = 3;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 1185.

```text
_set_id {
  string set_id = 1;
  }
  repeated .chesscom.courses.v1.RecommendedCourse courses = 2;
  optional bool is_fallback = 3;
}

message ReportRecommendationImpressionRequest {
  oneof _set_id {
  string set_id = 2;
  }
  oneof _is_fallback {
  bool is_fallback = 5;
  }
  optional string user_id = 1;
  repeated string course_ids = 3;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 4;
}

mes
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01935"></a>
## FND-01935: message declaration: chesscom.courses.v1.ReportRecommendationImpressionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ReportRecommendationImpressionRequest {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 1219.

```text

  repeated .chesscom.courses.v1.RecommendedCourse courses = 2;
  optional bool is_fallback = 3;
}

message ReportRecommendationImpressionRequest {
  oneof _set_id {
  string set_id = 2;
  }
  oneof _is_fallback {
  bool is_fallback = 5;
  }
  optional string user_id = 1;
  repeated string course_ids = 3;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 4;
}

message ReportRecommendationImpressio
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01936"></a>
## FND-01936: oneof declaration: chesscom.courses.v1.ReportRecommendationImpressionRequest._set_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _set_id {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 1079.

```text
ses.v1.RecommendationTouchpoint touchpoint = 2;
}

message GetUserCourseRecommendationsResponse {
  oneof _set_id {
  string set_id = 1;
  }
  repeated .chesscom.courses.v1.RecommendedCourse courses = 2;
  optional bool is_fallback = 3;
}

message ReportRecommendationImpressionRequest {
  oneof _set_id {
  string set_id = 2;
  }
  oneof _is_fallback {
  bool is_fallback = 5;
  }
  optional string user_id = 1;
  repea
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01937"></a>
## FND-01937: chesscom.courses.v1.ReportRecommendationImpressionRequest.set_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string set_id = 2;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 1287.

```text
tional bool is_fallback = 3;
}

message ReportRecommendationImpressionRequest {
  oneof _set_id {
  string set_id = 2;
  }
  oneof _is_fallback {
  bool is_fallback = 5;
  }
  optional string user_id = 1;
  repeated string course_ids = 3;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 4;
}

message ReportRecommendationImpressionResponse {
}

```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01938"></a>
## FND-01938: oneof declaration: chesscom.courses.v1.ReportRecommendationImpressionRequest._is_fallback

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_fallback {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 1312.

```text
 3;
}

message ReportRecommendationImpressionRequest {
  oneof _set_id {
  string set_id = 2;
  }
  oneof _is_fallback {
  bool is_fallback = 5;
  }
  optional string user_id = 1;
  repeated string course_ids = 3;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 4;
}

message ReportRecommendationImpressionResponse {
}

```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01939"></a>
## FND-01939: chesscom.courses.v1.ReportRecommendationImpressionRequest.is_fallback = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_fallback = 5;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 1335.

```text
commendationImpressionRequest {
  oneof _set_id {
  string set_id = 2;
  }
  oneof _is_fallback {
  bool is_fallback = 5;
  }
  optional string user_id = 1;
  repeated string course_ids = 3;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 4;
}

message ReportRecommendationImpressionResponse {
}

```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01940"></a>
## FND-01940: chesscom.courses.v1.ReportRecommendationImpressionRequest.user_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_id = 1;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 925.

```text
ses = 1;
}

message GetUserCourseRecommendationsRequest {
  oneof _limit {
  int32 limit = 3;
  }
  optional string user_id = 1;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 2;
}

message GetUserCourseRecommendationsResponse {
  oneof _set_id {
  string set_id = 1;
  }
  repeated .chesscom.courses.v1.RecommendedCourse courses = 2;
  optional bool is_fallback = 3;
}

message ReportRecommendati
```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01941"></a>
## FND-01941: chesscom.courses.v1.ReportRecommendationImpressionRequest.course_ids = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string course_ids = 3;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 1394.

```text
set_id = 2;
  }
  oneof _is_fallback {
  bool is_fallback = 5;
  }
  optional string user_id = 1;
  repeated string course_ids = 3;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 4;
}

message ReportRecommendationImpressionResponse {
}

```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01942"></a>
## FND-01942: chesscom.courses.v1.ReportRecommendationImpressionRequest.touchpoint = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 4;

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 1428.

```text
ck {
  bool is_fallback = 5;
  }
  optional string user_id = 1;
  repeated string course_ids = 3;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 4;
}

message ReportRecommendationImpressionResponse {
}

```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01943"></a>
## FND-01943: message declaration: chesscom.courses.v1.ReportRecommendationImpressionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ReportRecommendationImpressionResponse {

### Evidence

- **SRC-0283** `research/proto/chesscom/courses/v1/course_recommendation_service.proto` — [preserved redacted evidence](../evidence/text/d720a899ff38996b2c0db28e8b2de08423eb8b78a0679fc414a31aa11bf6badd.proto)
  Character offset 1502.

```text
 string course_ids = 3;
  optional .chesscom.courses.v1.RecommendationTouchpoint touchpoint = 4;
}

message ReportRecommendationImpressionResponse {
}

```

**Source references:** SRC-0283, SRC-1254  
**URL references:** None independently associated  
**Related findings:** FND-01905, FND-01906, FND-01907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01944"></a>
## FND-01944: enum declaration: chesscom.courses.v1.CourseTag

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseTag {

### Evidence

- **SRC-0284** `research/proto/chesscom/courses/v1/course_tag.proto` — [preserved redacted evidence](../evidence/text/6055fffee94aae2b6eed45d30e1a0530335e400d86479dc922c2a19248b4ec37.proto)
  Character offset 97.

```text
// source: chesscom/courses/v1/course_tag.proto
// syntax: proto3

package chesscom.courses.v1;

enum CourseTag {
  COURSE_TAG_UNSPECIFIED = 0;
  COURSE_TAG_RECOMMENDED = 1;
  COURSE_TAG_BEST_SELLER = 2;
  COURSE_TAG_ON_SALE = 3;
  COURSE_TAG_VIDEO = 4;
  COURSE_TAG_DIAMOND_EXCLUSIVE = 5;
  COURSE_TAG_FREE = 6;
  COURSE_TAG_TOP_PLAYERS = 7;
}

```

**Source references:** SRC-0284, SRC-1255  
**URL references:** None independently associated  
**Related findings:** FND-01945, FND-01946

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01945"></a>
## FND-01945: chesscom.courses.v1.CourseTag.COURSE_TAG_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TAG_UNSPECIFIED = 0;

### Evidence

- **SRC-0284** `research/proto/chesscom/courses/v1/course_tag.proto` — [preserved redacted evidence](../evidence/text/6055fffee94aae2b6eed45d30e1a0530335e400d86479dc922c2a19248b4ec37.proto)
  Character offset 116.

```text
com/courses/v1/course_tag.proto
// syntax: proto3

package chesscom.courses.v1;

enum CourseTag {
  COURSE_TAG_UNSPECIFIED = 0;
  COURSE_TAG_RECOMMENDED = 1;
  COURSE_TAG_BEST_SELLER = 2;
  COURSE_TAG_ON_SALE = 3;
  COURSE_TAG_VIDEO = 4;
  COURSE_TAG_DIAMOND_EXCLUSIVE = 5;
  COURSE_TAG_FREE = 6;
  COURSE_TAG_TOP_PLAYERS = 7;
}

```

**Source references:** SRC-0284, SRC-1255  
**URL references:** None independently associated  
**Related findings:** FND-01944, FND-01946

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01946"></a>
## FND-01946: chesscom.courses.v1.CourseTag.COURSE_TAG_RECOMMENDED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TAG_RECOMMENDED = 1;

### Evidence

- **SRC-0284** `research/proto/chesscom/courses/v1/course_tag.proto` — [preserved redacted evidence](../evidence/text/6055fffee94aae2b6eed45d30e1a0530335e400d86479dc922c2a19248b4ec37.proto)
  Character offset 146.

```text
o
// syntax: proto3

package chesscom.courses.v1;

enum CourseTag {
  COURSE_TAG_UNSPECIFIED = 0;
  COURSE_TAG_RECOMMENDED = 1;
  COURSE_TAG_BEST_SELLER = 2;
  COURSE_TAG_ON_SALE = 3;
  COURSE_TAG_VIDEO = 4;
  COURSE_TAG_DIAMOND_EXCLUSIVE = 5;
  COURSE_TAG_FREE = 6;
  COURSE_TAG_TOP_PLAYERS = 7;
}

```

**Source references:** SRC-0284, SRC-1255  
**URL references:** None independently associated  
**Related findings:** FND-01944, FND-01945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01947"></a>
## FND-01947: chesscom.courses.v1.CourseTag.COURSE_TAG_BEST_SELLER = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TAG_BEST_SELLER = 2;

### Evidence

- **SRC-0284** `research/proto/chesscom/courses/v1/course_tag.proto` — [preserved redacted evidence](../evidence/text/6055fffee94aae2b6eed45d30e1a0530335e400d86479dc922c2a19248b4ec37.proto)
  Character offset 176.

```text
hesscom.courses.v1;

enum CourseTag {
  COURSE_TAG_UNSPECIFIED = 0;
  COURSE_TAG_RECOMMENDED = 1;
  COURSE_TAG_BEST_SELLER = 2;
  COURSE_TAG_ON_SALE = 3;
  COURSE_TAG_VIDEO = 4;
  COURSE_TAG_DIAMOND_EXCLUSIVE = 5;
  COURSE_TAG_FREE = 6;
  COURSE_TAG_TOP_PLAYERS = 7;
}

```

**Source references:** SRC-0284, SRC-1255  
**URL references:** None independently associated  
**Related findings:** FND-01944, FND-01945, FND-01946

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01948"></a>
## FND-01948: chesscom.courses.v1.CourseTag.COURSE_TAG_ON_SALE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TAG_ON_SALE = 3;

### Evidence

- **SRC-0284** `research/proto/chesscom/courses/v1/course_tag.proto` — [preserved redacted evidence](../evidence/text/6055fffee94aae2b6eed45d30e1a0530335e400d86479dc922c2a19248b4ec37.proto)
  Character offset 206.

```text
seTag {
  COURSE_TAG_UNSPECIFIED = 0;
  COURSE_TAG_RECOMMENDED = 1;
  COURSE_TAG_BEST_SELLER = 2;
  COURSE_TAG_ON_SALE = 3;
  COURSE_TAG_VIDEO = 4;
  COURSE_TAG_DIAMOND_EXCLUSIVE = 5;
  COURSE_TAG_FREE = 6;
  COURSE_TAG_TOP_PLAYERS = 7;
}

```

**Source references:** SRC-0284, SRC-1255  
**URL references:** None independently associated  
**Related findings:** FND-01944, FND-01945, FND-01946

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01949"></a>
## FND-01949: chesscom.courses.v1.CourseTag.COURSE_TAG_VIDEO = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TAG_VIDEO = 4;

### Evidence

- **SRC-0284** `research/proto/chesscom/courses/v1/course_tag.proto` — [preserved redacted evidence](../evidence/text/6055fffee94aae2b6eed45d30e1a0530335e400d86479dc922c2a19248b4ec37.proto)
  Character offset 232.

```text
CIFIED = 0;
  COURSE_TAG_RECOMMENDED = 1;
  COURSE_TAG_BEST_SELLER = 2;
  COURSE_TAG_ON_SALE = 3;
  COURSE_TAG_VIDEO = 4;
  COURSE_TAG_DIAMOND_EXCLUSIVE = 5;
  COURSE_TAG_FREE = 6;
  COURSE_TAG_TOP_PLAYERS = 7;
}

```

**Source references:** SRC-0284, SRC-1255  
**URL references:** None independently associated  
**Related findings:** FND-01944, FND-01945, FND-01946

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01950"></a>
## FND-01950: chesscom.courses.v1.CourseTag.COURSE_TAG_DIAMOND_EXCLUSIVE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TAG_DIAMOND_EXCLUSIVE = 5;

### Evidence

- **SRC-0284** `research/proto/chesscom/courses/v1/course_tag.proto` — [preserved redacted evidence](../evidence/text/6055fffee94aae2b6eed45d30e1a0530335e400d86479dc922c2a19248b4ec37.proto)
  Character offset 256.

```text
_RECOMMENDED = 1;
  COURSE_TAG_BEST_SELLER = 2;
  COURSE_TAG_ON_SALE = 3;
  COURSE_TAG_VIDEO = 4;
  COURSE_TAG_DIAMOND_EXCLUSIVE = 5;
  COURSE_TAG_FREE = 6;
  COURSE_TAG_TOP_PLAYERS = 7;
}

```

**Source references:** SRC-0284, SRC-1255  
**URL references:** None independently associated  
**Related findings:** FND-01944, FND-01945, FND-01946

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01951"></a>
## FND-01951: chesscom.courses.v1.CourseTag.COURSE_TAG_FREE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TAG_FREE = 6;

### Evidence

- **SRC-0284** `research/proto/chesscom/courses/v1/course_tag.proto` — [preserved redacted evidence](../evidence/text/6055fffee94aae2b6eed45d30e1a0530335e400d86479dc922c2a19248b4ec37.proto)
  Character offset 292.

```text
SELLER = 2;
  COURSE_TAG_ON_SALE = 3;
  COURSE_TAG_VIDEO = 4;
  COURSE_TAG_DIAMOND_EXCLUSIVE = 5;
  COURSE_TAG_FREE = 6;
  COURSE_TAG_TOP_PLAYERS = 7;
}

```

**Source references:** SRC-0284, SRC-1255  
**URL references:** None independently associated  
**Related findings:** FND-01944, FND-01945, FND-01946

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01952"></a>
## FND-01952: chesscom.courses.v1.CourseTag.COURSE_TAG_TOP_PLAYERS = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TAG_TOP_PLAYERS = 7;

### Evidence

- **SRC-0284** `research/proto/chesscom/courses/v1/course_tag.proto` — [preserved redacted evidence](../evidence/text/6055fffee94aae2b6eed45d30e1a0530335e400d86479dc922c2a19248b4ec37.proto)
  Character offset 315.

```text
G_ON_SALE = 3;
  COURSE_TAG_VIDEO = 4;
  COURSE_TAG_DIAMOND_EXCLUSIVE = 5;
  COURSE_TAG_FREE = 6;
  COURSE_TAG_TOP_PLAYERS = 7;
}

```

**Source references:** SRC-0284, SRC-1255  
**URL references:** None independently associated  
**Related findings:** FND-01944, FND-01945, FND-01946

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01953"></a>
## FND-01953: enum declaration: chesscom.courses.v1.CourseType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseType {

### Evidence

- **SRC-0285** `research/proto/chesscom/courses/v1/course_type.proto` — [preserved redacted evidence](../evidence/text/2b3eeaa9e3725607809e0cc97284ff17cda051933551cc68c8ff1c2e1c290d10.proto)
  Character offset 98.

```text
// source: chesscom/courses/v1/course_type.proto
// syntax: proto3

package chesscom.courses.v1;

enum CourseType {
  COURSE_TYPE_UNSPECIFIED = 0;
  COURSE_TYPE_FREE = 1;
  COURSE_TYPE_DIAMOND_EXCLUSIVE = 2;
  COURSE_TYPE_PAID = 3;
}

```

**Source references:** SRC-0285, SRC-1256  
**URL references:** None independently associated  
**Related findings:** FND-01954, FND-01955

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01954"></a>
## FND-01954: chesscom.courses.v1.CourseType.COURSE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0285** `research/proto/chesscom/courses/v1/course_type.proto` — [preserved redacted evidence](../evidence/text/2b3eeaa9e3725607809e0cc97284ff17cda051933551cc68c8ff1c2e1c290d10.proto)
  Character offset 118.

```text
m/courses/v1/course_type.proto
// syntax: proto3

package chesscom.courses.v1;

enum CourseType {
  COURSE_TYPE_UNSPECIFIED = 0;
  COURSE_TYPE_FREE = 1;
  COURSE_TYPE_DIAMOND_EXCLUSIVE = 2;
  COURSE_TYPE_PAID = 3;
}

```

**Source references:** SRC-0285, SRC-1256  
**URL references:** None independently associated  
**Related findings:** FND-01953, FND-01955

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01955"></a>
## FND-01955: chesscom.courses.v1.CourseType.COURSE_TYPE_FREE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TYPE_FREE = 1;

### Evidence

- **SRC-0285** `research/proto/chesscom/courses/v1/course_type.proto` — [preserved redacted evidence](../evidence/text/2b3eeaa9e3725607809e0cc97284ff17cda051933551cc68c8ff1c2e1c290d10.proto)
  Character offset 149.

```text
// syntax: proto3

package chesscom.courses.v1;

enum CourseType {
  COURSE_TYPE_UNSPECIFIED = 0;
  COURSE_TYPE_FREE = 1;
  COURSE_TYPE_DIAMOND_EXCLUSIVE = 2;
  COURSE_TYPE_PAID = 3;
}

```

**Source references:** SRC-0285, SRC-1256  
**URL references:** None independently associated  
**Related findings:** FND-01953, FND-01954

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01956"></a>
## FND-01956: chesscom.courses.v1.CourseType.COURSE_TYPE_DIAMOND_EXCLUSIVE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TYPE_DIAMOND_EXCLUSIVE = 2;

### Evidence

- **SRC-0285** `research/proto/chesscom/courses/v1/course_type.proto` — [preserved redacted evidence](../evidence/text/2b3eeaa9e3725607809e0cc97284ff17cda051933551cc68c8ff1c2e1c290d10.proto)
  Character offset 173.

```text
ge chesscom.courses.v1;

enum CourseType {
  COURSE_TYPE_UNSPECIFIED = 0;
  COURSE_TYPE_FREE = 1;
  COURSE_TYPE_DIAMOND_EXCLUSIVE = 2;
  COURSE_TYPE_PAID = 3;
}

```

**Source references:** SRC-0285, SRC-1256  
**URL references:** None independently associated  
**Related findings:** FND-01953, FND-01954, FND-01955

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01957"></a>
## FND-01957: chesscom.courses.v1.CourseType.COURSE_TYPE_PAID = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_TYPE_PAID = 3;

### Evidence

- **SRC-0285** `research/proto/chesscom/courses/v1/course_type.proto` — [preserved redacted evidence](../evidence/text/2b3eeaa9e3725607809e0cc97284ff17cda051933551cc68c8ff1c2e1c290d10.proto)
  Character offset 210.

```text
ype {
  COURSE_TYPE_UNSPECIFIED = 0;
  COURSE_TYPE_FREE = 1;
  COURSE_TYPE_DIAMOND_EXCLUSIVE = 2;
  COURSE_TYPE_PAID = 3;
}

```

**Source references:** SRC-0285, SRC-1256  
**URL references:** None independently associated  
**Related findings:** FND-01953, FND-01954, FND-01955

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01958"></a>
## FND-01958: message declaration: chesscom.courses.v1.CourseUserLearningInformation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseUserLearningInformation {

### Evidence

- **SRC-0286** `research/proto/chesscom/courses/v1/course_user_learning_information.proto` — [preserved redacted evidence](../evidence/text/5c93ed71c946ee81d7d38eb3f60f56f0815b92a8e8bbcc33a725b712c751da8d.proto)
  Character offset 119.

```text
/courses/v1/course_user_learning_information.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseUserLearningInformation {
  oneof _last_studied_at {
  .google.protobuf.Timestamp last_studied_at = 3;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 6;
  }
  optional int32 learned_variation_amount = 1;
  optional int32 review_ready_amount = 2;
  optional .google.protobuf.Tim
```

**Source references:** SRC-0286, SRC-1257  
**URL references:** None independently associated  
**Related findings:** FND-01959, FND-01960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01959"></a>
## FND-01959: oneof declaration: chesscom.courses.v1.CourseUserLearningInformation._last_studied_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_studied_at {

### Evidence

- **SRC-0286** `research/proto/chesscom/courses/v1/course_user_learning_information.proto` — [preserved redacted evidence](../evidence/text/5c93ed71c946ee81d7d38eb3f60f56f0815b92a8e8bbcc33a725b712c751da8d.proto)
  Character offset 161.

```text
on.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseUserLearningInformation {
  oneof _last_studied_at {
  .google.protobuf.Timestamp last_studied_at = 3;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 6;
  }
  optional int32 learned_variation_amount = 1;
  optional int32 review_ready_amount = 2;
  optional .google.protobuf.Timestamp acquired_at = 4;
  optional bool is
```

**Source references:** SRC-0286, SRC-1257  
**URL references:** None independently associated  
**Related findings:** FND-01958, FND-01960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01960"></a>
## FND-01960: chesscom.courses.v1.CourseUserLearningInformation.last_studied_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp last_studied_at = 3;

### Evidence

- **SRC-0286** `research/proto/chesscom/courses/v1/course_user_learning_information.proto` — [preserved redacted evidence](../evidence/text/5c93ed71c946ee81d7d38eb3f60f56f0815b92a8e8bbcc33a725b712c751da8d.proto)
  Character offset 188.

```text

package chesscom.courses.v1;

message CourseUserLearningInformation {
  oneof _last_studied_at {
  .google.protobuf.Timestamp last_studied_at = 3;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 6;
  }
  optional int32 learned_variation_amount = 1;
  optional int32 review_ready_amount = 2;
  optional .google.protobuf.Timestamp acquired_at = 4;
  optional bool is_paused = 5;
  optional boo
```

**Source references:** SRC-0286, SRC-1257  
**URL references:** None independently associated  
**Related findings:** FND-01958, FND-01959

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01961"></a>
## FND-01961: oneof declaration: chesscom.courses.v1.CourseUserLearningInformation._next_review_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _next_review_at {

### Evidence

- **SRC-0286** `research/proto/chesscom/courses/v1/course_user_learning_information.proto` — [preserved redacted evidence](../evidence/text/5c93ed71c946ee81d7d38eb3f60f56f0815b92a8e8bbcc33a725b712c751da8d.proto)
  Character offset 242.

```text
ingInformation {
  oneof _last_studied_at {
  .google.protobuf.Timestamp last_studied_at = 3;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 6;
  }
  optional int32 learned_variation_amount = 1;
  optional int32 review_ready_amount = 2;
  optional .google.protobuf.Timestamp acquired_at = 4;
  optional bool is_paused = 5;
  optional bool is_inactive = 7;
  optional int32 mastery_level = 8;
```

**Source references:** SRC-0286, SRC-1257  
**URL references:** None independently associated  
**Related findings:** FND-01958, FND-01959, FND-01960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01962"></a>
## FND-01962: chesscom.courses.v1.CourseUserLearningInformation.next_review_at = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp next_review_at = 6;

### Evidence

- **SRC-0286** `research/proto/chesscom/courses/v1/course_user_learning_information.proto` — [preserved redacted evidence](../evidence/text/5c93ed71c946ee81d7d38eb3f60f56f0815b92a8e8bbcc33a725b712c751da8d.proto)
  Character offset 268.

```text
last_studied_at {
  .google.protobuf.Timestamp last_studied_at = 3;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 6;
  }
  optional int32 learned_variation_amount = 1;
  optional int32 review_ready_amount = 2;
  optional .google.protobuf.Timestamp acquired_at = 4;
  optional bool is_paused = 5;
  optional bool is_inactive = 7;
  optional int32 mastery_level = 8;
  optional int32 max_mast
```

**Source references:** SRC-0286, SRC-1257  
**URL references:** None independently associated  
**Related findings:** FND-01958, FND-01959, FND-01960

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01963"></a>
## FND-01963: chesscom.courses.v1.CourseUserLearningInformation.learned_variation_amount = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 learned_variation_amount = 1;

### Evidence

- **SRC-0286** `research/proto/chesscom/courses/v1/course_user_learning_information.proto` — [preserved redacted evidence](../evidence/text/5c93ed71c946ee81d7d38eb3f60f56f0815b92a8e8bbcc33a725b712c751da8d.proto)
  Character offset 321.

```text
tudied_at = 3;
  }
  oneof _next_review_at {
  .google.protobuf.Timestamp next_review_at = 6;
  }
  optional int32 learned_variation_amount = 1;
  optional int32 review_ready_amount = 2;
  optional .google.protobuf.Timestamp acquired_at = 4;
  optional bool is_paused = 5;
  optional bool is_inactive = 7;
  optional int32 mastery_level = 8;
  optional int32 max_mastery_level = 9;
}

```

**Source references:** SRC-0286, SRC-1257  
**URL references:** None independently associated  
**Related findings:** FND-01958, FND-01959, FND-01960

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01964"></a>
## FND-01964: chesscom.courses.v1.CourseUserLearningInformation.review_ready_amount = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 review_ready_amount = 2;

### Evidence

- **SRC-0286** `research/proto/chesscom/courses/v1/course_user_learning_information.proto` — [preserved redacted evidence](../evidence/text/5c93ed71c946ee81d7d38eb3f60f56f0815b92a8e8bbcc33a725b712c751da8d.proto)
  Character offset 368.

```text
.google.protobuf.Timestamp next_review_at = 6;
  }
  optional int32 learned_variation_amount = 1;
  optional int32 review_ready_amount = 2;
  optional .google.protobuf.Timestamp acquired_at = 4;
  optional bool is_paused = 5;
  optional bool is_inactive = 7;
  optional int32 mastery_level = 8;
  optional int32 max_mastery_level = 9;
}

```

**Source references:** SRC-0286, SRC-1257  
**URL references:** None independently associated  
**Related findings:** FND-01958, FND-01959, FND-01960

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01965"></a>
## FND-01965: chesscom.courses.v1.CourseUserLearningInformation.acquired_at = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp acquired_at = 4;

### Evidence

- **SRC-0286** `research/proto/chesscom/courses/v1/course_user_learning_information.proto` — [preserved redacted evidence](../evidence/text/5c93ed71c946ee81d7d38eb3f60f56f0815b92a8e8bbcc33a725b712c751da8d.proto)
  Character offset 410.

```text
= 6;
  }
  optional int32 learned_variation_amount = 1;
  optional int32 review_ready_amount = 2;
  optional .google.protobuf.Timestamp acquired_at = 4;
  optional bool is_paused = 5;
  optional bool is_inactive = 7;
  optional int32 mastery_level = 8;
  optional int32 max_mastery_level = 9;
}

```

**Source references:** SRC-0286, SRC-1257  
**URL references:** None independently associated  
**Related findings:** FND-01958, FND-01959, FND-01960

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01966"></a>
## FND-01966: chesscom.courses.v1.CourseUserLearningInformation.is_paused = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_paused = 5;

### Evidence

- **SRC-0286** `research/proto/chesscom/courses/v1/course_user_learning_information.proto` — [preserved redacted evidence](../evidence/text/5c93ed71c946ee81d7d38eb3f60f56f0815b92a8e8bbcc33a725b712c751da8d.proto)
  Character offset 465.

```text

  optional int32 review_ready_amount = 2;
  optional .google.protobuf.Timestamp acquired_at = 4;
  optional bool is_paused = 5;
  optional bool is_inactive = 7;
  optional int32 mastery_level = 8;
  optional int32 max_mastery_level = 9;
}

```

**Source references:** SRC-0286, SRC-1257  
**URL references:** None independently associated  
**Related findings:** FND-01958, FND-01959, FND-01960

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01967"></a>
## FND-01967: chesscom.courses.v1.CourseUserLearningInformation.is_inactive = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_inactive = 7;

### Evidence

- **SRC-0286** `research/proto/chesscom/courses/v1/course_user_learning_information.proto` — [preserved redacted evidence](../evidence/text/5c93ed71c946ee81d7d38eb3f60f56f0815b92a8e8bbcc33a725b712c751da8d.proto)
  Character offset 496.

```text
amount = 2;
  optional .google.protobuf.Timestamp acquired_at = 4;
  optional bool is_paused = 5;
  optional bool is_inactive = 7;
  optional int32 mastery_level = 8;
  optional int32 max_mastery_level = 9;
}

```

**Source references:** SRC-0286, SRC-1257  
**URL references:** None independently associated  
**Related findings:** FND-01958, FND-01959, FND-01960

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01968"></a>
## FND-01968: chesscom.courses.v1.CourseUserLearningInformation.mastery_level = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 mastery_level = 8;

### Evidence

- **SRC-0286** `research/proto/chesscom/courses/v1/course_user_learning_information.proto` — [preserved redacted evidence](../evidence/text/5c93ed71c946ee81d7d38eb3f60f56f0815b92a8e8bbcc33a725b712c751da8d.proto)
  Character offset 529.

```text
otobuf.Timestamp acquired_at = 4;
  optional bool is_paused = 5;
  optional bool is_inactive = 7;
  optional int32 mastery_level = 8;
  optional int32 max_mastery_level = 9;
}

```

**Source references:** SRC-0286, SRC-1257  
**URL references:** None independently associated  
**Related findings:** FND-01958, FND-01959, FND-01960

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01969"></a>
## FND-01969: chesscom.courses.v1.CourseUserLearningInformation.max_mastery_level = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 max_mastery_level = 9;

### Evidence

- **SRC-0286** `research/proto/chesscom/courses/v1/course_user_learning_information.proto` — [preserved redacted evidence](../evidence/text/5c93ed71c946ee81d7d38eb3f60f56f0815b92a8e8bbcc33a725b712c751da8d.proto)
  Character offset 565.

```text
optional bool is_paused = 5;
  optional bool is_inactive = 7;
  optional int32 mastery_level = 8;
  optional int32 max_mastery_level = 9;
}

```

**Source references:** SRC-0286, SRC-1257  
**URL references:** None independently associated  
**Related findings:** FND-01958, FND-01959, FND-01960

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01970"></a>
## FND-01970: message declaration: chesscom.courses.v1.CourseVariation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseVariation {

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 103.

```text
source: chesscom/courses/v1/course_variation.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseVariation {
  oneof _video_start {
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
  .google.protobuf.Ti
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01971, FND-01972

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01971"></a>
## FND-01971: oneof declaration: chesscom.courses.v1.CourseVariation._video_start

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _video_start {

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 131.

```text
course_variation.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseVariation {
  oneof _video_start {
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
  .google.protobuf.Timestamp last_reviewed_at = 1
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01972

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01972"></a>
## FND-01972: chesscom.courses.v1.CourseVariation.video_start = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 video_start = 9;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 154.

```text
// syntax: proto3

package chesscom.courses.v1;

message CourseVariation {
  oneof _video_start {
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
  oneof _next_re
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01973"></a>
## FND-01973: oneof declaration: chesscom.courses.v1.CourseVariation._video_end

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _video_end {

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 183.

```text
esscom.courses.v1;

message CourseVariation {
  oneof _video_start {
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
  .google.protobuf.
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01974"></a>
## FND-01974: chesscom.courses.v1.CourseVariation.video_end = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 video_end = 10;

### Evidence

- **SRC-0287** `research/proto/chesscom/courses/v1/course_variation.proto` — [preserved redacted evidence](../evidence/text/18ec6333d99ba96bb99fca200a0ffcccb55f2ebeccd97461e0505d9e16cc3686.proto)
  Character offset 204.

```text
essage CourseVariation {
  oneof _video_start {
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
  .google.protobuf.Timestamp next_review
```

**Source references:** SRC-0287, SRC-1258  
**URL references:** None independently associated  
**Related findings:** FND-01970, FND-01971, FND-01972

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
