# data_models — findings 5001–5100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-05275"></a>
## FND-05275: chesscom.game_review.v2.GameReviewStartSource.GAME_REVIEW_START_SOURCE_GAME_END = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_START_SOURCE_GAME_END = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2370.

```text
CE_HOME = 1;
  GAME_REVIEW_START_SOURCE_GAME_ARCHIVE = 2;
  GAME_REVIEW_START_SOURCE_PROFILE = 3;
  GAME_REVIEW_START_SOURCE_GAME_END = 4;
  GAME_REVIEW_START_SOURCE_ANALYSIS = 5;
  GAME_REVIEW_START_SOURCE_COACH_NUDGE = 6;
  GAME_REVIEW_START_SOURCE_DEEPLINK = 7;
  GAME_REVIEW_START_SOURCE_STATS = 8;
}

enum GameReviewResult {
  GAME_REVIEW_RESULT_UNSPECIFIED = 0;
  GAME_REVIEW_RESULT_USER_WON = 1;
  GAME_REVIEW_RES
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05276"></a>
## FND-05276: chesscom.game_review.v2.GameReviewStartSource.GAME_REVIEW_START_SOURCE_ANALYSIS = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_START_SOURCE_ANALYSIS = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2411.

```text
AME_ARCHIVE = 2;
  GAME_REVIEW_START_SOURCE_PROFILE = 3;
  GAME_REVIEW_START_SOURCE_GAME_END = 4;
  GAME_REVIEW_START_SOURCE_ANALYSIS = 5;
  GAME_REVIEW_START_SOURCE_COACH_NUDGE = 6;
  GAME_REVIEW_START_SOURCE_DEEPLINK = 7;
  GAME_REVIEW_START_SOURCE_STATS = 8;
}

enum GameReviewResult {
  GAME_REVIEW_RESULT_UNSPECIFIED = 0;
  GAME_REVIEW_RESULT_USER_WON = 1;
  GAME_REVIEW_RESULT_USER_LOST = 2;
  GAME_REVIEW_RESULT_U
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05277"></a>
## FND-05277: chesscom.game_review.v2.GameReviewStartSource.GAME_REVIEW_START_SOURCE_COACH_NUDGE = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_START_SOURCE_COACH_NUDGE = 6;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2452.

```text
CE_PROFILE = 3;
  GAME_REVIEW_START_SOURCE_GAME_END = 4;
  GAME_REVIEW_START_SOURCE_ANALYSIS = 5;
  GAME_REVIEW_START_SOURCE_COACH_NUDGE = 6;
  GAME_REVIEW_START_SOURCE_DEEPLINK = 7;
  GAME_REVIEW_START_SOURCE_STATS = 8;
}

enum GameReviewResult {
  GAME_REVIEW_RESULT_UNSPECIFIED = 0;
  GAME_REVIEW_RESULT_USER_WON = 1;
  GAME_REVIEW_RESULT_USER_LOST = 2;
  GAME_REVIEW_RESULT_USER_DRAW = 3;
}

enum GameReviewCourseRec
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05278"></a>
## FND-05278: chesscom.game_review.v2.GameReviewStartSource.GAME_REVIEW_START_SOURCE_DEEPLINK = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_START_SOURCE_DEEPLINK = 7;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2496.

```text
AME_END = 4;
  GAME_REVIEW_START_SOURCE_ANALYSIS = 5;
  GAME_REVIEW_START_SOURCE_COACH_NUDGE = 6;
  GAME_REVIEW_START_SOURCE_DEEPLINK = 7;
  GAME_REVIEW_START_SOURCE_STATS = 8;
}

enum GameReviewResult {
  GAME_REVIEW_RESULT_UNSPECIFIED = 0;
  GAME_REVIEW_RESULT_USER_WON = 1;
  GAME_REVIEW_RESULT_USER_LOST = 2;
  GAME_REVIEW_RESULT_USER_DRAW = 3;
}

enum GameReviewCourseRecommendationType {
  GAME_REVIEW_COURSE_RECOM
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05279"></a>
## FND-05279: chesscom.game_review.v2.GameReviewStartSource.GAME_REVIEW_START_SOURCE_STATS = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_START_SOURCE_STATS = 8;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2537.

```text
NALYSIS = 5;
  GAME_REVIEW_START_SOURCE_COACH_NUDGE = 6;
  GAME_REVIEW_START_SOURCE_DEEPLINK = 7;
  GAME_REVIEW_START_SOURCE_STATS = 8;
}

enum GameReviewResult {
  GAME_REVIEW_RESULT_UNSPECIFIED = 0;
  GAME_REVIEW_RESULT_USER_WON = 1;
  GAME_REVIEW_RESULT_USER_LOST = 2;
  GAME_REVIEW_RESULT_USER_DRAW = 3;
}

enum GameReviewCourseRecommendationType {
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_UNSPECIFIED = 0;
  GAME_RE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05280"></a>
## FND-05280: enum declaration: chesscom.game_review.v2.GameReviewResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameReviewResult {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2576.

```text
_COACH_NUDGE = 6;
  GAME_REVIEW_START_SOURCE_DEEPLINK = 7;
  GAME_REVIEW_START_SOURCE_STATS = 8;
}

