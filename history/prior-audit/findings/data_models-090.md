# data_models — findings 8901–9000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-09175"></a>
## FND-09175: chesscom.user_activity.v1.DisplayMode.DISPLAY_MODE_STANDALONE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DISPLAY_MODE_STANDALONE = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 193.

```text
user_activity.v1;

enum DisplayMode {
  DISPLAY_MODE_UNSPECIFIED = 0;
  DISPLAY_MODE_BROWSER = 1;
  DISPLAY_MODE_STANDALONE = 2;
  DISPLAY_MODE_FULLSCREEN = 3;
  DISPLAY_MODE_MINIMAL_UI = 4;
}

enum DeviceType {
  DEVICE_TYPE_UNSPECIFIED = 0;
  DESKTOP = 1;
  MOBILE = 2;
  TABLET = 3;
  TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTI
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09176"></a>
## FND-09176: chesscom.user_activity.v1.DisplayMode.DISPLAY_MODE_FULLSCREEN = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DISPLAY_MODE_FULLSCREEN = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 224.

```text
Mode {
  DISPLAY_MODE_UNSPECIFIED = 0;
  DISPLAY_MODE_BROWSER = 1;
  DISPLAY_MODE_STANDALONE = 2;
  DISPLAY_MODE_FULLSCREEN = 3;
  DISPLAY_MODE_MINIMAL_UI = 4;
}

enum DeviceType {
  DEVICE_TYPE_UNSPECIFIED = 0;
  DESKTOP = 1;
  MOBILE = 2;
  TABLET = 3;
  TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINA
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09177"></a>
## FND-09177: chesscom.user_activity.v1.DisplayMode.DISPLAY_MODE_MINIMAL_UI = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DISPLAY_MODE_MINIMAL_UI = 4;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 255.

```text
ED = 0;
  DISPLAY_MODE_BROWSER = 1;
  DISPLAY_MODE_STANDALONE = 2;
  DISPLAY_MODE_FULLSCREEN = 3;
  DISPLAY_MODE_MINIMAL_UI = 4;
}

enum DeviceType {
  DEVICE_TYPE_UNSPECIFIED = 0;
  DESKTOP = 1;
  MOBILE = 2;
  TABLET = 3;
  TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATIO
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09178"></a>
## FND-09178: enum declaration: chesscom.user_activity.v1.DeviceType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum DeviceType {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 287.

```text
 1;
  DISPLAY_MODE_STANDALONE = 2;
  DISPLAY_MODE_FULLSCREEN = 3;
  DISPLAY_MODE_MINIMAL_UI = 4;
}

enum DeviceType {
  DEVICE_TYPE_UNSPECIFIED = 0;
  DESKTOP = 1;
  MOBILE = 2;
  TABLET = 3;
  TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_U
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09179"></a>
## FND-09179: chesscom.user_activity.v1.DeviceType.DEVICE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DEVICE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 307.

```text
TANDALONE = 2;
  DISPLAY_MODE_FULLSCREEN = 3;
  DISPLAY_MODE_MINIMAL_UI = 4;
}

enum DeviceType {
  DEVICE_TYPE_UNSPECIFIED = 0;
  DESKTOP = 1;
  MOBILE = 2;
  TABLET = 3;
  TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09180"></a>
## FND-09180: chesscom.user_activity.v1.DeviceType.DESKTOP = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DESKTOP = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 338.

```text
ULLSCREEN = 3;
  DISPLAY_MODE_MINIMAL_UI = 4;
}

enum DeviceType {
  DEVICE_TYPE_UNSPECIFIED = 0;
  DESKTOP = 1;
  MOBILE = 2;
  TABLET = 3;
  TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICA
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09181"></a>
## FND-09181: chesscom.user_activity.v1.DeviceType.MOBILE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MOBILE = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 353.

```text
  DISPLAY_MODE_MINIMAL_UI = 4;
}

enum DeviceType {
  DEVICE_TYPE_UNSPECIFIED = 0;
  DESKTOP = 1;
  MOBILE = 2;
  TABLET = 3;
  TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIE
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09182"></a>
## FND-09182: chesscom.user_activity.v1.DeviceType.TABLET = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TABLET = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 367.

```text
_MINIMAL_UI = 4;
}

enum DeviceType {
  DEVICE_TYPE_UNSPECIFIED = 0;
  DESKTOP = 1;
  MOBILE = 2;
  TABLET = 3;
  TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLI
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09183"></a>
## FND-09183: chesscom.user_activity.v1.DeviceType.TV = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

TV = 4;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 381.

```text
4;
}

enum DeviceType {
  DEVICE_TYPE_UNSPECIFIED = 0;
  DESKTOP = 1;
  MOBILE = 2;
  TABLET = 3;
  TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCO
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09184"></a>
## FND-09184: chesscom.user_activity.v1.DeviceType.VR_HEADSET = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

VR_HEADSET = 5;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 391.

```text
 DeviceType {
  DEVICE_TYPE_UNSPECIFIED = 0;
  DESKTOP = 1;
  MOBILE = 2;
  TABLET = 3;
  TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}


```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09185"></a>
## FND-09185: chesscom.user_activity.v1.DeviceType.AR_HEADSET = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

AR_HEADSET = 6;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 409.

```text
VICE_TYPE_UNSPECIFIED = 0;
  DESKTOP = 1;
  MOBILE = 2;
  TABLET = 3;
  TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}

enum DestinationUp
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09186"></a>
## FND-09186: enum declaration: chesscom.user_activity.v1.Destination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Destination {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 428.

