# data_models — findings 7801–7900

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-08075"></a>
## FND-08075: chesscom.shared_board.v1alpha.SharedBoardClockType.SHARED_BOARD_CLOCK_TYPE_SESSION_TIME = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CLOCK_TYPE_SESSION_TIME = 2;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 242.

```text
lockType {
  SHARED_BOARD_CLOCK_TYPE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_TYPE_CURRENT_TIME = 1;
  SHARED_BOARD_CLOCK_TYPE_SESSION_TIME = 2;
  SHARED_BOARD_CLOCK_TYPE_TIMER = 3;
  SHARED_BOARD_CLOCK_TYPE_STOPWATCH = 4;
}

enum SharedBoardClockState {
  SHARED_BOARD_CLOCK_STATE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_STATE_ENDED = 1;
  SHARED_BOARD_CLOCK_STATE_STARTED = 2;
  SHARED_BOARD_CLOCK_STATE_STOPPED = 3;
}

mes
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08076"></a>
## FND-08076: chesscom.shared_board.v1alpha.SharedBoardClockType.SHARED_BOARD_CLOCK_TYPE_TIMER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CLOCK_TYPE_TIMER = 3;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 286.

```text
FIED = 0;
  SHARED_BOARD_CLOCK_TYPE_CURRENT_TIME = 1;
  SHARED_BOARD_CLOCK_TYPE_SESSION_TIME = 2;
  SHARED_BOARD_CLOCK_TYPE_TIMER = 3;
  SHARED_BOARD_CLOCK_TYPE_STOPWATCH = 4;
}

enum SharedBoardClockState {
  SHARED_BOARD_CLOCK_STATE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_STATE_ENDED = 1;
  SHARED_BOARD_CLOCK_STATE_STARTED = 2;
  SHARED_BOARD_CLOCK_STATE_STOPPED = 3;
}

message SharedBoardClock {
  optional .chesscom
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08077"></a>
## FND-08077: chesscom.shared_board.v1alpha.SharedBoardClockType.SHARED_BOARD_CLOCK_TYPE_STOPWATCH = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CLOCK_TYPE_STOPWATCH = 4;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 323.

```text
URRENT_TIME = 1;
  SHARED_BOARD_CLOCK_TYPE_SESSION_TIME = 2;
  SHARED_BOARD_CLOCK_TYPE_TIMER = 3;
  SHARED_BOARD_CLOCK_TYPE_STOPWATCH = 4;
}

enum SharedBoardClockState {
  SHARED_BOARD_CLOCK_STATE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_STATE_ENDED = 1;
  SHARED_BOARD_CLOCK_STATE_STARTED = 2;
  SHARED_BOARD_CLOCK_STATE_STOPPED = 3;
}

message SharedBoardClock {
  optional .chesscom.shared_board.v1alpha.SharedBoardCloc
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08078"></a>
## FND-08078: enum declaration: chesscom.shared_board.v1alpha.SharedBoardClockState

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SharedBoardClockState {

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 365.

```text
_SESSION_TIME = 2;
  SHARED_BOARD_CLOCK_TYPE_TIMER = 3;
  SHARED_BOARD_CLOCK_TYPE_STOPWATCH = 4;
}

enum SharedBoardClockState {
  SHARED_BOARD_CLOCK_STATE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_STATE_ENDED = 1;
  SHARED_BOARD_CLOCK_STATE_STARTED = 2;
  SHARED_BOARD_CLOCK_STATE_STOPPED = 3;
}

message SharedBoardClock {
  optional .chesscom.shared_board.v1alpha.SharedBoardClockType type = 1;
  optional .chesscom.share
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08079"></a>
## FND-08079: chesscom.shared_board.v1alpha.SharedBoardClockState.SHARED_BOARD_CLOCK_STATE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CLOCK_STATE_UNSPECIFIED = 0;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 396.

```text
RD_CLOCK_TYPE_TIMER = 3;
  SHARED_BOARD_CLOCK_TYPE_STOPWATCH = 4;
}

enum SharedBoardClockState {
  SHARED_BOARD_CLOCK_STATE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_STATE_ENDED = 1;
  SHARED_BOARD_CLOCK_STATE_STARTED = 2;
  SHARED_BOARD_CLOCK_STATE_STOPPED = 3;
}

message SharedBoardClock {
  optional .chesscom.shared_board.v1alpha.SharedBoardClockType type = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardCloc
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08080"></a>
## FND-08080: chesscom.shared_board.v1alpha.SharedBoardClockState.SHARED_BOARD_CLOCK_STATE_ENDED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CLOCK_STATE_ENDED = 1;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 440.

```text
K_TYPE_STOPWATCH = 4;
}

enum SharedBoardClockState {
  SHARED_BOARD_CLOCK_STATE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_STATE_ENDED = 1;
  SHARED_BOARD_CLOCK_STATE_STARTED = 2;
  SHARED_BOARD_CLOCK_STATE_STOPPED = 3;
}

message SharedBoardClock {
  optional .chesscom.shared_board.v1alpha.SharedBoardClockType type = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue timer = 2;
  optional .chesscom.share
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08081"></a>
## FND-08081: chesscom.shared_board.v1alpha.SharedBoardClockState.SHARED_BOARD_CLOCK_STATE_STARTED = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CLOCK_STATE_STARTED = 2;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 478.

```text
ardClockState {
  SHARED_BOARD_CLOCK_STATE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_STATE_ENDED = 1;
  SHARED_BOARD_CLOCK_STATE_STARTED = 2;
  SHARED_BOARD_CLOCK_STATE_STOPPED = 3;
}

message SharedBoardClock {
  optional .chesscom.shared_board.v1alpha.SharedBoardClockType type = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue timer = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue 
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08082"></a>
## FND-08082: chesscom.shared_board.v1alpha.SharedBoardClockState.SHARED_BOARD_CLOCK_STATE_STOPPED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CLOCK_STATE_STOPPED = 3;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 518.

```text
TE_UNSPECIFIED = 0;
  SHARED_BOARD_CLOCK_STATE_ENDED = 1;
  SHARED_BOARD_CLOCK_STATE_STARTED = 2;
  SHARED_BOARD_CLOCK_STATE_STOPPED = 3;
}

