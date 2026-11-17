# data_models — findings 7401–7500

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-07675"></a>
## FND-07675: oneof declaration: chesscom.ratings.v2.Rating._timestamp

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _timestamp {

### Evidence

- **SRC-0528** `research/proto/chesscom/ratings/v2/rating.proto` — [preserved redacted evidence](../evidence/text/5378162ec605ecace49fcb88bc32b5a5f03cb0e8b78fc1cf4e10abf7043ff213.proto)
  Character offset 112.

```text
hesscom/ratings/v2/rating.proto
// syntax: proto3

package chesscom.ratings.v2;

message Rating {
  oneof _timestamp {
  .google.protobuf.Timestamp timestamp = 3;
  }
  optional uint32 value = 1;
  optional .chesscom.api.v1.Decimal deviation = 2;
}

```

**Source references:** SRC-0528, SRC-1499  
**URL references:** None independently associated  
**Related findings:** FND-07674, FND-07676

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07676"></a>
## FND-07676: chesscom.ratings.v2.Rating.timestamp = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp timestamp = 3;

### Evidence

- **SRC-0528** `research/proto/chesscom/ratings/v2/rating.proto` — [preserved redacted evidence](../evidence/text/5378162ec605ecace49fcb88bc32b5a5f03cb0e8b78fc1cf4e10abf7043ff213.proto)
  Character offset 133.

```text
ting.proto
// syntax: proto3

package chesscom.ratings.v2;

message Rating {
  oneof _timestamp {
  .google.protobuf.Timestamp timestamp = 3;
  }
  optional uint32 value = 1;
  optional .chesscom.api.v1.Decimal deviation = 2;
}

```

**Source references:** SRC-0528, SRC-1499  
**URL references:** None independently associated  
**Related findings:** FND-07674, FND-07675

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07677"></a>
## FND-07677: chesscom.ratings.v2.Rating.value = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 value = 1;

### Evidence

- **SRC-0528** `research/proto/chesscom/ratings/v2/rating.proto` — [preserved redacted evidence](../evidence/text/5378162ec605ecace49fcb88bc32b5a5f03cb0e8b78fc1cf4e10abf7043ff213.proto)
  Character offset 181.

```text
atings.v2;

message Rating {
  oneof _timestamp {
  .google.protobuf.Timestamp timestamp = 3;
  }
  optional uint32 value = 1;
  optional .chesscom.api.v1.Decimal deviation = 2;
}

```

**Source references:** SRC-0528, SRC-1499  
**URL references:** None independently associated  
**Related findings:** FND-07674, FND-07675, FND-07676

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07678"></a>
## FND-07678: chesscom.ratings.v2.Rating.deviation = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Decimal deviation = 2;

### Evidence

- **SRC-0528** `research/proto/chesscom/ratings/v2/rating.proto` — [preserved redacted evidence](../evidence/text/5378162ec605ecace49fcb88bc32b5a5f03cb0e8b78fc1cf4e10abf7043ff213.proto)
  Character offset 210.

```text
  oneof _timestamp {
  .google.protobuf.Timestamp timestamp = 3;
  }
  optional uint32 value = 1;
  optional .chesscom.api.v1.Decimal deviation = 2;
}

```

**Source references:** SRC-0528, SRC-1499  
**URL references:** None independently associated  
**Related findings:** FND-07674, FND-07675, FND-07676

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07679"></a>
## FND-07679: message declaration: chesscom.ratings.v2.VariantTimeClassRating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message VariantTimeClassRating {

### Evidence

- **SRC-0529** `research/proto/chesscom/ratings/v2/variant_time_class_rating.proto` — [preserved redacted evidence](../evidence/text/cde2a52894e3f8d5b01eb1e4167f1a257a56d23460b9ea75a040bac6333fadad.proto)
  Character offset 112.

```text
hesscom/ratings/v2/variant_time_class_rating.proto
// syntax: proto3

package chesscom.ratings.v2;

message VariantTimeClassRating {
  optional .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  optional .chesscom.ratings.v2.Rating rating = 3;
}

message VariantTimeClassRatingGroup {
  optional .chesscom.chess.v1.Variant variant = 1;
  repeated .chesscom.ratings.v2.TimeC
```

**Source references:** SRC-0529, SRC-1500  
**URL references:** None independently associated  
**Related findings:** FND-07680, FND-07681

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07680"></a>
## FND-07680: chesscom.ratings.v2.VariantTimeClassRating.variant = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Variant variant = 1;

### Evidence

- **SRC-0529** `research/proto/chesscom/ratings/v2/variant_time_class_rating.proto` — [preserved redacted evidence](../evidence/text/cde2a52894e3f8d5b01eb1e4167f1a257a56d23460b9ea75a040bac6333fadad.proto)
  Character offset 147.

```text
ss_rating.proto
// syntax: proto3

package chesscom.ratings.v2;

message VariantTimeClassRating {
  optional .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  optional .chesscom.ratings.v2.Rating rating = 3;
}

message VariantTimeClassRatingGroup {
  optional .chesscom.chess.v1.Variant variant = 1;
  repeated .chesscom.ratings.v2.TimeClassRating time_class_rating = 2;
}
```

**Source references:** SRC-0529, SRC-1500  
**URL references:** None independently associated  
**Related findings:** FND-07679, FND-07681

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07681"></a>
## FND-07681: chesscom.ratings.v2.VariantTimeClassRating.time_class = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.TimeClass time_class = 2;

### Evidence

- **SRC-0529** `research/proto/chesscom/ratings/v2/variant_time_class_rating.proto` — [preserved redacted evidence](../evidence/text/cde2a52894e3f8d5b01eb1e4167f1a257a56d23460b9ea75a040bac6333fadad.proto)
  Character offset 198.

```text
.ratings.v2;

message VariantTimeClassRating {
  optional .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  optional .chesscom.ratings.v2.Rating rating = 3;
}

message VariantTimeClassRatingGroup {
  optional .chesscom.chess.v1.Variant variant = 1;
  repeated .chesscom.ratings.v2.TimeClassRating time_class_rating = 2;
}

message TimeClassRating {
  optional .chesscom.ch
```

**Source references:** SRC-0529, SRC-1500  
**URL references:** None independently associated  
**Related findings:** FND-07679, FND-07680

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07682"></a>
## FND-07682: chesscom.ratings.v2.VariantTimeClassRating.rating = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ratings.v2.Rating rating = 3;

### Evidence

- **SRC-0529** `research/proto/chesscom/ratings/v2/variant_time_class_rating.proto` — [preserved redacted evidence](../evidence/text/cde2a52894e3f8d5b01eb1e4167f1a257a56d23460b9ea75a040bac6333fadad.proto)
  Character offset 254.

```text
l .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  optional .chesscom.ratings.v2.Rating rating = 3;
}

message VariantTimeClassRatingGroup {
  optional .chesscom.chess.v1.Variant variant = 1;
  repeated .chesscom.ratings.v2.TimeClassRating time_class_rating = 2;
}

message TimeClassRating {
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ra
```

**Source references:** SRC-0529, SRC-1500  
**URL references:** None independently associated  
**Related findings:** FND-07679, FND-07680, FND-07681

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07683"></a>
## FND-07683: message declaration: chesscom.ratings.v2.VariantTimeClassRatingGroup

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message VariantTimeClassRatingGroup {

### Evidence

- **SRC-0529** `research/proto/chesscom/ratings/v2/variant_time_class_rating.proto` — [preserved redacted evidence](../evidence/text/cde2a52894e3f8d5b01eb1e4167f1a257a56d23460b9ea75a040bac6333fadad.proto)
  Character offset 306.

```text
 .chesscom.chess.v1.TimeClass time_class = 2;
  optional .chesscom.ratings.v2.Rating rating = 3;
}

message VariantTimeClassRatingGroup {
  optional .chesscom.chess.v1.Variant variant = 1;
  repeated .chesscom.ratings.v2.TimeClassRating time_class_rating = 2;
}

message TimeClassRating {
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ratings.v2.Rating rating = 2;
}

```

**Source references:** SRC-0529, SRC-1500  
**URL references:** None independently associated  
**Related findings:** FND-07679, FND-07680, FND-07681

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07684"></a>
## FND-07684: chesscom.ratings.v2.VariantTimeClassRatingGroup.variant = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Variant variant = 1;

### Evidence

- **SRC-0529** `research/proto/chesscom/ratings/v2/variant_time_class_rating.proto` — [preserved redacted evidence](../evidence/text/cde2a52894e3f8d5b01eb1e4167f1a257a56d23460b9ea75a040bac6333fadad.proto)
  Character offset 147.

```text
ss_rating.proto
// syntax: proto3

package chesscom.ratings.v2;

message VariantTimeClassRating {
  optional .chesscom.chess.v1.Variant variant = 1;
  optional .chesscom.chess.v1.TimeClass time_class = 2;
  optional .chesscom.ratings.v2.Rating rating = 3;
}

message VariantTimeClassRatingGroup {
  optional .chesscom.chess.v1.Variant variant = 1;
  repeated .chesscom.ratings.v2.TimeClassRating time_class_rating = 2;
}
```

**Source references:** SRC-0529, SRC-1500  
**URL references:** None independently associated  
**Related findings:** FND-07679, FND-07680, FND-07681

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07685"></a>
## FND-07685: chesscom.ratings.v2.VariantTimeClassRatingGroup.time_class_rating = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.ratings.v2.TimeClassRating time_class_rating = 2;

### Evidence

- **SRC-0529** `research/proto/chesscom/ratings/v2/variant_time_class_rating.proto` — [preserved redacted evidence](../evidence/text/cde2a52894e3f8d5b01eb1e4167f1a257a56d23460b9ea75a040bac6333fadad.proto)
  Character offset 397.

```text
 = 3;
}

message VariantTimeClassRatingGroup {
  optional .chesscom.chess.v1.Variant variant = 1;
  repeated .chesscom.ratings.v2.TimeClassRating time_class_rating = 2;
}

message TimeClassRating {
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ratings.v2.Rating rating = 2;
}

```

**Source references:** SRC-0529, SRC-1500  
**URL references:** None independently associated  
**Related findings:** FND-07679, FND-07680, FND-07681

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07686"></a>
## FND-07686: message declaration: chesscom.ratings.v2.TimeClassRating

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TimeClassRating {

### Evidence

- **SRC-0529** `research/proto/chesscom/ratings/v2/variant_time_class_rating.proto` — [preserved redacted evidence](../evidence/text/cde2a52894e3f8d5b01eb1e4167f1a257a56d23460b9ea75a040bac6333fadad.proto)
  Character offset 469.

```text
s.v1.Variant variant = 1;
  repeated .chesscom.ratings.v2.TimeClassRating time_class_rating = 2;
}

message TimeClassRating {
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ratings.v2.Rating rating = 2;
}

```

**Source references:** SRC-0529, SRC-1500  
**URL references:** None independently associated  
**Related findings:** FND-07679, FND-07680, FND-07681

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07687"></a>
## FND-07687: chesscom.ratings.v2.TimeClassRating.time_class = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.TimeClass time_class = 1;

### Evidence

- **SRC-0529** `research/proto/chesscom/ratings/v2/variant_time_class_rating.proto` — [preserved redacted evidence](../evidence/text/cde2a52894e3f8d5b01eb1e4167f1a257a56d23460b9ea75a040bac6333fadad.proto)
  Character offset 497.

```text
repeated .chesscom.ratings.v2.TimeClassRating time_class_rating = 2;
}

message TimeClassRating {
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ratings.v2.Rating rating = 2;
}

```

**Source references:** SRC-0529, SRC-1500  
**URL references:** None independently associated  
**Related findings:** FND-07679, FND-07680, FND-07681

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07688"></a>
## FND-07688: chesscom.ratings.v2.TimeClassRating.rating = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.ratings.v2.Rating rating = 2;

### Evidence

- **SRC-0529** `research/proto/chesscom/ratings/v2/variant_time_class_rating.proto` — [preserved redacted evidence](../evidence/text/cde2a52894e3f8d5b01eb1e4167f1a257a56d23460b9ea75a040bac6333fadad.proto)
  Character offset 553.

```text
_rating = 2;
}

message TimeClassRating {
  optional .chesscom.chess.v1.TimeClass time_class = 1;
  optional .chesscom.ratings.v2.Rating rating = 2;
}

```

**Source references:** SRC-0529, SRC-1500  
**URL references:** None independently associated  
**Related findings:** FND-07679, FND-07680, FND-07681

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07689"></a>
## FND-07689: message declaration: chesscom.settings.v1.BoardSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BoardSetting {

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 103.

```text
source: chesscom/settings/v1/settings_board.proto
// syntax: proto3

package chesscom.settings.v1;

message BoardSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String coordinates = 1;
  .chesscom.settings.v1.SettingValue.String move_list_style = 2;
  .chesscom.settings.v1.SettingValue.String animation_type = 3;
  .chesscom.settings.v1.SettingValue.String win_celebration = 4;
  .chesscom.settings.v1.Se
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07690, FND-07691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07690"></a>
## FND-07690: oneof declaration: chesscom.settings.v1.BoardSetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 128.

```text
/v1/settings_board.proto
// syntax: proto3

package chesscom.settings.v1;

message BoardSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String coordinates = 1;
  .chesscom.settings.v1.SettingValue.String move_list_style = 2;
  .chesscom.settings.v1.SettingValue.String animation_type = 3;
  .chesscom.settings.v1.SettingValue.String win_celebration = 4;
  .chesscom.settings.v1.SettingValue.String move_me
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07691

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07691"></a>
## FND-07691: chesscom.settings.v1.BoardSetting.coordinates = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String coordinates = 1;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 144.

```text
rd.proto
// syntax: proto3

package chesscom.settings.v1;

message BoardSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String coordinates = 1;
  .chesscom.settings.v1.SettingValue.String move_list_style = 2;
  .chesscom.settings.v1.SettingValue.String animation_type = 3;
  .chesscom.settings.v1.SettingValue.String win_celebration = 4;
  .chesscom.settings.v1.SettingValue.String move_method = 5;
  .che
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07692"></a>
## FND-07692: chesscom.settings.v1.BoardSetting.move_list_style = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String move_list_style = 2;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 205.

```text
ssage BoardSetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.String coordinates = 1;
  .chesscom.settings.v1.SettingValue.String move_list_style = 2;
  .chesscom.settings.v1.SettingValue.String animation_type = 3;
  .chesscom.settings.v1.SettingValue.String win_celebration = 4;
  .chesscom.settings.v1.SettingValue.String move_method = 5;
  .chesscom.settings.v1.SettingValue.Boolean highlight_moves = 6;
 
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07693"></a>
## FND-07693: chesscom.settings.v1.BoardSetting.animation_type = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String animation_type = 3;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 270.

```text
ingValue.String coordinates = 1;
  .chesscom.settings.v1.SettingValue.String move_list_style = 2;
  .chesscom.settings.v1.SettingValue.String animation_type = 3;
  .chesscom.settings.v1.SettingValue.String win_celebration = 4;
  .chesscom.settings.v1.SettingValue.String move_method = 5;
  .chesscom.settings.v1.SettingValue.Boolean highlight_moves = 6;
  .chesscom.settings.v1.SettingValue.Boolean white_always_on_botto
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07694"></a>
## FND-07694: chesscom.settings.v1.BoardSetting.win_celebration = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String win_celebration = 4;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 334.

```text
Value.String move_list_style = 2;
  .chesscom.settings.v1.SettingValue.String animation_type = 3;
  .chesscom.settings.v1.SettingValue.String win_celebration = 4;
  .chesscom.settings.v1.SettingValue.String move_method = 5;
  .chesscom.settings.v1.SettingValue.Boolean highlight_moves = 6;
  .chesscom.settings.v1.SettingValue.Boolean white_always_on_bottom = 7;
  .chesscom.settings.v1.SettingValue.Boolean play_sounds 
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07695"></a>
## FND-07695: chesscom.settings.v1.BoardSetting.move_method = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String move_method = 5;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 399.

```text
Value.String animation_type = 3;
  .chesscom.settings.v1.SettingValue.String win_celebration = 4;
  .chesscom.settings.v1.SettingValue.String move_method = 5;
  .chesscom.settings.v1.SettingValue.Boolean highlight_moves = 6;
  .chesscom.settings.v1.SettingValue.Boolean white_always_on_bottom = 7;
  .chesscom.settings.v1.SettingValue.Boolean play_sounds = 8;
  .chesscom.settings.v1.SettingValue.Boolean show_legal_move
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07696"></a>
## FND-07696: chesscom.settings.v1.BoardSetting.highlight_moves = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean highlight_moves = 6;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 460.

```text
ingValue.String win_celebration = 4;
  .chesscom.settings.v1.SettingValue.String move_method = 5;
  .chesscom.settings.v1.SettingValue.Boolean highlight_moves = 6;
  .chesscom.settings.v1.SettingValue.Boolean white_always_on_bottom = 7;
  .chesscom.settings.v1.SettingValue.Boolean play_sounds = 8;
  .chesscom.settings.v1.SettingValue.Boolean show_legal_moves = 9;
  .chesscom.settings.v1.SettingValue.Boolean show_anim
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07697"></a>
## FND-07697: chesscom.settings.v1.BoardSetting.white_always_on_bottom = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean white_always_on_bottom = 7;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 526.

```text
ngValue.String move_method = 5;
  .chesscom.settings.v1.SettingValue.Boolean highlight_moves = 6;
  .chesscom.settings.v1.SettingValue.Boolean white_always_on_bottom = 7;
  .chesscom.settings.v1.SettingValue.Boolean play_sounds = 8;
  .chesscom.settings.v1.SettingValue.Boolean show_legal_moves = 9;
  .chesscom.settings.v1.SettingValue.Boolean show_animations = 10;
  .chesscom.settings.v1.SettingValue.String board_sty
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07698"></a>
## FND-07698: chesscom.settings.v1.BoardSetting.play_sounds = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean play_sounds = 8;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 599.

```text
ean highlight_moves = 6;
  .chesscom.settings.v1.SettingValue.Boolean white_always_on_bottom = 7;
  .chesscom.settings.v1.SettingValue.Boolean play_sounds = 8;
  .chesscom.settings.v1.SettingValue.Boolean show_legal_moves = 9;
  .chesscom.settings.v1.SettingValue.Boolean show_animations = 10;
  .chesscom.settings.v1.SettingValue.String board_style = 11;
  .chesscom.settings.v1.SettingValue.String pieces_style = 12;
 
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07699"></a>
## FND-07699: chesscom.settings.v1.BoardSetting.show_legal_moves = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_legal_moves = 9;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 661.

```text
Boolean white_always_on_bottom = 7;
  .chesscom.settings.v1.SettingValue.Boolean play_sounds = 8;
  .chesscom.settings.v1.SettingValue.Boolean show_legal_moves = 9;
  .chesscom.settings.v1.SettingValue.Boolean show_animations = 10;
  .chesscom.settings.v1.SettingValue.String board_style = 11;
  .chesscom.settings.v1.SettingValue.String pieces_style = 12;
  .chesscom.settings.v1.SettingValue.String sound_theme = 13;
 
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07700"></a>
## FND-07700: chesscom.settings.v1.BoardSetting.show_animations = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_animations = 10;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 728.

```text
Value.Boolean play_sounds = 8;
  .chesscom.settings.v1.SettingValue.Boolean show_legal_moves = 9;
  .chesscom.settings.v1.SettingValue.Boolean show_animations = 10;
  .chesscom.settings.v1.SettingValue.String board_style = 11;
  .chesscom.settings.v1.SettingValue.String pieces_style = 12;
  .chesscom.settings.v1.SettingValue.String sound_theme = 13;
  .chesscom.settings.v1.SettingValue.String castling_type = 14;
  .c
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07701"></a>
## FND-07701: chesscom.settings.v1.BoardSetting.board_style = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String board_style = 11;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 795.

```text
.Boolean show_legal_moves = 9;
  .chesscom.settings.v1.SettingValue.Boolean show_animations = 10;
  .chesscom.settings.v1.SettingValue.String board_style = 11;
  .chesscom.settings.v1.SettingValue.String pieces_style = 12;
  .chesscom.settings.v1.SettingValue.String sound_theme = 13;
  .chesscom.settings.v1.SettingValue.String castling_type = 14;
  .chesscom.settings.v1.SettingValue.String move_classification_style =
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07702"></a>
## FND-07702: chesscom.settings.v1.BoardSetting.pieces_style = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String pieces_style = 12;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 857.

```text
Value.Boolean show_animations = 10;
  .chesscom.settings.v1.SettingValue.String board_style = 11;
  .chesscom.settings.v1.SettingValue.String pieces_style = 12;
  .chesscom.settings.v1.SettingValue.String sound_theme = 13;
  .chesscom.settings.v1.SettingValue.String castling_type = 14;
  .chesscom.settings.v1.SettingValue.String move_classification_style = 15;
  .chesscom.settings.v1.SettingValue.Boolean game_result_
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07703"></a>
## FND-07703: chesscom.settings.v1.BoardSetting.sound_theme = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String sound_theme = 13;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 920.

```text
tingValue.String board_style = 11;
  .chesscom.settings.v1.SettingValue.String pieces_style = 12;
  .chesscom.settings.v1.SettingValue.String sound_theme = 13;
  .chesscom.settings.v1.SettingValue.String castling_type = 14;
  .chesscom.settings.v1.SettingValue.String move_classification_style = 15;
  .chesscom.settings.v1.SettingValue.Boolean game_result_animations = 16;
  .chesscom.settings.v1.SettingValue.String ga
```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07704"></a>
## FND-07704: chesscom.settings.v1.BoardSetting.castling_type = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String castling_type = 14;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 982.

```text
tingValue.String pieces_style = 12;
  .chesscom.settings.v1.SettingValue.String sound_theme = 13;
  .chesscom.settings.v1.SettingValue.String castling_type = 14;
  .chesscom.settings.v1.SettingValue.String move_classification_style = 15;
  .chesscom.settings.v1.SettingValue.Boolean game_result_animations = 16;
  .chesscom.settings.v1.SettingValue.String game_over_screen = 17;
  }
}

```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07705"></a>
## FND-07705: chesscom.settings.v1.BoardSetting.move_classification_style = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String move_classification_style = 15;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 1046.

```text
ingValue.String sound_theme = 13;
  .chesscom.settings.v1.SettingValue.String castling_type = 14;
  .chesscom.settings.v1.SettingValue.String move_classification_style = 15;
  .chesscom.settings.v1.SettingValue.Boolean game_result_animations = 16;
  .chesscom.settings.v1.SettingValue.String game_over_screen = 17;
  }
}

```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07706"></a>
## FND-07706: chesscom.settings.v1.BoardSetting.game_result_animations = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean game_result_animations = 16;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 1122.

```text
g castling_type = 14;
  .chesscom.settings.v1.SettingValue.String move_classification_style = 15;
  .chesscom.settings.v1.SettingValue.Boolean game_result_animations = 16;
  .chesscom.settings.v1.SettingValue.String game_over_screen = 17;
  }
}

```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07707"></a>
## FND-07707: chesscom.settings.v1.BoardSetting.game_over_screen = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String game_over_screen = 17;

### Evidence

- **SRC-0530** `research/proto/chesscom/settings/v1/settings_board.proto` — [preserved redacted evidence](../evidence/text/9b3ba817baa309c08edbed3947ef8e885b632a17d6899b2188fafa7159acec4b.proto)
  Character offset 1196.

```text
ssification_style = 15;
  .chesscom.settings.v1.SettingValue.Boolean game_result_animations = 16;
  .chesscom.settings.v1.SettingValue.String game_over_screen = 17;
  }
}

```

**Source references:** SRC-0530, SRC-1501  
**URL references:** None independently associated  
**Related findings:** FND-07689, FND-07690, FND-07691

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07708"></a>
## FND-07708: message declaration: chesscom.settings.v1.GameplaySetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameplaySetting {

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 106.

```text
rce: chesscom/settings/v1/settings_gameplay.proto
// syntax: proto3

package chesscom.settings.v1;

message GameplaySetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean confirm_resign = 1;
  .chesscom.settings.v1.SettingValue.Boolean focus_mode = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_analysis = 3;
  .chesscom.settings.v1.SettingValue.String allow_challenges_from = 4;
  .chesscom.setti
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07709, FND-07710

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07709"></a>
## FND-07709: oneof declaration: chesscom.settings.v1.GameplaySetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 134.

```text
ttings_gameplay.proto
// syntax: proto3

package chesscom.settings.v1;

message GameplaySetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean confirm_resign = 1;
  .chesscom.settings.v1.SettingValue.Boolean focus_mode = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_analysis = 3;
  .chesscom.settings.v1.SettingValue.String allow_challenges_from = 4;
  .chesscom.settings.v1.SettingValue.String a
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07710

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07710"></a>
## FND-07710: chesscom.settings.v1.GameplaySetting.confirm_resign = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean confirm_resign = 1;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 150.

```text
proto
// syntax: proto3

package chesscom.settings.v1;

message GameplaySetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean confirm_resign = 1;
  .chesscom.settings.v1.SettingValue.Boolean focus_mode = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_analysis = 3;
  .chesscom.settings.v1.SettingValue.String allow_challenges_from = 4;
  .chesscom.settings.v1.SettingValue.String allow_game_chat_w
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07711"></a>
## FND-07711: chesscom.settings.v1.GameplaySetting.focus_mode = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean focus_mode = 2;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 215.

```text
ameplaySetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean confirm_resign = 1;
  .chesscom.settings.v1.SettingValue.Boolean focus_mode = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_analysis = 3;
  .chesscom.settings.v1.SettingValue.String allow_challenges_from = 4;
  .chesscom.settings.v1.SettingValue.String allow_game_chat_with = 5;
  .chesscom.settings.v1.SettingValue.Integer challenge_m
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07712"></a>
## FND-07712: chesscom.settings.v1.GameplaySetting.auto_analysis = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean auto_analysis = 3;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 276.

```text
ingValue.Boolean confirm_resign = 1;
  .chesscom.settings.v1.SettingValue.Boolean focus_mode = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_analysis = 3;
  .chesscom.settings.v1.SettingValue.String allow_challenges_from = 4;
  .chesscom.settings.v1.SettingValue.String allow_game_chat_with = 5;
  .chesscom.settings.v1.SettingValue.Integer challenge_min_rating = 6;
  .chesscom.settings.v1.SettingValue.Integer c
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07713"></a>
## FND-07713: chesscom.settings.v1.GameplaySetting.allow_challenges_from = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String allow_challenges_from = 4;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 340.

```text
tingValue.Boolean focus_mode = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_analysis = 3;
  .chesscom.settings.v1.SettingValue.String allow_challenges_from = 4;
  .chesscom.settings.v1.SettingValue.String allow_game_chat_with = 5;
  .chesscom.settings.v1.SettingValue.Integer challenge_min_rating = 6;
  .chesscom.settings.v1.SettingValue.Integer challenge_max_rating = 7;
  .chesscom.settings.v1.SettingValue.In
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07714"></a>
## FND-07714: chesscom.settings.v1.GameplaySetting.allow_game_chat_with = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String allow_game_chat_with = 5;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 411.

```text
Boolean auto_analysis = 3;
  .chesscom.settings.v1.SettingValue.String allow_challenges_from = 4;
  .chesscom.settings.v1.SettingValue.String allow_game_chat_with = 5;
  .chesscom.settings.v1.SettingValue.Integer challenge_min_rating = 6;
  .chesscom.settings.v1.SettingValue.Integer challenge_max_rating = 7;
  .chesscom.settings.v1.SettingValue.Integer seek_min_rating = 8;
  .chesscom.settings.v1.SettingValue.Integer
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07715"></a>
## FND-07715: chesscom.settings.v1.GameplaySetting.challenge_min_rating = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Integer challenge_min_rating = 6;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 481.

```text
 allow_challenges_from = 4;
  .chesscom.settings.v1.SettingValue.String allow_game_chat_with = 5;
  .chesscom.settings.v1.SettingValue.Integer challenge_min_rating = 6;
  .chesscom.settings.v1.SettingValue.Integer challenge_max_rating = 7;
  .chesscom.settings.v1.SettingValue.Integer seek_min_rating = 8;
  .chesscom.settings.v1.SettingValue.Integer seek_max_rating = 9;
  .chesscom.settings.v1.SettingValue.String seek
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07716"></a>
## FND-07716: chesscom.settings.v1.GameplaySetting.challenge_max_rating = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Integer challenge_max_rating = 7;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 552.

```text
 allow_game_chat_with = 5;
  .chesscom.settings.v1.SettingValue.Integer challenge_min_rating = 6;
  .chesscom.settings.v1.SettingValue.Integer challenge_max_rating = 7;
  .chesscom.settings.v1.SettingValue.Integer seek_min_rating = 8;
  .chesscom.settings.v1.SettingValue.Integer seek_max_rating = 9;
  .chesscom.settings.v1.SettingValue.String seek_game_type = 10;
  .chesscom.settings.v1.SettingValue.Boolean show_time
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07717"></a>
## FND-07717: chesscom.settings.v1.GameplaySetting.seek_min_rating = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Integer seek_min_rating = 8;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 623.

```text
 challenge_min_rating = 6;
  .chesscom.settings.v1.SettingValue.Integer challenge_max_rating = 7;
  .chesscom.settings.v1.SettingValue.Integer seek_min_rating = 8;
  .chesscom.settings.v1.SettingValue.Integer seek_max_rating = 9;
  .chesscom.settings.v1.SettingValue.String seek_game_type = 10;
  .chesscom.settings.v1.SettingValue.Boolean show_timestamps = 11;
  .chesscom.settings.v1.SettingValue.Boolean friends_can_c
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07718"></a>
## FND-07718: chesscom.settings.v1.GameplaySetting.seek_max_rating = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Integer seek_max_rating = 9;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 689.

```text
teger challenge_max_rating = 7;
  .chesscom.settings.v1.SettingValue.Integer seek_min_rating = 8;
  .chesscom.settings.v1.SettingValue.Integer seek_max_rating = 9;
  .chesscom.settings.v1.SettingValue.String seek_game_type = 10;
  .chesscom.settings.v1.SettingValue.Boolean show_timestamps = 11;
  .chesscom.settings.v1.SettingValue.Boolean friends_can_challenge_me_no_matter_what = 12;
  .chesscom.settings.v1.SettingVa
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07719"></a>
## FND-07719: chesscom.settings.v1.GameplaySetting.seek_game_type = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String seek_game_type = 10;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 755.

```text
ue.Integer seek_min_rating = 8;
  .chesscom.settings.v1.SettingValue.Integer seek_max_rating = 9;
  .chesscom.settings.v1.SettingValue.String seek_game_type = 10;
  .chesscom.settings.v1.SettingValue.Boolean show_timestamps = 11;
  .chesscom.settings.v1.SettingValue.Boolean friends_can_challenge_me_no_matter_what = 12;
  .chesscom.settings.v1.SettingValue.Boolean play_streaks = 13;
  .chesscom.settings.v1.SettingValu
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07720"></a>
## FND-07720: chesscom.settings.v1.GameplaySetting.show_timestamps = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_timestamps = 11;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 820.

```text
lue.Integer seek_max_rating = 9;
  .chesscom.settings.v1.SettingValue.String seek_game_type = 10;
  .chesscom.settings.v1.SettingValue.Boolean show_timestamps = 11;
  .chesscom.settings.v1.SettingValue.Boolean friends_can_challenge_me_no_matter_what = 12;
  .chesscom.settings.v1.SettingValue.Boolean play_streaks = 13;
  .chesscom.settings.v1.SettingValue.Boolean show_membership_badges = 14;
  .chesscom.settings.v1.Ga
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07721"></a>
## FND-07721: chesscom.settings.v1.GameplaySetting.friends_can_challenge_me_no_matter_what = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean friends_can_challenge_me_no_matter_what = 12;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 887.

```text
ue.String seek_game_type = 10;
  .chesscom.settings.v1.SettingValue.Boolean show_timestamps = 11;
  .chesscom.settings.v1.SettingValue.Boolean friends_can_challenge_me_no_matter_what = 12;
  .chesscom.settings.v1.SettingValue.Boolean play_streaks = 13;
  .chesscom.settings.v1.SettingValue.Boolean show_membership_badges = 14;
  .chesscom.settings.v1.GameplaySetting.GameplayLiveSetting live = 15;
  .chesscom.settings.v
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07722"></a>
## FND-07722: chesscom.settings.v1.GameplaySetting.play_streaks = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean play_streaks = 13;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 978.

```text
 = 11;
  .chesscom.settings.v1.SettingValue.Boolean friends_can_challenge_me_no_matter_what = 12;
  .chesscom.settings.v1.SettingValue.Boolean play_streaks = 13;
  .chesscom.settings.v1.SettingValue.Boolean show_membership_badges = 14;
  .chesscom.settings.v1.GameplaySetting.GameplayLiveSetting live = 15;
  .chesscom.settings.v1.GameplaySetting.GameplayDailySetting daily = 16;
  .chesscom.settings.v1.GameplaySetting.
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07723"></a>
## FND-07723: chesscom.settings.v1.GameplaySetting.show_membership_badges = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_membership_badges = 14;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1042.

```text
challenge_me_no_matter_what = 12;
  .chesscom.settings.v1.SettingValue.Boolean play_streaks = 13;
  .chesscom.settings.v1.SettingValue.Boolean show_membership_badges = 14;
  .chesscom.settings.v1.GameplaySetting.GameplayLiveSetting live = 15;
  .chesscom.settings.v1.GameplaySetting.GameplayDailySetting daily = 16;
  .chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting analysis = 17;
  .chesscom.settings.v1.S
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07724"></a>
## FND-07724: chesscom.settings.v1.GameplaySetting.live = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.GameplaySetting.GameplayLiveSetting live = 15;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1116.

```text
lean play_streaks = 13;
  .chesscom.settings.v1.SettingValue.Boolean show_membership_badges = 14;
  .chesscom.settings.v1.GameplaySetting.GameplayLiveSetting live = 15;
  .chesscom.settings.v1.GameplaySetting.GameplayDailySetting daily = 16;
  .chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting analysis = 17;
  .chesscom.settings.v1.SettingValue.Boolean show_my_membership_badge = 18;
  .chesscom.settings.v1
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07725"></a>
## FND-07725: chesscom.settings.v1.GameplaySetting.daily = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.GameplaySetting.GameplayDailySetting daily = 16;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1187.

```text
ow_membership_badges = 14;
  .chesscom.settings.v1.GameplaySetting.GameplayLiveSetting live = 15;
  .chesscom.settings.v1.GameplaySetting.GameplayDailySetting daily = 16;
  .chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting analysis = 17;
  .chesscom.settings.v1.SettingValue.Boolean show_my_membership_badge = 18;
  .chesscom.settings.v1.SettingValue.Boolean show_player_flair = 19;
  .chesscom.settings.v1.S
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07726"></a>
## FND-07726: chesscom.settings.v1.GameplaySetting.analysis = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting analysis = 17;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1260.

```text
ayLiveSetting live = 15;
  .chesscom.settings.v1.GameplaySetting.GameplayDailySetting daily = 16;
  .chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting analysis = 17;
  .chesscom.settings.v1.SettingValue.Boolean show_my_membership_badge = 18;
  .chesscom.settings.v1.SettingValue.Boolean show_player_flair = 19;
  .chesscom.settings.v1.SettingValue.String seek_time_class = 20;
  .chesscom.settings.v1.SettingV
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07727"></a>
## FND-07727: chesscom.settings.v1.GameplaySetting.show_my_membership_badge = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_my_membership_badge = 18;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1339.

```text
etting daily = 16;
  .chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting analysis = 17;
  .chesscom.settings.v1.SettingValue.Boolean show_my_membership_badge = 18;
  .chesscom.settings.v1.SettingValue.Boolean show_player_flair = 19;
  .chesscom.settings.v1.SettingValue.String seek_time_class = 20;
  .chesscom.settings.v1.SettingValue.Boolean voice_move = 21;
  .chesscom.settings.v1.SettingValue.Boolean auto
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07728"></a>
## FND-07728: chesscom.settings.v1.GameplaySetting.show_player_flair = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean show_player_flair = 19;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1415.

```text
etting analysis = 17;
  .chesscom.settings.v1.SettingValue.Boolean show_my_membership_badge = 18;
  .chesscom.settings.v1.SettingValue.Boolean show_player_flair = 19;
  .chesscom.settings.v1.SettingValue.String seek_time_class = 20;
  .chesscom.settings.v1.SettingValue.Boolean voice_move = 21;
  .chesscom.settings.v1.SettingValue.Boolean auto_save_bot_games = 22;
  }
  message GameplayLiveSetting {
    oneof value {

```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07729"></a>
## FND-07729: chesscom.settings.v1.GameplaySetting.seek_time_class = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String seek_time_class = 20;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1484.

```text
ow_my_membership_badge = 18;
  .chesscom.settings.v1.SettingValue.Boolean show_player_flair = 19;
  .chesscom.settings.v1.SettingValue.String seek_time_class = 20;
  .chesscom.settings.v1.SettingValue.Boolean voice_move = 21;
  .chesscom.settings.v1.SettingValue.Boolean auto_save_bot_games = 22;
  }
  message GameplayLiveSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean premoves = 1;
  .chessco
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07730"></a>
## FND-07730: chesscom.settings.v1.GameplaySetting.voice_move = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean voice_move = 21;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1550.

```text
Boolean show_player_flair = 19;
  .chesscom.settings.v1.SettingValue.String seek_time_class = 20;
  .chesscom.settings.v1.SettingValue.Boolean voice_move = 21;
  .chesscom.settings.v1.SettingValue.Boolean auto_save_bot_games = 22;
  }
  message GameplayLiveSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean premoves = 1;
  .chesscom.settings.v1.SettingValue.Boolean auto_promote_queen = 2;
  .ches
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07731"></a>
## FND-07731: chesscom.settings.v1.GameplaySetting.auto_save_bot_games = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean auto_save_bot_games = 22;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1612.

```text
gValue.String seek_time_class = 20;
  .chesscom.settings.v1.SettingValue.Boolean voice_move = 21;
  .chesscom.settings.v1.SettingValue.Boolean auto_save_bot_games = 22;
  }
  message GameplayLiveSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean premoves = 1;
  .chesscom.settings.v1.SettingValue.Boolean auto_promote_queen = 2;
  .chesscom.settings.v1.SettingValue.Boolean play_multiple_games = 3;
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07732"></a>
## FND-07732: message declaration: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameplayLiveSetting {

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1687.

```text
olean voice_move = 21;
  .chesscom.settings.v1.SettingValue.Boolean auto_save_bot_games = 22;
  }
  message GameplayLiveSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean premoves = 1;
  .chesscom.settings.v1.SettingValue.Boolean auto_promote_queen = 2;
  .chesscom.settings.v1.SettingValue.Boolean play_multiple_games = 3;
  .chesscom.settings.v1.SettingValue.Boolean auto_switch_game = 4;
  .ches
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07733"></a>
## FND-07733: oneof declaration: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 134.

```text
ttings_gameplay.proto
// syntax: proto3

package chesscom.settings.v1;

message GameplaySetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean confirm_resign = 1;
  .chesscom.settings.v1.SettingValue.Boolean focus_mode = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_analysis = 3;
  .chesscom.settings.v1.SettingValue.String allow_challenges_from = 4;
  .chesscom.settings.v1.SettingValue.String a
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07734"></a>
## FND-07734: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.premoves = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean premoves = 1;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1737.

```text
tingValue.Boolean auto_save_bot_games = 22;
  }
  message GameplayLiveSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean premoves = 1;
  .chesscom.settings.v1.SettingValue.Boolean auto_promote_queen = 2;
  .chesscom.settings.v1.SettingValue.Boolean play_multiple_games = 3;
  .chesscom.settings.v1.SettingValue.Boolean auto_switch_game = 4;
  .chesscom.settings.v1.SettingValue.Boolean auto_watch_t
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07735"></a>
## FND-07735: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.auto_promote_queen = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean auto_promote_queen = 2;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1796.