```text
ED = 0;
  DESKTOP = 1;
  MOBILE = 2;
  TABLET = 3;
  TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}

enum DestinationUpdateType {
  DESTIN
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09187"></a>
## FND-09187: chesscom.user_activity.v1.Destination.DESTINATION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DESTINATION_UNSPECIFIED = 0;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 449.

```text
;
  MOBILE = 2;
  TABLET = 3;
  TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}

enum DestinationUpdateType {
  DESTINATION_UPDATE_TYPE_UNS
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09188"></a>
## FND-09188: chesscom.user_activity.v1.Destination.DESTINATION_ITERABLE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DESTINATION_ITERABLE = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 480.

```text
 TV = 4;
  VR_HEADSET = 5;
  AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}

enum DestinationUpdateType {
  DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0;
  DESTINATION_UPD
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09189"></a>
## FND-09189: chesscom.user_activity.v1.Destination.DESTINATION_AMPLITUDE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DESTINATION_AMPLITUDE = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 508.

```text
 AR_HEADSET = 6;
}

enum Destination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}

enum DestinationUpdateType {
  DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0;
  DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTIN
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09190"></a>
## FND-09190: chesscom.user_activity.v1.Destination.DESTINATION_BIGQUERY = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DESTINATION_BIGQUERY = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 537.

```text
ination {
  DESTINATION_UNSPECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}

enum DestinationUpdateType {
  DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0;
  DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09191"></a>
## FND-09191: chesscom.user_activity.v1.Destination.DESTINATION_WORKFLOWS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DESTINATION_WORKFLOWS = 4;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 565.

```text
ECIFIED = 0;
  DESTINATION_ITERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}

enum DestinationUpdateType {
  DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0;
  DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09192"></a>
## FND-09192: chesscom.user_activity.v1.Destination.DESTINATION_USER_PROPERTIES = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DESTINATION_USER_PROPERTIES = 5;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 594.

```text
ERABLE = 1;
  DESTINATION_AMPLITUDE = 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}

enum DestinationUpdateType {
  DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0;
  DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.us
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09193"></a>
## FND-09193: enum declaration: chesscom.user_activity.v1.Application

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Application {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 630.

```text
= 2;
  DESTINATION_BIGQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}

enum DestinationUpdateType {
  DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0;
  DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 6;
  .che
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09194"></a>
## FND-09194: chesscom.user_activity.v1.Application.APPLICATION_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

APPLICATION_UNSPECIFIED = 0;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 651.

```text
GQUERY = 3;
  DESTINATION_WORKFLOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}

enum DestinationUpdateType {
  DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0;
  DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 6;
  .chesscom.user_activity.v
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09195"></a>
## FND-09195: chesscom.user_activity.v1.Application.APPLICATION_CHESSCOM = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

APPLICATION_CHESSCOM = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 682.

```text
LOWS = 4;
  DESTINATION_USER_PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}

enum DestinationUpdateType {
  DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0;
  DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 6;
  .chesscom.user_activity.v1.Screen screen = 7;
  }
  oneo
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09196"></a>
## FND-09196: enum declaration: chesscom.user_activity.v1.DestinationUpdateType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum DestinationUpdateType {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 711.

```text
PROPERTIES = 5;
}

enum Application {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}

enum DestinationUpdateType {
  DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0;
  DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 6;
  .chesscom.user_activity.v1.Screen screen = 7;
  }
  oneof _user_properties_cohorts {

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09197"></a>
## FND-09197: chesscom.user_activity.v1.DestinationUpdateType.DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 742.

```text
tion {
  APPLICATION_UNSPECIFIED = 0;
  APPLICATION_CHESSCOM = 1;
}

