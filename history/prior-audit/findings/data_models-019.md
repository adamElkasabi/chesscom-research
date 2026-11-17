# data_models — findings 1801–1900

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-02075"></a>
## FND-02075: chesscom.courses.v1.SetCourseInactiveRequest.course_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_id = 1;

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 274.

```text
e {
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

message SetCourseUnpausedResponse {
}

message AssignTutorialRequest {
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02076"></a>
## FND-02076: message declaration: chesscom.courses.v1.SetCourseInactiveResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetCourseInactiveResponse {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 308.

```text
1.Course course_list = 1;
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

message SetCourseUnpausedResponse {
}

message AssignTutorialRequest {
  oneof _tutorial_category {
  .c
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02077"></a>
## FND-02077: message declaration: chesscom.courses.v1.SetCoursePausedRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetCoursePausedRequest {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 347.

```text
tCourseInactiveRequest {
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

message SetCourseUnpausedResponse {
}

message AssignTutorialRequest {
  oneof _tutorial_category {
  .chesscom.courses.v1.TutorialCategory tut
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02078"></a>
## FND-02078: chesscom.courses.v1.SetCoursePausedRequest.course_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_id = 1;

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 274.

```text
e {
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

message SetCourseUnpausedResponse {
}

message AssignTutorialRequest {
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02079"></a>
## FND-02079: message declaration: chesscom.courses.v1.SetCoursePausedResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetCoursePausedResponse {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 416.

```text
SetCourseInactiveResponse {
}

message SetCoursePausedRequest {
  optional string course_id = 1;
}

message SetCoursePausedResponse {
}

message SetCourseUnpausedRequest {
  optional string course_id = 1;
}

message SetCourseUnpausedResponse {
}

message AssignTutorialRequest {
  oneof _tutorial_category {
  .chesscom.courses.v1.TutorialCategory tutorial_category = 2;
  }
  optional int32 user_rating = 1;
  optional 
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02080"></a>
## FND-02080: message declaration: chesscom.courses.v1.SetCourseUnpausedRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetCourseUnpausedRequest {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 453.

```text
e SetCoursePausedRequest {
  optional string course_id = 1;
}

message SetCoursePausedResponse {
}

message SetCourseUnpausedRequest {
  optional string course_id = 1;
}

message SetCourseUnpausedResponse {
}

message AssignTutorialRequest {
  oneof _tutorial_category {
  .chesscom.courses.v1.TutorialCategory tutorial_category = 2;
  }
  optional int32 user_rating = 1;
  optional string course_id = 3;
}

message Assi
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02081"></a>
## FND-02081: chesscom.courses.v1.SetCourseUnpausedRequest.course_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_id = 1;

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 274.

```text
e {
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

message SetCourseUnpausedResponse {
}

message AssignTutorialRequest {
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02082"></a>
## FND-02082: message declaration: chesscom.courses.v1.SetCourseUnpausedResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetCourseUnpausedResponse {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 524.

```text
SetCoursePausedResponse {
}

message SetCourseUnpausedRequest {
  optional string course_id = 1;
}

message SetCourseUnpausedResponse {
}

message AssignTutorialRequest {
  oneof _tutorial_category {
  .chesscom.courses.v1.TutorialCategory tutorial_category = 2;
  }
  optional int32 user_rating = 1;
  optional string course_id = 3;
}

message AssignTutorialResponse {
  optional string default_move_trainer_id = 1;
}


```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02083"></a>
## FND-02083: message declaration: chesscom.courses.v1.AssignTutorialRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AssignTutorialRequest {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 563.

```text
tCourseUnpausedRequest {
  optional string course_id = 1;
}

message SetCourseUnpausedResponse {
}

message AssignTutorialRequest {
  oneof _tutorial_category {
  .chesscom.courses.v1.TutorialCategory tutorial_category = 2;
  }
  optional int32 user_rating = 1;
  optional string course_id = 3;
}

message AssignTutorialResponse {
  optional string default_move_trainer_id = 1;
}

message GetAvailableTutorialsRequest {

```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02084"></a>
## FND-02084: oneof declaration: chesscom.courses.v1.AssignTutorialRequest._tutorial_category

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tutorial_category {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 597.

```text
l string course_id = 1;
}

message SetCourseUnpausedResponse {
}

message AssignTutorialRequest {
  oneof _tutorial_category {
  .chesscom.courses.v1.TutorialCategory tutorial_category = 2;
  }
  optional int32 user_rating = 1;
  optional string course_id = 3;
}

message AssignTutorialResponse {
  optional string default_move_trainer_id = 1;
}

message GetAvailableTutorialsRequest {
  optional int32 user_rating = 1;

```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02085"></a>
## FND-02085: chesscom.courses.v1.AssignTutorialRequest.tutorial_category = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.TutorialCategory tutorial_category = 2;

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 626.

```text
ssage SetCourseUnpausedResponse {
}

message AssignTutorialRequest {
  oneof _tutorial_category {
  .chesscom.courses.v1.TutorialCategory tutorial_category = 2;
  }
  optional int32 user_rating = 1;
  optional string course_id = 3;
}

message AssignTutorialResponse {
  optional string default_move_trainer_id = 1;
}

message GetAvailableTutorialsRequest {
  optional int32 user_rating = 1;
}

message GetAvailableTutori
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02086"></a>
## FND-02086: chesscom.courses.v1.AssignTutorialRequest.user_rating = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 user_rating = 1;

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 693.

```text
{
  oneof _tutorial_category {
  .chesscom.courses.v1.TutorialCategory tutorial_category = 2;
  }
  optional int32 user_rating = 1;
  optional string course_id = 3;
}

message AssignTutorialResponse {
  optional string default_move_trainer_id = 1;
}

message GetAvailableTutorialsRequest {
  optional int32 user_rating = 1;
}

message GetAvailableTutorialsResponse {
  repeated .chesscom.courses.v1.CourseProduct course_
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02087"></a>
## FND-02087: chesscom.courses.v1.AssignTutorialRequest.course_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_id = 3;

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 727.

```text
chesscom.courses.v1.TutorialCategory tutorial_category = 2;
  }
  optional int32 user_rating = 1;
  optional string course_id = 3;
}

message AssignTutorialResponse {
  optional string default_move_trainer_id = 1;
}

message GetAvailableTutorialsRequest {
  optional int32 user_rating = 1;
}

message GetAvailableTutorialsResponse {
  repeated .chesscom.courses.v1.CourseProduct course_list = 1;
  repeated .chesscom.cou
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02088"></a>
## FND-02088: message declaration: chesscom.courses.v1.AssignTutorialResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AssignTutorialResponse {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 761.

```text
ry tutorial_category = 2;
  }
  optional int32 user_rating = 1;
  optional string course_id = 3;
}

message AssignTutorialResponse {
  optional string default_move_trainer_id = 1;
}

message GetAvailableTutorialsRequest {
  optional int32 user_rating = 1;
}

message GetAvailableTutorialsResponse {
  repeated .chesscom.courses.v1.CourseProduct course_list = 1;
  repeated .chesscom.courses.v1.GetAvailableTutorialsRespo
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02089"></a>
## FND-02089: chesscom.courses.v1.AssignTutorialResponse.default_move_trainer_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string default_move_trainer_id = 1;

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 796.

```text
ional int32 user_rating = 1;
  optional string course_id = 3;
}

message AssignTutorialResponse {
  optional string default_move_trainer_id = 1;
}

message GetAvailableTutorialsRequest {
  optional int32 user_rating = 1;
}

message GetAvailableTutorialsResponse {
  repeated .chesscom.courses.v1.CourseProduct course_list = 1;
  repeated .chesscom.courses.v1.GetAvailableTutorialsResponse.CourseListByCategoryEntry cours
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02090"></a>
## FND-02090: message declaration: chesscom.courses.v1.GetAvailableTutorialsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetAvailableTutorialsRequest {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 844.

```text
ourse_id = 3;
}

message AssignTutorialResponse {
  optional string default_move_trainer_id = 1;
}

message GetAvailableTutorialsRequest {
  optional int32 user_rating = 1;
}

message GetAvailableTutorialsResponse {
  repeated .chesscom.courses.v1.CourseProduct course_list = 1;
  repeated .chesscom.courses.v1.GetAvailableTutorialsResponse.CourseListByCategoryEntry course_list_by_category = 2;
  message CourseListByCa
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02091"></a>
## FND-02091: chesscom.courses.v1.GetAvailableTutorialsRequest.user_rating = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 user_rating = 1;

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 693.

```text
{
  oneof _tutorial_category {
  .chesscom.courses.v1.TutorialCategory tutorial_category = 2;
  }
  optional int32 user_rating = 1;
  optional string course_id = 3;
}

message AssignTutorialResponse {
  optional string default_move_trainer_id = 1;
}

message GetAvailableTutorialsRequest {
  optional int32 user_rating = 1;
}

message GetAvailableTutorialsResponse {
  repeated .chesscom.courses.v1.CourseProduct course_
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02092"></a>
## FND-02092: message declaration: chesscom.courses.v1.GetAvailableTutorialsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetAvailableTutorialsResponse {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 920.

```text
move_trainer_id = 1;
}

message GetAvailableTutorialsRequest {
  optional int32 user_rating = 1;
}

message GetAvailableTutorialsResponse {
  repeated .chesscom.courses.v1.CourseProduct course_list = 1;
  repeated .chesscom.courses.v1.GetAvailableTutorialsResponse.CourseListByCategoryEntry course_list_by_category = 2;
  message CourseListByCategoryEntry {
  optional string key = 1;
  optional .chesscom.courses.v1.Cou
```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02093"></a>
## FND-02093: chesscom.courses.v1.GetAvailableTutorialsResponse.course_list = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseProduct course_list = 1;

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 962.

```text
leTutorialsRequest {
  optional int32 user_rating = 1;
}

message GetAvailableTutorialsResponse {
  repeated .chesscom.courses.v1.CourseProduct course_list = 1;
  repeated .chesscom.courses.v1.GetAvailableTutorialsResponse.CourseListByCategoryEntry course_list_by_category = 2;
  message CourseListByCategoryEntry {
  optional string key = 1;
  optional .chesscom.courses.v1.CourseProductList value = 2;
  }
}

```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02094"></a>
## FND-02094: chesscom.courses.v1.GetAvailableTutorialsResponse.course_list_by_category = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.GetAvailableTutorialsResponse.CourseListByCategoryEntry course_list_by_category = 2;

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 1025.

```text
ge GetAvailableTutorialsResponse {
  repeated .chesscom.courses.v1.CourseProduct course_list = 1;
  repeated .chesscom.courses.v1.GetAvailableTutorialsResponse.CourseListByCategoryEntry course_list_by_category = 2;
  message CourseListByCategoryEntry {
  optional string key = 1;
  optional .chesscom.courses.v1.CourseProductList value = 2;
  }
}

```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02095"></a>
## FND-02095: message declaration: chesscom.courses.v1.GetAvailableTutorialsResponse.CourseListByCategoryEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseListByCategoryEntry {

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 1142.

```text
m.courses.v1.GetAvailableTutorialsResponse.CourseListByCategoryEntry course_list_by_category = 2;
  message CourseListByCategoryEntry {
  optional string key = 1;
  optional .chesscom.courses.v1.CourseProductList value = 2;
  }
}

```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02096"></a>
## FND-02096: chesscom.courses.v1.GetAvailableTutorialsResponse.CourseListByCategoryEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 1180.

```text
onse.CourseListByCategoryEntry course_list_by_category = 2;
  message CourseListByCategoryEntry {
  optional string key = 1;
  optional .chesscom.courses.v1.CourseProductList value = 2;
  }
}

```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02097"></a>
## FND-02097: chesscom.courses.v1.GetAvailableTutorialsResponse.CourseListByCategoryEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseProductList value = 2;

### Evidence

- **SRC-0291** `research/proto/chesscom/courses/v1/courses_dashboard_service.proto` — [preserved redacted evidence](../evidence/text/34230c431a2f5570b41b4d16f148fa284d877dd4e00cdd0c988b04c01cd14852.proto)
  Character offset 1207.

```text
try course_list_by_category = 2;
  message CourseListByCategoryEntry {
  optional string key = 1;
  optional .chesscom.courses.v1.CourseProductList value = 2;
  }
}

```

**Source references:** SRC-0291, SRC-1262  
**URL references:** None independently associated  
**Related findings:** FND-02071, FND-02072, FND-02073

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02098"></a>
## FND-02098: message declaration: chesscom.courses.v1.GetHasUserAccessToSkuRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetHasUserAccessToSkuRequest {

### Evidence

- **SRC-0292** `research/proto/chesscom/courses/v1/courses_has_user_access_to_sku_service.proto` — [preserved redacted evidence](../evidence/text/8f039776494b3245e158e3bf02626740688a2f2dc6aba21ca2d65742dd633ed9.proto)
  Character offset 125.

```text
es/v1/courses_has_user_access_to_sku_service.proto
// syntax: proto3

package chesscom.courses.v1;

message GetHasUserAccessToSkuRequest {
  optional string chesscom_user_id = 1;
  optional string sku = 2;
}

message GetHasUserAccessToSkuResponse {
  optional bool has_access = 1;
}

```

**Source references:** SRC-0292, SRC-1263  
**URL references:** None independently associated  
**Related findings:** FND-02099, FND-02100

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02099"></a>
## FND-02099: chesscom.courses.v1.GetHasUserAccessToSkuRequest.chesscom_user_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string chesscom_user_id = 1;

### Evidence

- **SRC-0292** `research/proto/chesscom/courses/v1/courses_has_user_access_to_sku_service.proto` — [preserved redacted evidence](../evidence/text/8f039776494b3245e158e3bf02626740688a2f2dc6aba21ca2d65742dd633ed9.proto)
  Character offset 166.

```text
ice.proto
// syntax: proto3

package chesscom.courses.v1;

message GetHasUserAccessToSkuRequest {
  optional string chesscom_user_id = 1;
  optional string sku = 2;
}

message GetHasUserAccessToSkuResponse {
  optional bool has_access = 1;
}

```

**Source references:** SRC-0292, SRC-1263  
**URL references:** None independently associated  
**Related findings:** FND-02098, FND-02100

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02100"></a>
## FND-02100: chesscom.courses.v1.GetHasUserAccessToSkuRequest.sku = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string sku = 2;

### Evidence

- **SRC-0292** `research/proto/chesscom/courses/v1/courses_has_user_access_to_sku_service.proto` — [preserved redacted evidence](../evidence/text/8f039776494b3245e158e3bf02626740688a2f2dc6aba21ca2d65742dd633ed9.proto)
  Character offset 206.

```text
sscom.courses.v1;

message GetHasUserAccessToSkuRequest {
  optional string chesscom_user_id = 1;
  optional string sku = 2;
}

message GetHasUserAccessToSkuResponse {
  optional bool has_access = 1;
}

```

**Source references:** SRC-0292, SRC-1263  
**URL references:** None independently associated  
**Related findings:** FND-02098, FND-02099

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02101"></a>
## FND-02101: message declaration: chesscom.courses.v1.GetHasUserAccessToSkuResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetHasUserAccessToSkuResponse {

### Evidence

- **SRC-0292** `research/proto/chesscom/courses/v1/courses_has_user_access_to_sku_service.proto` — [preserved redacted evidence](../evidence/text/8f039776494b3245e158e3bf02626740688a2f2dc6aba21ca2d65742dd633ed9.proto)
  Character offset 234.

```text
etHasUserAccessToSkuRequest {
  optional string chesscom_user_id = 1;
  optional string sku = 2;
}

message GetHasUserAccessToSkuResponse {
  optional bool has_access = 1;
}

```

**Source references:** SRC-0292, SRC-1263  
**URL references:** None independently associated  
**Related findings:** FND-02098, FND-02099, FND-02100

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02102"></a>
## FND-02102: chesscom.courses.v1.GetHasUserAccessToSkuResponse.has_access = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool has_access = 1;

### Evidence

- **SRC-0292** `research/proto/chesscom/courses/v1/courses_has_user_access_to_sku_service.proto` — [preserved redacted evidence](../evidence/text/8f039776494b3245e158e3bf02626740688a2f2dc6aba21ca2d65742dd633ed9.proto)
  Character offset 276.

```text
tring chesscom_user_id = 1;
  optional string sku = 2;
}

message GetHasUserAccessToSkuResponse {
  optional bool has_access = 1;
}

```

**Source references:** SRC-0292, SRC-1263  
**URL references:** None independently associated  
**Related findings:** FND-02098, FND-02099, FND-02100

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02103"></a>
## FND-02103: message declaration: chesscom.courses.v1.GetPreviewsInformationRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetPreviewsInformationRequest {

### Evidence

- **SRC-0293** `research/proto/chesscom/courses/v1/courses_previews_information_service.proto` — [preserved redacted evidence](../evidence/text/8370fe997da8ad024ffb6904fba3990805789066a6ca600a08b6c967abded08d.proto)
  Character offset 123.

```text
rses/v1/courses_previews_information_service.proto
// syntax: proto3

package chesscom.courses.v1;

message GetPreviewsInformationRequest {
}

message GetPreviewsInformationResponse {
  oneof _total_amount {
  int32 total_amount = 2;
  }
  oneof _variation_resets_in_days_amount {
  int32 variation_resets_in_days_amount = 3;
  }
  optional int32 used_amount = 1;
  optional int32 period = 4;
  optional int32 max_previe
```

**Source references:** SRC-0293, SRC-1264  
**URL references:** None independently associated  
**Related findings:** FND-02104, FND-02105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02104"></a>
## FND-02104: message declaration: chesscom.courses.v1.GetPreviewsInformationResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetPreviewsInformationResponse {

### Evidence

- **SRC-0293** `research/proto/chesscom/courses/v1/courses_previews_information_service.proto` — [preserved redacted evidence](../evidence/text/8370fe997da8ad024ffb6904fba3990805789066a6ca600a08b6c967abded08d.proto)
  Character offset 166.

```text
e.proto
// syntax: proto3

package chesscom.courses.v1;

message GetPreviewsInformationRequest {
}

message GetPreviewsInformationResponse {
  oneof _total_amount {
  int32 total_amount = 2;
  }
  oneof _variation_resets_in_days_amount {
  int32 variation_resets_in_days_amount = 3;
  }
  optional int32 used_amount = 1;
  optional int32 period = 4;
  optional int32 max_previews_per_course = 5;
}

```

**Source references:** SRC-0293, SRC-1264  
**URL references:** None independently associated  
**Related findings:** FND-02103, FND-02105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02105"></a>
## FND-02105: oneof declaration: chesscom.courses.v1.GetPreviewsInformationResponse._total_amount

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _total_amount {

### Evidence

- **SRC-0293** `research/proto/chesscom/courses/v1/courses_previews_information_service.proto` — [preserved redacted evidence](../evidence/text/8370fe997da8ad024ffb6904fba3990805789066a6ca600a08b6c967abded08d.proto)
  Character offset 209.

```text
.courses.v1;

message GetPreviewsInformationRequest {
}

message GetPreviewsInformationResponse {
  oneof _total_amount {
  int32 total_amount = 2;
  }
  oneof _variation_resets_in_days_amount {
  int32 variation_resets_in_days_amount = 3;
  }
  optional int32 used_amount = 1;
  optional int32 period = 4;
  optional int32 max_previews_per_course = 5;
}

```

**Source references:** SRC-0293, SRC-1264  
**URL references:** None independently associated  
**Related findings:** FND-02103, FND-02104

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02106"></a>
## FND-02106: chesscom.courses.v1.GetPreviewsInformationResponse.total_amount = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 total_amount = 2;

### Evidence

- **SRC-0293** `research/proto/chesscom/courses/v1/courses_previews_information_service.proto` — [preserved redacted evidence](../evidence/text/8370fe997da8ad024ffb6904fba3990805789066a6ca600a08b6c967abded08d.proto)
  Character offset 233.

```text
tPreviewsInformationRequest {
}

message GetPreviewsInformationResponse {
  oneof _total_amount {
  int32 total_amount = 2;
  }
  oneof _variation_resets_in_days_amount {
  int32 variation_resets_in_days_amount = 3;
  }
  optional int32 used_amount = 1;
  optional int32 period = 4;
  optional int32 max_previews_per_course = 5;
}

```

**Source references:** SRC-0293, SRC-1264  
**URL references:** None independently associated  
**Related findings:** FND-02103, FND-02104, FND-02105

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02107"></a>
## FND-02107: oneof declaration: chesscom.courses.v1.GetPreviewsInformationResponse._variation_resets_in_days_amount

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _variation_resets_in_days_amount {

### Evidence

- **SRC-0293** `research/proto/chesscom/courses/v1/courses_previews_information_service.proto` — [preserved redacted evidence](../evidence/text/8370fe997da8ad024ffb6904fba3990805789066a6ca600a08b6c967abded08d.proto)
  Character offset 263.

```text
}

message GetPreviewsInformationResponse {
  oneof _total_amount {
  int32 total_amount = 2;
  }
  oneof _variation_resets_in_days_amount {
  int32 variation_resets_in_days_amount = 3;
  }
  optional int32 used_amount = 1;
  optional int32 period = 4;
  optional int32 max_previews_per_course = 5;
}

```

**Source references:** SRC-0293, SRC-1264  
**URL references:** None independently associated  
**Related findings:** FND-02103, FND-02104, FND-02105

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02108"></a>
## FND-02108: chesscom.courses.v1.GetPreviewsInformationResponse.variation_resets_in_days_amount = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 variation_resets_in_days_amount = 3;

### Evidence

- **SRC-0293** `research/proto/chesscom/courses/v1/courses_previews_information_service.proto` — [preserved redacted evidence](../evidence/text/8370fe997da8ad024ffb6904fba3990805789066a6ca600a08b6c967abded08d.proto)
  Character offset 306.

```text

  oneof _total_amount {
  int32 total_amount = 2;
  }
  oneof _variation_resets_in_days_amount {
  int32 variation_resets_in_days_amount = 3;
  }
  optional int32 used_amount = 1;
  optional int32 period = 4;
  optional int32 max_previews_per_course = 5;
}

```

**Source references:** SRC-0293, SRC-1264  
**URL references:** None independently associated  
**Related findings:** FND-02103, FND-02104, FND-02105

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02109"></a>
## FND-02109: chesscom.courses.v1.GetPreviewsInformationResponse.used_amount = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 used_amount = 1;

### Evidence

- **SRC-0293** `research/proto/chesscom/courses/v1/courses_previews_information_service.proto` — [preserved redacted evidence](../evidence/text/8370fe997da8ad024ffb6904fba3990805789066a6ca600a08b6c967abded08d.proto)
  Character offset 355.

```text
;
  }
  oneof _variation_resets_in_days_amount {
  int32 variation_resets_in_days_amount = 3;
  }
  optional int32 used_amount = 1;
  optional int32 period = 4;
  optional int32 max_previews_per_course = 5;
}

```

**Source references:** SRC-0293, SRC-1264  
**URL references:** None independently associated  
**Related findings:** FND-02103, FND-02104, FND-02105

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02110"></a>
## FND-02110: chesscom.courses.v1.GetPreviewsInformationResponse.period = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 period = 4;

### Evidence

- **SRC-0293** `research/proto/chesscom/courses/v1/courses_previews_information_service.proto` — [preserved redacted evidence](../evidence/text/8370fe997da8ad024ffb6904fba3990805789066a6ca600a08b6c967abded08d.proto)
  Character offset 389.

```text
_days_amount {
  int32 variation_resets_in_days_amount = 3;
  }
  optional int32 used_amount = 1;
  optional int32 period = 4;
  optional int32 max_previews_per_course = 5;
}

```

**Source references:** SRC-0293, SRC-1264  
**URL references:** None independently associated  
**Related findings:** FND-02103, FND-02104, FND-02105

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02111"></a>
## FND-02111: chesscom.courses.v1.GetPreviewsInformationResponse.max_previews_per_course = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 max_previews_per_course = 5;

### Evidence

- **SRC-0293** `research/proto/chesscom/courses/v1/courses_previews_information_service.proto` — [preserved redacted evidence](../evidence/text/8370fe997da8ad024ffb6904fba3990805789066a6ca600a08b6c967abded08d.proto)
  Character offset 418.

```text
ion_resets_in_days_amount = 3;
  }
  optional int32 used_amount = 1;
  optional int32 period = 4;
  optional int32 max_previews_per_course = 5;
}

```

**Source references:** SRC-0293, SRC-1264  
**URL references:** None independently associated  
**Related findings:** FND-02103, FND-02104, FND-02105

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02112"></a>
## FND-02112: message declaration: chesscom.courses.v1.CoursesShopPagination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoursesShopPagination {

### Evidence

- **SRC-0294** `research/proto/chesscom/courses/v1/courses_shop_pagination.proto` — [preserved redacted evidence](../evidence/text/4130f77a3306901d4bfe2a13ae6316d6b4c6c37d5400c3827b3e01cd3fd69cf5.proto)
  Character offset 110.

```text
 chesscom/courses/v1/courses_shop_pagination.proto
// syntax: proto3

package chesscom.courses.v1;

message CoursesShopPagination {
  optional int32 limit = 1;
  optional int32 offset = 2;
}

```

**Source references:** SRC-0294, SRC-1265  
**URL references:** None independently associated  
**Related findings:** FND-02113, FND-02114

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02113"></a>
## FND-02113: chesscom.courses.v1.CoursesShopPagination.limit = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 limit = 1;

### Evidence

- **SRC-0294** `research/proto/chesscom/courses/v1/courses_shop_pagination.proto` — [preserved redacted evidence](../evidence/text/4130f77a3306901d4bfe2a13ae6316d6b4c6c37d5400c3827b3e01cd3fd69cf5.proto)
  Character offset 144.

```text
pagination.proto
// syntax: proto3

package chesscom.courses.v1;

message CoursesShopPagination {
  optional int32 limit = 1;
  optional int32 offset = 2;
}

```

**Source references:** SRC-0294, SRC-1265  
**URL references:** None independently associated  
**Related findings:** FND-02112, FND-02114

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02114"></a>
## FND-02114: chesscom.courses.v1.CoursesShopPagination.offset = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 offset = 2;

### Evidence

- **SRC-0294** `research/proto/chesscom/courses/v1/courses_shop_pagination.proto` — [preserved redacted evidence](../evidence/text/4130f77a3306901d4bfe2a13ae6316d6b4c6c37d5400c3827b3e01cd3fd69cf5.proto)
  Character offset 172.

```text
proto3

package chesscom.courses.v1;

message CoursesShopPagination {
  optional int32 limit = 1;
  optional int32 offset = 2;
}

```

**Source references:** SRC-0294, SRC-1265  
**URL references:** None independently associated  
**Related findings:** FND-02112, FND-02113

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02115"></a>
## FND-02115: message declaration: chesscom.courses.v1.GetCourseProductListRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseProductListRequest {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 107.

```text
ce: chesscom/courses/v1/courses_shop_service.proto
// syntax: proto3

package chesscom.courses.v1;

message GetCourseProductListRequest {
  oneof _pagination {
  .chesscom.courses.v1.CoursesShopPagination pagination = 1;
  }
  oneof _search_query {
  string search_query = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _price_range_in_cents {
  .chesscom.courses_common.v1.Range price_range_i
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02116"></a>
## FND-02116: oneof declaration: chesscom.courses.v1.GetCourseProductListRequest._pagination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pagination {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 147.

```text
vice.proto
// syntax: proto3

package chesscom.courses.v1;

message GetCourseProductListRequest {
  oneof _pagination {
  .chesscom.courses.v1.CoursesShopPagination pagination = 1;
  }
  oneof _search_query {
  string search_query = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _price_range_in_cents {
  .chesscom.courses_common.v1.Range price_range_in_cents = 8;
  }
  oneof _exclude_owned_
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02117"></a>
## FND-02117: chesscom.courses.v1.GetCourseProductListRequest.pagination = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CoursesShopPagination pagination = 1;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 169.

```text
proto3

package chesscom.courses.v1;

message GetCourseProductListRequest {
  oneof _pagination {
  .chesscom.courses.v1.CoursesShopPagination pagination = 1;
  }
  oneof _search_query {
  string search_query = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _price_range_in_cents {
  .chesscom.courses_common.v1.Range price_range_in_cents = 8;
  }
  oneof _exclude_owned_courses {
  bool exclu
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02118"></a>
## FND-02118: oneof declaration: chesscom.courses.v1.GetCourseProductListRequest._search_query

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _search_query {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 234.

```text
tRequest {
  oneof _pagination {
  .chesscom.courses.v1.CoursesShopPagination pagination = 1;
  }
  oneof _search_query {
  string search_query = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _price_range_in_cents {
  .chesscom.courses_common.v1.Range price_range_in_cents = 8;
  }
  oneof _exclude_owned_courses {
  bool exclude_owned_courses = 9;
  }
  oneof _user_rating {
  int32 user_rat
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02119"></a>
## FND-02119: chesscom.courses.v1.GetCourseProductListRequest.search_query = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string search_query = 2;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 258.

```text
nation {
  .chesscom.courses.v1.CoursesShopPagination pagination = 1;
  }
  oneof _search_query {
  string search_query = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _price_range_in_cents {
  .chesscom.courses_common.v1.Range price_range_in_cents = 8;
  }
  oneof _exclude_owned_courses {
  bool exclude_owned_courses = 9;
  }
  oneof _user_rating {
  int32 user_rating = 10;
  }
  oneof _r
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02120"></a>
## FND-02120: oneof declaration: chesscom.courses.v1.GetCourseProductListRequest._color

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _color {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 289.

```text
.CoursesShopPagination pagination = 1;
  }
  oneof _search_query {
  string search_query = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _price_range_in_cents {
  .chesscom.courses_common.v1.Range price_range_in_cents = 8;
  }
  oneof _exclude_owned_courses {
  bool exclude_owned_courses = 9;
  }
  oneof _user_rating {
  int32 user_rating = 10;
  }
  oneof _retrieve_mode {
  .chesscom.cour
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02121"></a>
## FND-02121: chesscom.courses.v1.GetCourseProductListRequest.color = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.chess.v1.Color color = 5;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 306.

```text
ation pagination = 1;
  }
  oneof _search_query {
  string search_query = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _price_range_in_cents {
  .chesscom.courses_common.v1.Range price_range_in_cents = 8;
  }
  oneof _exclude_owned_courses {
  bool exclude_owned_courses = 9;
  }
  oneof _user_rating {
  int32 user_rating = 10;
  }
  oneof _retrieve_mode {
  .chesscom.courses.v1.ProductLis
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02122"></a>
## FND-02122: oneof declaration: chesscom.courses.v1.GetCourseProductListRequest._price_range_in_cents

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _price_range_in_cents {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 348.

```text
query {
  string search_query = 2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _price_range_in_cents {
  .chesscom.courses_common.v1.Range price_range_in_cents = 8;
  }
  oneof _exclude_owned_courses {
  bool exclude_owned_courses = 9;
  }
  oneof _user_rating {
  int32 user_rating = 10;
  }
  oneof _retrieve_mode {
  .chesscom.courses.v1.ProductListRetrieveMode retrieve_mode = 11;
  }
  on
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02123"></a>
## FND-02123: chesscom.courses.v1.GetCourseProductListRequest.price_range_in_cents = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses_common.v1.Range price_range_in_cents = 8;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 380.

```text
2;
  }
  oneof _color {
  .chesscom.chess.v1.Color color = 5;
  }
  oneof _price_range_in_cents {
  .chesscom.courses_common.v1.Range price_range_in_cents = 8;
  }
  oneof _exclude_owned_courses {
  bool exclude_owned_courses = 9;
  }
  oneof _user_rating {
  int32 user_rating = 10;
  }
  oneof _retrieve_mode {
  .chesscom.courses.v1.ProductListRetrieveMode retrieve_mode = 11;
  }
  oneof _price_range {
  .chesscom.c
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02124"></a>
## FND-02124: oneof declaration: chesscom.courses.v1.GetCourseProductListRequest._exclude_owned_courses

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _exclude_owned_courses {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 446.

```text
  oneof _price_range_in_cents {
  .chesscom.courses_common.v1.Range price_range_in_cents = 8;
  }
  oneof _exclude_owned_courses {
  bool exclude_owned_courses = 9;
  }
  oneof _user_rating {
  int32 user_rating = 10;
  }
  oneof _retrieve_mode {
  .chesscom.courses.v1.ProductListRetrieveMode retrieve_mode = 11;
  }
  oneof _price_range {
  .chesscom.courses.v1.PriceRange price_range = 12;
  }
  oneof _fen {
  string
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02125"></a>
## FND-02125: chesscom.courses.v1.GetCourseProductListRequest.exclude_owned_courses = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool exclude_owned_courses = 9;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 479.

```text
 .chesscom.courses_common.v1.Range price_range_in_cents = 8;
  }
  oneof _exclude_owned_courses {
  bool exclude_owned_courses = 9;
  }
  oneof _user_rating {
  int32 user_rating = 10;
  }
  oneof _retrieve_mode {
  .chesscom.courses.v1.ProductListRetrieveMode retrieve_mode = 11;
  }
  oneof _price_range {
  .chesscom.courses.v1.PriceRange price_range = 12;
  }
  oneof _fen {
  string fen = 13;
  }
  oneof _sort {
  
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02126"></a>
## FND-02126: oneof declaration: chesscom.courses.v1.GetCourseProductListRequest._user_rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_rating {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 517.

```text
ce_range_in_cents = 8;
  }
  oneof _exclude_owned_courses {
  bool exclude_owned_courses = 9;
  }
  oneof _user_rating {
  int32 user_rating = 10;
  }
  oneof _retrieve_mode {
  .chesscom.courses.v1.ProductListRetrieveMode retrieve_mode = 11;
  }
  oneof _price_range {
  .chesscom.courses.v1.PriceRange price_range = 12;
  }
  oneof _fen {
  string fen = 13;
  }
  oneof _sort {
  .chesscom.courses.v1.ShopSortOption so
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02127"></a>
## FND-02127: chesscom.courses.v1.GetCourseProductListRequest.user_rating = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 user_rating = 10;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 540.

```text
  }
  oneof _exclude_owned_courses {
  bool exclude_owned_courses = 9;
  }
  oneof _user_rating {
  int32 user_rating = 10;
  }
  oneof _retrieve_mode {
  .chesscom.courses.v1.ProductListRetrieveMode retrieve_mode = 11;
  }
  oneof _price_range {
  .chesscom.courses.v1.PriceRange price_range = 12;
  }
  oneof _fen {
  string fen = 13;
  }
  oneof _sort {
  .chesscom.courses.v1.ShopSortOption sort = 15;
  }
  oneof _i
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02128"></a>
## FND-02128: oneof declaration: chesscom.courses.v1.GetCourseProductListRequest._retrieve_mode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _retrieve_mode {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 570.

```text
rses {
  bool exclude_owned_courses = 9;
  }
  oneof _user_rating {
  int32 user_rating = 10;
  }
  oneof _retrieve_mode {
  .chesscom.courses.v1.ProductListRetrieveMode retrieve_mode = 11;
  }
  oneof _price_range {
  .chesscom.courses.v1.PriceRange price_range = 12;
  }
  oneof _fen {
  string fen = 13;
  }
  oneof _sort {
  .chesscom.courses.v1.ShopSortOption sort = 15;
  }
  oneof _include_only_owned_courses {
  
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02129"></a>
## FND-02129: chesscom.courses.v1.GetCourseProductListRequest.retrieve_mode = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.ProductListRetrieveMode retrieve_mode = 11;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 595.

```text
ed_courses = 9;
  }
  oneof _user_rating {
  int32 user_rating = 10;
  }
  oneof _retrieve_mode {
  .chesscom.courses.v1.ProductListRetrieveMode retrieve_mode = 11;
  }
  oneof _price_range {
  .chesscom.courses.v1.PriceRange price_range = 12;
  }
  oneof _fen {
  string fen = 13;
  }
  oneof _sort {
  .chesscom.courses.v1.ShopSortOption sort = 15;
  }
  oneof _include_only_owned_courses {
  bool include_only_owned_c
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02130"></a>
## FND-02130: oneof declaration: chesscom.courses.v1.GetCourseProductListRequest._price_range

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _price_range {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 666.

```text
}
  oneof _retrieve_mode {
  .chesscom.courses.v1.ProductListRetrieveMode retrieve_mode = 11;
  }
  oneof _price_range {
  .chesscom.courses.v1.PriceRange price_range = 12;
  }
  oneof _fen {
  string fen = 13;
  }
  oneof _sort {
  .chesscom.courses.v1.ShopSortOption sort = 15;
  }
  oneof _include_only_owned_courses {
  bool include_only_owned_courses = 16;
  }
  repeated .chesscom.courses_common.v1.CourseGameAspec
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02131"></a>
## FND-02131: chesscom.courses.v1.GetCourseProductListRequest.price_range = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.PriceRange price_range = 12;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 689.

```text
e {
  .chesscom.courses.v1.ProductListRetrieveMode retrieve_mode = 11;
  }
  oneof _price_range {
  .chesscom.courses.v1.PriceRange price_range = 12;
  }
  oneof _fen {
  string fen = 13;
  }
  oneof _sort {
  .chesscom.courses.v1.ShopSortOption sort = 15;
  }
  oneof _include_only_owned_courses {
  bool include_only_owned_courses = 16;
  }
  repeated .chesscom.courses_common.v1.CourseGameAspectType game_aspects = 3;
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02132"></a>
## FND-02132: oneof declaration: chesscom.courses.v1.GetCourseProductListRequest._fen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fen {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 745.

```text
eve_mode = 11;
  }
  oneof _price_range {
  .chesscom.courses.v1.PriceRange price_range = 12;
  }
  oneof _fen {
  string fen = 13;
  }
  oneof _sort {
  .chesscom.courses.v1.ShopSortOption sort = 15;
  }
  oneof _include_only_owned_courses {
  bool include_only_owned_courses = 16;
  }
  repeated .chesscom.courses_common.v1.CourseGameAspectType game_aspects = 3;
  repeated .chesscom.courses_common.v1.Range elo_ranges
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02133"></a>
## FND-02133: chesscom.courses.v1.GetCourseProductListRequest.fen = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string fen = 13;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 760.

```text
  }
  oneof _price_range {
  .chesscom.courses.v1.PriceRange price_range = 12;
  }
  oneof _fen {
  string fen = 13;
  }
  oneof _sort {
  .chesscom.courses.v1.ShopSortOption sort = 15;
  }
  oneof _include_only_owned_courses {
  bool include_only_owned_courses = 16;
  }
  repeated .chesscom.courses_common.v1.CourseGameAspectType game_aspects = 3;
  repeated .chesscom.courses_common.v1.Range elo_ranges = 4;
  repeate
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02134"></a>
## FND-02134: oneof declaration: chesscom.courses.v1.GetCourseProductListRequest._sort

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _sort {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 783.

```text
e {
  .chesscom.courses.v1.PriceRange price_range = 12;
  }
  oneof _fen {
  string fen = 13;
  }
  oneof _sort {
  .chesscom.courses.v1.ShopSortOption sort = 15;
  }
  oneof _include_only_owned_courses {
  bool include_only_owned_courses = 16;
  }
  repeated .chesscom.courses_common.v1.CourseGameAspectType game_aspects = 3;
  repeated .chesscom.courses_common.v1.Range elo_ranges = 4;
  repeated .chesscom.courses.v1.
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02135"></a>
## FND-02135: chesscom.courses.v1.GetCourseProductListRequest.sort = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.ShopSortOption sort = 15;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 799.

```text
courses.v1.PriceRange price_range = 12;
  }
  oneof _fen {
  string fen = 13;
  }
  oneof _sort {
  .chesscom.courses.v1.ShopSortOption sort = 15;
  }
  oneof _include_only_owned_courses {
  bool include_only_owned_courses = 16;
  }
  repeated .chesscom.courses_common.v1.CourseGameAspectType game_aspects = 3;
  repeated .chesscom.courses_common.v1.Range elo_ranges = 4;
  repeated .chesscom.courses.v1.CourseTag tags =
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02136"></a>
## FND-02136: oneof declaration: chesscom.courses.v1.GetCourseProductListRequest._include_only_owned_courses

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _include_only_owned_courses {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 852.

```text
fen {
  string fen = 13;
  }
  oneof _sort {
  .chesscom.courses.v1.ShopSortOption sort = 15;
  }
  oneof _include_only_owned_courses {
  bool include_only_owned_courses = 16;
  }
  repeated .chesscom.courses_common.v1.CourseGameAspectType game_aspects = 3;
  repeated .chesscom.courses_common.v1.Range elo_ranges = 4;
  repeated .chesscom.courses.v1.CourseTag tags = 6;
  optional string country_code = 7;
  repeated .c
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02137"></a>
## FND-02137: chesscom.courses.v1.GetCourseProductListRequest.include_only_owned_courses = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool include_only_owned_courses = 16;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 890.

```text
sort {
  .chesscom.courses.v1.ShopSortOption sort = 15;
  }
  oneof _include_only_owned_courses {
  bool include_only_owned_courses = 16;
  }
  repeated .chesscom.courses_common.v1.CourseGameAspectType game_aspects = 3;
  repeated .chesscom.courses_common.v1.Range elo_ranges = 4;
  repeated .chesscom.courses.v1.CourseTag tags = 6;
  optional string country_code = 7;
  repeated .chesscom.courses.v1.CourseCustomTag cou
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02138"></a>
## FND-02138: chesscom.courses.v1.GetCourseProductListRequest.game_aspects = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses_common.v1.CourseGameAspectType game_aspects = 3;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 934.

```text
 sort = 15;
  }
  oneof _include_only_owned_courses {
  bool include_only_owned_courses = 16;
  }
  repeated .chesscom.courses_common.v1.CourseGameAspectType game_aspects = 3;
  repeated .chesscom.courses_common.v1.Range elo_ranges = 4;
  repeated .chesscom.courses.v1.CourseTag tags = 6;
  optional string country_code = 7;
  repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 14;
}

message GetCoursePr
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02139"></a>
## FND-02139: chesscom.courses.v1.GetCourseProductListRequest.elo_ranges = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses_common.v1.Range elo_ranges = 4;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 1012.

```text
d_courses = 16;
  }
  repeated .chesscom.courses_common.v1.CourseGameAspectType game_aspects = 3;
  repeated .chesscom.courses_common.v1.Range elo_ranges = 4;
  repeated .chesscom.courses.v1.CourseTag tags = 6;
  optional string country_code = 7;
  repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 14;
}

message GetCourseProductListResponse {
  optional int32 total = 1;
  repeated .chesscom.courses.v
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02140"></a>
## FND-02140: chesscom.courses.v1.GetCourseProductListRequest.tags = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseTag tags = 6;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 1073.

```text
urseGameAspectType game_aspects = 3;
  repeated .chesscom.courses_common.v1.Range elo_ranges = 4;
  repeated .chesscom.courses.v1.CourseTag tags = 6;
  optional string country_code = 7;
  repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 14;
}

message GetCourseProductListResponse {
  optional int32 total = 1;
  repeated .chesscom.courses.v1.CourseProduct product_list = 2;
}

message GetShopMetadataR
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02141"></a>
## FND-02141: chesscom.courses.v1.GetCourseProductListRequest.country_code = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string country_code = 7;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 1125.

```text
sscom.courses_common.v1.Range elo_ranges = 4;
  repeated .chesscom.courses.v1.CourseTag tags = 6;
  optional string country_code = 7;
  repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 14;
}

message GetCourseProductListResponse {
  optional int32 total = 1;
  repeated .chesscom.courses.v1.CourseProduct product_list = 2;
}

message GetShopMetadataRequest {
  optional string country_code = 1;
}

mess
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02142"></a>
## FND-02142: chesscom.courses.v1.GetCourseProductListRequest.course_custom_tags = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 14;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 1161.

```text
nges = 4;
  repeated .chesscom.courses.v1.CourseTag tags = 6;
  optional string country_code = 7;
  repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 14;
}

message GetCourseProductListResponse {
  optional int32 total = 1;
  repeated .chesscom.courses.v1.CourseProduct product_list = 2;
}

message GetShopMetadataRequest {
  optional string country_code = 1;
}

message GetShopMetadataResponse {
  opti
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02143"></a>
## FND-02143: message declaration: chesscom.courses.v1.GetCourseProductListResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseProductListResponse {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 1235.

```text
tring country_code = 7;
  repeated .chesscom.courses.v1.CourseCustomTag course_custom_tags = 14;
}

message GetCourseProductListResponse {
  optional int32 total = 1;
  repeated .chesscom.courses.v1.CourseProduct product_list = 2;
}

message GetShopMetadataRequest {
  optional string country_code = 1;
}

message GetShopMetadataResponse {
  optional int32 number_of_courses_on_sale = 1;
  optional .chesscom.api.v1.Mone
```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02144"></a>
## FND-02144: chesscom.courses.v1.GetCourseProductListResponse.total = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 total = 1;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 1276.

```text
com.courses.v1.CourseCustomTag course_custom_tags = 14;
}

message GetCourseProductListResponse {
  optional int32 total = 1;
  repeated .chesscom.courses.v1.CourseProduct product_list = 2;
}

message GetShopMetadataRequest {
  optional string country_code = 1;
}

message GetShopMetadataResponse {
  optional int32 number_of_courses_on_sale = 1;
  optional .chesscom.api.v1.Money max_price = 2;
}

```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02145"></a>
## FND-02145: chesscom.courses.v1.GetCourseProductListResponse.product_list = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseProduct product_list = 2;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 1304.

```text
ag course_custom_tags = 14;
}

message GetCourseProductListResponse {
  optional int32 total = 1;
  repeated .chesscom.courses.v1.CourseProduct product_list = 2;
}

message GetShopMetadataRequest {
  optional string country_code = 1;
}

message GetShopMetadataResponse {
  optional int32 number_of_courses_on_sale = 1;
  optional .chesscom.api.v1.Money max_price = 2;
}

```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02146"></a>
## FND-02146: message declaration: chesscom.courses.v1.GetShopMetadataRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetShopMetadataRequest {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 1369.

```text
se {
  optional int32 total = 1;
  repeated .chesscom.courses.v1.CourseProduct product_list = 2;
}

message GetShopMetadataRequest {
  optional string country_code = 1;
}

message GetShopMetadataResponse {
  optional int32 number_of_courses_on_sale = 1;
  optional .chesscom.api.v1.Money max_price = 2;
}

```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02147"></a>
## FND-02147: chesscom.courses.v1.GetShopMetadataRequest.country_code = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string country_code = 1;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 1404.

```text
repeated .chesscom.courses.v1.CourseProduct product_list = 2;
}

message GetShopMetadataRequest {
  optional string country_code = 1;
}

message GetShopMetadataResponse {
  optional int32 number_of_courses_on_sale = 1;
  optional .chesscom.api.v1.Money max_price = 2;
}

```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02148"></a>
## FND-02148: message declaration: chesscom.courses.v1.GetShopMetadataResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetShopMetadataResponse {

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 1441.

```text
roduct product_list = 2;
}

message GetShopMetadataRequest {
  optional string country_code = 1;
}

message GetShopMetadataResponse {
  optional int32 number_of_courses_on_sale = 1;
  optional .chesscom.api.v1.Money max_price = 2;
}

```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02149"></a>
## FND-02149: chesscom.courses.v1.GetShopMetadataResponse.number_of_courses_on_sale = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 number_of_courses_on_sale = 1;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 1477.

```text
GetShopMetadataRequest {
  optional string country_code = 1;
}

message GetShopMetadataResponse {
  optional int32 number_of_courses_on_sale = 1;
  optional .chesscom.api.v1.Money max_price = 2;
}

```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02150"></a>
## FND-02150: chesscom.courses.v1.GetShopMetadataResponse.max_price = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Money max_price = 2;

### Evidence

- **SRC-0295** `research/proto/chesscom/courses/v1/courses_shop_service.proto` — [preserved redacted evidence](../evidence/text/bdad3f68f8783b847060219adcd84c3c11b6c3c554bc9b405b0639e55b4d3b9c.proto)
  Character offset 1525.

```text
ry_code = 1;
}

message GetShopMetadataResponse {
  optional int32 number_of_courses_on_sale = 1;
  optional .chesscom.api.v1.Money max_price = 2;
}

```

**Source references:** SRC-0295, SRC-1266  
**URL references:** None independently associated  
**Related findings:** FND-02115, FND-02116, FND-02117

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02151"></a>
## FND-02151: message declaration: chesscom.courses.v1.GetCourseLearningSessionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseLearningSessionRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 111.

```text
chesscom/courses/v1/courses_training_service.proto
// syntax: proto3

package chesscom.courses.v1;

message GetCourseLearningSessionRequest {
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
  optional .chesscom.courses.v1.CourseLe
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02152"></a>
## FND-02152: oneof declaration: chesscom.courses.v1.GetCourseLearningSessionRequest._learning_session_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _learning_session_id {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 155.

```text
.proto
// syntax: proto3

package chesscom.courses.v1;

message GetCourseLearningSessionRequest {
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
  option
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02153"></a>
## FND-02153: chesscom.courses.v1.GetCourseLearningSessionRequest.learning_session_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string learning_session_id = 3;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 186.

```text
ge chesscom.courses.v1;

message GetCourseLearningSessionRequest {
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
  optional string learning_session_id =
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02154"></a>
## FND-02154: oneof declaration: chesscom.courses.v1.GetCourseLearningSessionRequest._course_slug

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

<a id="FND-02155"></a>
## FND-02155: chesscom.courses.v1.GetCourseLearningSessionRequest.course_slug = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string course_slug = 4;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 247.

```text
est {
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
  optional .chesscom.courses.v1.CourseLearningSessionProg
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02156"></a>
## FND-02156: chesscom.courses.v1.GetCourseLearningSessionRequest.context_type = 1

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

<a id="FND-02157"></a>
## FND-02157: chesscom.courses.v1.GetCourseLearningSessionRequest.context_id = 2

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

<a id="FND-02158"></a>
## FND-02158: message declaration: chesscom.courses.v1.GetCourseLearningSessionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseLearningSessionResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 348.

```text
tring course_slug = 4;
  }
  optional string context_type = 1;
  optional string context_id = 2;
}

message GetCourseLearningSessionResponse {
  optional .chesscom.courses.v1.CourseLearningSession learning_session = 1;
  optional string learning_session_id = 2;
  optional .chesscom.courses.v1.CourseLearningSessionProgress progress = 3;
}

message GetCourseTrainingForLearningRequest {
  optional string variation_id = 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02159"></a>
## FND-02159: chesscom.courses.v1.GetCourseLearningSessionResponse.learning_session = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseLearningSession learning_session = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 393.

```text
context_type = 1;
  optional string context_id = 2;
}

message GetCourseLearningSessionResponse {
  optional .chesscom.courses.v1.CourseLearningSession learning_session = 1;
  optional string learning_session_id = 2;
  optional .chesscom.courses.v1.CourseLearningSessionProgress progress = 3;
}

message GetCourseTrainingForLearningRequest {
  optional string variation_id = 1;
  optional string learning_session_id = 2;
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02160"></a>
## FND-02160: chesscom.courses.v1.GetCourseLearningSessionResponse.learning_session_id = 2

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

<a id="FND-02161"></a>
## FND-02161: chesscom.courses.v1.GetCourseLearningSessionResponse.progress = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseLearningSessionProgress progress = 3;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 512.

```text
courses.v1.CourseLearningSession learning_session = 1;
  optional string learning_session_id = 2;
  optional .chesscom.courses.v1.CourseLearningSessionProgress progress = 3;
}

message GetCourseTrainingForLearningRequest {
  optional string variation_id = 1;
  optional string learning_session_id = 2;
}

message GetCourseTrainingForLearningResponse {
  optional .chesscom.courses.v1.CourseLesson lesson = 1;
  optional 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02162"></a>
## FND-02162: message declaration: chesscom.courses.v1.GetCourseTrainingForLearningRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseTrainingForLearningRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 589.

```text
ning_session_id = 2;
  optional .chesscom.courses.v1.CourseLearningSessionProgress progress = 3;
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
  o
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02163"></a>
## FND-02163: chesscom.courses.v1.GetCourseTrainingForLearningRequest.variation_id = 1

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

<a id="FND-02164"></a>
## FND-02164: chesscom.courses.v1.GetCourseTrainingForLearningRequest.learning_session_id = 2

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

<a id="FND-02165"></a>
## FND-02165: message declaration: chesscom.courses.v1.GetCourseTrainingForLearningResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseTrainingForLearningResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 717.

```text
LearningRequest {
  optional string variation_id = 1;
  optional string learning_session_id = 2;
}

message GetCourseTrainingForLearningResponse {
  optional .chesscom.courses.v1.CourseLesson lesson = 1;
  optional string training_id = 2;
}

message GetCourseTrainingForReviewingRequest {
  optional string variation_id = 1;
  optional string learning_session_id = 2;
}

message GetCourseTrainingForReviewingResponse {
 
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02166"></a>
## FND-02166: chesscom.courses.v1.GetCourseTrainingForLearningResponse.lesson = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseLesson lesson = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 766.

```text
= 1;
  optional string learning_session_id = 2;
}

message GetCourseTrainingForLearningResponse {
  optional .chesscom.courses.v1.CourseLesson lesson = 1;
  optional string training_id = 2;
}

message GetCourseTrainingForReviewingRequest {
  optional string variation_id = 1;
  optional string learning_session_id = 2;
}

message GetCourseTrainingForReviewingResponse {
  optional .chesscom.courses.v1.CourseLesson lesso
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02167"></a>
## FND-02167: chesscom.courses.v1.GetCourseTrainingForLearningResponse.training_id = 2

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

<a id="FND-02168"></a>
## FND-02168: message declaration: chesscom.courses.v1.GetCourseTrainingForReviewingRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseTrainingForReviewingRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 859.

```text
se {
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

message StoreCourseTrainingProgressRequest {
  o
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02169"></a>
## FND-02169: chesscom.courses.v1.GetCourseTrainingForReviewingRequest.variation_id = 1

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

<a id="FND-02170"></a>
## FND-02170: chesscom.courses.v1.GetCourseTrainingForReviewingRequest.learning_session_id = 2

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

<a id="FND-02171"></a>
## FND-02171: message declaration: chesscom.courses.v1.GetCourseTrainingForReviewingResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCourseTrainingForReviewingResponse {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 988.

```text
eviewingRequest {
  optional string variation_id = 1;
  optional string learning_session_id = 2;
}

message GetCourseTrainingForReviewingResponse {
  optional .chesscom.courses.v1.CourseLesson lesson = 1;
  optional string training_id = 2;
}

message StoreCourseTrainingProgressRequest {
  optional string ply_id = 1;
  optional string san = 2;
  optional .chesscom.courses.v1.MoveTrainerTrainingMode training_mode = 3;

```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-02172"></a>
## FND-02172: chesscom.courses.v1.GetCourseTrainingForReviewingResponse.lesson = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.CourseLesson lesson = 1;

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 766.

```text
= 1;
  optional string learning_session_id = 2;
}

message GetCourseTrainingForLearningResponse {
  optional .chesscom.courses.v1.CourseLesson lesson = 1;
  optional string training_id = 2;
}

message GetCourseTrainingForReviewingRequest {
  optional string variation_id = 1;
  optional string learning_session_id = 2;
}

message GetCourseTrainingForReviewingResponse {
  optional .chesscom.courses.v1.CourseLesson lesso
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-02173"></a>
## FND-02173: chesscom.courses.v1.GetCourseTrainingForReviewingResponse.training_id = 2

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

<a id="FND-02174"></a>
## FND-02174: message declaration: chesscom.courses.v1.StoreCourseTrainingProgressRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message StoreCourseTrainingProgressRequest {

### Evidence

- **SRC-0296** `research/proto/chesscom/courses/v1/courses_training_service.proto` — [preserved redacted evidence](../evidence/text/b883b8c214e144561200ffff3e95ad0c542b6ec72f66c376dc89a23b4ec005d6.proto)
  Character offset 1131.

```text
se {
  optional .chesscom.courses.v1.CourseLesson lesson = 1;
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

message Store
```

**Source references:** SRC-0296, SRC-1267  
**URL references:** None independently associated  
**Related findings:** FND-02151, FND-02152, FND-02153

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