```text
ameplayLiveSetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.Boolean premoves = 1;
  .chesscom.settings.v1.SettingValue.Boolean auto_promote_queen = 2;
  .chesscom.settings.v1.SettingValue.Boolean play_multiple_games = 3;
  .chesscom.settings.v1.SettingValue.Boolean auto_switch_game = 4;
  .chesscom.settings.v1.SettingValue.Boolean auto_watch_top_game = 5;
  .chesscom.settings.v1.SettingValue.Boolean l
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07736"></a>
## FND-07736: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.play_multiple_games = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean play_multiple_games = 3;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1865.

```text
gValue.Boolean premoves = 1;
  .chesscom.settings.v1.SettingValue.Boolean auto_promote_queen = 2;
  .chesscom.settings.v1.SettingValue.Boolean play_multiple_games = 3;
  .chesscom.settings.v1.SettingValue.Boolean auto_switch_game = 4;
  .chesscom.settings.v1.SettingValue.Boolean auto_watch_top_game = 5;
  .chesscom.settings.v1.SettingValue.Boolean low_time_warning = 6;
  .chesscom.settings.v1.SettingValue.Boolean eng
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07737"></a>
## FND-07737: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.auto_switch_game = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean auto_switch_game = 4;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 1935.

```text
ean auto_promote_queen = 2;
  .chesscom.settings.v1.SettingValue.Boolean play_multiple_games = 3;
  .chesscom.settings.v1.SettingValue.Boolean auto_switch_game = 4;
  .chesscom.settings.v1.SettingValue.Boolean auto_watch_top_game = 5;
  .chesscom.settings.v1.SettingValue.Boolean low_time_warning = 6;
  .chesscom.settings.v1.SettingValue.Boolean engine_evaluation = 7;
  .chesscom.settings.v1.SettingValue.Boolean evalu
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07738"></a>
## FND-07738: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.auto_watch_top_game = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean auto_watch_top_game = 5;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2002.

```text
olean play_multiple_games = 3;
  .chesscom.settings.v1.SettingValue.Boolean auto_switch_game = 4;
  .chesscom.settings.v1.SettingValue.Boolean auto_watch_top_game = 5;
  .chesscom.settings.v1.SettingValue.Boolean low_time_warning = 6;
  .chesscom.settings.v1.SettingValue.Boolean engine_evaluation = 7;
  .chesscom.settings.v1.SettingValue.Boolean evaluation_bar = 8;
  .chesscom.settings.v1.SettingValue.Boolean allow_o
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07739"></a>
## FND-07739: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.low_time_warning = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean low_time_warning = 6;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2072.

