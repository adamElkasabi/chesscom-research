# data_models — findings 8001–8100

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-08275"></a>
## FND-08275: message declaration: chesscom.shared_board.v1alpha.SharedBoardSessionSummary

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardSessionSummary {

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 1241.

```text
= 10;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource linked_resource = 11;
}

message SharedBoardSessionSummary {
  optional string id = 1;
  optional string slug = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 3;
  optional bool open_enrollment = 4;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 5;
  optional .chesscom.shared_board.v
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08276"></a>
## FND-08276: chesscom.shared_board.v1alpha.SharedBoardSessionSummary.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 586.

```text
Id {
  oneof id {
  string session_id = 1;
  string slug = 2;
  }
}

message SharedBoardSession {
  optional string id = 1;
  optional string current_board_id = 2;
  repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional string slug = 5;
  repeated .chesscom.shared_board.v1alpha.SharedBoardParticipant participants = 6;
  optional bool open_enro
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08277"></a>
## FND-08277: chesscom.shared_board.v1alpha.SharedBoardSessionSummary.slug = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string slug = 2;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 1305.

```text
onResource linked_resource = 11;
}

message SharedBoardSessionSummary {
  optional string id = 1;
  optional string slug = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 3;
  optional bool open_enrollment = 4;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 5;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 6;
  optional .chesscom.shared_boa
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08278"></a>
## FND-08278: chesscom.shared_board.v1alpha.SharedBoardSessionSummary.source = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 3;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 1333.

```text
 11;
}

message SharedBoardSessionSummary {
  optional string id = 1;
  optional string slug = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 3;
  optional bool open_enrollment = 4;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 5;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 6;
  optional .chesscom.shared_board.v1alpha.SharedBoardPartic
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08279"></a>
## FND-08279: chesscom.shared_board.v1alpha.SharedBoardSessionSummary.open_enrollment = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool open_enrollment = 4;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 1412.

```text
l string slug = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 3;
  optional bool open_enrollment = 4;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 5;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 6;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 7;
  optional .google.protobuf.Timestamp creat
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08280"></a>
## FND-08280: chesscom.shared_board.v1alpha.SharedBoardSessionSummary.status = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 5;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 1449.

```text
om.shared_board.v1alpha.SharedBoardSessionSource source = 3;
  optional bool open_enrollment = 4;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 5;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 6;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 7;
  optional .google.protobuf.Timestamp created_at = 8;
  optional .google.protobu
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08281"></a>
## FND-08281: chesscom.shared_board.v1alpha.SharedBoardSessionSummary.role = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 6;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 1528.

```text
en_enrollment = 4;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 5;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 6;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 7;
  optional .google.protobuf.Timestamp created_at = 8;
  optional .google.protobuf.Timestamp updated_at = 9;
}

```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08282"></a>
## FND-08282: chesscom.shared_board.v1alpha.SharedBoardSessionSummary.participant_status = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 7;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 1596.

```text
oardSessionStatus status = 5;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 6;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 7;
  optional .google.protobuf.Timestamp created_at = 8;
  optional .google.protobuf.Timestamp updated_at = 9;
}

```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08283"></a>
## FND-08283: chesscom.shared_board.v1alpha.SharedBoardSessionSummary.created_at = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp created_at = 8;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 1691.

```text
6;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 7;
  optional .google.protobuf.Timestamp created_at = 8;
  optional .google.protobuf.Timestamp updated_at = 9;
}

```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08284"></a>
## FND-08284: chesscom.shared_board.v1alpha.SharedBoardSessionSummary.updated_at = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp updated_at = 9;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 1745.

```text
rdParticipantStatus participant_status = 7;
  optional .google.protobuf.Timestamp created_at = 8;
  optional .google.protobuf.Timestamp updated_at = 9;
}

```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08285"></a>
## FND-08285: message declaration: chesscom.shared_board.v1alpha.SharedBoardSessionEndedNotification

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardSessionEndedNotification {

### Evidence

- **SRC-0549** `research/proto/chesscom/shared_board/v1alpha/shared_board_session_ended_notification.proto` — [preserved redacted evidence](../evidence/text/631443d3fc342db84f85c7d388f66836a1f693d7413ce70de2baacf0ef43a1f5.proto)
  Character offset 146.

```text
d_board_session_ended_notification.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

message SharedBoardSessionEndedNotification {
  optional string session_id = 1;
  optional string author_id = 2;
}

```

**Source references:** SRC-0549, SRC-1520  
**URL references:** None independently associated  
**Related findings:** FND-08286, FND-08287

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08286"></a>
## FND-08286: chesscom.shared_board.v1alpha.SharedBoardSessionEndedNotification.session_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string session_id = 1;

### Evidence

- **SRC-0549** `research/proto/chesscom/shared_board/v1alpha/shared_board_session_ended_notification.proto` — [preserved redacted evidence](../evidence/text/631443d3fc342db84f85c7d388f66836a1f693d7413ce70de2baacf0ef43a1f5.proto)
  Character offset 194.

```text
ax: proto3

package chesscom.shared_board.v1alpha;

message SharedBoardSessionEndedNotification {
  optional string session_id = 1;
  optional string author_id = 2;
}

```

**Source references:** SRC-0549, SRC-1520  
**URL references:** None independently associated  
**Related findings:** FND-08285, FND-08287

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08287"></a>
## FND-08287: chesscom.shared_board.v1alpha.SharedBoardSessionEndedNotification.author_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string author_id = 2;

### Evidence

- **SRC-0549** `research/proto/chesscom/shared_board/v1alpha/shared_board_session_ended_notification.proto` — [preserved redacted evidence](../evidence/text/631443d3fc342db84f85c7d388f66836a1f693d7413ce70de2baacf0ef43a1f5.proto)
  Character offset 228.

```text
d_board.v1alpha;

message SharedBoardSessionEndedNotification {
  optional string session_id = 1;
  optional string author_id = 2;
}

```

**Source references:** SRC-0549, SRC-1520  
**URL references:** None independently associated  
**Related findings:** FND-08285, FND-08286

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08288"></a>
## FND-08288: message declaration: chesscom.shared_board.v1alpha.SharedBoardSessionResource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardSessionResource {

### Evidence

- **SRC-0550** `research/proto/chesscom/shared_board/v1alpha/shared_board_session_resource.proto` — [preserved redacted evidence](../evidence/text/2ca053d901602f0fbcae5129b918ce8715d6a59a95a60e49cdc6529fac2301b2.proto)
  Character offset 136.

```text
lpha/shared_board_session_resource.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

message SharedBoardSessionResource {
  optional string resource_type = 1;
  optional string resource_id = 2;
}

```

**Source references:** SRC-0550, SRC-1521  
**URL references:** None independently associated  
**Related findings:** FND-08289, FND-08290

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08289"></a>
## FND-08289: chesscom.shared_board.v1alpha.SharedBoardSessionResource.resource_type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string resource_type = 1;

### Evidence

- **SRC-0550** `research/proto/chesscom/shared_board/v1alpha/shared_board_session_resource.proto` — [preserved redacted evidence](../evidence/text/2ca053d901602f0fbcae5129b918ce8715d6a59a95a60e49cdc6529fac2301b2.proto)
  Character offset 175.

```text
o
// syntax: proto3

package chesscom.shared_board.v1alpha;

message SharedBoardSessionResource {
  optional string resource_type = 1;
  optional string resource_id = 2;
}

```

**Source references:** SRC-0550, SRC-1521  
**URL references:** None independently associated  
**Related findings:** FND-08288, FND-08290

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08290"></a>
## FND-08290: chesscom.shared_board.v1alpha.SharedBoardSessionResource.resource_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string resource_id = 2;

### Evidence

- **SRC-0550** `research/proto/chesscom/shared_board/v1alpha/shared_board_session_resource.proto` — [preserved redacted evidence](../evidence/text/2ca053d901602f0fbcae5129b918ce8715d6a59a95a60e49cdc6529fac2301b2.proto)
  Character offset 212.

```text
.shared_board.v1alpha;

message SharedBoardSessionResource {
  optional string resource_type = 1;
  optional string resource_id = 2;
}

```

**Source references:** SRC-0550, SRC-1521  
**URL references:** None independently associated  
**Related findings:** FND-08288, FND-08289

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08291"></a>
## FND-08291: message declaration: chesscom.shared_board.v1alpha.SharedBoardSessionUpdatedNotification

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardSessionUpdatedNotification {

### Evidence

- **SRC-0551** `research/proto/chesscom/shared_board/v1alpha/shared_board_session_updated_notification.proto` — [preserved redacted evidence](../evidence/text/ae6b5b87147cd1d94499db253ed57fc9d2bbc2e3a4911abf233452bea1b4cdbe.proto)
  Character offset 148.

```text
board_session_updated_notification.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

message SharedBoardSessionUpdatedNotification {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
  optional string author_id = 2;
}

```

**Source references:** SRC-0551, SRC-1522  
**URL references:** None independently associated  
**Related findings:** FND-08292, FND-08293

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08292"></a>
## FND-08292: chesscom.shared_board.v1alpha.SharedBoardSessionUpdatedNotification.session = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;

### Evidence

- **SRC-0551** `research/proto/chesscom/shared_board/v1alpha/shared_board_session_updated_notification.proto` — [preserved redacted evidence](../evidence/text/ae6b5b87147cd1d94499db253ed57fc9d2bbc2e3a4911abf233452bea1b4cdbe.proto)
  Character offset 198.

```text
: proto3

package chesscom.shared_board.v1alpha;

message SharedBoardSessionUpdatedNotification {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
  optional string author_id = 2;
}

```

**Source references:** SRC-0551, SRC-1522  
**URL references:** None independently associated  
**Related findings:** FND-08291, FND-08293

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08293"></a>
## FND-08293: chesscom.shared_board.v1alpha.SharedBoardSessionUpdatedNotification.author_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string author_id = 2;

### Evidence

- **SRC-0551** `research/proto/chesscom/shared_board/v1alpha/shared_board_session_updated_notification.proto` — [preserved redacted evidence](../evidence/text/ae6b5b87147cd1d94499db253ed57fc9d2bbc2e3a4911abf233452bea1b4cdbe.proto)
  Character offset 272.

```text
onUpdatedNotification {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
  optional string author_id = 2;
}

```

**Source references:** SRC-0551, SRC-1522  
**URL references:** None independently associated  
**Related findings:** FND-08291, FND-08292

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08294"></a>
## FND-08294: enum declaration: chesscom.shared_board.v1alpha.SharedBoardUpdateType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SharedBoardUpdateType {

### Evidence

- **SRC-0552** `research/proto/chesscom/shared_board/v1alpha/shared_board_updated_notification.proto` — [preserved redacted evidence](../evidence/text/902ab041d69f3fe4227a5d2090279c9fe754590f401c916416447acd1c4bd450.proto)
  Character offset 140.

```text
/shared_board_updated_notification.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

enum SharedBoardUpdateType {
  SHARED_BOARD_UPDATE_TYPE_UNSPECIFIED = 0;
  SHARED_BOARD_UPDATE_TYPE_CREATED = 1;
  SHARED_BOARD_UPDATE_TYPE_UPDATED = 2;
  SHARED_BOARD_UPDATE_TYPE_DELETED = 3;
}

message SharedBoardUpdatedNotification {
  optional string session_id = 1;
  optional string author_id = 2;
  optional .ches
```

**Source references:** SRC-0552, SRC-1523  
**URL references:** None independently associated  
**Related findings:** FND-08295, FND-08296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08295"></a>
## FND-08295: chesscom.shared_board.v1alpha.SharedBoardUpdateType.SHARED_BOARD_UPDATE_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_UPDATE_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0552** `research/proto/chesscom/shared_board/v1alpha/shared_board_updated_notification.proto` — [preserved redacted evidence](../evidence/text/902ab041d69f3fe4227a5d2090279c9fe754590f401c916416447acd1c4bd450.proto)
  Character offset 171.

```text
ion.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

enum SharedBoardUpdateType {
  SHARED_BOARD_UPDATE_TYPE_UNSPECIFIED = 0;
  SHARED_BOARD_UPDATE_TYPE_CREATED = 1;
  SHARED_BOARD_UPDATE_TYPE_UPDATED = 2;
  SHARED_BOARD_UPDATE_TYPE_DELETED = 3;
}

message SharedBoardUpdatedNotification {
  optional string session_id = 1;
  optional string author_id = 2;
  optional .chesscom.shared_board.v1alpha.Share
```

**Source references:** SRC-0552, SRC-1523  
**URL references:** None independently associated  
**Related findings:** FND-08294, FND-08296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08296"></a>
## FND-08296: chesscom.shared_board.v1alpha.SharedBoardUpdateType.SHARED_BOARD_UPDATE_TYPE_CREATED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_UPDATE_TYPE_CREATED = 1;

### Evidence

- **SRC-0552** `research/proto/chesscom/shared_board/v1alpha/shared_board_updated_notification.proto` — [preserved redacted evidence](../evidence/text/902ab041d69f3fe4227a5d2090279c9fe754590f401c916416447acd1c4bd450.proto)
  Character offset 215.

```text
m.shared_board.v1alpha;

enum SharedBoardUpdateType {
  SHARED_BOARD_UPDATE_TYPE_UNSPECIFIED = 0;
  SHARED_BOARD_UPDATE_TYPE_CREATED = 1;
  SHARED_BOARD_UPDATE_TYPE_UPDATED = 2;
  SHARED_BOARD_UPDATE_TYPE_DELETED = 3;
}

message SharedBoardUpdatedNotification {
  optional string session_id = 1;
  optional string author_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 3;
  optional .chesscom.share
```

**Source references:** SRC-0552, SRC-1523  
**URL references:** None independently associated  
**Related findings:** FND-08294, FND-08295

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08297"></a>
## FND-08297: chesscom.shared_board.v1alpha.SharedBoardUpdateType.SHARED_BOARD_UPDATE_TYPE_UPDATED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_UPDATE_TYPE_UPDATED = 2;

### Evidence

- **SRC-0552** `research/proto/chesscom/shared_board/v1alpha/shared_board_updated_notification.proto` — [preserved redacted evidence](../evidence/text/902ab041d69f3fe4227a5d2090279c9fe754590f401c916416447acd1c4bd450.proto)
  Character offset 255.

```text
dUpdateType {
  SHARED_BOARD_UPDATE_TYPE_UNSPECIFIED = 0;
  SHARED_BOARD_UPDATE_TYPE_CREATED = 1;
  SHARED_BOARD_UPDATE_TYPE_UPDATED = 2;
  SHARED_BOARD_UPDATE_TYPE_DELETED = 3;
}

message SharedBoardUpdatedNotification {
  optional string session_id = 1;
  optional string author_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardUpdateType up
```

**Source references:** SRC-0552, SRC-1523  
**URL references:** None independently associated  
**Related findings:** FND-08294, FND-08295, FND-08296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08298"></a>
## FND-08298: chesscom.shared_board.v1alpha.SharedBoardUpdateType.SHARED_BOARD_UPDATE_TYPE_DELETED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_UPDATE_TYPE_DELETED = 3;

### Evidence

- **SRC-0552** `research/proto/chesscom/shared_board/v1alpha/shared_board_updated_notification.proto` — [preserved redacted evidence](../evidence/text/902ab041d69f3fe4227a5d2090279c9fe754590f401c916416447acd1c4bd450.proto)
  Character offset 295.

```text
_UNSPECIFIED = 0;
  SHARED_BOARD_UPDATE_TYPE_CREATED = 1;
  SHARED_BOARD_UPDATE_TYPE_UPDATED = 2;
  SHARED_BOARD_UPDATE_TYPE_DELETED = 3;
}

message SharedBoardUpdatedNotification {
  optional string session_id = 1;
  optional string author_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardUpdateType update_type = 4;
}

```

**Source references:** SRC-0552, SRC-1523  
**URL references:** None independently associated  
**Related findings:** FND-08294, FND-08295, FND-08296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08299"></a>
## FND-08299: message declaration: chesscom.shared_board.v1alpha.SharedBoardUpdatedNotification

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardUpdatedNotification {

### Evidence

- **SRC-0552** `research/proto/chesscom/shared_board/v1alpha/shared_board_updated_notification.proto` — [preserved redacted evidence](../evidence/text/902ab041d69f3fe4227a5d2090279c9fe754590f401c916416447acd1c4bd450.proto)
  Character offset 336.

```text
YPE_CREATED = 1;
  SHARED_BOARD_UPDATE_TYPE_UPDATED = 2;
  SHARED_BOARD_UPDATE_TYPE_DELETED = 3;
}

message SharedBoardUpdatedNotification {
  optional string session_id = 1;
  optional string author_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardUpdateType update_type = 4;
}

```

**Source references:** SRC-0552, SRC-1523  
**URL references:** None independently associated  
**Related findings:** FND-08294, FND-08295, FND-08296

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08300"></a>
## FND-08300: chesscom.shared_board.v1alpha.SharedBoardUpdatedNotification.session_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string session_id = 1;

### Evidence

- **SRC-0552** `research/proto/chesscom/shared_board/v1alpha/shared_board_updated_notification.proto` — [preserved redacted evidence](../evidence/text/902ab041d69f3fe4227a5d2090279c9fe754590f401c916416447acd1c4bd450.proto)
  Character offset 379.

```text
_UPDATED = 2;
  SHARED_BOARD_UPDATE_TYPE_DELETED = 3;
}

message SharedBoardUpdatedNotification {
  optional string session_id = 1;
  optional string author_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardUpdateType update_type = 4;
}

```

**Source references:** SRC-0552, SRC-1523  
**URL references:** None independently associated  
**Related findings:** FND-08294, FND-08295, FND-08296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08301"></a>
## FND-08301: chesscom.shared_board.v1alpha.SharedBoardUpdatedNotification.author_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string author_id = 2;

### Evidence

- **SRC-0552** `research/proto/chesscom/shared_board/v1alpha/shared_board_updated_notification.proto` — [preserved redacted evidence](../evidence/text/902ab041d69f3fe4227a5d2090279c9fe754590f401c916416447acd1c4bd450.proto)
  Character offset 413.

```text
E_TYPE_DELETED = 3;
}

message SharedBoardUpdatedNotification {
  optional string session_id = 1;
  optional string author_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardUpdateType update_type = 4;
}

```

**Source references:** SRC-0552, SRC-1523  
**URL references:** None independently associated  
**Related findings:** FND-08294, FND-08295, FND-08296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08302"></a>
## FND-08302: chesscom.shared_board.v1alpha.SharedBoardUpdatedNotification.board = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoard board = 3;

### Evidence

- **SRC-0552** `research/proto/chesscom/shared_board/v1alpha/shared_board_updated_notification.proto` — [preserved redacted evidence](../evidence/text/902ab041d69f3fe4227a5d2090279c9fe754590f401c916416447acd1c4bd450.proto)
  Character offset 446.

```text
aredBoardUpdatedNotification {
  optional string session_id = 1;
  optional string author_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardUpdateType update_type = 4;
}

```

**Source references:** SRC-0552, SRC-1523  
**URL references:** None independently associated  
**Related findings:** FND-08294, FND-08295, FND-08296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08303"></a>
## FND-08303: chesscom.shared_board.v1alpha.SharedBoardUpdatedNotification.update_type = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardUpdateType update_type = 4;

### Evidence

- **SRC-0552** `research/proto/chesscom/shared_board/v1alpha/shared_board_updated_notification.proto` — [preserved redacted evidence](../evidence/text/902ab041d69f3fe4227a5d2090279c9fe754590f401c916416447acd1c4bd450.proto)
  Character offset 511.

```text
  optional string author_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardUpdateType update_type = 4;
}

```

**Source references:** SRC-0552, SRC-1523  
**URL references:** None independently associated  
**Related findings:** FND-08294, FND-08295, FND-08296

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08304"></a>
## FND-08304: message declaration: chesscom.skills.v1.EligibilityError

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EligibilityError {

### Evidence

- **SRC-0553** `research/proto/chesscom/skills/v1/eligibility_error.proto` — [preserved redacted evidence](../evidence/text/a4b9cafb5078653ed6e185fd9e91ea11864f42721715bc7799643f01eb3e3ac8.proto)
  Character offset 102.

```text
 source: chesscom/skills/v1/eligibility_error.proto
// syntax: proto3

package chesscom.skills.v1;

message EligibilityError {
  optional .chesscom.skills.v1.EligibilityError.Reason reason = 1;
  enum Reason {
    REASON_UNSPECIFIED = 0;
    REASON_GAME_SKILL_POINTS_EXPIRED = 1;
    REASON_NOT_A_GAME_PARTICIPANT = 2;
    REASON_PLAYER_DISABLED = 3;
    REASON_GAME_NOT_FOUND = 4;
  }
}

```

**Source references:** SRC-0553, SRC-1524  
**URL references:** None independently associated  
**Related findings:** FND-08305, FND-08306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08305"></a>
## FND-08305: chesscom.skills.v1.EligibilityError.reason = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.skills.v1.EligibilityError.Reason reason = 1;

### Evidence

- **SRC-0553** `research/proto/chesscom/skills/v1/eligibility_error.proto` — [preserved redacted evidence](../evidence/text/a4b9cafb5078653ed6e185fd9e91ea11864f42721715bc7799643f01eb3e3ac8.proto)
  Character offset 131.

```text
ligibility_error.proto
// syntax: proto3

package chesscom.skills.v1;

message EligibilityError {
  optional .chesscom.skills.v1.EligibilityError.Reason reason = 1;
  enum Reason {
    REASON_UNSPECIFIED = 0;
    REASON_GAME_SKILL_POINTS_EXPIRED = 1;
    REASON_NOT_A_GAME_PARTICIPANT = 2;
    REASON_PLAYER_DISABLED = 3;
    REASON_GAME_NOT_FOUND = 4;
  }
}

```

**Source references:** SRC-0553, SRC-1524  
**URL references:** None independently associated  
**Related findings:** FND-08304, FND-08306

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08306"></a>
## FND-08306: enum declaration: chesscom.skills.v1.EligibilityError.Reason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Reason {

### Evidence

- **SRC-0553** `research/proto/chesscom/skills/v1/eligibility_error.proto` — [preserved redacted evidence](../evidence/text/a4b9cafb5078653ed6e185fd9e91ea11864f42721715bc7799643f01eb3e3ac8.proto)
  Character offset 198.

```text
1;

message EligibilityError {
  optional .chesscom.skills.v1.EligibilityError.Reason reason = 1;
  enum Reason {
    REASON_UNSPECIFIED = 0;
    REASON_GAME_SKILL_POINTS_EXPIRED = 1;
    REASON_NOT_A_GAME_PARTICIPANT = 2;
    REASON_PLAYER_DISABLED = 3;
    REASON_GAME_NOT_FOUND = 4;
  }
}

```

**Source references:** SRC-0553, SRC-1524  
**URL references:** None independently associated  
**Related findings:** FND-08304, FND-08305

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08307"></a>
## FND-08307: chesscom.skills.v1.EligibilityError.Reason.REASON_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

REASON_UNSPECIFIED = 0;

### Evidence

- **SRC-0553** `research/proto/chesscom/skills/v1/eligibility_error.proto` — [preserved redacted evidence](../evidence/text/a4b9cafb5078653ed6e185fd9e91ea11864f42721715bc7799643f01eb3e3ac8.proto)
  Character offset 216.

```text
ilityError {
  optional .chesscom.skills.v1.EligibilityError.Reason reason = 1;
  enum Reason {
    REASON_UNSPECIFIED = 0;
    REASON_GAME_SKILL_POINTS_EXPIRED = 1;
    REASON_NOT_A_GAME_PARTICIPANT = 2;
    REASON_PLAYER_DISABLED = 3;
    REASON_GAME_NOT_FOUND = 4;
  }
}

```

**Source references:** SRC-0553, SRC-1524  
**URL references:** None independently associated  
**Related findings:** FND-08304, FND-08305, FND-08306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08308"></a>
## FND-08308: chesscom.skills.v1.EligibilityError.Reason.REASON_GAME_SKILL_POINTS_EXPIRED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

REASON_GAME_SKILL_POINTS_EXPIRED = 1;

### Evidence

- **SRC-0553** `research/proto/chesscom/skills/v1/eligibility_error.proto` — [preserved redacted evidence](../evidence/text/a4b9cafb5078653ed6e185fd9e91ea11864f42721715bc7799643f01eb3e3ac8.proto)
  Character offset 244.

```text
sscom.skills.v1.EligibilityError.Reason reason = 1;
  enum Reason {
    REASON_UNSPECIFIED = 0;
    REASON_GAME_SKILL_POINTS_EXPIRED = 1;
    REASON_NOT_A_GAME_PARTICIPANT = 2;
    REASON_PLAYER_DISABLED = 3;
    REASON_GAME_NOT_FOUND = 4;
  }
}

```

**Source references:** SRC-0553, SRC-1524  
**URL references:** None independently associated  
**Related findings:** FND-08304, FND-08305, FND-08306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08309"></a>
## FND-08309: chesscom.skills.v1.EligibilityError.Reason.REASON_NOT_A_GAME_PARTICIPANT = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

REASON_NOT_A_GAME_PARTICIPANT = 2;

### Evidence

- **SRC-0553** `research/proto/chesscom/skills/v1/eligibility_error.proto` — [preserved redacted evidence](../evidence/text/a4b9cafb5078653ed6e185fd9e91ea11864f42721715bc7799643f01eb3e3ac8.proto)
  Character offset 286.

```text
ason = 1;
  enum Reason {
    REASON_UNSPECIFIED = 0;
    REASON_GAME_SKILL_POINTS_EXPIRED = 1;
    REASON_NOT_A_GAME_PARTICIPANT = 2;
    REASON_PLAYER_DISABLED = 3;
    REASON_GAME_NOT_FOUND = 4;
  }
}

```

**Source references:** SRC-0553, SRC-1524  
**URL references:** None independently associated  
**Related findings:** FND-08304, FND-08305, FND-08306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08310"></a>
## FND-08310: chesscom.skills.v1.EligibilityError.Reason.REASON_PLAYER_DISABLED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

REASON_PLAYER_DISABLED = 3;

### Evidence

- **SRC-0553** `research/proto/chesscom/skills/v1/eligibility_error.proto` — [preserved redacted evidence](../evidence/text/a4b9cafb5078653ed6e185fd9e91ea11864f42721715bc7799643f01eb3e3ac8.proto)
  Character offset 325.

```text
SPECIFIED = 0;
    REASON_GAME_SKILL_POINTS_EXPIRED = 1;
    REASON_NOT_A_GAME_PARTICIPANT = 2;
    REASON_PLAYER_DISABLED = 3;
    REASON_GAME_NOT_FOUND = 4;
  }
}

```

**Source references:** SRC-0553, SRC-1524  
**URL references:** None independently associated  
**Related findings:** FND-08304, FND-08305, FND-08306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08311"></a>
## FND-08311: chesscom.skills.v1.EligibilityError.Reason.REASON_GAME_NOT_FOUND = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

REASON_GAME_NOT_FOUND = 4;

### Evidence

- **SRC-0553** `research/proto/chesscom/skills/v1/eligibility_error.proto` — [preserved redacted evidence](../evidence/text/a4b9cafb5078653ed6e185fd9e91ea11864f42721715bc7799643f01eb3e3ac8.proto)
  Character offset 357.

```text
KILL_POINTS_EXPIRED = 1;
    REASON_NOT_A_GAME_PARTICIPANT = 2;
    REASON_PLAYER_DISABLED = 3;
    REASON_GAME_NOT_FOUND = 4;
  }
}

```

**Source references:** SRC-0553, SRC-1524  
**URL references:** None independently associated  
**Related findings:** FND-08304, FND-08305, FND-08306

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08312"></a>
## FND-08312: enum declaration: chesscom.skills.v1.SkillCategory

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SkillCategory {

### Evidence

- **SRC-0554** `research/proto/chesscom/skills/v1/skill_category.proto` — [preserved redacted evidence](../evidence/text/dfcfb009d4c48c67d25e042d3882bf96936eb668aa6fdad909052d887e83d2bd.proto)
  Character offset 99.

```text
// source: chesscom/skills/v1/skill_category.proto
// syntax: proto3

package chesscom.skills.v1;

enum SkillCategory {
  SKILL_CATEGORY_UNSPECIFIED = 0;
  SKILL_CATEGORY_FUNDAMENTALS = 1;
  SKILL_CATEGORY_OPENINGS = 2;
  SKILL_CATEGORY_TACTICS = 3;
  SKILL_CATEGORY_STRATEGY = 4;
  SKILL_CATEGORY_ENDGAME = 5;
}

```

**Source references:** SRC-0554, SRC-1525  
**URL references:** None independently associated  
**Related findings:** FND-08313, FND-08314

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08313"></a>
## FND-08313: chesscom.skills.v1.SkillCategory.SKILL_CATEGORY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_CATEGORY_UNSPECIFIED = 0;

### Evidence

- **SRC-0554** `research/proto/chesscom/skills/v1/skill_category.proto` — [preserved redacted evidence](../evidence/text/dfcfb009d4c48c67d25e042d3882bf96936eb668aa6fdad909052d887e83d2bd.proto)
  Character offset 122.

```text
ills/v1/skill_category.proto
// syntax: proto3

package chesscom.skills.v1;

enum SkillCategory {
  SKILL_CATEGORY_UNSPECIFIED = 0;
  SKILL_CATEGORY_FUNDAMENTALS = 1;
  SKILL_CATEGORY_OPENINGS = 2;
  SKILL_CATEGORY_TACTICS = 3;
  SKILL_CATEGORY_STRATEGY = 4;
  SKILL_CATEGORY_ENDGAME = 5;
}

```

**Source references:** SRC-0554, SRC-1525  
**URL references:** None independently associated  
**Related findings:** FND-08312, FND-08314

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08314"></a>
## FND-08314: chesscom.skills.v1.SkillCategory.SKILL_CATEGORY_FUNDAMENTALS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_CATEGORY_FUNDAMENTALS = 1;

### Evidence

- **SRC-0554** `research/proto/chesscom/skills/v1/skill_category.proto` — [preserved redacted evidence](../evidence/text/dfcfb009d4c48c67d25e042d3882bf96936eb668aa6fdad909052d887e83d2bd.proto)
  Character offset 156.

```text
ntax: proto3

package chesscom.skills.v1;

enum SkillCategory {
  SKILL_CATEGORY_UNSPECIFIED = 0;
  SKILL_CATEGORY_FUNDAMENTALS = 1;
  SKILL_CATEGORY_OPENINGS = 2;
  SKILL_CATEGORY_TACTICS = 3;
  SKILL_CATEGORY_STRATEGY = 4;
  SKILL_CATEGORY_ENDGAME = 5;
}

```

**Source references:** SRC-0554, SRC-1525  
**URL references:** None independently associated  
**Related findings:** FND-08312, FND-08313

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08315"></a>
## FND-08315: chesscom.skills.v1.SkillCategory.SKILL_CATEGORY_OPENINGS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_CATEGORY_OPENINGS = 2;

### Evidence

- **SRC-0554** `research/proto/chesscom/skills/v1/skill_category.proto` — [preserved redacted evidence](../evidence/text/dfcfb009d4c48c67d25e042d3882bf96936eb668aa6fdad909052d887e83d2bd.proto)
  Character offset 191.

```text
ls.v1;

enum SkillCategory {
  SKILL_CATEGORY_UNSPECIFIED = 0;
  SKILL_CATEGORY_FUNDAMENTALS = 1;
  SKILL_CATEGORY_OPENINGS = 2;
  SKILL_CATEGORY_TACTICS = 3;
  SKILL_CATEGORY_STRATEGY = 4;
  SKILL_CATEGORY_ENDGAME = 5;
}

```

**Source references:** SRC-0554, SRC-1525  
**URL references:** None independently associated  
**Related findings:** FND-08312, FND-08313, FND-08314

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08316"></a>
## FND-08316: chesscom.skills.v1.SkillCategory.SKILL_CATEGORY_TACTICS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_CATEGORY_TACTICS = 3;

### Evidence

- **SRC-0554** `research/proto/chesscom/skills/v1/skill_category.proto` — [preserved redacted evidence](../evidence/text/dfcfb009d4c48c67d25e042d3882bf96936eb668aa6fdad909052d887e83d2bd.proto)
  Character offset 222.

```text
SKILL_CATEGORY_UNSPECIFIED = 0;
  SKILL_CATEGORY_FUNDAMENTALS = 1;
  SKILL_CATEGORY_OPENINGS = 2;
  SKILL_CATEGORY_TACTICS = 3;
  SKILL_CATEGORY_STRATEGY = 4;
  SKILL_CATEGORY_ENDGAME = 5;
}

```

**Source references:** SRC-0554, SRC-1525  
**URL references:** None independently associated  
**Related findings:** FND-08312, FND-08313, FND-08314

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08317"></a>
## FND-08317: chesscom.skills.v1.SkillCategory.SKILL_CATEGORY_STRATEGY = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_CATEGORY_STRATEGY = 4;

### Evidence

- **SRC-0554** `research/proto/chesscom/skills/v1/skill_category.proto` — [preserved redacted evidence](../evidence/text/dfcfb009d4c48c67d25e042d3882bf96936eb668aa6fdad909052d887e83d2bd.proto)
  Character offset 252.

```text
;
  SKILL_CATEGORY_FUNDAMENTALS = 1;
  SKILL_CATEGORY_OPENINGS = 2;
  SKILL_CATEGORY_TACTICS = 3;
  SKILL_CATEGORY_STRATEGY = 4;
  SKILL_CATEGORY_ENDGAME = 5;
}

```

**Source references:** SRC-0554, SRC-1525  
**URL references:** None independently associated  
**Related findings:** FND-08312, FND-08313, FND-08314

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08318"></a>
## FND-08318: chesscom.skills.v1.SkillCategory.SKILL_CATEGORY_ENDGAME = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SKILL_CATEGORY_ENDGAME = 5;

### Evidence

- **SRC-0554** `research/proto/chesscom/skills/v1/skill_category.proto` — [preserved redacted evidence](../evidence/text/dfcfb009d4c48c67d25e042d3882bf96936eb668aa6fdad909052d887e83d2bd.proto)
  Character offset 283.

```text
 = 1;
  SKILL_CATEGORY_OPENINGS = 2;
  SKILL_CATEGORY_TACTICS = 3;
  SKILL_CATEGORY_STRATEGY = 4;
  SKILL_CATEGORY_ENDGAME = 5;
}

```

**Source references:** SRC-0554, SRC-1525  
**URL references:** None independently associated  
**Related findings:** FND-08312, FND-08313, FND-08314

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08319"></a>
## FND-08319: message declaration: chesscom.skills.v1.SkillPointGained

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillPointGained {

### Evidence

- **SRC-0555** `research/proto/chesscom/skills/v1/skill_point_gained.proto` — [preserved redacted evidence](../evidence/text/1367324e5df98f4976f8a6550f6bea968ecf48ff515cb03dd7b54b777f4bc615.proto)
  Character offset 103.

```text
source: chesscom/skills/v1/skill_point_gained.proto
// syntax: proto3

package chesscom.skills.v1;

message SkillPointGained {
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional uint32 new_value = 2;
  optional uint32 max_value = 3;
}

```

**Source references:** SRC-0555, SRC-1526  
**URL references:** None independently associated  
**Related findings:** FND-08320, FND-08321

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08320"></a>
## FND-08320: chesscom.skills.v1.SkillPointGained.skill = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Skill skill = 1;

### Evidence

- **SRC-0555** `research/proto/chesscom/skills/v1/skill_point_gained.proto` — [preserved redacted evidence](../evidence/text/1367324e5df98f4976f8a6550f6bea968ecf48ff515cb03dd7b54b777f4bc615.proto)
  Character offset 132.

```text
ill_point_gained.proto
// syntax: proto3

package chesscom.skills.v1;

message SkillPointGained {
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional uint32 new_value = 2;
  optional uint32 max_value = 3;
}

```

**Source references:** SRC-0555, SRC-1526  
**URL references:** None independently associated  
**Related findings:** FND-08319, FND-08321

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08321"></a>
## FND-08321: chesscom.skills.v1.SkillPointGained.new_value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 new_value = 2;

### Evidence

- **SRC-0555** `research/proto/chesscom/skills/v1/skill_point_gained.proto` — [preserved redacted evidence](../evidence/text/1367324e5df98f4976f8a6550f6bea968ecf48ff515cb03dd7b54b777f4bc615.proto)
  Character offset 192.

```text
kills.v1;

message SkillPointGained {
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional uint32 new_value = 2;
  optional uint32 max_value = 3;
}

```

**Source references:** SRC-0555, SRC-1526  
**URL references:** None independently associated  
**Related findings:** FND-08319, FND-08320

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08322"></a>
## FND-08322: chesscom.skills.v1.SkillPointGained.max_value = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 max_value = 3;

### Evidence

- **SRC-0555** `research/proto/chesscom/skills/v1/skill_point_gained.proto` — [preserved redacted evidence](../evidence/text/1367324e5df98f4976f8a6550f6bea968ecf48ff515cb03dd7b54b777f4bc615.proto)
  Character offset 225.

```text
ed {
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional uint32 new_value = 2;
  optional uint32 max_value = 3;
}

```

**Source references:** SRC-0555, SRC-1526  
**URL references:** None independently associated  
**Related findings:** FND-08319, FND-08320, FND-08321

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08323"></a>
## FND-08323: message declaration: chesscom.skills.v1.SkillView

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillView {

### Evidence

- **SRC-0556** `research/proto/chesscom/skills/v1/skill_view.proto` — [preserved redacted evidence](../evidence/text/ec6149379087a21f5c652773cbc3c39144f1a593ab6716f6fe8f281fa33130c9.proto)
  Character offset 95.

```text
// source: chesscom/skills/v1/skill_view.proto
// syntax: proto3

package chesscom.skills.v1;

message SkillView {
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional .chesscom.skills.v1.SkillCategory category = 2;
  optional uint32 points_required = 3;
  optional uint32 points_gained = 4;
  optional bool is_unlocked = 5;
  optional bool is_mastered = 6;
}

```

**Source references:** SRC-0556, SRC-1527  
**URL references:** None independently associated  
**Related findings:** FND-08324, FND-08325

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08324"></a>
## FND-08324: chesscom.skills.v1.SkillView.skill = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Skill skill = 1;

### Evidence

- **SRC-0556** `research/proto/chesscom/skills/v1/skill_view.proto` — [preserved redacted evidence](../evidence/text/ec6149379087a21f5c652773cbc3c39144f1a593ab6716f6fe8f281fa33130c9.proto)
  Character offset 117.

```text
om/skills/v1/skill_view.proto
// syntax: proto3

package chesscom.skills.v1;

message SkillView {
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional .chesscom.skills.v1.SkillCategory category = 2;
  optional uint32 points_required = 3;
  optional uint32 points_gained = 4;
  optional bool is_unlocked = 5;
  optional bool is_mastered = 6;
}

```

**Source references:** SRC-0556, SRC-1527  
**URL references:** None independently associated  
**Related findings:** FND-08323, FND-08325

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08325"></a>
## FND-08325: chesscom.skills.v1.SkillView.category = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.skills.v1.SkillCategory category = 2;

### Evidence

- **SRC-0556** `research/proto/chesscom/skills/v1/skill_view.proto` — [preserved redacted evidence](../evidence/text/ec6149379087a21f5c652773cbc3c39144f1a593ab6716f6fe8f281fa33130c9.proto)
  Character offset 177.

```text
sscom.skills.v1;

message SkillView {
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional .chesscom.skills.v1.SkillCategory category = 2;
  optional uint32 points_required = 3;
  optional uint32 points_gained = 4;
  optional bool is_unlocked = 5;
  optional bool is_mastered = 6;
}

```

**Source references:** SRC-0556, SRC-1527  
**URL references:** None independently associated  
**Related findings:** FND-08323, FND-08324

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08326"></a>
## FND-08326: chesscom.skills.v1.SkillView.points_required = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 points_required = 3;

### Evidence

- **SRC-0556** `research/proto/chesscom/skills/v1/skill_view.proto` — [preserved redacted evidence](../evidence/text/ec6149379087a21f5c652773cbc3c39144f1a593ab6716f6fe8f281fa33130c9.proto)
  Character offset 236.

```text
explanation_engine.v1.Skill skill = 1;
  optional .chesscom.skills.v1.SkillCategory category = 2;
  optional uint32 points_required = 3;
  optional uint32 points_gained = 4;
  optional bool is_unlocked = 5;
  optional bool is_mastered = 6;
}

```

**Source references:** SRC-0556, SRC-1527  
**URL references:** None independently associated  
**Related findings:** FND-08323, FND-08324, FND-08325

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08327"></a>
## FND-08327: chesscom.skills.v1.SkillView.points_gained = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 points_gained = 4;

### Evidence

- **SRC-0556** `research/proto/chesscom/skills/v1/skill_view.proto` — [preserved redacted evidence](../evidence/text/ec6149379087a21f5c652773cbc3c39144f1a593ab6716f6fe8f281fa33130c9.proto)
  Character offset 275.

```text
  optional .chesscom.skills.v1.SkillCategory category = 2;
  optional uint32 points_required = 3;
  optional uint32 points_gained = 4;
  optional bool is_unlocked = 5;
  optional bool is_mastered = 6;
}

```

**Source references:** SRC-0556, SRC-1527  
**URL references:** None independently associated  
**Related findings:** FND-08323, FND-08324, FND-08325

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08328"></a>
## FND-08328: chesscom.skills.v1.SkillView.is_unlocked = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_unlocked = 5;

### Evidence

- **SRC-0556** `research/proto/chesscom/skills/v1/skill_view.proto` — [preserved redacted evidence](../evidence/text/ec6149379087a21f5c652773cbc3c39144f1a593ab6716f6fe8f281fa33130c9.proto)
  Character offset 312.

```text
ategory category = 2;
  optional uint32 points_required = 3;
  optional uint32 points_gained = 4;
  optional bool is_unlocked = 5;
  optional bool is_mastered = 6;
}

```

**Source references:** SRC-0556, SRC-1527  
**URL references:** None independently associated  
**Related findings:** FND-08323, FND-08324, FND-08325

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08329"></a>
## FND-08329: chesscom.skills.v1.SkillView.is_mastered = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_mastered = 6;

### Evidence

- **SRC-0556** `research/proto/chesscom/skills/v1/skill_view.proto` — [preserved redacted evidence](../evidence/text/ec6149379087a21f5c652773cbc3c39144f1a593ab6716f6fe8f281fa33130c9.proto)
  Character offset 345.

```text
uint32 points_required = 3;
  optional uint32 points_gained = 4;
  optional bool is_unlocked = 5;
  optional bool is_mastered = 6;
}

```

**Source references:** SRC-0556, SRC-1527  
**URL references:** None independently associated  
**Related findings:** FND-08323, FND-08324, FND-08325

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08330"></a>
## FND-08330: message declaration: chesscom.skills.v1.SkillConfiguration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillConfiguration {

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 105.

```text
urce: chesscom/skills/v1/skills_configuration.proto
// syntax: proto3

package chesscom.skills.v1;

message SkillConfiguration {
  repeated .chesscom.skills.v1.SkillItemConfiguration skill_items = 1;
}

message SkillItemConfiguration {
  oneof unlocking_condition {
  .chesscom.skills.v1.UnlockedByAll unlocked_by_all = 7;
  .chesscom.skills.v1.UnlockedByAny unlocked_by_any = 8;
  }
  optional .chesscom.explanation_eng
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08331, FND-08332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08331"></a>
## FND-08331: chesscom.skills.v1.SkillConfiguration.skill_items = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.skills.v1.SkillItemConfiguration skill_items = 1;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 136.

```text
_configuration.proto
// syntax: proto3

package chesscom.skills.v1;

message SkillConfiguration {
  repeated .chesscom.skills.v1.SkillItemConfiguration skill_items = 1;
}

message SkillItemConfiguration {
  oneof unlocking_condition {
  .chesscom.skills.v1.UnlockedByAll unlocked_by_all = 7;
  .chesscom.skills.v1.UnlockedByAny unlocked_by_any = 8;
  }
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optio
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08332"></a>
## FND-08332: message declaration: chesscom.skills.v1.SkillItemConfiguration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillItemConfiguration {

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 208.

```text
sage SkillConfiguration {
  repeated .chesscom.skills.v1.SkillItemConfiguration skill_items = 1;
}

message SkillItemConfiguration {
  oneof unlocking_condition {
  .chesscom.skills.v1.UnlockedByAll unlocked_by_all = 7;
  .chesscom.skills.v1.UnlockedByAny unlocked_by_any = 8;
  }
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional .chesscom.i18n.v1.Translation name = 2;
  optional .chesscom.skills.
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08333"></a>
## FND-08333: oneof declaration: chesscom.skills.v1.SkillItemConfiguration.unlocking_condition

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof unlocking_condition {

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 243.

```text
d .chesscom.skills.v1.SkillItemConfiguration skill_items = 1;
}

message SkillItemConfiguration {
  oneof unlocking_condition {
  .chesscom.skills.v1.UnlockedByAll unlocked_by_all = 7;
  .chesscom.skills.v1.UnlockedByAny unlocked_by_any = 8;
  }
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional .chesscom.i18n.v1.Translation name = 2;
  optional .chesscom.skills.v1.SkillCategory category = 3;
  op
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08334"></a>
## FND-08334: chesscom.skills.v1.SkillItemConfiguration.unlocked_by_all = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.skills.v1.UnlockedByAll unlocked_by_all = 7;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 273.

```text
mConfiguration skill_items = 1;
}

message SkillItemConfiguration {
  oneof unlocking_condition {
  .chesscom.skills.v1.UnlockedByAll unlocked_by_all = 7;
  .chesscom.skills.v1.UnlockedByAny unlocked_by_any = 8;
  }
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional .chesscom.i18n.v1.Translation name = 2;
  optional .chesscom.skills.v1.SkillCategory category = 3;
  optional uint32 points_to_master
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08335"></a>
## FND-08335: chesscom.skills.v1.SkillItemConfiguration.unlocked_by_any = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.skills.v1.UnlockedByAny unlocked_by_any = 8;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 330.

```text
guration {
  oneof unlocking_condition {
  .chesscom.skills.v1.UnlockedByAll unlocked_by_all = 7;
  .chesscom.skills.v1.UnlockedByAny unlocked_by_any = 8;
  }
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional .chesscom.i18n.v1.Translation name = 2;
  optional .chesscom.skills.v1.SkillCategory category = 3;
  optional uint32 points_to_master = 4;
  optional string diagram = 5;
  optional .chesscom
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08336"></a>
## FND-08336: chesscom.skills.v1.SkillItemConfiguration.skill = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.explanation_engine.v1.Skill skill = 1;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 391.

```text
1.UnlockedByAll unlocked_by_all = 7;
  .chesscom.skills.v1.UnlockedByAny unlocked_by_any = 8;
  }
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional .chesscom.i18n.v1.Translation name = 2;
  optional .chesscom.skills.v1.SkillCategory category = 3;
  optional uint32 points_to_master = 4;
  optional string diagram = 5;
  optional .chesscom.i18n.v1.Translation description = 6;
  optional .chesscom.ap
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08337"></a>
## FND-08337: chesscom.skills.v1.SkillItemConfiguration.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.i18n.v1.Translation name = 2;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 451.

```text
nlockedByAny unlocked_by_any = 8;
  }
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional .chesscom.i18n.v1.Translation name = 2;
  optional .chesscom.skills.v1.SkillCategory category = 3;
  optional uint32 points_to_master = 4;
  optional string diagram = 5;
  optional .chesscom.i18n.v1.Translation description = 6;
  optional .chesscom.api.v1.Asset icon_png = 9;
  optional .chesscom.api.v1.Asset i
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08338"></a>
## FND-08338: chesscom.skills.v1.SkillItemConfiguration.category = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.skills.v1.SkillCategory category = 3;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 502.

```text
hesscom.explanation_engine.v1.Skill skill = 1;
  optional .chesscom.i18n.v1.Translation name = 2;
  optional .chesscom.skills.v1.SkillCategory category = 3;
  optional uint32 points_to_master = 4;
  optional string diagram = 5;
  optional .chesscom.i18n.v1.Translation description = 6;
  optional .chesscom.api.v1.Asset icon_png = 9;
  optional .chesscom.api.v1.Asset icon_svg = 10;
}

message UnlockedByAll {
  repeated
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08339"></a>
## FND-08339: chesscom.skills.v1.SkillItemConfiguration.points_to_master = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional uint32 points_to_master = 4;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 561.

```text
chesscom.i18n.v1.Translation name = 2;
  optional .chesscom.skills.v1.SkillCategory category = 3;
  optional uint32 points_to_master = 4;
  optional string diagram = 5;
  optional .chesscom.i18n.v1.Translation description = 6;
  optional .chesscom.api.v1.Asset icon_png = 9;
  optional .chesscom.api.v1.Asset icon_svg = 10;
}

message UnlockedByAll {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_all = 1;
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08340"></a>
## FND-08340: chesscom.skills.v1.SkillItemConfiguration.diagram = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string diagram = 5;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 601.

```text
 optional .chesscom.skills.v1.SkillCategory category = 3;
  optional uint32 points_to_master = 4;
  optional string diagram = 5;
  optional .chesscom.i18n.v1.Translation description = 6;
  optional .chesscom.api.v1.Asset icon_png = 9;
  optional .chesscom.api.v1.Asset icon_svg = 10;
}

message UnlockedByAll {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_all = 1;
}

message UnlockedByAny {
  repeated .
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08341"></a>
## FND-08341: chesscom.skills.v1.SkillItemConfiguration.description = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.i18n.v1.Translation description = 6;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 632.

```text
killCategory category = 3;
  optional uint32 points_to_master = 4;
  optional string diagram = 5;
  optional .chesscom.i18n.v1.Translation description = 6;
  optional .chesscom.api.v1.Asset icon_png = 9;
  optional .chesscom.api.v1.Asset icon_svg = 10;
}

message UnlockedByAll {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_all = 1;
}

message UnlockedByAny {
  repeated .chesscom.explanation_engine.v1.
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08342"></a>
## FND-08342: chesscom.skills.v1.SkillItemConfiguration.icon_png = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Asset icon_png = 9;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 690.

```text
ter = 4;
  optional string diagram = 5;
  optional .chesscom.i18n.v1.Translation description = 6;
  optional .chesscom.api.v1.Asset icon_png = 9;
  optional .chesscom.api.v1.Asset icon_svg = 10;
}

message UnlockedByAll {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_all = 1;
}

message UnlockedByAny {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_any = 1;
}

message SkillCategoryConfigu
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08343"></a>
## FND-08343: chesscom.skills.v1.SkillItemConfiguration.icon_svg = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Asset icon_svg = 10;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 738.

```text
al .chesscom.i18n.v1.Translation description = 6;
  optional .chesscom.api.v1.Asset icon_png = 9;
  optional .chesscom.api.v1.Asset icon_svg = 10;
}

message UnlockedByAll {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_all = 1;
}

message UnlockedByAny {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_any = 1;
}

message SkillCategoryConfiguration {
  repeated .chesscom.skills.v1.SkillCat
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08344"></a>
## FND-08344: message declaration: chesscom.skills.v1.UnlockedByAll

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UnlockedByAll {

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 788.

```text
  optional .chesscom.api.v1.Asset icon_png = 9;
  optional .chesscom.api.v1.Asset icon_svg = 10;
}

message UnlockedByAll {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_all = 1;
}

message UnlockedByAny {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_any = 1;
}

message SkillCategoryConfiguration {
  repeated .chesscom.skills.v1.SkillCategoryItemConfiguration skills_categories = 1;
}

m
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08345"></a>
## FND-08345: chesscom.skills.v1.UnlockedByAll.unlocked_by_all = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.Skill unlocked_by_all = 1;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 814.

```text
1.Asset icon_png = 9;
  optional .chesscom.api.v1.Asset icon_svg = 10;
}

message UnlockedByAll {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_all = 1;
}

message UnlockedByAny {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_any = 1;
}

message SkillCategoryConfiguration {
  repeated .chesscom.skills.v1.SkillCategoryItemConfiguration skills_categories = 1;
}

message SkillCategoryItemCo
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08346"></a>
## FND-08346: message declaration: chesscom.skills.v1.UnlockedByAny

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UnlockedByAny {

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 885.

```text
}

message UnlockedByAll {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_all = 1;
}

message UnlockedByAny {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_any = 1;
}

message SkillCategoryConfiguration {
  repeated .chesscom.skills.v1.SkillCategoryItemConfiguration skills_categories = 1;
}

message SkillCategoryItemConfiguration {
  optional .chesscom.skills.v1.SkillCategory category = 1
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08347"></a>
## FND-08347: chesscom.skills.v1.UnlockedByAny.unlocked_by_any = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.Skill unlocked_by_any = 1;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 911.

```text

  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_all = 1;
}

message UnlockedByAny {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_any = 1;
}

message SkillCategoryConfiguration {
  repeated .chesscom.skills.v1.SkillCategoryItemConfiguration skills_categories = 1;
}

message SkillCategoryItemConfiguration {
  optional .chesscom.skills.v1.SkillCategory category = 1;
  optional .chesscom.i18
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08348"></a>
## FND-08348: message declaration: chesscom.skills.v1.SkillCategoryConfiguration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillCategoryConfiguration {

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 982.

```text
}

message UnlockedByAny {
  repeated .chesscom.explanation_engine.v1.Skill unlocked_by_any = 1;
}

message SkillCategoryConfiguration {
  repeated .chesscom.skills.v1.SkillCategoryItemConfiguration skills_categories = 1;
}

message SkillCategoryItemConfiguration {
  optional .chesscom.skills.v1.SkillCategory category = 1;
  optional .chesscom.i18n.v1.Translation name = 2;
}

```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08349"></a>
## FND-08349: chesscom.skills.v1.SkillCategoryConfiguration.skills_categories = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.skills.v1.SkillCategoryItemConfiguration skills_categories = 1;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 1021.

```text
chesscom.explanation_engine.v1.Skill unlocked_by_any = 1;
}

message SkillCategoryConfiguration {
  repeated .chesscom.skills.v1.SkillCategoryItemConfiguration skills_categories = 1;
}

message SkillCategoryItemConfiguration {
  optional .chesscom.skills.v1.SkillCategory category = 1;
  optional .chesscom.i18n.v1.Translation name = 2;
}

```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08350"></a>
## FND-08350: message declaration: chesscom.skills.v1.SkillCategoryItemConfiguration

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SkillCategoryItemConfiguration {

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 1107.

```text
iguration {
  repeated .chesscom.skills.v1.SkillCategoryItemConfiguration skills_categories = 1;
}

message SkillCategoryItemConfiguration {
  optional .chesscom.skills.v1.SkillCategory category = 1;
  optional .chesscom.i18n.v1.Translation name = 2;
}

```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08351"></a>
## FND-08351: chesscom.skills.v1.SkillCategoryItemConfiguration.category = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.skills.v1.SkillCategory category = 1;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 1150.

```text
SkillCategoryItemConfiguration skills_categories = 1;
}

message SkillCategoryItemConfiguration {
  optional .chesscom.skills.v1.SkillCategory category = 1;
  optional .chesscom.i18n.v1.Translation name = 2;
}

```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08352"></a>
## FND-08352: chesscom.skills.v1.SkillCategoryItemConfiguration.name = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.i18n.v1.Translation name = 2;

### Evidence

- **SRC-0557** `research/proto/chesscom/skills/v1/skills_configuration.proto` — [preserved redacted evidence](../evidence/text/572ee4b708165380fd75edec6c5bbbd7dd0b0ee4f5ed7e7e89c7fcbafe58c3d5.proto)
  Character offset 451.

```text
nlockedByAny unlocked_by_any = 8;
  }
  optional .chesscom.explanation_engine.v1.Skill skill = 1;
  optional .chesscom.i18n.v1.Translation name = 2;
  optional .chesscom.skills.v1.SkillCategory category = 3;
  optional uint32 points_to_master = 4;
  optional string diagram = 5;
  optional .chesscom.i18n.v1.Translation description = 6;
  optional .chesscom.api.v1.Asset icon_png = 9;
  optional .chesscom.api.v1.Asset i
```

**Source references:** SRC-0557, SRC-1528  
**URL references:** None independently associated  
**Related findings:** FND-08330, FND-08331, FND-08332

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08353"></a>
## FND-08353: message declaration: chesscom.skills.v1.GainSkillPointsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GainSkillPointsRequest {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 99.

```text
// source: chesscom/skills/v1/skills_service.proto
// syntax: proto3

package chesscom.skills.v1;

message GainSkillPointsRequest {
  oneof input {
  .chesscom.skills.v1.GainSkillPointsRequest.CoachInput coach_input = 3;
  .chesscom.skills.v1.GainSkillPointsRequest.GameReviewInput game_review_input = 4;
  }
  optional string game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;

```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08354"></a>
## FND-08354: oneof declaration: chesscom.skills.v1.GainSkillPointsRequest.input

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof input {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 134.

```text
ls_service.proto
// syntax: proto3

package chesscom.skills.v1;

message GainSkillPointsRequest {
  oneof input {
  .chesscom.skills.v1.GainSkillPointsRequest.CoachInput coach_input = 3;
  .chesscom.skills.v1.GainSkillPointsRequest.GameReviewInput game_review_input = 4;
  }
  optional string game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
  message CoachInput {
  optional .
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08355"></a>
## FND-08355: chesscom.skills.v1.GainSkillPointsRequest.coach_input = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.skills.v1.GainSkillPointsRequest.CoachInput coach_input = 3;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 150.

```text

// syntax: proto3

package chesscom.skills.v1;

message GainSkillPointsRequest {
  oneof input {
  .chesscom.skills.v1.GainSkillPointsRequest.CoachInput coach_input = 3;
  .chesscom.skills.v1.GainSkillPointsRequest.GameReviewInput game_review_input = 4;
  }
  optional string game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
  message CoachInput {
  optional .chesscom.chess.v
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08356"></a>
## FND-08356: chesscom.skills.v1.GainSkillPointsRequest.game_review_input = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.skills.v1.GainSkillPointsRequest.GameReviewInput game_review_input = 4;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 223.

```text
equest {
  oneof input {
  .chesscom.skills.v1.GainSkillPointsRequest.CoachInput coach_input = 3;
  .chesscom.skills.v1.GainSkillPointsRequest.GameReviewInput game_review_input = 4;
  }
  optional string game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
  message CoachInput {
  optional .chesscom.chess.v1.Color player_color = 1;
  }
  message GameReviewInput {
  }
}

message 
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08357"></a>
## FND-08357: chesscom.skills.v1.GainSkillPointsRequest.game_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string game_id = 1;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 311.

```text
nput = 3;
  .chesscom.skills.v1.GainSkillPointsRequest.GameReviewInput game_review_input = 4;
  }
  optional string game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
  message CoachInput {
  optional .chesscom.chess.v1.Color player_color = 1;
  }
  message GameReviewInput {
  }
}

message GainSkillPointsResponse {
  oneof result {
  .chesscom.skills.v1.GainSkillPointsResponse
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08358"></a>
## FND-08358: chesscom.skills.v1.GainSkillPointsRequest.skill_positions = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 342.

```text
.GainSkillPointsRequest.GameReviewInput game_review_input = 4;
  }
  optional string game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
  message CoachInput {
  optional .chesscom.chess.v1.Color player_color = 1;
  }
  message GameReviewInput {
  }
}

message GainSkillPointsResponse {
  oneof result {
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess success
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08359"></a>
## FND-08359: message declaration: chesscom.skills.v1.GainSkillPointsRequest.CoachInput

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CoachInput {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 421.

```text
tring game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
  message CoachInput {
  optional .chesscom.chess.v1.Color player_color = 1;
  }
  message GameReviewInput {
  }
}

message GainSkillPointsResponse {
  oneof result {
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess success = 1;
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsFailure fail
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08360"></a>
## FND-08360: chesscom.skills.v1.GainSkillPointsRequest.CoachInput.player_color = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.chess.v1.Color player_color = 1;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 444.

```text
peated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
  message CoachInput {
  optional .chesscom.chess.v1.Color player_color = 1;
  }
  message GameReviewInput {
  }
}

message GainSkillPointsResponse {
  oneof result {
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess success = 1;
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsFailure failure = 2;
  }
  message 
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08361"></a>
## FND-08361: message declaration: chesscom.skills.v1.GainSkillPointsRequest.GameReviewInput

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GameReviewInput {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 502.

```text
l_positions = 2;
  message CoachInput {
  optional .chesscom.chess.v1.Color player_color = 1;
  }
  message GameReviewInput {
  }
}

message GainSkillPointsResponse {
  oneof result {
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess success = 1;
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsFailure failure = 2;
  }
  message GainSkillPointsSuccess {
  repeated .chesscom.explanation_
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08362"></a>
## FND-08362: message declaration: chesscom.skills.v1.GainSkillPointsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GainSkillPointsResponse {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 535.

```text
nput {
  optional .chesscom.chess.v1.Color player_color = 1;
  }
  message GameReviewInput {
  }
}

message GainSkillPointsResponse {
  oneof result {
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess success = 1;
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsFailure failure = 2;
  }
  message GainSkillPointsSuccess {
  repeated .chesscom.explanation_engine.v1.Skill skills_unlocked =
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08363"></a>
## FND-08363: oneof declaration: chesscom.skills.v1.GainSkillPointsResponse.result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof result {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 571.

```text
.Color player_color = 1;
  }
  message GameReviewInput {
  }
}

message GainSkillPointsResponse {
  oneof result {
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess success = 1;
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsFailure failure = 2;
  }
  message GainSkillPointsSuccess {
  repeated .chesscom.explanation_engine.v1.Skill skills_unlocked = 1;
  repeated .chesscom.skills.v1.S
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08364"></a>
## FND-08364: chesscom.skills.v1.GainSkillPointsResponse.success = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess success = 1;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 588.

```text
or = 1;
  }
  message GameReviewInput {
  }
}

message GainSkillPointsResponse {
  oneof result {
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess success = 1;
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsFailure failure = 2;
  }
  message GainSkillPointsSuccess {
  repeated .chesscom.explanation_engine.v1.Skill skills_unlocked = 1;
  repeated .chesscom.skills.v1.SkillPointGained s
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08365"></a>
## FND-08365: chesscom.skills.v1.GainSkillPointsResponse.failure = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsFailure failure = 2;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 670.

```text
 oneof result {
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess success = 1;
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsFailure failure = 2;
  }
  message GainSkillPointsSuccess {
  repeated .chesscom.explanation_engine.v1.Skill skills_unlocked = 1;
  repeated .chesscom.skills.v1.SkillPointGained skill_points_gained = 2;
  repeated .chesscom.explanation_engine.v1.Skill skills_ma
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08366"></a>
## FND-08366: message declaration: chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GainSkillPointsSuccess {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 756.

```text
uccess = 1;
  .chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsFailure failure = 2;
  }
  message GainSkillPointsSuccess {
  repeated .chesscom.explanation_engine.v1.Skill skills_unlocked = 1;
  repeated .chesscom.skills.v1.SkillPointGained skill_points_gained = 2;
  repeated .chesscom.explanation_engine.v1.Skill skills_mastered = 3;
  optional bool has_mastered_all = 4;
  optional bool is_first_ever_skill_
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08367"></a>
## FND-08367: chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess.skills_unlocked = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.Skill skills_unlocked = 1;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 791.

```text
ainSkillPointsResponse.GainSkillPointsFailure failure = 2;
  }
  message GainSkillPointsSuccess {
  repeated .chesscom.explanation_engine.v1.Skill skills_unlocked = 1;
  repeated .chesscom.skills.v1.SkillPointGained skill_points_gained = 2;
  repeated .chesscom.explanation_engine.v1.Skill skills_mastered = 3;
  optional bool has_mastered_all = 4;
  optional bool is_first_ever_skill_point = 5;
  }
  message GainSkillP
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08368"></a>
## FND-08368: chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess.skill_points_gained = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.skills.v1.SkillPointGained skill_points_gained = 2;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 861.

```text
ge GainSkillPointsSuccess {
  repeated .chesscom.explanation_engine.v1.Skill skills_unlocked = 1;
  repeated .chesscom.skills.v1.SkillPointGained skill_points_gained = 2;
  repeated .chesscom.explanation_engine.v1.Skill skills_mastered = 3;
  optional bool has_mastered_all = 4;
  optional bool is_first_ever_skill_point = 5;
  }
  message GainSkillPointsFailure {
  optional .chesscom.skills.v1.EligibilityError error =
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08369"></a>
## FND-08369: chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess.skills_mastered = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.explanation_engine.v1.Skill skills_mastered = 3;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 934.

```text
ill skills_unlocked = 1;
  repeated .chesscom.skills.v1.SkillPointGained skill_points_gained = 2;
  repeated .chesscom.explanation_engine.v1.Skill skills_mastered = 3;
  optional bool has_mastered_all = 4;
  optional bool is_first_ever_skill_point = 5;
  }
  message GainSkillPointsFailure {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

message GetSkillsRequest {
}

message GetSkillsResponse {
  re
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08370"></a>
## FND-08370: chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess.has_mastered_all = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool has_mastered_all = 4;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1004.

```text
ed skill_points_gained = 2;
  repeated .chesscom.explanation_engine.v1.Skill skills_mastered = 3;
  optional bool has_mastered_all = 4;
  optional bool is_first_ever_skill_point = 5;
  }
  message GainSkillPointsFailure {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

message GetSkillsRequest {
}

message GetSkillsResponse {
  repeated .chesscom.skills.v1.SkillView skill_items = 1;
  optional bool 
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08371"></a>
## FND-08371: chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsSuccess.is_first_ever_skill_point = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool is_first_ever_skill_point = 5;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1042.

```text
 .chesscom.explanation_engine.v1.Skill skills_mastered = 3;
  optional bool has_mastered_all = 4;
  optional bool is_first_ever_skill_point = 5;
  }
  message GainSkillPointsFailure {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

message GetSkillsRequest {
}

message GetSkillsResponse {
  repeated .chesscom.skills.v1.SkillView skill_items = 1;
  optional bool has_mastered_all = 2;
}

message GetSk
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08372"></a>
## FND-08372: message declaration: chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsFailure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GainSkillPointsFailure {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1093.

```text
red = 3;
  optional bool has_mastered_all = 4;
  optional bool is_first_ever_skill_point = 5;
  }
  message GainSkillPointsFailure {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

message GetSkillsRequest {
}

message GetSkillsResponse {
  repeated .chesscom.skills.v1.SkillView skill_items = 1;
  optional bool has_mastered_all = 2;
}

message GetSkillsPositionsRequest {
  optional string game_id = 
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08373"></a>
## FND-08373: chesscom.skills.v1.GainSkillPointsResponse.GainSkillPointsFailure.error = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.skills.v1.EligibilityError error = 1;

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1128.

```text
ed_all = 4;
  optional bool is_first_ever_skill_point = 5;
  }
  message GainSkillPointsFailure {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

message GetSkillsRequest {
}

message GetSkillsResponse {
  repeated .chesscom.skills.v1.SkillView skill_items = 1;
  optional bool has_mastered_all = 2;
}

message GetSkillsPositionsRequest {
  optional string game_id = 1;
  repeated .chesscom.explanation
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08374"></a>
## FND-08374: message declaration: chesscom.skills.v1.GetSkillsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSkillsRequest {

### Evidence

- **SRC-0558** `research/proto/chesscom/skills/v1/skills_service.proto` — [preserved redacted evidence](../evidence/text/8f3787dc5f658ad646dc2917032899baa26560210ea301b9a4250f2eba1e7233.proto)
  Character offset 1192.

```text
 message GainSkillPointsFailure {
  optional .chesscom.skills.v1.EligibilityError error = 1;
  }
}

message GetSkillsRequest {
}

message GetSkillsResponse {
  repeated .chesscom.skills.v1.SkillView skill_items = 1;
  optional bool has_mastered_all = 2;
}

message GetSkillsPositionsRequest {
  optional string game_id = 1;
  repeated .chesscom.explanation_engine.v1.SkillsPosition skill_positions = 2;
}

message GetSki
```

**Source references:** SRC-0558, SRC-1529  
**URL references:** None independently associated  
**Related findings:** FND-08353, FND-08354, FND-08355

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
