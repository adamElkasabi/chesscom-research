# data_models — findings 8501–8600

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-08775"></a>
## FND-08775: chesscom.themes.v2.Attributes.display_priority = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 display_priority = 5;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5412.

```text
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
}

message ThemeElementIds {
  option
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08776"></a>
## FND-08776: message declaration: chesscom.themes.v2.ThemeElementCategory

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ThemeElementCategory {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5452.

```text
ool is_default = 2;
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
}

message ThemeElementIds {
  optional string background_id = 1;
  optional 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08777"></a>
## FND-08777: chesscom.themes.v2.ThemeElementCategory.id = 1

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

<a id="FND-08778"></a>
## FND-08778: chesscom.themes.v2.ThemeElementCategory.localized_name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string localized_name = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5511.

```text
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
}

message ThemeElementIds {
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id =
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08779"></a>
## FND-08779: chesscom.themes.v2.ThemeElementCategory.display_priority = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 display_priority = 3;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5549.

```text
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
}

message ThemeElementIds {
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08780"></a>
## FND-08780: message declaration: chesscom.themes.v2.ThemeId

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ThemeId {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5589.

```text
onal string id = 1;
  optional string localized_name = 2;
  optional int32 display_priority = 3;
}

message ThemeId {
  oneof id {
  string preset = 1;
  .chesscom.themes.v2.ThemeElementIds custom = 2;
  }
}

message ThemeElementIds {
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  opti
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08781"></a>
## FND-08781: oneof declaration: chesscom.themes.v2.ThemeId.id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof id {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5609.

```text
  optional string localized_name = 2;
  optional int32 display_priority = 3;
}

message ThemeId {
  oneof id {
  string preset = 1;
  .chesscom.themes.v2.ThemeElementIds custom = 2;
  }
}

message ThemeElementIds {
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.theme
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08782"></a>
## FND-08782: chesscom.themes.v2.ThemeId.preset = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string preset = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5622.

```text
ring localized_name = 2;
  optional int32 display_priority = 3;
}

message ThemeId {
  oneof id {
  string preset = 1;
  .chesscom.themes.v2.ThemeElementIds custom = 2;
  }
}

message ThemeElementIds {
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTh
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08783"></a>
## FND-08783: chesscom.themes.v2.ThemeId.custom = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.themes.v2.ThemeElementIds custom = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5643.

```text
 2;
  optional int32 display_priority = 3;
}

message ThemeId {
  oneof id {
  string preset = 1;
  .chesscom.themes.v2.ThemeElementIds custom = 2;
  }
}

message ThemeElementIds {
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  opti
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08784"></a>
## FND-08784: message declaration: chesscom.themes.v2.ThemeElementIds

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ThemeElementIds {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5698.

```text
hemeId {
  oneof id {
  string preset = 1;
  .chesscom.themes.v2.ThemeElementIds custom = 2;
  }
}

message ThemeElementIds {
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelecti
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08785"></a>
## FND-08785: chesscom.themes.v2.ThemeElementIds.background_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string background_id = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5726.

```text
ng preset = 1;
  .chesscom.themes.v2.ThemeElementIds custom = 2;
  }
}

message ThemeElementIds {
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chessco
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08786"></a>
## FND-08786: chesscom.themes.v2.ThemeElementIds.board_style_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string board_style_id = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5763.

```text
ThemeElementIds custom = 2;
  }
}

message ThemeElementIds {
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08787"></a>
## FND-08787: chesscom.themes.v2.ThemeElementIds.piece_set_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string piece_set_id = 3;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5801.

```text
sage ThemeElementIds {
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}


```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08788"></a>
## FND-08788: chesscom.themes.v2.ThemeElementIds.sound_set_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string sound_set_id = 4;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5837.

```text
ring background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}

message BoardStyleSelectionItem {
  
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08789"></a>
## FND-08789: message declaration: chesscom.themes.v2.ThemeSelectionItem

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ThemeSelectionItem {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5874.

```text
ring board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}

message BoardStyleSelectionItem {
  optional .chesscom.themes.v2.BoardSty
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08790"></a>
## FND-08790: chesscom.themes.v2.ThemeSelectionItem.theme = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.PresetTheme theme = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5905.

```text
onal string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}

message BoardStyleSelectionItem {
  optional .chesscom.themes.v2.BoardStyle board_style = 1;
  optional 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08791"></a>
## FND-08791: chesscom.themes.v2.ThemeSelectionItem.is_unlocked = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_unlocked = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5959.

```text
set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}

message BoardStyleSelectionItem {
  optional .chesscom.themes.v2.BoardStyle board_style = 1;
  optional bool is_unlocked = 2;
}

message PieceSetSelectionItem
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08792"></a>
## FND-08792: message declaration: chesscom.themes.v2.BackgroundSelectionItem

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BackgroundSelectionItem {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5993.

```text
ionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}

message BoardStyleSelectionItem {
  optional .chesscom.themes.v2.BoardStyle board_style = 1;
  optional bool is_unlocked = 2;
}

message PieceSetSelectionItem {
  optional .chesscom.themes.v2.
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08793"></a>
## FND-08793: chesscom.themes.v2.BackgroundSelectionItem.background = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.Background background = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 6029.

```text
s.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}

message BoardStyleSelectionItem {
  optional .chesscom.themes.v2.BoardStyle board_style = 1;
  optional bool is_unlocked = 2;
}

message PieceSetSelectionItem {
  optional .chesscom.themes.v2.PieceSet piece_set = 1;
  optional b
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08794"></a>
## FND-08794: chesscom.themes.v2.BackgroundSelectionItem.is_unlocked = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_unlocked = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5959.

```text
set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}

message BoardStyleSelectionItem {
  optional .chesscom.themes.v2.BoardStyle board_style = 1;
  optional bool is_unlocked = 2;
}

message PieceSetSelectionItem
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08795"></a>
## FND-08795: message declaration: chesscom.themes.v2.BoardStyleSelectionItem

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BoardStyleSelectionItem {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 6121.

```text
tem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}

message BoardStyleSelectionItem {
  optional .chesscom.themes.v2.BoardStyle board_style = 1;
  optional bool is_unlocked = 2;
}

message PieceSetSelectionItem {
  optional .chesscom.themes.v2.PieceSet piece_set = 1;
  optional bool is_unlocked = 2;
}

message SoundSetSelectionItem {
  optional .chesscom.themes.v2.Sound
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08796"></a>
## FND-08796: chesscom.themes.v2.BoardStyleSelectionItem.board_style = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.BoardStyle board_style = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 6157.

```text
.Background background = 1;
  optional bool is_unlocked = 2;
}

message BoardStyleSelectionItem {
  optional .chesscom.themes.v2.BoardStyle board_style = 1;
  optional bool is_unlocked = 2;
}

message PieceSetSelectionItem {
  optional .chesscom.themes.v2.PieceSet piece_set = 1;
  optional bool is_unlocked = 2;
}

message SoundSetSelectionItem {
  optional .chesscom.themes.v2.SoundSet sound_set = 1;
  optional bool i
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08797"></a>
## FND-08797: chesscom.themes.v2.BoardStyleSelectionItem.is_unlocked = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_unlocked = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5959.

```text
set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}

message BoardStyleSelectionItem {
  optional .chesscom.themes.v2.BoardStyle board_style = 1;
  optional bool is_unlocked = 2;
}

message PieceSetSelectionItem
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08798"></a>
## FND-08798: message declaration: chesscom.themes.v2.PieceSetSelectionItem

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PieceSetSelectionItem {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 6250.

```text
em {
  optional .chesscom.themes.v2.BoardStyle board_style = 1;
  optional bool is_unlocked = 2;
}

message PieceSetSelectionItem {
  optional .chesscom.themes.v2.PieceSet piece_set = 1;
  optional bool is_unlocked = 2;
}

message SoundSetSelectionItem {
  optional .chesscom.themes.v2.SoundSet sound_set = 1;
  optional bool is_unlocked = 2;
}

message ThemeSelection {
  oneof _theme_id {
  string theme_id = 16;
  }
 
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08799"></a>
## FND-08799: chesscom.themes.v2.PieceSetSelectionItem.piece_set = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.PieceSet piece_set = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 6284.

```text
2.BoardStyle board_style = 1;
  optional bool is_unlocked = 2;
}

message PieceSetSelectionItem {
  optional .chesscom.themes.v2.PieceSet piece_set = 1;
  optional bool is_unlocked = 2;
}

message SoundSetSelectionItem {
  optional .chesscom.themes.v2.SoundSet sound_set = 1;
  optional bool is_unlocked = 2;
}

message ThemeSelection {
  oneof _theme_id {
  string theme_id = 16;
  }
  optional string background_id = 1
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08800"></a>
## FND-08800: chesscom.themes.v2.PieceSetSelectionItem.is_unlocked = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_unlocked = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5959.

```text
set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}

message BoardStyleSelectionItem {
  optional .chesscom.themes.v2.BoardStyle board_style = 1;
  optional bool is_unlocked = 2;
}

message PieceSetSelectionItem
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08801"></a>
## FND-08801: message declaration: chesscom.themes.v2.SoundSetSelectionItem

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SoundSetSelectionItem {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 6373.

```text
onItem {
  optional .chesscom.themes.v2.PieceSet piece_set = 1;
  optional bool is_unlocked = 2;
}

message SoundSetSelectionItem {
  optional .chesscom.themes.v2.SoundSet sound_set = 1;
  optional bool is_unlocked = 2;
}

message ThemeSelection {
  oneof _theme_id {
  string theme_id = 16;
  }
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional st
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08802"></a>
## FND-08802: chesscom.themes.v2.SoundSetSelectionItem.sound_set = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.SoundSet sound_set = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 6407.

```text
es.v2.PieceSet piece_set = 1;
  optional bool is_unlocked = 2;
}

message SoundSetSelectionItem {
  optional .chesscom.themes.v2.SoundSet sound_set = 1;
  optional bool is_unlocked = 2;
}

message ThemeSelection {
  oneof _theme_id {
  string theme_id = 16;
  }
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08803"></a>
## FND-08803: chesscom.themes.v2.SoundSetSelectionItem.is_unlocked = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_unlocked = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5959.

```text
set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}

message BoardStyleSelectionItem {
  optional .chesscom.themes.v2.BoardStyle board_style = 1;
  optional bool is_unlocked = 2;
}

message PieceSetSelectionItem
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08804"></a>
## FND-08804: message declaration: chesscom.themes.v2.ThemeSelection

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ThemeSelection {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 6496.

```text
onItem {
  optional .chesscom.themes.v2.SoundSet sound_set = 1;
  optional bool is_unlocked = 2;
}

message ThemeSelection {
  oneof _theme_id {
  string theme_id = 16;
  }
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08805"></a>
## FND-08805: oneof declaration: chesscom.themes.v2.ThemeSelection._theme_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _theme_id {

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 6523.

```text
om.themes.v2.SoundSet sound_set = 1;
  optional bool is_unlocked = 2;
}

message ThemeSelection {
  oneof _theme_id {
  string theme_id = 16;
  }
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08806"></a>
## FND-08806: chesscom.themes.v2.ThemeSelection.theme_id = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string theme_id = 16;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 6543.

```text
t sound_set = 1;
  optional bool is_unlocked = 2;
}

message ThemeSelection {
  oneof _theme_id {
  string theme_id = 16;
  }
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08807"></a>
## FND-08807: chesscom.themes.v2.ThemeSelection.background_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string background_id = 1;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5726.

```text
ng preset = 1;
  .chesscom.themes.v2.ThemeElementIds custom = 2;
  }
}

message ThemeElementIds {
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chessco
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08808"></a>
## FND-08808: chesscom.themes.v2.ThemeSelection.board_style_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string board_style_id = 2;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5763.

```text
ThemeElementIds custom = 2;
  }
}

message ThemeElementIds {
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08809"></a>
## FND-08809: chesscom.themes.v2.ThemeSelection.piece_set_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string piece_set_id = 3;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5801.

```text
sage ThemeElementIds {
  optional string background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}


```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08810"></a>
## FND-08810: chesscom.themes.v2.ThemeSelection.sound_set_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string sound_set_id = 4;

### Evidence

- **SRC-0568** `research/proto/chesscom/themes/v2/core.proto` — [preserved redacted evidence](../evidence/text/7b8debe860ba6e3c3dcfe625172e246fc49870d314ce13eaf987241db750b76b.proto)
  Character offset 5837.

```text
ring background_id = 1;
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
}

message ThemeSelectionItem {
  optional .chesscom.themes.v2.PresetTheme theme = 1;
  optional bool is_unlocked = 2;
}

message BackgroundSelectionItem {
  optional .chesscom.themes.v2.Background background = 1;
  optional bool is_unlocked = 2;
}

message BoardStyleSelectionItem {
  
```

**Source references:** SRC-0568, SRC-1539  
**URL references:** None independently associated  
**Related findings:** FND-08635, FND-08636, FND-08637

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08811"></a>
## FND-08811: enum declaration: chesscom.themes.v2.Platform

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Platform {

### Evidence

- **SRC-0569** `research/proto/chesscom/themes/v2/platform.proto` — [preserved redacted evidence](../evidence/text/1f92148d5fc706c6d69ef79efa557c6e7ded60e57a2c0b0554359cdcfe173616.proto)
  Character offset 93.

```text
// source: chesscom/themes/v2/platform.proto
// syntax: proto3

package chesscom.themes.v2;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_WEB = 1;
  PLATFORM_ANDROID = 2;
  PLATFORM_IPHONE = 3;
}

```

**Source references:** SRC-0569, SRC-1540  
**URL references:** None independently associated  
**Related findings:** FND-08812, FND-08813

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08812"></a>
## FND-08812: chesscom.themes.v2.Platform.PLATFORM_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_UNSPECIFIED = 0;

### Evidence

- **SRC-0569** `research/proto/chesscom/themes/v2/platform.proto` — [preserved redacted evidence](../evidence/text/1f92148d5fc706c6d69ef79efa557c6e7ded60e57a2c0b0554359cdcfe173616.proto)
  Character offset 111.

```text
chesscom/themes/v2/platform.proto
// syntax: proto3

package chesscom.themes.v2;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_WEB = 1;
  PLATFORM_ANDROID = 2;
  PLATFORM_IPHONE = 3;
}

```

**Source references:** SRC-0569, SRC-1540  
**URL references:** None independently associated  
**Related findings:** FND-08811, FND-08813

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08813"></a>
## FND-08813: chesscom.themes.v2.Platform.PLATFORM_WEB = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_WEB = 1;

### Evidence

- **SRC-0569** `research/proto/chesscom/themes/v2/platform.proto` — [preserved redacted evidence](../evidence/text/1f92148d5fc706c6d69ef79efa557c6e7ded60e57a2c0b0554359cdcfe173616.proto)
  Character offset 139.

```text
proto
// syntax: proto3

package chesscom.themes.v2;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_WEB = 1;
  PLATFORM_ANDROID = 2;
  PLATFORM_IPHONE = 3;
}

```

**Source references:** SRC-0569, SRC-1540  
**URL references:** None independently associated  
**Related findings:** FND-08811, FND-08812

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08814"></a>
## FND-08814: chesscom.themes.v2.Platform.PLATFORM_ANDROID = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_ANDROID = 2;

### Evidence

- **SRC-0569** `research/proto/chesscom/themes/v2/platform.proto` — [preserved redacted evidence](../evidence/text/1f92148d5fc706c6d69ef79efa557c6e7ded60e57a2c0b0554359cdcfe173616.proto)
  Character offset 159.

```text
to3

package chesscom.themes.v2;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_WEB = 1;
  PLATFORM_ANDROID = 2;
  PLATFORM_IPHONE = 3;
}

```

**Source references:** SRC-0569, SRC-1540  
**URL references:** None independently associated  
**Related findings:** FND-08811, FND-08812, FND-08813

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08815"></a>
## FND-08815: chesscom.themes.v2.Platform.PLATFORM_IPHONE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PLATFORM_IPHONE = 3;

### Evidence

- **SRC-0569** `research/proto/chesscom/themes/v2/platform.proto` — [preserved redacted evidence](../evidence/text/1f92148d5fc706c6d69ef79efa557c6e7ded60e57a2c0b0554359cdcfe173616.proto)
  Character offset 183.

```text
emes.v2;

enum Platform {
  PLATFORM_UNSPECIFIED = 0;
  PLATFORM_WEB = 1;
  PLATFORM_ANDROID = 2;
  PLATFORM_IPHONE = 3;
}

```

**Source references:** SRC-0569, SRC-1540  
**URL references:** None independently associated  
**Related findings:** FND-08811, FND-08812, FND-08813

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08816"></a>
## FND-08816: message declaration: chesscom.themes.v2.ListAllThemeElementsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListAllThemeElementsRequest {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 99.

```text
// source: chesscom/themes/v2/themes_service.proto
// syntax: proto3

package chesscom.themes.v2;

message ListAllThemeElementsRequest {
  optional int32 board_size = 1;
  optional int32 pieces_size = 2;
}

message ListAllThemeElementsResponse {
  repeated .chesscom.themes.v2.PresetTheme themes = 1;
  repeated .chesscom.themes.v2.Background backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyle board_styles = 3;
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08817"></a>
## FND-08817: chesscom.themes.v2.ListAllThemeElementsRequest.board_size = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 board_size = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 139.

```text
rvice.proto
// syntax: proto3

package chesscom.themes.v2;

message ListAllThemeElementsRequest {
  optional int32 board_size = 1;
  optional int32 pieces_size = 2;
}

message ListAllThemeElementsResponse {
  repeated .chesscom.themes.v2.PresetTheme themes = 1;
  repeated .chesscom.themes.v2.Background backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyle board_styles = 3;
  repeated .chesscom.themes.v2.PieceSet
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08818"></a>
## FND-08818: chesscom.themes.v2.ListAllThemeElementsRequest.pieces_size = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 pieces_size = 2;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 172.

```text
ckage chesscom.themes.v2;

message ListAllThemeElementsRequest {
  optional int32 board_size = 1;
  optional int32 pieces_size = 2;
}

message ListAllThemeElementsResponse {
  repeated .chesscom.themes.v2.PresetTheme themes = 1;
  repeated .chesscom.themes.v2.Background backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyle board_styles = 3;
  repeated .chesscom.themes.v2.PieceSet piece_sets = 4;
  repeated .ches
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08819"></a>
## FND-08819: message declaration: chesscom.themes.v2.ListAllThemeElementsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListAllThemeElementsResponse {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 207.

```text
ListAllThemeElementsRequest {
  optional int32 board_size = 1;
  optional int32 pieces_size = 2;
}

message ListAllThemeElementsResponse {
  repeated .chesscom.themes.v2.PresetTheme themes = 1;
  repeated .chesscom.themes.v2.Background backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyle board_styles = 3;
  repeated .chesscom.themes.v2.PieceSet piece_sets = 4;
  repeated .chesscom.themes.v2.SoundSet sound_sets 
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08820"></a>
## FND-08820: chesscom.themes.v2.ListAllThemeElementsResponse.themes = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.PresetTheme themes = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 248.

```text
int32 board_size = 1;
  optional int32 pieces_size = 2;
}

message ListAllThemeElementsResponse {
  repeated .chesscom.themes.v2.PresetTheme themes = 1;
  repeated .chesscom.themes.v2.Background backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyle board_styles = 3;
  repeated .chesscom.themes.v2.PieceSet piece_sets = 4;
  repeated .chesscom.themes.v2.SoundSet sound_sets = 5;
}

message ListThemesSelectionReques
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08821"></a>
## FND-08821: chesscom.themes.v2.ListAllThemeElementsResponse.backgrounds = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.Background backgrounds = 2;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 303.

```text

}

message ListAllThemeElementsResponse {
  repeated .chesscom.themes.v2.PresetTheme themes = 1;
  repeated .chesscom.themes.v2.Background backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyle board_styles = 3;
  repeated .chesscom.themes.v2.PieceSet piece_sets = 4;
  repeated .chesscom.themes.v2.SoundSet sound_sets = 5;
}

message ListThemesSelectionRequest {
}

message ListThemesSelectionResponse {
  repeated
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08822"></a>
## FND-08822: chesscom.themes.v2.ListAllThemeElementsResponse.board_styles = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.BoardStyle board_styles = 3;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 362.

```text
scom.themes.v2.PresetTheme themes = 1;
  repeated .chesscom.themes.v2.Background backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyle board_styles = 3;
  repeated .chesscom.themes.v2.PieceSet piece_sets = 4;
  repeated .chesscom.themes.v2.SoundSet sound_sets = 5;
}

message ListThemesSelectionRequest {
}

message ListThemesSelectionResponse {
  repeated .chesscom.themes.v2.ThemeSelectionItem themes = 1;
  repea
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08823"></a>
## FND-08823: chesscom.themes.v2.ListAllThemeElementsResponse.piece_sets = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.PieceSet piece_sets = 4;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 422.

```text
themes.v2.Background backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyle board_styles = 3;
  repeated .chesscom.themes.v2.PieceSet piece_sets = 4;
  repeated .chesscom.themes.v2.SoundSet sound_sets = 5;
}

message ListThemesSelectionRequest {
}

message ListThemesSelectionResponse {
  repeated .chesscom.themes.v2.ThemeSelectionItem themes = 1;
  repeated .chesscom.themes.v2.BackgroundSelectionItem backgrounds 
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08824"></a>
## FND-08824: chesscom.themes.v2.ListAllThemeElementsResponse.sound_sets = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.SoundSet sound_sets = 5;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 478.

```text
om.themes.v2.BoardStyle board_styles = 3;
  repeated .chesscom.themes.v2.PieceSet piece_sets = 4;
  repeated .chesscom.themes.v2.SoundSet sound_sets = 5;
}

message ListThemesSelectionRequest {
}

message ListThemesSelectionResponse {
  repeated .chesscom.themes.v2.ThemeSelectionItem themes = 1;
  repeated .chesscom.themes.v2.BackgroundSelectionItem backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyleSelectionI
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08825"></a>
## FND-08825: message declaration: chesscom.themes.v2.ListThemesSelectionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListThemesSelectionRequest {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 535.

```text
sscom.themes.v2.PieceSet piece_sets = 4;
  repeated .chesscom.themes.v2.SoundSet sound_sets = 5;
}

message ListThemesSelectionRequest {
}

message ListThemesSelectionResponse {
  repeated .chesscom.themes.v2.ThemeSelectionItem themes = 1;
  repeated .chesscom.themes.v2.BackgroundSelectionItem backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyleSelectionItem board_styles = 3;
  repeated .chesscom.themes.v2.Piec
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08826"></a>
## FND-08826: message declaration: chesscom.themes.v2.ListThemesSelectionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListThemesSelectionResponse {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 575.

```text

  repeated .chesscom.themes.v2.SoundSet sound_sets = 5;
}

message ListThemesSelectionRequest {
}

message ListThemesSelectionResponse {
  repeated .chesscom.themes.v2.ThemeSelectionItem themes = 1;
  repeated .chesscom.themes.v2.BackgroundSelectionItem backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyleSelectionItem board_styles = 3;
  repeated .chesscom.themes.v2.PieceSetSelectionItem piece_sets = 4;
  repe
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08827"></a>
## FND-08827: chesscom.themes.v2.ListThemesSelectionResponse.themes = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.ThemeSelectionItem themes = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 615.

```text
 sound_sets = 5;
}

message ListThemesSelectionRequest {
}

message ListThemesSelectionResponse {
  repeated .chesscom.themes.v2.ThemeSelectionItem themes = 1;
  repeated .chesscom.themes.v2.BackgroundSelectionItem backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyleSelectionItem board_styles = 3;
  repeated .chesscom.themes.v2.PieceSetSelectionItem piece_sets = 4;
  repeated .chesscom.themes.v2.SoundSetSelecti
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08828"></a>
## FND-08828: chesscom.themes.v2.ListThemesSelectionResponse.backgrounds = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.BackgroundSelectionItem backgrounds = 2;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 677.

```text
ssage ListThemesSelectionResponse {
  repeated .chesscom.themes.v2.ThemeSelectionItem themes = 1;
  repeated .chesscom.themes.v2.BackgroundSelectionItem backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyleSelectionItem board_styles = 3;
  repeated .chesscom.themes.v2.PieceSetSelectionItem piece_sets = 4;
  repeated .chesscom.themes.v2.SoundSetSelectionItem sound_sets = 5;
  repeated .chesscom.themes.v2.ThemeEle
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08829"></a>
## FND-08829: chesscom.themes.v2.ListThemesSelectionResponse.board_styles = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.BoardStyleSelectionItem board_styles = 3;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 749.

```text
SelectionItem themes = 1;
  repeated .chesscom.themes.v2.BackgroundSelectionItem backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyleSelectionItem board_styles = 3;
  repeated .chesscom.themes.v2.PieceSetSelectionItem piece_sets = 4;
  repeated .chesscom.themes.v2.SoundSetSelectionItem sound_sets = 5;
  repeated .chesscom.themes.v2.ThemeElementCategory board_style_categories = 6;
  repeated .chesscom.themes.v2.
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08830"></a>
## FND-08830: chesscom.themes.v2.ListThemesSelectionResponse.piece_sets = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.PieceSetSelectionItem piece_sets = 4;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 822.

```text
ionItem backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyleSelectionItem board_styles = 3;
  repeated .chesscom.themes.v2.PieceSetSelectionItem piece_sets = 4;
  repeated .chesscom.themes.v2.SoundSetSelectionItem sound_sets = 5;
  repeated .chesscom.themes.v2.ThemeElementCategory board_style_categories = 6;
  repeated .chesscom.themes.v2.ThemeElementCategory piece_set_categories = 7;
  repeated .chesscom.theme
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08831"></a>
## FND-08831: chesscom.themes.v2.ListThemesSelectionResponse.sound_sets = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.SoundSetSelectionItem sound_sets = 5;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 891.

```text
ectionItem board_styles = 3;
  repeated .chesscom.themes.v2.PieceSetSelectionItem piece_sets = 4;
  repeated .chesscom.themes.v2.SoundSetSelectionItem sound_sets = 5;
  repeated .chesscom.themes.v2.ThemeElementCategory board_style_categories = 6;
  repeated .chesscom.themes.v2.ThemeElementCategory piece_set_categories = 7;
  repeated .chesscom.themes.v2.ThemeElementCategory sound_set_categories = 8;
}

message ListTh
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08832"></a>
## FND-08832: chesscom.themes.v2.ListThemesSelectionResponse.board_style_categories = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.ThemeElementCategory board_style_categories = 6;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 960.

```text
electionItem piece_sets = 4;
  repeated .chesscom.themes.v2.SoundSetSelectionItem sound_sets = 5;
  repeated .chesscom.themes.v2.ThemeElementCategory board_style_categories = 6;
  repeated .chesscom.themes.v2.ThemeElementCategory piece_set_categories = 7;
  repeated .chesscom.themes.v2.ThemeElementCategory sound_set_categories = 8;
}

message ListThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
 
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08833"></a>
## FND-08833: chesscom.themes.v2.ListThemesSelectionResponse.piece_set_categories = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.ThemeElementCategory piece_set_categories = 7;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1040.

```text
m sound_sets = 5;
  repeated .chesscom.themes.v2.ThemeElementCategory board_style_categories = 6;
  repeated .chesscom.themes.v2.ThemeElementCategory piece_set_categories = 7;
  repeated .chesscom.themes.v2.ThemeElementCategory sound_set_categories = 8;
}

message ListThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message Lis
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08834"></a>
## FND-08834: chesscom.themes.v2.ListThemesSelectionResponse.sound_set_categories = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.ThemeElementCategory sound_set_categories = 8;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1118.

```text
yle_categories = 6;
  repeated .chesscom.themes.v2.ThemeElementCategory piece_set_categories = 7;
  repeated .chesscom.themes.v2.ThemeElementCategory sound_set_categories = 8;
}

message ListThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message 
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08835"></a>
## FND-08835: message declaration: chesscom.themes.v2.ListThemesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListThemesRequest {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1197.

```text
et_categories = 7;
  repeated .chesscom.themes.v2.ThemeElementCategory sound_set_categories = 8;
}

message ListThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;

```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08836"></a>
## FND-08836: chesscom.themes.v2.ListThemesRequest.platform = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.Platform platform = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1227.

```text
.chesscom.themes.v2.ThemeElementCategory sound_set_categories = 8;
}

message ListThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResp
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08837"></a>
## FND-08837: chesscom.themes.v2.ListThemesRequest.board_size = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 board_size = 2;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1281.

```text
egories = 8;
}

message ListThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResponse {
  repeated .chesscom.themes.v2.Background backg
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08838"></a>
## FND-08838: chesscom.themes.v2.ListThemesRequest.pieces_size = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 pieces_size = 3;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1314.

```text
sRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResponse {
  repeated .chesscom.themes.v2.Background backgrounds = 1;
}

message ListBoardS
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08839"></a>
## FND-08839: message declaration: chesscom.themes.v2.ListThemesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListThemesResponse {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1349.

```text
mes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResponse {
  repeated .chesscom.themes.v2.Background backgrounds = 1;
}

message ListBoardStylesRequest {
  optional .chesscom
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08840"></a>
## FND-08840: chesscom.themes.v2.ListThemesResponse.themes = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.Theme themes = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1380.

```text
 optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResponse {
  repeated .chesscom.themes.v2.Background backgrounds = 1;
}

message ListBoardStylesRequest {
  optional .chesscom.themes.v2.Platform platform = 
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08841"></a>
## FND-08841: message declaration: chesscom.themes.v2.ListBackgroundsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListBackgroundsRequest {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1430.

```text
ieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResponse {
  repeated .chesscom.themes.v2.Background backgrounds = 1;
}

message ListBoardStylesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
}

message Lis
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08842"></a>
## FND-08842: chesscom.themes.v2.ListBackgroundsRequest.platform = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.Platform platform = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1227.

```text
.chesscom.themes.v2.ThemeElementCategory sound_set_categories = 8;
}

message ListThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResp
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08843"></a>
## FND-08843: message declaration: chesscom.themes.v2.ListBackgroundsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListBackgroundsResponse {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1520.

```text
s = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResponse {
  repeated .chesscom.themes.v2.Background backgrounds = 1;
}

message ListBoardStylesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
}

message ListBoardStylesResponse {
  repeated .chesscom.themes.v2.BoardStyle board_styles = 1;
}

mess
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08844"></a>
## FND-08844: chesscom.themes.v2.ListBackgroundsResponse.backgrounds = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.Background backgrounds = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1556.

```text
uest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResponse {
  repeated .chesscom.themes.v2.Background backgrounds = 1;
}

message ListBoardStylesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
}

message ListBoardStylesResponse {
  repeated .chesscom.themes.v2.BoardStyle board_styles = 1;
}

message ListPieceSetsRequest {
  optiona
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08845"></a>
## FND-08845: message declaration: chesscom.themes.v2.ListBoardStylesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListBoardStylesRequest {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1616.

```text

}

message ListBackgroundsResponse {
  repeated .chesscom.themes.v2.Background backgrounds = 1;
}

message ListBoardStylesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
}

message ListBoardStylesResponse {
  repeated .chesscom.themes.v2.BoardStyle board_styles = 1;
}

message ListPieceSetsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int3
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08846"></a>
## FND-08846: chesscom.themes.v2.ListBoardStylesRequest.platform = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.Platform platform = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1227.

```text
.chesscom.themes.v2.ThemeElementCategory sound_set_categories = 8;
}

message ListThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResp
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08847"></a>
## FND-08847: chesscom.themes.v2.ListBoardStylesRequest.board_size = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 board_size = 2;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1281.

```text
egories = 8;
}

message ListThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResponse {
  repeated .chesscom.themes.v2.Background backg
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08848"></a>
## FND-08848: message declaration: chesscom.themes.v2.ListBoardStylesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListBoardStylesResponse {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1739.

```text
Request {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
}

message ListBoardStylesResponse {
  repeated .chesscom.themes.v2.BoardStyle board_styles = 1;
}

message ListPieceSetsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 pieces_size = 2;
}

message ListPieceSetsResponse {
  repeated .chesscom.themes.v2.PieceSet piece_sets = 1;
}

message Li
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08849"></a>
## FND-08849: chesscom.themes.v2.ListBoardStylesResponse.board_styles = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.BoardStyle board_styles = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1775.

```text
s.v2.Platform platform = 1;
  optional int32 board_size = 2;
}

message ListBoardStylesResponse {
  repeated .chesscom.themes.v2.BoardStyle board_styles = 1;
}

message ListPieceSetsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 pieces_size = 2;
}

message ListPieceSetsResponse {
  repeated .chesscom.themes.v2.PieceSet piece_sets = 1;
}

message ListSoundSetsRequest {
  optional .che
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08850"></a>
## FND-08850: message declaration: chesscom.themes.v2.ListPieceSetsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListPieceSetsRequest {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1836.

```text
}