```text
olean auto_switch_game = 4;
  .chesscom.settings.v1.SettingValue.Boolean auto_watch_top_game = 5;
  .chesscom.settings.v1.SettingValue.Boolean low_time_warning = 6;
  .chesscom.settings.v1.SettingValue.Boolean engine_evaluation = 7;
  .chesscom.settings.v1.SettingValue.Boolean evaluation_bar = 8;
  .chesscom.settings.v1.SettingValue.Boolean allow_offline_challenges = 9;
  .chesscom.settings.v1.SettingValue.String all
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07740"></a>
## FND-07740: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.engine_evaluation = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean engine_evaluation = 7;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2139.

```text
olean auto_watch_top_game = 5;
  .chesscom.settings.v1.SettingValue.Boolean low_time_warning = 6;
  .chesscom.settings.v1.SettingValue.Boolean engine_evaluation = 7;
  .chesscom.settings.v1.SettingValue.Boolean evaluation_bar = 8;
  .chesscom.settings.v1.SettingValue.Boolean allow_offline_challenges = 9;
  .chesscom.settings.v1.SettingValue.String allow_chat_requests_from = 10;
  .chesscom.settings.v1.SettingValue.St
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07741"></a>
## FND-07741: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.evaluation_bar = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean evaluation_bar = 8;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2207.