message SharedBoardClock {
  optional .chesscom.shared_board.v1alpha.SharedBoardClockType type = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue timer = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue stopwatch = 3;
  optional .google.protob
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08083"></a>
## FND-08083: message declaration: chesscom.shared_board.v1alpha.SharedBoardClock

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardClock {

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 559.

```text
STATE_ENDED = 1;
  SHARED_BOARD_CLOCK_STATE_STARTED = 2;
  SHARED_BOARD_CLOCK_STATE_STOPPED = 3;
}

message SharedBoardClock {
  optional .chesscom.shared_board.v1alpha.SharedBoardClockType type = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue timer = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue stopwatch = 3;
  optional .google.protobuf.Timestamp created_at = 4;
}

message S
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08084"></a>
## FND-08084: chesscom.shared_board.v1alpha.SharedBoardClock.type = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardClockType type = 1;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 588.

```text
RD_CLOCK_STATE_STARTED = 2;
  SHARED_BOARD_CLOCK_STATE_STOPPED = 3;
}

message SharedBoardClock {
  optional .chesscom.shared_board.v1alpha.SharedBoardClockType type = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue timer = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue stopwatch = 3;
  optional .google.protobuf.Timestamp created_at = 4;
}

message SharedBoardClockValue {
  opti
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08085"></a>
## FND-08085: chesscom.shared_board.v1alpha.SharedBoardClock.timer = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardClockValue timer = 2;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 661.

```text
ssage SharedBoardClock {
  optional .chesscom.shared_board.v1alpha.SharedBoardClockType type = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue timer = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue stopwatch = 3;
  optional .google.protobuf.Timestamp created_at = 4;
}

message SharedBoardClockValue {
  optional .google.protobuf.Duration duration = 1;
  optional .chesscom.shared_
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08086"></a>
## FND-08086: chesscom.shared_board.v1alpha.SharedBoardClock.stopwatch = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardClockValue stopwatch = 3;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 736.

```text
ardClockType type = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue timer = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue stopwatch = 3;
  optional .google.protobuf.Timestamp created_at = 4;
}

message SharedBoardClockValue {
  optional .google.protobuf.Duration duration = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockState state = 2;
  optional .google.protobuf.
```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08087"></a>
## FND-08087: chesscom.shared_board.v1alpha.SharedBoardClock.created_at = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp created_at = 4;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 815.

```text
ckValue timer = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockValue stopwatch = 3;
  optional .google.protobuf.Timestamp created_at = 4;
}

message SharedBoardClockValue {
  optional .google.protobuf.Duration duration = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockState state = 2;
  optional .google.protobuf.Timestamp updated_at = 3;
}

```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08088"></a>
## FND-08088: message declaration: chesscom.shared_board.v1alpha.SharedBoardClockValue

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardClockValue {

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 870.

```text
alpha.SharedBoardClockValue stopwatch = 3;
  optional .google.protobuf.Timestamp created_at = 4;
}

message SharedBoardClockValue {
  optional .google.protobuf.Duration duration = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockState state = 2;
  optional .google.protobuf.Timestamp updated_at = 3;
}

```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08089"></a>
## FND-08089: chesscom.shared_board.v1alpha.SharedBoardClockValue.duration = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Duration duration = 1;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 904.

```text
tch = 3;
  optional .google.protobuf.Timestamp created_at = 4;
}

message SharedBoardClockValue {
  optional .google.protobuf.Duration duration = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockState state = 2;
  optional .google.protobuf.Timestamp updated_at = 3;
}

```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08090"></a>
## FND-08090: chesscom.shared_board.v1alpha.SharedBoardClockValue.state = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardClockState state = 2;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 955.

```text
ted_at = 4;
}

message SharedBoardClockValue {
  optional .google.protobuf.Duration duration = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockState state = 2;
  optional .google.protobuf.Timestamp updated_at = 3;
}

```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08091"></a>
## FND-08091: chesscom.shared_board.v1alpha.SharedBoardClockValue.updated_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp updated_at = 3;

### Evidence

- **SRC-0543** `research/proto/chesscom/shared_board/v1alpha/shared_board_clock.proto` — [preserved redacted evidence](../evidence/text/fb2ebf0d0960895075a96314d888bd863ffa1ef9f0713d1ebb45dd3aadfd1606.proto)
  Character offset 1030.

```text
Duration duration = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardClockState state = 2;
  optional .google.protobuf.Timestamp updated_at = 3;
}

```

**Source references:** SRC-0543, SRC-1514  
**URL references:** None independently associated  
**Related findings:** FND-08072, FND-08073, FND-08074

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08092"></a>
## FND-08092: enum declaration: chesscom.shared_board.v1alpha.SharedBoardRole

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SharedBoardRole {

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 131.

```text
d/v1alpha/shared_board_participant.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

enum SharedBoardRole {
  SHARED_BOARD_ROLE_UNSPECIFIED = 0;
  SHARED_BOARD_ROLE_HOST = 1;
  SHARED_BOARD_ROLE_CO_HOST = 2;
  SHARED_BOARD_ROLE_VIEWER = 3;
}

