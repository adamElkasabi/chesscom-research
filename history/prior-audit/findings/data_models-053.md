# data_models — findings 5201–5300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-05475"></a>
## FND-05475: chesscom.game_review.v2.GameReviewCourseRecommendationClicked.course_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_name = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12194.

```text
ion = 8;
  optional string engine_strength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCour
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05476"></a>
## FND-05476: chesscom.game_review.v2.GameReviewCourseRecommendationClicked.author_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string author_name = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12229.

```text
trength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
  op
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05477"></a>
## FND-05477: chesscom.game_review.v2.GameReviewCourseRecommendationClicked.type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12264.

```text
ourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
  optional string opening_name = 4;
  o
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05478"></a>
## FND-05478: chesscom.game_review.v2.GameReviewCourseRecommendationClicked.opening_name = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string opening_name = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12547.

```text
author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
  optional string opening_name = 4;
  optional string fen = 5;
  optional string variation_preview_url = 6;
  optional string course_id = 7;
  optional string course_url = 8;
  optional string cover_image_url = 9;
  optional float rating = 10;
  optional int32 review_count = 11;
  optional string short_description = 12;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05479"></a>
## FND-05479: chesscom.game_review.v2.GameReviewCourseRecommendationClicked.fen = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string fen = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12583.

```text
m.game_review.v2.GameReviewCourseRecommendationType type = 3;
  optional string opening_name = 4;
  optional string fen = 5;
  optional string variation_preview_url = 6;
  optional string course_id = 7;
  optional string course_url = 8;
  optional string cover_image_url = 9;
  optional float rating = 10;
  optional int32 review_count = 11;
  optional string short_description = 12;
  optional string user_color = 13;
}
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05480"></a>
## FND-05480: chesscom.game_review.v2.GameReviewCourseRecommendationClicked.variation_preview_url = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string variation_preview_url = 6;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12610.

```text
CourseRecommendationType type = 3;
  optional string opening_name = 4;
  optional string fen = 5;
  optional string variation_preview_url = 6;
  optional string course_id = 7;
  optional string course_url = 8;
  optional string cover_image_url = 9;
  optional float rating = 10;
  optional int32 review_count = 11;
  optional string short_description = 12;
  optional string user_color = 13;
}

message GameReviewCourseR
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05481"></a>
## FND-05481: chesscom.game_review.v2.GameReviewCourseRecommendationClicked.course_id = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_id = 7;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12655.

```text
 string opening_name = 4;
  optional string fen = 5;
  optional string variation_preview_url = 6;
  optional string course_id = 7;
  optional string course_url = 8;
  optional string cover_image_url = 9;
  optional float rating = 10;
  optional int32 review_count = 11;
  optional string short_description = 12;
  optional string user_color = 13;
}

message GameReviewCourseRecommendationDecision {
  oneof _rating {
  i
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05482"></a>
## FND-05482: chesscom.game_review.v2.GameReviewCourseRecommendationClicked.course_url = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_url = 8;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12688.

```text
nal string fen = 5;
  optional string variation_preview_url = 6;
  optional string course_id = 7;
  optional string course_url = 8;
  optional string cover_image_url = 9;
  optional float rating = 10;
  optional int32 review_count = 11;
  optional string short_description = 12;
  optional string user_color = 13;
}

message GameReviewCourseRecommendationDecision {
  oneof _rating {
  int32 rating = 6;
  }
  optional b
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05483"></a>
## FND-05483: chesscom.game_review.v2.GameReviewCourseRecommendationClicked.cover_image_url = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string cover_image_url = 9;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12722.

```text
ing variation_preview_url = 6;
  optional string course_id = 7;
  optional string course_url = 8;
  optional string cover_image_url = 9;
  optional float rating = 10;
  optional int32 review_count = 11;
  optional string short_description = 12;
  optional string user_color = 13;
}

message GameReviewCourseRecommendationDecision {
  oneof _rating {
  int32 rating = 6;
  }
  optional bool rec_eligible = 1;
  optional b
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05484"></a>
## FND-05484: chesscom.game_review.v2.GameReviewCourseRecommendationClicked.rating = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float rating = 10;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12761.

```text
al string course_id = 7;
  optional string course_url = 8;
  optional string cover_image_url = 9;
  optional float rating = 10;
  optional int32 review_count = 11;
  optional string short_description = 12;
  optional string user_color = 13;
}