enum GameReviewResult {
  GAME_REVIEW_RESULT_UNSPECIFIED = 0;
  GAME_REVIEW_RESULT_USER_WON = 1;
  GAME_REVIEW_RESULT_USER_LOST = 2;
  GAME_REVIEW_RESULT_USER_DRAW = 3;
}

enum GameReviewCourseRecommendationType {
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_BOOK = 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05281"></a>
## FND-05281: chesscom.game_review.v2.GameReviewResult.GAME_REVIEW_RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2602.

```text
EVIEW_START_SOURCE_DEEPLINK = 7;
  GAME_REVIEW_START_SOURCE_STATS = 8;
}

enum GameReviewResult {
  GAME_REVIEW_RESULT_UNSPECIFIED = 0;
  GAME_REVIEW_RESULT_USER_WON = 1;
  GAME_REVIEW_RESULT_USER_LOST = 2;
  GAME_REVIEW_RESULT_USER_DRAW = 3;
}

enum GameReviewCourseRecommendationType {
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_BOOK = 1;
  GAME_REVIEW_COURSE_RE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05282"></a>
## FND-05282: chesscom.game_review.v2.GameReviewResult.GAME_REVIEW_RESULT_USER_WON = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_RESULT_USER_WON = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2640.

```text
E_REVIEW_START_SOURCE_STATS = 8;
}

enum GameReviewResult {
  GAME_REVIEW_RESULT_UNSPECIFIED = 0;
  GAME_REVIEW_RESULT_USER_WON = 1;
  GAME_REVIEW_RESULT_USER_LOST = 2;
  GAME_REVIEW_RESULT_USER_DRAW = 3;
}

enum GameReviewCourseRecommendationType {
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_BOOK = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_MISTAKE = 2;
  GAME_
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05283"></a>
## FND-05283: chesscom.game_review.v2.GameReviewResult.GAME_REVIEW_RESULT_USER_LOST = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_RESULT_USER_LOST = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2675.

```text

enum GameReviewResult {
  GAME_REVIEW_RESULT_UNSPECIFIED = 0;
  GAME_REVIEW_RESULT_USER_WON = 1;
  GAME_REVIEW_RESULT_USER_LOST = 2;
  GAME_REVIEW_RESULT_USER_DRAW = 3;
}

enum GameReviewCourseRecommendationType {
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_BOOK = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_MISTAKE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_E
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05284"></a>
## FND-05284: chesscom.game_review.v2.GameReviewResult.GAME_REVIEW_RESULT_USER_DRAW = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_RESULT_USER_DRAW = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2711.

```text
EW_RESULT_UNSPECIFIED = 0;
  GAME_REVIEW_RESULT_USER_WON = 1;
  GAME_REVIEW_RESULT_USER_LOST = 2;
  GAME_REVIEW_RESULT_USER_DRAW = 3;
}

enum GameReviewCourseRecommendationType {
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_BOOK = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_MISTAKE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_EXPLORER = 3;
}

enum GameReviewCours
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05285"></a>
## FND-05285: enum declaration: chesscom.game_review.v2.GameReviewCourseRecommendationType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameReviewCourseRecommendationType {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2748.

```text
IEW_RESULT_USER_WON = 1;
  GAME_REVIEW_RESULT_USER_LOST = 2;
  GAME_REVIEW_RESULT_USER_DRAW = 3;
}

enum GameReviewCourseRecommendationType {
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_BOOK = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_MISTAKE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_EXPLORER = 3;
}

enum GameReviewCourseRecommendationDecisionReason {
  GAM
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05286"></a>
## FND-05286: chesscom.game_review.v2.GameReviewCourseRecommendationType.GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2792.

```text
T_USER_LOST = 2;
  GAME_REVIEW_RESULT_USER_DRAW = 3;
}

enum GameReviewCourseRecommendationType {
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_BOOK = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_MISTAKE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_EXPLORER = 3;
}

enum GameReviewCourseRecommendationDecisionReason {
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REAS
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05287"></a>
## FND-05287: chesscom.game_review.v2.GameReviewCourseRecommendationType.GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_BOOK = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_BOOK = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2850.

```text
um GameReviewCourseRecommendationType {
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_BOOK = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_MISTAKE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_EXPLORER = 3;
}

enum GameReviewCourseRecommendationDecisionReason {
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_DE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05288"></a>
## FND-05288: chesscom.game_review.v2.GameReviewCourseRecommendationType.GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_MISTAKE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_MISTAKE = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2901.

```text
EW_COURSE_RECOMMENDATION_TYPE_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_BOOK = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_MISTAKE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_EXPLORER = 3;
}

enum GameReviewCourseRecommendationDecisionReason {
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_NO_COURSE_MATCHED = 1;
  GAME_REVIEW_
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05289"></a>
## FND-05289: chesscom.game_review.v2.GameReviewCourseRecommendationType.GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_EXPLORER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_EXPLORER = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 2955.

```text
REVIEW_COURSE_RECOMMENDATION_TYPE_BOOK = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_MISTAKE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_EXPLORER = 3;
}

enum GameReviewCourseRecommendationDecisionReason {
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_NO_COURSE_MATCHED = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_OWNS_OR_CLAIMED 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05290"></a>
## FND-05290: enum declaration: chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameReviewCourseRecommendationDecisionReason {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3011.

```text
W_COURSE_RECOMMENDATION_TYPE_MISTAKE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_TYPE_EXPLORER = 3;
}