enum SharedBoardParticipantStatus {
  SHARED_BOARD_PARTICIPANT_STATUS_UNSPECIFIED = 0;
  SHARED_BOARD_PARTICIPANT_STATUS_PENDING = 1;
  SHARED_BOARD_PARTICIPANT_S
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08093"></a>
## FND-08093: chesscom.shared_board.v1alpha.SharedBoardRole.SHARED_BOARD_ROLE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_ROLE_UNSPECIFIED = 0;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 156.

```text
rticipant.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

enum SharedBoardRole {
  SHARED_BOARD_ROLE_UNSPECIFIED = 0;
  SHARED_BOARD_ROLE_HOST = 1;
  SHARED_BOARD_ROLE_CO_HOST = 2;
  SHARED_BOARD_ROLE_VIEWER = 3;
}

enum SharedBoardParticipantStatus {
  SHARED_BOARD_PARTICIPANT_STATUS_UNSPECIFIED = 0;
  SHARED_BOARD_PARTICIPANT_STATUS_PENDING = 1;
  SHARED_BOARD_PARTICIPANT_STATUS_REQUESTING = 2;
  S
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08094"></a>
## FND-08094: chesscom.shared_board.v1alpha.SharedBoardRole.SHARED_BOARD_ROLE_HOST = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_ROLE_HOST = 1;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 193.

```text
ckage chesscom.shared_board.v1alpha;

enum SharedBoardRole {
  SHARED_BOARD_ROLE_UNSPECIFIED = 0;
  SHARED_BOARD_ROLE_HOST = 1;
  SHARED_BOARD_ROLE_CO_HOST = 2;
  SHARED_BOARD_ROLE_VIEWER = 3;
}

enum SharedBoardParticipantStatus {
  SHARED_BOARD_PARTICIPANT_STATUS_UNSPECIFIED = 0;
  SHARED_BOARD_PARTICIPANT_STATUS_PENDING = 1;
  SHARED_BOARD_PARTICIPANT_STATUS_REQUESTING = 2;
  SHARED_BOARD_PARTICIPANT_STATUS_ACCEPT
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08095"></a>
## FND-08095: chesscom.shared_board.v1alpha.SharedBoardRole.SHARED_BOARD_ROLE_CO_HOST = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_ROLE_CO_HOST = 2;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 223.

```text
alpha;

enum SharedBoardRole {
  SHARED_BOARD_ROLE_UNSPECIFIED = 0;
  SHARED_BOARD_ROLE_HOST = 1;
  SHARED_BOARD_ROLE_CO_HOST = 2;
  SHARED_BOARD_ROLE_VIEWER = 3;
}

enum SharedBoardParticipantStatus {
  SHARED_BOARD_PARTICIPANT_STATUS_UNSPECIFIED = 0;
  SHARED_BOARD_PARTICIPANT_STATUS_PENDING = 1;
  SHARED_BOARD_PARTICIPANT_STATUS_REQUESTING = 2;
  SHARED_BOARD_PARTICIPANT_STATUS_ACCEPTED = 3;
  SHARED_BOARD_PARTICI
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08096"></a>
## FND-08096: chesscom.shared_board.v1alpha.SharedBoardRole.SHARED_BOARD_ROLE_VIEWER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_ROLE_VIEWER = 3;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 256.

```text
SHARED_BOARD_ROLE_UNSPECIFIED = 0;
  SHARED_BOARD_ROLE_HOST = 1;
  SHARED_BOARD_ROLE_CO_HOST = 2;
  SHARED_BOARD_ROLE_VIEWER = 3;
}

enum SharedBoardParticipantStatus {
  SHARED_BOARD_PARTICIPANT_STATUS_UNSPECIFIED = 0;
  SHARED_BOARD_PARTICIPANT_STATUS_PENDING = 1;
  SHARED_BOARD_PARTICIPANT_STATUS_REQUESTING = 2;
  SHARED_BOARD_PARTICIPANT_STATUS_ACCEPTED = 3;
  SHARED_BOARD_PARTICIPANT_STATUS_DECLINED = 4;
}

enum
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08097"></a>
## FND-08097: enum declaration: chesscom.shared_board.v1alpha.SharedBoardParticipantStatus

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SharedBoardParticipantStatus {

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 289.

```text
;
  SHARED_BOARD_ROLE_HOST = 1;
  SHARED_BOARD_ROLE_CO_HOST = 2;
  SHARED_BOARD_ROLE_VIEWER = 3;
}

enum SharedBoardParticipantStatus {
  SHARED_BOARD_PARTICIPANT_STATUS_UNSPECIFIED = 0;
  SHARED_BOARD_PARTICIPANT_STATUS_PENDING = 1;
  SHARED_BOARD_PARTICIPANT_STATUS_REQUESTING = 2;
  SHARED_BOARD_PARTICIPANT_STATUS_ACCEPTED = 3;
  SHARED_BOARD_PARTICIPANT_STATUS_DECLINED = 4;
}

enum SharedBoardCapability {
  SHARED
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08098"></a>
## FND-08098: chesscom.shared_board.v1alpha.SharedBoardParticipantStatus.SHARED_BOARD_PARTICIPANT_STATUS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_PARTICIPANT_STATUS_UNSPECIFIED = 0;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 327.

```text
ED_BOARD_ROLE_CO_HOST = 2;
  SHARED_BOARD_ROLE_VIEWER = 3;
}

enum SharedBoardParticipantStatus {
  SHARED_BOARD_PARTICIPANT_STATUS_UNSPECIFIED = 0;
  SHARED_BOARD_PARTICIPANT_STATUS_PENDING = 1;
  SHARED_BOARD_PARTICIPANT_STATUS_REQUESTING = 2;
  SHARED_BOARD_PARTICIPANT_STATUS_ACCEPTED = 3;
  SHARED_BOARD_PARTICIPANT_STATUS_DECLINED = 4;
}

enum SharedBoardCapability {
  SHARED_BOARD_CAPABILITY_UNSPECIFIED = 0;
  S
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08099"></a>
## FND-08099: chesscom.shared_board.v1alpha.SharedBoardParticipantStatus.SHARED_BOARD_PARTICIPANT_STATUS_PENDING = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_PARTICIPANT_STATUS_PENDING = 1;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 378.

```text
ER = 3;
}

enum SharedBoardParticipantStatus {
  SHARED_BOARD_PARTICIPANT_STATUS_UNSPECIFIED = 0;
  SHARED_BOARD_PARTICIPANT_STATUS_PENDING = 1;
  SHARED_BOARD_PARTICIPANT_STATUS_REQUESTING = 2;
  SHARED_BOARD_PARTICIPANT_STATUS_ACCEPTED = 3;
  SHARED_BOARD_PARTICIPANT_STATUS_DECLINED = 4;
}

enum SharedBoardCapability {
  SHARED_BOARD_CAPABILITY_UNSPECIFIED = 0;
  SHARED_BOARD_CAPABILITY_MOVE_WHITE = 1;
  SHARED_BOA
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08100"></a>
## FND-08100: chesscom.shared_board.v1alpha.SharedBoardParticipantStatus.SHARED_BOARD_PARTICIPANT_STATUS_REQUESTING = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_PARTICIPANT_STATUS_REQUESTING = 2;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 425.

```text
  SHARED_BOARD_PARTICIPANT_STATUS_UNSPECIFIED = 0;
  SHARED_BOARD_PARTICIPANT_STATUS_PENDING = 1;
  SHARED_BOARD_PARTICIPANT_STATUS_REQUESTING = 2;
  SHARED_BOARD_PARTICIPANT_STATUS_ACCEPTED = 3;
  SHARED_BOARD_PARTICIPANT_STATUS_DECLINED = 4;
}

enum SharedBoardCapability {
  SHARED_BOARD_CAPABILITY_UNSPECIFIED = 0;
  SHARED_BOARD_CAPABILITY_MOVE_WHITE = 1;
  SHARED_BOARD_CAPABILITY_MOVE_BLACK = 2;
  SHARED_BOARD_CA
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08101"></a>
## FND-08101: chesscom.shared_board.v1alpha.SharedBoardParticipantStatus.SHARED_BOARD_PARTICIPANT_STATUS_ACCEPTED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_PARTICIPANT_STATUS_ACCEPTED = 3;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 475.

```text

  SHARED_BOARD_PARTICIPANT_STATUS_PENDING = 1;
  SHARED_BOARD_PARTICIPANT_STATUS_REQUESTING = 2;
  SHARED_BOARD_PARTICIPANT_STATUS_ACCEPTED = 3;
  SHARED_BOARD_PARTICIPANT_STATUS_DECLINED = 4;
}

enum SharedBoardCapability {
  SHARED_BOARD_CAPABILITY_UNSPECIFIED = 0;
  SHARED_BOARD_CAPABILITY_MOVE_WHITE = 1;
  SHARED_BOARD_CAPABILITY_MOVE_BLACK = 2;
  SHARED_BOARD_CAPABILITY_DRAW_ARROWS = 3;
  SHARED_BOARD_CAPABILIT
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08102"></a>
## FND-08102: chesscom.shared_board.v1alpha.SharedBoardParticipantStatus.SHARED_BOARD_PARTICIPANT_STATUS_DECLINED = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_PARTICIPANT_STATUS_DECLINED = 4;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 523.

```text
  SHARED_BOARD_PARTICIPANT_STATUS_REQUESTING = 2;
  SHARED_BOARD_PARTICIPANT_STATUS_ACCEPTED = 3;
  SHARED_BOARD_PARTICIPANT_STATUS_DECLINED = 4;
}

enum SharedBoardCapability {
  SHARED_BOARD_CAPABILITY_UNSPECIFIED = 0;
  SHARED_BOARD_CAPABILITY_MOVE_WHITE = 1;
  SHARED_BOARD_CAPABILITY_MOVE_BLACK = 2;
  SHARED_BOARD_CAPABILITY_DRAW_ARROWS = 3;
  SHARED_BOARD_CAPABILITY_EDIT_COLLECTION = 4;
}

message SharedBoardPar
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08103"></a>
## FND-08103: enum declaration: chesscom.shared_board.v1alpha.SharedBoardCapability

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SharedBoardCapability {

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 572.

```text

  SHARED_BOARD_PARTICIPANT_STATUS_ACCEPTED = 3;
  SHARED_BOARD_PARTICIPANT_STATUS_DECLINED = 4;
}

enum SharedBoardCapability {
  SHARED_BOARD_CAPABILITY_UNSPECIFIED = 0;
  SHARED_BOARD_CAPABILITY_MOVE_WHITE = 1;
  SHARED_BOARD_CAPABILITY_MOVE_BLACK = 2;
  SHARED_BOARD_CAPABILITY_DRAW_ARROWS = 3;
  SHARED_BOARD_CAPABILITY_EDIT_COLLECTION = 4;
}

message SharedBoardParticipant {
  oneof _username {
  string username 
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08104"></a>
## FND-08104: chesscom.shared_board.v1alpha.SharedBoardCapability.SHARED_BOARD_CAPABILITY_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CAPABILITY_UNSPECIFIED = 0;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 603.

```text
TUS_ACCEPTED = 3;
  SHARED_BOARD_PARTICIPANT_STATUS_DECLINED = 4;
}

enum SharedBoardCapability {
  SHARED_BOARD_CAPABILITY_UNSPECIFIED = 0;
  SHARED_BOARD_CAPABILITY_MOVE_WHITE = 1;
  SHARED_BOARD_CAPABILITY_MOVE_BLACK = 2;
  SHARED_BOARD_CAPABILITY_DRAW_ARROWS = 3;
  SHARED_BOARD_CAPABILITY_EDIT_COLLECTION = 4;
}

message SharedBoardParticipant {
  oneof _username {
  string username = 8;
  }
  oneof _avatar_url {

```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08105"></a>
## FND-08105: chesscom.shared_board.v1alpha.SharedBoardCapability.SHARED_BOARD_CAPABILITY_MOVE_WHITE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CAPABILITY_MOVE_WHITE = 1;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 646.

```text
T_STATUS_DECLINED = 4;
}

enum SharedBoardCapability {
  SHARED_BOARD_CAPABILITY_UNSPECIFIED = 0;
  SHARED_BOARD_CAPABILITY_MOVE_WHITE = 1;
  SHARED_BOARD_CAPABILITY_MOVE_BLACK = 2;
  SHARED_BOARD_CAPABILITY_DRAW_ARROWS = 3;
  SHARED_BOARD_CAPABILITY_EDIT_COLLECTION = 4;
}

message SharedBoardParticipant {
  oneof _username {
  string username = 8;
  }
  oneof _avatar_url {
  string avatar_url = 9;
  }
  oneof _chess
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08106"></a>
## FND-08106: chesscom.shared_board.v1alpha.SharedBoardCapability.SHARED_BOARD_CAPABILITY_MOVE_BLACK = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CAPABILITY_MOVE_BLACK = 2;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 688.

```text
Capability {
  SHARED_BOARD_CAPABILITY_UNSPECIFIED = 0;
  SHARED_BOARD_CAPABILITY_MOVE_WHITE = 1;
  SHARED_BOARD_CAPABILITY_MOVE_BLACK = 2;
  SHARED_BOARD_CAPABILITY_DRAW_ARROWS = 3;
  SHARED_BOARD_CAPABILITY_EDIT_COLLECTION = 4;
}

message SharedBoardParticipant {
  oneof _username {
  string username = 8;
  }
  oneof _avatar_url {
  string avatar_url = 9;
  }
  oneof _chess_title {
  string chess_title = 10;
  }
  
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08107"></a>
## FND-08107: chesscom.shared_board.v1alpha.SharedBoardCapability.SHARED_BOARD_CAPABILITY_DRAW_ARROWS = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CAPABILITY_DRAW_ARROWS = 3;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 730.

```text
PECIFIED = 0;
  SHARED_BOARD_CAPABILITY_MOVE_WHITE = 1;
  SHARED_BOARD_CAPABILITY_MOVE_BLACK = 2;
  SHARED_BOARD_CAPABILITY_DRAW_ARROWS = 3;
  SHARED_BOARD_CAPABILITY_EDIT_COLLECTION = 4;
}

message SharedBoardParticipant {
  oneof _username {
  string username = 8;
  }
  oneof _avatar_url {
  string avatar_url = 9;
  }
  oneof _chess_title {
  string chess_title = 10;
  }
  oneof _country {
  string country = 11;
  
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08108"></a>
## FND-08108: chesscom.shared_board.v1alpha.SharedBoardCapability.SHARED_BOARD_CAPABILITY_EDIT_COLLECTION = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SHARED_BOARD_CAPABILITY_EDIT_COLLECTION = 4;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 773.

```text
E_WHITE = 1;
  SHARED_BOARD_CAPABILITY_MOVE_BLACK = 2;
  SHARED_BOARD_CAPABILITY_DRAW_ARROWS = 3;
  SHARED_BOARD_CAPABILITY_EDIT_COLLECTION = 4;
}

message SharedBoardParticipant {
  oneof _username {
  string username = 8;
  }
  oneof _avatar_url {
  string avatar_url = 9;
  }
  oneof _chess_title {
  string chess_title = 10;
  }
  oneof _country {
  string country = 11;
  }
  oneof _flair_code {
  string flair_code
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08109"></a>
## FND-08109: message declaration: chesscom.shared_board.v1alpha.SharedBoardParticipant

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardParticipant {

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 821.

```text
K = 2;
  SHARED_BOARD_CAPABILITY_DRAW_ARROWS = 3;
  SHARED_BOARD_CAPABILITY_EDIT_COLLECTION = 4;
}

message SharedBoardParticipant {
  oneof _username {
  string username = 8;
  }
  oneof _avatar_url {
  string avatar_url = 9;
  }
  oneof _chess_title {
  string chess_title = 10;
  }
  oneof _country {
  string country = 11;
  }
  oneof _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_stre
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08110"></a>
## FND-08110: oneof declaration: chesscom.shared_board.v1alpha.SharedBoardParticipant._username

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _username {

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 856.

```text
AW_ARROWS = 3;
  SHARED_BOARD_CAPABILITY_EDIT_COLLECTION = 4;
}

message SharedBoardParticipant {
  oneof _username {
  string username = 8;
  }
  oneof _avatar_url {
  string avatar_url = 9;
  }
  oneof _chess_title {
  string chess_title = 10;
  }
  oneof _country {
  string country = 11;
  }
  oneof _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08111"></a>
## FND-08111: chesscom.shared_board.v1alpha.SharedBoardParticipant.username = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string username = 8;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 876.

```text
RED_BOARD_CAPABILITY_EDIT_COLLECTION = 4;
}

message SharedBoardParticipant {
  oneof _username {
  string username = 8;
  }
  oneof _avatar_url {
  string avatar_url = 9;
  }
  oneof _chess_title {
  string chess_title = 10;
  }
  oneof _country {
  string country = 11;
  }
  oneof _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.Fl
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08112"></a>
## FND-08112: oneof declaration: chesscom.shared_board.v1alpha.SharedBoardParticipant._avatar_url

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _avatar_url {

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 903.

```text
OLLECTION = 4;
}

message SharedBoardParticipant {
  oneof _username {
  string username = 8;
  }
  oneof _avatar_url {
  string avatar_url = 9;
  }
  oneof _chess_title {
  string chess_title = 10;
  }
  oneof _country {
  string country = 11;
  }
  oneof _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  o
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08113"></a>
## FND-08113: chesscom.shared_board.v1alpha.SharedBoardParticipant.avatar_url = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string avatar_url = 9;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 925.

```text
age SharedBoardParticipant {
  oneof _username {
  string username = 8;
  }
  oneof _avatar_url {
  string avatar_url = 9;
  }
  oneof _chess_title {
  string chess_title = 10;
  }
  oneof _country {
  string country = 11;
  }
  oneof _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  s
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08114"></a>
## FND-08114: oneof declaration: chesscom.shared_board.v1alpha.SharedBoardParticipant._chess_title

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _chess_title {

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 954.

```text
  oneof _username {
  string username = 8;
  }
  oneof _avatar_url {
  string avatar_url = 9;
  }
  oneof _chess_title {
  string chess_title = 10;
  }
  oneof _country {
  string country = 11;
  }
  oneof _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08115"></a>
## FND-08115: chesscom.shared_board.v1alpha.SharedBoardParticipant.chess_title = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string chess_title = 10;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 977.

```text
tring username = 8;
  }
  oneof _avatar_url {
  string avatar_url = 9;
  }
  oneof _chess_title {
  string chess_title = 10;
  }
  oneof _country {
  string country = 11;
  }
  oneof _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  optional string user_id
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08116"></a>
## FND-08116: oneof declaration: chesscom.shared_board.v1alpha.SharedBoardParticipant._country

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _country {

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1008.

```text
 _avatar_url {
  string avatar_url = 9;
  }
  oneof _chess_title {
  string chess_title = 10;
  }
  oneof _country {
  string country = 11;
  }
  oneof _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  optional string user_id = 1;
  optional .chesscom.shar
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08117"></a>
## FND-08117: chesscom.shared_board.v1alpha.SharedBoardParticipant.country = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string country = 11;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1027.

```text
ring avatar_url = 9;
  }
  oneof _chess_title {
  string chess_title = 10;
  }
  oneof _country {
  string country = 11;
  }
  oneof _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  optional string user_id = 1;
  optional .chesscom.shared_board.v1alpha.Sh
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08118"></a>
## FND-08118: oneof declaration: chesscom.shared_board.v1alpha.SharedBoardParticipant._flair_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _flair_code {

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1054.

```text
oneof _chess_title {
  string chess_title = 10;
  }
  oneof _country {
  string country = 11;
  }
  oneof _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  optional string user_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 2;
  o
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08119"></a>
## FND-08119: chesscom.shared_board.v1alpha.SharedBoardParticipant.flair_code = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string flair_code = 12;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1076.

```text
 string chess_title = 10;
  }
  oneof _country {
  string country = 11;
  }
  oneof _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  optional string user_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 2;
  optional .chesscom.shar
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08120"></a>
## FND-08120: oneof declaration: chesscom.shared_board.v1alpha.SharedBoardParticipant._is_streamer

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _is_streamer {

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1106.

```text
  oneof _country {
  string country = 11;
  }
  oneof _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  optional string user_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardPa
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08121"></a>
## FND-08121: chesscom.shared_board.v1alpha.SharedBoardParticipant.is_streamer = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

bool is_streamer = 13;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1129.

```text
ring country = 11;
  }
  oneof _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  optional string user_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus status 
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08122"></a>
## FND-08122: oneof declaration: chesscom.shared_board.v1alpha.SharedBoardParticipant._flair

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _flair {

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1158.

```text
f _flair_code {
  string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  optional string user_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus status = 3;
  repeated .chesscom.sha
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08123"></a>
## FND-08123: chesscom.shared_board.v1alpha.SharedBoardParticipant.flair = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.flair.v1.FlairView flair = 14;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1175.

```text
 string flair_code = 12;
  }
  oneof _is_streamer {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  optional string user_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus status = 3;
  repeated .chesscom.shared_board.v1alpha
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08124"></a>
## FND-08124: oneof declaration: chesscom.shared_board.v1alpha.SharedBoardParticipant._membership

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _membership {

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1222.

```text
er {
  bool is_streamer = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  optional string user_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus status = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
  opti
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08125"></a>
## FND-08125: chesscom.shared_board.v1alpha.SharedBoardParticipant.membership = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string membership = 15;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1244.

```text
r = 13;
  }
  oneof _flair {
  .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  optional string user_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus status = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
  optional string invited_by
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08126"></a>
## FND-08126: chesscom.shared_board.v1alpha.SharedBoardParticipant.user_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_id = 1;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1274.

```text
 .chesscom.flair.v1.FlairView flair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  optional string user_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus status = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
  optional string invited_by_id = 5;
  optional .google.pr
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08127"></a>
## FND-08127: chesscom.shared_board.v1alpha.SharedBoardParticipant.role = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 2;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1305.

```text
lair = 14;
  }
  oneof _membership {
  string membership = 15;
  }
  optional string user_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus status = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
  optional string invited_by_id = 5;
  optional .google.protobuf.Timestamp created_at = 6
```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08128"></a>
## FND-08128: chesscom.shared_board.v1alpha.SharedBoardParticipant.status = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus status = 3;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1373.

```text
 optional string user_id = 1;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus status = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
  optional string invited_by_id = 5;
  optional .google.protobuf.Timestamp created_at = 6;
  optional .google.protobuf.Timestamp updated_at = 7;
}

```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08129"></a>
## FND-08129: chesscom.shared_board.v1alpha.SharedBoardParticipant.capabilities = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1456.

```text
Role role = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipantStatus status = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
  optional string invited_by_id = 5;
  optional .google.protobuf.Timestamp created_at = 6;
  optional .google.protobuf.Timestamp updated_at = 7;
}

```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08130"></a>
## FND-08130: chesscom.shared_board.v1alpha.SharedBoardParticipant.invited_by_id = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string invited_by_id = 5;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1538.

```text
tus status = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
  optional string invited_by_id = 5;
  optional .google.protobuf.Timestamp created_at = 6;
  optional .google.protobuf.Timestamp updated_at = 7;
}

```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08131"></a>
## FND-08131: chesscom.shared_board.v1alpha.SharedBoardParticipant.created_at = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp created_at = 6;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1575.

```text
shared_board.v1alpha.SharedBoardCapability capabilities = 4;
  optional string invited_by_id = 5;
  optional .google.protobuf.Timestamp created_at = 6;
  optional .google.protobuf.Timestamp updated_at = 7;
}

```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08132"></a>
## FND-08132: chesscom.shared_board.v1alpha.SharedBoardParticipant.updated_at = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp updated_at = 7;

### Evidence

- **SRC-0544** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant.proto` — [preserved redacted evidence](../evidence/text/c7e9887a504e39f7a25a313a527999e56d1acbebe1ad151b806a8c61c72f580e.proto)
  Character offset 1629.

```text
s = 4;
  optional string invited_by_id = 5;
  optional .google.protobuf.Timestamp created_at = 6;
  optional .google.protobuf.Timestamp updated_at = 7;
}

```

**Source references:** SRC-0544, SRC-1515  
**URL references:** None independently associated  
**Related findings:** FND-08092, FND-08093, FND-08094

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08133"></a>
## FND-08133: message declaration: chesscom.shared_board.v1alpha.InviteSharedBoardParticipantRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InviteSharedBoardParticipantRequest {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 139.

```text
a/shared_board_participant_service.proto
// syntax: proto3

package chesscom.shared_board.v1alpha;

message InviteSharedBoardParticipantRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
}

message InviteSharedBoardParticipantResponse {
  optiona
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08134"></a>
## FND-08134: chesscom.shared_board.v1alpha.InviteSharedBoardParticipantRequest.session_id = 1

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
**Related findings:** FND-08133, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08135"></a>
## FND-08135: chesscom.shared_board.v1alpha.InviteSharedBoardParticipantRequest.user_id = 2

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
**Related findings:** FND-08133, FND-08134

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08136"></a>
## FND-08136: chesscom.shared_board.v1alpha.InviteSharedBoardParticipantRequest.role = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 252.

```text
eSharedBoardParticipantRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
}

message InviteSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RequestToJoinSharedBoardSessi
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08137"></a>
## FND-08137: chesscom.shared_board.v1alpha.InviteSharedBoardParticipantRequest.capabilities = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 320.

```text
 optional string user_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
}

message InviteSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RequestToJoinSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSes
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08138"></a>
## FND-08138: message declaration: chesscom.shared_board.v1alpha.InviteSharedBoardParticipantResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InviteSharedBoardParticipantResponse {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 403.

```text
Role role = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
}

message InviteSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RequestToJoinSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message RequestToJoinSharedBoardSessionResponse {
  optio
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08139"></a>
## FND-08139: chesscom.shared_board.v1alpha.InviteSharedBoardParticipantResponse.participant = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 452.

```text
v1alpha.SharedBoardCapability capabilities = 4;
}

message InviteSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RequestToJoinSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message RequestToJoinSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardPar
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08140"></a>
## FND-08140: message declaration: chesscom.shared_board.v1alpha.RequestToJoinSharedBoardSessionRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RequestToJoinSharedBoardSessionRequest {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 535.

```text
pantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RequestToJoinSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message RequestToJoinSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
  optional string session_id = 2;
}

message RespondToSha
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08141"></a>
## FND-08141: chesscom.shared_board.v1alpha.RequestToJoinSharedBoardSessionRequest.session_id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 586.

```text
alpha.SharedBoardParticipant participant = 1;
}

message RequestToJoinSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message RequestToJoinSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
  optional string session_id = 2;
}

message RespondToSharedBoardInvitationRequest {
  optional string sessi
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08142"></a>
## FND-08142: message declaration: chesscom.shared_board.v1alpha.RequestToJoinSharedBoardSessionResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RequestToJoinSharedBoardSessionResponse {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 666.

```text
dSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message RequestToJoinSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
  optional string session_id = 2;
}