message GameReviewCourseRecommendationDecision {
  oneof _rating {
  int32 rating = 6;
  }
  optional bool rec_eligible = 1;
  optional bool course_matched = 2;
  optional .che
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05485"></a>
## FND-05485: chesscom.game_review.v2.GameReviewCourseRecommendationClicked.review_count = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 review_count = 11;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12791.

```text
ional string course_url = 8;
  optional string cover_image_url = 9;
  optional float rating = 10;
  optional int32 review_count = 11;
  optional string short_description = 12;
  optional string user_color = 13;
}

message GameReviewCourseRecommendationDecision {
  oneof _rating {
  int32 rating = 6;
  }
  optional bool rec_eligible = 1;
  optional bool course_matched = 2;
  optional .chesscom.game_review.v2.GameRevie
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05486"></a>
## FND-05486: chesscom.game_review.v2.GameReviewCourseRecommendationClicked.short_description = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string short_description = 12;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12827.

```text
nal string cover_image_url = 9;
  optional float rating = 10;
  optional int32 review_count = 11;
  optional string short_description = 12;
  optional string user_color = 13;
}

message GameReviewCourseRecommendationDecision {
  oneof _rating {
  int32 rating = 6;
  }
  optional bool rec_eligible = 1;
  optional bool course_matched = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05487"></a>
## FND-05487: chesscom.game_review.v2.GameReviewCourseRecommendationClicked.user_color = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_color = 13;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12869.

```text
 float rating = 10;
  optional int32 review_count = 11;
  optional string short_description = 12;
  optional string user_color = 13;
}

message GameReviewCourseRecommendationDecision {
  oneof _rating {
  int32 rating = 6;
  }
  optional bool rec_eligible = 1;
  optional bool course_matched = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason reason = 3;
  optional .chesscom.courses.v
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05488"></a>
## FND-05488: message declaration: chesscom.game_review.v2.GameReviewCourseRecommendationDecision

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewCourseRecommendationDecision {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12905.

```text
 review_count = 11;
  optional string short_description = 12;
  optional string user_color = 13;
}

message GameReviewCourseRecommendationDecision {
  oneof _rating {
  int32 rating = 6;
  }
  optional bool rec_eligible = 1;
  optional bool course_matched = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason reason = 3;
  optional .chesscom.courses.v1.RecommendationReason recommendatio
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05489"></a>
## FND-05489: oneof declaration: chesscom.game_review.v2.GameReviewCourseRecommendationDecision._rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12956.

```text
tion = 12;
  optional string user_color = 13;
}

message GameReviewCourseRecommendationDecision {
  oneof _rating {
  int32 rating = 6;
  }
  optional bool rec_eligible = 1;
  optional bool course_matched = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason reason = 3;
  optional .chesscom.courses.v1.RecommendationReason recommendation_reason = 4;
  optional string fen = 5;
}

message
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05490"></a>
## FND-05490: chesscom.game_review.v2.GameReviewCourseRecommendationDecision.rating = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating = 6;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12974.

```text
nal string user_color = 13;
}

message GameReviewCourseRecommendationDecision {
  oneof _rating {
  int32 rating = 6;
  }
  optional bool rec_eligible = 1;
  optional bool course_matched = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason reason = 3;
  optional .chesscom.courses.v1.RecommendationReason recommendation_reason = 4;
  optional string fen = 5;
}

message GameReviewCourseR
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05491"></a>
## FND-05491: chesscom.game_review.v2.GameReviewCourseRecommendationDecision.rec_eligible = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool rec_eligible = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12998.

```text
13;
}

message GameReviewCourseRecommendationDecision {
  oneof _rating {
  int32 rating = 6;
  }
  optional bool rec_eligible = 1;
  optional bool course_matched = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason reason = 3;
  optional .chesscom.courses.v1.RecommendationReason recommendation_reason = 4;
  optional string fen = 5;
}

message GameReviewCourseRecommendationSuppressed 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05492"></a>
## FND-05492: chesscom.game_review.v2.GameReviewCourseRecommendationDecision.course_matched = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool course_matched = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13032.

```text
ommendationDecision {
  oneof _rating {
  int32 rating = 6;
  }
  optional bool rec_eligible = 1;
  optional bool course_matched = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason reason = 3;
  optional .chesscom.courses.v1.RecommendationReason recommendation_reason = 4;
  optional string fen = 5;
}

