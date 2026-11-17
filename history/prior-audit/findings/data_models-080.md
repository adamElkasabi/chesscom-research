# data_models — findings 7901–8000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-08175"></a>
## FND-08175: chesscom.shared_board.v1alpha.RemoveSharedBoardParticipantRequest.user_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_id = 2;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 221.

```text
d_board.v1alpha;

message InviteSharedBoardParticipantRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
}

message InviteSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

messag
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08176"></a>
## FND-08176: message declaration: chesscom.shared_board.v1alpha.RemoveSharedBoardParticipantResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RemoveSharedBoardParticipantResponse {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 2372.

```text
SharedBoardParticipantRequest {
  optional string session_id = 1;
  optional string user_id = 2;
}

message RemoveSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message LeaveSharedBoardSessionRequest {
  optional string session_id = 1;
}

message LeaveSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08177"></a>
## FND-08177: chesscom.shared_board.v1alpha.RemoveSharedBoardParticipantResponse.session = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 2183.

```text
tring session_id = 1;
  optional string user_id = 2;
}

message TransferSharedBoardHostResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message RemoveSharedBoardParticipantRequest {
  optional string session_id = 1;
  optional string user_id = 2;
}

message RemoveSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08178"></a>
## FND-08178: message declaration: chesscom.shared_board.v1alpha.LeaveSharedBoardSessionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LeaveSharedBoardSessionRequest {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 2496.

```text
dParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message LeaveSharedBoardSessionRequest {
  optional string session_id = 1;
}

message LeaveSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08179"></a>
## FND-08179: chesscom.shared_board.v1alpha.LeaveSharedBoardSessionRequest.session_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string session_id = 1;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 187.

```text
ax: proto3

package chesscom.shared_board.v1alpha;

message InviteSharedBoardParticipantRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
}

message InviteSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardPart
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08180"></a>
## FND-08180: message declaration: chesscom.shared_board.v1alpha.LeaveSharedBoardSessionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message LeaveSharedBoardSessionResponse {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 2574.

```text
ssion session = 1;
}

message LeaveSharedBoardSessionRequest {
  optional string session_id = 1;
}

message LeaveSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08181"></a>
## FND-08181: chesscom.shared_board.v1alpha.LeaveSharedBoardSessionResponse.session = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 2183.

```text
tring session_id = 1;
  optional string user_id = 2;
}

message TransferSharedBoardHostResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message RemoveSharedBoardParticipantRequest {
  optional string session_id = 1;
  optional string user_id = 2;
}

message RemoveSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08182"></a>
## FND-08182: message declaration: chesscom.shared_board.v1alpha.SharedBoardParticipantUpdatedNotification

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardParticipantUpdatedNotification {

### Evidence

- **SRC-0546** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_updated_notification.proto` — [preserved redacted evidence](../evidence/text/ec9392f568315e09f3c2e163b51d4bb6851dc74a34adab07d8f2f48c00b84b32.proto)
  Character offset 152.

```text
d_participant_updated_notification.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

message SharedBoardParticipantUpdatedNotification {
  optional string session_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 2;
  optional bool removed = 3;
  optional string author_id = 4;
}

```

**Source references:** SRC-0546, SRC-1517  
**URL references:** None independently associated  
**Related findings:** FND-08183, FND-08184

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08183"></a>
## FND-08183: chesscom.shared_board.v1alpha.SharedBoardParticipantUpdatedNotification.session_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string session_id = 1;

### Evidence

- **SRC-0546** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_updated_notification.proto` — [preserved redacted evidence](../evidence/text/ec9392f568315e09f3c2e163b51d4bb6851dc74a34adab07d8f2f48c00b84b32.proto)
  Character offset 206.

```text
oto3

package chesscom.shared_board.v1alpha;

message SharedBoardParticipantUpdatedNotification {
  optional string session_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 2;
  optional bool removed = 3;
  optional string author_id = 4;
}

```

**Source references:** SRC-0546, SRC-1517  
**URL references:** None independently associated  
**Related findings:** FND-08182, FND-08184

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08184"></a>
## FND-08184: chesscom.shared_board.v1alpha.SharedBoardParticipantUpdatedNotification.participant = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 2;

### Evidence

- **SRC-0546** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_updated_notification.proto` — [preserved redacted evidence](../evidence/text/ec9392f568315e09f3c2e163b51d4bb6851dc74a34adab07d8f2f48c00b84b32.proto)
  Character offset 240.

```text
d.v1alpha;

message SharedBoardParticipantUpdatedNotification {
  optional string session_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 2;
  optional bool removed = 3;
  optional string author_id = 4;
}

```

**Source references:** SRC-0546, SRC-1517  
**URL references:** None independently associated  
**Related findings:** FND-08182, FND-08183

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08185"></a>
## FND-08185: chesscom.shared_board.v1alpha.SharedBoardParticipantUpdatedNotification.removed = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool removed = 3;

### Evidence

- **SRC-0546** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_updated_notification.proto` — [preserved redacted evidence](../evidence/text/ec9392f568315e09f3c2e163b51d4bb6851dc74a34adab07d8f2f48c00b84b32.proto)
  Character offset 322.

```text
session_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 2;
  optional bool removed = 3;
  optional string author_id = 4;
}