enum DestinationUpdateType {
  DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0;
  DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 6;
  .chesscom.user_activity.v1.Screen screen = 7;
  }
  oneof _user_properties_cohorts {
  .chesscom.user_activity.v1.Us
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09198"></a>
## FND-09198: chesscom.user_activity.v1.DestinationUpdateType.DESTINATION_UPDATE_TYPE_ADDED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DESTINATION_UPDATE_TYPE_ADDED = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 785.

```text
LICATION_CHESSCOM = 1;
}

enum DestinationUpdateType {
  DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0;
  DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 6;
  .chesscom.user_activity.v1.Screen screen = 7;
  }
  oneof _user_properties_cohorts {
  .chesscom.user_activity.v1.UserProperties user_properties_cohorts = 9;
 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09199"></a>
## FND-09199: chesscom.user_activity.v1.DestinationUpdateType.DESTINATION_UPDATE_TYPE_REMOVED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

DESTINATION_UPDATE_TYPE_REMOVED = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 822.

```text
ationUpdateType {
  DESTINATION_UPDATE_TYPE_UNSPECIFIED = 0;
  DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 6;
  .chesscom.user_activity.v1.Screen screen = 7;
  }
  oneof _user_properties_cohorts {
  .chesscom.user_activity.v1.UserProperties user_properties_cohorts = 9;
  }
  optional string name = 1;
  opti
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09200"></a>
## FND-09200: message declaration: chesscom.user_activity.v1.TrackEvent

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TrackEvent {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 862.

```text
YPE_UNSPECIFIED = 0;
  DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 6;
  .chesscom.user_activity.v1.Screen screen = 7;
  }
  oneof _user_properties_cohorts {
  .chesscom.user_activity.v1.UserProperties user_properties_cohorts = 9;
  }
  optional string name = 1;
  optional .chesscom.user_activity.v1.EventHea
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09201"></a>
## FND-09201: oneof declaration: chesscom.user_activity.v1.TrackEvent.source

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof source {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 885.

```text
DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 6;
  .chesscom.user_activity.v1.Screen screen = 7;
  }
  oneof _user_properties_cohorts {
  .chesscom.user_activity.v1.UserProperties user_properties_cohorts = 9;
  }
  optional string name = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  opt
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09202"></a>
## FND-09202: chesscom.user_activity.v1.TrackEvent.page = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.Page page = 6;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 902.

```text
E_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 6;
  .chesscom.user_activity.v1.Screen screen = 7;
  }
  oneof _user_properties_cohorts {
  .chesscom.user_activity.v1.UserProperties user_properties_cohorts = 9;
  }
  optional string name = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  optional .chesscom.u
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09203"></a>
## FND-09203: chesscom.user_activity.v1.TrackEvent.screen = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.Screen screen = 7;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 946.

```text
REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 6;
  .chesscom.user_activity.v1.Screen screen = 7;
  }
  oneof _user_properties_cohorts {
  .chesscom.user_activity.v1.UserProperties user_properties_cohorts = 9;
  }
  optional string name = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
  repea
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09204"></a>
## FND-09204: oneof declaration: chesscom.user_activity.v1.TrackEvent._user_properties_cohorts

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_properties_cohorts {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 998.

```text
{
  .chesscom.user_activity.v1.Page page = 6;
  .chesscom.user_activity.v1.Screen screen = 7;
  }
  oneof _user_properties_cohorts {
  .chesscom.user_activity.v1.UserProperties user_properties_cohorts = 9;
  }
  optional string name = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
  repeated .chesscom.user_activity.v1.TrackEvent.EventPrope
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09205"></a>
## FND-09205: chesscom.user_activity.v1.TrackEvent.user_properties_cohorts = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.UserProperties user_properties_cohorts = 9;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1033.

```text
 page = 6;
  .chesscom.user_activity.v1.Screen screen = 7;
  }
  oneof _user_properties_cohorts {
  .chesscom.user_activity.v1.UserProperties user_properties_cohorts = 9;
  }
  optional string name = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
  repeated .chesscom.user_activity.v1.TrackEvent.EventPropertiesEntry event_properties = 4;
  
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09206"></a>
## FND-09206: chesscom.user_activity.v1.TrackEvent.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1110.

```text
properties_cohorts {
  .chesscom.user_activity.v1.UserProperties user_properties_cohorts = 9;
  }
  optional string name = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
  repeated .chesscom.user_activity.v1.TrackEvent.EventPropertiesEntry event_properties = 4;
  repeated .chesscom.user_activity.v1.TrackEvent.UserPropertiesEntry user_prope
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09207"></a>
## FND-09207: chesscom.user_activity.v1.TrackEvent.headers = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.EventHeaders headers = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1138.

```text
scom.user_activity.v1.UserProperties user_properties_cohorts = 9;
  }
  optional string name = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
  repeated .chesscom.user_activity.v1.TrackEvent.EventPropertiesEntry event_properties = 4;
  repeated .chesscom.user_activity.v1.TrackEvent.UserPropertiesEntry user_properties = 5;
  repeated .chess
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09208"></a>
## FND-09208: chesscom.user_activity.v1.TrackEvent.context = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.Context context = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1202.

```text
;
  }
  optional string name = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
  repeated .chesscom.user_activity.v1.TrackEvent.EventPropertiesEntry event_properties = 4;
  repeated .chesscom.user_activity.v1.TrackEvent.UserPropertiesEntry user_properties = 5;
  repeated .chesscom.user_activity.v1.TrackEvent.IncrementPropertiesEntry increme
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09209"></a>
## FND-09209: chesscom.user_activity.v1.TrackEvent.event_properties = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_activity.v1.TrackEvent.EventPropertiesEntry event_properties = 4;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1261.

```text
_activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
  repeated .chesscom.user_activity.v1.TrackEvent.EventPropertiesEntry event_properties = 4;
  repeated .chesscom.user_activity.v1.TrackEvent.UserPropertiesEntry user_properties = 5;
  repeated .chesscom.user_activity.v1.TrackEvent.IncrementPropertiesEntry increment_properties = 8;
  repeated .chesscom.user_activity.v1.Tr
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09210"></a>
## FND-09210: chesscom.user_activity.v1.TrackEvent.user_properties = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_activity.v1.TrackEvent.UserPropertiesEntry user_properties = 5;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1353.

```text
 = 3;
  repeated .chesscom.user_activity.v1.TrackEvent.EventPropertiesEntry event_properties = 4;
  repeated .chesscom.user_activity.v1.TrackEvent.UserPropertiesEntry user_properties = 5;
  repeated .chesscom.user_activity.v1.TrackEvent.IncrementPropertiesEntry increment_properties = 8;
  repeated .chesscom.user_activity.v1.TrackEvent.EnrichmentUserPropertiesEntry enrichment_user_properties = 10;
  message EventPrope
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09211"></a>
## FND-09211: chesscom.user_activity.v1.TrackEvent.increment_properties = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_activity.v1.TrackEvent.IncrementPropertiesEntry increment_properties = 8;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1443.

```text
es = 4;
  repeated .chesscom.user_activity.v1.TrackEvent.UserPropertiesEntry user_properties = 5;
  repeated .chesscom.user_activity.v1.TrackEvent.IncrementPropertiesEntry increment_properties = 8;
  repeated .chesscom.user_activity.v1.TrackEvent.EnrichmentUserPropertiesEntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09212"></a>
## FND-09212: chesscom.user_activity.v1.TrackEvent.enrichment_user_properties = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_activity.v1.TrackEvent.EnrichmentUserPropertiesEntry enrichment_user_properties = 10;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1543.