message GameReviewCourseRecommendationSuppressed {
  oneof _type {
  .chesscom.game
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05493"></a>
## FND-05493: chesscom.game_review.v2.GameReviewCourseRecommendationDecision.reason = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason reason = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13068.

```text
g {
  int32 rating = 6;
  }
  optional bool rec_eligible = 1;
  optional bool course_matched = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason reason = 3;
  optional .chesscom.courses.v1.RecommendationReason recommendation_reason = 4;
  optional string fen = 5;
}

message GameReviewCourseRecommendationSuppressed {
  oneof _type {
  .chesscom.game_review.v2.GameReviewCourseRecommend
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05494"></a>
## FND-05494: chesscom.game_review.v2.GameReviewCourseRecommendationDecision.recommendation_reason = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses.v1.RecommendationReason recommendation_reason = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13161.

```text
= 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason reason = 3;
  optional .chesscom.courses.v1.RecommendationReason recommendation_reason = 4;
  optional string fen = 5;
}

message GameReviewCourseRecommendationSuppressed {
  oneof _type {
  .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 2;
  }
  oneof _rating {
  int32 rating = 3;
  }
  oneof _fen {
  string fen
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05495"></a>
## FND-05495: chesscom.game_review.v2.GameReviewCourseRecommendationDecision.fen = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string fen = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12583.

```text
m.game_review.v2.GameReviewCourseRecommendationType type = 3;
  optional string opening_name = 4;
  optional string fen = 5;
  optional string variation_preview_url = 6;
  optional string course_id = 7;
  optional string course_url = 8;
  optional string cover_image_url = 9;
  optional float rating = 10;
  optional int32 review_count = 11;
  optional string short_description = 12;
  optional string user_color = 13;
}
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05496"></a>
## FND-05496: message declaration: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewCourseRecommendationSuppressed {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13269.

```text
 .chesscom.courses.v1.RecommendationReason recommendation_reason = 4;
  optional string fen = 5;
}

message GameReviewCourseRecommendationSuppressed {
  oneof _type {
  .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 2;
  }
  oneof _rating {
  int32 rating = 3;
  }
  oneof _fen {
  string fen = 4;
  }
  oneof _opening {
  string opening = 5;
  }
  optional .chesscom.game_review.v2.GameReviewCourseR
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05497"></a>
## FND-05497: oneof declaration: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressed._type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _type {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13322.

```text
tion_reason = 4;
  optional string fen = 5;
}

message GameReviewCourseRecommendationSuppressed {
  oneof _type {
  .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 2;
  }
  oneof _rating {
  int32 rating = 3;
  }
  oneof _fen {
  string fen = 4;
  }
  oneof _opening {
  string opening = 5;
  }
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason reason = 1;
}

message
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05498"></a>
## FND-05498: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressed.type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewCourseRecommendationType type = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13338.

```text

  optional string fen = 5;
}

message GameReviewCourseRecommendationSuppressed {
  oneof _type {
  .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 2;
  }
  oneof _rating {
  int32 rating = 3;
  }
  oneof _fen {
  string fen = 4;
  }
  oneof _opening {
  string opening = 5;
  }
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason reason = 1;
}

message GameReviewCours
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05499"></a>
## FND-05499: oneof declaration: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressed._rating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _rating {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12956.

```text
tion = 12;
  optional string user_color = 13;
}

message GameReviewCourseRecommendationDecision {
  oneof _rating {
  int32 rating = 6;
  }
  optional bool rec_eligible = 1;
  optional bool course_matched = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason reason = 3;
  optional .chesscom.courses.v1.RecommendationReason recommendation_reason = 4;
  optional string fen = 5;
}

message
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05500"></a>
## FND-05500: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressed.rating = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 rating = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13432.

```text
e {
  .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 2;
  }
  oneof _rating {
  int32 rating = 3;
  }
  oneof _fen {
  string fen = 4;
  }
  oneof _opening {
  string opening = 5;
  }
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason reason = 1;
}

message GameReviewCourseDeviationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
}

me
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05501"></a>
## FND-05501: oneof declaration: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressed._fen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _fen {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13456.