```

**Source references:** SRC-0546, SRC-1517  
**URL references:** None independently associated  
**Related findings:** FND-08182, FND-08183, FND-08184

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08186"></a>
## FND-08186: chesscom.shared_board.v1alpha.SharedBoardParticipantUpdatedNotification.author_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string author_id = 4;

### Evidence

- **SRC-0546** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_updated_notification.proto` — [preserved redacted evidence](../evidence/text/ec9392f568315e09f3c2e163b51d4bb6851dc74a34adab07d8f2f48c00b84b32.proto)
  Character offset 351.

```text
hesscom.shared_board.v1alpha.SharedBoardParticipant participant = 2;
  optional bool removed = 3;
  optional string author_id = 4;
}

```

**Source references:** SRC-0546, SRC-1517  
**URL references:** None independently associated  
**Related findings:** FND-08182, FND-08183, FND-08184

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08187"></a>
## FND-08187: message declaration: chesscom.shared_board.v1alpha.CreateSharedBoardSessionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CreateSharedBoardSessionRequest {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 127.

```text
board/v1alpha/shared_board_service.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

message CreateSharedBoardSessionRequest {
  repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 1;
  optional bool open_enrollment = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBo
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08188"></a>
## FND-08188: chesscom.shared_board.v1alpha.CreateSharedBoardSessionRequest.boards = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 171.

```text
syntax: proto3

package chesscom.shared_board.v1alpha;

message CreateSharedBoardSessionRequest {
  repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 1;
  optional bool open_enrollment = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetShared
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08189"></a>
## FND-08189: chesscom.shared_board.v1alpha.CreateSharedBoardSessionRequest.open_enrollment = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool open_enrollment = 2;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 237.

```text
eateSharedBoardSessionRequest {
  repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 1;
  optional bool open_enrollment = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.Sh
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08190"></a>
## FND-08190: chesscom.shared_board.v1alpha.CreateSharedBoardSessionRequest.source = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 3;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 274.

```text
eated .chesscom.shared_board.v1alpha.SharedBoard boards = 1;
  optional bool open_enrollment = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08191"></a>
## FND-08191: message declaration: chesscom.shared_board.v1alpha.CreateSharedBoardSessionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CreateSharedBoardSessionResponse {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 354.

```text
n_enrollment = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message GetSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alp
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08192"></a>
## FND-08192: chesscom.shared_board.v1alpha.CreateSharedBoardSessionResponse.session = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 399.

```text
_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message GetSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08193"></a>
## FND-08193: message declaration: chesscom.shared_board.v1alpha.GetSharedBoardSessionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSharedBoardSessionRequest {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 474.

```text
BoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message GetSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message FindSharedBoardSessionByResourceRequest {
  optional .chesscom.shared_boar
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08194"></a>
## FND-08194: chesscom.shared_board.v1alpha.GetSharedBoardSessionRequest.session_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 515.

```text
om.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message GetSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message FindSharedBoardSessionByResourceRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource reso
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08195"></a>
## FND-08195: message declaration: chesscom.shared_board.v1alpha.GetSharedBoardSessionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetSharedBoardSessionResponse {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 595.

```text
dSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message GetSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message FindSharedBoardSessionByResourceRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;
}

message FindSharedBoardSessionByResourceResponse {
  optional .ches
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08196"></a>
## FND-08196: chesscom.shared_board.v1alpha.GetSharedBoardSessionResponse.session = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 399.

```text
_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message GetSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08197"></a>
## FND-08197: message declaration: chesscom.shared_board.v1alpha.FindSharedBoardSessionByResourceRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FindSharedBoardSessionByResourceRequest {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 712.

```text
BoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message FindSharedBoardSessionByResourceRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;
}

message FindSharedBoardSessionByResourceResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message CreateSharedBoardSessionForResourceRequest {
  o
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08198"></a>
## FND-08198: chesscom.shared_board.v1alpha.FindSharedBoardSessionByResourceRequest.resource = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 764.

```text
oard.v1alpha.SharedBoardSession session = 1;
}

message FindSharedBoardSessionByResourceRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;
}

message FindSharedBoardSessionByResourceResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message CreateSharedBoardSessionForResourceRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSe
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08199"></a>
## FND-08199: message declaration: chesscom.shared_board.v1alpha.FindSharedBoardSessionByResourceResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FindSharedBoardSessionByResourceResponse {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 848.

```text
urceRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;
}

message FindSharedBoardSessionByResourceResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message CreateSharedBoardSessionForResourceRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;
  repeated .chesscom.shared_board.v1alpha.SharedBoard bo
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08200"></a>
## FND-08200: chesscom.shared_board.v1alpha.FindSharedBoardSessionByResourceResponse.session = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 399.

```text
_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message GetSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08201"></a>
## FND-08201: message declaration: chesscom.shared_board.v1alpha.CreateSharedBoardSessionForResourceRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CreateSharedBoardSessionForResourceRequest {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 976.

```text
onByResourceResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message CreateSharedBoardSessionForResourceRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;
  repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 2;
  optional bool open_enrollment = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 4;
}

```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08202"></a>
## FND-08202: chesscom.shared_board.v1alpha.CreateSharedBoardSessionForResourceRequest.resource = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 764.