message ListBoardStylesResponse {
  repeated .chesscom.themes.v2.BoardStyle board_styles = 1;
}

message ListPieceSetsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 pieces_size = 2;
}

message ListPieceSetsResponse {
  repeated .chesscom.themes.v2.PieceSet piece_sets = 1;
}

message ListSoundSetsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListSoundSe
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08851"></a>
## FND-08851: chesscom.themes.v2.ListPieceSetsRequest.platform = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.Platform platform = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1227.

```text
.chesscom.themes.v2.ThemeElementCategory sound_set_categories = 8;
}

message ListThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResp
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08852"></a>
## FND-08852: chesscom.themes.v2.ListPieceSetsRequest.pieces_size = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 pieces_size = 2;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 172.

```text
ckage chesscom.themes.v2;

message ListAllThemeElementsRequest {
  optional int32 board_size = 1;
  optional int32 pieces_size = 2;
}

message ListAllThemeElementsResponse {
  repeated .chesscom.themes.v2.PresetTheme themes = 1;
  repeated .chesscom.themes.v2.Background backgrounds = 2;
  repeated .chesscom.themes.v2.BoardStyle board_styles = 3;
  repeated .chesscom.themes.v2.PieceSet piece_sets = 4;
  repeated .ches
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08853"></a>
## FND-08853: message declaration: chesscom.themes.v2.ListPieceSetsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListPieceSetsResponse {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1958.

```text
equest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 pieces_size = 2;
}

message ListPieceSetsResponse {
  repeated .chesscom.themes.v2.PieceSet piece_sets = 1;
}

message ListSoundSetsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListSoundSetsResponse {
  repeated .chesscom.themes.v2.SoundSet sound_sets = 1;
}

message ListOnboardingThemesRequest {
  optional .
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08854"></a>
## FND-08854: chesscom.themes.v2.ListPieceSetsResponse.piece_sets = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.PieceSet piece_sets = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1992.

```text
es.v2.Platform platform = 1;
  optional int32 pieces_size = 2;
}