enum GameReviewCourseRecommendationDecisionReason {
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_NO_COURSE_MATCHED = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_OWNS_OR_CLAIMED = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05291"></a>
## FND-05291: chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason.GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3065.

```text
W_COURSE_RECOMMENDATION_TYPE_EXPLORER = 3;
}

enum GameReviewCourseRecommendationDecisionReason {
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_NO_COURSE_MATCHED = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_OWNS_OR_CLAIMED = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_COURSE_FIT_RATING = 3;
  GAME_REVIEW_COURSE_RECOMMEND
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05292"></a>
## FND-05292: chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason.GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_NO_COURSE_MATCHED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_NO_COURSE_MATCHED = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3134.

```text
commendationDecisionReason {
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_NO_COURSE_MATCHED = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_OWNS_OR_CLAIMED = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_COURSE_FIT_RATING = 3;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_MATCHED = 4;
}

enum GameReviewCourseRecommenda
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05293"></a>
## FND-05293: chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason.GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_OWNS_OR_CLAIMED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_OWNS_OR_CLAIMED = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3209.

```text
EASON_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_NO_COURSE_MATCHED = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_OWNS_OR_CLAIMED = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_COURSE_FIT_RATING = 3;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_MATCHED = 4;
}

enum GameReviewCourseRecommendationSuppressionReason {
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REA
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05294"></a>
## FND-05294: chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason.GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_COURSE_FIT_RATING = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_COURSE_FIT_RATING = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3282.

```text
N_NO_COURSE_MATCHED = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_OWNS_OR_CLAIMED = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_COURSE_FIT_RATING = 3;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_MATCHED = 4;
}

enum GameReviewCourseRecommendationSuppressionReason {
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REAS
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05295"></a>
## FND-05295: chesscom.game_review.v2.GameReviewCourseRecommendationDecisionReason.GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_MATCHED = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_MATCHED = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3357.

```text
N_OWNS_OR_CLAIMED = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_COURSE_FIT_RATING = 3;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_MATCHED = 4;
}

enum GameReviewCourseRecommendationSuppressionReason {
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_AUDIENCE_INELIGIBLE = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05296"></a>
## FND-05296: enum declaration: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameReviewCourseRecommendationSuppressionReason {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3423.

```text
N_REASON_COURSE_FIT_RATING = 3;
  GAME_REVIEW_COURSE_RECOMMENDATION_DECISION_REASON_MATCHED = 4;
}

enum GameReviewCourseRecommendationSuppressionReason {
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_AUDIENCE_INELIGIBLE = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_LOCALE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSIO
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05297"></a>
## FND-05297: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason.GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3480.

```text
MMENDATION_DECISION_REASON_MATCHED = 4;
}

enum GameReviewCourseRecommendationSuppressionReason {
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_AUDIENCE_INELIGIBLE = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_LOCALE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_COACH_COMMENTARY = 3;
  GAME_REVIEW_COURSE_RECOM
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05298"></a>
## FND-05298: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason.GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_AUDIENCE_INELIGIBLE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_AUDIENCE_INELIGIBLE = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3552.

```text
dationSuppressionReason {
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_AUDIENCE_INELIGIBLE = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_LOCALE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_COACH_COMMENTARY = 3;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_FEATURE_FLAG = 4;
  GAME_REVIEW_COURSE_RECO
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05299"></a>
## FND-05299: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason.GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_LOCALE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_LOCALE = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3632.

```text
_UNSPECIFIED = 0;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_AUDIENCE_INELIGIBLE = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_LOCALE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_COACH_COMMENTARY = 3;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_FEATURE_FLAG = 4;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_EXPERIMENT_SEGMENT = 5;
  GAME_REVIEW_COURSE_RECOM
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05300"></a>
## FND-05300: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason.GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_COACH_COMMENTARY = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_COACH_COMMENTARY = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3699.

```text
EASON_AUDIENCE_INELIGIBLE = 1;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_LOCALE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_COACH_COMMENTARY = 3;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_FEATURE_FLAG = 4;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_EXPERIMENT_SEGMENT = 5;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_DEVIATION_SHOWN = 6;
  GAME_REVIEW_COU
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05301"></a>
## FND-05301: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason.GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_FEATURE_FLAG = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_FEATURE_FLAG = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3776.

```text
N_REASON_LOCALE = 2;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_COACH_COMMENTARY = 3;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_FEATURE_FLAG = 4;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_EXPERIMENT_SEGMENT = 5;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_DEVIATION_SHOWN = 6;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NOT_LOGGED_IN = 7;
  GAME_REVIEW_COURSE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05302"></a>
## FND-05302: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason.GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_EXPERIMENT_SEGMENT = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_EXPERIMENT_SEGMENT = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3849.

```text
ON_COACH_COMMENTARY = 3;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_FEATURE_FLAG = 4;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_EXPERIMENT_SEGMENT = 5;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_DEVIATION_SHOWN = 6;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NOT_LOGGED_IN = 7;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_USER_COLOR = 8;
  GAME_REVIEW_COURS
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05303"></a>
## FND-05303: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason.GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_DEVIATION_SHOWN = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_DEVIATION_SHOWN = 6;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 3928.

```text
_FEATURE_FLAG = 4;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_EXPERIMENT_SEGMENT = 5;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_DEVIATION_SHOWN = 6;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NOT_LOGGED_IN = 7;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_USER_COLOR = 8;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_QUALIFYING_POSITION = 9;
  GAME_REVIEW_C
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05304"></a>
## FND-05304: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason.GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NOT_LOGGED_IN = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NOT_LOGGED_IN = 7;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4004.

```text
PERIMENT_SEGMENT = 5;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_DEVIATION_SHOWN = 6;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NOT_LOGGED_IN = 7;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_USER_COLOR = 8;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_QUALIFYING_POSITION = 9;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_RPC_ERROR = 10;
}

enum GameReviewSh
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05305"></a>
## FND-05305: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason.GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_USER_COLOR = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_USER_COLOR = 8;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4078.

```text
ON_DEVIATION_SHOWN = 6;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NOT_LOGGED_IN = 7;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_USER_COLOR = 8;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_QUALIFYING_POSITION = 9;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_RPC_ERROR = 10;
}

enum GameReviewSharePlacement {
  GAME_REVIEW_SHARE_PLACEMENT_UNSPECIFIED = 0;
  GAME_REVIE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05306"></a>
## FND-05306: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason.GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_QUALIFYING_POSITION = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_QUALIFYING_POSITION = 9;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4152.

```text
ASON_NOT_LOGGED_IN = 7;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_USER_COLOR = 8;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_QUALIFYING_POSITION = 9;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_RPC_ERROR = 10;
}