```text
oard.v1alpha.SharedBoardSession session = 1;
}

message FindSharedBoardSessionByResourceRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;
}

message FindSharedBoardSessionByResourceResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message CreateSharedBoardSessionForResourceRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSe
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08203"></a>
## FND-08203: chesscom.shared_board.v1alpha.CreateSharedBoardSessionForResourceRequest.boards = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 2;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1114.

```text
ourceRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;
  repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 2;
  optional bool open_enrollment = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 4;
}

message CreateSharedBoardSessionForResourceResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

messag
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08204"></a>
## FND-08204: chesscom.shared_board.v1alpha.CreateSharedBoardSessionForResourceRequest.open_enrollment = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool open_enrollment = 3;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1180.

```text
rdSessionResource resource = 1;
  repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 2;
  optional bool open_enrollment = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 4;
}

message CreateSharedBoardSessionForResourceResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message SyncCollectionRosterRequest {
  optional .chesscom.shared_board.
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08205"></a>
## FND-08205: chesscom.shared_board.v1alpha.CreateSharedBoardSessionForResourceRequest.source = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 4;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1217.

```text
eated .chesscom.shared_board.v1alpha.SharedBoard boards = 2;
  optional bool open_enrollment = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 4;
}

message CreateSharedBoardSessionForResourceResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message SyncCollectionRosterRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource re
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08206"></a>
## FND-08206: message declaration: chesscom.shared_board.v1alpha.CreateSharedBoardSessionForResourceResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CreateSharedBoardSessionForResourceResponse {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1297.

```text
n_enrollment = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 4;
}

message CreateSharedBoardSessionForResourceResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message SyncCollectionRosterRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;
}

message SyncCollectionRosterResponse {
  optional .chesscom.share
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08207"></a>
## FND-08207: chesscom.shared_board.v1alpha.CreateSharedBoardSessionForResourceResponse.session = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 399.

```text
_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message GetSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08208"></a>
## FND-08208: message declaration: chesscom.shared_board.v1alpha.SyncCollectionRosterRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SyncCollectionRosterRequest {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1428.

```text
nForResourceResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message SyncCollectionRosterRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;
}

message SyncCollectionRosterResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message ListSharedBoardSessionsRequest {
  oneof _pagination {
  .chesscom.api.v
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08209"></a>
## FND-08209: chesscom.shared_board.v1alpha.SyncCollectionRosterRequest.resource = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 764.

```text
oard.v1alpha.SharedBoardSession session = 1;
}

message FindSharedBoardSessionByResourceRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;
}

message FindSharedBoardSessionByResourceResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message CreateSharedBoardSessionForResourceRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSe
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08210"></a>
## FND-08210: message declaration: chesscom.shared_board.v1alpha.SyncCollectionRosterResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SyncCollectionRosterResponse {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1552.

```text
sterRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource resource = 1;
}

message SyncCollectionRosterResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message ListSharedBoardSessionsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 1;
  opt
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08211"></a>
## FND-08211: chesscom.shared_board.v1alpha.SyncCollectionRosterResponse.session = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 399.

```text
_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message GetSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08212"></a>
## FND-08212: message declaration: chesscom.shared_board.v1alpha.ListSharedBoardSessionsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListSharedBoardSessionsRequest {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1668.

```text
ectionRosterResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message ListSharedBoardSessionsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoard
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08213"></a>
## FND-08213: oneof declaration: chesscom.shared_board.v1alpha.ListSharedBoardSessionsRequest._pagination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pagination {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1711.

```text
.shared_board.v1alpha.SharedBoardSession session = 1;
}

message ListSharedBoardSessionsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 4;
}
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08214"></a>
## FND-08214: chesscom.shared_board.v1alpha.ListSharedBoardSessionsRequest.pagination = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.RequestPagination pagination = 2;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1733.

```text
SharedBoardSession session = 1;
}

message ListSharedBoardSessionsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 4;
}

message ListSharedBo
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08215"></a>
## FND-08215: chesscom.shared_board.v1alpha.ListSharedBoardSessionsRequest.source = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1790.

```text
dSessionsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 4;
}

message ListSharedBoardSessionsResponse {
  oneof _pagination {
  .chesscom.a
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08216"></a>
## FND-08216: chesscom.shared_board.v1alpha.ListSharedBoardSessionsRequest.role = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1869.

```text
agination = 2;
  }
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 4;
}

message ListSharedBoardSessionsResponse {
  oneof _pagination {
  .chesscom.api.v1.ResponsePagination pagination = 2;
  }
  repeated .chesscom.shared_board.
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08217"></a>
## FND-08217: chesscom.shared_board.v1alpha.ListSharedBoardSessionsRequest.participant_status = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 4;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1937.

```text
oardSessionSource source = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 4;
}

message ListSharedBoardSessionsResponse {
  oneof _pagination {
  .chesscom.api.v1.ResponsePagination pagination = 2;
  }
  repeated .chesscom.shared_board.v1alpha.SharedBoardSessionSummary sessions = 1;
}

message UpdateSha
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08218"></a>
## FND-08218: message declaration: chesscom.shared_board.v1alpha.ListSharedBoardSessionsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListSharedBoardSessionsResponse {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2033.

```text
;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 4;
}

message ListSharedBoardSessionsResponse {
  oneof _pagination {
  .chesscom.api.v1.ResponsePagination pagination = 2;
  }
  repeated .chesscom.shared_board.v1alpha.SharedBoardSessionSummary sessions = 1;
}

message UpdateSharedBoardSessionRequest {
  optional string session_id = 1;
  optional string current_board_id = 
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08219"></a>
## FND-08219: oneof declaration: chesscom.shared_board.v1alpha.ListSharedBoardSessionsResponse._pagination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pagination {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1711.

```text
.shared_board.v1alpha.SharedBoardSession session = 1;
}

message ListSharedBoardSessionsRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 2;
  }
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus participant_status = 4;
}
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08220"></a>
## FND-08220: chesscom.shared_board.v1alpha.ListSharedBoardSessionsResponse.pagination = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.ResponsePagination pagination = 2;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2099.

```text
Status participant_status = 4;
}

message ListSharedBoardSessionsResponse {
  oneof _pagination {
  .chesscom.api.v1.ResponsePagination pagination = 2;
  }
  repeated .chesscom.shared_board.v1alpha.SharedBoardSessionSummary sessions = 1;
}

message UpdateSharedBoardSessionRequest {
  optional string session_id = 1;
  optional string current_board_id = 2;
  optional bool open_enrollment = 3;
}

message UpdateSharedBoa
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08221"></a>
## FND-08221: chesscom.shared_board.v1alpha.ListSharedBoardSessionsResponse.sessions = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.shared_board.v1alpha.SharedBoardSessionSummary sessions = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2157.

```text
essionsResponse {
  oneof _pagination {
  .chesscom.api.v1.ResponsePagination pagination = 2;
  }
  repeated .chesscom.shared_board.v1alpha.SharedBoardSessionSummary sessions = 1;
}

message UpdateSharedBoardSessionRequest {
  optional string session_id = 1;
  optional string current_board_id = 2;
  optional bool open_enrollment = 3;
}

message UpdateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1al
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08222"></a>
## FND-08222: message declaration: chesscom.shared_board.v1alpha.UpdateSharedBoardSessionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UpdateSharedBoardSessionRequest {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2240.

```text
ation = 2;
  }
  repeated .chesscom.shared_board.v1alpha.SharedBoardSessionSummary sessions = 1;
}

message UpdateSharedBoardSessionRequest {
  optional string session_id = 1;
  optional string current_board_id = 2;
  optional bool open_enrollment = 3;
}

message UpdateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardClockRequest {
  op
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08223"></a>
## FND-08223: chesscom.shared_board.v1alpha.UpdateSharedBoardSessionRequest.session_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string session_id = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2284.

```text
oard.v1alpha.SharedBoardSessionSummary sessions = 1;
}

message UpdateSharedBoardSessionRequest {
  optional string session_id = 1;
  optional string current_board_id = 2;
  optional bool open_enrollment = 3;
}

message UpdateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardClockRequest {
  optional string session_id = 1;
  optional .ch
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08224"></a>
## FND-08224: chesscom.shared_board.v1alpha.UpdateSharedBoardSessionRequest.current_board_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string current_board_id = 2;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2318.

```text
mary sessions = 1;
}

message UpdateSharedBoardSessionRequest {
  optional string session_id = 1;
  optional string current_board_id = 2;
  optional bool open_enrollment = 3;
}

message UpdateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardClockRequest {
  optional string session_id = 1;
  optional .chesscom.shared_board.v1alpha.Shared
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08225"></a>
## FND-08225: chesscom.shared_board.v1alpha.UpdateSharedBoardSessionRequest.open_enrollment = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool open_enrollment = 3;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 1180.

```text
rdSessionResource resource = 1;
  repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 2;
  optional bool open_enrollment = 3;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 4;
}

message CreateSharedBoardSessionForResourceResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message SyncCollectionRosterRequest {
  optional .chesscom.shared_board.
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08226"></a>
## FND-08226: message declaration: chesscom.shared_board.v1alpha.UpdateSharedBoardSessionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UpdateSharedBoardSessionResponse {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2396.

```text
ing session_id = 1;
  optional string current_board_id = 2;
  optional bool open_enrollment = 3;
}

message UpdateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardClockRequest {
  optional string session_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClock clock = 2;
}

message UpdateSharedBoardClockResponse {
  optional .
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08227"></a>
## FND-08227: chesscom.shared_board.v1alpha.UpdateSharedBoardSessionResponse.session = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 399.

```text
_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message GetSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08228"></a>
## FND-08228: message declaration: chesscom.shared_board.v1alpha.UpdateSharedBoardClockRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UpdateSharedBoardClockRequest {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2516.

```text
BoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardClockRequest {
  optional string session_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClock clock = 2;
}

message UpdateSharedBoardClockResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message CreateSharedBoardRequest {
  optional string se
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08229"></a>
## FND-08229: chesscom.shared_board.v1alpha.UpdateSharedBoardClockRequest.session_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string session_id = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2284.

```text
oard.v1alpha.SharedBoardSessionSummary sessions = 1;
}

message UpdateSharedBoardSessionRequest {
  optional string session_id = 1;
  optional string current_board_id = 2;
  optional bool open_enrollment = 3;
}

message UpdateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardClockRequest {
  optional string session_id = 1;
  optional .ch
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08230"></a>
## FND-08230: chesscom.shared_board.v1alpha.UpdateSharedBoardClockRequest.clock = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardClock clock = 2;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2592.

```text
Session session = 1;
}

message UpdateSharedBoardClockRequest {
  optional string session_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClock clock = 2;
}

message UpdateSharedBoardClockResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message CreateSharedBoardRequest {
  optional string session_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08231"></a>
## FND-08231: message declaration: chesscom.shared_board.v1alpha.UpdateSharedBoardClockResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UpdateSharedBoardClockResponse {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2663.

```text
nal string session_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClock clock = 2;
}

message UpdateSharedBoardClockResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message CreateSharedBoardRequest {
  optional string session_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 2;
}

message CreateSharedBoardResponse {
  optional .chesscom.shared_b
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08232"></a>
## FND-08232: chesscom.shared_board.v1alpha.UpdateSharedBoardClockResponse.session = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 399.

```text
_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message GetSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08233"></a>
## FND-08233: message declaration: chesscom.shared_board.v1alpha.CreateSharedBoardRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CreateSharedBoardRequest {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2781.

```text
edBoardClockResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message CreateSharedBoardRequest {
  optional string session_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 2;
}

message CreateSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message DeleteSharedBoardRequest {
  optional string session_id = 1;
  optional
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08234"></a>
## FND-08234: chesscom.shared_board.v1alpha.CreateSharedBoardRequest.session_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string session_id = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2284.

```text
oard.v1alpha.SharedBoardSessionSummary sessions = 1;
}

message UpdateSharedBoardSessionRequest {
  optional string session_id = 1;
  optional string current_board_id = 2;
  optional bool open_enrollment = 3;
}

message UpdateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardClockRequest {
  optional string session_id = 1;
  optional .ch
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08235"></a>
## FND-08235: chesscom.shared_board.v1alpha.CreateSharedBoardRequest.board = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoard board = 2;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2852.

```text
BoardSession session = 1;
}

message CreateSharedBoardRequest {
  optional string session_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 2;
}

message CreateSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message DeleteSharedBoardRequest {
  optional string session_id = 1;
  optional string board_id = 2;
}

message DeleteSharedBoardResponse {
  optional
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08236"></a>
## FND-08236: message declaration: chesscom.shared_board.v1alpha.CreateSharedBoardResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CreateSharedBoardResponse {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2918.

```text
optional string session_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 2;
}

message CreateSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message DeleteSharedBoardRequest {
  optional string session_id = 1;
  optional string board_id = 2;
}

message DeleteSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08237"></a>
## FND-08237: chesscom.shared_board.v1alpha.CreateSharedBoardResponse.board = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2956.

```text
onal .chesscom.shared_board.v1alpha.SharedBoard board = 2;
}

message CreateSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message DeleteSharedBoardRequest {
  optional string session_id = 1;
  optional string board_id = 2;
}

message DeleteSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardRequest {
  
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08238"></a>
## FND-08238: message declaration: chesscom.shared_board.v1alpha.DeleteSharedBoardRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DeleteSharedBoardRequest {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 3022.

```text
age CreateSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message DeleteSharedBoardRequest {
  optional string session_id = 1;
  optional string board_id = 2;
}

message DeleteSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}


```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08239"></a>
## FND-08239: chesscom.shared_board.v1alpha.DeleteSharedBoardRequest.session_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string session_id = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2284.

```text
oard.v1alpha.SharedBoardSessionSummary sessions = 1;
}

message UpdateSharedBoardSessionRequest {
  optional string session_id = 1;
  optional string current_board_id = 2;
  optional bool open_enrollment = 3;
}

message UpdateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardClockRequest {
  optional string session_id = 1;
  optional .ch
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08240"></a>
## FND-08240: chesscom.shared_board.v1alpha.DeleteSharedBoardRequest.board_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string board_id = 2;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 3093.

```text
ha.SharedBoard board = 1;
}

message DeleteSharedBoardRequest {
  optional string session_id = 1;
  optional string board_id = 2;
}

message DeleteSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message UpdateSharedBoardResponse {
  optional .chesscom.shared_board.v
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08241"></a>
## FND-08241: message declaration: chesscom.shared_board.v1alpha.DeleteSharedBoardResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DeleteSharedBoardResponse {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 3126.

```text
age DeleteSharedBoardRequest {
  optional string session_id = 1;
  optional string board_id = 2;
}

message DeleteSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message UpdateSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}


```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08242"></a>
## FND-08242: chesscom.shared_board.v1alpha.DeleteSharedBoardResponse.session = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 399.

```text
_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message GetSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08243"></a>
## FND-08243: message declaration: chesscom.shared_board.v1alpha.UpdateSharedBoardRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UpdateSharedBoardRequest {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 3239.

```text
eSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message UpdateSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message EndSharedBoardSessionRequest {
  optional string session_id = 1;
}

message EndSharedBoardSessionResponse
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08244"></a>
## FND-08244: chesscom.shared_board.v1alpha.UpdateSharedBoardRequest.board = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2956.

```text
onal .chesscom.shared_board.v1alpha.SharedBoard board = 2;
}

message CreateSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message DeleteSharedBoardRequest {
  optional string session_id = 1;
  optional string board_id = 2;
}

message DeleteSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardRequest {
  
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08245"></a>
## FND-08245: message declaration: chesscom.shared_board.v1alpha.UpdateSharedBoardResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UpdateSharedBoardResponse {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 3342.

```text
sage UpdateSharedBoardRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message UpdateSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message EndSharedBoardSessionRequest {
  optional string session_id = 1;
}

message EndSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08246"></a>
## FND-08246: chesscom.shared_board.v1alpha.UpdateSharedBoardResponse.board = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2956.

```text
onal .chesscom.shared_board.v1alpha.SharedBoard board = 2;
}

message CreateSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message DeleteSharedBoardRequest {
  optional string session_id = 1;
  optional string board_id = 2;
}

message DeleteSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardRequest {
  
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08247"></a>
## FND-08247: message declaration: chesscom.shared_board.v1alpha.EndSharedBoardSessionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EndSharedBoardSessionRequest {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 3446.

```text
age UpdateSharedBoardResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoard board = 1;
}

message EndSharedBoardSessionRequest {
  optional string session_id = 1;
}

message EndSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08248"></a>
## FND-08248: chesscom.shared_board.v1alpha.EndSharedBoardSessionRequest.session_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string session_id = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 2284.

```text
oard.v1alpha.SharedBoardSessionSummary sessions = 1;
}

message UpdateSharedBoardSessionRequest {
  optional string session_id = 1;
  optional string current_board_id = 2;
  optional bool open_enrollment = 3;
}

message UpdateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message UpdateSharedBoardClockRequest {
  optional string session_id = 1;
  optional .ch
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08249"></a>
## FND-08249: message declaration: chesscom.shared_board.v1alpha.EndSharedBoardSessionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message EndSharedBoardSessionResponse {

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 3522.

```text
aredBoard board = 1;
}

