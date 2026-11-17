# data_models — findings 8601–8700

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-08875"></a>
## FND-08875: chesscom.themes.v2.GetCustomThemeRequest.board_style_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string board_style_id = 2;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2835.

```text
 = 1;
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
  optional .chesscom.themes.v2.Theme theme = 1;
}

m
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08876"></a>
## FND-08876: chesscom.themes.v2.GetCustomThemeRequest.piece_set_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string piece_set_id = 3;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2873.

```text
 {
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
  optional .chesscom.themes.v2.Theme theme = 1;
}

message SelectThemeRequest {
  optional
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08877"></a>
## FND-08877: chesscom.themes.v2.GetCustomThemeRequest.sound_set_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string sound_set_id = 4;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2909.

```text
 background_id = 1;
  }
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
  optional .chesscom.themes.v2.Platform platform = 11;
  optional int32 board_size = 12;
  optional int32 pieces_size = 13;
}

message GetCustomThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

message SelectThemeRequest {
  optional string theme_id = 1;
  optional .ch
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08878"></a>
## FND-08878: chesscom.themes.v2.GetCustomThemeRequest.platform = 11

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

<a id="FND-08879"></a>
## FND-08879: chesscom.themes.v2.GetCustomThemeRequest.board_size = 12

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

<a id="FND-08880"></a>
## FND-08880: chesscom.themes.v2.GetCustomThemeRequest.pieces_size = 13

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

<a id="FND-08881"></a>
## FND-08881: message declaration: chesscom.themes.v2.GetCustomThemeResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetCustomThemeResponse {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 3070.

```text
.v2.Platform platform = 11;
  optional int32 board_size = 12;
  optional int32 pieces_size = 13;
}

message GetCustomThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

message SelectThemeRequest {
  optional string theme_id = 1;
  optional .chesscom.themes.v2.Platform platform = 11;
}

message SelectThemeResponse {
}