```text
iew.v2.GameReviewCourseRecommendationType type = 2;
  }
  oneof _rating {
  int32 rating = 3;
  }
  oneof _fen {
  string fen = 4;
  }
  oneof _opening {
  string opening = 5;
  }
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason reason = 1;
}

message GameReviewCourseDeviationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
}

message GameReviewCourseDe
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05502"></a>
## FND-05502: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressed.fen = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string fen = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13471.

```text
ewCourseRecommendationType type = 2;
  }
  oneof _rating {
  int32 rating = 3;
  }
  oneof _fen {
  string fen = 4;
  }
  oneof _opening {
  string opening = 5;
  }
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason reason = 1;
}

message GameReviewCourseDeviationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
}

message GameReviewCourseDeviationClicked 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05503"></a>
## FND-05503: oneof declaration: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressed._opening

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _opening {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13493.

```text
Type type = 2;
  }
  oneof _rating {
  int32 rating = 3;
  }
  oneof _fen {
  string fen = 4;
  }
  oneof _opening {
  string opening = 5;
  }
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason reason = 1;
}

message GameReviewCourseDeviationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
}

message GameReviewCourseDeviationClicked {
  optional string co
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05504"></a>
## FND-05504: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressed.opening = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string opening = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13512.

```text
  oneof _rating {
  int32 rating = 3;
  }
  oneof _fen {
  string fen = 4;
  }
  oneof _opening {
  string opening = 5;
  }
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason reason = 1;
}

message GameReviewCourseDeviationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
}

message GameReviewCourseDeviationClicked {
  optional string course_name = 1;
  op
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05505"></a>
## FND-05505: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressed.reason = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason reason = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13538.

```text
rating = 3;
  }
  oneof _fen {
  string fen = 4;
  }
  oneof _opening {
  string opening = 5;
  }
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason reason = 1;
}

message GameReviewCourseDeviationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
}

message GameReviewCourseDeviationClicked {
  optional string course_name = 1;
  optional string author_name 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05506"></a>
## FND-05506: message declaration: chesscom.game_review.v2.GameReviewCourseDeviationViewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewCourseDeviationViewed {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13635.

```text

  optional .chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason reason = 1;
}

message GameReviewCourseDeviationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
}

message GameReviewCourseDeviationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
}

message GameReviewCourseDeviationShowMovesClicked {
  optional string course_name = 1;
  
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05507"></a>
## FND-05507: chesscom.game_review.v2.GameReviewCourseDeviationViewed.course_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_name = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12194.

```text
ion = 8;
  optional string engine_strength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCour
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05508"></a>
## FND-05508: chesscom.game_review.v2.GameReviewCourseDeviationViewed.author_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string author_name = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12229.

```text
trength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
  op
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05509"></a>
## FND-05509: message declaration: chesscom.game_review.v2.GameReviewCourseDeviationClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewCourseDeviationClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13750.

```text
iewCourseDeviationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
}

message GameReviewCourseDeviationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
}

message GameReviewCourseDeviationShowMovesClicked {
  optional string course_name = 1;
  optional string author_name = 2;
}

message GameReviewUserMoveMade {
  oneof _user_or_opponent_move {
  .chesscom.g
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05510"></a>
## FND-05510: chesscom.game_review.v2.GameReviewCourseDeviationClicked.course_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_name = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12194.

```text
ion = 8;
  optional string engine_strength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCour
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05511"></a>
## FND-05511: chesscom.game_review.v2.GameReviewCourseDeviationClicked.author_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string author_name = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12229.

```text
trength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
  op
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05512"></a>
## FND-05512: message declaration: chesscom.game_review.v2.GameReviewCourseDeviationShowMovesClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewCourseDeviationShowMovesClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13866.

```text
ewCourseDeviationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
}

message GameReviewCourseDeviationShowMovesClicked {
  optional string course_name = 1;
  optional string author_name = 2;
}

message GameReviewUserMoveMade {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameRev
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05513"></a>
## FND-05513: chesscom.game_review.v2.GameReviewCourseDeviationShowMovesClicked.course_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string course_name = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12194.

```text
ion = 8;
  optional string engine_strength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCour
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05514"></a>
## FND-05514: chesscom.game_review.v2.GameReviewCourseDeviationShowMovesClicked.author_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string author_name = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 12229.

```text
trength = 9;
}

message GameReviewCourseRecommendationViewed {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
}