```text
Boolean low_time_warning = 6;
  .chesscom.settings.v1.SettingValue.Boolean engine_evaluation = 7;
  .chesscom.settings.v1.SettingValue.Boolean evaluation_bar = 8;
  .chesscom.settings.v1.SettingValue.Boolean allow_offline_challenges = 9;
  .chesscom.settings.v1.SettingValue.String allow_chat_requests_from = 10;
  .chesscom.settings.v1.SettingValue.String challenge_alerts = 11;
  .chesscom.settings.v1.SettingValue.Str
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07742"></a>
## FND-07742: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.allow_offline_challenges = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean allow_offline_challenges = 9;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2272.

```text
e.Boolean engine_evaluation = 7;
  .chesscom.settings.v1.SettingValue.Boolean evaluation_bar = 8;
  .chesscom.settings.v1.SettingValue.Boolean allow_offline_challenges = 9;
  .chesscom.settings.v1.SettingValue.String allow_chat_requests_from = 10;
  .chesscom.settings.v1.SettingValue.String challenge_alerts = 11;
  .chesscom.settings.v1.SettingValue.String friends_alerts = 12;
  .chesscom.settings.v1.SettingValue.Str
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07743"></a>
## FND-07743: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.allow_chat_requests_from = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String allow_chat_requests_from = 10;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2347.