enum GameReviewSharePlacement {
  GAME_REVIEW_SHARE_PLACEMENT_UNSPECIFIED = 0;
  GAME_REVIEW_SHARE_PLACEMENT_REPLACE_COG = 1;
  GAME_REVIEW_SHARE_PLACEMENT_BY_NEW_GA
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05307"></a>
## FND-05307: chesscom.game_review.v2.GameReviewCourseRecommendationSuppressionReason.GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_RPC_ERROR = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_RPC_ERROR = 10;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4235.

```text
SER_COLOR = 8;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_NO_QUALIFYING_POSITION = 9;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_RPC_ERROR = 10;
}

enum GameReviewSharePlacement {
  GAME_REVIEW_SHARE_PLACEMENT_UNSPECIFIED = 0;
  GAME_REVIEW_SHARE_PLACEMENT_REPLACE_COG = 1;
  GAME_REVIEW_SHARE_PLACEMENT_BY_NEW_GAME = 2;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_HEADER = 3;
  GAME_REVIEW_SHARE_PLACEME
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05308"></a>
## FND-05308: enum declaration: chesscom.game_review.v2.GameReviewSharePlacement

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameReviewSharePlacement {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4307.

```text
_QUALIFYING_POSITION = 9;
  GAME_REVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_RPC_ERROR = 10;
}

enum GameReviewSharePlacement {
  GAME_REVIEW_SHARE_PLACEMENT_UNSPECIFIED = 0;
  GAME_REVIEW_SHARE_PLACEMENT_REPLACE_COG = 1;
  GAME_REVIEW_SHARE_PLACEMENT_BY_NEW_GAME = 2;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_HEADER = 3;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_BOTTOM_BAR = 4;
  GAME_REVIEW_SHARE_PLACEMENT_COACH_BUBBLE = 5;
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05309"></a>
## FND-05309: chesscom.game_review.v2.GameReviewSharePlacement.GAME_REVIEW_SHARE_PLACEMENT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_SHARE_PLACEMENT_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4341.

```text
EVIEW_COURSE_RECOMMENDATION_SUPPRESSION_REASON_RPC_ERROR = 10;
}

enum GameReviewSharePlacement {
  GAME_REVIEW_SHARE_PLACEMENT_UNSPECIFIED = 0;
  GAME_REVIEW_SHARE_PLACEMENT_REPLACE_COG = 1;
  GAME_REVIEW_SHARE_PLACEMENT_BY_NEW_GAME = 2;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_HEADER = 3;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_BOTTOM_BAR = 4;
  GAME_REVIEW_SHARE_PLACEMENT_COACH_BUBBLE = 5;
}

enum GameReviewTakeawaysTrainC
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05310"></a>
## FND-05310: chesscom.game_review.v2.GameReviewSharePlacement.GAME_REVIEW_SHARE_PLACEMENT_REPLACE_COG = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_SHARE_PLACEMENT_REPLACE_COG = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4388.

```text
RPC_ERROR = 10;
}

enum GameReviewSharePlacement {
  GAME_REVIEW_SHARE_PLACEMENT_UNSPECIFIED = 0;
  GAME_REVIEW_SHARE_PLACEMENT_REPLACE_COG = 1;
  GAME_REVIEW_SHARE_PLACEMENT_BY_NEW_GAME = 2;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_HEADER = 3;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_BOTTOM_BAR = 4;
  GAME_REVIEW_SHARE_PLACEMENT_COACH_BUBBLE = 5;
}

