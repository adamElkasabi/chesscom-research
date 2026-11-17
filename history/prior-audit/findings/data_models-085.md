# data_models — findings 8401–8500

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-08675"></a>
## FND-08675: message declaration: chesscom.themes.v2.BoardStyle

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BoardStyle {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 1656.

```text
}
  optional string url = 1;
  }
  message PlainColorStyle {
  optional string hex_code = 1;
  }
}

message BoardStyle {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  repeated .chesscom.api.v1.Platform supported_platforms = 7;
  optional .chesscom.unloc
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08676"></a>
## FND-08676: oneof declaration: chesscom.themes.v2.BoardStyle._legacy_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _legacy_id {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 107.

```text
ce: chesscom/themes/v2/core.proto
// syntax: proto3

package chesscom.themes.v2;

message Theme {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chessco
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08677"></a>
## FND-08677: chesscom.themes.v2.BoardStyle.legacy_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 legacy_id = 4;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 128.

```text
2/core.proto
// syntax: proto3

package chesscom.themes.v2;

message Theme {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyl
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08678"></a>
## FND-08678: chesscom.themes.v2.BoardStyle.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 155.

```text
to3

package chesscom.themes.v2;

message Theme {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optio
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08679"></a>
## FND-08679: chesscom.themes.v2.BoardStyle.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 181.

```text
es.v2;

message Theme {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optional .chesscom.themes.v2.Pi
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08680"></a>
## FND-08680: chesscom.themes.v2.BoardStyle.is_default = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_default = 3;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 209.

```text
eof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optional .chesscom.themes.v2.PieceSet piece_set = 13;
  opt
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08681"></a>
## FND-08681: chesscom.themes.v2.BoardStyle.localized_name = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string localized_name = 5;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 241.

```text
id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optional .chesscom.themes.v2.PieceSet piece_set = 13;
  optional .chesscom.themes.v2.SoundS
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08682"></a>
## FND-08682: chesscom.themes.v2.BoardStyle.display_priority = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 display_priority = 6;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 279.

```text
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optional .chesscom.themes.v2.PieceSet piece_set = 13;
  optional .chesscom.themes.v2.SoundSet sound_set = 14;
  optional bool is_
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08683"></a>
## FND-08683: chesscom.themes.v2.BoardStyle.supported_platforms = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.api.v1.Platform supported_platforms = 7;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 1256.

```text
bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  repeated .chesscom.api.v1.Platform supported_platforms = 7;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 8;
  optional string preview_image = 11;
  message ImageStyle {
    oneof _fallback_color {
  .chesscom.themes.v2.Background.PlainColorStyle fallback_color = 2;
    }
  optional string 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08684"></a>
## FND-08684: chesscom.themes.v2.BoardStyle.unlockable_preview = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 8;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 1318.

```text
ptional int32 display_priority = 6;
  repeated .chesscom.api.v1.Platform supported_platforms = 7;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 8;
  optional string preview_image = 11;
  message ImageStyle {
    oneof _fallback_color {
  .chesscom.themes.v2.Background.PlainColorStyle fallback_color = 2;
    }
  optional string url = 1;
  }
  message PlainColorStyle {
  optional string hex
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08685"></a>
## FND-08685: chesscom.themes.v2.BoardStyle.preview_image = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.BoardStyle.PreviewImage preview_image = 11;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2030.

```text
rted_platforms = 7;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 8;
  optional .chesscom.themes.v2.BoardStyle.PreviewImage preview_image = 11;
  optional string image = 12;
  optional .chesscom.themes.v2.BoardStyle.ThreeDimensionalImage image_3d = 13;
  optional string coordinate_color_dark = 14;
  optional string coordinate_color_light = 15;
  optional string highlight_color = 16;
  opt
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08686"></a>
## FND-08686: chesscom.themes.v2.BoardStyle.image = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string image = 12;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2105.

```text
nlockable_preview = 8;
  optional .chesscom.themes.v2.BoardStyle.PreviewImage preview_image = 11;
  optional string image = 12;
  optional .chesscom.themes.v2.BoardStyle.ThreeDimensionalImage image_3d = 13;
  optional string coordinate_color_dark = 14;
  optional string coordinate_color_light = 15;
  optional string highlight_color = 16;
  optional string category_id = 17;
  message PreviewImage {
  optional string s
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08687"></a>
## FND-08687: chesscom.themes.v2.BoardStyle.image_3d = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.BoardStyle.ThreeDimensionalImage image_3d = 13;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2135.

```text
nal .chesscom.themes.v2.BoardStyle.PreviewImage preview_image = 11;
  optional string image = 12;
  optional .chesscom.themes.v2.BoardStyle.ThreeDimensionalImage image_3d = 13;
  optional string coordinate_color_dark = 14;
  optional string coordinate_color_light = 15;
  optional string highlight_color = 16;
  optional string category_id = 17;
  message PreviewImage {
  optional string square = 1;
  optional string l
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08688"></a>
## FND-08688: chesscom.themes.v2.BoardStyle.coordinate_color_dark = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coordinate_color_dark = 14;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2214.

```text
string image = 12;
  optional .chesscom.themes.v2.BoardStyle.ThreeDimensionalImage image_3d = 13;
  optional string coordinate_color_dark = 14;
  optional string coordinate_color_light = 15;
  optional string highlight_color = 16;
  optional string category_id = 17;
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message ThreeDimensionalImage {
  optional string board = 1;
 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08689"></a>
## FND-08689: chesscom.themes.v2.BoardStyle.coordinate_color_light = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coordinate_color_light = 15;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2260.

```text
.v2.BoardStyle.ThreeDimensionalImage image_3d = 13;
  optional string coordinate_color_dark = 14;
  optional string coordinate_color_light = 15;
  optional string highlight_color = 16;
  optional string category_id = 17;
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message ThreeDimensionalImage {
  optional string board = 1;
  optional string coordinates = 2;
  }
}

messa
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08690"></a>
## FND-08690: chesscom.themes.v2.BoardStyle.highlight_color = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string highlight_color = 16;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2307.

```text
 13;
  optional string coordinate_color_dark = 14;
  optional string coordinate_color_light = 15;
  optional string highlight_color = 16;
  optional string category_id = 17;
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message ThreeDimensionalImage {
  optional string board = 1;
  optional string coordinates = 2;
  }
}

message PieceSet {
  oneof _legacy_id {
  int32 lega
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08691"></a>
## FND-08691: chesscom.themes.v2.BoardStyle.category_id = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string category_id = 17;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2347.

```text
dark = 14;
  optional string coordinate_color_light = 15;
  optional string highlight_color = 16;
  optional string category_id = 17;
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message ThreeDimensionalImage {
  optional string board = 1;
  optional string coordinates = 2;
  }
}

message PieceSet {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08692"></a>
## FND-08692: message declaration: chesscom.themes.v2.BoardStyle.PreviewImage

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PreviewImage {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2383.

```text
ate_color_light = 15;
  optional string highlight_color = 16;
  optional string category_id = 17;
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message ThreeDimensionalImage {
  optional string board = 1;
  optional string coordinates = 2;
  }
}

message PieceSet {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optio
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08693"></a>
## FND-08693: chesscom.themes.v2.BoardStyle.PreviewImage.square = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string square = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2408.

```text
ptional string highlight_color = 16;
  optional string category_id = 17;
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message ThreeDimensionalImage {
  optional string board = 1;
  optional string coordinates = 2;
  }
}

message PieceSet {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;

```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08694"></a>
## FND-08694: chesscom.themes.v2.BoardStyle.PreviewImage.linear = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string linear = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2438.

```text
 = 16;
  optional string category_id = 17;
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message ThreeDimensionalImage {
  optional string board = 1;
  optional string coordinates = 2;
  }
}

message PieceSet {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_na
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08695"></a>
## FND-08695: message declaration: chesscom.themes.v2.BoardStyle.ThreeDimensionalImage

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ThreeDimensionalImage {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2472.

```text
id = 17;
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message ThreeDimensionalImage {
  optional string board = 1;
  optional string coordinates = 2;
  }
}

message PieceSet {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_p
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08696"></a>
## FND-08696: chesscom.themes.v2.BoardStyle.ThreeDimensionalImage.board = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string board = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2506.

```text
  optional string square = 1;
  optional string linear = 2;
  }
  message ThreeDimensionalImage {
  optional string board = 1;
  optional string coordinates = 2;
  }
}

message PieceSet {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  repeated .chesscom.
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08697"></a>
## FND-08697: chesscom.themes.v2.BoardStyle.ThreeDimensionalImage.coordinates = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string coordinates = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2535.

```text

  optional string linear = 2;
  }
  message ThreeDimensionalImage {
  optional string board = 1;
  optional string coordinates = 2;
  }
}

message PieceSet {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  repeated .chesscom.api.v1.Platform supported_pla
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08698"></a>
## FND-08698: message declaration: chesscom.themes.v2.PieceSet

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PieceSet {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2575.

```text
sage ThreeDimensionalImage {
  optional string board = 1;
  optional string coordinates = 2;
  }
}

message PieceSet {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  repeated .chesscom.api.v1.Platform supported_platforms = 7;
  optional .chesscom.unlocka
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08699"></a>
## FND-08699: oneof declaration: chesscom.themes.v2.PieceSet._legacy_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _legacy_id {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 107.

```text
ce: chesscom/themes/v2/core.proto
// syntax: proto3

package chesscom.themes.v2;

message Theme {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chessco
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08700"></a>
## FND-08700: chesscom.themes.v2.PieceSet.legacy_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 legacy_id = 4;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 128.

```text
2/core.proto
// syntax: proto3

package chesscom.themes.v2;

message Theme {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyl
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08701"></a>
## FND-08701: chesscom.themes.v2.PieceSet.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 155.

```text
to3

package chesscom.themes.v2;

message Theme {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optio
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08702"></a>
## FND-08702: chesscom.themes.v2.PieceSet.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 181.

```text
es.v2;

message Theme {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optional .chesscom.themes.v2.Pi
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08703"></a>
## FND-08703: chesscom.themes.v2.PieceSet.is_default = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_default = 3;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 209.

```text
eof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optional .chesscom.themes.v2.PieceSet piece_set = 13;
  opt
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08704"></a>
## FND-08704: chesscom.themes.v2.PieceSet.localized_name = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string localized_name = 5;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 241.

```text
id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optional .chesscom.themes.v2.PieceSet piece_set = 13;
  optional .chesscom.themes.v2.SoundS
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08705"></a>
## FND-08705: chesscom.themes.v2.PieceSet.display_priority = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 display_priority = 6;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 279.

```text
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optional .chesscom.themes.v2.PieceSet piece_set = 13;
  optional .chesscom.themes.v2.SoundSet sound_set = 14;
  optional bool is_
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08706"></a>
## FND-08706: chesscom.themes.v2.PieceSet.supported_platforms = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.api.v1.Platform supported_platforms = 7;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 1256.

```text
bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  repeated .chesscom.api.v1.Platform supported_platforms = 7;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 8;
  optional string preview_image = 11;
  message ImageStyle {
    oneof _fallback_color {
  .chesscom.themes.v2.Background.PlainColorStyle fallback_color = 2;
    }
  optional string 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08707"></a>
## FND-08707: chesscom.themes.v2.PieceSet.unlockable_preview = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 8;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 1318.

```text
ptional int32 display_priority = 6;
  repeated .chesscom.api.v1.Platform supported_platforms = 7;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 8;
  optional string preview_image = 11;
  message ImageStyle {
    oneof _fallback_color {
  .chesscom.themes.v2.Background.PlainColorStyle fallback_color = 2;
    }
  optional string url = 1;
  }
  message PlainColorStyle {
  optional string hex
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08708"></a>
## FND-08708: chesscom.themes.v2.PieceSet.preview_image = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.PieceSet.PreviewImage preview_image = 11;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2947.

```text
rted_platforms = 7;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 8;
  optional .chesscom.themes.v2.PieceSet.PreviewImage preview_image = 11;
  optional .chesscom.themes.v2.PieceSet.Images images = 12;
  optional .chesscom.themes.v2.PieceSet.PiecePerspective perspective = 13;
  optional string category_id = 14;
  enum PiecePerspective {
    PIECE_PERSPECTIVE_UNSPECIFIED = 0;
    PIECE_PER
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08709"></a>
## FND-08709: chesscom.themes.v2.PieceSet.images = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.PieceSet.Images images = 12;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3020.

```text
 unlockable_preview = 8;
  optional .chesscom.themes.v2.PieceSet.PreviewImage preview_image = 11;
  optional .chesscom.themes.v2.PieceSet.Images images = 12;
  optional .chesscom.themes.v2.PieceSet.PiecePerspective perspective = 13;
  optional string category_id = 14;
  enum PiecePerspective {
    PIECE_PERSPECTIVE_UNSPECIFIED = 0;
    PIECE_PERSPECTIVE_TOP_DOWN = 1;
    PIECE_PERSPECTIVE_PSEUDO_3D = 2;
    PIECE_PER
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08710"></a>
## FND-08710: chesscom.themes.v2.PieceSet.perspective = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.PieceSet.PiecePerspective perspective = 13;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3080.

```text
eSet.PreviewImage preview_image = 11;
  optional .chesscom.themes.v2.PieceSet.Images images = 12;
  optional .chesscom.themes.v2.PieceSet.PiecePerspective perspective = 13;
  optional string category_id = 14;
  enum PiecePerspective {
    PIECE_PERSPECTIVE_UNSPECIFIED = 0;
    PIECE_PERSPECTIVE_TOP_DOWN = 1;
    PIECE_PERSPECTIVE_PSEUDO_3D = 2;
    PIECE_PERSPECTIVE_REAL_3D = 3;
  }
  message PreviewImage {
  optiona
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08711"></a>
## FND-08711: chesscom.themes.v2.PieceSet.category_id = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string category_id = 14;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3155.

```text
et.Images images = 12;
  optional .chesscom.themes.v2.PieceSet.PiecePerspective perspective = 13;
  optional string category_id = 14;
  enum PiecePerspective {
    PIECE_PERSPECTIVE_UNSPECIFIED = 0;
    PIECE_PERSPECTIVE_TOP_DOWN = 1;
    PIECE_PERSPECTIVE_PSEUDO_3D = 2;
    PIECE_PERSPECTIVE_REAL_3D = 3;
  }
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message Images {
 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08712"></a>
## FND-08712: enum declaration: chesscom.themes.v2.PieceSet.PiecePerspective

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PiecePerspective {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3191.

```text
hesscom.themes.v2.PieceSet.PiecePerspective perspective = 13;
  optional string category_id = 14;
  enum PiecePerspective {
    PIECE_PERSPECTIVE_UNSPECIFIED = 0;
    PIECE_PERSPECTIVE_TOP_DOWN = 1;
    PIECE_PERSPECTIVE_PSEUDO_3D = 2;
    PIECE_PERSPECTIVE_REAL_3D = 3;
  }
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message Images {
  optional string white_pawn = 1;
  o
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08713"></a>
## FND-08713: chesscom.themes.v2.PieceSet.PiecePerspective.PIECE_PERSPECTIVE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PIECE_PERSPECTIVE_UNSPECIFIED = 0;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3219.

```text
iecePerspective perspective = 13;
  optional string category_id = 14;
  enum PiecePerspective {
    PIECE_PERSPECTIVE_UNSPECIFIED = 0;
    PIECE_PERSPECTIVE_TOP_DOWN = 1;
    PIECE_PERSPECTIVE_PSEUDO_3D = 2;
    PIECE_PERSPECTIVE_REAL_3D = 3;
  }
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message Images {
  optional string white_pawn = 1;
  optional string white_knight 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08714"></a>
## FND-08714: chesscom.themes.v2.PieceSet.PiecePerspective.PIECE_PERSPECTIVE_TOP_DOWN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PIECE_PERSPECTIVE_TOP_DOWN = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3258.

```text
ional string category_id = 14;
  enum PiecePerspective {
    PIECE_PERSPECTIVE_UNSPECIFIED = 0;
    PIECE_PERSPECTIVE_TOP_DOWN = 1;
    PIECE_PERSPECTIVE_PSEUDO_3D = 2;
    PIECE_PERSPECTIVE_REAL_3D = 3;
  }
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message Images {
  optional string white_pawn = 1;
  optional string white_knight = 2;
  optional string white_bishop = 3
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08715"></a>
## FND-08715: chesscom.themes.v2.PieceSet.PiecePerspective.PIECE_PERSPECTIVE_PSEUDO_3D = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PIECE_PERSPECTIVE_PSEUDO_3D = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3294.

```text
m PiecePerspective {
    PIECE_PERSPECTIVE_UNSPECIFIED = 0;
    PIECE_PERSPECTIVE_TOP_DOWN = 1;
    PIECE_PERSPECTIVE_PSEUDO_3D = 2;
    PIECE_PERSPECTIVE_REAL_3D = 3;
  }
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message Images {
  optional string white_pawn = 1;
  optional string white_knight = 2;
  optional string white_bishop = 3;
  optional string white_rook = 4;

```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08716"></a>
## FND-08716: chesscom.themes.v2.PieceSet.PiecePerspective.PIECE_PERSPECTIVE_REAL_3D = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PIECE_PERSPECTIVE_REAL_3D = 3;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3331.

```text
CTIVE_UNSPECIFIED = 0;
    PIECE_PERSPECTIVE_TOP_DOWN = 1;
    PIECE_PERSPECTIVE_PSEUDO_3D = 2;
    PIECE_PERSPECTIVE_REAL_3D = 3;
  }
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message Images {
  optional string white_pawn = 1;
  optional string white_knight = 2;
  optional string white_bishop = 3;
  optional string white_rook = 4;
  optional string white_queen = 5;
  
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08717"></a>
## FND-08717: message declaration: chesscom.themes.v2.PieceSet.PreviewImage

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PreviewImage {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2383.

```text
ate_color_light = 15;
  optional string highlight_color = 16;
  optional string category_id = 17;
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message ThreeDimensionalImage {
  optional string board = 1;
  optional string coordinates = 2;
  }
}

message PieceSet {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optio
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08718"></a>
## FND-08718: chesscom.themes.v2.PieceSet.PreviewImage.square = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string square = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2408.

```text
ptional string highlight_color = 16;
  optional string category_id = 17;
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message ThreeDimensionalImage {
  optional string board = 1;
  optional string coordinates = 2;
  }
}

message PieceSet {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;

```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08719"></a>
## FND-08719: chesscom.themes.v2.PieceSet.PreviewImage.linear = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string linear = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 2438.

```text
 = 16;
  optional string category_id = 17;
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message ThreeDimensionalImage {
  optional string board = 1;
  optional string coordinates = 2;
  }
}

message PieceSet {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_na
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08720"></a>
## FND-08720: message declaration: chesscom.themes.v2.PieceSet.Images

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Images {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3457.

```text
= 3;
  }
  message PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message Images {
  optional string white_pawn = 1;
  optional string white_knight = 2;
  optional string white_bishop = 3;
  optional string white_rook = 4;
  optional string white_queen = 5;
  optional string white_king = 6;
  optional string black_pawn = 7;
  optional string black_knight = 8;
  optional string black_
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08721"></a>
## FND-08721: chesscom.themes.v2.PieceSet.Images.white_pawn = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string white_pawn = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3476.

```text
PreviewImage {
  optional string square = 1;
  optional string linear = 2;
  }
  message Images {
  optional string white_pawn = 1;
  optional string white_knight = 2;
  optional string white_bishop = 3;
  optional string white_rook = 4;
  optional string white_queen = 5;
  optional string white_king = 6;
  optional string black_pawn = 7;
  optional string black_knight = 8;
  optional string black_bishop = 9;
  optio
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08722"></a>
## FND-08722: chesscom.themes.v2.PieceSet.Images.white_knight = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string white_knight = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3510.

```text
quare = 1;
  optional string linear = 2;
  }
  message Images {
  optional string white_pawn = 1;
  optional string white_knight = 2;
  optional string white_bishop = 3;
  optional string white_rook = 4;
  optional string white_queen = 5;
  optional string white_king = 6;
  optional string black_pawn = 7;
  optional string black_knight = 8;
  optional string black_bishop = 9;
  optional string black_rook = 10;
  opti
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08723"></a>
## FND-08723: chesscom.themes.v2.PieceSet.Images.white_bishop = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string white_bishop = 3;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3546.

```text
= 2;
  }
  message Images {
  optional string white_pawn = 1;
  optional string white_knight = 2;
  optional string white_bishop = 3;
  optional string white_rook = 4;
  optional string white_queen = 5;
  optional string white_king = 6;
  optional string black_pawn = 7;
  optional string black_knight = 8;
  optional string black_bishop = 9;
  optional string black_rook = 10;
  optional string black_queen = 11;
  opti
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08724"></a>
## FND-08724: chesscom.themes.v2.PieceSet.Images.white_rook = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string white_rook = 4;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3582.

```text
al string white_pawn = 1;
  optional string white_knight = 2;
  optional string white_bishop = 3;
  optional string white_rook = 4;
  optional string white_queen = 5;
  optional string white_king = 6;
  optional string black_pawn = 7;
  optional string black_knight = 8;
  optional string black_bishop = 9;
  optional string black_rook = 10;
  optional string black_queen = 11;
  optional string black_king = 12;
  }
}


```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08725"></a>
## FND-08725: chesscom.themes.v2.PieceSet.Images.white_queen = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string white_queen = 5;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3616.

```text
al string white_knight = 2;
  optional string white_bishop = 3;
  optional string white_rook = 4;
  optional string white_queen = 5;
  optional string white_king = 6;
  optional string black_pawn = 7;
  optional string black_knight = 8;
  optional string black_bishop = 9;
  optional string black_rook = 10;
  optional string black_queen = 11;
  optional string black_king = 12;
  }
}

message SoundSet {
  oneof sounds 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08726"></a>
## FND-08726: chesscom.themes.v2.PieceSet.Images.white_king = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string white_king = 6;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3651.

```text
nal string white_bishop = 3;
  optional string white_rook = 4;
  optional string white_queen = 5;
  optional string white_king = 6;
  optional string black_pawn = 7;
  optional string black_knight = 8;
  optional string black_bishop = 9;
  optional string black_rook = 10;
  optional string black_queen = 11;
  optional string black_king = 12;
  }
}

message SoundSet {
  oneof sounds {
  .chesscom.themes.v2.SoundSet.So
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08727"></a>
## FND-08727: chesscom.themes.v2.PieceSet.Images.black_pawn = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string black_pawn = 7;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3685.

```text
ional string white_rook = 4;
  optional string white_queen = 5;
  optional string white_king = 6;
  optional string black_pawn = 7;
  optional string black_knight = 8;
  optional string black_bishop = 9;
  optional string black_rook = 10;
  optional string black_queen = 11;
  optional string black_king = 12;
  }
}

message SoundSet {
  oneof sounds {
  .chesscom.themes.v2.SoundSet.SoundArchives sound_archives = 11;
 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08728"></a>
## FND-08728: chesscom.themes.v2.PieceSet.Images.black_knight = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string black_knight = 8;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3719.

```text
ional string white_queen = 5;
  optional string white_king = 6;
  optional string black_pawn = 7;
  optional string black_knight = 8;
  optional string black_bishop = 9;
  optional string black_rook = 10;
  optional string black_queen = 11;
  optional string black_king = 12;
  }
}

message SoundSet {
  oneof sounds {
  .chesscom.themes.v2.SoundSet.SoundArchives sound_archives = 11;
  .chesscom.themes.v2.SoundSet.Soun
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08729"></a>
## FND-08729: chesscom.themes.v2.PieceSet.Images.black_bishop = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string black_bishop = 9;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3755.

```text
onal string white_king = 6;
  optional string black_pawn = 7;
  optional string black_knight = 8;
  optional string black_bishop = 9;
  optional string black_rook = 10;
  optional string black_queen = 11;
  optional string black_king = 12;
  }
}

message SoundSet {
  oneof sounds {
  .chesscom.themes.v2.SoundSet.SoundArchives sound_archives = 11;
  .chesscom.themes.v2.SoundSet.SoundFiles sound_files = 12;
  }
  oneof
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08730"></a>
## FND-08730: chesscom.themes.v2.PieceSet.Images.black_rook = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string black_rook = 10;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3791.

```text
al string black_pawn = 7;
  optional string black_knight = 8;
  optional string black_bishop = 9;
  optional string black_rook = 10;
  optional string black_queen = 11;
  optional string black_king = 12;
  }
}

message SoundSet {
  oneof sounds {
  .chesscom.themes.v2.SoundSet.SoundArchives sound_archives = 11;
  .chesscom.themes.v2.SoundSet.SoundFiles sound_files = 12;
  }
  oneof _legacy_id {
  int32 legacy_id = 4;
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08731"></a>
## FND-08731: chesscom.themes.v2.PieceSet.Images.black_queen = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string black_queen = 11;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3826.

```text
l string black_knight = 8;
  optional string black_bishop = 9;
  optional string black_rook = 10;
  optional string black_queen = 11;
  optional string black_king = 12;
  }
}

message SoundSet {
  oneof sounds {
  .chesscom.themes.v2.SoundSet.SoundArchives sound_archives = 11;
  .chesscom.themes.v2.SoundSet.SoundFiles sound_files = 12;
  }
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  op
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08732"></a>
## FND-08732: chesscom.themes.v2.PieceSet.Images.black_king = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string black_king = 12;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3862.

```text
l string black_bishop = 9;
  optional string black_rook = 10;
  optional string black_queen = 11;
  optional string black_king = 12;
  }
}

message SoundSet {
  oneof sounds {
  .chesscom.themes.v2.SoundSet.SoundArchives sound_archives = 11;
  .chesscom.themes.v2.SoundSet.SoundFiles sound_files = 12;
  }
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional b
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08733"></a>
## FND-08733: message declaration: chesscom.themes.v2.SoundSet

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SoundSet {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3902.

```text
ring black_rook = 10;
  optional string black_queen = 11;
  optional string black_king = 12;
  }
}

message SoundSet {
  oneof sounds {
  .chesscom.themes.v2.SoundSet.SoundArchives sound_archives = 11;
  .chesscom.themes.v2.SoundSet.SoundFiles sound_files = 12;
  }
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string lo
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08734"></a>
## FND-08734: oneof declaration: chesscom.themes.v2.SoundSet.sounds

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof sounds {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3923.

```text

  optional string black_queen = 11;
  optional string black_king = 12;
  }
}

message SoundSet {
  oneof sounds {
  .chesscom.themes.v2.SoundSet.SoundArchives sound_archives = 11;
  .chesscom.themes.v2.SoundSet.SoundFiles sound_files = 12;
  }
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  o
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08735"></a>
## FND-08735: chesscom.themes.v2.SoundSet.sound_archives = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.themes.v2.SoundSet.SoundArchives sound_archives = 11;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 3940.

```text
g black_queen = 11;
  optional string black_king = 12;
  }
}

message SoundSet {
  oneof sounds {
  .chesscom.themes.v2.SoundSet.SoundArchives sound_archives = 11;
  .chesscom.themes.v2.SoundSet.SoundFiles sound_files = 12;
  }
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 dis
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08736"></a>
## FND-08736: chesscom.themes.v2.SoundSet.sound_files = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.themes.v2.SoundSet.SoundFiles sound_files = 12;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4006.

```text
age SoundSet {
  oneof sounds {
  .chesscom.themes.v2.SoundSet.SoundArchives sound_archives = 11;
  .chesscom.themes.v2.SoundSet.SoundFiles sound_files = 12;
  }
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  repeated .chesscom.api.v1.Platform supported_
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08737"></a>
## FND-08737: oneof declaration: chesscom.themes.v2.SoundSet._legacy_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _legacy_id {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 107.

```text
ce: chesscom/themes/v2/core.proto
// syntax: proto3

package chesscom.themes.v2;

message Theme {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chessco
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08738"></a>
## FND-08738: chesscom.themes.v2.SoundSet.legacy_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 legacy_id = 4;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 128.

```text
2/core.proto
// syntax: proto3

package chesscom.themes.v2;

message Theme {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyl
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08739"></a>
## FND-08739: chesscom.themes.v2.SoundSet.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 155.

```text
to3

package chesscom.themes.v2;

message Theme {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optio
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08740"></a>
## FND-08740: chesscom.themes.v2.SoundSet.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 181.

```text
es.v2;

message Theme {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optional .chesscom.themes.v2.Pi
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08741"></a>
## FND-08741: chesscom.themes.v2.SoundSet.is_default = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_default = 3;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 209.

```text
eof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optional .chesscom.themes.v2.PieceSet piece_set = 13;
  opt
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08742"></a>
## FND-08742: chesscom.themes.v2.SoundSet.localized_name = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string localized_name = 5;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 241.

```text
id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optional .chesscom.themes.v2.PieceSet piece_set = 13;
  optional .chesscom.themes.v2.SoundS
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08743"></a>
## FND-08743: chesscom.themes.v2.SoundSet.display_priority = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 display_priority = 6;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 279.

```text
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chesscom.themes.v2.BoardStyle board_style = 12;
  optional .chesscom.themes.v2.PieceSet piece_set = 13;
  optional .chesscom.themes.v2.SoundSet sound_set = 14;
  optional bool is_
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08744"></a>
## FND-08744: chesscom.themes.v2.SoundSet.supported_platforms = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.api.v1.Platform supported_platforms = 7;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 1256.

```text
bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  repeated .chesscom.api.v1.Platform supported_platforms = 7;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 8;
  optional string preview_image = 11;
  message ImageStyle {
    oneof _fallback_color {
  .chesscom.themes.v2.Background.PlainColorStyle fallback_color = 2;
    }
  optional string 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08745"></a>
## FND-08745: chesscom.themes.v2.SoundSet.unlockable_preview = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 8;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 1318.

```text
ptional int32 display_priority = 6;
  repeated .chesscom.api.v1.Platform supported_platforms = 7;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 8;
  optional string preview_image = 11;
  message ImageStyle {
    oneof _fallback_color {
  .chesscom.themes.v2.Background.PlainColorStyle fallback_color = 2;
    }
  optional string url = 1;
  }
  message PlainColorStyle {
  optional string hex
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08746"></a>
## FND-08746: chesscom.themes.v2.SoundSet.category_id = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string category_id = 13;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4421.

```text
rted_platforms = 7;
  optional .chesscom.unlockables.v1.UnlockablePreview unlockable_preview = 8;
  optional string category_id = 13;
  message SoundArchives {
  optional string mp3 = 1;
  optional string ogg = 2;
  optional string wav = 3;
  optional string webm = 4;
  }
  message SoundFiles {
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry mp3 = 1;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.OggE
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08747"></a>
## FND-08747: message declaration: chesscom.themes.v2.SoundSet.SoundArchives

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SoundArchives {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4457.

```text
scom.unlockables.v1.UnlockablePreview unlockable_preview = 8;
  optional string category_id = 13;
  message SoundArchives {
  optional string mp3 = 1;
  optional string ogg = 2;
  optional string wav = 3;
  optional string webm = 4;
  }
  message SoundFiles {
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry mp3 = 1;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.OggEntry ogg = 2;
  repeated .chesscom.t
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08748"></a>
## FND-08748: chesscom.themes.v2.SoundSet.SoundArchives.mp3 = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string mp3 = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4483.

```text
ablePreview unlockable_preview = 8;
  optional string category_id = 13;
  message SoundArchives {
  optional string mp3 = 1;
  optional string ogg = 2;
  optional string wav = 3;
  optional string webm = 4;
  }
  message SoundFiles {
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry mp3 = 1;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.OggEntry ogg = 2;
  repeated .chesscom.themes.v2.SoundSet.SoundFil
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08749"></a>
## FND-08749: chesscom.themes.v2.SoundSet.SoundArchives.ogg = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string ogg = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4510.

```text
iew = 8;
  optional string category_id = 13;
  message SoundArchives {
  optional string mp3 = 1;
  optional string ogg = 2;
  optional string wav = 3;
  optional string webm = 4;
  }
  message SoundFiles {
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry mp3 = 1;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.OggEntry ogg = 2;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WavEntry wav = 3;
  repe
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08750"></a>
## FND-08750: chesscom.themes.v2.SoundSet.SoundArchives.wav = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string wav = 3;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4537.

```text
category_id = 13;
  message SoundArchives {
  optional string mp3 = 1;
  optional string ogg = 2;
  optional string wav = 3;
  optional string webm = 4;
  }
  message SoundFiles {
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry mp3 = 1;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.OggEntry ogg = 2;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WavEntry wav = 3;
  repeated .chesscom.themes.v2.So
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08751"></a>
## FND-08751: chesscom.themes.v2.SoundSet.SoundArchives.webm = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string webm = 4;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4564.

```text
 SoundArchives {
  optional string mp3 = 1;
  optional string ogg = 2;
  optional string wav = 3;
  optional string webm = 4;
  }
  message SoundFiles {
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry mp3 = 1;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.OggEntry ogg = 2;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WavEntry wav = 3;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08752"></a>
## FND-08752: message declaration: chesscom.themes.v2.SoundSet.SoundFiles

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SoundFiles {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4596.

```text
ng mp3 = 1;
  optional string ogg = 2;
  optional string wav = 3;
  optional string webm = 4;
  }
  message SoundFiles {
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry mp3 = 1;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.OggEntry ogg = 2;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WavEntry wav = 3;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08753"></a>
## FND-08753: chesscom.themes.v2.SoundSet.SoundFiles.mp3 = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry mp3 = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4619.

```text
string ogg = 2;
  optional string wav = 3;
  optional string webm = 4;
  }
  message SoundFiles {
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry mp3 = 1;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.OggEntry ogg = 2;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WavEntry wav = 3;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry {
  optional string key
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08754"></a>
## FND-08754: chesscom.themes.v2.SoundSet.SoundFiles.ogg = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.SoundSet.SoundFiles.OggEntry ogg = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4688.

```text
;
  }
  message SoundFiles {
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry mp3 = 1;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.OggEntry ogg = 2;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WavEntry wav = 3;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry {
  optional string key = 1;
  optional string value = 2;
    }
    message OggEntry {
  opt
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08755"></a>
## FND-08755: chesscom.themes.v2.SoundSet.SoundFiles.wav = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.SoundSet.SoundFiles.WavEntry wav = 3;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4757.

```text
SoundFiles.Mp3Entry mp3 = 1;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.OggEntry ogg = 2;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WavEntry wav = 3;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry {
  optional string key = 1;
  optional string value = 2;
    }
    message OggEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08756"></a>
## FND-08756: chesscom.themes.v2.SoundSet.SoundFiles.webm = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4826.

```text
SoundFiles.OggEntry ogg = 2;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WavEntry wav = 3;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry {
  optional string key = 1;
  optional string value = 2;
    }
    message OggEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WavEntry {
  optional string key = 1;
  optional string value = 2;
  
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08757"></a>
## FND-08757: message declaration: chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Mp3Entry {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4899.

```text
dFiles.WavEntry wav = 3;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry {
  optional string key = 1;
  optional string value = 2;
    }
    message OggEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WavEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WebmEntry {
  optional string key = 1;
  optional string 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08758"></a>
## FND-08758: chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4920.

```text
 3;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry {
  optional string key = 1;
  optional string value = 2;
    }
    message OggEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WavEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WebmEntry {
  optional string key = 1;
  optional string value = 2;
    }
  }

```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08759"></a>
## FND-08759: chesscom.themes.v2.SoundSet.SoundFiles.Mp3Entry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4947.

```text
emes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry {
  optional string key = 1;
  optional string value = 2;
    }
    message OggEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WavEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WebmEntry {
  optional string key = 1;
  optional string value = 2;
    }
  }
}

message Attributes {
  o
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08760"></a>
## FND-08760: message declaration: chesscom.themes.v2.SoundSet.SoundFiles.OggEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message OggEntry {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4984.

```text
 webm = 4;
    message Mp3Entry {
  optional string key = 1;
  optional string value = 2;
    }
    message OggEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WavEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WebmEntry {
  optional string key = 1;
  optional string value = 2;
    }
  }
}

message Attributes {
  oneof _legacy_id {
  int32 legacy_id =
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08761"></a>
## FND-08761: chesscom.themes.v2.SoundSet.SoundFiles.OggEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4920.

```text
 3;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry {
  optional string key = 1;
  optional string value = 2;
    }
    message OggEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WavEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WebmEntry {
  optional string key = 1;
  optional string value = 2;
    }
  }

```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08762"></a>
## FND-08762: chesscom.themes.v2.SoundSet.SoundFiles.OggEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4947.

```text
emes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry {
  optional string key = 1;
  optional string value = 2;
    }
    message OggEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WavEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WebmEntry {
  optional string key = 1;
  optional string value = 2;
    }
  }
}

message Attributes {
  o
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08763"></a>
## FND-08763: message declaration: chesscom.themes.v2.SoundSet.SoundFiles.WavEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message WavEntry {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5069.

```text
= 2;
    }
    message OggEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WavEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WebmEntry {
  optional string key = 1;
  optional string value = 2;
    }
  }
}

message Attributes {
  oneof _legacy_id {
  int32 legacy_id = 3;
  }
  optional string name = 1;
  optional bool is_default = 2;
  optional string
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08764"></a>
## FND-08764: chesscom.themes.v2.SoundSet.SoundFiles.WavEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4920.

```text
 3;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry {
  optional string key = 1;
  optional string value = 2;
    }
    message OggEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WavEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WebmEntry {
  optional string key = 1;
  optional string value = 2;
    }
  }

```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08765"></a>
## FND-08765: chesscom.themes.v2.SoundSet.SoundFiles.WavEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4947.

```text
emes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry {
  optional string key = 1;
  optional string value = 2;
    }
    message OggEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WavEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WebmEntry {
  optional string key = 1;
  optional string value = 2;
    }
  }
}

message Attributes {
  o
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08766"></a>
## FND-08766: message declaration: chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message WebmEntry {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5154.

```text
= 2;
    }
    message WavEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WebmEntry {
  optional string key = 1;
  optional string value = 2;
    }
  }
}

message Attributes {
  oneof _legacy_id {
  int32 legacy_id = 3;
  }
  optional string name = 1;
  optional bool is_default = 2;
  optional string localized_name = 4;
  optional int32 display_priority = 5;
}

message ThemeElementCa
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08767"></a>
## FND-08767: chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4920.

```text
 3;
  repeated .chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry {
  optional string key = 1;
  optional string value = 2;
    }
    message OggEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WavEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WebmEntry {
  optional string key = 1;
  optional string value = 2;
    }
  }

```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08768"></a>
## FND-08768: chesscom.themes.v2.SoundSet.SoundFiles.WebmEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string value = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 4947.

```text
emes.v2.SoundSet.SoundFiles.WebmEntry webm = 4;
    message Mp3Entry {
  optional string key = 1;
  optional string value = 2;
    }
    message OggEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WavEntry {
  optional string key = 1;
  optional string value = 2;
    }
    message WebmEntry {
  optional string key = 1;
  optional string value = 2;
    }
  }
}

message Attributes {
  o
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08769"></a>
## FND-08769: message declaration: chesscom.themes.v2.Attributes

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Attributes {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5243.

```text

    }
    message WebmEntry {
  optional string key = 1;
  optional string value = 2;
    }
  }
}

message Attributes {
  oneof _legacy_id {
  int32 legacy_id = 3;
  }
  optional string name = 1;
  optional bool is_default = 2;
  optional string localized_name = 4;
  optional int32 display_priority = 5;
}

message ThemeElementCategory {
  optional string id = 1;
  optional string localized_name = 2;
  optional int32
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08770"></a>
## FND-08770: oneof declaration: chesscom.themes.v2.Attributes._legacy_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _legacy_id {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 107.

```text
ce: chesscom/themes/v2/core.proto
// syntax: proto3

package chesscom.themes.v2;

message Theme {
  oneof _legacy_id {
  int32 legacy_id = 4;
  }
  optional string id = 1;
  optional string name = 2;
  optional bool is_default = 3;
  optional string localized_name = 5;
  optional int32 display_priority = 6;
  optional bool onboarding = 10;
  optional .chesscom.themes.v2.Background background = 11;
  optional .chessco
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08771"></a>
## FND-08771: chesscom.themes.v2.Attributes.legacy_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 legacy_id = 3;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5287.

```text
ring key = 1;
  optional string value = 2;
    }
  }
}

message Attributes {
  oneof _legacy_id {
  int32 legacy_id = 3;
  }
  optional string name = 1;
  optional bool is_default = 2;
  optional string localized_name = 4;
  optional int32 display_priority = 5;
}

message ThemeElementCategory {
  optional string id = 1;
  optional string localized_name = 2;
  optional int32 display_priority = 3;
}

message ThemeId {

```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08772"></a>
## FND-08772: chesscom.themes.v2.Attributes.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5314.

```text
ring value = 2;
    }
  }
}

message Attributes {
  oneof _legacy_id {
  int32 legacy_id = 3;
  }
  optional string name = 1;
  optional bool is_default = 2;
  optional string localized_name = 4;
  optional int32 display_priority = 5;
}

message ThemeElementCategory {
  optional string id = 1;
  optional string localized_name = 2;
  optional int32 display_priority = 3;
}

message ThemeId {
  oneof id {
  string prese
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08773"></a>
## FND-08773: chesscom.themes.v2.Attributes.is_default = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_default = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5342.

```text

message Attributes {
  oneof _legacy_id {
  int32 legacy_id = 3;
  }
  optional string name = 1;
  optional bool is_default = 2;
  optional string localized_name = 4;
  optional int32 display_priority = 5;
}

message ThemeElementCategory {
  optional string id = 1;
  optional string localized_name = 2;
  optional int32 display_priority = 3;
}

message ThemeId {
  oneof id {
  string preset = 1;
  .chesscom.themes.v2
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08774"></a>
## FND-08774: chesscom.themes.v2.Attributes.localized_name = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string localized_name = 4;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5374.

```text
egacy_id {
  int32 legacy_id = 3;
  }
  optional string name = 1;
  optional bool is_default = 2;
  optional string localized_name = 4;
  optional int32 display_priority = 5;
}

message ThemeElementCategory {
  optional string id = 1;
  optional string localized_name = 2;
  optional int32 display_priority = 3;
}

message ThemeId {
  oneof id {
  string preset = 1;
  .chesscom.themes.v2.ThemeElementIds custom = 2;
  }
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