message RespondToSharedBoardInvitationRequest {
  optional string session_id = 1;
  optional bool accept = 2;
}

message RespondToSharedBoardInvitation
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08143"></a>
## FND-08143: chesscom.shared_board.v1alpha.RequestToJoinSharedBoardSessionResponse.participant = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 452.

```text
v1alpha.SharedBoardCapability capabilities = 4;
}

message InviteSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RequestToJoinSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message RequestToJoinSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardPar
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08144"></a>
## FND-08144: chesscom.shared_board.v1alpha.RequestToJoinSharedBoardSessionResponse.session_id = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string session_id = 2;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 800.

```text
ssionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
  optional string session_id = 2;
}

message RespondToSharedBoardInvitationRequest {
  optional string session_id = 1;
  optional bool accept = 2;
}

message RespondToSharedBoardInvitationResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RespondToSharedBoardJoinReques
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08145"></a>
## FND-08145: message declaration: chesscom.shared_board.v1alpha.RespondToSharedBoardInvitationRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RespondToSharedBoardInvitationRequest {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 835.

```text
m.shared_board.v1alpha.SharedBoardParticipant participant = 1;
  optional string session_id = 2;
}

message RespondToSharedBoardInvitationRequest {
  optional string session_id = 1;
  optional bool accept = 2;
}

message RespondToSharedBoardInvitationResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RespondToSharedBoardJoinRequestRequest {
  optional string sessio
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08146"></a>
## FND-08146: chesscom.shared_board.v1alpha.RespondToSharedBoardInvitationRequest.session_id = 1

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

<a id="FND-08147"></a>
## FND-08147: chesscom.shared_board.v1alpha.RespondToSharedBoardInvitationRequest.accept = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool accept = 2;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 919.

```text
sion_id = 2;
}