```text
repeated .chesscom.user_activity.v1.TrackEvent.IncrementPropertiesEntry increment_properties = 8;
  repeated .chesscom.user_activity.v1.TrackEvent.EnrichmentUserPropertiesEntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09213"></a>
## FND-09213: message declaration: chesscom.user_activity.v1.TrackEvent.EventPropertiesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EventPropertiesEntry {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1655.

```text
esscom.user_activity.v1.TrackEvent.EnrichmentUserPropertiesEntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09214"></a>
## FND-09214: chesscom.user_activity.v1.TrackEvent.EventPropertiesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1688.

```text
t.EnrichmentUserPropertiesEntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09215"></a>
## FND-09215: chesscom.user_activity.v1.TrackEvent.EventPropertiesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Value value = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1715.

```text
ntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {
  optional string key = 1;

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09216"></a>
## FND-09216: message declaration: chesscom.user_activity.v1.TrackEvent.UserPropertiesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserPropertiesEntry {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1764.

```text
ventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09217"></a>
## FND-09217: chesscom.user_activity.v1.TrackEvent.UserPropertiesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1688.

```text
t.EnrichmentUserPropertiesEntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09218"></a>
## FND-09218: chesscom.user_activity.v1.TrackEvent.UserPropertiesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Value value = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1715.

```text
ntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {
  optional string key = 1;

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09219"></a>
## FND-09219: message declaration: chesscom.user_activity.v1.TrackEvent.IncrementPropertiesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message IncrementPropertiesEntry {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1872.

```text
UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message TypedEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 4;
  .chesscom.user_activi
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09220"></a>
## FND-09220: chesscom.user_activity.v1.TrackEvent.IncrementPropertiesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1688.

```text
t.EnrichmentUserPropertiesEntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09221"></a>
## FND-09221: chesscom.user_activity.v1.TrackEvent.IncrementPropertiesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 value = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1936.

```text
gle.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message TypedEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 4;
  .chesscom.user_activity.v1.Screen screen = 5;
  }
  optional .google.protobuf.Any eve
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09222"></a>
## FND-09222: message declaration: chesscom.user_activity.v1.TrackEvent.EnrichmentUserPropertiesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EnrichmentUserPropertiesEntry {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1968.

```text
}
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message TypedEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 4;
  .chesscom.user_activity.v1.Screen screen = 5;
  }
  optional .google.protobuf.Any event = 1;
  optional .chesscom.use
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09223"></a>
## FND-09223: chesscom.user_activity.v1.TrackEvent.EnrichmentUserPropertiesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1688.

```text
t.EnrichmentUserPropertiesEntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09224"></a>
## FND-09224: chesscom.user_activity.v1.TrackEvent.EnrichmentUserPropertiesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Value value = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1715.

```text
ntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {
  optional string key = 1;

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09225"></a>
## FND-09225: message declaration: chesscom.user_activity.v1.TypedEvent

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TypedEvent {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 2087.

```text
serPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message TypedEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 4;
  .chesscom.user_activity.v1.Screen screen = 5;
  }
  optional .google.protobuf.Any event = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
}

message IdentifyE
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09226"></a>
## FND-09226: oneof declaration: chesscom.user_activity.v1.TypedEvent.source

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof source {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 885.

```text
DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 6;
  .chesscom.user_activity.v1.Screen screen = 7;
  }
  oneof _user_properties_cohorts {
  .chesscom.user_activity.v1.UserProperties user_properties_cohorts = 9;
  }
  optional string name = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  opt
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09227"></a>
## FND-09227: chesscom.user_activity.v1.TypedEvent.page = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.Page page = 4;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 2127.

```text
ey = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message TypedEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 4;
  .chesscom.user_activity.v1.Screen screen = 5;
  }
  optional .google.protobuf.Any event = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
}

message IdentifyEvent {
  optional .chesscom.user_activit
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09228"></a>
## FND-09228: chesscom.user_activity.v1.TypedEvent.screen = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.Screen screen = 5;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 2171.

```text
lue = 2;
  }
}

message TypedEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 4;
  .chesscom.user_activity.v1.Screen screen = 5;
  }
  optional .google.protobuf.Any event = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
}

message IdentifyEvent {
  optional .chesscom.user_activity.v1.EventHeaders headers = 1;
  optional .c
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09229"></a>
## FND-09229: chesscom.user_activity.v1.TypedEvent.event = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Any event = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 2223.

```text
{
  .chesscom.user_activity.v1.Page page = 4;
  .chesscom.user_activity.v1.Screen screen = 5;
  }
  optional .google.protobuf.Any event = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
}

message IdentifyEvent {
  optional .chesscom.user_activity.v1.EventHeaders headers = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
  opti
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09230"></a>
## FND-09230: chesscom.user_activity.v1.TypedEvent.headers = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.EventHeaders headers = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1138.

```text
scom.user_activity.v1.UserProperties user_properties_cohorts = 9;
  }
  optional string name = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
  repeated .chesscom.user_activity.v1.TrackEvent.EventPropertiesEntry event_properties = 4;
  repeated .chesscom.user_activity.v1.TrackEvent.UserPropertiesEntry user_properties = 5;
  repeated .chess
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09231"></a>
## FND-09231: chesscom.user_activity.v1.TypedEvent.context = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.Context context = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1202.

```text
;
  }
  optional string name = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
  repeated .chesscom.user_activity.v1.TrackEvent.EventPropertiesEntry event_properties = 4;
  repeated .chesscom.user_activity.v1.TrackEvent.UserPropertiesEntry user_properties = 5;
  repeated .chesscom.user_activity.v1.TrackEvent.IncrementPropertiesEntry increme
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09232"></a>
## FND-09232: message declaration: chesscom.user_activity.v1.IdentifyEvent

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message IdentifyEvent {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 2390.

```text
activity.v1.EventHeaders headers = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
}

message IdentifyEvent {
  optional .chesscom.user_activity.v1.EventHeaders headers = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
  optional string user_id = 3;
  repeated .chesscom.user_activity.v1.IdentifyEvent.UserPropertiesEntry user_properties = 4;
  repeated .chesscom.user_activity.v1.IdentifyEve
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09233"></a>
## FND-09233: chesscom.user_activity.v1.IdentifyEvent.headers = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.EventHeaders headers = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 2416.

```text
eaders = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
}

