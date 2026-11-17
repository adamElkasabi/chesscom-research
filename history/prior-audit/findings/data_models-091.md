# data_models — findings 9001–9100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-09275"></a>
## FND-09275: chesscom.user_activity.v1.EventHeaders.sequence_number = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint64 sequence_number = 7;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4036.

```text
ed = 11;
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
  .chesscom.api.v1.Location location = 7;
  }
  oneof _network {
  .chesscom.use
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09276"></a>
## FND-09276: message declaration: chesscom.user_activity.v1.Context

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Context {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4076.

```text
= 1;
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
  .chesscom.api.v1.Location location = 7;
  }
  oneof _network {
  .chesscom.user_activity.v1.Network network = 8;
  }
 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09277"></a>
## FND-09277: oneof declaration: chesscom.user_activity.v1.Context._ip

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ip {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4096.

```text
gle.protobuf.Timestamp timestamp = 2;
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
  .chesscom.api.v1.Location location = 7;
  }
  oneof _network {
  .chesscom.user_activity.v1.Network network = 8;
  }
  oneof _os {
  .ches
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09278"></a>
## FND-09278: chesscom.user_activity.v1.Context.ip = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string ip = 4;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4110.

```text
imestamp timestamp = 2;
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
  .chesscom.api.v1.Location location = 7;
  }
  oneof _network {
  .chesscom.user_activity.v1.Network network = 8;
  }
  oneof _os {
  .chesscom.user_acti
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09279"></a>
## FND-09279: oneof declaration: chesscom.user_activity.v1.Context._user_agent

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_agent {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4131.

```text
2;
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
  .chesscom.api.v1.Location location = 7;
  }
  oneof _network {
  .chesscom.user_activity.v1.Network network = 8;
  }
  oneof _os {
  .chesscom.user_activity.v1.OS os = 9;
  
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09280"></a>
## FND-09280: chesscom.user_activity.v1.Context.user_agent = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_agent = 5;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4153.

```text
equence_number = 7;
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
  .chesscom.api.v1.Location location = 7;
  }
  oneof _network {
  .chesscom.user_activity.v1.Network network = 8;
  }
  oneof _os {
  .chesscom.user_activity.v1.OS os = 9;
  }
  oneof _screen_reso
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09281"></a>
## FND-09281: oneof declaration: chesscom.user_activity.v1.Context._campaign

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _campaign {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4182.

```text
e Context {
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
  .chesscom.api.v1.Location location = 7;
  }
  oneof _network {
  .chesscom.user_activity.v1.Network network = 8;
  }
  oneof _os {
  .chesscom.user_activity.v1.OS os = 9;
  }
  oneof _screen_resolution {
  .chesscom.user_act
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09282"></a>
## FND-09282: chesscom.user_activity.v1.Context.campaign = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.Campaign campaign = 6;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4202.

```text
_ip {
  string ip = 4;
  }
  oneof _user_agent {
  string user_agent = 5;
  }
  oneof _campaign {
  .chesscom.user_activity.v1.Campaign campaign = 6;
  }
  oneof _location {
  .chesscom.api.v1.Location location = 7;
  }
  oneof _network {
  .chesscom.user_activity.v1.Network network = 8;
  }
  oneof _os {
  .chesscom.user_activity.v1.OS os = 9;
  }
  oneof _screen_resolution {
  .chesscom.user_activity.v1.ScreenResol
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09283"></a>
## FND-09283: oneof declaration: chesscom.user_activity.v1.Context._location

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _location {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4258.

```text
g user_agent = 5;
  }
  oneof _campaign {
  .chesscom.user_activity.v1.Campaign campaign = 6;
  }
  oneof _location {
  .chesscom.api.v1.Location location = 7;
  }
  oneof _network {
  .chesscom.user_activity.v1.Network network = 8;
  }
  oneof _os {
  .chesscom.user_activity.v1.OS os = 9;
  }
  oneof _screen_resolution {
  .chesscom.user_activity.v1.ScreenResolution screen_resolution = 10;
  }
  oneof _device {
  .c
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09284"></a>
## FND-09284: chesscom.user_activity.v1.Context.location = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.Location location = 7;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4278.

```text
}
  oneof _campaign {
  .chesscom.user_activity.v1.Campaign campaign = 6;
  }
  oneof _location {
  .chesscom.api.v1.Location location = 7;
  }
  oneof _network {
  .chesscom.user_activity.v1.Network network = 8;
  }
  oneof _os {
  .chesscom.user_activity.v1.OS os = 9;
  }
  oneof _screen_resolution {
  .chesscom.user_activity.v1.ScreenResolution screen_resolution = 10;
  }
  oneof _device {
  .chesscom.user_activit
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09285"></a>
## FND-09285: oneof declaration: chesscom.user_activity.v1.Context._network

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _network {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4324.

```text
y.v1.Campaign campaign = 6;
  }
  oneof _location {
  .chesscom.api.v1.Location location = 7;
  }
  oneof _network {
  .chesscom.user_activity.v1.Network network = 8;
  }
  oneof _os {
  .chesscom.user_activity.v1.OS os = 9;
  }
  oneof _screen_resolution {
  .chesscom.user_activity.v1.ScreenResolution screen_resolution = 10;
  }
  oneof _device {
  .chesscom.user_activity.v1.Device device = 11;
  }
  oneof _language
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09286"></a>
## FND-09286: chesscom.user_activity.v1.Context.network = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.Network network = 8;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4343.

```text
ign = 6;
  }
  oneof _location {
  .chesscom.api.v1.Location location = 7;
  }
  oneof _network {
  .chesscom.user_activity.v1.Network network = 8;
  }
  oneof _os {
  .chesscom.user_activity.v1.OS os = 9;
  }
  oneof _screen_resolution {
  .chesscom.user_activity.v1.ScreenResolution screen_resolution = 10;
  }
  oneof _device {
  .chesscom.user_activity.v1.Device device = 11;
  }
  oneof _language {
  string languag
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09287"></a>
## FND-09287: oneof declaration: chesscom.user_activity.v1.Context._os

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _os {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4397.

```text
cation location = 7;
  }
  oneof _network {
  .chesscom.user_activity.v1.Network network = 8;
  }
  oneof _os {
  .chesscom.user_activity.v1.OS os = 9;
  }
  oneof _screen_resolution {
  .chesscom.user_activity.v1.ScreenResolution screen_resolution = 10;
  }
  oneof _device {
  .chesscom.user_activity.v1.Device device = 11;
  }
  oneof _language {
  string language = 12;
  }
  oneof _bucketing_id {
  string bucketing
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09288"></a>
## FND-09288: chesscom.user_activity.v1.Context.os = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.OS os = 9;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4411.

```text
n = 7;
  }
  oneof _network {
  .chesscom.user_activity.v1.Network network = 8;
  }
  oneof _os {
  .chesscom.user_activity.v1.OS os = 9;
  }
  oneof _screen_resolution {
  .chesscom.user_activity.v1.ScreenResolution screen_resolution = 10;
  }
  oneof _device {
  .chesscom.user_activity.v1.Device device = 11;
  }
  oneof _language {
  string language = 12;
  }
  oneof _bucketing_id {
  string bucketing_id = 13;
  }

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09289"></a>
## FND-09289: oneof declaration: chesscom.user_activity.v1.Context._screen_resolution

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _screen_resolution {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4455.

```text
er_activity.v1.Network network = 8;
  }
  oneof _os {
  .chesscom.user_activity.v1.OS os = 9;
  }
  oneof _screen_resolution {
  .chesscom.user_activity.v1.ScreenResolution screen_resolution = 10;
  }
  oneof _device {
  .chesscom.user_activity.v1.Device device = 11;
  }
  oneof _language {
  string language = 12;
  }
  oneof _bucketing_id {
  string bucketing_id = 13;
  }
  oneof _interaction_event_id {
  string int
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09290"></a>
## FND-09290: chesscom.user_activity.v1.Context.screen_resolution = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.ScreenResolution screen_resolution = 10;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4484.

```text
k = 8;
  }
  oneof _os {
  .chesscom.user_activity.v1.OS os = 9;
  }
  oneof _screen_resolution {
  .chesscom.user_activity.v1.ScreenResolution screen_resolution = 10;
  }
  oneof _device {
  .chesscom.user_activity.v1.Device device = 11;
  }
  oneof _language {
  string language = 12;
  }
  oneof _bucketing_id {
  string bucketing_id = 13;
  }
  oneof _interaction_event_id {
  string interaction_event_id = 14;
  }
 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09291"></a>
## FND-09291: oneof declaration: chesscom.user_activity.v1.Context._device

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _device {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4558.

```text
of _screen_resolution {
  .chesscom.user_activity.v1.ScreenResolution screen_resolution = 10;
  }
  oneof _device {
  .chesscom.user_activity.v1.Device device = 11;
  }
  oneof _language {
  string language = 12;
  }
  oneof _bucketing_id {
  string bucketing_id = 13;
  }
  oneof _interaction_event_id {
  string interaction_event_id = 14;
  }
  optional .chesscom.user_activity.v1.Application application = 1;
  option
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09292"></a>
## FND-09292: chesscom.user_activity.v1.Context.device = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.Device device = 11;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4576.

```text
ion {
  .chesscom.user_activity.v1.ScreenResolution screen_resolution = 10;
  }
  oneof _device {
  .chesscom.user_activity.v1.Device device = 11;
  }
  oneof _language {
  string language = 12;
  }
  oneof _bucketing_id {
  string bucketing_id = 13;
  }
  oneof _interaction_event_id {
  string interaction_event_id = 14;
  }
  optional .chesscom.user_activity.v1.Application application = 1;
  optional .chesscom.user_
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09293"></a>
## FND-09293: oneof declaration: chesscom.user_activity.v1.Context._language

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _language {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4629.

```text
creen_resolution = 10;
  }
  oneof _device {
  .chesscom.user_activity.v1.Device device = 11;
  }
  oneof _language {
  string language = 12;
  }
  oneof _bucketing_id {
  string bucketing_id = 13;
  }
  oneof _interaction_event_id {
  string interaction_event_id = 14;
  }
  optional .chesscom.user_activity.v1.Application application = 1;
  optional .chesscom.user_activity.v1.Client client = 2;
  optional .chesscom.u
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09294"></a>
## FND-09294: chesscom.user_activity.v1.Context.language = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string language = 12;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4649.

```text
0;
  }
  oneof _device {
  .chesscom.user_activity.v1.Device device = 11;
  }
  oneof _language {
  string language = 12;
  }
  oneof _bucketing_id {
  string bucketing_id = 13;
  }
  oneof _interaction_event_id {
  string interaction_event_id = 14;
  }
  optional .chesscom.user_activity.v1.Application application = 1;
  optional .chesscom.user_activity.v1.Client client = 2;
  optional .chesscom.user_activity.v1.Libr
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09295"></a>
## FND-09295: oneof declaration: chesscom.user_activity.v1.Context._bucketing_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _bucketing_id {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4677.

```text
chesscom.user_activity.v1.Device device = 11;
  }
  oneof _language {
  string language = 12;
  }
  oneof _bucketing_id {
  string bucketing_id = 13;
  }
  oneof _interaction_event_id {
  string interaction_event_id = 14;
  }
  optional .chesscom.user_activity.v1.Application application = 1;
  optional .chesscom.user_activity.v1.Client client = 2;
  optional .chesscom.user_activity.v1.Library library = 3;
  repeated 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09296"></a>
## FND-09296: chesscom.user_activity.v1.Context.bucketing_id = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string bucketing_id = 13;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4701.

```text
1.Device device = 11;
  }
  oneof _language {
  string language = 12;
  }
  oneof _bucketing_id {
  string bucketing_id = 13;
  }
  oneof _interaction_event_id {
  string interaction_event_id = 14;
  }
  optional .chesscom.user_activity.v1.Application application = 1;
  optional .chesscom.user_activity.v1.Client client = 2;
  optional .chesscom.user_activity.v1.Library library = 3;
  repeated .google.protobuf.Any ext
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09297"></a>
## FND-09297: oneof declaration: chesscom.user_activity.v1.Context._interaction_event_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _interaction_event_id {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4733.

```text
f _language {
  string language = 12;
  }
  oneof _bucketing_id {
  string bucketing_id = 13;
  }
  oneof _interaction_event_id {
  string interaction_event_id = 14;
  }
  optional .chesscom.user_activity.v1.Application application = 1;
  optional .chesscom.user_activity.v1.Client client = 2;
  optional .chesscom.user_activity.v1.Library library = 3;
  repeated .google.protobuf.Any extensions = 15;
  repeated string 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09298"></a>
## FND-09298: chesscom.user_activity.v1.Context.interaction_event_id = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string interaction_event_id = 14;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4765.

```text
= 12;
  }
  oneof _bucketing_id {
  string bucketing_id = 13;
  }
  oneof _interaction_event_id {
  string interaction_event_id = 14;
  }
  optional .chesscom.user_activity.v1.Application application = 1;
  optional .chesscom.user_activity.v1.Client client = 2;
  optional .chesscom.user_activity.v1.Library library = 3;
  repeated .google.protobuf.Any extensions = 15;
  repeated string unified_screen = 16;
}

message 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09299"></a>
## FND-09299: chesscom.user_activity.v1.Context.application = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.Application application = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4805.

```text
ng bucketing_id = 13;
  }
  oneof _interaction_event_id {
  string interaction_event_id = 14;
  }
  optional .chesscom.user_activity.v1.Application application = 1;
  optional .chesscom.user_activity.v1.Client client = 2;
  optional .chesscom.user_activity.v1.Library library = 3;
  repeated .google.protobuf.Any extensions = 15;
  repeated string unified_screen = 16;
}

message Network {
  optional string type = 1;
  
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09300"></a>
## FND-09300: chesscom.user_activity.v1.Context.client = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.Client client = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4872.

```text
interaction_event_id = 14;
  }
  optional .chesscom.user_activity.v1.Application application = 1;
  optional .chesscom.user_activity.v1.Client client = 2;
  optional .chesscom.user_activity.v1.Library library = 3;
  repeated .google.protobuf.Any extensions = 15;
  repeated string unified_screen = 16;
}

message Network {
  optional string type = 1;
  optional string effective_type = 2;
  optional string provider_name
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09301"></a>
## FND-09301: chesscom.user_activity.v1.Context.library = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.Library library = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4929.

```text
activity.v1.Application application = 1;
  optional .chesscom.user_activity.v1.Client client = 2;
  optional .chesscom.user_activity.v1.Library library = 3;
  repeated .google.protobuf.Any extensions = 15;
  repeated string unified_screen = 16;
}

message Network {
  optional string type = 1;
  optional string effective_type = 2;
  optional string provider_name = 3;
}

message Screen {
  oneof _entity {
  .chesscom.n
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09302"></a>
## FND-09302: chesscom.user_activity.v1.Context.extensions = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .google.protobuf.Any extensions = 15;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 4988.

```text
om.user_activity.v1.Client client = 2;
  optional .chesscom.user_activity.v1.Library library = 3;
  repeated .google.protobuf.Any extensions = 15;
  repeated string unified_screen = 16;
}

message Network {
  optional string type = 1;
  optional string effective_type = 2;
  optional string provider_name = 3;
}

message Screen {
  oneof _entity {
  .chesscom.navigation.v1.ScreenEntity entity = 3;
  }
  optional string
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09303"></a>
## FND-09303: chesscom.user_activity.v1.Context.unified_screen = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string unified_screen = 16;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5037.

```text
 .chesscom.user_activity.v1.Library library = 3;
  repeated .google.protobuf.Any extensions = 15;
  repeated string unified_screen = 16;
}

message Network {
  optional string type = 1;
  optional string effective_type = 2;
  optional string provider_name = 3;
}

message Screen {
  oneof _entity {
  .chesscom.navigation.v1.ScreenEntity entity = 3;
  }
  optional string name = 1;
  repeated .chesscom.user_activity.v1.
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09304"></a>
## FND-09304: message declaration: chesscom.user_activity.v1.Network

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Network {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5077.

```text
ary = 3;
  repeated .google.protobuf.Any extensions = 15;
  repeated string unified_screen = 16;
}

message Network {
  optional string type = 1;
  optional string effective_type = 2;
  optional string provider_name = 3;
}

message Screen {
  oneof _entity {
  .chesscom.navigation.v1.ScreenEntity entity = 3;
  }
  optional string name = 1;
  repeated .chesscom.user_activity.v1.Screen.PropertiesEntry properties = 2;
 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09305"></a>
## FND-09305: chesscom.user_activity.v1.Network.type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string type = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5097.

```text
.google.protobuf.Any extensions = 15;
  repeated string unified_screen = 16;
}

message Network {
  optional string type = 1;
  optional string effective_type = 2;
  optional string provider_name = 3;
}

message Screen {
  oneof _entity {
  .chesscom.navigation.v1.ScreenEntity entity = 3;
  }
  optional string name = 1;
  repeated .chesscom.user_activity.v1.Screen.PropertiesEntry properties = 2;
  message PropertiesE
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09306"></a>
## FND-09306: chesscom.user_activity.v1.Network.effective_type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string effective_type = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5125.

```text
ons = 15;
  repeated string unified_screen = 16;
}

message Network {
  optional string type = 1;
  optional string effective_type = 2;
  optional string provider_name = 3;
}

message Screen {
  oneof _entity {
  .chesscom.navigation.v1.ScreenEntity entity = 3;
  }
  optional string name = 1;
  repeated .chesscom.user_activity.v1.Screen.PropertiesEntry properties = 2;
  message PropertiesEntry {
  optional string key
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09307"></a>
## FND-09307: chesscom.user_activity.v1.Network.provider_name = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string provider_name = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5163.

```text
reen = 16;
}

message Network {
  optional string type = 1;
  optional string effective_type = 2;
  optional string provider_name = 3;
}

message Screen {
  oneof _entity {
  .chesscom.navigation.v1.ScreenEntity entity = 3;
  }
  optional string name = 1;
  repeated .chesscom.user_activity.v1.Screen.PropertiesEntry properties = 2;
  message PropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Valu
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09308"></a>
## FND-09308: message declaration: chesscom.user_activity.v1.Screen

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Screen {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5201.

```text
onal string type = 1;
  optional string effective_type = 2;
  optional string provider_name = 3;
}

message Screen {
  oneof _entity {
  .chesscom.navigation.v1.ScreenEntity entity = 3;
  }
  optional string name = 1;
  repeated .chesscom.user_activity.v1.Screen.PropertiesEntry properties = 2;
  message PropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ScreenReso
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09309"></a>
## FND-09309: oneof declaration: chesscom.user_activity.v1.Screen._entity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _entity {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5220.

```text
1;
  optional string effective_type = 2;
  optional string provider_name = 3;
}

message Screen {
  oneof _entity {
  .chesscom.navigation.v1.ScreenEntity entity = 3;
  }
  optional string name = 1;
  repeated .chesscom.user_activity.v1.Screen.PropertiesEntry properties = 2;
  message PropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ScreenResolution {
  optional
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09310"></a>
## FND-09310: chesscom.user_activity.v1.Screen.entity = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.navigation.v1.ScreenEntity entity = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5238.

```text
ng effective_type = 2;
  optional string provider_name = 3;
}

message Screen {
  oneof _entity {
  .chesscom.navigation.v1.ScreenEntity entity = 3;
  }
  optional string name = 1;
  repeated .chesscom.user_activity.v1.Screen.PropertiesEntry properties = 2;
  message PropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ScreenResolution {
  optional uint32 width = 1;
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09311"></a>
## FND-09311: chesscom.user_activity.v1.Screen.name = 1

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

<a id="FND-09312"></a>
## FND-09312: chesscom.user_activity.v1.Screen.properties = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_activity.v1.Screen.PropertiesEntry properties = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5321.

```text
neof _entity {
  .chesscom.navigation.v1.ScreenEntity entity = 3;
  }
  optional string name = 1;
  repeated .chesscom.user_activity.v1.Screen.PropertiesEntry properties = 2;
  message PropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ScreenResolution {
  optional uint32 width = 1;
  optional uint32 height = 2;
  optional uint32 dpi = 3;
}

message Page {
  oneof
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09313"></a>
## FND-09313: message declaration: chesscom.user_activity.v1.Screen.PropertiesEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PropertiesEntry {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5398.

```text
nal string name = 1;
  repeated .chesscom.user_activity.v1.Screen.PropertiesEntry properties = 2;
  message PropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ScreenResolution {
  optional uint32 width = 1;
  optional uint32 height = 2;
  optional uint32 dpi = 3;
}

message Page {
  oneof _referrer {
  string referrer = 4;
  }
  oneof _search {
  string search = 5
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09314"></a>
## FND-09314: chesscom.user_activity.v1.Screen.PropertiesEntry.key = 1

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

<a id="FND-09315"></a>
## FND-09315: chesscom.user_activity.v1.Screen.PropertiesEntry.value = 2

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

<a id="FND-09316"></a>
## FND-09316: message declaration: chesscom.user_activity.v1.ScreenResolution

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ScreenResolution {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5503.

```text
ge PropertiesEntry {
  optional string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ScreenResolution {
  optional uint32 width = 1;
  optional uint32 height = 2;
  optional uint32 dpi = 3;
}

message Page {
  oneof _referrer {
  string referrer = 4;
  }
  oneof _search {
  string search = 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09317"></a>
## FND-09317: chesscom.user_activity.v1.ScreenResolution.width = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 width = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5532.

```text
al string key = 1;
  optional .google.protobuf.Value value = 2;
  }
}

message ScreenResolution {
  optional uint32 width = 1;
  optional uint32 height = 2;
  optional uint32 dpi = 3;
}

message Page {
  oneof _referrer {
  string referrer = 4;
  }
  oneof _search {
  string search = 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.us
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09318"></a>
## FND-09318: chesscom.user_activity.v1.ScreenResolution.height = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 height = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5561.

```text
 .google.protobuf.Value value = 2;
  }
}

message ScreenResolution {
  optional uint32 width = 1;
  optional uint32 height = 2;
  optional uint32 dpi = 3;
}

message Page {
  oneof _referrer {
  string referrer = 4;
  }
  oneof _search {
  string search = 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode di
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09319"></a>
## FND-09319: chesscom.user_activity.v1.ScreenResolution.dpi = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 dpi = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5591.

```text
= 2;
  }
}

message ScreenResolution {
  optional uint32 width = 1;
  optional uint32 height = 2;
  optional uint32 dpi = 3;
}

message Page {
  oneof _referrer {
  string referrer = 4;
  }
  oneof _search {
  string search = 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09320"></a>
## FND-09320: message declaration: chesscom.user_activity.v1.Page

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Page {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5619.

```text
solution {
  optional uint32 width = 1;
  optional uint32 height = 2;
  optional uint32 dpi = 3;
}

message Page {
  oneof _referrer {
  string referrer = 4;
  }
  oneof _search {
  string search = 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09321"></a>
## FND-09321: oneof declaration: chesscom.user_activity.v1.Page._referrer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _referrer {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5636.

```text
onal uint32 width = 1;
  optional uint32 height = 2;
  optional uint32 dpi = 3;
}

message Page {
  oneof _referrer {
  string referrer = 4;
  }
  oneof _search {
  string search = 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional string path = 2;
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09322"></a>
## FND-09322: chesscom.user_activity.v1.Page.referrer = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string referrer = 4;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5656.

```text
1;
  optional uint32 height = 2;
  optional uint32 dpi = 3;
}

message Page {
  oneof _referrer {
  string referrer = 4;
  }
  oneof _search {
  string search = 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional string path = 2;
  optional string t
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09323"></a>
## FND-09323: oneof declaration: chesscom.user_activity.v1.Page._search

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _search {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5683.

```text
 = 2;
  optional uint32 dpi = 3;
}

message Page {
  oneof _referrer {
  string referrer = 4;
  }
  oneof _search {
  string search = 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional string path = 2;
  optional string title = 3;
}

message OS {
 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09324"></a>
## FND-09324: chesscom.user_activity.v1.Page.search = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string search = 5;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5701.

```text
int32 dpi = 3;
}

message Page {
  oneof _referrer {
  string referrer = 4;
  }
  oneof _search {
  string search = 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional string path = 2;
  optional string title = 3;
}

message OS {
  optional string n
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09325"></a>
## FND-09325: oneof declaration: chesscom.user_activity.v1.Page._hash

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _hash {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5726.

```text
 Page {
  oneof _referrer {
  string referrer = 4;
  }
  oneof _search {
  string search = 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional string path = 2;
  optional string title = 3;
}

message OS {
  optional string name = 1;
  optional strin
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09326"></a>
## FND-09326: chesscom.user_activity.v1.Page.hash = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string hash = 6;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5742.

```text
_referrer {
  string referrer = 4;
  }
  oneof _search {
  string search = 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional string path = 2;
  optional string title = 3;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09327"></a>
## FND-09327: oneof declaration: chesscom.user_activity.v1.Page._route_name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _route_name {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5765.

```text
ferrer = 4;
  }
  oneof _search {
  string search = 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional string path = 2;
  optional string title = 3;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}

message Library {
  o
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09328"></a>
## FND-09328: chesscom.user_activity.v1.Page.route_name = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string route_name = 7;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5787.

```text
f _search {
  string search = 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional string path = 2;
  optional string title = 3;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}

message Library {
  optional .chesscom.user
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09329"></a>
## FND-09329: oneof declaration: chesscom.user_activity.v1.Page._display_mode

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _display_mode {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5816.

```text
 5;
  }
  oneof _hash {
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional string path = 2;
  optional string title = 3;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}

message Library {
  optional .chesscom.user_activity.v1.Library.Name nam
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09330"></a>
## FND-09330: chesscom.user_activity.v1.Page.display_mode = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_activity.v1.DisplayMode display_mode = 8;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5840.

```text
  string hash = 6;
  }
  oneof _route_name {
  string route_name = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional string path = 2;
  optional string title = 3;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}

message Library {
  optional .chesscom.user_activity.v1.Library.Name name = 1;
  optional string
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09331"></a>
## FND-09331: chesscom.user_activity.v1.Page.host = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string host = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5903.

```text
e = 7;
  }
  oneof _display_mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional string path = 2;
  optional string title = 3;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}

message Library {
  optional .chesscom.user_activity.v1.Library.Name name = 1;
  optional string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09332"></a>
## FND-09332: chesscom.user_activity.v1.Page.path = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string path = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5931.

```text
mode {
  .chesscom.user_activity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional string path = 2;
  optional string title = 3;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}

message Library {
  optional .chesscom.user_activity.v1.Library.Name name = 1;
  optional string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
   
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09333"></a>
## FND-09333: chesscom.user_activity.v1.Page.title = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string title = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5959.

```text
vity.v1.DisplayMode display_mode = 8;
  }
  optional string host = 1;
  optional string path = 2;
  optional string title = 3;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}

message Library {
  optional .chesscom.user_activity.v1.Library.Name name = 1;
  optional string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    C
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09334"></a>
## FND-09334: message declaration: chesscom.user_activity.v1.OS

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message OS {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 5989.

```text
de = 8;
  }
  optional string host = 1;
  optional string path = 2;
  optional string title = 3;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}

message Library {
  optional .chesscom.user_activity.v1.Library.Name name = 1;
  optional string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    C
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09335"></a>
## FND-09335: chesscom.user_activity.v1.OS.name = 1

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

<a id="FND-09336"></a>
## FND-09336: chesscom.user_activity.v1.OS.version = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string version = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6032.

```text
ptional string path = 2;
  optional string title = 3;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}

message Library {
  optional .chesscom.user_activity.v1.Library.Name name = 1;
  optional string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK =
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09337"></a>
## FND-09337: message declaration: chesscom.user_activity.v1.Library

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Library {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6064.

```text
nal string title = 3;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}

message Library {
  optional .chesscom.user_activity.v1.Library.Name name = 1;
  optional string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09338"></a>
## FND-09338: chesscom.user_activity.v1.Library.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.Library.Name name = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6084.

```text
;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}

message Library {
  optional .chesscom.user_activity.v1.Library.Name name = 1;
  optional string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09339"></a>
## FND-09339: chesscom.user_activity.v1.Library.version = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string version = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6032.

```text
ptional string path = 2;
  optional string title = 3;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}

message Library {
  optional .chesscom.user_activity.v1.Library.Name name = 1;
  optional string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK =
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09340"></a>
## FND-09340: enum declaration: chesscom.user_activity.v1.Library.Name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Name {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6176.

```text
ary {
  optional .chesscom.user_activity.v1.Library.Name name = 1;
  optional string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional stri
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09341"></a>
## FND-09341: chesscom.user_activity.v1.Library.Name.LIBRARY_NAME_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

LIBRARY_NAME_UNSPECIFIED = 0;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6192.

```text
 .chesscom.user_activity.v1.Library.Name name = 1;
  optional string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional string manufacturer 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09342"></a>
## FND-09342: chesscom.user_activity.v1.Library.Name.CHESSCOM_PHP_SDK = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESSCOM_PHP_SDK = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6226.

```text
y.Name name = 1;
  optional string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional string manufacturer = 2;
  optional string model = 3;

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09343"></a>
## FND-09343: chesscom.user_activity.v1.Library.Name.CHESSCOM_IOS_SDK = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESSCOM_IOS_SDK = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6252.

```text
l string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional string manufacturer = 2;
  optional string model = 3;
  optional string name = 4
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09344"></a>
## FND-09344: chesscom.user_activity.v1.Library.Name.CHESSCOM_ANDROID_SDK = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESSCOM_ANDROID_SDK = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6278.

```text
um Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional string manufacturer = 2;
  optional string model = 3;
  optional string name = 4;
  optional .chesscom.use
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09345"></a>
## FND-09345: chesscom.user_activity.v1.Library.Name.CHESSCOM_JS_SDK = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESSCOM_JS_SDK = 4;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6308.

```text
PECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional string manufacturer = 2;
  optional string model = 3;
  optional string name = 4;
  optional .chesscom.user_activity.v1.DeviceType type 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09346"></a>
## FND-09346: chesscom.user_activity.v1.Library.Name.CHESSCOM_JAVA_SDK = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESSCOM_JAVA_SDK = 5;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6333.

```text
M_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional string manufacturer = 2;
  optional string model = 3;
  optional string name = 4;
  optional .chesscom.user_activity.v1.DeviceType type = 5;
}

message Campaign 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09347"></a>
## FND-09347: chesscom.user_activity.v1.Library.Name.CHESSCOM_COURSES_PHP_SDK = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CHESSCOM_COURSES_PHP_SDK = 6;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6360.

```text
_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional string manufacturer = 2;
  optional string model = 3;
  optional string name = 4;
  optional .chesscom.user_activity.v1.DeviceType type = 5;
}

message Campaign {
  oneof _campaign_id {
  
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09348"></a>
## FND-09348: message declaration: chesscom.user_activity.v1.Device

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Device {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6397.

```text
K = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional string manufacturer = 2;
  optional string model = 3;
  optional string name = 4;
  optional .chesscom.user_activity.v1.DeviceType type = 5;
}

message Campaign {
  oneof _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _t
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09349"></a>
## FND-09349: oneof declaration: chesscom.user_activity.v1.Device._brand

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _brand {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6416.

```text
_JS_SDK = 4;
    CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional string manufacturer = 2;
  optional string model = 3;
  optional string name = 4;
  optional .chesscom.user_activity.v1.DeviceType type = 5;
}

message Campaign {
  oneof _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _template_id {
  int3
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09350"></a>
## FND-09350: chesscom.user_activity.v1.Device.brand = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string brand = 6;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6433.

```text
CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional string manufacturer = 2;
  optional string model = 3;
  optional string name = 4;
  optional .chesscom.user_activity.v1.DeviceType type = 5;
}

message Campaign {
  oneof _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _template_id {
  int32 template_id = 7
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09351"></a>
## FND-09351: chesscom.user_activity.v1.Device.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6457.

```text
   CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional string manufacturer = 2;
  optional string model = 3;
  optional string name = 4;
  optional .chesscom.user_activity.v1.DeviceType type = 5;
}

message Campaign {
  oneof _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _template_id {
  int32 template_id = 7;
  }
  optional string 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09352"></a>
## FND-09352: chesscom.user_activity.v1.Device.manufacturer = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string manufacturer = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6483.

```text
K = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional string manufacturer = 2;
  optional string model = 3;
  optional string name = 4;
  optional .chesscom.user_activity.v1.DeviceType type = 5;
}

message Campaign {
  oneof _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _template_id {
  int32 template_id = 7;
  }
  optional string source = 1;
  optional str
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09353"></a>
## FND-09353: chesscom.user_activity.v1.Device.model = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string model = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6519.

```text
of _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional string manufacturer = 2;
  optional string model = 3;
  optional string name = 4;
  optional .chesscom.user_activity.v1.DeviceType type = 5;
}

message Campaign {
  oneof _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _template_id {
  int32 template_id = 7;
  }
  optional string source = 1;
  optional string medium = 2;
  optional string na
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09354"></a>
## FND-09354: chesscom.user_activity.v1.Device.name = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 4;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6548.

```text
6;
  }
  optional string id = 1;
  optional string manufacturer = 2;
  optional string model = 3;
  optional string name = 4;
  optional .chesscom.user_activity.v1.DeviceType type = 5;
}

message Campaign {
  oneof _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _template_id {
  int32 template_id = 7;
  }
  optional string source = 1;
  optional string medium = 2;
  optional string name = 3;
  optional string ter
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09355"></a>
## FND-09355: chesscom.user_activity.v1.Device.type = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.DeviceType type = 5;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6576.

```text
= 1;
  optional string manufacturer = 2;
  optional string model = 3;
  optional string name = 4;
  optional .chesscom.user_activity.v1.DeviceType type = 5;
}

message Campaign {
  oneof _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _template_id {
  int32 template_id = 7;
  }
  optional string source = 1;
  optional string medium = 2;
  optional string name = 3;
  optional string term = 4;
  optional string con
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09356"></a>
## FND-09356: message declaration: chesscom.user_activity.v1.Campaign

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Campaign {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6636.

```text
odel = 3;
  optional string name = 4;
  optional .chesscom.user_activity.v1.DeviceType type = 5;
}

message Campaign {
  oneof _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _template_id {
  int32 template_id = 7;
  }
  optional string source = 1;
  optional string medium = 2;
  optional string name = 3;
  optional string term = 4;
  optional string content = 5;
}

message Client {
  optional .chesscom.user_acti
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09357"></a>
## FND-09357: oneof declaration: chesscom.user_activity.v1.Campaign._campaign_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _campaign_id {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6657.

```text
string name = 4;
  optional .chesscom.user_activity.v1.DeviceType type = 5;
}

message Campaign {
  oneof _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _template_id {
  int32 template_id = 7;
  }
  optional string source = 1;
  optional string medium = 2;
  optional string name = 3;
  optional string term = 4;
  optional string content = 5;
}

message Client {
  optional .chesscom.user_activity.v1.Client.Name n
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09358"></a>
## FND-09358: chesscom.user_activity.v1.Campaign.campaign_id = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 campaign_id = 6;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6680.

```text
onal .chesscom.user_activity.v1.DeviceType type = 5;
}

message Campaign {
  oneof _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _template_id {
  int32 template_id = 7;
  }
  optional string source = 1;
  optional string medium = 2;
  optional string name = 3;
  optional string term = 4;
  optional string content = 5;
}

message Client {
  optional .chesscom.user_activity.v1.Client.Name name = 1;
  optional str
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09359"></a>
## FND-09359: oneof declaration: chesscom.user_activity.v1.Campaign._template_id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _template_id {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6709.

```text
v1.DeviceType type = 5;
}

message Campaign {
  oneof _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _template_id {
  int32 template_id = 7;
  }
  optional string source = 1;
  optional string medium = 2;
  optional string name = 3;
  optional string term = 4;
  optional string content = 5;
}

message Client {
  optional .chesscom.user_activity.v1.Client.Name name = 1;
  optional string version = 2;
  optional s
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09360"></a>
## FND-09360: chesscom.user_activity.v1.Campaign.template_id = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 template_id = 7;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6732.

```text

}

message Campaign {
  oneof _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _template_id {
  int32 template_id = 7;
  }
  optional string source = 1;
  optional string medium = 2;
  optional string name = 3;
  optional string term = 4;
  optional string content = 5;
}

message Client {
  optional .chesscom.user_activity.v1.Client.Name name = 1;
  optional string version = 2;
  optional string build = 3;
  enum
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09361"></a>
## FND-09361: chesscom.user_activity.v1.Campaign.source = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string source = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6761.

```text
f _campaign_id {
  int32 campaign_id = 6;
  }
  oneof _template_id {
  int32 template_id = 7;
  }
  optional string source = 1;
  optional string medium = 2;
  optional string name = 3;
  optional string term = 4;
  optional string content = 5;
}

message Client {
  optional .chesscom.user_activity.v1.Client.Name name = 1;
  optional string version = 2;
  optional string build = 3;
  enum Name {
    CLIENT_NAME_UNSPE
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09362"></a>
## FND-09362: chesscom.user_activity.v1.Campaign.medium = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string medium = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6791.

```text
ign_id = 6;
  }
  oneof _template_id {
  int32 template_id = 7;
  }
  optional string source = 1;
  optional string medium = 2;
  optional string name = 3;
  optional string term = 4;
  optional string content = 5;
}

message Client {
  optional .chesscom.user_activity.v1.Client.Name name = 1;
  optional string version = 2;
  optional string build = 3;
  enum Name {
    CLIENT_NAME_UNSPECIFIED = 0;
    WEB = 1;
    I
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09363"></a>
## FND-09363: chesscom.user_activity.v1.Campaign.name = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string name = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6821.

```text
ate_id {
  int32 template_id = 7;
  }
  optional string source = 1;
  optional string medium = 2;
  optional string name = 3;
  optional string term = 4;
  optional string content = 5;
}

message Client {
  optional .chesscom.user_activity.v1.Client.Name name = 1;
  optional string version = 2;
  optional string build = 3;
  enum Name {
    CLIENT_NAME_UNSPECIFIED = 0;
    WEB = 1;
    IOS = 2;
    ANDROID = 3;
    U
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09364"></a>
## FND-09364: chesscom.user_activity.v1.Campaign.term = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string term = 4;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6849.

```text
 = 7;
  }
  optional string source = 1;
  optional string medium = 2;
  optional string name = 3;
  optional string term = 4;
  optional string content = 5;
}

message Client {
  optional .chesscom.user_activity.v1.Client.Name name = 1;
  optional string version = 2;
  optional string build = 3;
  enum Name {
    CLIENT_NAME_UNSPECIFIED = 0;
    WEB = 1;
    IOS = 2;
    ANDROID = 3;
    USER_PROPERTIES = 4;
    ON_P
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09365"></a>
## FND-09365: chesscom.user_activity.v1.Campaign.content = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string content = 5;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6877.

```text
source = 1;
  optional string medium = 2;
  optional string name = 3;
  optional string term = 4;
  optional string content = 5;
}

message Client {
  optional .chesscom.user_activity.v1.Client.Name name = 1;
  optional string version = 2;
  optional string build = 3;
  enum Name {
    CLIENT_NAME_UNSPECIFIED = 0;
    WEB = 1;
    IOS = 2;
    ANDROID = 3;
    USER_PROPERTIES = 4;
    ON_PLATFORM_MESSAGING = 5;
    W
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09366"></a>
## FND-09366: message declaration: chesscom.user_activity.v1.Client

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Client {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6909.

```text
dium = 2;
  optional string name = 3;
  optional string term = 4;
  optional string content = 5;
}

message Client {
  optional .chesscom.user_activity.v1.Client.Name name = 1;
  optional string version = 2;
  optional string build = 3;
  enum Name {
    CLIENT_NAME_UNSPECIFIED = 0;
    WEB = 1;
    IOS = 2;
    ANDROID = 3;
    USER_PROPERTIES = 4;
    ON_PLATFORM_MESSAGING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
 
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09367"></a>
## FND-09367: chesscom.user_activity.v1.Client.name = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_activity.v1.Client.Name name = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6928.

```text
l string name = 3;
  optional string term = 4;
  optional string content = 5;
}

message Client {
  optional .chesscom.user_activity.v1.Client.Name name = 1;
  optional string version = 2;
  optional string build = 3;
  enum Name {
    CLIENT_NAME_UNSPECIFIED = 0;
    WEB = 1;
    IOS = 2;
    ANDROID = 3;
    USER_PROPERTIES = 4;
    ON_PLATFORM_MESSAGING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
    RCN_SERVICE = 8;
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09368"></a>
## FND-09368: chesscom.user_activity.v1.Client.version = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string version = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6032.

```text
ptional string path = 2;
  optional string title = 3;
}

message OS {
  optional string name = 1;
  optional string version = 2;
}

message Library {
  optional .chesscom.user_activity.v1.Library.Name name = 1;
  optional string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK =
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09369"></a>
## FND-09369: chesscom.user_activity.v1.Client.build = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string build = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7019.

```text
ient {
  optional .chesscom.user_activity.v1.Client.Name name = 1;
  optional string version = 2;
  optional string build = 3;
  enum Name {
    CLIENT_NAME_UNSPECIFIED = 0;
    WEB = 1;
    IOS = 2;
    ANDROID = 3;
    USER_PROPERTIES = 4;
    ON_PLATFORM_MESSAGING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
    RCN_SERVICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09370"></a>
## FND-09370: enum declaration: chesscom.user_activity.v1.Client.Name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Name {

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 6176.

```text
ary {
  optional .chesscom.user_activity.v1.Library.Name name = 1;
  optional string version = 2;
  enum Name {
    LIBRARY_NAME_UNSPECIFIED = 0;
    CHESSCOM_PHP_SDK = 1;
    CHESSCOM_IOS_SDK = 2;
    CHESSCOM_ANDROID_SDK = 3;
    CHESSCOM_JS_SDK = 4;
    CHESSCOM_JAVA_SDK = 5;
    CHESSCOM_COURSES_PHP_SDK = 6;
  }
}

message Device {
  oneof _brand {
  string brand = 6;
  }
  optional string id = 1;
  optional stri
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09371"></a>
## FND-09371: chesscom.user_activity.v1.Client.Name.CLIENT_NAME_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

CLIENT_NAME_UNSPECIFIED = 0;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7064.

```text
Client.Name name = 1;
  optional string version = 2;
  optional string build = 3;
  enum Name {
    CLIENT_NAME_UNSPECIFIED = 0;
    WEB = 1;
    IOS = 2;
    ANDROID = 3;
    USER_PROPERTIES = 4;
    ON_PLATFORM_MESSAGING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
    RCN_SERVICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }

```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09372"></a>
## FND-09372: chesscom.user_activity.v1.Client.Name.WEB = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

WEB = 1;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7097.

```text
string version = 2;
  optional string build = 3;
  enum Name {
    CLIENT_NAME_UNSPECIFIED = 0;
    WEB = 1;
    IOS = 2;
    ANDROID = 3;
    USER_PROPERTIES = 4;
    ON_PLATFORM_MESSAGING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
    RCN_SERVICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  one
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09373"></a>
## FND-09373: chesscom.user_activity.v1.Client.Name.IOS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

IOS = 2;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7110.

```text
n = 2;
  optional string build = 3;
  enum Name {
    CLIENT_NAME_UNSPECIFIED = 0;
    WEB = 1;
    IOS = 2;
    ANDROID = 3;
    USER_PROPERTIES = 4;
    ON_PLATFORM_MESSAGING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
    RCN_SERVICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_na
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09374"></a>
## FND-09374: chesscom.user_activity.v1.Client.Name.ANDROID = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

ANDROID = 3;

### Evidence

- **SRC-0592** `research/proto/chesscom/user_activity/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/749f648a79a5ce9f2995985c48d8ea65ffebfe9ec61f62cc3b26565ebe9052e2.proto)
  Character offset 7123.

```text
onal string build = 3;
  enum Name {
    CLIENT_NAME_UNSPECIFIED = 0;
    WEB = 1;
    IOS = 2;
    ANDROID = 3;
    USER_PROPERTIES = 4;
    ON_PLATFORM_MESSAGING = 5;
    WORKFLOWS = 6;
    COURSES = 7;
    RCN_SERVICE = 8;
    PROGRESSION_SERVICE = 9;
    ITERABLE_CONNECTOR = 10;
    SENDGRID_WEBHOOKS = 11;
    EMAIL_SENDER = 12;
    PUSH_SENDER = 13;
  }
}

message UserProperties {
  oneof _client_name {
  .chess
```

**Source references:** SRC-0592, SRC-1563  
**URL references:** None independently associated  
**Related findings:** FND-09172, FND-09173, FND-09174

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