message GameReviewCourseRecommendationClicked {
  optional string course_name = 1;
  optional string author_name = 2;
  optional .chesscom.game_review.v2.GameReviewCourseRecommendationType type = 3;
  op
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05515"></a>
## FND-05515: message declaration: chesscom.game_review.v2.GameReviewUserMoveMade

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewUserMoveMade {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 13991.

```text
eviationShowMovesClicked {
  optional string course_name = 1;
  optional string author_name = 2;
}

message GameReviewUserMoveMade {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional i
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05516"></a>
## FND-05516: oneof declaration: chesscom.game_review.v2.GameReviewUserMoveMade._user_or_opponent_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_or_opponent_move {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7207.

```text
result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05517"></a>
## FND-05517: chesscom.game_review.v2.GameReviewUserMoveMade.user_or_opponent_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7240.

```text
s_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chessco
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05518"></a>
## FND-05518: oneof declaration: chesscom.game_review.v2.GameReviewUserMoveMade._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05519"></a>
## FND-05519: chesscom.game_review.v2.GameReviewUserMoveMade.result = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7335.

```text
 {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.gam
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05520"></a>
## FND-05520: chesscom.game_review.v2.GameReviewUserMoveMade.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6869.

```text
nEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClassificationsExpandClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassifi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05521"></a>
## FND-05521: chesscom.game_review.v2.GameReviewUserMoveMade.percent_reviewed = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8587.

```text
t = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 4;
}

message GameReviewMoveChangedClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05522"></a>
## FND-05522: message declaration: chesscom.game_review.v2.GameReviewTakeawaysViewed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewTakeawaysViewed {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14341.

```text
ion_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 4;
}

message GameReviewTakeawaysViewed {
  oneof _train_cta_destination {
  .chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination train_cta_destination = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  opti
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05523"></a>
## FND-05523: oneof declaration: chesscom.game_review.v2.GameReviewTakeawaysViewed._train_cta_destination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _train_cta_destination {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14379.

```text
classification = 1;
  optional int32 percent_reviewed = 4;
}

message GameReviewTakeawaysViewed {
  oneof _train_cta_destination {
  .chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination train_cta_destination = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool paywall_shown = 2;
}

messag
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05524"></a>
## FND-05524: chesscom.game_review.v2.GameReviewTakeawaysViewed.train_cta_destination = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination train_cta_destination = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14412.

```text
t32 percent_reviewed = 4;
}

message GameReviewTakeawaysViewed {
  oneof _train_cta_destination {
  .chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination train_cta_destination = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool paywall_shown = 2;
}

message GameReviewTakeawaysUpgradeClick
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05525"></a>
## FND-05525: oneof declaration: chesscom.game_review.v2.GameReviewTakeawaysViewed._train_item_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _train_item_type {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14509.

```text

  .chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination train_cta_destination = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool paywall_shown = 2;
}

message GameReviewTakeawaysUpgradeClicked {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
}

message GameReviewTakeawaysT
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05526"></a>
## FND-05526: chesscom.game_review.v2.GameReviewTakeawaysViewed.train_item_type = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.train.v1.TrainItemType train_item_type = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14536.

```text
.GameReviewTakeawaysTrainCtaDestination train_cta_destination = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool paywall_shown = 2;
}

message GameReviewTakeawaysUpgradeClicked {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
}

message GameReviewTakeawaysTrainCtaClicked {
  oneof _g
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05527"></a>
## FND-05527: chesscom.game_review.v2.GameReviewTakeawaysViewed.category = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.stats.v1.AdvancedStatType category = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14596.

```text
n = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool paywall_shown = 2;
}

message GameReviewTakeawaysUpgradeClicked {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
}

message GameReviewTakeawaysTrainCtaClicked {
  oneof _game_id {
  string game_id = 3;
  }
  oneof _train_item_type 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05528"></a>
## FND-05528: chesscom.game_review.v2.GameReviewTakeawaysViewed.paywall_shown = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool paywall_shown = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14657.

```text
ainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool paywall_shown = 2;
}

message GameReviewTakeawaysUpgradeClicked {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
}

message GameReviewTakeawaysTrainCtaClicked {
  oneof _game_id {
  string game_id = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05529"></a>
## FND-05529: message declaration: chesscom.game_review.v2.GameReviewTakeawaysUpgradeClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewTakeawaysUpgradeClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14693.

```text

  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool paywall_shown = 2;
}

message GameReviewTakeawaysUpgradeClicked {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
}

