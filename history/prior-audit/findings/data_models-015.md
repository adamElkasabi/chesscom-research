# data_models — findings 1401–1500

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-01675"></a>
## FND-01675: oneof declaration: chesscom.courses.v1.CourseChapter._user_video_position

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_video_position {

### Evidence

- **SRC-0267** `research/proto/chesscom/courses/v1/course_chapter.proto` — [preserved redacted evidence](../evidence/text/ee405a9161cc794693ce5b9505e13d025201dcfc1227ce009872e1022de0c742.proto)
  Character offset 201.

```text
message CourseChapter {
  oneof _video {
  .chesscom.courses_common.v1.CourseVideo video = 3;
  }
  oneof _user_video_position {
  int32 user_video_position = 4;
  }
  optional string id = 1;
  optional string name = 2;
}

```

**Source references:** SRC-0267, SRC-1238  
**URL references:** None independently associated  
**Related findings:** FND-01672, FND-01673, FND-01674

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01676"></a>
## FND-01676: chesscom.courses.v1.CourseChapter.user_video_position = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 user_video_position = 4;

### Evidence

- **SRC-0267** `research/proto/chesscom/courses/v1/course_chapter.proto` — [preserved redacted evidence](../evidence/text/ee405a9161cc794693ce5b9505e13d025201dcfc1227ce009872e1022de0c742.proto)
  Character offset 232.

```text
 _video {
  .chesscom.courses_common.v1.CourseVideo video = 3;
  }
  oneof _user_video_position {
  int32 user_video_position = 4;
  }
  optional string id = 1;
  optional string name = 2;
}

```

**Source references:** SRC-0267, SRC-1238  
**URL references:** None independently associated  
**Related findings:** FND-01672, FND-01673, FND-01674

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01677"></a>
## FND-01677: chesscom.courses.v1.CourseChapter.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0267** `research/proto/chesscom/courses/v1/course_chapter.proto` — [preserved redacted evidence](../evidence/text/ee405a9161cc794693ce5b9505e13d025201dcfc1227ce009872e1022de0c742.proto)
  Character offset 269.

```text
v1.CourseVideo video = 3;
  }
  oneof _user_video_position {
  int32 user_video_position = 4;
  }
  optional string id = 1;
  optional string name = 2;
}

```

**Source references:** SRC-0267, SRC-1238  
**URL references:** None independently associated  
**Related findings:** FND-01672, FND-01673, FND-01674

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01678"></a>
## FND-01678: chesscom.courses.v1.CourseChapter.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0267** `research/proto/chesscom/courses/v1/course_chapter.proto` — [preserved redacted evidence](../evidence/text/ee405a9161cc794693ce5b9505e13d025201dcfc1227ce009872e1022de0c742.proto)
  Character offset 295.

```text
  }
  oneof _user_video_position {
  int32 user_video_position = 4;
  }
  optional string id = 1;
  optional string name = 2;
}

```

**Source references:** SRC-0267, SRC-1238  
**URL references:** None independently associated  
**Related findings:** FND-01672, FND-01673, FND-01674

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01679"></a>
## FND-01679: message declaration: chesscom.courses.v1.CourseChapterDetails

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseChapterDetails {

### Evidence

- **SRC-0268** `research/proto/chesscom/courses/v1/course_chapter_details.proto` — [preserved redacted evidence](../evidence/text/d60dcb5704ee0c107eddce374b3913668e3b4b2a70a57de393cc0b2468f9387e.proto)
  Character offset 109.

```text
: chesscom/courses/v1/course_chapter_details.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseChapterDetails {
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses_common.v1.CourseChapterStats stats = 3;
}

```

**Source references:** SRC-0268, SRC-1239  
**URL references:** None independently associated  
**Related findings:** FND-01680, FND-01681

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01680"></a>
## FND-01680: chesscom.courses.v1.CourseChapterDetails.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0268** `research/proto/chesscom/courses/v1/course_chapter_details.proto` — [preserved redacted evidence](../evidence/text/d60dcb5704ee0c107eddce374b3913668e3b4b2a70a57de393cc0b2468f9387e.proto)
  Character offset 142.

```text
ter_details.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseChapterDetails {
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses_common.v1.CourseChapterStats stats = 3;
}

```

**Source references:** SRC-0268, SRC-1239  
**URL references:** None independently associated  
**Related findings:** FND-01679, FND-01681

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01681"></a>
## FND-01681: chesscom.courses.v1.CourseChapterDetails.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0268** `research/proto/chesscom/courses/v1/course_chapter_details.proto` — [preserved redacted evidence](../evidence/text/d60dcb5704ee0c107eddce374b3913668e3b4b2a70a57de393cc0b2468f9387e.proto)
  Character offset 168.

```text
x: proto3

package chesscom.courses.v1;

message CourseChapterDetails {
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses_common.v1.CourseChapterStats stats = 3;
}

```

**Source references:** SRC-0268, SRC-1239  
**URL references:** None independently associated  
**Related findings:** FND-01679, FND-01680

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01682"></a>
## FND-01682: chesscom.courses.v1.CourseChapterDetails.stats = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseChapterStats stats = 3;

### Evidence

- **SRC-0268** `research/proto/chesscom/courses/v1/course_chapter_details.proto` — [preserved redacted evidence](../evidence/text/d60dcb5704ee0c107eddce374b3913668e3b4b2a70a57de393cc0b2468f9387e.proto)
  Character offset 196.

```text
courses.v1;

message CourseChapterDetails {
  optional string id = 1;
  optional string name = 2;
  optional .chesscom.courses_common.v1.CourseChapterStats stats = 3;
}

```

**Source references:** SRC-0268, SRC-1239  
**URL references:** None independently associated  
**Related findings:** FND-01679, FND-01680, FND-01681

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01683"></a>
## FND-01683: message declaration: chesscom.courses.v1.CourseCoach

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseCoach {

### Evidence

- **SRC-0269** `research/proto/chesscom/courses/v1/course_coach.proto` — [preserved redacted evidence](../evidence/text/50d02d5f3a736d7e7be974fe7947e352982f236d7c49a9514b49ce34a63e95a8.proto)
  Character offset 99.

```text
// source: chesscom/courses/v1/course_coach.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseCoach {
  optional .chesscom.courses_common.v1.CourseCoachAvatar avatar = 1;
}

```

**Source references:** SRC-0269, SRC-1240  
**URL references:** None independently associated  
**Related findings:** FND-01684

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01684"></a>
## FND-01684: chesscom.courses.v1.CourseCoach.avatar = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.courses_common.v1.CourseCoachAvatar avatar = 1;

### Evidence

- **SRC-0269** `research/proto/chesscom/courses/v1/course_coach.proto` — [preserved redacted evidence](../evidence/text/50d02d5f3a736d7e7be974fe7947e352982f236d7c49a9514b49ce34a63e95a8.proto)
  Character offset 123.

```text
rses/v1/course_coach.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseCoach {
  optional .chesscom.courses_common.v1.CourseCoachAvatar avatar = 1;
}

```

**Source references:** SRC-0269, SRC-1240  
**URL references:** None independently associated  
**Related findings:** FND-01683

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01685"></a>
## FND-01685: message declaration: chesscom.courses.v1.CourseCoachComment

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseCoachComment {

### Evidence

- **SRC-0270** `research/proto/chesscom/courses/v1/course_coach_comment.proto` — [preserved redacted evidence](../evidence/text/4c95f7117a278fed8373ac20653634dfa2bca25356663e27eb869a15567315dd.proto)
  Character offset 107.

```text
ce: chesscom/courses/v1/course_coach_comment.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseCoachComment {
  oneof _speech {
  .chesscom.courses.v1.CourseCoachSpeechItem speech = 2;
  }
  optional string text = 1;
}

```

**Source references:** SRC-0270, SRC-1241  
**URL references:** None independently associated  
**Related findings:** FND-01686, FND-01687

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01686"></a>
## FND-01686: oneof declaration: chesscom.courses.v1.CourseCoachComment._speech

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _speech {

### Evidence

- **SRC-0270** `research/proto/chesscom/courses/v1/course_coach_comment.proto` — [preserved redacted evidence](../evidence/text/4c95f7117a278fed8373ac20653634dfa2bca25356663e27eb869a15567315dd.proto)
  Character offset 138.

```text
coach_comment.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseCoachComment {
  oneof _speech {
  .chesscom.courses.v1.CourseCoachSpeechItem speech = 2;
  }
  optional string text = 1;
}

```

**Source references:** SRC-0270, SRC-1241  
**URL references:** None independently associated  
**Related findings:** FND-01685, FND-01687

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01687"></a>
## FND-01687: chesscom.courses.v1.CourseCoachComment.speech = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseCoachSpeechItem speech = 2;

### Evidence

- **SRC-0270** `research/proto/chesscom/courses/v1/course_coach_comment.proto` — [preserved redacted evidence](../evidence/text/4c95f7117a278fed8373ac20653634dfa2bca25356663e27eb869a15567315dd.proto)
  Character offset 156.

```text
o
// syntax: proto3

package chesscom.courses.v1;

message CourseCoachComment {
  oneof _speech {
  .chesscom.courses.v1.CourseCoachSpeechItem speech = 2;
  }
  optional string text = 1;
}

```

**Source references:** SRC-0270, SRC-1241  
**URL references:** None independently associated  
**Related findings:** FND-01685, FND-01686

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01688"></a>
## FND-01688: chesscom.courses.v1.CourseCoachComment.text = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string text = 1;

### Evidence

- **SRC-0270** `research/proto/chesscom/courses/v1/course_coach_comment.proto` — [preserved redacted evidence](../evidence/text/4c95f7117a278fed8373ac20653634dfa2bca25356663e27eb869a15567315dd.proto)
  Character offset 217.

```text
urseCoachComment {
  oneof _speech {
  .chesscom.courses.v1.CourseCoachSpeechItem speech = 2;
  }
  optional string text = 1;
}

```

**Source references:** SRC-0270, SRC-1241  
**URL references:** None independently associated  
**Related findings:** FND-01685, FND-01686, FND-01687

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01689"></a>
## FND-01689: message declaration: chesscom.courses.v1.CourseCoachSpeech

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseCoachSpeech {

### Evidence

- **SRC-0271** `research/proto/chesscom/courses/v1/course_coach_speech.proto` — [preserved redacted evidence](../evidence/text/16b4ec270930969ee7124a49b4fb58366ed89b1f1d05bca88928e02d9e9bb45f.proto)
  Character offset 106.

```text
rce: chesscom/courses/v1/course_coach_speech.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseCoachSpeech {
  oneof _intro {
  .chesscom.courses.v1.CourseCoachSpeechItem intro = 1;
  }
  oneof _main {
  .chesscom.courses.v1.CourseCoachSpeechItem main = 2;
  }
  repeated .chesscom.courses.v1.CourseCoachSpeechItem subvariation_items = 3;
}

message CourseCoachSpeechItem {
  oneof _san {
  string san
```

**Source references:** SRC-0271, SRC-1242  
**URL references:** None independently associated  
**Related findings:** FND-01690, FND-01691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01690"></a>
## FND-01690: oneof declaration: chesscom.courses.v1.CourseCoachSpeech._intro

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _intro {

### Evidence

- **SRC-0271** `research/proto/chesscom/courses/v1/course_coach_speech.proto` — [preserved redacted evidence](../evidence/text/16b4ec270930969ee7124a49b4fb58366ed89b1f1d05bca88928e02d9e9bb45f.proto)
  Character offset 136.

```text
e_coach_speech.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseCoachSpeech {
  oneof _intro {
  .chesscom.courses.v1.CourseCoachSpeechItem intro = 1;
  }
  oneof _main {
  .chesscom.courses.v1.CourseCoachSpeechItem main = 2;
  }
  repeated .chesscom.courses.v1.CourseCoachSpeechItem subvariation_items = 3;
}

message CourseCoachSpeechItem {
  oneof _san {
  string san = 3;
  }
  optional string te
```

**Source references:** SRC-0271, SRC-1242  
**URL references:** None independently associated  
**Related findings:** FND-01689, FND-01691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01691"></a>
## FND-01691: chesscom.courses.v1.CourseCoachSpeech.intro = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseCoachSpeechItem intro = 1;

### Evidence

- **SRC-0271** `research/proto/chesscom/courses/v1/course_coach_speech.proto` — [preserved redacted evidence](../evidence/text/16b4ec270930969ee7124a49b4fb58366ed89b1f1d05bca88928e02d9e9bb45f.proto)
  Character offset 153.

```text
oto
// syntax: proto3

package chesscom.courses.v1;

message CourseCoachSpeech {
  oneof _intro {
  .chesscom.courses.v1.CourseCoachSpeechItem intro = 1;
  }
  oneof _main {
  .chesscom.courses.v1.CourseCoachSpeechItem main = 2;
  }
  repeated .chesscom.courses.v1.CourseCoachSpeechItem subvariation_items = 3;
}

message CourseCoachSpeechItem {
  oneof _san {
  string san = 3;
  }
  optional string text_item_id = 1;
 
```

**Source references:** SRC-0271, SRC-1242  
**URL references:** None independently associated  
**Related findings:** FND-01689, FND-01690

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01692"></a>
## FND-01692: oneof declaration: chesscom.courses.v1.CourseCoachSpeech._main

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _main {

### Evidence

- **SRC-0271** `research/proto/chesscom/courses/v1/course_coach_speech.proto` — [preserved redacted evidence](../evidence/text/16b4ec270930969ee7124a49b4fb58366ed89b1f1d05bca88928e02d9e9bb45f.proto)
  Character offset 213.

```text
 CourseCoachSpeech {
  oneof _intro {
  .chesscom.courses.v1.CourseCoachSpeechItem intro = 1;
  }
  oneof _main {
  .chesscom.courses.v1.CourseCoachSpeechItem main = 2;
  }
  repeated .chesscom.courses.v1.CourseCoachSpeechItem subvariation_items = 3;
}

message CourseCoachSpeechItem {
  oneof _san {
  string san = 3;
  }
  optional string text_item_id = 1;
  optional string audio_url_hash = 2;
}

```

**Source references:** SRC-0271, SRC-1242  
**URL references:** None independently associated  
**Related findings:** FND-01689, FND-01690, FND-01691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01693"></a>
## FND-01693: chesscom.courses.v1.CourseCoachSpeech.main = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseCoachSpeechItem main = 2;

### Evidence

- **SRC-0271** `research/proto/chesscom/courses/v1/course_coach_speech.proto` — [preserved redacted evidence](../evidence/text/16b4ec270930969ee7124a49b4fb58366ed89b1f1d05bca88928e02d9e9bb45f.proto)
  Character offset 229.

```text
ch {
  oneof _intro {
  .chesscom.courses.v1.CourseCoachSpeechItem intro = 1;
  }
  oneof _main {
  .chesscom.courses.v1.CourseCoachSpeechItem main = 2;
  }
  repeated .chesscom.courses.v1.CourseCoachSpeechItem subvariation_items = 3;
}

message CourseCoachSpeechItem {
  oneof _san {
  string san = 3;
  }
  optional string text_item_id = 1;
  optional string audio_url_hash = 2;
}

```

**Source references:** SRC-0271, SRC-1242  
**URL references:** None independently associated  
**Related findings:** FND-01689, FND-01690, FND-01691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01694"></a>
## FND-01694: chesscom.courses.v1.CourseCoachSpeech.subvariation_items = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseCoachSpeechItem subvariation_items = 3;

### Evidence

- **SRC-0271** `research/proto/chesscom/courses/v1/course_coach_speech.proto` — [preserved redacted evidence](../evidence/text/16b4ec270930969ee7124a49b4fb58366ed89b1f1d05bca88928e02d9e9bb45f.proto)
  Character offset 288.

```text
echItem intro = 1;
  }
  oneof _main {
  .chesscom.courses.v1.CourseCoachSpeechItem main = 2;
  }
  repeated .chesscom.courses.v1.CourseCoachSpeechItem subvariation_items = 3;
}

message CourseCoachSpeechItem {
  oneof _san {
  string san = 3;
  }
  optional string text_item_id = 1;
  optional string audio_url_hash = 2;
}

```

**Source references:** SRC-0271, SRC-1242  
**URL references:** None independently associated  
**Related findings:** FND-01689, FND-01690, FND-01691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01695"></a>
## FND-01695: message declaration: chesscom.courses.v1.CourseCoachSpeechItem

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseCoachSpeechItem {

### Evidence

- **SRC-0271** `research/proto/chesscom/courses/v1/course_coach_speech.proto` — [preserved redacted evidence](../evidence/text/16b4ec270930969ee7124a49b4fb58366ed89b1f1d05bca88928e02d9e9bb45f.proto)
  Character offset 367.

```text
Item main = 2;
  }
  repeated .chesscom.courses.v1.CourseCoachSpeechItem subvariation_items = 3;
}

message CourseCoachSpeechItem {
  oneof _san {
  string san = 3;
  }
  optional string text_item_id = 1;
  optional string audio_url_hash = 2;
}

```

**Source references:** SRC-0271, SRC-1242  
**URL references:** None independently associated  
**Related findings:** FND-01689, FND-01690, FND-01691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01696"></a>
## FND-01696: oneof declaration: chesscom.courses.v1.CourseCoachSpeechItem._san

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _san {

### Evidence

- **SRC-0271** `research/proto/chesscom/courses/v1/course_coach_speech.proto` — [preserved redacted evidence](../evidence/text/16b4ec270930969ee7124a49b4fb58366ed89b1f1d05bca88928e02d9e9bb45f.proto)
  Character offset 401.

```text
sscom.courses.v1.CourseCoachSpeechItem subvariation_items = 3;
}

message CourseCoachSpeechItem {
  oneof _san {
  string san = 3;
  }
  optional string text_item_id = 1;
  optional string audio_url_hash = 2;
}

```

**Source references:** SRC-0271, SRC-1242  
**URL references:** None independently associated  
**Related findings:** FND-01689, FND-01690, FND-01691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01697"></a>
## FND-01697: chesscom.courses.v1.CourseCoachSpeechItem.san = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string san = 3;

### Evidence

- **SRC-0271** `research/proto/chesscom/courses/v1/course_coach_speech.proto` — [preserved redacted evidence](../evidence/text/16b4ec270930969ee7124a49b4fb58366ed89b1f1d05bca88928e02d9e9bb45f.proto)
  Character offset 416.

```text
1.CourseCoachSpeechItem subvariation_items = 3;
}

message CourseCoachSpeechItem {
  oneof _san {
  string san = 3;
  }
  optional string text_item_id = 1;
  optional string audio_url_hash = 2;
}

```

**Source references:** SRC-0271, SRC-1242  
**URL references:** None independently associated  
**Related findings:** FND-01689, FND-01690, FND-01691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01698"></a>
## FND-01698: chesscom.courses.v1.CourseCoachSpeechItem.text_item_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string text_item_id = 1;

### Evidence

- **SRC-0271** `research/proto/chesscom/courses/v1/course_coach_speech.proto` — [preserved redacted evidence](../evidence/text/16b4ec270930969ee7124a49b4fb58366ed89b1f1d05bca88928e02d9e9bb45f.proto)
  Character offset 438.

```text
m subvariation_items = 3;
}

message CourseCoachSpeechItem {
  oneof _san {
  string san = 3;
  }
  optional string text_item_id = 1;
  optional string audio_url_hash = 2;
}

```

**Source references:** SRC-0271, SRC-1242  
**URL references:** None independently associated  
**Related findings:** FND-01689, FND-01690, FND-01691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01699"></a>
## FND-01699: chesscom.courses.v1.CourseCoachSpeechItem.audio_url_hash = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string audio_url_hash = 2;

### Evidence

- **SRC-0271** `research/proto/chesscom/courses/v1/course_coach_speech.proto` — [preserved redacted evidence](../evidence/text/16b4ec270930969ee7124a49b4fb58366ed89b1f1d05bca88928e02d9e9bb45f.proto)
  Character offset 474.

```text
 CourseCoachSpeechItem {
  oneof _san {
  string san = 3;
  }
  optional string text_item_id = 1;
  optional string audio_url_hash = 2;
}

```

**Source references:** SRC-0271, SRC-1242  
**URL references:** None independently associated  
**Related findings:** FND-01689, FND-01690, FND-01691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01700"></a>
## FND-01700: enum declaration: chesscom.courses.v1.CourseLearnType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseLearnType {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 107.

```text
ce: chesscom/courses/v1/course_configuration.proto
// syntax: proto3

package chesscom.courses.v1;

enum CourseLearnType {
  COURSE_LEARN_TYPE_UNSPECIFIED = 0;
  COURSE_LEARN_TYPE_ALL = 1;
  COURSE_LEARN_TYPE_KEY = 2;
}

enum CourseConsumptionMode {
  COURSE_CONSUMPTION_MODE_UNSPECIFIED = 0;
  COURSE_CONSUMPTION_MODE_LEARN = 1;
  COURSE_CONSUMPTION_MODE_READ = 2;
  COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH = 3;
}


```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01701"></a>
## FND-01701: chesscom.courses.v1.CourseLearnType.COURSE_LEARN_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_LEARN_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 132.

```text
ourse_configuration.proto
// syntax: proto3

package chesscom.courses.v1;

enum CourseLearnType {
  COURSE_LEARN_TYPE_UNSPECIFIED = 0;
  COURSE_LEARN_TYPE_ALL = 1;
  COURSE_LEARN_TYPE_KEY = 2;
}

enum CourseConsumptionMode {
  COURSE_CONSUMPTION_MODE_UNSPECIFIED = 0;
  COURSE_CONSUMPTION_MODE_LEARN = 1;
  COURSE_CONSUMPTION_MODE_READ = 2;
  COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH = 3;
}

enum CourseReviewType {
 
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01702"></a>
## FND-01702: chesscom.courses.v1.CourseLearnType.COURSE_LEARN_TYPE_ALL = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_LEARN_TYPE_ALL = 1;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 169.

```text
proto3

package chesscom.courses.v1;

enum CourseLearnType {
  COURSE_LEARN_TYPE_UNSPECIFIED = 0;
  COURSE_LEARN_TYPE_ALL = 1;
  COURSE_LEARN_TYPE_KEY = 2;
}

enum CourseConsumptionMode {
  COURSE_CONSUMPTION_MODE_UNSPECIFIED = 0;
  COURSE_CONSUMPTION_MODE_LEARN = 1;
  COURSE_CONSUMPTION_MODE_READ = 2;
  COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH = 3;
}

enum CourseReviewType {
  COURSE_REVIEW_TYPE_UNSPECIFIED = 0;

```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01703"></a>
## FND-01703: chesscom.courses.v1.CourseLearnType.COURSE_LEARN_TYPE_KEY = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_LEARN_TYPE_KEY = 2;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 198.

```text
ses.v1;

enum CourseLearnType {
  COURSE_LEARN_TYPE_UNSPECIFIED = 0;
  COURSE_LEARN_TYPE_ALL = 1;
  COURSE_LEARN_TYPE_KEY = 2;
}

enum CourseConsumptionMode {
  COURSE_CONSUMPTION_MODE_UNSPECIFIED = 0;
  COURSE_CONSUMPTION_MODE_LEARN = 1;
  COURSE_CONSUMPTION_MODE_READ = 2;
  COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH = 3;
}

enum CourseReviewType {
  COURSE_REVIEW_TYPE_UNSPECIFIED = 0;
  COURSE_REVIEW_TYPE_LEARNED_
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01704"></a>
## FND-01704: enum declaration: chesscom.courses.v1.CourseConsumptionMode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseConsumptionMode {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 228.

```text
{
  COURSE_LEARN_TYPE_UNSPECIFIED = 0;
  COURSE_LEARN_TYPE_ALL = 1;
  COURSE_LEARN_TYPE_KEY = 2;
}

enum CourseConsumptionMode {
  COURSE_CONSUMPTION_MODE_UNSPECIFIED = 0;
  COURSE_CONSUMPTION_MODE_LEARN = 1;
  COURSE_CONSUMPTION_MODE_READ = 2;
  COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH = 3;
}

enum CourseReviewType {
  COURSE_REVIEW_TYPE_UNSPECIFIED = 0;
  COURSE_REVIEW_TYPE_LEARNED_ORDER = 1;
  COURSE_REVIEW_TYP
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01705"></a>
## FND-01705: chesscom.courses.v1.CourseConsumptionMode.COURSE_CONSUMPTION_MODE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_CONSUMPTION_MODE_UNSPECIFIED = 0;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 259.

```text
ED = 0;
  COURSE_LEARN_TYPE_ALL = 1;
  COURSE_LEARN_TYPE_KEY = 2;
}

enum CourseConsumptionMode {
  COURSE_CONSUMPTION_MODE_UNSPECIFIED = 0;
  COURSE_CONSUMPTION_MODE_LEARN = 1;
  COURSE_CONSUMPTION_MODE_READ = 2;
  COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH = 3;
}

enum CourseReviewType {
  COURSE_REVIEW_TYPE_UNSPECIFIED = 0;
  COURSE_REVIEW_TYPE_LEARNED_ORDER = 1;
  COURSE_REVIEW_TYPE_RANDOM_ORDER = 2;
  COURSE_RE
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01706"></a>
## FND-01706: chesscom.courses.v1.CourseConsumptionMode.COURSE_CONSUMPTION_MODE_LEARN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_CONSUMPTION_MODE_LEARN = 1;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 302.

```text
SE_LEARN_TYPE_KEY = 2;
}

enum CourseConsumptionMode {
  COURSE_CONSUMPTION_MODE_UNSPECIFIED = 0;
  COURSE_CONSUMPTION_MODE_LEARN = 1;
  COURSE_CONSUMPTION_MODE_READ = 2;
  COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH = 3;
}

enum CourseReviewType {
  COURSE_REVIEW_TYPE_UNSPECIFIED = 0;
  COURSE_REVIEW_TYPE_LEARNED_ORDER = 1;
  COURSE_REVIEW_TYPE_RANDOM_ORDER = 2;
  COURSE_REVIEW_TYPE_MOVE_TRAINER_ORDER = 3;
}

enum C
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01707"></a>
## FND-01707: chesscom.courses.v1.CourseConsumptionMode.COURSE_CONSUMPTION_MODE_READ = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_CONSUMPTION_MODE_READ = 2;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 339.

```text
ConsumptionMode {
  COURSE_CONSUMPTION_MODE_UNSPECIFIED = 0;
  COURSE_CONSUMPTION_MODE_LEARN = 1;
  COURSE_CONSUMPTION_MODE_READ = 2;
  COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH = 3;
}

enum CourseReviewType {
  COURSE_REVIEW_TYPE_UNSPECIFIED = 0;
  COURSE_REVIEW_TYPE_LEARNED_ORDER = 1;
  COURSE_REVIEW_TYPE_RANDOM_ORDER = 2;
  COURSE_REVIEW_TYPE_MOVE_TRAINER_ORDER = 3;
}

enum CourseScheduleType {
  COURSE_SCHEDULE
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01708"></a>
## FND-01708: chesscom.courses.v1.CourseConsumptionMode.COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH = 3;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 375.

```text
ON_MODE_UNSPECIFIED = 0;
  COURSE_CONSUMPTION_MODE_LEARN = 1;
  COURSE_CONSUMPTION_MODE_READ = 2;
  COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH = 3;
}

enum CourseReviewType {
  COURSE_REVIEW_TYPE_UNSPECIFIED = 0;
  COURSE_REVIEW_TYPE_LEARNED_ORDER = 1;
  COURSE_REVIEW_TYPE_RANDOM_ORDER = 2;
  COURSE_REVIEW_TYPE_MOVE_TRAINER_ORDER = 3;
}

enum CourseScheduleType {
  COURSE_SCHEDULE_TYPE_UNSPECIFIED = 0;
  COURSE_SCHE
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01709"></a>
## FND-01709: enum declaration: chesscom.courses.v1.CourseReviewType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseReviewType {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 427.

```text
EARN = 1;
  COURSE_CONSUMPTION_MODE_READ = 2;
  COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH = 3;
}

enum CourseReviewType {
  COURSE_REVIEW_TYPE_UNSPECIFIED = 0;
  COURSE_REVIEW_TYPE_LEARNED_ORDER = 1;
  COURSE_REVIEW_TYPE_RANDOM_ORDER = 2;
  COURSE_REVIEW_TYPE_MOVE_TRAINER_ORDER = 3;
}

enum CourseScheduleType {
  COURSE_SCHEDULE_TYPE_UNSPECIFIED = 0;
  COURSE_SCHEDULE_TYPE_SPACED_REPETITION = 1;
  COURSE_SCHEDULE_T
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01710"></a>
## FND-01710: chesscom.courses.v1.CourseReviewType.COURSE_REVIEW_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_REVIEW_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 453.

```text
TION_MODE_READ = 2;
  COURSE_CONSUMPTION_MODE_LEARN_WITHOUT_COACH = 3;
}

enum CourseReviewType {
  COURSE_REVIEW_TYPE_UNSPECIFIED = 0;
  COURSE_REVIEW_TYPE_LEARNED_ORDER = 1;
  COURSE_REVIEW_TYPE_RANDOM_ORDER = 2;
  COURSE_REVIEW_TYPE_MOVE_TRAINER_ORDER = 3;
}

enum CourseScheduleType {
  COURSE_SCHEDULE_TYPE_UNSPECIFIED = 0;
  COURSE_SCHEDULE_TYPE_SPACED_REPETITION = 1;
  COURSE_SCHEDULE_TYPE_CYCLICAL = 2;
  COURSE
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01711"></a>
## FND-01711: chesscom.courses.v1.CourseReviewType.COURSE_REVIEW_TYPE_LEARNED_ORDER = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_REVIEW_TYPE_LEARNED_ORDER = 1;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 491.

```text
ON_MODE_LEARN_WITHOUT_COACH = 3;
}

enum CourseReviewType {
  COURSE_REVIEW_TYPE_UNSPECIFIED = 0;
  COURSE_REVIEW_TYPE_LEARNED_ORDER = 1;
  COURSE_REVIEW_TYPE_RANDOM_ORDER = 2;
  COURSE_REVIEW_TYPE_MOVE_TRAINER_ORDER = 3;
}

enum CourseScheduleType {
  COURSE_SCHEDULE_TYPE_UNSPECIFIED = 0;
  COURSE_SCHEDULE_TYPE_SPACED_REPETITION = 1;
  COURSE_SCHEDULE_TYPE_CYCLICAL = 2;
  COURSE_SCHEDULE_TYPE_CUSTOM = 3;
}

enum Cou
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01712"></a>
## FND-01712: chesscom.courses.v1.CourseReviewType.COURSE_REVIEW_TYPE_RANDOM_ORDER = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_REVIEW_TYPE_RANDOM_ORDER = 2;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 531.

```text
 CourseReviewType {
  COURSE_REVIEW_TYPE_UNSPECIFIED = 0;
  COURSE_REVIEW_TYPE_LEARNED_ORDER = 1;
  COURSE_REVIEW_TYPE_RANDOM_ORDER = 2;
  COURSE_REVIEW_TYPE_MOVE_TRAINER_ORDER = 3;
}

enum CourseScheduleType {
  COURSE_SCHEDULE_TYPE_UNSPECIFIED = 0;
  COURSE_SCHEDULE_TYPE_SPACED_REPETITION = 1;
  COURSE_SCHEDULE_TYPE_CYCLICAL = 2;
  COURSE_SCHEDULE_TYPE_CUSTOM = 3;
}

enum CourseReviewFailedBehavior {
  COURSE_REVIE
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01713"></a>
## FND-01713: chesscom.courses.v1.CourseReviewType.COURSE_REVIEW_TYPE_MOVE_TRAINER_ORDER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_REVIEW_TYPE_MOVE_TRAINER_ORDER = 3;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 570.

```text
E_UNSPECIFIED = 0;
  COURSE_REVIEW_TYPE_LEARNED_ORDER = 1;
  COURSE_REVIEW_TYPE_RANDOM_ORDER = 2;
  COURSE_REVIEW_TYPE_MOVE_TRAINER_ORDER = 3;
}

enum CourseScheduleType {
  COURSE_SCHEDULE_TYPE_UNSPECIFIED = 0;
  COURSE_SCHEDULE_TYPE_SPACED_REPETITION = 1;
  COURSE_SCHEDULE_TYPE_CYCLICAL = 2;
  COURSE_SCHEDULE_TYPE_CUSTOM = 3;
}

enum CourseReviewFailedBehavior {
  COURSE_REVIEW_FAILED_BEHAVIOR_UNSPECIFIED = 0;
  CO
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01714"></a>
## FND-01714: enum declaration: chesscom.courses.v1.CourseScheduleType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseScheduleType {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 616.

```text
D_ORDER = 1;
  COURSE_REVIEW_TYPE_RANDOM_ORDER = 2;
  COURSE_REVIEW_TYPE_MOVE_TRAINER_ORDER = 3;
}

enum CourseScheduleType {
  COURSE_SCHEDULE_TYPE_UNSPECIFIED = 0;
  COURSE_SCHEDULE_TYPE_SPACED_REPETITION = 1;
  COURSE_SCHEDULE_TYPE_CYCLICAL = 2;
  COURSE_SCHEDULE_TYPE_CUSTOM = 3;
}

enum CourseReviewFailedBehavior {
  COURSE_REVIEW_FAILED_BEHAVIOR_UNSPECIFIED = 0;
  COURSE_REVIEW_FAILED_BEHAVIOR_MOVE_TO_NEXT_CYCLE
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01715"></a>
## FND-01715: chesscom.courses.v1.CourseScheduleType.COURSE_SCHEDULE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_SCHEDULE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 644.

```text
_TYPE_RANDOM_ORDER = 2;
  COURSE_REVIEW_TYPE_MOVE_TRAINER_ORDER = 3;
}

enum CourseScheduleType {
  COURSE_SCHEDULE_TYPE_UNSPECIFIED = 0;
  COURSE_SCHEDULE_TYPE_SPACED_REPETITION = 1;
  COURSE_SCHEDULE_TYPE_CYCLICAL = 2;
  COURSE_SCHEDULE_TYPE_CUSTOM = 3;
}

enum CourseReviewFailedBehavior {
  COURSE_REVIEW_FAILED_BEHAVIOR_UNSPECIFIED = 0;
  COURSE_REVIEW_FAILED_BEHAVIOR_MOVE_TO_NEXT_CYCLE = 1;
  COURSE_REVIEW_FAILED
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01716"></a>
## FND-01716: chesscom.courses.v1.CourseScheduleType.COURSE_SCHEDULE_TYPE_SPACED_REPETITION = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_SCHEDULE_TYPE_SPACED_REPETITION = 1;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 684.

```text
TYPE_MOVE_TRAINER_ORDER = 3;
}

enum CourseScheduleType {
  COURSE_SCHEDULE_TYPE_UNSPECIFIED = 0;
  COURSE_SCHEDULE_TYPE_SPACED_REPETITION = 1;
  COURSE_SCHEDULE_TYPE_CYCLICAL = 2;
  COURSE_SCHEDULE_TYPE_CUSTOM = 3;
}

enum CourseReviewFailedBehavior {
  COURSE_REVIEW_FAILED_BEHAVIOR_UNSPECIFIED = 0;
  COURSE_REVIEW_FAILED_BEHAVIOR_MOVE_TO_NEXT_CYCLE = 1;
  COURSE_REVIEW_FAILED_BEHAVIOR_REPEAT_CURRENT_CYCLE = 2;
  CO
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01717"></a>
## FND-01717: chesscom.courses.v1.CourseScheduleType.COURSE_SCHEDULE_TYPE_CYCLICAL = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_SCHEDULE_TYPE_CYCLICAL = 2;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 730.

```text
eduleType {
  COURSE_SCHEDULE_TYPE_UNSPECIFIED = 0;
  COURSE_SCHEDULE_TYPE_SPACED_REPETITION = 1;
  COURSE_SCHEDULE_TYPE_CYCLICAL = 2;
  COURSE_SCHEDULE_TYPE_CUSTOM = 3;
}

enum CourseReviewFailedBehavior {
  COURSE_REVIEW_FAILED_BEHAVIOR_UNSPECIFIED = 0;
  COURSE_REVIEW_FAILED_BEHAVIOR_MOVE_TO_NEXT_CYCLE = 1;
  COURSE_REVIEW_FAILED_BEHAVIOR_REPEAT_CURRENT_CYCLE = 2;
  COURSE_REVIEW_FAILED_BEHAVIOR_BACK_TO_FIRST_CYCL
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01718"></a>
## FND-01718: chesscom.courses.v1.CourseScheduleType.COURSE_SCHEDULE_TYPE_CUSTOM = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_SCHEDULE_TYPE_CUSTOM = 3;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 767.

```text
SPECIFIED = 0;
  COURSE_SCHEDULE_TYPE_SPACED_REPETITION = 1;
  COURSE_SCHEDULE_TYPE_CYCLICAL = 2;
  COURSE_SCHEDULE_TYPE_CUSTOM = 3;
}

enum CourseReviewFailedBehavior {
  COURSE_REVIEW_FAILED_BEHAVIOR_UNSPECIFIED = 0;
  COURSE_REVIEW_FAILED_BEHAVIOR_MOVE_TO_NEXT_CYCLE = 1;
  COURSE_REVIEW_FAILED_BEHAVIOR_REPEAT_CURRENT_CYCLE = 2;
  COURSE_REVIEW_FAILED_BEHAVIOR_BACK_TO_FIRST_CYCLE = 3;
}

message CourseConfiguration
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01719"></a>
## FND-01719: enum declaration: chesscom.courses.v1.CourseReviewFailedBehavior

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum CourseReviewFailedBehavior {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 803.

```text
E_SPACED_REPETITION = 1;
  COURSE_SCHEDULE_TYPE_CYCLICAL = 2;
  COURSE_SCHEDULE_TYPE_CUSTOM = 3;
}

enum CourseReviewFailedBehavior {
  COURSE_REVIEW_FAILED_BEHAVIOR_UNSPECIFIED = 0;
  COURSE_REVIEW_FAILED_BEHAVIOR_MOVE_TO_NEXT_CYCLE = 1;
  COURSE_REVIEW_FAILED_BEHAVIOR_REPEAT_CURRENT_CYCLE = 2;
  COURSE_REVIEW_FAILED_BEHAVIOR_BACK_TO_FIRST_CYCLE = 3;
}

message CourseConfiguration {
  oneof _show_video {
  bool show
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01720"></a>
## FND-01720: chesscom.courses.v1.CourseReviewFailedBehavior.COURSE_REVIEW_FAILED_BEHAVIOR_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_REVIEW_FAILED_BEHAVIOR_UNSPECIFIED = 0;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 839.

```text
HEDULE_TYPE_CYCLICAL = 2;
  COURSE_SCHEDULE_TYPE_CUSTOM = 3;
}

enum CourseReviewFailedBehavior {
  COURSE_REVIEW_FAILED_BEHAVIOR_UNSPECIFIED = 0;
  COURSE_REVIEW_FAILED_BEHAVIOR_MOVE_TO_NEXT_CYCLE = 1;
  COURSE_REVIEW_FAILED_BEHAVIOR_REPEAT_CURRENT_CYCLE = 2;
  COURSE_REVIEW_FAILED_BEHAVIOR_BACK_TO_FIRST_CYCLE = 3;
}

message CourseConfiguration {
  oneof _show_video {
  bool show_video = 1;
  }
  oneof _language {

```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01721"></a>
## FND-01721: chesscom.courses.v1.CourseReviewFailedBehavior.COURSE_REVIEW_FAILED_BEHAVIOR_MOVE_TO_NEXT_CYCLE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_REVIEW_FAILED_BEHAVIOR_MOVE_TO_NEXT_CYCLE = 1;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 888.

```text
CUSTOM = 3;
}

enum CourseReviewFailedBehavior {
  COURSE_REVIEW_FAILED_BEHAVIOR_UNSPECIFIED = 0;
  COURSE_REVIEW_FAILED_BEHAVIOR_MOVE_TO_NEXT_CYCLE = 1;
  COURSE_REVIEW_FAILED_BEHAVIOR_REPEAT_CURRENT_CYCLE = 2;
  COURSE_REVIEW_FAILED_BEHAVIOR_BACK_TO_FIRST_CYCLE = 3;
}

message CourseConfiguration {
  oneof _show_video {
  bool show_video = 1;
  }
  oneof _language {
  string language = 2;
  }
  oneof _learn_type {

```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01722"></a>
## FND-01722: chesscom.courses.v1.CourseReviewFailedBehavior.COURSE_REVIEW_FAILED_BEHAVIOR_REPEAT_CURRENT_CYCLE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_REVIEW_FAILED_BEHAVIOR_REPEAT_CURRENT_CYCLE = 2;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 944.

```text
E_REVIEW_FAILED_BEHAVIOR_UNSPECIFIED = 0;
  COURSE_REVIEW_FAILED_BEHAVIOR_MOVE_TO_NEXT_CYCLE = 1;
  COURSE_REVIEW_FAILED_BEHAVIOR_REPEAT_CURRENT_CYCLE = 2;
  COURSE_REVIEW_FAILED_BEHAVIOR_BACK_TO_FIRST_CYCLE = 3;
}

message CourseConfiguration {
  oneof _show_video {
  bool show_video = 1;
  }
  oneof _language {
  string language = 2;
  }
  oneof _learn_type {
  .chesscom.courses.v1.CourseLearnType learn_type = 3;
 
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01723"></a>
## FND-01723: chesscom.courses.v1.CourseReviewFailedBehavior.COURSE_REVIEW_FAILED_BEHAVIOR_BACK_TO_FIRST_CYCLE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

COURSE_REVIEW_FAILED_BEHAVIOR_BACK_TO_FIRST_CYCLE = 3;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1002.

```text
FAILED_BEHAVIOR_MOVE_TO_NEXT_CYCLE = 1;
  COURSE_REVIEW_FAILED_BEHAVIOR_REPEAT_CURRENT_CYCLE = 2;
  COURSE_REVIEW_FAILED_BEHAVIOR_BACK_TO_FIRST_CYCLE = 3;
}

message CourseConfiguration {
  oneof _show_video {
  bool show_video = 1;
  }
  oneof _language {
  string language = 2;
  }
  oneof _learn_type {
  .chesscom.courses.v1.CourseLearnType learn_type = 3;
  }
  oneof _review_type {
  .chesscom.courses.v1.CourseRev
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01724"></a>
## FND-01724: message declaration: chesscom.courses.v1.CourseConfiguration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseConfiguration {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1060.

```text
ILED_BEHAVIOR_REPEAT_CURRENT_CYCLE = 2;
  COURSE_REVIEW_FAILED_BEHAVIOR_BACK_TO_FIRST_CYCLE = 3;
}

message CourseConfiguration {
  oneof _show_video {
  bool show_video = 1;
  }
  oneof _language {
  string language = 2;
  }
  oneof _learn_type {
  .chesscom.courses.v1.CourseLearnType learn_type = 3;
  }
  oneof _review_type {
  .chesscom.courses.v1.CourseReviewType review_type = 4;
  }
  oneof _repetition_amount {

```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01725"></a>
## FND-01725: oneof declaration: chesscom.courses.v1.CourseConfiguration._show_video

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _show_video {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1092.

```text
LE = 2;
  COURSE_REVIEW_FAILED_BEHAVIOR_BACK_TO_FIRST_CYCLE = 3;
}

message CourseConfiguration {
  oneof _show_video {
  bool show_video = 1;
  }
  oneof _language {
  string language = 2;
  }
  oneof _learn_type {
  .chesscom.courses.v1.CourseLearnType learn_type = 3;
  }
  oneof _review_type {
  .chesscom.courses.v1.CourseReviewType review_type = 4;
  }
  oneof _repetition_amount {
  int32 repetition_amount = 5;
 
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01726"></a>
## FND-01726: chesscom.courses.v1.CourseConfiguration.show_video = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool show_video = 1;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1114.

```text
W_FAILED_BEHAVIOR_BACK_TO_FIRST_CYCLE = 3;
}

message CourseConfiguration {
  oneof _show_video {
  bool show_video = 1;
  }
  oneof _language {
  string language = 2;
  }
  oneof _learn_type {
  .chesscom.courses.v1.CourseLearnType learn_type = 3;
  }
  oneof _review_type {
  .chesscom.courses.v1.CourseReviewType review_type = 4;
  }
  oneof _repetition_amount {
  int32 repetition_amount = 5;
  }
  oneof _depth {
  
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01727"></a>
## FND-01727: oneof declaration: chesscom.courses.v1.CourseConfiguration._language

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _language {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1141.

```text
IRST_CYCLE = 3;
}

message CourseConfiguration {
  oneof _show_video {
  bool show_video = 1;
  }
  oneof _language {
  string language = 2;
  }
  oneof _learn_type {
  .chesscom.courses.v1.CourseLearnType learn_type = 3;
  }
  oneof _review_type {
  .chesscom.courses.v1.CourseReviewType review_type = 4;
  }
  oneof _repetition_amount {
  int32 repetition_amount = 5;
  }
  oneof _depth {
  int32 depth = 6;
  }
  oneo
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01728"></a>
## FND-01728: chesscom.courses.v1.CourseConfiguration.language = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string language = 2;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1161.

```text
essage CourseConfiguration {
  oneof _show_video {
  bool show_video = 1;
  }
  oneof _language {
  string language = 2;
  }
  oneof _learn_type {
  .chesscom.courses.v1.CourseLearnType learn_type = 3;
  }
  oneof _review_type {
  .chesscom.courses.v1.CourseReviewType review_type = 4;
  }
  oneof _repetition_amount {
  int32 repetition_amount = 5;
  }
  oneof _depth {
  int32 depth = 6;
  }
  oneof _schedule_type {
 
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01729"></a>
## FND-01729: oneof declaration: chesscom.courses.v1.CourseConfiguration._learn_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _learn_type {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1188.

```text
{
  oneof _show_video {
  bool show_video = 1;
  }
  oneof _language {
  string language = 2;
  }
  oneof _learn_type {
  .chesscom.courses.v1.CourseLearnType learn_type = 3;
  }
  oneof _review_type {
  .chesscom.courses.v1.CourseReviewType review_type = 4;
  }
  oneof _repetition_amount {
  int32 repetition_amount = 5;
  }
  oneof _depth {
  int32 depth = 6;
  }
  oneof _schedule_type {
  .chesscom.courses.v1.Cours
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01730"></a>
## FND-01730: chesscom.courses.v1.CourseConfiguration.learn_type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseLearnType learn_type = 3;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1210.

```text
{
  bool show_video = 1;
  }
  oneof _language {
  string language = 2;
  }
  oneof _learn_type {
  .chesscom.courses.v1.CourseLearnType learn_type = 3;
  }
  oneof _review_type {
  .chesscom.courses.v1.CourseReviewType review_type = 4;
  }
  oneof _repetition_amount {
  int32 repetition_amount = 5;
  }
  oneof _depth {
  int32 depth = 6;
  }
  oneof _schedule_type {
  .chesscom.courses.v1.CourseScheduleType schedule
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01731"></a>
## FND-01731: oneof declaration: chesscom.courses.v1.CourseConfiguration._review_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _review_type {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1269.

```text
anguage = 2;
  }
  oneof _learn_type {
  .chesscom.courses.v1.CourseLearnType learn_type = 3;
  }
  oneof _review_type {
  .chesscom.courses.v1.CourseReviewType review_type = 4;
  }
  oneof _repetition_amount {
  int32 repetition_amount = 5;
  }
  oneof _depth {
  int32 depth = 6;
  }
  oneof _schedule_type {
  .chesscom.courses.v1.CourseScheduleType schedule_type = 7;
  }
  oneof _schedule {
  .chesscom.courses.v1.S
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01732"></a>
## FND-01732: chesscom.courses.v1.CourseConfiguration.review_type = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseReviewType review_type = 4;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1292.

```text
f _learn_type {
  .chesscom.courses.v1.CourseLearnType learn_type = 3;
  }
  oneof _review_type {
  .chesscom.courses.v1.CourseReviewType review_type = 4;
  }
  oneof _repetition_amount {
  int32 repetition_amount = 5;
  }
  oneof _depth {
  int32 depth = 6;
  }
  oneof _schedule_type {
  .chesscom.courses.v1.CourseScheduleType schedule_type = 7;
  }
  oneof _schedule {
  .chesscom.courses.v1.SpacedRepetitionSchedule
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01733"></a>
## FND-01733: oneof declaration: chesscom.courses.v1.CourseConfiguration._repetition_amount

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _repetition_amount {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1353.

```text
type = 3;
  }
  oneof _review_type {
  .chesscom.courses.v1.CourseReviewType review_type = 4;
  }
  oneof _repetition_amount {
  int32 repetition_amount = 5;
  }
  oneof _depth {
  int32 depth = 6;
  }
  oneof _schedule_type {
  .chesscom.courses.v1.CourseScheduleType schedule_type = 7;
  }
  oneof _schedule {
  .chesscom.courses.v1.SpacedRepetitionSchedule schedule = 8;
  }
  oneof _auto_next {
  bool auto_next = 9;
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01734"></a>
## FND-01734: chesscom.courses.v1.CourseConfiguration.repetition_amount = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 repetition_amount = 5;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1382.

```text
_type {
  .chesscom.courses.v1.CourseReviewType review_type = 4;
  }
  oneof _repetition_amount {
  int32 repetition_amount = 5;
  }
  oneof _depth {
  int32 depth = 6;
  }
  oneof _schedule_type {
  .chesscom.courses.v1.CourseScheduleType schedule_type = 7;
  }
  oneof _schedule {
  .chesscom.courses.v1.SpacedRepetitionSchedule schedule = 8;
  }
  oneof _auto_next {
  bool auto_next = 9;
  }
  oneof _quiz_time_limit
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01735"></a>
## FND-01735: oneof declaration: chesscom.courses.v1.CourseConfiguration._depth

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _depth {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1417.

```text
seReviewType review_type = 4;
  }
  oneof _repetition_amount {
  int32 repetition_amount = 5;
  }
  oneof _depth {
  int32 depth = 6;
  }
  oneof _schedule_type {
  .chesscom.courses.v1.CourseScheduleType schedule_type = 7;
  }
  oneof _schedule {
  .chesscom.courses.v1.SpacedRepetitionSchedule schedule = 8;
  }
  oneof _auto_next {
  bool auto_next = 9;
  }
  oneof _quiz_time_limit {
  bool quiz_time_limit = 10;
  }
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01736"></a>
## FND-01736: chesscom.courses.v1.CourseConfiguration.depth = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 depth = 6;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1434.

```text
ew_type = 4;
  }
  oneof _repetition_amount {
  int32 repetition_amount = 5;
  }
  oneof _depth {
  int32 depth = 6;
  }
  oneof _schedule_type {
  .chesscom.courses.v1.CourseScheduleType schedule_type = 7;
  }
  oneof _schedule {
  .chesscom.courses.v1.SpacedRepetitionSchedule schedule = 8;
  }
  oneof _auto_next {
  bool auto_next = 9;
  }
  oneof _quiz_time_limit {
  bool quiz_time_limit = 10;
  }
  oneof _timer {
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01737"></a>
## FND-01737: oneof declaration: chesscom.courses.v1.CourseConfiguration._schedule_type

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _schedule_type {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1457.

```text
f _repetition_amount {
  int32 repetition_amount = 5;
  }
  oneof _depth {
  int32 depth = 6;
  }
  oneof _schedule_type {
  .chesscom.courses.v1.CourseScheduleType schedule_type = 7;
  }
  oneof _schedule {
  .chesscom.courses.v1.SpacedRepetitionSchedule schedule = 8;
  }
  oneof _auto_next {
  bool auto_next = 9;
  }
  oneof _quiz_time_limit {
  bool quiz_time_limit = 10;
  }
  oneof _timer {
  int32 timer = 11;
  
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01738"></a>
## FND-01738: chesscom.courses.v1.CourseConfiguration.schedule_type = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseScheduleType schedule_type = 7;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1482.

```text
int32 repetition_amount = 5;
  }
  oneof _depth {
  int32 depth = 6;
  }
  oneof _schedule_type {
  .chesscom.courses.v1.CourseScheduleType schedule_type = 7;
  }
  oneof _schedule {
  .chesscom.courses.v1.SpacedRepetitionSchedule schedule = 8;
  }
  oneof _auto_next {
  bool auto_next = 9;
  }
  oneof _quiz_time_limit {
  bool quiz_time_limit = 10;
  }
  oneof _timer {
  int32 timer = 11;
  }
  oneof _assisted_quiz 
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01739"></a>
## FND-01739: oneof declaration: chesscom.courses.v1.CourseConfiguration._schedule

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _schedule {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1547.

```text
 6;
  }
  oneof _schedule_type {
  .chesscom.courses.v1.CourseScheduleType schedule_type = 7;
  }
  oneof _schedule {
  .chesscom.courses.v1.SpacedRepetitionSchedule schedule = 8;
  }
  oneof _auto_next {
  bool auto_next = 9;
  }
  oneof _quiz_time_limit {
  bool quiz_time_limit = 10;
  }
  oneof _timer {
  int32 timer = 11;
  }
  oneof _assisted_quiz {
  bool assisted_quiz = 12;
  }
  oneof _review_failed_behavior 
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01740"></a>
## FND-01740: chesscom.courses.v1.CourseConfiguration.schedule = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.SpacedRepetitionSchedule schedule = 8;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1567.

```text
edule_type {
  .chesscom.courses.v1.CourseScheduleType schedule_type = 7;
  }
  oneof _schedule {
  .chesscom.courses.v1.SpacedRepetitionSchedule schedule = 8;
  }
  oneof _auto_next {
  bool auto_next = 9;
  }
  oneof _quiz_time_limit {
  bool quiz_time_limit = 10;
  }
  oneof _timer {
  int32 timer = 11;
  }
  oneof _assisted_quiz {
  bool assisted_quiz = 12;
  }
  oneof _review_failed_behavior {
  .chesscom.course
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01741"></a>
## FND-01741: oneof declaration: chesscom.courses.v1.CourseConfiguration._auto_next

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _auto_next {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1633.

```text
pe = 7;
  }
  oneof _schedule {
  .chesscom.courses.v1.SpacedRepetitionSchedule schedule = 8;
  }
  oneof _auto_next {
  bool auto_next = 9;
  }
  oneof _quiz_time_limit {
  bool quiz_time_limit = 10;
  }
  oneof _timer {
  int32 timer = 11;
  }
  oneof _assisted_quiz {
  bool assisted_quiz = 12;
  }
  oneof _review_failed_behavior {
  .chesscom.courses.v1.CourseReviewFailedBehavior review_failed_behavior = 13;
  }
 
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01742"></a>
## FND-01742: chesscom.courses.v1.CourseConfiguration.auto_next = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool auto_next = 9;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1654.

```text
schedule {
  .chesscom.courses.v1.SpacedRepetitionSchedule schedule = 8;
  }
  oneof _auto_next {
  bool auto_next = 9;
  }
  oneof _quiz_time_limit {
  bool quiz_time_limit = 10;
  }
  oneof _timer {
  int32 timer = 11;
  }
  oneof _assisted_quiz {
  bool assisted_quiz = 12;
  }
  oneof _review_failed_behavior {
  .chesscom.courses.v1.CourseReviewFailedBehavior review_failed_behavior = 13;
  }
  oneof _assisted_quiz
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01743"></a>
## FND-01743: oneof declaration: chesscom.courses.v1.CourseConfiguration._quiz_time_limit

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _quiz_time_limit {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1680.

```text
rses.v1.SpacedRepetitionSchedule schedule = 8;
  }
  oneof _auto_next {
  bool auto_next = 9;
  }
  oneof _quiz_time_limit {
  bool quiz_time_limit = 10;
  }
  oneof _timer {
  int32 timer = 11;
  }
  oneof _assisted_quiz {
  bool assisted_quiz = 12;
  }
  oneof _review_failed_behavior {
  .chesscom.courses.v1.CourseReviewFailedBehavior review_failed_behavior = 13;
  }
  oneof _assisted_quiz_pause_to_read {
  bool as
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01744"></a>
## FND-01744: chesscom.courses.v1.CourseConfiguration.quiz_time_limit = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool quiz_time_limit = 10;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1707.

```text
edule schedule = 8;
  }
  oneof _auto_next {
  bool auto_next = 9;
  }
  oneof _quiz_time_limit {
  bool quiz_time_limit = 10;
  }
  oneof _timer {
  int32 timer = 11;
  }
  oneof _assisted_quiz {
  bool assisted_quiz = 12;
  }
  oneof _review_failed_behavior {
  .chesscom.courses.v1.CourseReviewFailedBehavior review_failed_behavior = 13;
  }
  oneof _assisted_quiz_pause_to_read {
  bool assisted_quiz_pause_to_read =
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01745"></a>
## FND-01745: oneof declaration: chesscom.courses.v1.CourseConfiguration._timer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _timer {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1740.

```text
auto_next {
  bool auto_next = 9;
  }
  oneof _quiz_time_limit {
  bool quiz_time_limit = 10;
  }
  oneof _timer {
  int32 timer = 11;
  }
  oneof _assisted_quiz {
  bool assisted_quiz = 12;
  }
  oneof _review_failed_behavior {
  .chesscom.courses.v1.CourseReviewFailedBehavior review_failed_behavior = 13;
  }
  oneof _assisted_quiz_pause_to_read {
  bool assisted_quiz_pause_to_read = 14;
  }
  oneof _learn_mode {
  
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01746"></a>
## FND-01746: chesscom.courses.v1.CourseConfiguration.timer = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 timer = 11;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1757.

```text
l auto_next = 9;
  }
  oneof _quiz_time_limit {
  bool quiz_time_limit = 10;
  }
  oneof _timer {
  int32 timer = 11;
  }
  oneof _assisted_quiz {
  bool assisted_quiz = 12;
  }
  oneof _review_failed_behavior {
  .chesscom.courses.v1.CourseReviewFailedBehavior review_failed_behavior = 13;
  }
  oneof _assisted_quiz_pause_to_read {
  bool assisted_quiz_pause_to_read = 14;
  }
  oneof _learn_mode {
  .chesscom.courses
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01747"></a>
## FND-01747: oneof declaration: chesscom.courses.v1.CourseConfiguration._assisted_quiz

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _assisted_quiz {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1781.

```text
neof _quiz_time_limit {
  bool quiz_time_limit = 10;
  }
  oneof _timer {
  int32 timer = 11;
  }
  oneof _assisted_quiz {
  bool assisted_quiz = 12;
  }
  oneof _review_failed_behavior {
  .chesscom.courses.v1.CourseReviewFailedBehavior review_failed_behavior = 13;
  }
  oneof _assisted_quiz_pause_to_read {
  bool assisted_quiz_pause_to_read = 14;
  }
  oneof _learn_mode {
  .chesscom.courses.v1.CourseConsumptionMod
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01748"></a>
## FND-01748: chesscom.courses.v1.CourseConfiguration.assisted_quiz = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool assisted_quiz = 12;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1806.

```text
 bool quiz_time_limit = 10;
  }
  oneof _timer {
  int32 timer = 11;
  }
  oneof _assisted_quiz {
  bool assisted_quiz = 12;
  }
  oneof _review_failed_behavior {
  .chesscom.courses.v1.CourseReviewFailedBehavior review_failed_behavior = 13;
  }
  oneof _assisted_quiz_pause_to_read {
  bool assisted_quiz_pause_to_read = 14;
  }
  oneof _learn_mode {
  .chesscom.courses.v1.CourseConsumptionMode learn_mode = 15;
  }
  
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01749"></a>
## FND-01749: oneof declaration: chesscom.courses.v1.CourseConfiguration._review_failed_behavior

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _review_failed_behavior {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1837.

```text

  oneof _timer {
  int32 timer = 11;
  }
  oneof _assisted_quiz {
  bool assisted_quiz = 12;
  }
  oneof _review_failed_behavior {
  .chesscom.courses.v1.CourseReviewFailedBehavior review_failed_behavior = 13;
  }
  oneof _assisted_quiz_pause_to_read {
  bool assisted_quiz_pause_to_read = 14;
  }
  oneof _learn_mode {
  .chesscom.courses.v1.CourseConsumptionMode learn_mode = 15;
  }
  oneof _learn_mode_set_by_user {
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01750"></a>
## FND-01750: chesscom.courses.v1.CourseConfiguration.review_failed_behavior = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseReviewFailedBehavior review_failed_behavior = 13;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1871.

```text
11;
  }
  oneof _assisted_quiz {
  bool assisted_quiz = 12;
  }
  oneof _review_failed_behavior {
  .chesscom.courses.v1.CourseReviewFailedBehavior review_failed_behavior = 13;
  }
  oneof _assisted_quiz_pause_to_read {
  bool assisted_quiz_pause_to_read = 14;
  }
  oneof _learn_mode {
  .chesscom.courses.v1.CourseConsumptionMode learn_mode = 15;
  }
  oneof _learn_mode_set_by_user {
  bool learn_mode_set_by_user = 1
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01751"></a>
## FND-01751: oneof declaration: chesscom.courses.v1.CourseConfiguration._assisted_quiz_pause_to_read

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _assisted_quiz_pause_to_read {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1954.

```text
led_behavior {
  .chesscom.courses.v1.CourseReviewFailedBehavior review_failed_behavior = 13;
  }
  oneof _assisted_quiz_pause_to_read {
  bool assisted_quiz_pause_to_read = 14;
  }
  oneof _learn_mode {
  .chesscom.courses.v1.CourseConsumptionMode learn_mode = 15;
  }
  oneof _learn_mode_set_by_user {
  bool learn_mode_set_by_user = 16;
  }
}

message SpacedRepetitionSchedule {
  repeated int32 seconds_amount = 1;
}
```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01752"></a>
## FND-01752: chesscom.courses.v1.CourseConfiguration.assisted_quiz_pause_to_read = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool assisted_quiz_pause_to_read = 14;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 1993.

```text
ourseReviewFailedBehavior review_failed_behavior = 13;
  }
  oneof _assisted_quiz_pause_to_read {
  bool assisted_quiz_pause_to_read = 14;
  }
  oneof _learn_mode {
  .chesscom.courses.v1.CourseConsumptionMode learn_mode = 15;
  }
  oneof _learn_mode_set_by_user {
  bool learn_mode_set_by_user = 16;
  }
}

message SpacedRepetitionSchedule {
  repeated int32 seconds_amount = 1;
}

```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01753"></a>
## FND-01753: oneof declaration: chesscom.courses.v1.CourseConfiguration._learn_mode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _learn_mode {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 2038.

```text
ior = 13;
  }
  oneof _assisted_quiz_pause_to_read {
  bool assisted_quiz_pause_to_read = 14;
  }
  oneof _learn_mode {
  .chesscom.courses.v1.CourseConsumptionMode learn_mode = 15;
  }
  oneof _learn_mode_set_by_user {
  bool learn_mode_set_by_user = 16;
  }
}

message SpacedRepetitionSchedule {
  repeated int32 seconds_amount = 1;
}

```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01754"></a>
## FND-01754: chesscom.courses.v1.CourseConfiguration.learn_mode = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.courses.v1.CourseConsumptionMode learn_mode = 15;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 2060.

```text
_assisted_quiz_pause_to_read {
  bool assisted_quiz_pause_to_read = 14;
  }
  oneof _learn_mode {
  .chesscom.courses.v1.CourseConsumptionMode learn_mode = 15;
  }
  oneof _learn_mode_set_by_user {
  bool learn_mode_set_by_user = 16;
  }
}

message SpacedRepetitionSchedule {
  repeated int32 seconds_amount = 1;
}

```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01755"></a>
## FND-01755: oneof declaration: chesscom.courses.v1.CourseConfiguration._learn_mode_set_by_user

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _learn_mode_set_by_user {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 2126.

```text
= 14;
  }
  oneof _learn_mode {
  .chesscom.courses.v1.CourseConsumptionMode learn_mode = 15;
  }
  oneof _learn_mode_set_by_user {
  bool learn_mode_set_by_user = 16;
  }
}

message SpacedRepetitionSchedule {
  repeated int32 seconds_amount = 1;
}

```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01756"></a>
## FND-01756: chesscom.courses.v1.CourseConfiguration.learn_mode_set_by_user = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool learn_mode_set_by_user = 16;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 2160.

```text
.chesscom.courses.v1.CourseConsumptionMode learn_mode = 15;
  }
  oneof _learn_mode_set_by_user {
  bool learn_mode_set_by_user = 16;
  }
}

message SpacedRepetitionSchedule {
  repeated int32 seconds_amount = 1;
}

```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01757"></a>
## FND-01757: message declaration: chesscom.courses.v1.SpacedRepetitionSchedule

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SpacedRepetitionSchedule {

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 2201.

```text
e learn_mode = 15;
  }
  oneof _learn_mode_set_by_user {
  bool learn_mode_set_by_user = 16;
  }
}

message SpacedRepetitionSchedule {
  repeated int32 seconds_amount = 1;
}

```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01758"></a>
## FND-01758: chesscom.courses.v1.SpacedRepetitionSchedule.seconds_amount = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated int32 seconds_amount = 1;

### Evidence

- **SRC-0272** `research/proto/chesscom/courses/v1/course_configuration.proto` — [preserved redacted evidence](../evidence/text/f5fd61014a2098132112a23f1af9b6e19eaa0946ebcafce044bc576e2e68698e.proto)
  Character offset 2238.

```text
_mode_set_by_user {
  bool learn_mode_set_by_user = 16;
  }
}

message SpacedRepetitionSchedule {
  repeated int32 seconds_amount = 1;
}

```

**Source references:** SRC-0272, SRC-1243  
**URL references:** None independently associated  
**Related findings:** FND-01700, FND-01701, FND-01702

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01759"></a>
## FND-01759: message declaration: chesscom.courses.v1.CourseCustomTag

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseCustomTag {

### Evidence

- **SRC-0273** `research/proto/chesscom/courses/v1/course_custom_tag.proto` — [preserved redacted evidence](../evidence/text/fa399cffc8274040dbcb38cd663a8d3ae187255c758ced0a58c7a41577925a96.proto)
  Character offset 104.

```text
ource: chesscom/courses/v1/course_custom_tag.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseCustomTag {
  optional string value = 1;
}

```

**Source references:** SRC-0273, SRC-1244  
**URL references:** None independently associated  
**Related findings:** FND-01760

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01760"></a>
## FND-01760: chesscom.courses.v1.CourseCustomTag.value = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 1;

### Evidence

- **SRC-0273** `research/proto/chesscom/courses/v1/course_custom_tag.proto` — [preserved redacted evidence](../evidence/text/fa399cffc8274040dbcb38cd663a8d3ae187255c758ced0a58c7a41577925a96.proto)
  Character offset 132.

```text
ourse_custom_tag.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseCustomTag {
  optional string value = 1;
}

```

**Source references:** SRC-0273, SRC-1244  
**URL references:** None independently associated  
**Related findings:** FND-01759

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01761"></a>
## FND-01761: message declaration: chesscom.courses.v1.CourseLearningSession

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseLearningSession {

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 110.

```text
 chesscom/courses/v1/course_learning_session.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseLearningSession {
  oneof _last_learned_variation_id {
  string last_learned_variation_id = 4;
  }
  repeated .chesscom.courses.v1.CourseVariation lessons_headers = 1;
  repeated .chesscom.courses.v1.CourseVariation reviews_headers = 2;
  repeated .chesscom.courses.v1.MoveTrainer move_trainers = 3;
}

mes
```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01762, FND-01763

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01762"></a>
## FND-01762: oneof declaration: chesscom.courses.v1.CourseLearningSession._last_learned_variation_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _last_learned_variation_id {

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 144.

```text
ng_session.proto
// syntax: proto3

package chesscom.courses.v1;

message CourseLearningSession {
  oneof _last_learned_variation_id {
  string last_learned_variation_id = 4;
  }
  repeated .chesscom.courses.v1.CourseVariation lessons_headers = 1;
  repeated .chesscom.courses.v1.CourseVariation reviews_headers = 2;
  repeated .chesscom.courses.v1.MoveTrainer move_trainers = 3;
}

message CourseLearningSessionStats {

```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01763

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01763"></a>
## FND-01763: chesscom.courses.v1.CourseLearningSession.last_learned_variation_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string last_learned_variation_id = 4;

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 181.

```text
ackage chesscom.courses.v1;

message CourseLearningSession {
  oneof _last_learned_variation_id {
  string last_learned_variation_id = 4;
  }
  repeated .chesscom.courses.v1.CourseVariation lessons_headers = 1;
  repeated .chesscom.courses.v1.CourseVariation reviews_headers = 2;
  repeated .chesscom.courses.v1.MoveTrainer move_trainers = 3;
}

message CourseLearningSessionStats {
  optional int32 total_learning_sessi
```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01764"></a>
## FND-01764: chesscom.courses.v1.CourseLearningSession.lessons_headers = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseVariation lessons_headers = 1;

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 225.

```text
earningSession {
  oneof _last_learned_variation_id {
  string last_learned_variation_id = 4;
  }
  repeated .chesscom.courses.v1.CourseVariation lessons_headers = 1;
  repeated .chesscom.courses.v1.CourseVariation reviews_headers = 2;
  repeated .chesscom.courses.v1.MoveTrainer move_trainers = 3;
}

message CourseLearningSessionStats {
  optional int32 total_learning_session_variations_amount = 1;
  optional int32 t
```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01765"></a>
## FND-01765: chesscom.courses.v1.CourseLearningSession.reviews_headers = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseVariation reviews_headers = 2;

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 294.

```text
earned_variation_id = 4;
  }
  repeated .chesscom.courses.v1.CourseVariation lessons_headers = 1;
  repeated .chesscom.courses.v1.CourseVariation reviews_headers = 2;
  repeated .chesscom.courses.v1.MoveTrainer move_trainers = 3;
}

message CourseLearningSessionStats {
  optional int32 total_learning_session_variations_amount = 1;
  optional int32 total_learning_session_time_seconds = 2;
  optional float total_learni
```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01766"></a>
## FND-01766: chesscom.courses.v1.CourseLearningSession.move_trainers = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.MoveTrainer move_trainers = 3;

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 363.

```text
riation lessons_headers = 1;
  repeated .chesscom.courses.v1.CourseVariation reviews_headers = 2;
  repeated .chesscom.courses.v1.MoveTrainer move_trainers = 3;
}

message CourseLearningSessionStats {
  optional int32 total_learning_session_variations_amount = 1;
  optional int32 total_learning_session_time_seconds = 2;
  optional float total_learning_session_accuracy = 3;
  optional int32 current_training_variations
```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01767"></a>
## FND-01767: message declaration: chesscom.courses.v1.CourseLearningSessionStats

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseLearningSessionStats {

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 427.

```text
rseVariation reviews_headers = 2;
  repeated .chesscom.courses.v1.MoveTrainer move_trainers = 3;
}

message CourseLearningSessionStats {
  optional int32 total_learning_session_variations_amount = 1;
  optional int32 total_learning_session_time_seconds = 2;
  optional float total_learning_session_accuracy = 3;
  optional int32 current_training_variations_amount = 4;
  optional int32 current_training_time_seconds = 5;
```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-01768"></a>
## FND-01768: chesscom.courses.v1.CourseLearningSessionStats.total_learning_session_variations_amount = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 total_learning_session_variations_amount = 1;

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 466.

```text
eated .chesscom.courses.v1.MoveTrainer move_trainers = 3;
}

message CourseLearningSessionStats {
  optional int32 total_learning_session_variations_amount = 1;
  optional int32 total_learning_session_time_seconds = 2;
  optional float total_learning_session_accuracy = 3;
  optional int32 current_training_variations_amount = 4;
  optional int32 current_training_time_seconds = 5;
  repeated .chesscom.courses.v1.Course
```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01769"></a>
## FND-01769: chesscom.courses.v1.CourseLearningSessionStats.total_learning_session_time_seconds = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 total_learning_session_time_seconds = 2;

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 529.

```text
ssage CourseLearningSessionStats {
  optional int32 total_learning_session_variations_amount = 1;
  optional int32 total_learning_session_time_seconds = 2;
  optional float total_learning_session_accuracy = 3;
  optional int32 current_training_variations_amount = 4;
  optional int32 current_training_time_seconds = 5;
  repeated .chesscom.courses.v1.CourseVariationTypeCount total_learning_session_variations_by_type = 
```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01770"></a>
## FND-01770: chesscom.courses.v1.CourseLearningSessionStats.total_learning_session_accuracy = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional float total_learning_session_accuracy = 3;

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 587.

```text
learning_session_variations_amount = 1;
  optional int32 total_learning_session_time_seconds = 2;
  optional float total_learning_session_accuracy = 3;
  optional int32 current_training_variations_amount = 4;
  optional int32 current_training_time_seconds = 5;
  repeated .chesscom.courses.v1.CourseVariationTypeCount total_learning_session_variations_by_type = 6;
}

message CourseLearningSessionProgress {
  repeated .
```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01771"></a>
## FND-01771: chesscom.courses.v1.CourseLearningSessionStats.current_training_variations_amount = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 current_training_variations_amount = 4;

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 641.

```text
32 total_learning_session_time_seconds = 2;
  optional float total_learning_session_accuracy = 3;
  optional int32 current_training_variations_amount = 4;
  optional int32 current_training_time_seconds = 5;
  repeated .chesscom.courses.v1.CourseVariationTypeCount total_learning_session_variations_by_type = 6;
}

message CourseLearningSessionProgress {
  repeated .chesscom.courses.v1.CourseVariationTypeCount total_lea
```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01772"></a>
## FND-01772: chesscom.courses.v1.CourseLearningSessionStats.current_training_time_seconds = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 current_training_time_seconds = 5;

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 698.

```text
oat total_learning_session_accuracy = 3;
  optional int32 current_training_variations_amount = 4;
  optional int32 current_training_time_seconds = 5;
  repeated .chesscom.courses.v1.CourseVariationTypeCount total_learning_session_variations_by_type = 6;
}

message CourseLearningSessionProgress {
  repeated .chesscom.courses.v1.CourseVariationTypeCount total_learning_session_variations_by_type = 1;
}

message CourseVa
```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01773"></a>
## FND-01773: chesscom.courses.v1.CourseLearningSessionStats.total_learning_session_variations_by_type = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.courses.v1.CourseVariationTypeCount total_learning_session_variations_by_type = 6;

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 750.

```text
int32 current_training_variations_amount = 4;
  optional int32 current_training_time_seconds = 5;
  repeated .chesscom.courses.v1.CourseVariationTypeCount total_learning_session_variations_by_type = 6;
}

message CourseLearningSessionProgress {
  repeated .chesscom.courses.v1.CourseVariationTypeCount total_learning_session_variations_by_type = 1;
}

message CourseVariationTypeCount {
  optional .chesscom.courses_comm
```

**Source references:** SRC-0274, SRC-1245  
**URL references:** None independently associated  
**Related findings:** FND-01761, FND-01762, FND-01763

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-01774"></a>
## FND-01774: message declaration: chesscom.courses.v1.CourseLearningSessionProgress

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CourseLearningSessionProgress {

### Evidence

- **SRC-0274** `research/proto/chesscom/courses/v1/course_learning_session.proto` — [preserved redacted evidence](../evidence/text/e2bf758156b93721281cf8a5e9ad77f383d6cdf1b10a1de41dddbb3d63ab477a.proto)
  Character offset 855.

```text
ted .chesscom.courses.v1.CourseVariationTypeCount total_learning_session_variations_by_type = 6;
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

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