message SelectCustomThemeRequest {
  oneof _background_id {
  string background_id =
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08882"></a>
## FND-08882: chesscom.themes.v2.GetCustomThemeResponse.theme = 1

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

<a id="FND-08883"></a>
## FND-08883: message declaration: chesscom.themes.v2.SelectThemeRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SelectThemeRequest {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 3154.

```text
s_size = 13;
}

message GetCustomThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

message SelectThemeRequest {
  optional string theme_id = 1;
  optional .chesscom.themes.v2.Platform platform = 11;
}

message SelectThemeResponse {
}

message SelectCustomThemeRequest {
  oneof _background_id {
  string background_id = 1;
  }
  oneof _board_style_id {
  string board_style_id = 2;
  }
  oneof _piece_se
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08884"></a>
## FND-08884: chesscom.themes.v2.SelectThemeRequest.theme_id = 1

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

<a id="FND-08885"></a>
## FND-08885: chesscom.themes.v2.SelectThemeRequest.platform = 11

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

<a id="FND-08886"></a>
## FND-08886: message declaration: chesscom.themes.v2.SelectThemeResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SelectThemeResponse {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 3273.

```text
Request {
  optional string theme_id = 1;
  optional .chesscom.themes.v2.Platform platform = 11;
}

message SelectThemeResponse {
}

message SelectCustomThemeRequest {
  oneof _background_id {
  string background_id = 1;
  }
  oneof _board_style_id {
  string board_style_id = 2;
  }
  oneof _piece_set_id {
  string piece_set_id = 3;
  }
  oneof _sound_set_id {
  string sound_set_id = 4;
  }
  optional .chesscom.theme
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08887"></a>
## FND-08887: message declaration: chesscom.themes.v2.SelectCustomThemeRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SelectCustomThemeRequest {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 3306.

```text
_id = 1;
  optional .chesscom.themes.v2.Platform platform = 11;
}

message SelectThemeResponse {
}

message SelectCustomThemeRequest {
  oneof _background_id {
  string background_id = 1;
  }
  oneof _board_style_id {
  string board_style_id = 2;
  }
  oneof _piece_set_id {
  string piece_set_id = 3;
  }
  oneof _sound_set_id {
  string sound_set_id = 4;
  }
  optional .chesscom.themes.v2.Platform platform = 11;
}

m
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08888"></a>
## FND-08888: oneof declaration: chesscom.themes.v2.SelectCustomThemeRequest._background_id

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

<a id="FND-08889"></a>
## FND-08889: chesscom.themes.v2.SelectCustomThemeRequest.background_id = 1

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

<a id="FND-08890"></a>
## FND-08890: oneof declaration: chesscom.themes.v2.SelectCustomThemeRequest._board_style_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _board_style_id {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 3400.

```text
 {
}

message SelectCustomThemeRequest {
  oneof _background_id {
  string background_id = 1;
  }
  oneof _board_style_id {
  string board_style_id = 2;
  }
  oneof _piece_set_id {
  string piece_set_id = 3;
  }
  oneof _sound_set_id {
  string sound_set_id = 4;
  }
  optional .chesscom.themes.v2.Platform platform = 11;
}

message SelectCustomThemeResponse {
}

message GetActiveThemeRequest {
  oneof _user_id {
  str
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08891"></a>
## FND-08891: chesscom.themes.v2.SelectCustomThemeRequest.board_style_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string board_style_id = 2;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2844.

```text
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
  optional .chesscom.themes.v2.Theme theme = 1;
}

message Se
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08892"></a>
## FND-08892: oneof declaration: chesscom.themes.v2.SelectCustomThemeRequest._piece_set_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _piece_set_id {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 3459.

```text
d_id {
  string background_id = 1;
  }
  oneof _board_style_id {
  string board_style_id = 2;
  }
  oneof _piece_set_id {
  string piece_set_id = 3;
  }
  oneof _sound_set_id {
  string sound_set_id = 4;
  }
  optional .chesscom.themes.v2.Platform platform = 11;
}

message SelectCustomThemeResponse {
}

message GetActiveThemeRequest {
  oneof _user_id {
  string user_id = 16;
  }
  optional .chesscom.themes.v2.Platfo
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08893"></a>
## FND-08893: chesscom.themes.v2.SelectCustomThemeRequest.piece_set_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string piece_set_id = 3;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2882.

```text
f _background_id {
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
  optional .chesscom.themes.v2.Theme theme = 1;
}

message SelectThemeRequest {
  optional string t
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08894"></a>
## FND-08894: oneof declaration: chesscom.themes.v2.SelectCustomThemeRequest._sound_set_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _sound_set_id {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 3514.

```text
tyle_id {
  string board_style_id = 2;
  }
  oneof _piece_set_id {
  string piece_set_id = 3;
  }
  oneof _sound_set_id {
  string sound_set_id = 4;
  }
  optional .chesscom.themes.v2.Platform platform = 11;
}

message SelectCustomThemeResponse {
}

message GetActiveThemeRequest {
  oneof _user_id {
  string user_id = 16;
  }
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  opt
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08895"></a>
## FND-08895: chesscom.themes.v2.SelectCustomThemeRequest.sound_set_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string sound_set_id = 4;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 2918.

```text
nd_id = 1;
  }
  optional string board_style_id = 2;
  optional string piece_set_id = 3;
  optional string sound_set_id = 4;
  optional .chesscom.themes.v2.Platform platform = 11;
  optional int32 board_size = 12;
  optional int32 pieces_size = 13;
}

message GetCustomThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

message SelectThemeRequest {
  optional string theme_id = 1;
  optional .chesscom.th
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08896"></a>
## FND-08896: chesscom.themes.v2.SelectCustomThemeRequest.platform = 11

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

<a id="FND-08897"></a>
## FND-08897: message declaration: chesscom.themes.v2.SelectCustomThemeResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SelectCustomThemeResponse {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 3625.

```text
d_set_id {
  string sound_set_id = 4;
  }
  optional .chesscom.themes.v2.Platform platform = 11;
}

message SelectCustomThemeResponse {
}

message GetActiveThemeRequest {
  oneof _user_id {
  string user_id = 16;
  }
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message GetActiveThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1
```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08898"></a>
## FND-08898: message declaration: chesscom.themes.v2.GetActiveThemeRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetActiveThemeRequest {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 3664.

```text
 }
  optional .chesscom.themes.v2.Platform platform = 11;
}

message SelectCustomThemeResponse {
}

message GetActiveThemeRequest {
  oneof _user_id {
  string user_id = 16;
  }
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message GetActiveThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08899"></a>
## FND-08899: oneof declaration: chesscom.themes.v2.GetActiveThemeRequest._user_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_id {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 3698.

```text
Platform platform = 11;
}

message SelectCustomThemeResponse {
}

message GetActiveThemeRequest {
  oneof _user_id {
  string user_id = 16;
  }
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message GetActiveThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08900"></a>
## FND-08900: chesscom.themes.v2.GetActiveThemeRequest.user_id = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_id = 16;

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 3717.

```text
 11;
}

message SelectCustomThemeResponse {
}

message GetActiveThemeRequest {
  oneof _user_id {
  string user_id = 16;
  }
  optional .chesscom.themes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message GetActiveThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08901"></a>
## FND-08901: chesscom.themes.v2.GetActiveThemeRequest.platform = 1

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

<a id="FND-08902"></a>
## FND-08902: chesscom.themes.v2.GetActiveThemeRequest.board_size = 2

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

<a id="FND-08903"></a>
## FND-08903: chesscom.themes.v2.GetActiveThemeRequest.pieces_size = 3

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

<a id="FND-08904"></a>
## FND-08904: message declaration: chesscom.themes.v2.GetActiveThemeResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetActiveThemeResponse {

### Evidence

- **SRC-0570** `research/proto/chesscom/themes/v2/themes_service.proto` — [preserved redacted evidence](../evidence/text/f1205d4b0fbc31c055118bd8f2ee439e4ceb3a066a590a18437e906f88ae4805.proto)
  Character offset 3866.

```text
mes.v2.Platform platform = 1;
  optional int32 board_size = 2;
  optional int32 pieces_size = 3;
}

message GetActiveThemeResponse {
  optional .chesscom.themes.v2.Theme theme = 1;
}

```

**Source references:** SRC-0570, SRC-1541  
**URL references:** None independently associated  
**Related findings:** FND-08816, FND-08817, FND-08818

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08905"></a>
## FND-08905: chesscom.themes.v2.GetActiveThemeResponse.theme = 1

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

<a id="FND-08906"></a>
## FND-08906: enum declaration: chesscom.train.v1.TrainBackfillStatus

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TrainBackfillStatus {

### Evidence

- **SRC-0571** `research/proto/chesscom/train/v1/train_backfill_status.proto` — [preserved redacted evidence](../evidence/text/3593bb96e81538e414db7506062c98eccd513720af4f55133c256a1bebe706d6.proto)
  Character offset 104.

```text
ource: chesscom/train/v1/train_backfill_status.proto
// syntax: proto3

package chesscom.train.v1;

enum TrainBackfillStatus {
  TRAIN_BACKFILL_STATUS_UNSPECIFIED = 0;
  TRAIN_BACKFILL_STATUS_IN_PROGRESS = 1;
  TRAIN_BACKFILL_STATUS_COMPLETED = 2;
}

```

**Source references:** SRC-0571, SRC-1542  
**URL references:** None independently associated  
**Related findings:** FND-08907, FND-08908

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08907"></a>
## FND-08907: chesscom.train.v1.TrainBackfillStatus.TRAIN_BACKFILL_STATUS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_BACKFILL_STATUS_UNSPECIFIED = 0;

### Evidence

- **SRC-0571** `research/proto/chesscom/train/v1/train_backfill_status.proto` — [preserved redacted evidence](../evidence/text/3593bb96e81538e414db7506062c98eccd513720af4f55133c256a1bebe706d6.proto)
  Character offset 133.

```text
n_backfill_status.proto
// syntax: proto3

package chesscom.train.v1;

enum TrainBackfillStatus {
  TRAIN_BACKFILL_STATUS_UNSPECIFIED = 0;
  TRAIN_BACKFILL_STATUS_IN_PROGRESS = 1;
  TRAIN_BACKFILL_STATUS_COMPLETED = 2;
}

```

**Source references:** SRC-0571, SRC-1542  
**URL references:** None independently associated  
**Related findings:** FND-08906, FND-08908

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08908"></a>
## FND-08908: chesscom.train.v1.TrainBackfillStatus.TRAIN_BACKFILL_STATUS_IN_PROGRESS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_BACKFILL_STATUS_IN_PROGRESS = 1;

### Evidence

- **SRC-0571** `research/proto/chesscom/train/v1/train_backfill_status.proto` — [preserved redacted evidence](../evidence/text/3593bb96e81538e414db7506062c98eccd513720af4f55133c256a1bebe706d6.proto)
  Character offset 174.

```text


package chesscom.train.v1;

enum TrainBackfillStatus {
  TRAIN_BACKFILL_STATUS_UNSPECIFIED = 0;
  TRAIN_BACKFILL_STATUS_IN_PROGRESS = 1;
  TRAIN_BACKFILL_STATUS_COMPLETED = 2;
}

```

**Source references:** SRC-0571, SRC-1542  
**URL references:** None independently associated  
**Related findings:** FND-08906, FND-08907

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08909"></a>
## FND-08909: chesscom.train.v1.TrainBackfillStatus.TRAIN_BACKFILL_STATUS_COMPLETED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_BACKFILL_STATUS_COMPLETED = 2;

### Evidence

- **SRC-0571** `research/proto/chesscom/train/v1/train_backfill_status.proto` — [preserved redacted evidence](../evidence/text/3593bb96e81538e414db7506062c98eccd513720af4f55133c256a1bebe706d6.proto)
  Character offset 215.

```text
ackfillStatus {
  TRAIN_BACKFILL_STATUS_UNSPECIFIED = 0;
  TRAIN_BACKFILL_STATUS_IN_PROGRESS = 1;
  TRAIN_BACKFILL_STATUS_COMPLETED = 2;
}

```

**Source references:** SRC-0571, SRC-1542  
**URL references:** None independently associated  
**Related findings:** FND-08906, FND-08907, FND-08908

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08910"></a>
## FND-08910: message declaration: chesscom.train.v1.TrainBlunderChallenge

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TrainBlunderChallenge {

### Evidence

- **SRC-0572** `research/proto/chesscom/train/v1/train_blunder_challenge.proto` — [preserved redacted evidence](../evidence/text/d8c8193038cac9e76b67f897dab335f7758f9cf7e61c0d53baf8bb6f9bd84259.proto)
  Character offset 106.

```text
rce: chesscom/train/v1/train_blunder_challenge.proto
// syntax: proto3

package chesscom.train.v1;

message TrainBlunderChallenge {
  oneof _theme {
  .chesscom.train.v1.TrainTacticalTheme theme = 2;
  }
  optional .chesscom.train.v1.TrainChallengeBucket bucket = 1;
  optional .chesscom.chess.v1.Move correct_move = 3;
}

```

**Source references:** SRC-0572, SRC-1543  
**URL references:** None independently associated  
**Related findings:** FND-08911, FND-08912

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08911"></a>
## FND-08911: oneof declaration: chesscom.train.v1.TrainBlunderChallenge._theme

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _theme {

### Evidence

- **SRC-0572** `research/proto/chesscom/train/v1/train_blunder_challenge.proto` — [preserved redacted evidence](../evidence/text/d8c8193038cac9e76b67f897dab335f7758f9cf7e61c0d53baf8bb6f9bd84259.proto)
  Character offset 140.

```text
er_challenge.proto
// syntax: proto3

package chesscom.train.v1;

message TrainBlunderChallenge {
  oneof _theme {
  .chesscom.train.v1.TrainTacticalTheme theme = 2;
  }
  optional .chesscom.train.v1.TrainChallengeBucket bucket = 1;
  optional .chesscom.chess.v1.Move correct_move = 3;
}

```

**Source references:** SRC-0572, SRC-1543  
**URL references:** None independently associated  
**Related findings:** FND-08910, FND-08912

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08912"></a>
## FND-08912: chesscom.train.v1.TrainBlunderChallenge.theme = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.train.v1.TrainTacticalTheme theme = 2;

### Evidence

- **SRC-0572** `research/proto/chesscom/train/v1/train_blunder_challenge.proto` — [preserved redacted evidence](../evidence/text/d8c8193038cac9e76b67f897dab335f7758f9cf7e61c0d53baf8bb6f9bd84259.proto)
  Character offset 157.

```text
o
// syntax: proto3

package chesscom.train.v1;

message TrainBlunderChallenge {
  oneof _theme {
  .chesscom.train.v1.TrainTacticalTheme theme = 2;
  }
  optional .chesscom.train.v1.TrainChallengeBucket bucket = 1;
  optional .chesscom.chess.v1.Move correct_move = 3;
}

```

**Source references:** SRC-0572, SRC-1543  
**URL references:** None independently associated  
**Related findings:** FND-08910, FND-08911

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08913"></a>
## FND-08913: chesscom.train.v1.TrainBlunderChallenge.bucket = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.train.v1.TrainChallengeBucket bucket = 1;

### Evidence

- **SRC-0572** `research/proto/chesscom/train/v1/train_blunder_challenge.proto` — [preserved redacted evidence](../evidence/text/d8c8193038cac9e76b67f897dab335f7758f9cf7e61c0d53baf8bb6f9bd84259.proto)
  Character offset 212.

```text
e TrainBlunderChallenge {
  oneof _theme {
  .chesscom.train.v1.TrainTacticalTheme theme = 2;
  }
  optional .chesscom.train.v1.TrainChallengeBucket bucket = 1;
  optional .chesscom.chess.v1.Move correct_move = 3;
}

```

**Source references:** SRC-0572, SRC-1543  
**URL references:** None independently associated  
**Related findings:** FND-08910, FND-08911, FND-08912

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08914"></a>
## FND-08914: chesscom.train.v1.TrainBlunderChallenge.correct_move = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move correct_move = 3;

### Evidence

- **SRC-0572** `research/proto/chesscom/train/v1/train_blunder_challenge.proto` — [preserved redacted evidence](../evidence/text/d8c8193038cac9e76b67f897dab335f7758f9cf7e61c0d53baf8bb6f9bd84259.proto)
  Character offset 275.

```text
.TrainTacticalTheme theme = 2;
  }
  optional .chesscom.train.v1.TrainChallengeBucket bucket = 1;
  optional .chesscom.chess.v1.Move correct_move = 3;
}

```

**Source references:** SRC-0572, SRC-1543  
**URL references:** None independently associated  
**Related findings:** FND-08910, FND-08911, FND-08912

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08915"></a>
## FND-08915: message declaration: chesscom.train.v1.TrainChallenge

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TrainChallenge {

### Evidence

- **SRC-0573** `research/proto/chesscom/train/v1/train_challenge.proto` — [preserved redacted evidence](../evidence/text/8c7e91f8f956ab4dbdd3eac90052455ed46cd14d5456cff9ccb477c193b59cc5.proto)
  Character offset 98.

```text
// source: chesscom/train/v1/train_challenge.proto
// syntax: proto3

package chesscom.train.v1;

message TrainChallenge {
  oneof challenge {
  .chesscom.train.v1.TrainMissChallenge miss = 1;
  .chesscom.train.v1.TrainBlunderChallenge blunder = 2;
  .chesscom.train.v1.TrainOpeningMistakeChallenge opening_mistake = 3;
  .chesscom.train.v1.TrainStrategyMistakeChallenge strategy_mistake = 4;
  .chesscom.train.v1.Trai
```

**Source references:** SRC-0573, SRC-1544  
**URL references:** None independently associated  
**Related findings:** FND-08916, FND-08917

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08916"></a>
## FND-08916: oneof declaration: chesscom.train.v1.TrainChallenge.challenge

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof challenge {

### Evidence

- **SRC-0573** `research/proto/chesscom/train/v1/train_challenge.proto` — [preserved redacted evidence](../evidence/text/8c7e91f8f956ab4dbdd3eac90052455ed46cd14d5456cff9ccb477c193b59cc5.proto)
  Character offset 125.

```text
/v1/train_challenge.proto
// syntax: proto3

package chesscom.train.v1;

message TrainChallenge {
  oneof challenge {
  .chesscom.train.v1.TrainMissChallenge miss = 1;
  .chesscom.train.v1.TrainBlunderChallenge blunder = 2;
  .chesscom.train.v1.TrainOpeningMistakeChallenge opening_mistake = 3;
  .chesscom.train.v1.TrainStrategyMistakeChallenge strategy_mistake = 4;
  .chesscom.train.v1.TrainEndgameMistakeChallenge en
```

**Source references:** SRC-0573, SRC-1544  
**URL references:** None independently associated  
**Related findings:** FND-08915, FND-08917

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08917"></a>
## FND-08917: chesscom.train.v1.TrainChallenge.miss = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.train.v1.TrainMissChallenge miss = 1;

### Evidence

- **SRC-0573** `research/proto/chesscom/train/v1/train_challenge.proto` — [preserved redacted evidence](../evidence/text/8c7e91f8f956ab4dbdd3eac90052455ed46cd14d5456cff9ccb477c193b59cc5.proto)
  Character offset 145.

```text
proto
// syntax: proto3

package chesscom.train.v1;

message TrainChallenge {
  oneof challenge {
  .chesscom.train.v1.TrainMissChallenge miss = 1;
  .chesscom.train.v1.TrainBlunderChallenge blunder = 2;
  .chesscom.train.v1.TrainOpeningMistakeChallenge opening_mistake = 3;
  .chesscom.train.v1.TrainStrategyMistakeChallenge strategy_mistake = 4;
  .chesscom.train.v1.TrainEndgameMistakeChallenge endgame_mistake = 5;
 
```

**Source references:** SRC-0573, SRC-1544  
**URL references:** None independently associated  
**Related findings:** FND-08915, FND-08916

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08918"></a>
## FND-08918: chesscom.train.v1.TrainChallenge.blunder = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.train.v1.TrainBlunderChallenge blunder = 2;

### Evidence

- **SRC-0573** `research/proto/chesscom/train/v1/train_challenge.proto` — [preserved redacted evidence](../evidence/text/8c7e91f8f956ab4dbdd3eac90052455ed46cd14d5456cff9ccb477c193b59cc5.proto)
  Character offset 195.

```text
;

message TrainChallenge {
  oneof challenge {
  .chesscom.train.v1.TrainMissChallenge miss = 1;
  .chesscom.train.v1.TrainBlunderChallenge blunder = 2;
  .chesscom.train.v1.TrainOpeningMistakeChallenge opening_mistake = 3;
  .chesscom.train.v1.TrainStrategyMistakeChallenge strategy_mistake = 4;
  .chesscom.train.v1.TrainEndgameMistakeChallenge endgame_mistake = 5;
  }
}

```

**Source references:** SRC-0573, SRC-1544  
**URL references:** None independently associated  
**Related findings:** FND-08915, FND-08916, FND-08917

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08919"></a>
## FND-08919: chesscom.train.v1.TrainChallenge.opening_mistake = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.train.v1.TrainOpeningMistakeChallenge opening_mistake = 3;

### Evidence

- **SRC-0573** `research/proto/chesscom/train/v1/train_challenge.proto` — [preserved redacted evidence](../evidence/text/8c7e91f8f956ab4dbdd3eac90052455ed46cd14d5456cff9ccb477c193b59cc5.proto)
  Character offset 251.

```text
com.train.v1.TrainMissChallenge miss = 1;
  .chesscom.train.v1.TrainBlunderChallenge blunder = 2;
  .chesscom.train.v1.TrainOpeningMistakeChallenge opening_mistake = 3;
  .chesscom.train.v1.TrainStrategyMistakeChallenge strategy_mistake = 4;
  .chesscom.train.v1.TrainEndgameMistakeChallenge endgame_mistake = 5;
  }
}

```

**Source references:** SRC-0573, SRC-1544  
**URL references:** None independently associated  
**Related findings:** FND-08915, FND-08916, FND-08917

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08920"></a>
## FND-08920: chesscom.train.v1.TrainChallenge.strategy_mistake = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.train.v1.TrainStrategyMistakeChallenge strategy_mistake = 4;

### Evidence

- **SRC-0573** `research/proto/chesscom/train/v1/train_challenge.proto` — [preserved redacted evidence](../evidence/text/8c7e91f8f956ab4dbdd3eac90052455ed46cd14d5456cff9ccb477c193b59cc5.proto)
  Character offset 322.

```text
nderChallenge blunder = 2;
  .chesscom.train.v1.TrainOpeningMistakeChallenge opening_mistake = 3;
  .chesscom.train.v1.TrainStrategyMistakeChallenge strategy_mistake = 4;
  .chesscom.train.v1.TrainEndgameMistakeChallenge endgame_mistake = 5;
  }
}

```

**Source references:** SRC-0573, SRC-1544  
**URL references:** None independently associated  
**Related findings:** FND-08915, FND-08916, FND-08917

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08921"></a>
## FND-08921: chesscom.train.v1.TrainChallenge.endgame_mistake = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.train.v1.TrainEndgameMistakeChallenge endgame_mistake = 5;

### Evidence

- **SRC-0573** `research/proto/chesscom/train/v1/train_challenge.proto` — [preserved redacted evidence](../evidence/text/8c7e91f8f956ab4dbdd3eac90052455ed46cd14d5456cff9ccb477c193b59cc5.proto)
  Character offset 395.

```text
nge opening_mistake = 3;
  .chesscom.train.v1.TrainStrategyMistakeChallenge strategy_mistake = 4;
  .chesscom.train.v1.TrainEndgameMistakeChallenge endgame_mistake = 5;
  }
}

```

**Source references:** SRC-0573, SRC-1544  
**URL references:** None independently associated  
**Related findings:** FND-08915, FND-08916, FND-08917

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08922"></a>
## FND-08922: enum declaration: chesscom.train.v1.TrainChallengeBucket

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TrainChallengeBucket {

### Evidence

- **SRC-0574** `research/proto/chesscom/train/v1/train_challenge_bucket.proto` — [preserved redacted evidence](../evidence/text/83d43ffd0d7d5e1c9737748b832ac527addee1b3c594551abdbf1549f8cfdebb.proto)
  Character offset 105.

```text
urce: chesscom/train/v1/train_challenge_bucket.proto
// syntax: proto3

package chesscom.train.v1;

enum TrainChallengeBucket {
  TRAIN_CHALLENGE_BUCKET_UNSPECIFIED = 0;
  TRAIN_CHALLENGE_BUCKET_FREE_PIECES = 1;
  TRAIN_CHALLENGE_BUCKET_TACTICS = 2;
  TRAIN_CHALLENGE_BUCKET_LEADS_TO = 3;
  TRAIN_CHALLENGE_BUCKET_BRILLIANT = 4;
}

```

**Source references:** SRC-0574, SRC-1545  
**URL references:** None independently associated  
**Related findings:** FND-08923, FND-08924

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08923"></a>
## FND-08923: chesscom.train.v1.TrainChallengeBucket.TRAIN_CHALLENGE_BUCKET_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_CHALLENGE_BUCKET_UNSPECIFIED = 0;

### Evidence

- **SRC-0574** `research/proto/chesscom/train/v1/train_challenge_bucket.proto` — [preserved redacted evidence](../evidence/text/83d43ffd0d7d5e1c9737748b832ac527addee1b3c594551abdbf1549f8cfdebb.proto)
  Character offset 135.

```text
challenge_bucket.proto
// syntax: proto3

package chesscom.train.v1;

enum TrainChallengeBucket {
  TRAIN_CHALLENGE_BUCKET_UNSPECIFIED = 0;
  TRAIN_CHALLENGE_BUCKET_FREE_PIECES = 1;
  TRAIN_CHALLENGE_BUCKET_TACTICS = 2;
  TRAIN_CHALLENGE_BUCKET_LEADS_TO = 3;
  TRAIN_CHALLENGE_BUCKET_BRILLIANT = 4;
}

```

**Source references:** SRC-0574, SRC-1545  
**URL references:** None independently associated  
**Related findings:** FND-08922, FND-08924

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08924"></a>
## FND-08924: chesscom.train.v1.TrainChallengeBucket.TRAIN_CHALLENGE_BUCKET_FREE_PIECES = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_CHALLENGE_BUCKET_FREE_PIECES = 1;

### Evidence

- **SRC-0574** `research/proto/chesscom/train/v1/train_challenge_bucket.proto` — [preserved redacted evidence](../evidence/text/83d43ffd0d7d5e1c9737748b832ac527addee1b3c594551abdbf1549f8cfdebb.proto)
  Character offset 177.

```text
package chesscom.train.v1;

enum TrainChallengeBucket {
  TRAIN_CHALLENGE_BUCKET_UNSPECIFIED = 0;
  TRAIN_CHALLENGE_BUCKET_FREE_PIECES = 1;
  TRAIN_CHALLENGE_BUCKET_TACTICS = 2;
  TRAIN_CHALLENGE_BUCKET_LEADS_TO = 3;
  TRAIN_CHALLENGE_BUCKET_BRILLIANT = 4;
}

```

**Source references:** SRC-0574, SRC-1545  
**URL references:** None independently associated  
**Related findings:** FND-08922, FND-08923

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08925"></a>
## FND-08925: chesscom.train.v1.TrainChallengeBucket.TRAIN_CHALLENGE_BUCKET_TACTICS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_CHALLENGE_BUCKET_TACTICS = 2;

### Evidence

- **SRC-0574** `research/proto/chesscom/train/v1/train_challenge_bucket.proto` — [preserved redacted evidence](../evidence/text/83d43ffd0d7d5e1c9737748b832ac527addee1b3c594551abdbf1549f8cfdebb.proto)
  Character offset 219.

```text
lengeBucket {
  TRAIN_CHALLENGE_BUCKET_UNSPECIFIED = 0;
  TRAIN_CHALLENGE_BUCKET_FREE_PIECES = 1;
  TRAIN_CHALLENGE_BUCKET_TACTICS = 2;
  TRAIN_CHALLENGE_BUCKET_LEADS_TO = 3;
  TRAIN_CHALLENGE_BUCKET_BRILLIANT = 4;
}

```

**Source references:** SRC-0574, SRC-1545  
**URL references:** None independently associated  
**Related findings:** FND-08922, FND-08923, FND-08924

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08926"></a>
## FND-08926: chesscom.train.v1.TrainChallengeBucket.TRAIN_CHALLENGE_BUCKET_LEADS_TO = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_CHALLENGE_BUCKET_LEADS_TO = 3;

### Evidence

- **SRC-0574** `research/proto/chesscom/train/v1/train_challenge_bucket.proto` — [preserved redacted evidence](../evidence/text/83d43ffd0d7d5e1c9737748b832ac527addee1b3c594551abdbf1549f8cfdebb.proto)
  Character offset 257.

```text
_UNSPECIFIED = 0;
  TRAIN_CHALLENGE_BUCKET_FREE_PIECES = 1;
  TRAIN_CHALLENGE_BUCKET_TACTICS = 2;
  TRAIN_CHALLENGE_BUCKET_LEADS_TO = 3;
  TRAIN_CHALLENGE_BUCKET_BRILLIANT = 4;
}

```

**Source references:** SRC-0574, SRC-1545  
**URL references:** None independently associated  
**Related findings:** FND-08922, FND-08923, FND-08924

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08927"></a>
## FND-08927: chesscom.train.v1.TrainChallengeBucket.TRAIN_CHALLENGE_BUCKET_BRILLIANT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_CHALLENGE_BUCKET_BRILLIANT = 4;

### Evidence

- **SRC-0574** `research/proto/chesscom/train/v1/train_challenge_bucket.proto` — [preserved redacted evidence](../evidence/text/83d43ffd0d7d5e1c9737748b832ac527addee1b3c594551abdbf1549f8cfdebb.proto)
  Character offset 296.

```text
KET_FREE_PIECES = 1;
  TRAIN_CHALLENGE_BUCKET_TACTICS = 2;
  TRAIN_CHALLENGE_BUCKET_LEADS_TO = 3;
  TRAIN_CHALLENGE_BUCKET_BRILLIANT = 4;
}

```

**Source references:** SRC-0574, SRC-1545  
**URL references:** None independently associated  
**Related findings:** FND-08922, FND-08923, FND-08924

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08928"></a>
## FND-08928: message declaration: chesscom.train.v1.TrainEndgameMistakeChallenge

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TrainEndgameMistakeChallenge {

### Evidence

- **SRC-0575** `research/proto/chesscom/train/v1/train_endgame_mistake_challenge.proto` — [preserved redacted evidence](../evidence/text/2554b37c8b86557c82e069e3f8d6080c02c80cf61fc1fd6f50e3d5dfb38cd38d.proto)
  Character offset 114.

```text
sscom/train/v1/train_endgame_mistake_challenge.proto
// syntax: proto3

package chesscom.train.v1;

message TrainEndgameMistakeChallenge {
  optional .chesscom.train.v1.TrainEndgameTheme theme = 1;
  optional .chesscom.chess.v1.Move correct_move = 2;
}

```

**Source references:** SRC-0575, SRC-1546  
**URL references:** None independently associated  
**Related findings:** FND-08929, FND-08930

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08929"></a>
## FND-08929: chesscom.train.v1.TrainEndgameMistakeChallenge.theme = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.train.v1.TrainEndgameTheme theme = 1;

### Evidence

- **SRC-0575** `research/proto/chesscom/train/v1/train_endgame_mistake_challenge.proto` — [preserved redacted evidence](../evidence/text/2554b37c8b86557c82e069e3f8d6080c02c80cf61fc1fd6f50e3d5dfb38cd38d.proto)
  Character offset 155.

```text
lenge.proto
// syntax: proto3

package chesscom.train.v1;

message TrainEndgameMistakeChallenge {
  optional .chesscom.train.v1.TrainEndgameTheme theme = 1;
  optional .chesscom.chess.v1.Move correct_move = 2;
}

```

**Source references:** SRC-0575, SRC-1546  
**URL references:** None independently associated  
**Related findings:** FND-08928, FND-08930

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08930"></a>
## FND-08930: chesscom.train.v1.TrainEndgameMistakeChallenge.correct_move = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move correct_move = 2;

### Evidence

- **SRC-0575** `research/proto/chesscom/train/v1/train_endgame_mistake_challenge.proto` — [preserved redacted evidence](../evidence/text/2554b37c8b86557c82e069e3f8d6080c02c80cf61fc1fd6f50e3d5dfb38cd38d.proto)
  Character offset 214.

```text
message TrainEndgameMistakeChallenge {
  optional .chesscom.train.v1.TrainEndgameTheme theme = 1;
  optional .chesscom.chess.v1.Move correct_move = 2;
}

```

**Source references:** SRC-0575, SRC-1546  
**URL references:** None independently associated  
**Related findings:** FND-08928, FND-08929

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08931"></a>
## FND-08931: enum declaration: chesscom.train.v1.TrainEndgameTheme

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TrainEndgameTheme {

### Evidence

- **SRC-0576** `research/proto/chesscom/train/v1/train_endgame_theme.proto` — [preserved redacted evidence](../evidence/text/b12d8912120db95113debc6ca11c000f04042fd933eb20836077967c35ee0cbb.proto)
  Character offset 102.

```text
 source: chesscom/train/v1/train_endgame_theme.proto
// syntax: proto3

package chesscom.train.v1;

enum TrainEndgameTheme {
  TRAIN_ENDGAME_THEME_UNSPECIFIED = 0;
  TRAIN_ENDGAME_THEME_QUEEN = 1;
  TRAIN_ENDGAME_THEME_ROOK_AND_PAWN = 2;
  TRAIN_ENDGAME_THEME_KING_AND_PAWN = 3;
  TRAIN_ENDGAME_THEME_OTHER = 4;
}

```

**Source references:** SRC-0576, SRC-1547  
**URL references:** None independently associated  
**Related findings:** FND-08932, FND-08933

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08932"></a>
## FND-08932: chesscom.train.v1.TrainEndgameTheme.TRAIN_ENDGAME_THEME_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_ENDGAME_THEME_UNSPECIFIED = 0;

### Evidence

- **SRC-0576** `research/proto/chesscom/train/v1/train_endgame_theme.proto` — [preserved redacted evidence](../evidence/text/b12d8912120db95113debc6ca11c000f04042fd933eb20836077967c35ee0cbb.proto)
  Character offset 129.

```text
train_endgame_theme.proto
// syntax: proto3

package chesscom.train.v1;

enum TrainEndgameTheme {
  TRAIN_ENDGAME_THEME_UNSPECIFIED = 0;
  TRAIN_ENDGAME_THEME_QUEEN = 1;
  TRAIN_ENDGAME_THEME_ROOK_AND_PAWN = 2;
  TRAIN_ENDGAME_THEME_KING_AND_PAWN = 3;
  TRAIN_ENDGAME_THEME_OTHER = 4;
}

```

**Source references:** SRC-0576, SRC-1547  
**URL references:** None independently associated  
**Related findings:** FND-08931, FND-08933

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08933"></a>
## FND-08933: chesscom.train.v1.TrainEndgameTheme.TRAIN_ENDGAME_THEME_QUEEN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_ENDGAME_THEME_QUEEN = 1;

### Evidence

- **SRC-0576** `research/proto/chesscom/train/v1/train_endgame_theme.proto` — [preserved redacted evidence](../evidence/text/b12d8912120db95113debc6ca11c000f04042fd933eb20836077967c35ee0cbb.proto)
  Character offset 168.

```text
oto3

package chesscom.train.v1;

enum TrainEndgameTheme {
  TRAIN_ENDGAME_THEME_UNSPECIFIED = 0;
  TRAIN_ENDGAME_THEME_QUEEN = 1;
  TRAIN_ENDGAME_THEME_ROOK_AND_PAWN = 2;
  TRAIN_ENDGAME_THEME_KING_AND_PAWN = 3;
  TRAIN_ENDGAME_THEME_OTHER = 4;
}

```

**Source references:** SRC-0576, SRC-1547  
**URL references:** None independently associated  
**Related findings:** FND-08931, FND-08932

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08934"></a>
## FND-08934: chesscom.train.v1.TrainEndgameTheme.TRAIN_ENDGAME_THEME_ROOK_AND_PAWN = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_ENDGAME_THEME_ROOK_AND_PAWN = 2;

### Evidence

- **SRC-0576** `research/proto/chesscom/train/v1/train_endgame_theme.proto` — [preserved redacted evidence](../evidence/text/b12d8912120db95113debc6ca11c000f04042fd933eb20836077967c35ee0cbb.proto)
  Character offset 201.

```text

enum TrainEndgameTheme {
  TRAIN_ENDGAME_THEME_UNSPECIFIED = 0;
  TRAIN_ENDGAME_THEME_QUEEN = 1;
  TRAIN_ENDGAME_THEME_ROOK_AND_PAWN = 2;
  TRAIN_ENDGAME_THEME_KING_AND_PAWN = 3;
  TRAIN_ENDGAME_THEME_OTHER = 4;
}

```

**Source references:** SRC-0576, SRC-1547  
**URL references:** None independently associated  
**Related findings:** FND-08931, FND-08932, FND-08933

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08935"></a>
## FND-08935: chesscom.train.v1.TrainEndgameTheme.TRAIN_ENDGAME_THEME_KING_AND_PAWN = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_ENDGAME_THEME_KING_AND_PAWN = 3;

### Evidence

- **SRC-0576** `research/proto/chesscom/train/v1/train_endgame_theme.proto` — [preserved redacted evidence](../evidence/text/b12d8912120db95113debc6ca11c000f04042fd933eb20836077967c35ee0cbb.proto)
  Character offset 242.

```text
_THEME_UNSPECIFIED = 0;
  TRAIN_ENDGAME_THEME_QUEEN = 1;
  TRAIN_ENDGAME_THEME_ROOK_AND_PAWN = 2;
  TRAIN_ENDGAME_THEME_KING_AND_PAWN = 3;
  TRAIN_ENDGAME_THEME_OTHER = 4;
}

```

**Source references:** SRC-0576, SRC-1547  
**URL references:** None independently associated  
**Related findings:** FND-08931, FND-08932, FND-08933

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08936"></a>
## FND-08936: chesscom.train.v1.TrainEndgameTheme.TRAIN_ENDGAME_THEME_OTHER = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_ENDGAME_THEME_OTHER = 4;

### Evidence

- **SRC-0576** `research/proto/chesscom/train/v1/train_endgame_theme.proto` — [preserved redacted evidence](../evidence/text/b12d8912120db95113debc6ca11c000f04042fd933eb20836077967c35ee0cbb.proto)
  Character offset 283.

```text
HEME_QUEEN = 1;
  TRAIN_ENDGAME_THEME_ROOK_AND_PAWN = 2;
  TRAIN_ENDGAME_THEME_KING_AND_PAWN = 3;
  TRAIN_ENDGAME_THEME_OTHER = 4;
}

```

**Source references:** SRC-0576, SRC-1547  
**URL references:** None independently associated  
**Related findings:** FND-08931, FND-08932, FND-08933

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08937"></a>
## FND-08937: enum declaration: chesscom.train.v1.TrainItemType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TrainItemType {

### Evidence

- **SRC-0577** `research/proto/chesscom/train/v1/train_item_type.proto` — [preserved redacted evidence](../evidence/text/d22fda725f05a25d045bda17e4bc99496f819fe5eab7a234f84d0f24e97fd15a.proto)
  Character offset 98.

```text
// source: chesscom/train/v1/train_item_type.proto
// syntax: proto3

package chesscom.train.v1;

enum TrainItemType {
  TRAIN_ITEM_TYPE_UNSPECIFIED = 0;
  TRAIN_ITEM_TYPE_RETRY_MISS = 1;
  TRAIN_ITEM_TYPE_RETRY_BLUNDER = 2;
  TRAIN_ITEM_TYPE_RETRY_OPENING_MISTAKE = 3;
  TRAIN_ITEM_TYPE_RETRY_STRATEGY_MISTAKE = 4;
  TRAIN_ITEM_TYPE_RETRY_ENDGAME_MISTAKE = 5;
}

```

**Source references:** SRC-0577, SRC-1548  
**URL references:** None independently associated  
**Related findings:** FND-08938, FND-08939

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08938"></a>
## FND-08938: chesscom.train.v1.TrainItemType.TRAIN_ITEM_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_ITEM_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0577** `research/proto/chesscom/train/v1/train_item_type.proto` — [preserved redacted evidence](../evidence/text/d22fda725f05a25d045bda17e4bc99496f819fe5eab7a234f84d0f24e97fd15a.proto)
  Character offset 121.

```text
rain/v1/train_item_type.proto
// syntax: proto3

package chesscom.train.v1;

enum TrainItemType {
  TRAIN_ITEM_TYPE_UNSPECIFIED = 0;
  TRAIN_ITEM_TYPE_RETRY_MISS = 1;
  TRAIN_ITEM_TYPE_RETRY_BLUNDER = 2;
  TRAIN_ITEM_TYPE_RETRY_OPENING_MISTAKE = 3;
  TRAIN_ITEM_TYPE_RETRY_STRATEGY_MISTAKE = 4;
  TRAIN_ITEM_TYPE_RETRY_ENDGAME_MISTAKE = 5;
}

```

**Source references:** SRC-0577, SRC-1548  
**URL references:** None independently associated  
**Related findings:** FND-08937, FND-08939

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08939"></a>
## FND-08939: chesscom.train.v1.TrainItemType.TRAIN_ITEM_TYPE_RETRY_MISS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_ITEM_TYPE_RETRY_MISS = 1;

### Evidence

- **SRC-0577** `research/proto/chesscom/train/v1/train_item_type.proto` — [preserved redacted evidence](../evidence/text/d22fda725f05a25d045bda17e4bc99496f819fe5eab7a234f84d0f24e97fd15a.proto)
  Character offset 156.

```text
ntax: proto3

package chesscom.train.v1;

enum TrainItemType {
  TRAIN_ITEM_TYPE_UNSPECIFIED = 0;
  TRAIN_ITEM_TYPE_RETRY_MISS = 1;
  TRAIN_ITEM_TYPE_RETRY_BLUNDER = 2;
  TRAIN_ITEM_TYPE_RETRY_OPENING_MISTAKE = 3;
  TRAIN_ITEM_TYPE_RETRY_STRATEGY_MISTAKE = 4;
  TRAIN_ITEM_TYPE_RETRY_ENDGAME_MISTAKE = 5;
}

```

**Source references:** SRC-0577, SRC-1548  
**URL references:** None independently associated  
**Related findings:** FND-08937, FND-08938

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08940"></a>
## FND-08940: chesscom.train.v1.TrainItemType.TRAIN_ITEM_TYPE_RETRY_BLUNDER = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_ITEM_TYPE_RETRY_BLUNDER = 2;

### Evidence

- **SRC-0577** `research/proto/chesscom/train/v1/train_item_type.proto` — [preserved redacted evidence](../evidence/text/d22fda725f05a25d045bda17e4bc99496f819fe5eab7a234f84d0f24e97fd15a.proto)
  Character offset 190.

```text
in.v1;

enum TrainItemType {
  TRAIN_ITEM_TYPE_UNSPECIFIED = 0;
  TRAIN_ITEM_TYPE_RETRY_MISS = 1;
  TRAIN_ITEM_TYPE_RETRY_BLUNDER = 2;
  TRAIN_ITEM_TYPE_RETRY_OPENING_MISTAKE = 3;
  TRAIN_ITEM_TYPE_RETRY_STRATEGY_MISTAKE = 4;
  TRAIN_ITEM_TYPE_RETRY_ENDGAME_MISTAKE = 5;
}

```

**Source references:** SRC-0577, SRC-1548  
**URL references:** None independently associated  
**Related findings:** FND-08937, FND-08938, FND-08939

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08941"></a>
## FND-08941: chesscom.train.v1.TrainItemType.TRAIN_ITEM_TYPE_RETRY_OPENING_MISTAKE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_ITEM_TYPE_RETRY_OPENING_MISTAKE = 3;

### Evidence

- **SRC-0577** `research/proto/chesscom/train/v1/train_item_type.proto` — [preserved redacted evidence](../evidence/text/d22fda725f05a25d045bda17e4bc99496f819fe5eab7a234f84d0f24e97fd15a.proto)
  Character offset 227.

```text
ITEM_TYPE_UNSPECIFIED = 0;
  TRAIN_ITEM_TYPE_RETRY_MISS = 1;
  TRAIN_ITEM_TYPE_RETRY_BLUNDER = 2;
  TRAIN_ITEM_TYPE_RETRY_OPENING_MISTAKE = 3;
  TRAIN_ITEM_TYPE_RETRY_STRATEGY_MISTAKE = 4;
  TRAIN_ITEM_TYPE_RETRY_ENDGAME_MISTAKE = 5;
}

```

**Source references:** SRC-0577, SRC-1548  
**URL references:** None independently associated  
**Related findings:** FND-08937, FND-08938, FND-08939

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08942"></a>
## FND-08942: chesscom.train.v1.TrainItemType.TRAIN_ITEM_TYPE_RETRY_STRATEGY_MISTAKE = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_ITEM_TYPE_RETRY_STRATEGY_MISTAKE = 4;

### Evidence

- **SRC-0577** `research/proto/chesscom/train/v1/train_item_type.proto` — [preserved redacted evidence](../evidence/text/d22fda725f05a25d045bda17e4bc99496f819fe5eab7a234f84d0f24e97fd15a.proto)
  Character offset 272.

```text
RETRY_MISS = 1;
  TRAIN_ITEM_TYPE_RETRY_BLUNDER = 2;
  TRAIN_ITEM_TYPE_RETRY_OPENING_MISTAKE = 3;
  TRAIN_ITEM_TYPE_RETRY_STRATEGY_MISTAKE = 4;
  TRAIN_ITEM_TYPE_RETRY_ENDGAME_MISTAKE = 5;
}

```

**Source references:** SRC-0577, SRC-1548  
**URL references:** None independently associated  
**Related findings:** FND-08937, FND-08938, FND-08939

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08943"></a>
## FND-08943: chesscom.train.v1.TrainItemType.TRAIN_ITEM_TYPE_RETRY_ENDGAME_MISTAKE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_ITEM_TYPE_RETRY_ENDGAME_MISTAKE = 5;

### Evidence

- **SRC-0577** `research/proto/chesscom/train/v1/train_item_type.proto` — [preserved redacted evidence](../evidence/text/d22fda725f05a25d045bda17e4bc99496f819fe5eab7a234f84d0f24e97fd15a.proto)
  Character offset 318.

```text
R = 2;
  TRAIN_ITEM_TYPE_RETRY_OPENING_MISTAKE = 3;
  TRAIN_ITEM_TYPE_RETRY_STRATEGY_MISTAKE = 4;
  TRAIN_ITEM_TYPE_RETRY_ENDGAME_MISTAKE = 5;
}

```

**Source references:** SRC-0577, SRC-1548  
**URL references:** None independently associated  
**Related findings:** FND-08937, FND-08938, FND-08939

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08944"></a>
## FND-08944: enum declaration: chesscom.train.v1.TrainMembershipContext

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TrainMembershipContext {

### Evidence

- **SRC-0578** `research/proto/chesscom/train/v1/train_membership_context.proto` — [preserved redacted evidence](../evidence/text/1001ece970dff6f2af48f1fdd924e4406ddc94d179e7c4d55e5cceb7d7bf5907.proto)
  Character offset 107.

```text
ce: chesscom/train/v1/train_membership_context.proto
// syntax: proto3

package chesscom.train.v1;

enum TrainMembershipContext {
  TRAIN_MEMBERSHIP_CONTEXT_UNSPECIFIED = 0;
  TRAIN_MEMBERSHIP_CONTEXT_PRO = 1;
  TRAIN_MEMBERSHIP_CONTEXT_FREEVIEW = 2;
}

```

**Source references:** SRC-0578, SRC-1549  
**URL references:** None independently associated  
**Related findings:** FND-08945, FND-08946

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08945"></a>
## FND-08945: chesscom.train.v1.TrainMembershipContext.TRAIN_MEMBERSHIP_CONTEXT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_MEMBERSHIP_CONTEXT_UNSPECIFIED = 0;

### Evidence

- **SRC-0578** `research/proto/chesscom/train/v1/train_membership_context.proto` — [preserved redacted evidence](../evidence/text/1001ece970dff6f2af48f1fdd924e4406ddc94d179e7c4d55e5cceb7d7bf5907.proto)
  Character offset 139.

```text
ership_context.proto
// syntax: proto3

package chesscom.train.v1;

enum TrainMembershipContext {
  TRAIN_MEMBERSHIP_CONTEXT_UNSPECIFIED = 0;
  TRAIN_MEMBERSHIP_CONTEXT_PRO = 1;
  TRAIN_MEMBERSHIP_CONTEXT_FREEVIEW = 2;
}

```

**Source references:** SRC-0578, SRC-1549  
**URL references:** None independently associated  
**Related findings:** FND-08944, FND-08946

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08946"></a>
## FND-08946: chesscom.train.v1.TrainMembershipContext.TRAIN_MEMBERSHIP_CONTEXT_PRO = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_MEMBERSHIP_CONTEXT_PRO = 1;

### Evidence

- **SRC-0578** `research/proto/chesscom/train/v1/train_membership_context.proto` — [preserved redacted evidence](../evidence/text/1001ece970dff6f2af48f1fdd924e4406ddc94d179e7c4d55e5cceb7d7bf5907.proto)
  Character offset 183.

```text
age chesscom.train.v1;

enum TrainMembershipContext {
  TRAIN_MEMBERSHIP_CONTEXT_UNSPECIFIED = 0;
  TRAIN_MEMBERSHIP_CONTEXT_PRO = 1;
  TRAIN_MEMBERSHIP_CONTEXT_FREEVIEW = 2;
}

```

**Source references:** SRC-0578, SRC-1549  
**URL references:** None independently associated  
**Related findings:** FND-08944, FND-08945

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08947"></a>
## FND-08947: chesscom.train.v1.TrainMembershipContext.TRAIN_MEMBERSHIP_CONTEXT_FREEVIEW = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_MEMBERSHIP_CONTEXT_FREEVIEW = 2;

### Evidence

- **SRC-0578** `research/proto/chesscom/train/v1/train_membership_context.proto` — [preserved redacted evidence](../evidence/text/1001ece970dff6f2af48f1fdd924e4406ddc94d179e7c4d55e5cceb7d7bf5907.proto)
  Character offset 219.

```text
mbershipContext {
  TRAIN_MEMBERSHIP_CONTEXT_UNSPECIFIED = 0;
  TRAIN_MEMBERSHIP_CONTEXT_PRO = 1;
  TRAIN_MEMBERSHIP_CONTEXT_FREEVIEW = 2;
}

```

**Source references:** SRC-0578, SRC-1549  
**URL references:** None independently associated  
**Related findings:** FND-08944, FND-08945, FND-08946

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08948"></a>
## FND-08948: message declaration: chesscom.train.v1.TrainMissChallenge

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TrainMissChallenge {

### Evidence

- **SRC-0579** `research/proto/chesscom/train/v1/train_miss_challenge.proto` — [preserved redacted evidence](../evidence/text/0ead791975993d2bbdbc0ead96c68f62c855a35b24f33809530128cfca045d50.proto)
  Character offset 103.

```text
source: chesscom/train/v1/train_miss_challenge.proto
// syntax: proto3

package chesscom.train.v1;

message TrainMissChallenge {
  oneof _theme {
  .chesscom.train.v1.TrainTacticalTheme theme = 2;
  }
  optional .chesscom.train.v1.TrainChallengeBucket bucket = 1;
  optional .chesscom.chess.v1.Move correct_move = 3;
  optional bool is_critical = 4;
}

```

**Source references:** SRC-0579, SRC-1550  
**URL references:** None independently associated  
**Related findings:** FND-08949, FND-08950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08949"></a>
## FND-08949: oneof declaration: chesscom.train.v1.TrainMissChallenge._theme

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _theme {

### Evidence

- **SRC-0579** `research/proto/chesscom/train/v1/train_miss_challenge.proto` — [preserved redacted evidence](../evidence/text/0ead791975993d2bbdbc0ead96c68f62c855a35b24f33809530128cfca045d50.proto)
  Character offset 134.

```text
_miss_challenge.proto
// syntax: proto3

package chesscom.train.v1;

message TrainMissChallenge {
  oneof _theme {
  .chesscom.train.v1.TrainTacticalTheme theme = 2;
  }
  optional .chesscom.train.v1.TrainChallengeBucket bucket = 1;
  optional .chesscom.chess.v1.Move correct_move = 3;
  optional bool is_critical = 4;
}

```

**Source references:** SRC-0579, SRC-1550  
**URL references:** None independently associated  
**Related findings:** FND-08948, FND-08950

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08950"></a>
## FND-08950: chesscom.train.v1.TrainMissChallenge.theme = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.train.v1.TrainTacticalTheme theme = 2;

### Evidence

- **SRC-0579** `research/proto/chesscom/train/v1/train_miss_challenge.proto` — [preserved redacted evidence](../evidence/text/0ead791975993d2bbdbc0ead96c68f62c855a35b24f33809530128cfca045d50.proto)
  Character offset 151.

```text
roto
// syntax: proto3

package chesscom.train.v1;

message TrainMissChallenge {
  oneof _theme {
  .chesscom.train.v1.TrainTacticalTheme theme = 2;
  }
  optional .chesscom.train.v1.TrainChallengeBucket bucket = 1;
  optional .chesscom.chess.v1.Move correct_move = 3;
  optional bool is_critical = 4;
}

```

**Source references:** SRC-0579, SRC-1550  
**URL references:** None independently associated  
**Related findings:** FND-08948, FND-08949

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08951"></a>
## FND-08951: chesscom.train.v1.TrainMissChallenge.bucket = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.train.v1.TrainChallengeBucket bucket = 1;

### Evidence

- **SRC-0579** `research/proto/chesscom/train/v1/train_miss_challenge.proto` — [preserved redacted evidence](../evidence/text/0ead791975993d2bbdbc0ead96c68f62c855a35b24f33809530128cfca045d50.proto)
  Character offset 206.

```text
sage TrainMissChallenge {
  oneof _theme {
  .chesscom.train.v1.TrainTacticalTheme theme = 2;
  }
  optional .chesscom.train.v1.TrainChallengeBucket bucket = 1;
  optional .chesscom.chess.v1.Move correct_move = 3;
  optional bool is_critical = 4;
}

```

**Source references:** SRC-0579, SRC-1550  
**URL references:** None independently associated  
**Related findings:** FND-08948, FND-08949, FND-08950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08952"></a>
## FND-08952: chesscom.train.v1.TrainMissChallenge.correct_move = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move correct_move = 3;

### Evidence

- **SRC-0579** `research/proto/chesscom/train/v1/train_miss_challenge.proto` — [preserved redacted evidence](../evidence/text/0ead791975993d2bbdbc0ead96c68f62c855a35b24f33809530128cfca045d50.proto)
  Character offset 269.

```text
.TrainTacticalTheme theme = 2;
  }
  optional .chesscom.train.v1.TrainChallengeBucket bucket = 1;
  optional .chesscom.chess.v1.Move correct_move = 3;
  optional bool is_critical = 4;
}

```

**Source references:** SRC-0579, SRC-1550  
**URL references:** None independently associated  
**Related findings:** FND-08948, FND-08949, FND-08950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08953"></a>
## FND-08953: chesscom.train.v1.TrainMissChallenge.is_critical = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_critical = 4;

### Evidence

- **SRC-0579** `research/proto/chesscom/train/v1/train_miss_challenge.proto` — [preserved redacted evidence](../evidence/text/0ead791975993d2bbdbc0ead96c68f62c855a35b24f33809530128cfca045d50.proto)
  Character offset 322.

```text
om.train.v1.TrainChallengeBucket bucket = 1;
  optional .chesscom.chess.v1.Move correct_move = 3;
  optional bool is_critical = 4;
}

```

**Source references:** SRC-0579, SRC-1550  
**URL references:** None independently associated  
**Related findings:** FND-08948, FND-08949, FND-08950

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08954"></a>
## FND-08954: message declaration: chesscom.train.v1.TrainOpeningMistakeChallenge

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TrainOpeningMistakeChallenge {

### Evidence

- **SRC-0580** `research/proto/chesscom/train/v1/train_opening_mistake_challenge.proto` — [preserved redacted evidence](../evidence/text/f134c40907e863c64a660fc0ad171b8e9dc95f9a710cf7c7b8d6ff9098d89b99.proto)
  Character offset 114.

```text
sscom/train/v1/train_opening_mistake_challenge.proto
// syntax: proto3

package chesscom.train.v1;

message TrainOpeningMistakeChallenge {
  optional int32 eco_family_id = 1;
  optional .chesscom.train.v1.TrainOpeningTheme theme = 2;
  optional .chesscom.chess.v1.Move correct_move = 3;
}

```

**Source references:** SRC-0580, SRC-1551  
**URL references:** None independently associated  
**Related findings:** FND-08955, FND-08956

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08955"></a>
## FND-08955: chesscom.train.v1.TrainOpeningMistakeChallenge.eco_family_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 eco_family_id = 1;

### Evidence

- **SRC-0580** `research/proto/chesscom/train/v1/train_opening_mistake_challenge.proto` — [preserved redacted evidence](../evidence/text/f134c40907e863c64a660fc0ad171b8e9dc95f9a710cf7c7b8d6ff9098d89b99.proto)
  Character offset 155.

```text
lenge.proto
// syntax: proto3

package chesscom.train.v1;

message TrainOpeningMistakeChallenge {
  optional int32 eco_family_id = 1;
  optional .chesscom.train.v1.TrainOpeningTheme theme = 2;
  optional .chesscom.chess.v1.Move correct_move = 3;
}

```

**Source references:** SRC-0580, SRC-1551  
**URL references:** None independently associated  
**Related findings:** FND-08954, FND-08956

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08956"></a>
## FND-08956: chesscom.train.v1.TrainOpeningMistakeChallenge.theme = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.train.v1.TrainOpeningTheme theme = 2;

### Evidence

- **SRC-0580** `research/proto/chesscom/train/v1/train_opening_mistake_challenge.proto` — [preserved redacted evidence](../evidence/text/f134c40907e863c64a660fc0ad171b8e9dc95f9a710cf7c7b8d6ff9098d89b99.proto)
  Character offset 191.

```text
ge chesscom.train.v1;

message TrainOpeningMistakeChallenge {
  optional int32 eco_family_id = 1;
  optional .chesscom.train.v1.TrainOpeningTheme theme = 2;
  optional .chesscom.chess.v1.Move correct_move = 3;
}

```

**Source references:** SRC-0580, SRC-1551  
**URL references:** None independently associated  
**Related findings:** FND-08954, FND-08955

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08957"></a>
## FND-08957: chesscom.train.v1.TrainOpeningMistakeChallenge.correct_move = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Move correct_move = 3;

### Evidence

- **SRC-0580** `research/proto/chesscom/train/v1/train_opening_mistake_challenge.proto` — [preserved redacted evidence](../evidence/text/f134c40907e863c64a660fc0ad171b8e9dc95f9a710cf7c7b8d6ff9098d89b99.proto)
  Character offset 250.

```text
 {
  optional int32 eco_family_id = 1;
  optional .chesscom.train.v1.TrainOpeningTheme theme = 2;
  optional .chesscom.chess.v1.Move correct_move = 3;
}

```

**Source references:** SRC-0580, SRC-1551  
**URL references:** None independently associated  
**Related findings:** FND-08954, FND-08955, FND-08956

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08958"></a>
## FND-08958: enum declaration: chesscom.train.v1.TrainOpeningTheme

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum TrainOpeningTheme {

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 102.

```text
 source: chesscom/train/v1/train_opening_theme.proto
// syntax: proto3

package chesscom.train.v1;

enum TrainOpeningTheme {
  TRAIN_OPENING_THEME_UNSPECIFIED = 0;
  TRAIN_OPENING_THEME_TOO_EARLY_QUEEN_DEVELOPMENT = 1;
  TRAIN_OPENING_THEME_MOVES_SAME_PIECE_IN_OPENING = 2;
  TRAIN_OPENING_THEME_CASTLES_INTO_ATTACK = 3;
  TRAIN_OPENING_THEME_LOSES_CASTLING_RIGHTS = 4;
  TRAIN_OPENING_THEME_NEVER_PLAY_F3 = 5;
  TRAIN_O
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08959"></a>
## FND-08959: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_UNSPECIFIED = 0;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 129.

```text
train_opening_theme.proto
// syntax: proto3

package chesscom.train.v1;

enum TrainOpeningTheme {
  TRAIN_OPENING_THEME_UNSPECIFIED = 0;
  TRAIN_OPENING_THEME_TOO_EARLY_QUEEN_DEVELOPMENT = 1;
  TRAIN_OPENING_THEME_MOVES_SAME_PIECE_IN_OPENING = 2;
  TRAIN_OPENING_THEME_CASTLES_INTO_ATTACK = 3;
  TRAIN_OPENING_THEME_LOSES_CASTLING_RIGHTS = 4;
  TRAIN_OPENING_THEME_NEVER_PLAY_F3 = 5;
  TRAIN_OPENING_THEME_MISSES_DEVELOP
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08960"></a>
## FND-08960: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_TOO_EARLY_QUEEN_DEVELOPMENT = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_TOO_EARLY_QUEEN_DEVELOPMENT = 1;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 168.

```text
oto3

package chesscom.train.v1;

enum TrainOpeningTheme {
  TRAIN_OPENING_THEME_UNSPECIFIED = 0;
  TRAIN_OPENING_THEME_TOO_EARLY_QUEEN_DEVELOPMENT = 1;
  TRAIN_OPENING_THEME_MOVES_SAME_PIECE_IN_OPENING = 2;
  TRAIN_OPENING_THEME_CASTLES_INTO_ATTACK = 3;
  TRAIN_OPENING_THEME_LOSES_CASTLING_RIGHTS = 4;
  TRAIN_OPENING_THEME_NEVER_PLAY_F3 = 5;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS = 6;
  TRAIN_OPENING_THEME_MISSES_DEV
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08961"></a>
## FND-08961: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_MOVES_SAME_PIECE_IN_OPENING = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_MOVES_SAME_PIECE_IN_OPENING = 2;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 223.

```text
e {
  TRAIN_OPENING_THEME_UNSPECIFIED = 0;
  TRAIN_OPENING_THEME_TOO_EARLY_QUEEN_DEVELOPMENT = 1;
  TRAIN_OPENING_THEME_MOVES_SAME_PIECE_IN_OPENING = 2;
  TRAIN_OPENING_THEME_CASTLES_INTO_ATTACK = 3;
  TRAIN_OPENING_THEME_LOSES_CASTLING_RIGHTS = 4;
  TRAIN_OPENING_THEME_NEVER_PLAY_F3 = 5;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS = 6;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_OPENING = 7;
  TRAIN_OPENING_THEME_MISSES_DEVELOP
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08962"></a>
## FND-08962: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_CASTLES_INTO_ATTACK = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_CASTLES_INTO_ATTACK = 3;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 278.

```text
ING_THEME_TOO_EARLY_QUEEN_DEVELOPMENT = 1;
  TRAIN_OPENING_THEME_MOVES_SAME_PIECE_IN_OPENING = 2;
  TRAIN_OPENING_THEME_CASTLES_INTO_ATTACK = 3;
  TRAIN_OPENING_THEME_LOSES_CASTLING_RIGHTS = 4;
  TRAIN_OPENING_THEME_NEVER_PLAY_F3 = 5;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS = 6;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_OPENING = 7;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_CENTER = 8;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_LAS
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08963"></a>
## FND-08963: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_LOSES_CASTLING_RIGHTS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_LOSES_CASTLING_RIGHTS = 4;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 325.

```text
AIN_OPENING_THEME_MOVES_SAME_PIECE_IN_OPENING = 2;
  TRAIN_OPENING_THEME_CASTLES_INTO_ATTACK = 3;
  TRAIN_OPENING_THEME_LOSES_CASTLING_RIGHTS = 4;
  TRAIN_OPENING_THEME_NEVER_PLAY_F3 = 5;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS = 6;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_OPENING = 7;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_CENTER = 8;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_LAST_PIECE = 9;
  TRAIN_OPENING_THEME_MISSES_DEVEL
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08964"></a>
## FND-08964: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_NEVER_PLAY_F3 = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_NEVER_PLAY_F3 = 5;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 374.

```text
;
  TRAIN_OPENING_THEME_CASTLES_INTO_ATTACK = 3;
  TRAIN_OPENING_THEME_LOSES_CASTLING_RIGHTS = 4;
  TRAIN_OPENING_THEME_NEVER_PLAY_F3 = 5;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS = 6;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_OPENING = 7;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_CENTER = 8;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_LAST_PIECE = 9;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_WITH_TEMPO = 10;
  TRAIN_OPENING_THEME_MISSES
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08965"></a>
## FND-08965: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_MISSES_DEVELOPS = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_MISSES_DEVELOPS = 6;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 415.

```text
CK = 3;
  TRAIN_OPENING_THEME_LOSES_CASTLING_RIGHTS = 4;
  TRAIN_OPENING_THEME_NEVER_PLAY_F3 = 5;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS = 6;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_OPENING = 7;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_CENTER = 8;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_LAST_PIECE = 9;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_WITH_TEMPO = 10;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_RECAPTURE = 11;
  TRAIN_OPENING
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08966"></a>
## FND-08966: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_MISSES_DEVELOPS_OPENING = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_MISSES_DEVELOPS_OPENING = 7;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 458.

```text
G_RIGHTS = 4;
  TRAIN_OPENING_THEME_NEVER_PLAY_F3 = 5;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS = 6;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_OPENING = 7;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_CENTER = 8;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_LAST_PIECE = 9;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_WITH_TEMPO = 10;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_RECAPTURE = 11;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_AND_PREVENTS_BREAK =
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08967"></a>
## FND-08967: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_MISSES_DEVELOPS_CENTER = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_MISSES_DEVELOPS_CENTER = 8;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 509.

```text
 5;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS = 6;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_OPENING = 7;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_CENTER = 8;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_LAST_PIECE = 9;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_WITH_TEMPO = 10;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_RECAPTURE = 11;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_AND_PREVENTS_BREAK = 12;
  TRAIN_OPENING_THEME_MISSES_PREPARES_BISHOP_D
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08968"></a>
## FND-08968: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_MISSES_DEVELOPS_LAST_PIECE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_MISSES_DEVELOPS_LAST_PIECE = 9;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 559.

```text
RAIN_OPENING_THEME_MISSES_DEVELOPS_OPENING = 7;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_CENTER = 8;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_LAST_PIECE = 9;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_WITH_TEMPO = 10;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_RECAPTURE = 11;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_AND_PREVENTS_BREAK = 12;
  TRAIN_OPENING_THEME_MISSES_PREPARES_BISHOP_DEVELOPMENT = 13;
  TRAIN_OPENING_THEME_MISSES_BISH
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08969"></a>
## FND-08969: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_MISSES_DEVELOPS_WITH_TEMPO = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_MISSES_DEVELOPS_WITH_TEMPO = 10;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 613.

```text
N_OPENING_THEME_MISSES_DEVELOPS_CENTER = 8;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_LAST_PIECE = 9;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_WITH_TEMPO = 10;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_RECAPTURE = 11;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_AND_PREVENTS_BREAK = 12;
  TRAIN_OPENING_THEME_MISSES_PREPARES_BISHOP_DEVELOPMENT = 13;
  TRAIN_OPENING_THEME_MISSES_BISHOP_GAINS_SCOPE = 14;
  TRAIN_OPENING_THEME_MISSES_OPEN
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08970"></a>
## FND-08970: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_MISSES_DEVELOPS_RECAPTURE = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_MISSES_DEVELOPS_RECAPTURE = 11;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 668.

```text
NING_THEME_MISSES_DEVELOPS_LAST_PIECE = 9;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_WITH_TEMPO = 10;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_RECAPTURE = 11;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_AND_PREVENTS_BREAK = 12;
  TRAIN_OPENING_THEME_MISSES_PREPARES_BISHOP_DEVELOPMENT = 13;
  TRAIN_OPENING_THEME_MISSES_BISHOP_GAINS_SCOPE = 14;
  TRAIN_OPENING_THEME_MISSES_OPENS_UP_SCOPE = 15;
  TRAIN_OPENING_THEME_MISSES_FIANCHETT
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08971"></a>
## FND-08971: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_MISSES_DEVELOPS_AND_PREVENTS_BREAK = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_MISSES_DEVELOPS_AND_PREVENTS_BREAK = 12;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 722.

```text
NING_THEME_MISSES_DEVELOPS_WITH_TEMPO = 10;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_RECAPTURE = 11;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_AND_PREVENTS_BREAK = 12;
  TRAIN_OPENING_THEME_MISSES_PREPARES_BISHOP_DEVELOPMENT = 13;
  TRAIN_OPENING_THEME_MISSES_BISHOP_GAINS_SCOPE = 14;
  TRAIN_OPENING_THEME_MISSES_OPENS_UP_SCOPE = 15;
  TRAIN_OPENING_THEME_MISSES_FIANCHETTO = 16;
  TRAIN_OPENING_THEME_MISSES_PREPARES_TO_CASTL
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08972"></a>
## FND-08972: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_MISSES_PREPARES_BISHOP_DEVELOPMENT = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_MISSES_PREPARES_BISHOP_DEVELOPMENT = 13;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 785.

```text
ME_MISSES_DEVELOPS_RECAPTURE = 11;
  TRAIN_OPENING_THEME_MISSES_DEVELOPS_AND_PREVENTS_BREAK = 12;
  TRAIN_OPENING_THEME_MISSES_PREPARES_BISHOP_DEVELOPMENT = 13;
  TRAIN_OPENING_THEME_MISSES_BISHOP_GAINS_SCOPE = 14;
  TRAIN_OPENING_THEME_MISSES_OPENS_UP_SCOPE = 15;
  TRAIN_OPENING_THEME_MISSES_FIANCHETTO = 16;
  TRAIN_OPENING_THEME_MISSES_PREPARES_TO_CASTLE_KINGSIDE = 17;
  TRAIN_OPENING_THEME_MISSES_PREPARES_TO_CASTL
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08973"></a>
## FND-08973: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_MISSES_BISHOP_GAINS_SCOPE = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_MISSES_BISHOP_GAINS_SCOPE = 14;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 848.

```text
_DEVELOPS_AND_PREVENTS_BREAK = 12;
  TRAIN_OPENING_THEME_MISSES_PREPARES_BISHOP_DEVELOPMENT = 13;
  TRAIN_OPENING_THEME_MISSES_BISHOP_GAINS_SCOPE = 14;
  TRAIN_OPENING_THEME_MISSES_OPENS_UP_SCOPE = 15;
  TRAIN_OPENING_THEME_MISSES_FIANCHETTO = 16;
  TRAIN_OPENING_THEME_MISSES_PREPARES_TO_CASTLE_KINGSIDE = 17;
  TRAIN_OPENING_THEME_MISSES_PREPARES_TO_CASTLE_QUEENSIDE = 18;
  TRAIN_OPENING_THEME_MISSES_CASTLES_KING_SID
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08974"></a>
## FND-08974: chesscom.train.v1.TrainOpeningTheme.TRAIN_OPENING_THEME_MISSES_OPENS_UP_SCOPE = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TRAIN_OPENING_THEME_MISSES_OPENS_UP_SCOPE = 15;

### Evidence

- **SRC-0581** `research/proto/chesscom/train/v1/train_opening_theme.proto` — [preserved redacted evidence](../evidence/text/018527ab02b8621c162518a2d098607a12b972b661add940835c9e721f01339b.proto)
  Character offset 902.

```text
ME_MISSES_PREPARES_BISHOP_DEVELOPMENT = 13;
  TRAIN_OPENING_THEME_MISSES_BISHOP_GAINS_SCOPE = 14;
  TRAIN_OPENING_THEME_MISSES_OPENS_UP_SCOPE = 15;
  TRAIN_OPENING_THEME_MISSES_FIANCHETTO = 16;
  TRAIN_OPENING_THEME_MISSES_PREPARES_TO_CASTLE_KINGSIDE = 17;
  TRAIN_OPENING_THEME_MISSES_PREPARES_TO_CASTLE_QUEENSIDE = 18;
  TRAIN_OPENING_THEME_MISSES_CASTLES_KING_SIDE = 19;
  TRAIN_OPENING_THEME_MISSES_CASTLES_QUEEN_SID
```

**Source references:** SRC-0581, SRC-1552  
**URL references:** None independently associated  
**Related findings:** FND-08958, FND-08959, FND-08960

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