```text
an evaluation_bar = 8;
  .chesscom.settings.v1.SettingValue.Boolean allow_offline_challenges = 9;
  .chesscom.settings.v1.SettingValue.String allow_chat_requests_from = 10;
  .chesscom.settings.v1.SettingValue.String challenge_alerts = 11;
  .chesscom.settings.v1.SettingValue.String friends_alerts = 12;
  .chesscom.settings.v1.SettingValue.String event_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean 
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07744"></a>
## FND-07744: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.challenge_alerts = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String challenge_alerts = 11;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2422.

```text
ffline_challenges = 9;
  .chesscom.settings.v1.SettingValue.String allow_chat_requests_from = 10;
  .chesscom.settings.v1.SettingValue.String challenge_alerts = 11;
  .chesscom.settings.v1.SettingValue.String friends_alerts = 12;
  .chesscom.settings.v1.SettingValue.String event_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean right_button_arrows = 14;
  .chesscom.settings.v1.SettingValue.Boolean seek
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07745"></a>
## FND-07745: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.friends_alerts = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String friends_alerts = 12;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2489.

```text
allow_chat_requests_from = 10;
  .chesscom.settings.v1.SettingValue.String challenge_alerts = 11;
  .chesscom.settings.v1.SettingValue.String friends_alerts = 12;
  .chesscom.settings.v1.SettingValue.String event_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean right_button_arrows = 14;
  .chesscom.settings.v1.SettingValue.Boolean seek_is_rated = 15;
  .chesscom.settings.v1.SettingValue.Integer seek_b
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07746"></a>
## FND-07746: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.event_announcements = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String event_announcements = 13;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2554.

```text
ue.String challenge_alerts = 11;
  .chesscom.settings.v1.SettingValue.String friends_alerts = 12;
  .chesscom.settings.v1.SettingValue.String event_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean right_button_arrows = 14;
  .chesscom.settings.v1.SettingValue.Boolean seek_is_rated = 15;
  .chesscom.settings.v1.SettingValue.Integer seek_base_time_chess = 16;
  .chesscom.settings.v1.SettingValue.Integer
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07747"></a>
## FND-07747: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.right_button_arrows = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean right_button_arrows = 14;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2624.