message ListPieceSetsResponse {
  repeated .chesscom.themes.v2.PieceSet piece_sets = 1;
}

message ListSoundSetsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListSoundSetsResponse {
  repeated .chesscom.themes.v2.SoundSet sound_sets = 1;
}

message ListOnboardingThemesRequest {
  optional .chesscom.themes.v2.Platform platfo
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08855"></a>
## FND-08855: message declaration: chesscom.themes.v2.ListSoundSetsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListSoundSetsRequest {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2049.

```text
 = 2;
}

message ListPieceSetsResponse {
  repeated .chesscom.themes.v2.PieceSet piece_sets = 1;
}

message ListSoundSetsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListSoundSetsResponse {
  repeated .chesscom.themes.v2.SoundSet sound_sets = 1;
}

message ListOnboardingThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08856"></a>
## FND-08856: chesscom.themes.v2.ListSoundSetsRequest.platform = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.Platform platform = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1227.

```text
.chesscom.themes.v2.ThemeElementCategory sound_set_categories = 8;
}

message ListThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResp
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08857"></a>
## FND-08857: message declaration: chesscom.themes.v2.ListSoundSetsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListSoundSetsResponse {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2137.

```text
ets = 1;
}

message ListSoundSetsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListSoundSetsResponse {
  repeated .chesscom.themes.v2.SoundSet sound_sets = 1;
}

message ListOnboardingThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListOnboardingThemesResponse {
  repeated .chesscom.themes.
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08858"></a>
## FND-08858: chesscom.themes.v2.ListSoundSetsResponse.sound_sets = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.SoundSet sound_sets = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2171.

```text
equest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListSoundSetsResponse {
  repeated .chesscom.themes.v2.SoundSet sound_sets = 1;
}

message ListOnboardingThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListOnboardingThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message Ge
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08859"></a>
## FND-08859: message declaration: chesscom.themes.v2.ListOnboardingThemesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListOnboardingThemesRequest {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2228.

```text
 = 1;
}

message ListSoundSetsResponse {
  repeated .chesscom.themes.v2.SoundSet sound_sets = 1;
}

message ListOnboardingThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListOnboardingThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message GetThemeRequest {
  optional string theme_id = 1;
  optiona
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08860"></a>
## FND-08860: chesscom.themes.v2.ListOnboardingThemesRequest.platform = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.Platform platform = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1227.

```text
.chesscom.themes.v2.ThemeElementCategory sound_set_categories = 8;
}

message ListThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResp
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08861"></a>
## FND-08861: chesscom.themes.v2.ListOnboardingThemesRequest.board_size = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 board_size = 2;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1281.

```text
egories = 8;
}

message ListThemesRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResponse {
  repeated .chesscom.themes.v2.Background backg
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08862"></a>
## FND-08862: chesscom.themes.v2.ListOnboardingThemesRequest.pieces_size = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 pieces_size = 3;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1314.

```text
sRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResponse {
  repeated .chesscom.themes.v2.Background backgrounds = 1;
}

message ListBoardS
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08863"></a>
## FND-08863: message declaration: chesscom.themes.v2.ListOnboardingThemesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListOnboardingThemesResponse {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2390.