enum GameReviewTakeawaysTrainCtaDestination {
  GAME_REVIEW_TAKEAWAYS_TRAIN_C
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05311"></a>
## FND-05311: chesscom.game_review.v2.GameReviewSharePlacement.GAME_REVIEW_SHARE_PLACEMENT_BY_NEW_GAME = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_SHARE_PLACEMENT_BY_NEW_GAME = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4435.

```text
t {
  GAME_REVIEW_SHARE_PLACEMENT_UNSPECIFIED = 0;
  GAME_REVIEW_SHARE_PLACEMENT_REPLACE_COG = 1;
  GAME_REVIEW_SHARE_PLACEMENT_BY_NEW_GAME = 2;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_HEADER = 3;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_BOTTOM_BAR = 4;
  GAME_REVIEW_SHARE_PLACEMENT_COACH_BUBBLE = 5;
}

enum GameReviewTakeawaysTrainCtaDestination {
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UNSPECIFIED = 0;
  GAME_REVIEW_T
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05312"></a>
## FND-05312: chesscom.game_review.v2.GameReviewSharePlacement.GAME_REVIEW_SHARE_PLACEMENT_MOVES_HEADER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_SHARE_PLACEMENT_MOVES_HEADER = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4482.

```text
 0;
  GAME_REVIEW_SHARE_PLACEMENT_REPLACE_COG = 1;
  GAME_REVIEW_SHARE_PLACEMENT_BY_NEW_GAME = 2;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_HEADER = 3;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_BOTTOM_BAR = 4;
  GAME_REVIEW_SHARE_PLACEMENT_COACH_BUBBLE = 5;
}

enum GameReviewTakeawaysTrainCtaDestination {
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UNSPECIFIED = 0;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_TRAIN = 1;
  GAM
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05313"></a>
## FND-05313: chesscom.game_review.v2.GameReviewSharePlacement.GAME_REVIEW_SHARE_PLACEMENT_MOVES_BOTTOM_BAR = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_SHARE_PLACEMENT_MOVES_BOTTOM_BAR = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4530.

```text
1;
  GAME_REVIEW_SHARE_PLACEMENT_BY_NEW_GAME = 2;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_HEADER = 3;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_BOTTOM_BAR = 4;
  GAME_REVIEW_SHARE_PLACEMENT_COACH_BUBBLE = 5;
}

enum GameReviewTakeawaysTrainCtaDestination {
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UNSPECIFIED = 0;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_TRAIN = 1;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UPGRADE
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05314"></a>
## FND-05314: chesscom.game_review.v2.GameReviewSharePlacement.GAME_REVIEW_SHARE_PLACEMENT_COACH_BUBBLE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_SHARE_PLACEMENT_COACH_BUBBLE = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4582.

```text
GAME_REVIEW_SHARE_PLACEMENT_MOVES_HEADER = 3;
  GAME_REVIEW_SHARE_PLACEMENT_MOVES_BOTTOM_BAR = 4;
  GAME_REVIEW_SHARE_PLACEMENT_COACH_BUBBLE = 5;
}

enum GameReviewTakeawaysTrainCtaDestination {
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UNSPECIFIED = 0;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_TRAIN = 1;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UPGRADE = 2;
}

enum GameReviewPremiumModalTrigger {
  GAME
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05315"></a>
## FND-05315: enum declaration: chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameReviewTakeawaysTrainCtaDestination {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4631.

```text
AME_REVIEW_SHARE_PLACEMENT_MOVES_BOTTOM_BAR = 4;
  GAME_REVIEW_SHARE_PLACEMENT_COACH_BUBBLE = 5;
}

enum GameReviewTakeawaysTrainCtaDestination {
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UNSPECIFIED = 0;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_TRAIN = 1;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UPGRADE = 2;
}

enum GameReviewPremiumModalTrigger {
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_UNSPECIFIED = 0;
  
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05316"></a>
## FND-05316: chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination.GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4679.

```text

  GAME_REVIEW_SHARE_PLACEMENT_COACH_BUBBLE = 5;
}

enum GameReviewTakeawaysTrainCtaDestination {
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UNSPECIFIED = 0;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_TRAIN = 1;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UPGRADE = 2;
}

enum GameReviewPremiumModalTrigger {
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_REVIEW_LIMIT =
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05317"></a>
## FND-05317: chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination.GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_TRAIN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_TRAIN = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4742.

```text
viewTakeawaysTrainCtaDestination {
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UNSPECIFIED = 0;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_TRAIN = 1;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UPGRADE = 2;
}

enum GameReviewPremiumModalTrigger {
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_REVIEW_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05318"></a>
## FND-05318: chesscom.game_review.v2.GameReviewTakeawaysTrainCtaDestination.GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UPGRADE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UPGRADE = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4799.

```text
S_TRAIN_CTA_DESTINATION_UNSPECIFIED = 0;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_TRAIN = 1;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UPGRADE = 2;
}