```text
String friends_alerts = 12;
  .chesscom.settings.v1.SettingValue.String event_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean right_button_arrows = 14;
  .chesscom.settings.v1.SettingValue.Boolean seek_is_rated = 15;
  .chesscom.settings.v1.SettingValue.Integer seek_base_time_chess = 16;
  .chesscom.settings.v1.SettingValue.Integer seek_increment_chess = 17;
  .chesscom.settings.v1.SettingValue.Integ
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07748"></a>
## FND-07748: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.seek_is_rated = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean seek_is_rated = 15;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2695.

```text
 event_announcements = 13;
  .chesscom.settings.v1.SettingValue.Boolean right_button_arrows = 14;
  .chesscom.settings.v1.SettingValue.Boolean seek_is_rated = 15;
  .chesscom.settings.v1.SettingValue.Integer seek_base_time_chess = 16;
  .chesscom.settings.v1.SettingValue.Integer seek_increment_chess = 17;
  .chesscom.settings.v1.SettingValue.Integer seek_base_time_variants = 18;
  .chesscom.settings.v1.SettingValue.I
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07749"></a>
## FND-07749: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.seek_base_time_chess = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Integer seek_base_time_chess = 16;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2760.

```text
oolean right_button_arrows = 14;
  .chesscom.settings.v1.SettingValue.Boolean seek_is_rated = 15;
  .chesscom.settings.v1.SettingValue.Integer seek_base_time_chess = 16;
  .chesscom.settings.v1.SettingValue.Integer seek_increment_chess = 17;
  .chesscom.settings.v1.SettingValue.Integer seek_base_time_variants = 18;
  .chesscom.settings.v1.SettingValue.Integer seek_increment_variants = 19;
  .chesscom.settings.v1.Sett
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07750"></a>
## FND-07750: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.seek_increment_chess = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Integer seek_increment_chess = 17;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2832.

```text
olean seek_is_rated = 15;
  .chesscom.settings.v1.SettingValue.Integer seek_base_time_chess = 16;
  .chesscom.settings.v1.SettingValue.Integer seek_increment_chess = 17;
  .chesscom.settings.v1.SettingValue.Integer seek_base_time_variants = 18;
  .chesscom.settings.v1.SettingValue.Integer seek_increment_variants = 19;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_hide_variants = 20;
  .chesscom.settings.v1
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07751"></a>
## FND-07751: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.seek_base_time_variants = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Integer seek_base_time_variants = 18;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2904.