```text
mes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListOnboardingThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message GetThemeRequest {
  optional string theme_id = 1;
  optional .chesscom.themes.v2.Platform platform = 11;
  optional int32 board_size = 12;
  optional int32 pieces_size = 13;
}

message GetThemeResponse {
  optional .chess
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08864"></a>
## FND-08864: chesscom.themes.v2.ListOnboardingThemesResponse.themes = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.themes.v2.Theme themes = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 1380.

```text
 optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message ListThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message ListBackgroundsRequest {
  optional .chesscom.themes.v2.Platform platform = 1;
}

message ListBackgroundsResponse {
  repeated .chesscom.themes.v2.Background backgrounds = 1;
}

message ListBoardStylesRequest {
  optional .chesscom.themes.v2.Platform platform = 
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08865"></a>
## FND-08865: message declaration: chesscom.themes.v2.GetThemeRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetThemeRequest {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2481.

```text
 = 3;
}

message ListOnboardingThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message GetThemeRequest {
  optional string theme_id = 1;
  optional .chesscom.themes.v2.Platform platform = 11;
  optional int32 board_size = 12;
  optional int32 pieces_size = 13;
}

message GetThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

message GetCustomThemeRequest {
  oneof _background_id {

```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08866"></a>
## FND-08866: chesscom.themes.v2.GetThemeRequest.theme_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string theme_id = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2509.

```text
ingThemesResponse {
  repeated .chesscom.themes.v2.Theme themes = 1;
}

message GetThemeRequest {
  optional string theme_id = 1;
  optional .chesscom.themes.v2.Platform platform = 11;
  optional int32 board_size = 12;
  optional int32 pieces_size = 13;
}

message GetThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

message GetCustomThemeRequest {
  oneof _background_id {
  string background_id = 1;

```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08867"></a>
## FND-08867: chesscom.themes.v2.GetThemeRequest.platform = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.Platform platform = 11;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2541.

```text
chesscom.themes.v2.Theme themes = 1;
}

message GetThemeRequest {
  optional string theme_id = 1;
  optional .chesscom.themes.v2.Platform platform = 11;
  optional int32 board_size = 12;
  optional int32 pieces_size = 13;
}

message GetThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

message GetCustomThemeRequest {
  oneof _background_id {
  string background_id = 1;
  }
  optional string board_styl
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08868"></a>
## FND-08868: chesscom.themes.v2.GetThemeRequest.board_size = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 board_size = 12;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2596.

```text
eRequest {
  optional string theme_id = 1;
  optional .chesscom.themes.v2.Platform platform = 11;
  optional int32 board_size = 12;
  optional int32 pieces_size = 13;
}

message GetThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

message GetCustomThemeRequest {
  oneof _background_id {
  string background_id = 1;
  }
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optiona
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08869"></a>
## FND-08869: chesscom.themes.v2.GetThemeRequest.pieces_size = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 pieces_size = 13;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2630.

```text
_id = 1;
  optional .chesscom.themes.v2.Platform platform = 11;
  optional int32 board_size = 12;
  optional int32 pieces_size = 13;
}

message GetThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

message GetCustomThemeRequest {
  oneof _background_id {
  string background_id = 1;
  }
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
  optio
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08870"></a>
## FND-08870: message declaration: chesscom.themes.v2.GetThemeResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetThemeResponse {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2666.

```text
.v2.Platform platform = 11;
  optional int32 board_size = 12;
  optional int32 pieces_size = 13;
}

message GetThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

message GetCustomThemeRequest {
  oneof _background_id {
  string background_id = 1;
  }
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
  optional .chesscom.themes.v2.Platform pla
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08871"></a>
## FND-08871: chesscom.themes.v2.GetThemeResponse.theme = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.themes.v2.Theme theme = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2695.

```text
 optional int32 board_size = 12;
  optional int32 pieces_size = 13;
}

message GetThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

message GetCustomThemeRequest {
  oneof _background_id {
  string background_id = 1;
  }
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
  optional .chesscom.themes.v2.Platform platform = 11;
  optional int32 
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08872"></a>
## FND-08872: message declaration: chesscom.themes.v2.GetCustomThemeRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCustomThemeRequest {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2744.

```text
 pieces_size = 13;
}

message GetThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

message GetCustomThemeRequest {
  oneof _background_id {
  string background_id = 1;
  }
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
  optional .chesscom.themes.v2.Platform platform = 11;
  optional int32 board_size = 12;
  optional int32 pieces_size = 1
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08873"></a>
## FND-08873: oneof declaration: chesscom.themes.v2.GetCustomThemeRequest._background_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _background_id {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2778.

```text
hemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

message GetCustomThemeRequest {
  oneof _background_id {
  string background_id = 1;
  }
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
  optional .chesscom.themes.v2.Platform platform = 11;
  optional int32 board_size = 12;
  optional int32 pieces_size = 13;
}

message GetCustomThemeRespon
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08874"></a>
## FND-08874: chesscom.themes.v2.GetCustomThemeRequest.background_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string background_id = 1;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2803.

```text
 .chesscom.themes.v2.Theme theme = 1;
}

message GetCustomThemeRequest {
  oneof _background_id {
  string background_id = 1;
  }
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
  optional .chesscom.themes.v2.Platform platform = 11;
  optional int32 board_size = 12;
  optional int32 pieces_size = 13;
}

message GetCustomThemeResponse {
  optional .chesscom
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