message EndSharedBoardSessionRequest {
  optional string session_id = 1;
}

message EndSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08250"></a>
## FND-08250: chesscom.shared_board.v1alpha.EndSharedBoardSessionResponse.session = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;

### Evidence

- **SRC-0547** `research/proto/chesscom/shared_board/v1alpha/shared_board_service.proto` — [preserved redacted evidence](../evidence/text/799d3ac858f79565feb6b6023ea166856eec81ec5df6a5120e244bae67eb7fcb.proto)
  Character offset 399.

```text
_board.v1alpha.SharedBoardSessionSource source = 3;
}

message CreateSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message GetSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message GetSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message
```

**Source references:** SRC-0547, SRC-1518  
**URL references:** None independently associated  
**Related findings:** FND-08187, FND-08188, FND-08189

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08251"></a>
## FND-08251: enum declaration: chesscom.shared_board.v1alpha.SharedBoardSessionStatus

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SharedBoardSessionStatus {

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 127.

```text
board/v1alpha/shared_board_session.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

enum SharedBoardSessionStatus {
  SHARED_BOARD_SESSION_STATUS_UNSPECIFIED = 0;
  SHARED_BOARD_SESSION_STATUS_ACTIVE = 1;
  SHARED_BOARD_SESSION_STATUS_ENDED = 2;
}

enum SharedBoardSessionSource {
  SHARED_BOARD_SESSION_SOURCE_UNSPECIFIED = 0;
  SHARED_BOARD_SESSION_SOURCE_ANALYSIS = 1;
  SHARED_BOARD_SESSION_SOURCE_EV
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08252, FND-08253

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08252"></a>
## FND-08252: chesscom.shared_board.v1alpha.SharedBoardSessionStatus.SHARED_BOARD_SESSION_STATUS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_SESSION_STATUS_UNSPECIFIED = 0;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 161.

```text
.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

enum SharedBoardSessionStatus {
  SHARED_BOARD_SESSION_STATUS_UNSPECIFIED = 0;
  SHARED_BOARD_SESSION_STATUS_ACTIVE = 1;
  SHARED_BOARD_SESSION_STATUS_ENDED = 2;
}

enum SharedBoardSessionSource {
  SHARED_BOARD_SESSION_SOURCE_UNSPECIFIED = 0;
  SHARED_BOARD_SESSION_SOURCE_ANALYSIS = 1;
  SHARED_BOARD_SESSION_SOURCE_EVENTS = 2;
}

message SharedBoardSe
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08253

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08253"></a>
## FND-08253: chesscom.shared_board.v1alpha.SharedBoardSessionStatus.SHARED_BOARD_SESSION_STATUS_ACTIVE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_SESSION_STATUS_ACTIVE = 1;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 208.

```text
ed_board.v1alpha;

enum SharedBoardSessionStatus {
  SHARED_BOARD_SESSION_STATUS_UNSPECIFIED = 0;
  SHARED_BOARD_SESSION_STATUS_ACTIVE = 1;
  SHARED_BOARD_SESSION_STATUS_ENDED = 2;
}

enum SharedBoardSessionSource {
  SHARED_BOARD_SESSION_SOURCE_UNSPECIFIED = 0;
  SHARED_BOARD_SESSION_SOURCE_ANALYSIS = 1;
  SHARED_BOARD_SESSION_SOURCE_EVENTS = 2;
}

message SharedBoardSessionId {
  oneof id {
  string session_id = 1;
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08254"></a>
## FND-08254: chesscom.shared_board.v1alpha.SharedBoardSessionStatus.SHARED_BOARD_SESSION_STATUS_ENDED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_SESSION_STATUS_ENDED = 2;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 250.

```text
Status {
  SHARED_BOARD_SESSION_STATUS_UNSPECIFIED = 0;
  SHARED_BOARD_SESSION_STATUS_ACTIVE = 1;
  SHARED_BOARD_SESSION_STATUS_ENDED = 2;
}

enum SharedBoardSessionSource {
  SHARED_BOARD_SESSION_SOURCE_UNSPECIFIED = 0;
  SHARED_BOARD_SESSION_SOURCE_ANALYSIS = 1;
  SHARED_BOARD_SESSION_SOURCE_EVENTS = 2;
}

message SharedBoardSessionId {
  oneof id {
  string session_id = 1;
  string slug = 2;
  }
}

message SharedB
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08255"></a>
## FND-08255: enum declaration: chesscom.shared_board.v1alpha.SharedBoardSessionSource

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SharedBoardSessionSource {

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 292.

```text
PECIFIED = 0;
  SHARED_BOARD_SESSION_STATUS_ACTIVE = 1;
  SHARED_BOARD_SESSION_STATUS_ENDED = 2;
}

enum SharedBoardSessionSource {
  SHARED_BOARD_SESSION_SOURCE_UNSPECIFIED = 0;
  SHARED_BOARD_SESSION_SOURCE_ANALYSIS = 1;
  SHARED_BOARD_SESSION_SOURCE_EVENTS = 2;
}

message SharedBoardSessionId {
  oneof id {
  string session_id = 1;
  string slug = 2;
  }
}

message SharedBoardSession {
  optional string id = 1;
  
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08256"></a>
## FND-08256: chesscom.shared_board.v1alpha.SharedBoardSessionSource.SHARED_BOARD_SESSION_SOURCE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_SESSION_SOURCE_UNSPECIFIED = 0;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 326.

```text
ON_STATUS_ACTIVE = 1;
  SHARED_BOARD_SESSION_STATUS_ENDED = 2;
}

enum SharedBoardSessionSource {
  SHARED_BOARD_SESSION_SOURCE_UNSPECIFIED = 0;
  SHARED_BOARD_SESSION_SOURCE_ANALYSIS = 1;
  SHARED_BOARD_SESSION_SOURCE_EVENTS = 2;
}

message SharedBoardSessionId {
  oneof id {
  string session_id = 1;
  string slug = 2;
  }
}

message SharedBoardSession {
  optional string id = 1;
  optional string current_board_id =
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08257"></a>
## FND-08257: chesscom.shared_board.v1alpha.SharedBoardSessionSource.SHARED_BOARD_SESSION_SOURCE_ANALYSIS = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_SESSION_SOURCE_ANALYSIS = 1;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 373.

```text
ATUS_ENDED = 2;
}

enum SharedBoardSessionSource {
  SHARED_BOARD_SESSION_SOURCE_UNSPECIFIED = 0;
  SHARED_BOARD_SESSION_SOURCE_ANALYSIS = 1;
  SHARED_BOARD_SESSION_SOURCE_EVENTS = 2;
}

message SharedBoardSessionId {
  oneof id {
  string session_id = 1;
  string slug = 2;
  }
}

message SharedBoardSession {
  optional string id = 1;
  optional string current_board_id = 2;
  repeated .chesscom.shared_board.v1alpha.S
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08258"></a>
## FND-08258: chesscom.shared_board.v1alpha.SharedBoardSessionSource.SHARED_BOARD_SESSION_SOURCE_EVENTS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_SESSION_SOURCE_EVENTS = 2;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 417.

```text
urce {
  SHARED_BOARD_SESSION_SOURCE_UNSPECIFIED = 0;
  SHARED_BOARD_SESSION_SOURCE_ANALYSIS = 1;
  SHARED_BOARD_SESSION_SOURCE_EVENTS = 2;
}

message SharedBoardSessionId {
  oneof id {
  string session_id = 1;
  string slug = 2;
  }
}

message SharedBoardSession {
  optional string id = 1;
  optional string current_board_id = 2;
  repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 3;
  optional .google.pr
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08259"></a>
## FND-08259: message declaration: chesscom.shared_board.v1alpha.SharedBoardSessionId

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardSessionId {

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 460.

```text
IFIED = 0;
  SHARED_BOARD_SESSION_SOURCE_ANALYSIS = 1;
  SHARED_BOARD_SESSION_SOURCE_EVENTS = 2;
}

message SharedBoardSessionId {
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
  optional
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08260"></a>
## FND-08260: oneof declaration: chesscom.shared_board.v1alpha.SharedBoardSessionId.id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof id {

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 493.

```text
_SOURCE_ANALYSIS = 1;
  SHARED_BOARD_SESSION_SOURCE_EVENTS = 2;
}

message SharedBoardSessionId {
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
  repeated .che
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08261"></a>
## FND-08261: chesscom.shared_board.v1alpha.SharedBoardSessionId.session_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string session_id = 1;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 506.

```text
SIS = 1;
  SHARED_BOARD_SESSION_SOURCE_EVENTS = 2;
}

message SharedBoardSessionId {
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
  repeated .chesscom.shared_
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08262"></a>
## FND-08262: chesscom.shared_board.v1alpha.SharedBoardSessionId.slug = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string slug = 2;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 531.

```text
ESSION_SOURCE_EVENTS = 2;
}

message SharedBoardSessionId {
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
  repeated .chesscom.shared_board.v1alpha.SharedBoard
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08263"></a>
## FND-08263: message declaration: chesscom.shared_board.v1alpha.SharedBoardSession

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardSession {

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 555.

```text
;
}

message SharedBoardSessionId {
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
  repeated .chesscom.shared_board.v1alpha.SharedBoardParticipant participants
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08264"></a>
## FND-08264: chesscom.shared_board.v1alpha.SharedBoardSession.id = 1

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

<a id="FND-08265"></a>
## FND-08265: chesscom.shared_board.v1alpha.SharedBoardSession.current_board_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string current_board_id = 2;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 612.

```text
 session_id = 1;
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
  optional bool open_enrollment = 7;
  optional .ch
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08266"></a>
## FND-08266: chesscom.shared_board.v1alpha.SharedBoardSession.boards = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 3;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 652.

```text
}

message SharedBoardSession {
  optional string id = 1;
  optional string current_board_id = 2;
  repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional string slug = 5;
  repeated .chesscom.shared_board.v1alpha.SharedBoardParticipant participants = 6;
  optional bool open_enrollment = 7;
  optional .chesscom.shared_board.v1alpha.SharedBoardS
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08267"></a>
## FND-08267: chesscom.shared_board.v1alpha.SharedBoardSession.created_at = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp created_at = 4;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 718.

```text
al string current_board_id = 2;
  repeated .chesscom.shared_board.v1alpha.SharedBoard boards = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional string slug = 5;
  repeated .chesscom.shared_board.v1alpha.SharedBoardParticipant participants = 6;
  optional bool open_enrollment = 7;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 8;
  optional .chesscom.shared_board.v1alpha
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08268"></a>
## FND-08268: chesscom.shared_board.v1alpha.SharedBoardSession.slug = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string slug = 5;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 772.

```text
hared_board.v1alpha.SharedBoard boards = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional string slug = 5;
  repeated .chesscom.shared_board.v1alpha.SharedBoardParticipant participants = 6;
  optional bool open_enrollment = 7;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 8;
  optional .chesscom.shared_board.v1alpha.SharedBoardClock clock = 9;
  optional .chesscom.shar
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08269"></a>
## FND-08269: chesscom.shared_board.v1alpha.SharedBoardSession.participants = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.shared_board.v1alpha.SharedBoardParticipant participants = 6;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 800.

```text
ard boards = 3;
  optional .google.protobuf.Timestamp created_at = 4;
  optional string slug = 5;
  repeated .chesscom.shared_board.v1alpha.SharedBoardParticipant participants = 6;
  optional bool open_enrollment = 7;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 8;
  optional .chesscom.shared_board.v1alpha.SharedBoardClock clock = 9;
  optional .chesscom.shared_board.v1alpha.SharedBoard
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08270"></a>
## FND-08270: chesscom.shared_board.v1alpha.SharedBoardSession.open_enrollment = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool open_enrollment = 7;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 883.

```text
ring slug = 5;
  repeated .chesscom.shared_board.v1alpha.SharedBoardParticipant participants = 6;
  optional bool open_enrollment = 7;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 8;
  optional .chesscom.shared_board.v1alpha.SharedBoardClock clock = 9;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 10;
  optional .chesscom.shared_board.v1alpha.SharedBoardSes
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08271"></a>
## FND-08271: chesscom.shared_board.v1alpha.SharedBoardSession.status = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 8;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 920.

```text
hared_board.v1alpha.SharedBoardParticipant participants = 6;
  optional bool open_enrollment = 7;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 8;
  optional .chesscom.shared_board.v1alpha.SharedBoardClock clock = 9;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 10;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource linked_resource = 11;
}

```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08272"></a>
## FND-08272: chesscom.shared_board.v1alpha.SharedBoardSession.clock = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardClock clock = 9;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 999.

```text
en_enrollment = 7;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionStatus status = 8;
  optional .chesscom.shared_board.v1alpha.SharedBoardClock clock = 9;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 10;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource linked_resource = 11;
}

message SharedBoardSessionSummary {
  optional string id = 1;
  optional strin
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08273"></a>
## FND-08273: chesscom.shared_board.v1alpha.SharedBoardSession.source = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 10;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 1069.

```text
rdSessionStatus status = 8;
  optional .chesscom.shared_board.v1alpha.SharedBoardClock clock = 9;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 10;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource linked_resource = 11;
}

message SharedBoardSessionSummary {
  optional string id = 1;
  optional string slug = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessi
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08274"></a>
## FND-08274: chesscom.shared_board.v1alpha.SharedBoardSession.linked_resource = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource linked_resource = 11;

### Evidence

- **SRC-0548** `research/proto/chesscom/shared_board/v1alpha/shared_board_session.proto` — [preserved redacted evidence](../evidence/text/a9d327c9f3818796b082566db53e42fa9cd4f5b0b1f6c2cedd37d6acf23e5b4d.proto)
  Character offset 1149.

```text
dClock clock = 9;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 10;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionResource linked_resource = 11;
}

message SharedBoardSessionSummary {
  optional string id = 1;
  optional string slug = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionSource source = 3;
  optional bool open_enrollment = 4;
  optional .chesscom.s
```

**Source references:** SRC-0548, SRC-1519  
**URL references:** None independently associated  
**Related findings:** FND-08251, FND-08252, FND-08253

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.