```text
eek_base_time_chess = 16;
  .chesscom.settings.v1.SettingValue.Integer seek_increment_chess = 17;
  .chesscom.settings.v1.SettingValue.Integer seek_base_time_variants = 18;
  .chesscom.settings.v1.SettingValue.Integer seek_increment_variants = 19;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_hide_variants = 20;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_premium_only = 21;
  .chesscom.setting
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07752"></a>
## FND-07752: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.seek_increment_variants = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Integer seek_increment_variants = 19;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 2979.

```text
_increment_chess = 17;
  .chesscom.settings.v1.SettingValue.Integer seek_base_time_variants = 18;
  .chesscom.settings.v1.SettingValue.Integer seek_increment_variants = 19;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_hide_variants = 20;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_premium_only = 21;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_rated_only = 22;
  .chesscom.settings
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07753"></a>
## FND-07753: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.seek_filter_hide_variants = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean seek_filter_hide_variants = 20;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3054.

```text
se_time_variants = 18;
  .chesscom.settings.v1.SettingValue.Integer seek_increment_variants = 19;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_hide_variants = 20;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_premium_only = 21;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_rated_only = 22;
  .chesscom.settings.v1.SettingValue.Boolean hide_ratings_during_the_game = 23;
  .chesscom.set
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07754"></a>
## FND-07754: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.seek_filter_premium_only = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean seek_filter_premium_only = 21;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3131.

```text
ement_variants = 19;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_hide_variants = 20;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_premium_only = 21;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_rated_only = 22;
  .chesscom.settings.v1.SettingValue.Boolean hide_ratings_during_the_game = 23;
  .chesscom.settings.v1.SettingValue.String seek_time_class = 24;
  .chesscom.settings.v1.Se
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07755"></a>
## FND-07755: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.seek_filter_rated_only = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean seek_filter_rated_only = 22;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3207.

```text
r_hide_variants = 20;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_premium_only = 21;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_rated_only = 22;
  .chesscom.settings.v1.SettingValue.Boolean hide_ratings_during_the_game = 23;
  .chesscom.settings.v1.SettingValue.String seek_time_class = 24;
  .chesscom.settings.v1.SettingValue.Boolean confirm_move = 25;
    }
  }
  message GameplayDailySetti
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07756"></a>
## FND-07756: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.hide_ratings_during_the_game = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean hide_ratings_during_the_game = 23;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3281.

```text
lter_premium_only = 21;
  .chesscom.settings.v1.SettingValue.Boolean seek_filter_rated_only = 22;
  .chesscom.settings.v1.SettingValue.Boolean hide_ratings_during_the_game = 23;
  .chesscom.settings.v1.SettingValue.String seek_time_class = 24;
  .chesscom.settings.v1.SettingValue.Boolean confirm_move = 25;
    }
  }
  message GameplayDailySetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.String after_m
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07757"></a>
## FND-07757: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.seek_time_class = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String seek_time_class = 24;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3361.

```text
_rated_only = 22;
  .chesscom.settings.v1.SettingValue.Boolean hide_ratings_during_the_game = 23;
  .chesscom.settings.v1.SettingValue.String seek_time_class = 24;
  .chesscom.settings.v1.SettingValue.Boolean confirm_move = 25;
    }
  }
  message GameplayDailySetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.String after_moving = 1;
  .chesscom.settings.v1.SettingValue.Boolean confirm_move = 2;
  .che
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07758"></a>
## FND-07758: chesscom.settings.v1.GameplaySetting.GameplayLiveSetting.confirm_move = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean confirm_move = 25;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3427.

```text
e_ratings_during_the_game = 23;
  .chesscom.settings.v1.SettingValue.String seek_time_class = 24;
  .chesscom.settings.v1.SettingValue.Boolean confirm_move = 25;
    }
  }
  message GameplayDailySetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.String after_moving = 1;
  .chesscom.settings.v1.SettingValue.Boolean confirm_move = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_win_on_time = 3;
  .ch
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07759"></a>
## FND-07759: message declaration: chesscom.settings.v1.GameplaySetting.GameplayDailySetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameplayDailySetting {

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3501.

```text
g seek_time_class = 24;
  .chesscom.settings.v1.SettingValue.Boolean confirm_move = 25;
    }
  }
  message GameplayDailySetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.String after_moving = 1;
  .chesscom.settings.v1.SettingValue.Boolean confirm_move = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_win_on_time = 3;
  .chesscom.settings.v1.SettingValue.Integer max_game_count = 4;
  .chesscom.se
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07760"></a>
## FND-07760: oneof declaration: chesscom.settings.v1.GameplaySetting.GameplayDailySetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 134.

```text
ttings_gameplay.proto
// syntax: proto3

package chesscom.settings.v1;

message GameplaySetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean confirm_resign = 1;
  .chesscom.settings.v1.SettingValue.Boolean focus_mode = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_analysis = 3;
  .chesscom.settings.v1.SettingValue.String allow_challenges_from = 4;
  .chesscom.settings.v1.SettingValue.String a
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07761"></a>
## FND-07761: chesscom.settings.v1.GameplaySetting.GameplayDailySetting.after_moving = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.String after_moving = 1;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3552.