message RespondToSharedBoardInvitationRequest {
  optional string session_id = 1;
  optional bool accept = 2;
}

message RespondToSharedBoardInvitationResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RespondToSharedBoardJoinRequestRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  optional bool accept = 3;
}

message Resp
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08148"></a>
## FND-08148: message declaration: chesscom.shared_board.v1alpha.RespondToSharedBoardInvitationResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RespondToSharedBoardInvitationResponse {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 948.

```text
ndToSharedBoardInvitationRequest {
  optional string session_id = 1;
  optional bool accept = 2;
}

message RespondToSharedBoardInvitationResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RespondToSharedBoardJoinRequestRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  optional bool accept = 3;
}

message RespondToSharedBoardJoinRequestRe
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08149"></a>
## FND-08149: chesscom.shared_board.v1alpha.RespondToSharedBoardInvitationResponse.participant = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 452.

```text
v1alpha.SharedBoardCapability capabilities = 4;
}

message InviteSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RequestToJoinSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message RequestToJoinSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardPar
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08150"></a>
## FND-08150: message declaration: chesscom.shared_board.v1alpha.RespondToSharedBoardJoinRequestRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RespondToSharedBoardJoinRequestRequest {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 1082.

```text
tionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RespondToSharedBoardJoinRequestRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  optional bool accept = 3;
}

message RespondToSharedBoardJoinRequestResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message UpdateSharedBoardParticipantRole
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08151"></a>
## FND-08151: chesscom.shared_board.v1alpha.RespondToSharedBoardJoinRequestRequest.session_id = 1

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

<a id="FND-08152"></a>
## FND-08152: chesscom.shared_board.v1alpha.RespondToSharedBoardJoinRequestRequest.user_id = 2

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

<a id="FND-08153"></a>
## FND-08153: chesscom.shared_board.v1alpha.RespondToSharedBoardJoinRequestRequest.accept = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool accept = 3;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 1198.

```text
oSharedBoardJoinRequestRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  optional bool accept = 3;
}

message RespondToSharedBoardJoinRequestResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message UpdateSharedBoardParticipantRoleRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  optional .chesscom.shared_board.v1alpha
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08154"></a>
## FND-08154: message declaration: chesscom.shared_board.v1alpha.RespondToSharedBoardJoinRequestResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RespondToSharedBoardJoinRequestResponse {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 1227.

```text
t {
  optional string session_id = 1;
  optional string user_id = 2;
  optional bool accept = 3;
}

message RespondToSharedBoardJoinRequestResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message UpdateSharedBoardParticipantRoleRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
}

```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08155"></a>
## FND-08155: chesscom.shared_board.v1alpha.RespondToSharedBoardJoinRequestResponse.participant = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 452.

```text
v1alpha.SharedBoardCapability capabilities = 4;
}

message InviteSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RequestToJoinSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message RequestToJoinSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardPar
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08156"></a>
## FND-08156: message declaration: chesscom.shared_board.v1alpha.UpdateSharedBoardParticipantRoleRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UpdateSharedBoardParticipantRoleRequest {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 1362.

```text
uestResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message UpdateSharedBoardParticipantRoleRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
}

message UpdateSharedBoardParticipantRoleResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08157"></a>
## FND-08157: chesscom.shared_board.v1alpha.UpdateSharedBoardParticipantRoleRequest.session_id = 1

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