enum GameReviewPremiumModalTrigger {
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_REVIEW_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05319"></a>
## FND-05319: enum declaration: chesscom.game_review.v2.GameReviewPremiumModalTrigger

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum GameReviewPremiumModalTrigger {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4859.

```text
WAYS_TRAIN_CTA_DESTINATION_TRAIN = 1;
  GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UPGRADE = 2;
}

enum GameReviewPremiumModalTrigger {
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_REVIEW_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _gam
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05320"></a>
## FND-05320: chesscom.game_review.v2.GameReviewPremiumModalTrigger.GAME_REVIEW_PREMIUM_MODAL_TRIGGER_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_PREMIUM_MODAL_TRIGGER_UNSPECIFIED = 0;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4898.

```text
 GAME_REVIEW_TAKEAWAYS_TRAIN_CTA_DESTINATION_UPGRADE = 2;
}

enum GameReviewPremiumModalTrigger {
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_REVIEW_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  opti
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05321"></a>
## FND-05321: chesscom.game_review.v2.GameReviewPremiumModalTrigger.GAME_REVIEW_PREMIUM_MODAL_TRIGGER_REVIEW_LIMIT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_PREMIUM_MODAL_TRIGGER_REVIEW_LIMIT = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 4951.

```text
= 2;
}

enum GameReviewPremiumModalTrigger {
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_REVIEW_LIMIT = 1;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
}

message GameReviewStart {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _game_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05322"></a>
## FND-05322: chesscom.game_review.v2.GameReviewPremiumModalTrigger.GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

GAME_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5005.

```text
VIEW_PREMIUM_MODAL_TRIGGER_UNSPECIFIED = 0;
  GAME_REVIEW_PREMIUM_MODAL_TRIGGER_REVIEW_LIMIT = 1;
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
  optional .chesscom.game_review.v2.GameReviewSt
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05323"></a>
## FND-05323: message declaration: chesscom.game_review.v2.GameReviewStart

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewStart {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5063.

```text
PREMIUM_MODAL_TRIGGER_REVIEW_LIMIT = 1;
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
  optional .chesscom.proto_options.e
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05324"></a>
## FND-05324: oneof declaration: chesscom.game_review.v2.GameReviewStart._result

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

<a id="FND-05325"></a>
## FND-05325: chesscom.game_review.v2.GameReviewStart.result = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5109.

```text
_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
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
}

message GameRev
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05326"></a>
## FND-05326: oneof declaration: chesscom.game_review.v2.GameReviewStart._game_id

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

<a id="FND-05327"></a>
## FND-05327: chesscom.game_review.v2.GameReviewStart.game_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string game_id = 5;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5188.

```text

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
  .chesscom.game_review.v2.GameReview
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05328"></a>
## FND-05328: chesscom.game_review.v2.GameReviewStart.game_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5214.

```text
scom.game_review.v2.GameReviewResult result = 2;
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
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  o
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05329"></a>
## FND-05329: chesscom.game_review.v2.GameReviewStart.source = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewStartSource source = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5279.

```text
e_id {
  string game_id = 5;
  }
  optional .chesscom.ceac.v1.GameAnalysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;
}

message GameReviewPremiumModalOpened {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModal
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05330"></a>
## FND-05330: chesscom.game_review.v2.GameReviewStart.funnel = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.events.v1.Funnel funnel = 4;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5349.

```text
ysisGameType game_type = 1;
  optional .chesscom.game_review.v2.GameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;
}

message GameReviewPremiumModalOpened {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.Adva
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05331"></a>
## FND-05331: message declaration: chesscom.game_review.v2.GameReviewPremiumModalOpened

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewPremiumModalOpened {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5414.

```text
ameReviewStartSource source = 3;
  optional .chesscom.proto_options.events.v1.Funnel funnel = 4;
}

message GameReviewPremiumModalOpened {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.AdvancedStatType category = 3;
  }
}

message GameReviewPremiumModalC
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05332"></a>
## FND-05332: oneof declaration: chesscom.game_review.v2.GameReviewPremiumModalOpened._result

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

<a id="FND-05333"></a>
## FND-05333: chesscom.game_review.v2.GameReviewPremiumModalOpened.result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5473.

```text
_options.events.v1.Funnel funnel = 4;
}

message GameReviewPremiumModalOpened {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.AdvancedStatType category = 3;
  }
}

message GameReviewPremiumModalClosed {
  oneof _result {
  .chesscom.game_review.v2.GameRe
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05334"></a>
## FND-05334: oneof declaration: chesscom.game_review.v2.GameReviewPremiumModalOpened._trigger

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _trigger {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5533.

```text
remiumModalOpened {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.AdvancedStatType category = 3;
  }
}

message GameReviewPremiumModalClosed {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _trigger {
  .chesscom.ga
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05335"></a>
## FND-05335: chesscom.game_review.v2.GameReviewPremiumModalOpened.trigger = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5552.

```text

  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.AdvancedStatType category = 3;
  }
}

message GameReviewPremiumModalClosed {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameRe
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05336"></a>
## FND-05336: oneof declaration: chesscom.game_review.v2.GameReviewPremiumModalOpened._category

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _category {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5626.

```text

  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.AdvancedStatType category = 3;
  }
}

message GameReviewPremiumModalClosed {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 3;
  }
  optional .chesscom.game_review.
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05337"></a>
## FND-05337: chesscom.game_review.v2.GameReviewPremiumModalOpened.category = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.stats.v1.AdvancedStatType category = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5646.

```text
r {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.AdvancedStatType category = 3;
  }
}

message GameReviewPremiumModalClosed {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 3;
  }
  optional .chesscom.game_review.v2.GameReviewPremium
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05338"></a>
## FND-05338: message declaration: chesscom.game_review.v2.GameReviewPremiumModalClosed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewPremiumModalClosed {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5703.

```text
ger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.AdvancedStatType category = 3;
  }
}

message GameReviewPremiumModalClosed {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 3;
  }
  optional .chesscom.game_review.v2.GameReviewPremiumModalButton button_name = 1;
}

message GameReviewPremium
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05339"></a>
## FND-05339: oneof declaration: chesscom.game_review.v2.GameReviewPremiumModalClosed._result

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

<a id="FND-05340"></a>
## FND-05340: chesscom.game_review.v2.GameReviewPremiumModalClosed.result = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5109.

```text
_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
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
}

message GameRev
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05341"></a>
## FND-05341: oneof declaration: chesscom.game_review.v2.GameReviewPremiumModalClosed._trigger

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _trigger {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5533.

```text
remiumModalOpened {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.AdvancedStatType category = 3;
  }
}

message GameReviewPremiumModalClosed {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _trigger {
  .chesscom.ga
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05342"></a>
## FND-05342: chesscom.game_review.v2.GameReviewPremiumModalClosed.trigger = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5841.

```text

  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 3;
  }
  optional .chesscom.game_review.v2.GameReviewPremiumModalButton button_name = 1;
}

message GameReviewPremiumModalUpgradeClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_re
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05343"></a>
## FND-05343: chesscom.game_review.v2.GameReviewPremiumModalClosed.button_name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.game_review.v2.GameReviewPremiumModalButton button_name = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5915.

```text

  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 3;
  }
  optional .chesscom.game_review.v2.GameReviewPremiumModalButton button_name = 1;
}

message GameReviewPremiumModalUpgradeClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
}

message GameRevi
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05344"></a>
## FND-05344: message declaration: chesscom.game_review.v2.GameReviewPremiumModalUpgradeClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewPremiumModalUpgradeClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5998.

```text
igger = 3;
  }
  optional .chesscom.game_review.v2.GameReviewPremiumModalButton button_name = 1;
}

message GameReviewPremiumModalUpgradeClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
}

message GameReviewStartReviewClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResul
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05345"></a>
## FND-05345: oneof declaration: chesscom.game_review.v2.GameReviewPremiumModalUpgradeClicked._result

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

<a id="FND-05346"></a>
## FND-05346: chesscom.game_review.v2.GameReviewPremiumModalUpgradeClicked.result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5473.

```text
_options.events.v1.Funnel funnel = 4;
}

message GameReviewPremiumModalOpened {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.AdvancedStatType category = 3;
  }
}

message GameReviewPremiumModalClosed {
  oneof _result {
  .chesscom.game_review.v2.GameRe
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05347"></a>
## FND-05347: oneof declaration: chesscom.game_review.v2.GameReviewPremiumModalUpgradeClicked._trigger

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _trigger {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5533.

```text
remiumModalOpened {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.AdvancedStatType category = 3;
  }
}

message GameReviewPremiumModalClosed {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _trigger {
  .chesscom.ga
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05348"></a>
## FND-05348: chesscom.game_review.v2.GameReviewPremiumModalUpgradeClicked.trigger = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5552.

```text

  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.AdvancedStatType category = 3;
  }
}

message GameReviewPremiumModalClosed {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameRe
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05349"></a>
## FND-05349: message declaration: chesscom.game_review.v2.GameReviewStartReviewClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewStartReviewClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6219.

```text
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
}

message GameReviewStartReviewClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
}

message GameReviewOverviewScreenContinueReviewClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
}

message GameReviewSelfAnalysisClicked {
  oneof _game_review_sc
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05350"></a>
## FND-05350: oneof declaration: chesscom.game_review.v2.GameReviewStartReviewClicked._result

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

<a id="FND-05351"></a>
## FND-05351: chesscom.game_review.v2.GameReviewStartReviewClicked.result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5473.

```text
_options.events.v1.Funnel funnel = 4;
}

message GameReviewPremiumModalOpened {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.AdvancedStatType category = 3;
  }
}

message GameReviewPremiumModalClosed {
  oneof _result {
  .chesscom.game_review.v2.GameRe
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05352"></a>
## FND-05352: message declaration: chesscom.game_review.v2.GameReviewOverviewScreenContinueReviewClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewOverviewScreenContinueReviewClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6339.

```text
artReviewClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
}

message GameReviewOverviewScreenContinueReviewClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
}

message GameReviewSelfAnalysisClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _result {
  .chesscom.game_review
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05353"></a>
## FND-05353: oneof declaration: chesscom.game_review.v2.GameReviewOverviewScreenContinueReviewClicked._result

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

<a id="FND-05354"></a>
## FND-05354: chesscom.game_review.v2.GameReviewOverviewScreenContinueReviewClicked.result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5473.

```text
_options.events.v1.Funnel funnel = 4;
}

message GameReviewPremiumModalOpened {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
  oneof _trigger {
  .chesscom.game_review.v2.GameReviewPremiumModalTrigger trigger = 2;
  }
  oneof _category {
  .chesscom.stats.v1.AdvancedStatType category = 3;
  }
}

message GameReviewPremiumModalClosed {
  oneof _result {
  .chesscom.game_review.v2.GameRe
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05355"></a>
## FND-05355: message declaration: chesscom.game_review.v2.GameReviewSelfAnalysisClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewSelfAnalysisClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6476.

```text
nueReviewClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 1;
  }
}

message GameReviewSelfAnalysisClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional int32 percent_reviewed = 3;
}