message IdentifyEvent {
  optional .chesscom.user_activity.v1.EventHeaders headers = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
  optional string user_id = 3;
  repeated .chesscom.user_activity.v1.IdentifyEvent.UserPropertiesEntry user_properties = 4;
  repeated .chesscom.user_activity.v1.IdentifyEvent.IncrementPropertiesEntr
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09234"></a>
## FND-09234: chesscom.user_activity.v1.IdentifyEvent.context = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.Context context = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 2480.

```text
t = 3;
}

message IdentifyEvent {
  optional .chesscom.user_activity.v1.EventHeaders headers = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
  optional string user_id = 3;
  repeated .chesscom.user_activity.v1.IdentifyEvent.UserPropertiesEntry user_properties = 4;
  repeated .chesscom.user_activity.v1.IdentifyEvent.IncrementPropertiesEntry increment_properties = 8;
  message UserPropertiesEntry {
  op
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09235"></a>
## FND-09235: chesscom.user_activity.v1.IdentifyEvent.user_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_id = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 2539.

```text
_activity.v1.EventHeaders headers = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
  optional string user_id = 3;
  repeated .chesscom.user_activity.v1.IdentifyEvent.UserPropertiesEntry user_properties = 4;
  repeated .chesscom.user_activity.v1.IdentifyEvent.IncrementPropertiesEntry increment_properties = 8;
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value va
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09236"></a>
## FND-09236: chesscom.user_activity.v1.IdentifyEvent.user_properties = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_activity.v1.IdentifyEvent.UserPropertiesEntry user_properties = 4;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 2570.

```text
rs = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
  optional string user_id = 3;
  repeated .chesscom.user_activity.v1.IdentifyEvent.UserPropertiesEntry user_properties = 4;
  repeated .chesscom.user_activity.v1.IdentifyEvent.IncrementPropertiesEntry increment_properties = 8;
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message Incremen
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09237"></a>
## FND-09237: chesscom.user_activity.v1.IdentifyEvent.increment_properties = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_activity.v1.IdentifyEvent.IncrementPropertiesEntry increment_properties = 8;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 2663.

```text
= 3;
  repeated .chesscom.user_activity.v1.IdentifyEvent.UserPropertiesEntry user_properties = 4;
  repeated .chesscom.user_activity.v1.IdentifyEvent.IncrementPropertiesEntry increment_properties = 8;
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
}

message Navi
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09238"></a>
## FND-09238: message declaration: chesscom.user_activity.v1.IdentifyEvent.UserPropertiesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserPropertiesEntry {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1764.

```text
ventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09239"></a>
## FND-09239: chesscom.user_activity.v1.IdentifyEvent.UserPropertiesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1688.

```text
t.EnrichmentUserPropertiesEntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09240"></a>
## FND-09240: chesscom.user_activity.v1.IdentifyEvent.UserPropertiesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Value value = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1715.

```text
ntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {
  optional string key = 1;

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09241"></a>
## FND-09241: message declaration: chesscom.user_activity.v1.IdentifyEvent.IncrementPropertiesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message IncrementPropertiesEntry {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1872.

```text
UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message TypedEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 4;
  .chesscom.user_activi
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09242"></a>
## FND-09242: chesscom.user_activity.v1.IdentifyEvent.IncrementPropertiesEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1688.

```text
t.EnrichmentUserPropertiesEntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09243"></a>
## FND-09243: chesscom.user_activity.v1.IdentifyEvent.IncrementPropertiesEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int64 value = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1936.

```text
gle.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message TypedEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 4;
  .chesscom.user_activity.v1.Screen screen = 5;
  }
  optional .google.protobuf.Any eve
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09244"></a>
## FND-09244: message declaration: chesscom.user_activity.v1.NavigationEvent

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message NavigationEvent {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 2971.

```text

  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
}

message NavigationEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 3;
  .chesscom.user_activity.v1.Screen screen = 4;
  }
  oneof _deeplink {
  .chesscom.user_activity.v1.Deeplink deeplink = 5;
  }
  optional .chesscom.user_activity.v1.EventHeaders headers = 1;
  optional .chesscom.user_activity.v1.Con
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09245"></a>
## FND-09245: oneof declaration: chesscom.user_activity.v1.NavigationEvent.source

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof source {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 885.

```text
DESTINATION_UPDATE_TYPE_ADDED = 1;
  DESTINATION_UPDATE_TYPE_REMOVED = 2;
}

message TrackEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 6;
  .chesscom.user_activity.v1.Screen screen = 7;
  }
  oneof _user_properties_cohorts {
  .chesscom.user_activity.v1.UserProperties user_properties_cohorts = 9;
  }
  optional string name = 1;
  optional .chesscom.user_activity.v1.EventHeaders headers = 2;
  opt
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09246"></a>
## FND-09246: chesscom.user_activity.v1.NavigationEvent.page = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.Page page = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3016.