message GameReviewTakeawaysTrainCtaClicked {
  oneof _game_id {
  string game_id = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.Advan
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05530"></a>
## FND-05530: chesscom.game_review.v2.GameReviewTakeawaysUpgradeClicked.category = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.stats.v1.AdvancedStatType category = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14596.

```text
n = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool paywall_shown = 2;
}

message GameReviewTakeawaysUpgradeClicked {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
}

message GameReviewTakeawaysTrainCtaClicked {
  oneof _game_id {
  string game_id = 3;
  }
  oneof _train_item_type 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05531"></a>
## FND-05531: message declaration: chesscom.game_review.v2.GameReviewTakeawaysTrainCtaClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewTakeawaysTrainCtaClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14801.

```text
GameReviewTakeawaysUpgradeClicked {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
}

message GameReviewTakeawaysTrainCtaClicked {
  oneof _game_id {
  string game_id = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination destina
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05532"></a>
## FND-05532: oneof declaration: chesscom.game_review.v2.GameReviewTakeawaysTrainCtaClicked._game_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_id {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5169.

```text
e GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;
}

message GameReviewPremiumModalOpened {
  oneof _result {
  .chesscom.game_r
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05533"></a>
## FND-05533: chesscom.game_review.v2.GameReviewTakeawaysTrainCtaClicked.game_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string game_id = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14867.

```text
AdvancedStatType category = 1;
}

message GameReviewTakeawaysTrainCtaClicked {
  oneof _game_id {
  string game_id = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination destination = 2;
}

message GameReviewTakeawaysNextClicked {
  oneof _tra
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05534"></a>
## FND-05534: oneof declaration: chesscom.game_review.v2.GameReviewTakeawaysTrainCtaClicked._train_item_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _train_item_type {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14509.

```text

  .chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination train_cta_destination = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool paywall_shown = 2;
}

message GameReviewTakeawaysUpgradeClicked {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
}

message GameReviewTakeawaysT
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05535"></a>
## FND-05535: chesscom.game_review.v2.GameReviewTakeawaysTrainCtaClicked.train_item_type = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.train.v1.TrainItemType train_item_type = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14536.

```text
.GameReviewTakeawaysTrainCtaDestination train_cta_destination = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool paywall_shown = 2;
}

message GameReviewTakeawaysUpgradeClicked {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
}

message GameReviewTakeawaysTrainCtaClicked {
  oneof _g
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05536"></a>
## FND-05536: chesscom.game_review.v2.GameReviewTakeawaysTrainCtaClicked.category = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.stats.v1.AdvancedStatType category = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14596.

```text
n = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool paywall_shown = 2;
}

message GameReviewTakeawaysUpgradeClicked {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
}

message GameReviewTakeawaysTrainCtaClicked {
  oneof _game_id {
  string game_id = 3;
  }
  oneof _train_item_type 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05537"></a>
## FND-05537: chesscom.game_review.v2.GameReviewTakeawaysTrainCtaClicked.destination = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination destination = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15041.

```text
ainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional .chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination destination = 2;
}

message GameReviewTakeawaysNextClicked {
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 3;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool train_cta_shown = 2;
}
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05538"></a>
## FND-05538: message declaration: chesscom.game_review.v2.GameReviewTakeawaysNextClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewTakeawaysNextClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15134.

```text
= 1;
  optional .chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination destination = 2;
}

message GameReviewTakeawaysNextClicked {
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 3;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool train_cta_shown = 2;
}

message GameReviewMoveContextExtension {
  oneof _user_or_opponent_move {
  .chesscom.game_
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05539"></a>
## FND-05539: oneof declaration: chesscom.game_review.v2.GameReviewTakeawaysNextClicked._train_item_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _train_item_type {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14509.

```text

  .chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination train_cta_destination = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool paywall_shown = 2;
}

message GameReviewTakeawaysUpgradeClicked {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
}

message GameReviewTakeawaysT
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05540"></a>
## FND-05540: chesscom.game_review.v2.GameReviewTakeawaysNextClicked.train_item_type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.train.v1.TrainItemType train_item_type = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15204.

```text
stination destination = 2;
}

message GameReviewTakeawaysNextClicked {
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 3;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool train_cta_shown = 2;
}

message GameReviewMoveContextExtension {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  optional
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05541"></a>
## FND-05541: chesscom.game_review.v2.GameReviewTakeawaysNextClicked.category = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.stats.v1.AdvancedStatType category = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 14596.

```text
n = 3;
  }
  oneof _train_item_type {
  .chesscom.train.v1.TrainItemType train_item_type = 4;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool paywall_shown = 2;
}

message GameReviewTakeawaysUpgradeClicked {
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
}

message GameReviewTakeawaysTrainCtaClicked {
  oneof _game_id {
  string game_id = 3;
  }
  oneof _train_item_type 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05542"></a>
## FND-05542: chesscom.game_review.v2.GameReviewTakeawaysNextClicked.train_cta_shown = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool train_cta_shown = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15325.

```text
ainItemType train_item_type = 3;
  }
  optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool train_cta_shown = 2;
}

message GameReviewMoveContextExtension {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  optional int32 move_number = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05543"></a>
## FND-05543: message declaration: chesscom.game_review.v2.GameReviewMoveContextExtension

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewMoveContextExtension {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15363.

```text
 optional .chesscom.stats.v1.AdvancedStatType category = 1;
  optional bool train_cta_shown = 2;
}

message GameReviewMoveContextExtension {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  optional int32 move_number = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional bool is_key_move = 4;
}

message Game
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05544"></a>
## FND-05544: oneof declaration: chesscom.game_review.v2.GameReviewMoveContextExtension._user_or_opponent_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_or_opponent_move {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7207.

```text
result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05545"></a>
## FND-05545: chesscom.game_review.v2.GameReviewMoveContextExtension.user_or_opponent_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7240.

```text
s_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chessco
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05546"></a>
## FND-05546: chesscom.game_review.v2.GameReviewMoveContextExtension.move_number = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 move_number = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15516.

```text
r_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  optional int32 move_number = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional bool is_key_move = 4;
}

message GameReviewContextExtension {
  oneof _specific_move {
  .chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove specific_move = 1;
  }
  message G
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05547"></a>
## FND-05547: chesscom.game_review.v2.GameReviewMoveContextExtension.move_classification = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15550.

```text
ame_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  optional int32 move_number = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional bool is_key_move = 4;
}

message GameReviewContextExtension {
  oneof _specific_move {
  .chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove specific_move = 1;
  }
  message GameReviewMove {
    oneof _user_or
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05548"></a>
## FND-05548: chesscom.game_review.v2.GameReviewMoveContextExtension.is_key_move = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_key_move = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15637.

```text
umber = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional bool is_key_move = 4;
}

message GameReviewContextExtension {
  oneof _specific_move {
  .chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove specific_move = 1;
  }
  message GameReviewMove {
    oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05549"></a>
## FND-05549: message declaration: chesscom.game_review.v2.GameReviewContextExtension

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewContextExtension {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15671.

```text
planation_engine.v1.MoveClassification move_classification = 3;
  optional bool is_key_move = 4;
}

message GameReviewContextExtension {
  oneof _specific_move {
  .chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove specific_move = 1;
  }
  message GameReviewMove {
    oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
    }
  optional int32 move_num
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05550"></a>
## FND-05550: oneof declaration: chesscom.game_review.v2.GameReviewContextExtension._specific_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _specific_move {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15710.

```text
move_classification = 3;
  optional bool is_key_move = 4;
}

message GameReviewContextExtension {
  oneof _specific_move {
  .chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove specific_move = 1;
  }
  message GameReviewMove {
    oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
    }
  optional int32 move_number = 1;
  optional .chesscom.explanati
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05551"></a>
## FND-05551: chesscom.game_review.v2.GameReviewContextExtension.specific_move = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove specific_move = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15735.

```text
  optional bool is_key_move = 4;
}

message GameReviewContextExtension {
  oneof _specific_move {
  .chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove specific_move = 1;
  }
  message GameReviewMove {
    oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
    }
  optional int32 move_number = 1;
  optional .chesscom.explanation_engine.v1.MoveClassifi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05552"></a>
## FND-05552: message declaration: chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewMove {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15827.

```text
ove {
  .chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove specific_move = 1;
  }
  message GameReviewMove {
    oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
    }
  optional int32 move_number = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional bool is_key_move = 4;
  }
}

message GameReviewEx
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05553"></a>
## FND-05553: oneof declaration: chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove._user_or_opponent_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_or_opponent_move {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7207.

```text
result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05554"></a>
## FND-05554: chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove.user_or_opponent_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7240.

```text
s_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chessco
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05555"></a>
## FND-05555: chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove.move_number = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 move_number = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15516.

```text
r_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  optional int32 move_number = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional bool is_key_move = 4;
}

message GameReviewContextExtension {
  oneof _specific_move {
  .chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove specific_move = 1;
  }
  message G
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05556"></a>
## FND-05556: chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove.move_classification = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15550.

```text
ame_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  optional int32 move_number = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional bool is_key_move = 4;
}

message GameReviewContextExtension {
  oneof _specific_move {
  .chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove specific_move = 1;
  }
  message GameReviewMove {
    oneof _user_or
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05557"></a>
## FND-05557: chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove.is_key_move = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_key_move = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 15637.

```text
umber = 1;
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 3;
  optional bool is_key_move = 4;
}

message GameReviewContextExtension {
  oneof _specific_move {
  .chesscom.game_review.v2.GameReviewContextExtension.GameReviewMove specific_move = 1;
  }
  message GameReviewMove {
    oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05558"></a>
## FND-05558: message declaration: chesscom.game_review.v2.GameReviewExplainButtonClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewExplainButtonClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 16127.

```text
ation_engine.v1.MoveClassification move_classification = 3;
  optional bool is_key_move = 4;
  }
}

message GameReviewExplainButtonClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  op
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05559"></a>
## FND-05559: oneof declaration: chesscom.game_review.v2.GameReviewExplainButtonClicked._user_or_opponent_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_or_opponent_move {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7207.

```text
result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05560"></a>
## FND-05560: chesscom.game_review.v2.GameReviewExplainButtonClicked.user_or_opponent_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7240.

```text
s_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chessco
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05561"></a>
## FND-05561: oneof declaration: chesscom.game_review.v2.GameReviewExplainButtonClicked._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05562"></a>
## FND-05562: chesscom.game_review.v2.GameReviewExplainButtonClicked.result = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7335.

```text
 {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.gam
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05563"></a>
## FND-05563: chesscom.game_review.v2.GameReviewExplainButtonClicked.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6869.

```text
nEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClassificationsExpandClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassifi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05564"></a>
## FND-05564: chesscom.game_review.v2.GameReviewExplainButtonClicked.percent_reviewed = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8587.

```text
t = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 4;
}

message GameReviewMoveChangedClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05565"></a>
## FND-05565: message declaration: chesscom.game_review.v2.GameReviewExplainButtonClosed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewExplainButtonClosed {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 16485.

```text
ion_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 4;
}

message GameReviewExplainButtonClosed {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  opt
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05566"></a>
## FND-05566: oneof declaration: chesscom.game_review.v2.GameReviewExplainButtonClosed._user_or_opponent_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_or_opponent_move {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7207.

```text
result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05567"></a>
## FND-05567: chesscom.game_review.v2.GameReviewExplainButtonClosed.user_or_opponent_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7240.

```text
s_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chessco
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05568"></a>
## FND-05568: oneof declaration: chesscom.game_review.v2.GameReviewExplainButtonClosed._result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _result {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5091.

```text
_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05569"></a>
## FND-05569: chesscom.game_review.v2.GameReviewExplainButtonClosed.result = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7335.

```text
 {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 3;
  }
  oneof _result {
  .chesscom.gam
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05570"></a>
## FND-05570: chesscom.game_review.v2.GameReviewExplainButtonClosed.move_classification = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6869.

```text
nEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClassificationsExpandClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassifi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05571"></a>
## FND-05571: chesscom.game_review.v2.GameReviewExplainButtonClosed.percent_reviewed = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 8587.

```text
t = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 4;
}

message GameReviewMoveChangedClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 4;
  }
  optional .chesscom.explanation_engine.v1.MoveClassi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05572"></a>
## FND-05572: message declaration: chesscom.game_review.v2.GameReviewExplainMoveNavClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewExplainMoveNavClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 16842.

```text
ion_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 4;
}

message GameReviewExplainMoveNavClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  o
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05573"></a>
## FND-05573: oneof declaration: chesscom.game_review.v2.GameReviewExplainMoveNavClicked._user_or_opponent_move

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_or_opponent_move {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7207.

```text
result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05574"></a>
## FND-05574: chesscom.game_review.v2.GameReviewExplainMoveNavClicked.user_or_opponent_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7240.

```text
s_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 3;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
}

message GameReviewStartGameClicked {
  oneof _game_review_screen {
  .chessco
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