```text
tingValue.Boolean confirm_move = 25;
    }
  }
  message GameplayDailySetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.String after_moving = 1;
  .chesscom.settings.v1.SettingValue.Boolean confirm_move = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_win_on_time = 3;
  .chesscom.settings.v1.SettingValue.Integer max_game_count = 4;
  .chesscom.settings.v1.SettingValue.Integer min_days_per_move = 
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07762"></a>
## FND-07762: chesscom.settings.v1.GameplaySetting.GameplayDailySetting.confirm_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean confirm_move = 2;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3614.

```text
layDailySetting {
    oneof value {
  .chesscom.settings.v1.SettingValue.String after_moving = 1;
  .chesscom.settings.v1.SettingValue.Boolean confirm_move = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_win_on_time = 3;
  .chesscom.settings.v1.SettingValue.Integer max_game_count = 4;
  .chesscom.settings.v1.SettingValue.Integer min_days_per_move = 5;
  .chesscom.settings.v1.SettingValue.Integer max_days_per_m
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07763"></a>
## FND-07763: chesscom.settings.v1.GameplaySetting.GameplayDailySetting.auto_win_on_time = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean auto_win_on_time = 3;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3677.

```text
tingValue.String after_moving = 1;
  .chesscom.settings.v1.SettingValue.Boolean confirm_move = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_win_on_time = 3;
  .chesscom.settings.v1.SettingValue.Integer max_game_count = 4;
  .chesscom.settings.v1.SettingValue.Integer min_days_per_move = 5;
  .chesscom.settings.v1.SettingValue.Integer max_days_per_move = 6;
  .chesscom.settings.v1.SettingValue.Integer seek_days
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07764"></a>
## FND-07764: chesscom.settings.v1.GameplaySetting.GameplayDailySetting.max_game_count = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Integer max_game_count = 4;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3744.

```text
alue.Boolean confirm_move = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_win_on_time = 3;
  .chesscom.settings.v1.SettingValue.Integer max_game_count = 4;
  .chesscom.settings.v1.SettingValue.Integer min_days_per_move = 5;
  .chesscom.settings.v1.SettingValue.Integer max_days_per_move = 6;
  .chesscom.settings.v1.SettingValue.Integer seek_days_per_move = 7;
    }
  }
  message GameplayAnalysisSetting {
    on
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07765"></a>
## FND-07765: chesscom.settings.v1.GameplaySetting.GameplayDailySetting.min_days_per_move = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Integer min_days_per_move = 5;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3809.

```text
ue.Boolean auto_win_on_time = 3;
  .chesscom.settings.v1.SettingValue.Integer max_game_count = 4;
  .chesscom.settings.v1.SettingValue.Integer min_days_per_move = 5;
  .chesscom.settings.v1.SettingValue.Integer max_days_per_move = 6;
  .chesscom.settings.v1.SettingValue.Integer seek_days_per_move = 7;
    }
  }
  message GameplayAnalysisSetting {
    oneof value {
  .chesscom.settings.v1.GameplaySetting.GameplayAnaly
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07766"></a>
## FND-07766: chesscom.settings.v1.GameplaySetting.GameplayDailySetting.max_days_per_move = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Integer max_days_per_move = 6;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3877.

```text
e.Integer max_game_count = 4;
  .chesscom.settings.v1.SettingValue.Integer min_days_per_move = 5;
  .chesscom.settings.v1.SettingValue.Integer max_days_per_move = 6;
  .chesscom.settings.v1.SettingValue.Integer seek_days_per_move = 7;
    }
  }
  message GameplayAnalysisSetting {
    oneof value {
  .chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting.EvaluationBarMode evaluation_bar_mode = 1;
    }
    mess
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07767"></a>
## FND-07767: chesscom.settings.v1.GameplaySetting.GameplayDailySetting.seek_days_per_move = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Integer seek_days_per_move = 7;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 3945.

```text
nteger min_days_per_move = 5;
  .chesscom.settings.v1.SettingValue.Integer max_days_per_move = 6;
  .chesscom.settings.v1.SettingValue.Integer seek_days_per_move = 7;
    }
  }
  message GameplayAnalysisSetting {
    oneof value {
  .chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting.EvaluationBarMode evaluation_bar_mode = 1;
    }
    message EvaluationBarMode {
      oneof value {
  .chesscom.settings.v1.
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07768"></a>
## FND-07768: message declaration: chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameplayAnalysisSetting {

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 4024.

```text
days_per_move = 6;
  .chesscom.settings.v1.SettingValue.Integer seek_days_per_move = 7;
    }
  }
  message GameplayAnalysisSetting {
    oneof value {
  .chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting.EvaluationBarMode evaluation_bar_mode = 1;
    }
    message EvaluationBarMode {
      oneof value {
  .chesscom.settings.v1.SettingValue.Boolean wdl_for_openings = 1;
  .chesscom.settings.v1.SettingValue
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07769"></a>
## FND-07769: oneof declaration: chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 134.

```text
ttings_gameplay.proto
// syntax: proto3

package chesscom.settings.v1;

message GameplaySetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean confirm_resign = 1;
  .chesscom.settings.v1.SettingValue.Boolean focus_mode = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_analysis = 3;
  .chesscom.settings.v1.SettingValue.String allow_challenges_from = 4;
  .chesscom.settings.v1.SettingValue.String a
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07770"></a>
## FND-07770: chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting.evaluation_bar_mode = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting.EvaluationBarMode evaluation_bar_mode = 1;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 4078.

```text
e.Integer seek_days_per_move = 7;
    }
  }
  message GameplayAnalysisSetting {
    oneof value {
  .chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting.EvaluationBarMode evaluation_bar_mode = 1;
    }
    message EvaluationBarMode {
      oneof value {
  .chesscom.settings.v1.SettingValue.Boolean wdl_for_openings = 1;
  .chesscom.settings.v1.SettingValue.Boolean tablebase_in_endgame = 2;
      }
    }
  }
}
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07771"></a>
## FND-07771: message declaration: chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting.EvaluationBarMode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EvaluationBarMode {

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 4193.

```text
ngs.v1.GameplaySetting.GameplayAnalysisSetting.EvaluationBarMode evaluation_bar_mode = 1;
    }
    message EvaluationBarMode {
      oneof value {
  .chesscom.settings.v1.SettingValue.Boolean wdl_for_openings = 1;
  .chesscom.settings.v1.SettingValue.Boolean tablebase_in_endgame = 2;
      }
    }
  }
}

```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07772"></a>
## FND-07772: oneof declaration: chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting.EvaluationBarMode.value

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof value {

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 134.

```text
ttings_gameplay.proto
// syntax: proto3

package chesscom.settings.v1;

message GameplaySetting {
  oneof value {
  .chesscom.settings.v1.SettingValue.Boolean confirm_resign = 1;
  .chesscom.settings.v1.SettingValue.Boolean focus_mode = 2;
  .chesscom.settings.v1.SettingValue.Boolean auto_analysis = 3;
  .chesscom.settings.v1.SettingValue.String allow_challenges_from = 4;
  .chesscom.settings.v1.SettingValue.String a
```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07773"></a>
## FND-07773: chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting.EvaluationBarMode.wdl_for_openings = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean wdl_for_openings = 1;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 4243.

```text
luationBarMode evaluation_bar_mode = 1;
    }
    message EvaluationBarMode {
      oneof value {
  .chesscom.settings.v1.SettingValue.Boolean wdl_for_openings = 1;
  .chesscom.settings.v1.SettingValue.Boolean tablebase_in_endgame = 2;
      }
    }
  }
}

```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07774"></a>
## FND-07774: chesscom.settings.v1.GameplaySetting.GameplayAnalysisSetting.EvaluationBarMode.tablebase_in_endgame = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.settings.v1.SettingValue.Boolean tablebase_in_endgame = 2;

### Evidence

- **SRC-0531** `research/proto/chesscom/settings/v1/settings_gameplay.proto` — [preserved redacted evidence](../evidence/text/ffd004eadeb45f8f961f7c0c8f907e69673ac4f3fc0a6a6621042c32dd4d7f4b.proto)
  Character offset 4310.

```text
nBarMode {
      oneof value {
  .chesscom.settings.v1.SettingValue.Boolean wdl_for_openings = 1;
  .chesscom.settings.v1.SettingValue.Boolean tablebase_in_endgame = 2;
      }
    }
  }
}

```

**Source references:** SRC-0531, SRC-1502  
**URL references:** None independently associated  
**Related findings:** FND-07708, FND-07709, FND-07710

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