message GameReviewOverviewScreenEvalGraphClicked {
  oneof
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05356"></a>
## FND-05356: oneof declaration: chesscom.game_review.v2.GameReviewSelfAnalysisClicked._game_review_screen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _game_review_screen {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6518.

```text
esscom.game_review.v2.GameReviewResult result = 1;
  }
}

message GameReviewSelfAnalysisClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional int32 percent_reviewed = 3;
}

message GameReviewOverviewScreenEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.Game
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05357"></a>
## FND-05357: chesscom.game_review.v2.GameReviewSelfAnalysisClicked.game_review_screen = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6548.

```text
ewResult result = 1;
  }
}

message GameReviewSelfAnalysisClicked {
  oneof _game_review_screen {
  .chesscom.game_review.v2.GameReviewScreen game_review_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional int32 percent_reviewed = 3;
}

message GameReviewOverviewScreenEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05358"></a>
## FND-05358: oneof declaration: chesscom.game_review.v2.GameReviewSelfAnalysisClicked._result

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

<a id="FND-05359"></a>
## FND-05359: chesscom.game_review.v2.GameReviewSelfAnalysisClicked.result = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5109.

```text
_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
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
}

message GameRev
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05360"></a>
## FND-05360: chesscom.game_review.v2.GameReviewSelfAnalysisClicked.percent_reviewed = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6698.

```text
iew_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional int32 percent_reviewed = 3;
}

message GameReviewOverviewScreenEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClas
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05361"></a>
## FND-05361: message declaration: chesscom.game_review.v2.GameReviewOverviewScreenEvalGraphClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewOverviewScreenEvalGraphClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6738.

```text
.chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional int32 percent_reviewed = 3;
}

message GameReviewOverviewScreenEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClassificationsExpandClicked {
  oneof _resu
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05362"></a>
## FND-05362: oneof declaration: chesscom.game_review.v2.GameReviewOverviewScreenEvalGraphClicked._result

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

<a id="FND-05363"></a>
## FND-05363: chesscom.game_review.v2.GameReviewOverviewScreenEvalGraphClicked.result = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5109.

```text
_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
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
}

message GameRev
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05364"></a>
## FND-05364: chesscom.game_review.v2.GameReviewOverviewScreenEvalGraphClicked.move_classification = 1

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

<a id="FND-05365"></a>
## FND-05365: chesscom.game_review.v2.GameReviewOverviewScreenEvalGraphClicked.percent_reviewed = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 percent_reviewed = 3;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6698.

```text
iew_screen = 1;
  }
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional int32 percent_reviewed = 3;
}

message GameReviewOverviewScreenEvalGraphClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional .chesscom.explanation_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClas
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05366"></a>
## FND-05366: message declaration: chesscom.game_review.v2.GameReviewClassificationsExpandClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewClassificationsExpandClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 6996.

```text
ion_engine.v1.MoveClassification move_classification = 1;
  optional int32 percent_reviewed = 3;
}

message GameReviewClassificationsExpandClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
  }
  optional bool is_expanded = 1;
}

message GameReviewMoveClassificationClicked {
  oneof _user_or_opponent_move {
  .chesscom.game_review.v2.UserOrOpponentMove user_or_opponent_move = 2;
  }
 
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05367"></a>
## FND-05367: oneof declaration: chesscom.game_review.v2.GameReviewClassificationsExpandClicked._result

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

<a id="FND-05368"></a>
## FND-05368: chesscom.game_review.v2.GameReviewClassificationsExpandClicked.result = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.game_review.v2.GameReviewResult result = 2;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 5109.

```text
_REVIEW_PREMIUM_MODAL_TRIGGER_TAKEAWAYS_TRAIN = 2;
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
}

message GameRev
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05369"></a>
## FND-05369: chesscom.game_review.v2.GameReviewClassificationsExpandClicked.is_expanded = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_expanded = 1;

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7125.

```text
ionsExpandClicked {
  oneof _result {
  .chesscom.game_review.v2.GameReviewResult result = 2;
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
  optional .chesscom.explanation_engine.v1.MoveClass
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-05370"></a>
## FND-05370: message declaration: chesscom.game_review.v2.GameReviewMoveClassificationClicked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewMoveClassificationClicked {

### Evidence

- **SRC-0454** `research/proto/chesscom/game_review/v2/user_activity.proto` — [preserved redacted evidence](../evidence/text/2e7f701f6d12ae5419c503c50fa197a7c50b9cc768855ecbd13173834c4a160d.proto)
  Character offset 7159.

```text
t {
  .chesscom.game_review.v2.GameReviewResult result = 2;
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
```

**Source references:** SRC-0454, SRC-1425  
**URL references:** None independently associated  
**Related findings:** FND-05227, FND-05228, FND-05229

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-05371"></a>
## FND-05371: oneof declaration: chesscom.game_review.v2.GameReviewMoveClassificationClicked._user_or_opponent_move

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

<a id="FND-05372"></a>
## FND-05372: chesscom.game_review.v2.GameReviewMoveClassificationClicked.user_or_opponent_move = 2

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

<a id="FND-05373"></a>
## FND-05373: oneof declaration: chesscom.game_review.v2.GameReviewMoveClassificationClicked._result

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

<a id="FND-05374"></a>
## FND-05374: chesscom.game_review.v2.GameReviewMoveClassificationClicked.result = 3

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