<a id="FND-08158"></a>
## FND-08158: chesscom.shared_board.v1alpha.UpdateSharedBoardParticipantRoleRequest.user_id = 2

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

<a id="FND-08159"></a>
## FND-08159: chesscom.shared_board.v1alpha.UpdateSharedBoardParticipantRoleRequest.role = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 252.

```text
eSharedBoardParticipantRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 4;
}

message InviteSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RequestToJoinSharedBoardSessi
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08160"></a>
## FND-08160: message declaration: chesscom.shared_board.v1alpha.UpdateSharedBoardParticipantRoleResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UpdateSharedBoardParticipantRoleResponse {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 1548.

```text
optional string user_id = 2;
  optional .chesscom.shared_board.v1alpha.SharedBoardRole role = 3;
}

message UpdateSharedBoardParticipantRoleResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message SetSharedBoardParticipantCapabilitiesRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability 
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08161"></a>
## FND-08161: chesscom.shared_board.v1alpha.UpdateSharedBoardParticipantRoleResponse.participant = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 452.

```text
v1alpha.SharedBoardCapability capabilities = 4;
}

message InviteSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RequestToJoinSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message RequestToJoinSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardPar
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08162"></a>
## FND-08162: message declaration: chesscom.shared_board.v1alpha.SetSharedBoardParticipantCapabilitiesRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetSharedBoardParticipantCapabilitiesRequest {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 1684.

```text
RoleResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message SetSharedBoardParticipantCapabilitiesRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 3;
}

message SetSharedBoardParticipantCapabilitiesResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardPartic
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08163"></a>
## FND-08163: chesscom.shared_board.v1alpha.SetSharedBoardParticipantCapabilitiesRequest.session_id = 1

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

<a id="FND-08164"></a>
## FND-08164: chesscom.shared_board.v1alpha.SetSharedBoardParticipantCapabilitiesRequest.user_id = 2

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

<a id="FND-08165"></a>
## FND-08165: chesscom.shared_board.v1alpha.SetSharedBoardParticipantCapabilitiesRequest.capabilities = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 3;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 1806.

```text
ParticipantCapabilitiesRequest {
  optional string session_id = 1;
  optional string user_id = 2;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 3;
}

message SetSharedBoardParticipantCapabilitiesResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message TransferSharedBoardHostRequest {
  optional string session_id = 1;
  optional string use
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08166"></a>
## FND-08166: message declaration: chesscom.shared_board.v1alpha.SetSharedBoardParticipantCapabilitiesResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SetSharedBoardParticipantCapabilitiesResponse {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 1889.

```text
g user_id = 2;
  repeated .chesscom.shared_board.v1alpha.SharedBoardCapability capabilities = 3;
}

message SetSharedBoardParticipantCapabilitiesResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message TransferSharedBoardHostRequest {
  optional string session_id = 1;
  optional string user_id = 2;
}

message TransferSharedBoardHostResponse {
  optional .chesscom.shared_
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08167"></a>
## FND-08167: chesscom.shared_board.v1alpha.SetSharedBoardParticipantCapabilitiesResponse.participant = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 452.

```text
v1alpha.SharedBoardCapability capabilities = 4;
}

message InviteSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message RequestToJoinSharedBoardSessionRequest {
  optional .chesscom.shared_board.v1alpha.SharedBoardSessionId session_id = 1;
}

message RequestToJoinSharedBoardSessionResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardPar
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-08168"></a>
## FND-08168: message declaration: chesscom.shared_board.v1alpha.TransferSharedBoardHostRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TransferSharedBoardHostRequest {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 2030.

```text
tiesResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardParticipant participant = 1;
}

message TransferSharedBoardHostRequest {
  optional string session_id = 1;
  optional string user_id = 2;
}

message TransferSharedBoardHostResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message RemoveSharedBoardParticipantRequest {
  optional string session_id = 1;
  optional s
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08169"></a>
## FND-08169: chesscom.shared_board.v1alpha.TransferSharedBoardHostRequest.session_id = 1

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

<a id="FND-08170"></a>
## FND-08170: chesscom.shared_board.v1alpha.TransferSharedBoardHostRequest.user_id = 2

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

<a id="FND-08171"></a>
## FND-08171: message declaration: chesscom.shared_board.v1alpha.TransferSharedBoardHostResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TransferSharedBoardHostResponse {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 2139.

```text
ransferSharedBoardHostRequest {
  optional string session_id = 1;
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
  optional .chesscom.shared_board.v1alph
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08172"></a>
## FND-08172: chesscom.shared_board.v1alpha.TransferSharedBoardHostResponse.session = 1

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

<a id="FND-08173"></a>
## FND-08173: message declaration: chesscom.shared_board.v1alpha.RemoveSharedBoardParticipantRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RemoveSharedBoardParticipantRequest {

### Evidence

- **SRC-0545** `research/proto/chesscom/shared_board/v1alpha/shared_board_participant_service.proto` — [preserved redacted evidence](../evidence/text/f2d7d9c657e1a9e6e8836beb7be915c014dd376946ff6a639cad649fdf8fe338.proto)
  Character offset 2258.

```text
redBoardHostResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message RemoveSharedBoardParticipantRequest {
  optional string session_id = 1;
  optional string user_id = 2;
}

message RemoveSharedBoardParticipantResponse {
  optional .chesscom.shared_board.v1alpha.SharedBoardSession session = 1;
}

message LeaveSharedBoardSessionRequest {
  optional string session_id = 1;
}

mess
```

**Source references:** SRC-0545, SRC-1516  
**URL references:** None independently associated  
**Related findings:** FND-08133, FND-08134, FND-08135

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-08174"></a>
## FND-08174: chesscom.shared_board.v1alpha.RemoveSharedBoardParticipantRequest.session_id = 1

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