```text
nal string key = 1;
  optional int64 value = 2;
  }
}

message NavigationEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 3;
  .chesscom.user_activity.v1.Screen screen = 4;
  }
  oneof _deeplink {
  .chesscom.user_activity.v1.Deeplink deeplink = 5;
  }
  optional .chesscom.user_activity.v1.EventHeaders headers = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
}

message Deeplink {
  opt
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09247"></a>
## FND-09247: chesscom.user_activity.v1.NavigationEvent.screen = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.Screen screen = 4;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3060.

```text
 2;
  }
}

message NavigationEvent {
  oneof source {
  .chesscom.user_activity.v1.Page page = 3;
  .chesscom.user_activity.v1.Screen screen = 4;
  }
  oneof _deeplink {
  .chesscom.user_activity.v1.Deeplink deeplink = 5;
  }
  optional .chesscom.user_activity.v1.EventHeaders headers = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
}

message Deeplink {
  optional string link = 1;
  repeated .chesscom.
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09248"></a>
## FND-09248: oneof declaration: chesscom.user_activity.v1.NavigationEvent._deeplink

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _deeplink {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3112.

```text
{
  .chesscom.user_activity.v1.Page page = 3;
  .chesscom.user_activity.v1.Screen screen = 4;
  }
  oneof _deeplink {
  .chesscom.user_activity.v1.Deeplink deeplink = 5;
  }
  optional .chesscom.user_activity.v1.EventHeaders headers = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
}

message Deeplink {
  optional string link = 1;
  repeated .chesscom.user_activity.v1.Deeplink.DataEntry data = 2;
  mess
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09249"></a>
## FND-09249: chesscom.user_activity.v1.NavigationEvent.deeplink = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.Deeplink deeplink = 5;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3132.

```text
ctivity.v1.Page page = 3;
  .chesscom.user_activity.v1.Screen screen = 4;
  }
  oneof _deeplink {
  .chesscom.user_activity.v1.Deeplink deeplink = 5;
  }
  optional .chesscom.user_activity.v1.EventHeaders headers = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
}

message Deeplink {
  optional string link = 1;
  repeated .chesscom.user_activity.v1.Deeplink.DataEntry data = 2;
  message DataEntry {
  op
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09250"></a>
## FND-09250: chesscom.user_activity.v1.NavigationEvent.headers = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.EventHeaders headers = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 2416.

```text
eaders = 2;
  optional .chesscom.user_activity.v1.Context context = 3;
}

message IdentifyEvent {
  optional .chesscom.user_activity.v1.EventHeaders headers = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
  optional string user_id = 3;
  repeated .chesscom.user_activity.v1.IdentifyEvent.UserPropertiesEntry user_properties = 4;
  repeated .chesscom.user_activity.v1.IdentifyEvent.IncrementPropertiesEntr
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09251"></a>
## FND-09251: chesscom.user_activity.v1.NavigationEvent.context = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.Context context = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 2480.

```text
t = 3;
}

message IdentifyEvent {
  optional .chesscom.user_activity.v1.EventHeaders headers = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
  optional string user_id = 3;
  repeated .chesscom.user_activity.v1.IdentifyEvent.UserPropertiesEntry user_properties = 4;
  repeated .chesscom.user_activity.v1.IdentifyEvent.IncrementPropertiesEntry increment_properties = 8;
  message UserPropertiesEntry {
  op
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09252"></a>
## FND-09252: message declaration: chesscom.user_activity.v1.Deeplink

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Deeplink {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3312.

```text
activity.v1.EventHeaders headers = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
}

message Deeplink {
  optional string link = 1;
  repeated .chesscom.user_activity.v1.Deeplink.DataEntry data = 2;
  message DataEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message EventHeaders {
  oneof _local_time {
  string local_time = 3;
  }
  oneof _user_id {
  string use
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09253"></a>
## FND-09253: chesscom.user_activity.v1.Deeplink.link = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string link = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3333.

```text
ers headers = 1;
  optional .chesscom.user_activity.v1.Context context = 2;
}

message Deeplink {
  optional string link = 1;
  repeated .chesscom.user_activity.v1.Deeplink.DataEntry data = 2;
  message DataEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message EventHeaders {
  oneof _local_time {
  string local_time = 3;
  }
  oneof _user_id {
  string user_id = 5;
  }
  oneof
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09254"></a>
## FND-09254: chesscom.user_activity.v1.Deeplink.data = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_activity.v1.Deeplink.DataEntry data = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3361.

```text
.chesscom.user_activity.v1.Context context = 2;
}

message Deeplink {
  optional string link = 1;
  repeated .chesscom.user_activity.v1.Deeplink.DataEntry data = 2;
  message DataEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message EventHeaders {
  oneof _local_time {
  string local_time = 3;
  }
  oneof _user_id {
  string user_id = 5;
  }
  oneof _legacy_user_id {
  uint64 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09255"></a>
## FND-09255: message declaration: chesscom.user_activity.v1.Deeplink.DataEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DataEntry {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3428.

```text
 {
  optional string link = 1;
  repeated .chesscom.user_activity.v1.Deeplink.DataEntry data = 2;
  message DataEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message EventHeaders {
  oneof _local_time {
  string local_time = 3;
  }
  oneof _user_id {
  string user_id = 5;
  }
  oneof _legacy_user_id {
  uint64 legacy_user_id = 6;
  }
  oneof _sent_at {
  .google.protobuf.Times
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09256"></a>
## FND-09256: chesscom.user_activity.v1.Deeplink.DataEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1688.

```text
t.EnrichmentUserPropertiesEntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09257"></a>
## FND-09257: chesscom.user_activity.v1.Deeplink.DataEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Value value = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 1715.

```text
ntry enrichment_user_properties = 10;
  message EventPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message UserPropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
  message IncrementPropertiesEntry {
  optional string key = 1;
  optional int64 value = 2;
  }
  message EnrichmentUserPropertiesEntry {
  optional string key = 1;

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09258"></a>
## FND-09258: message declaration: chesscom.user_activity.v1.EventHeaders

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EventHeaders {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3527.

```text
 message DataEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message EventHeaders {
  oneof _local_time {
  string local_time = 3;
  }
  oneof _user_id {
  string user_id = 5;
  }
  oneof _legacy_user_id {
  uint64 legacy_user_id = 6;
  }
  oneof _sent_at {
  .google.protobuf.Timestamp sent_at = 8;
  }
  oneof _product_session_id {
  string product_session_id = 9;
  }
  oneof _a
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09259"></a>
## FND-09259: oneof declaration: chesscom.user_activity.v1.EventHeaders._local_time

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _local_time {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3552.

```text
tional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message EventHeaders {
  oneof _local_time {
  string local_time = 3;
  }
  oneof _user_id {
  string user_id = 5;
  }
  oneof _legacy_user_id {
  uint64 legacy_user_id = 6;
  }
  oneof _sent_at {
  .google.protobuf.Timestamp sent_at = 8;
  }
  oneof _product_session_id {
  string product_session_id = 9;
  }
  oneof _auth_user_id {
  string au
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09260"></a>
## FND-09260: chesscom.user_activity.v1.EventHeaders.local_time = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string local_time = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3574.

```text

  optional .google.protobuf.Value value = 2;
  }
}

message EventHeaders {
  oneof _local_time {
  string local_time = 3;
  }
  oneof _user_id {
  string user_id = 5;
  }
  oneof _legacy_user_id {
  uint64 legacy_user_id = 6;
  }
  oneof _sent_at {
  .google.protobuf.Timestamp sent_at = 8;
  }
  oneof _product_session_id {
  string product_session_id = 9;
  }
  oneof _auth_user_id {
  string auth_user_id = 10;
  }
 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09261"></a>
## FND-09261: oneof declaration: chesscom.user_activity.v1.EventHeaders._user_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_id {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3603.

```text
Value value = 2;
  }
}

message EventHeaders {
  oneof _local_time {
  string local_time = 3;
  }
  oneof _user_id {
  string user_id = 5;
  }
  oneof _legacy_user_id {
  uint64 legacy_user_id = 6;
  }
  oneof _sent_at {
  .google.protobuf.Timestamp sent_at = 8;
  }
  oneof _product_session_id {
  string product_session_id = 9;
  }
  oneof _auth_user_id {
  string auth_user_id = 10;
  }
  oneof _event_trusted {
  boo
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09262"></a>
## FND-09262: chesscom.user_activity.v1.EventHeaders.user_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_id = 5;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3622.

```text
}
}

message EventHeaders {
  oneof _local_time {
  string local_time = 3;
  }
  oneof _user_id {
  string user_id = 5;
  }
  oneof _legacy_user_id {
  uint64 legacy_user_id = 6;
  }
  oneof _sent_at {
  .google.protobuf.Timestamp sent_at = 8;
  }
  oneof _product_session_id {
  string product_session_id = 9;
  }
  oneof _auth_user_id {
  string auth_user_id = 10;
  }
  oneof _event_trusted {
  bool event_trusted = 1
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09263"></a>
## FND-09263: oneof declaration: chesscom.user_activity.v1.EventHeaders._legacy_user_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _legacy_user_id {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3648.

```text
{
  oneof _local_time {
  string local_time = 3;
  }
  oneof _user_id {
  string user_id = 5;
  }
  oneof _legacy_user_id {
  uint64 legacy_user_id = 6;
  }
  oneof _sent_at {
  .google.protobuf.Timestamp sent_at = 8;
  }
  oneof _product_session_id {
  string product_session_id = 9;
  }
  oneof _auth_user_id {
  string auth_user_id = 10;
  }
  oneof _event_trusted {
  bool event_trusted = 11;
  }
  optional string e
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09264"></a>
## FND-09264: chesscom.user_activity.v1.EventHeaders.legacy_user_id = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

uint64 legacy_user_id = 6;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3674.

```text
string local_time = 3;
  }
  oneof _user_id {
  string user_id = 5;
  }
  oneof _legacy_user_id {
  uint64 legacy_user_id = 6;
  }
  oneof _sent_at {
  .google.protobuf.Timestamp sent_at = 8;
  }
  oneof _product_session_id {
  string product_session_id = 9;
  }
  oneof _auth_user_id {
  string auth_user_id = 10;
  }
  oneof _event_trusted {
  bool event_trusted = 11;
  }
  optional string event_id = 1;
  optional .g
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09265"></a>
## FND-09265: oneof declaration: chesscom.user_activity.v1.EventHeaders._sent_at

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _sent_at {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3707.

```text
f _user_id {
  string user_id = 5;
  }
  oneof _legacy_user_id {
  uint64 legacy_user_id = 6;
  }
  oneof _sent_at {
  .google.protobuf.Timestamp sent_at = 8;
  }
  oneof _product_session_id {
  string product_session_id = 9;
  }
  oneof _auth_user_id {
  string auth_user_id = 10;
  }
  oneof _event_trusted {
  bool event_trusted = 11;
  }
  optional string event_id = 1;
  optional .google.protobuf.Timestamp timestam
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09266"></a>
## FND-09266: chesscom.user_activity.v1.EventHeaders.sent_at = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.google.protobuf.Timestamp sent_at = 8;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3726.

```text
ng user_id = 5;
  }
  oneof _legacy_user_id {
  uint64 legacy_user_id = 6;
  }
  oneof _sent_at {
  .google.protobuf.Timestamp sent_at = 8;
  }
  oneof _product_session_id {
  string product_session_id = 9;
  }
  oneof _auth_user_id {
  string auth_user_id = 10;
  }
  oneof _event_trusted {
  bool event_trusted = 11;
  }
  optional string event_id = 1;
  optional .google.protobuf.Timestamp timestamp = 2;
  optional u
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09267"></a>
## FND-09267: oneof declaration: chesscom.user_activity.v1.EventHeaders._product_session_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _product_session_id {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3772.

```text
  uint64 legacy_user_id = 6;
  }
  oneof _sent_at {
  .google.protobuf.Timestamp sent_at = 8;
  }
  oneof _product_session_id {
  string product_session_id = 9;
  }
  oneof _auth_user_id {
  string auth_user_id = 10;
  }
  oneof _event_trusted {
  bool event_trusted = 11;
  }
  optional string event_id = 1;
  optional .google.protobuf.Timestamp timestamp = 2;
  optional uint64 sequence_number = 7;
}

message Context 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09268"></a>
## FND-09268: chesscom.user_activity.v1.EventHeaders.product_session_id = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string product_session_id = 9;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3802.

```text
 }
  oneof _sent_at {
  .google.protobuf.Timestamp sent_at = 8;
  }
  oneof _product_session_id {
  string product_session_id = 9;
  }
  oneof _auth_user_id {
  string auth_user_id = 10;
  }
  oneof _event_trusted {
  bool event_trusted = 11;
  }
  optional string event_id = 1;
  optional .google.protobuf.Timestamp timestamp = 2;
  optional uint64 sequence_number = 7;
}

message Context {
  oneof _ip {
  string ip = 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09269"></a>
## FND-09269: oneof declaration: chesscom.user_activity.v1.EventHeaders._auth_user_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _auth_user_id {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3839.

```text
buf.Timestamp sent_at = 8;
  }
  oneof _product_session_id {
  string product_session_id = 9;
  }
  oneof _auth_user_id {
  string auth_user_id = 10;
  }
  oneof _event_trusted {
  bool event_trusted = 11;
  }
  optional string event_id = 1;
  optional .google.protobuf.Timestamp timestamp = 2;
  optional uint64 sequence_number = 7;
}

message Context {
  oneof _ip {
  string ip = 4;
  }
  oneof _user_agent {
  string
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09270"></a>
## FND-09270: chesscom.user_activity.v1.EventHeaders.auth_user_id = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string auth_user_id = 10;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3863.

```text
8;
  }
  oneof _product_session_id {
  string product_session_id = 9;
  }
  oneof _auth_user_id {
  string auth_user_id = 10;
  }
  oneof _event_trusted {
  bool event_trusted = 11;
  }
  optional string event_id = 1;
  optional .google.protobuf.Timestamp timestamp = 2;
  optional uint64 sequence_number = 7;
}

message Context {
  oneof _ip {
  string ip = 4;
  }
  oneof _user_agent {
  string user_agent = 5;
  }
  o
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09271"></a>
## FND-09271: oneof declaration: chesscom.user_activity.v1.EventHeaders._event_trusted

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _event_trusted {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3895.

```text
id {
  string product_session_id = 9;
  }
  oneof _auth_user_id {
  string auth_user_id = 10;
  }
  oneof _event_trusted {
  bool event_trusted = 11;
  }
  optional string event_id = 1;
  optional .google.protobuf.Timestamp timestamp = 2;
  optional uint64 sequence_number = 7;
}

message Context {
  oneof _ip {
  string ip = 4;
  }
  oneof _user_agent {
  string user_agent = 5;
  }
  oneof _campaign {
  .chesscom.use
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09272"></a>
## FND-09272: chesscom.user_activity.v1.EventHeaders.event_trusted = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool event_trusted = 11;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3920.

```text
sion_id = 9;
  }
  oneof _auth_user_id {
  string auth_user_id = 10;
  }
  oneof _event_trusted {
  bool event_trusted = 11;
  }
  optional string event_id = 1;
  optional .google.protobuf.Timestamp timestamp = 2;
  optional uint64 sequence_number = 7;
}

message Context {
  oneof _ip {
  string ip = 4;
  }
  oneof _user_agent {
  string user_agent = 5;
  }
  oneof _campaign {
  .chesscom.user_activity.v1.Campaign ca
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09273"></a>
## FND-09273: chesscom.user_activity.v1.EventHeaders.event_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string event_id = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3951.

```text
user_id {
  string auth_user_id = 10;
  }
  oneof _event_trusted {
  bool event_trusted = 11;
  }
  optional string event_id = 1;
  optional .google.protobuf.Timestamp timestamp = 2;
  optional uint64 sequence_number = 7;
}

message Context {
  oneof _ip {
  string ip = 4;
  }
  oneof _user_agent {
  string user_agent = 5;
  }
  oneof _campaign {
  .chesscom.user_activity.v1.Campaign campaign = 6;
  }
  oneof _locati
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09274"></a>
## FND-09274: chesscom.user_activity.v1.EventHeaders.timestamp = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp timestamp = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 3983.

```text
= 10;
  }
  oneof _event_trusted {
  bool event_trusted = 11;
  }
  optional string event_id = 1;
  optional .google.protobuf.Timestamp timestamp = 2;
  optional uint64 sequence_number = 7;
}

message Context {
  oneof _ip {
  string ip = 4;
  }
  oneof _user_agent {
  string user_agent = 5;
  }
  oneof _campaign {
  .chesscom.user_activity.v1.Campaign campaign = 6;
  }
  oneof _location {
  .chesscom.api.v1.Location
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
