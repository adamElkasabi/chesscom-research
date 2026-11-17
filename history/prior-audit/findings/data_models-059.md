# data_models — findings 5801–5900

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-06075"></a>
## FND-06075: chesscom.i18n.v1.SyncFailure.error_message = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string error_message = 3;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 3052.

```text
  optional string file_path = 1;
  optional .chesscom.i18n.v1.FailedSyncErrorCode error_code = 2;
  optional string error_message = 3;
  repeated string keys = 4;
}

message SyncWarning {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.SyncWarningKind kind = 2;
  optional string message = 3;
  repeated string keys = 4;
}

```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06076"></a>
## FND-06076: chesscom.i18n.v1.SyncFailure.keys = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string keys = 4;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 3089.

```text
tional .chesscom.i18n.v1.FailedSyncErrorCode error_code = 2;
  optional string error_message = 3;
  repeated string keys = 4;
}

message SyncWarning {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.SyncWarningKind kind = 2;
  optional string message = 3;
  repeated string keys = 4;
}

```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06077"></a>
## FND-06077: message declaration: chesscom.i18n.v1.SyncWarning

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SyncWarning {

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 3118.

```text
edSyncErrorCode error_code = 2;
  optional string error_message = 3;
  repeated string keys = 4;
}

message SyncWarning {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.SyncWarningKind kind = 2;
  optional string message = 3;
  repeated string keys = 4;
}

```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06078"></a>
## FND-06078: chesscom.i18n.v1.SyncWarning.file_path = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string file_path = 1;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 2954.

```text
leData {
  optional string file_id = 1;
  optional string new_value = 2;
}

message SyncFailure {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.FailedSyncErrorCode error_code = 2;
  optional string error_message = 3;
  repeated string keys = 4;
}

message SyncWarning {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.SyncWarningKind kind = 2;
  optional string message = 3;
  repeated stri
```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06079"></a>
## FND-06079: chesscom.i18n.v1.SyncWarning.kind = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.i18n.v1.SyncWarningKind kind = 2;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 3175.

```text
essage = 3;
  repeated string keys = 4;
}

message SyncWarning {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.SyncWarningKind kind = 2;
  optional string message = 3;
  repeated string keys = 4;
}

```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06080"></a>
## FND-06080: chesscom.i18n.v1.SyncWarning.message = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string message = 3;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 3230.

```text
Warning {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.SyncWarningKind kind = 2;
  optional string message = 3;
  repeated string keys = 4;
}

```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06081"></a>
## FND-06081: chesscom.i18n.v1.SyncWarning.keys = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string keys = 4;

### Evidence

- **SRC-0474** `research/proto/chesscom/i18n/v1/translation.proto` — [preserved redacted evidence](../evidence/text/944964cd958c7529476df3c68055f034618148a4c38f4004dac1a26efc889ba7.proto)
  Character offset 3089.

```text
tional .chesscom.i18n.v1.FailedSyncErrorCode error_code = 2;
  optional string error_message = 3;
  repeated string keys = 4;
}

message SyncWarning {
  optional string file_path = 1;
  optional .chesscom.i18n.v1.SyncWarningKind kind = 2;
  optional string message = 3;
  repeated string keys = 4;
}

```

**Source references:** SRC-0474, SRC-1445  
**URL references:** None independently associated  
**Related findings:** FND-05996, FND-05997, FND-05998

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06082"></a>
## FND-06082: enum declaration: chesscom.inbox.v1.BatchMessageContext

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum BatchMessageContext {

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 100.

```text
// source: chesscom/inbox/v1/user_message_core.proto
// syntax: proto3

package chesscom.inbox.v1;

enum BatchMessageContext {
  BATCH_MESSAGE_CONTEXT_UNSPECIFIED = 0;
  BATCH_MESSAGE_CONTEXT_SHARE = 1;
}

enum MessageSendNotAllowedReason {
  MESSAGE_SEND_NOT_ALLOWED_REASON_UNSPECIFIED = 0;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_FRIENDS_ONLY = 1;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_NOBODY = 2;
  MESSAGE_SEND
```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06083, FND-06084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06083"></a>
## FND-06083: chesscom.inbox.v1.BatchMessageContext.BATCH_MESSAGE_CONTEXT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BATCH_MESSAGE_CONTEXT_UNSPECIFIED = 0;

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 129.

```text
user_message_core.proto
// syntax: proto3

package chesscom.inbox.v1;

enum BatchMessageContext {
  BATCH_MESSAGE_CONTEXT_UNSPECIFIED = 0;
  BATCH_MESSAGE_CONTEXT_SHARE = 1;
}

enum MessageSendNotAllowedReason {
  MESSAGE_SEND_NOT_ALLOWED_REASON_UNSPECIFIED = 0;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_FRIENDS_ONLY = 1;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_NOBODY = 2;
  MESSAGE_SEND_NOT_ALLOWED_REASON_BLOCKED =
```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06082, FND-06084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06084"></a>
## FND-06084: chesscom.inbox.v1.BatchMessageContext.BATCH_MESSAGE_CONTEXT_SHARE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

BATCH_MESSAGE_CONTEXT_SHARE = 1;

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 170.

```text


package chesscom.inbox.v1;

enum BatchMessageContext {
  BATCH_MESSAGE_CONTEXT_UNSPECIFIED = 0;
  BATCH_MESSAGE_CONTEXT_SHARE = 1;
}

enum MessageSendNotAllowedReason {
  MESSAGE_SEND_NOT_ALLOWED_REASON_UNSPECIFIED = 0;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_FRIENDS_ONLY = 1;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_NOBODY = 2;
  MESSAGE_SEND_NOT_ALLOWED_REASON_BLOCKED = 3;
  MESSAGE_SEND_NOT_ALLOWED_REASON_TRU
```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06082, FND-06083

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06085"></a>
## FND-06085: enum declaration: chesscom.inbox.v1.MessageSendNotAllowedReason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum MessageSendNotAllowedReason {

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 206.

```text
atchMessageContext {
  BATCH_MESSAGE_CONTEXT_UNSPECIFIED = 0;
  BATCH_MESSAGE_CONTEXT_SHARE = 1;
}

enum MessageSendNotAllowedReason {
  MESSAGE_SEND_NOT_ALLOWED_REASON_UNSPECIFIED = 0;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_FRIENDS_ONLY = 1;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_NOBODY = 2;
  MESSAGE_SEND_NOT_ALLOWED_REASON_BLOCKED = 3;
  MESSAGE_SEND_NOT_ALLOWED_REASON_TRUST_LEVEL = 4;
  MESSAGE_SEND_NOT_ALL
```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06082, FND-06083, FND-06084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06086"></a>
## FND-06086: chesscom.inbox.v1.MessageSendNotAllowedReason.MESSAGE_SEND_NOT_ALLOWED_REASON_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MESSAGE_SEND_NOT_ALLOWED_REASON_UNSPECIFIED = 0;

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 243.

```text
CONTEXT_UNSPECIFIED = 0;
  BATCH_MESSAGE_CONTEXT_SHARE = 1;
}

enum MessageSendNotAllowedReason {
  MESSAGE_SEND_NOT_ALLOWED_REASON_UNSPECIFIED = 0;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_FRIENDS_ONLY = 1;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_NOBODY = 2;
  MESSAGE_SEND_NOT_ALLOWED_REASON_BLOCKED = 3;
  MESSAGE_SEND_NOT_ALLOWED_REASON_TRUST_LEVEL = 4;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SAFE_MODE = 5;
  MESSAGE_
```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06082, FND-06083, FND-06084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06087"></a>
## FND-06087: chesscom.inbox.v1.MessageSendNotAllowedReason.MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_FRIENDS_ONLY = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_FRIENDS_ONLY = 1;

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 294.

```text
ARE = 1;
}

enum MessageSendNotAllowedReason {
  MESSAGE_SEND_NOT_ALLOWED_REASON_UNSPECIFIED = 0;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_FRIENDS_ONLY = 1;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_NOBODY = 2;
  MESSAGE_SEND_NOT_ALLOWED_REASON_BLOCKED = 3;
  MESSAGE_SEND_NOT_ALLOWED_REASON_TRUST_LEVEL = 4;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SAFE_MODE = 5;
  MESSAGE_SEND_NOT_ALLOWED_REASON_RATE_LIMITED = 6;
  MESSAGE
```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06082, FND-06083, FND-06084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06088"></a>
## FND-06088: chesscom.inbox.v1.MessageSendNotAllowedReason.MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_NOBODY = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_NOBODY = 2;

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 354.

```text
D_NOT_ALLOWED_REASON_UNSPECIFIED = 0;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_FRIENDS_ONLY = 1;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_NOBODY = 2;
  MESSAGE_SEND_NOT_ALLOWED_REASON_BLOCKED = 3;
  MESSAGE_SEND_NOT_ALLOWED_REASON_TRUST_LEVEL = 4;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SAFE_MODE = 5;
  MESSAGE_SEND_NOT_ALLOWED_REASON_RATE_LIMITED = 6;
  MESSAGE_SEND_NOT_ALLOWED_REASON_GUEST_ACCOUNT = 7;
  MESSAGE_SEND_N
```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06082, FND-06083, FND-06084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06089"></a>
## FND-06089: chesscom.inbox.v1.MessageSendNotAllowedReason.MESSAGE_SEND_NOT_ALLOWED_REASON_BLOCKED = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MESSAGE_SEND_NOT_ALLOWED_REASON_BLOCKED = 3;

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 408.

```text
OT_ALLOWED_REASON_PRIVACY_FRIENDS_ONLY = 1;
  MESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_NOBODY = 2;
  MESSAGE_SEND_NOT_ALLOWED_REASON_BLOCKED = 3;
  MESSAGE_SEND_NOT_ALLOWED_REASON_TRUST_LEVEL = 4;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SAFE_MODE = 5;
  MESSAGE_SEND_NOT_ALLOWED_REASON_RATE_LIMITED = 6;
  MESSAGE_SEND_NOT_ALLOWED_REASON_GUEST_ACCOUNT = 7;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SENDER_PRIVACY = 8;
  MESSAGE_SEND_N
```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06082, FND-06083, FND-06084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06090"></a>
## FND-06090: chesscom.inbox.v1.MessageSendNotAllowedReason.MESSAGE_SEND_NOT_ALLOWED_REASON_TRUST_LEVEL = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MESSAGE_SEND_NOT_ALLOWED_REASON_TRUST_LEVEL = 4;

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 455.

```text
ESSAGE_SEND_NOT_ALLOWED_REASON_PRIVACY_NOBODY = 2;
  MESSAGE_SEND_NOT_ALLOWED_REASON_BLOCKED = 3;
  MESSAGE_SEND_NOT_ALLOWED_REASON_TRUST_LEVEL = 4;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SAFE_MODE = 5;
  MESSAGE_SEND_NOT_ALLOWED_REASON_RATE_LIMITED = 6;
  MESSAGE_SEND_NOT_ALLOWED_REASON_GUEST_ACCOUNT = 7;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SENDER_PRIVACY = 8;
  MESSAGE_SEND_NOT_ALLOWED_REASON_CONTENT_HIDDEN = 9;
}

```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06082, FND-06083, FND-06084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06091"></a>
## FND-06091: chesscom.inbox.v1.MessageSendNotAllowedReason.MESSAGE_SEND_NOT_ALLOWED_REASON_SAFE_MODE = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MESSAGE_SEND_NOT_ALLOWED_REASON_SAFE_MODE = 5;

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 506.

```text
  MESSAGE_SEND_NOT_ALLOWED_REASON_BLOCKED = 3;
  MESSAGE_SEND_NOT_ALLOWED_REASON_TRUST_LEVEL = 4;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SAFE_MODE = 5;
  MESSAGE_SEND_NOT_ALLOWED_REASON_RATE_LIMITED = 6;
  MESSAGE_SEND_NOT_ALLOWED_REASON_GUEST_ACCOUNT = 7;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SENDER_PRIVACY = 8;
  MESSAGE_SEND_NOT_ALLOWED_REASON_CONTENT_HIDDEN = 9;
}

```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06082, FND-06083, FND-06084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06092"></a>
## FND-06092: chesscom.inbox.v1.MessageSendNotAllowedReason.MESSAGE_SEND_NOT_ALLOWED_REASON_RATE_LIMITED = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MESSAGE_SEND_NOT_ALLOWED_REASON_RATE_LIMITED = 6;

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 555.

```text
MESSAGE_SEND_NOT_ALLOWED_REASON_TRUST_LEVEL = 4;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SAFE_MODE = 5;
  MESSAGE_SEND_NOT_ALLOWED_REASON_RATE_LIMITED = 6;
  MESSAGE_SEND_NOT_ALLOWED_REASON_GUEST_ACCOUNT = 7;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SENDER_PRIVACY = 8;
  MESSAGE_SEND_NOT_ALLOWED_REASON_CONTENT_HIDDEN = 9;
}

```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06082, FND-06083, FND-06084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06093"></a>
## FND-06093: chesscom.inbox.v1.MessageSendNotAllowedReason.MESSAGE_SEND_NOT_ALLOWED_REASON_GUEST_ACCOUNT = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MESSAGE_SEND_NOT_ALLOWED_REASON_GUEST_ACCOUNT = 7;

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 607.

```text
ESSAGE_SEND_NOT_ALLOWED_REASON_SAFE_MODE = 5;
  MESSAGE_SEND_NOT_ALLOWED_REASON_RATE_LIMITED = 6;
  MESSAGE_SEND_NOT_ALLOWED_REASON_GUEST_ACCOUNT = 7;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SENDER_PRIVACY = 8;
  MESSAGE_SEND_NOT_ALLOWED_REASON_CONTENT_HIDDEN = 9;
}

```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06082, FND-06083, FND-06084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06094"></a>
## FND-06094: chesscom.inbox.v1.MessageSendNotAllowedReason.MESSAGE_SEND_NOT_ALLOWED_REASON_SENDER_PRIVACY = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MESSAGE_SEND_NOT_ALLOWED_REASON_SENDER_PRIVACY = 8;

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 660.

```text
GE_SEND_NOT_ALLOWED_REASON_RATE_LIMITED = 6;
  MESSAGE_SEND_NOT_ALLOWED_REASON_GUEST_ACCOUNT = 7;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SENDER_PRIVACY = 8;
  MESSAGE_SEND_NOT_ALLOWED_REASON_CONTENT_HIDDEN = 9;
}

```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06082, FND-06083, FND-06084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06095"></a>
## FND-06095: chesscom.inbox.v1.MessageSendNotAllowedReason.MESSAGE_SEND_NOT_ALLOWED_REASON_CONTENT_HIDDEN = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

MESSAGE_SEND_NOT_ALLOWED_REASON_CONTENT_HIDDEN = 9;

### Evidence

- **SRC-0475** `research/proto/chesscom/inbox/v1/user_message_core.proto` — [preserved redacted evidence](../evidence/text/5ce7e34f608adfebe96afd75776040b4b340508c50462e32d915a297ae214da1.proto)
  Character offset 714.

```text
_SEND_NOT_ALLOWED_REASON_GUEST_ACCOUNT = 7;
  MESSAGE_SEND_NOT_ALLOWED_REASON_SENDER_PRIVACY = 8;
  MESSAGE_SEND_NOT_ALLOWED_REASON_CONTENT_HIDDEN = 9;
}

```

**Source references:** SRC-0475, SRC-1446  
**URL references:** None independently associated  
**Related findings:** FND-06082, FND-06083, FND-06084

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06096"></a>
## FND-06096: message declaration: chesscom.inbox.v1.BatchSendUserMessageRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BatchSendUserMessageRequest {

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 103.

```text
source: chesscom/inbox/v1/user_message_service.proto
// syntax: proto3

package chesscom.inbox.v1;

message BatchSendUserMessageRequest {
  optional string sender_user_uuid = 1;
  repeated string recipient_user_uuids = 2;
  optional string message_text = 3;
  optional .chesscom.inbox.v1.BatchMessageContext context = 4;
}

message BatchSendUserMessageResponse {
  repeated .chesscom.inbox.v1.BatchSendUserMessageRespons
```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06097, FND-06098

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06097"></a>
## FND-06097: chesscom.inbox.v1.BatchSendUserMessageRequest.sender_user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string sender_user_uuid = 1;

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 143.

```text
ervice.proto
// syntax: proto3

package chesscom.inbox.v1;

message BatchSendUserMessageRequest {
  optional string sender_user_uuid = 1;
  repeated string recipient_user_uuids = 2;
  optional string message_text = 3;
  optional .chesscom.inbox.v1.BatchMessageContext context = 4;
}

message BatchSendUserMessageResponse {
  repeated .chesscom.inbox.v1.BatchSendUserMessageResponse.Result results = 1;
  message Result {
```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06098

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06098"></a>
## FND-06098: chesscom.inbox.v1.BatchSendUserMessageRequest.recipient_user_uuids = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string recipient_user_uuids = 2;

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 183.

```text
chesscom.inbox.v1;

message BatchSendUserMessageRequest {
  optional string sender_user_uuid = 1;
  repeated string recipient_user_uuids = 2;
  optional string message_text = 3;
  optional .chesscom.inbox.v1.BatchMessageContext context = 4;
}

message BatchSendUserMessageResponse {
  repeated .chesscom.inbox.v1.BatchSendUserMessageResponse.Result results = 1;
  message Result {
    oneof _error_code {
  string error_
```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06099"></a>
## FND-06099: chesscom.inbox.v1.BatchSendUserMessageRequest.message_text = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string message_text = 3;

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 227.

```text
sageRequest {
  optional string sender_user_uuid = 1;
  repeated string recipient_user_uuids = 2;
  optional string message_text = 3;
  optional .chesscom.inbox.v1.BatchMessageContext context = 4;
}

message BatchSendUserMessageResponse {
  repeated .chesscom.inbox.v1.BatchSendUserMessageResponse.Result results = 1;
  message Result {
    oneof _error_code {
  string error_code = 3;
    }
  optional string recipient_
```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06100"></a>
## FND-06100: chesscom.inbox.v1.BatchSendUserMessageRequest.context = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.inbox.v1.BatchMessageContext context = 4;

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 263.

```text
er_user_uuid = 1;
  repeated string recipient_user_uuids = 2;
  optional string message_text = 3;
  optional .chesscom.inbox.v1.BatchMessageContext context = 4;
}

message BatchSendUserMessageResponse {
  repeated .chesscom.inbox.v1.BatchSendUserMessageResponse.Result results = 1;
  message Result {
    oneof _error_code {
  string error_code = 3;
    }
  optional string recipient_user_uuid = 1;
  optional bool succe
```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06101"></a>
## FND-06101: message declaration: chesscom.inbox.v1.BatchSendUserMessageResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BatchSendUserMessageResponse {

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 327.

```text
optional string message_text = 3;
  optional .chesscom.inbox.v1.BatchMessageContext context = 4;
}

message BatchSendUserMessageResponse {
  repeated .chesscom.inbox.v1.BatchSendUserMessageResponse.Result results = 1;
  message Result {
    oneof _error_code {
  string error_code = 3;
    }
  optional string recipient_user_uuid = 1;
  optional bool success = 2;
  }
}

message CheckCanSendUserMessageRequest {
  option
```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06102"></a>
## FND-06102: chesscom.inbox.v1.BatchSendUserMessageResponse.results = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.inbox.v1.BatchSendUserMessageResponse.Result results = 1;

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 368.

```text
nal .chesscom.inbox.v1.BatchMessageContext context = 4;
}

message BatchSendUserMessageResponse {
  repeated .chesscom.inbox.v1.BatchSendUserMessageResponse.Result results = 1;
  message Result {
    oneof _error_code {
  string error_code = 3;
    }
  optional string recipient_user_uuid = 1;
  optional bool success = 2;
  }
}

message CheckCanSendUserMessageRequest {
  optional string sender_user_uuid = 1;
  optiona
```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06103"></a>
## FND-06103: message declaration: chesscom.inbox.v1.BatchSendUserMessageResponse.Result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Result {

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 447.

```text
rMessageResponse {
  repeated .chesscom.inbox.v1.BatchSendUserMessageResponse.Result results = 1;
  message Result {
    oneof _error_code {
  string error_code = 3;
    }
  optional string recipient_user_uuid = 1;
  optional bool success = 2;
  }
}

message CheckCanSendUserMessageRequest {
  optional string sender_user_uuid = 1;
  optional string recipient_user_uuid = 2;
}

message CheckCanSendUserMessageResponse {

```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06104"></a>
## FND-06104: oneof declaration: chesscom.inbox.v1.BatchSendUserMessageResponse.Result._error_code

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _error_code {

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 468.

```text
repeated .chesscom.inbox.v1.BatchSendUserMessageResponse.Result results = 1;
  message Result {
    oneof _error_code {
  string error_code = 3;
    }
  optional string recipient_user_uuid = 1;
  optional bool success = 2;
  }
}

message CheckCanSendUserMessageRequest {
  optional string sender_user_uuid = 1;
  optional string recipient_user_uuid = 2;
}

message CheckCanSendUserMessageResponse {
  optional bool can_s
```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06105"></a>
## FND-06105: chesscom.inbox.v1.BatchSendUserMessageResponse.Result.error_code = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string error_code = 3;

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 490.

```text
ox.v1.BatchSendUserMessageResponse.Result results = 1;
  message Result {
    oneof _error_code {
  string error_code = 3;
    }
  optional string recipient_user_uuid = 1;
  optional bool success = 2;
  }
}

message CheckCanSendUserMessageRequest {
  optional string sender_user_uuid = 1;
  optional string recipient_user_uuid = 2;
}

message CheckCanSendUserMessageResponse {
  optional bool can_send = 1;
  optional .c
```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06106"></a>
## FND-06106: chesscom.inbox.v1.BatchSendUserMessageResponse.Result.recipient_user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string recipient_user_uuid = 1;

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 521.

```text
nse.Result results = 1;
  message Result {
    oneof _error_code {
  string error_code = 3;
    }
  optional string recipient_user_uuid = 1;
  optional bool success = 2;
  }
}

message CheckCanSendUserMessageRequest {
  optional string sender_user_uuid = 1;
  optional string recipient_user_uuid = 2;
}

message CheckCanSendUserMessageResponse {
  optional bool can_send = 1;
  optional .chesscom.inbox.v1.MessageSendNot
```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06107"></a>
## FND-06107: chesscom.inbox.v1.BatchSendUserMessageResponse.Result.success = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool success = 2;

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 564.

```text
    oneof _error_code {
  string error_code = 3;
    }
  optional string recipient_user_uuid = 1;
  optional bool success = 2;
  }
}

message CheckCanSendUserMessageRequest {
  optional string sender_user_uuid = 1;
  optional string recipient_user_uuid = 2;
}

message CheckCanSendUserMessageResponse {
  optional bool can_send = 1;
  optional .chesscom.inbox.v1.MessageSendNotAllowedReason reason = 2;
}

```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06108"></a>
## FND-06108: message declaration: chesscom.inbox.v1.CheckCanSendUserMessageRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CheckCanSendUserMessageRequest {

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 598.

```text
rror_code = 3;
    }
  optional string recipient_user_uuid = 1;
  optional bool success = 2;
  }
}

message CheckCanSendUserMessageRequest {
  optional string sender_user_uuid = 1;
  optional string recipient_user_uuid = 2;
}

message CheckCanSendUserMessageResponse {
  optional bool can_send = 1;
  optional .chesscom.inbox.v1.MessageSendNotAllowedReason reason = 2;
}

```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06109"></a>
## FND-06109: chesscom.inbox.v1.CheckCanSendUserMessageRequest.sender_user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string sender_user_uuid = 1;

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 143.

```text
ervice.proto
// syntax: proto3

package chesscom.inbox.v1;

message BatchSendUserMessageRequest {
  optional string sender_user_uuid = 1;
  repeated string recipient_user_uuids = 2;
  optional string message_text = 3;
  optional .chesscom.inbox.v1.BatchMessageContext context = 4;
}

message BatchSendUserMessageResponse {
  repeated .chesscom.inbox.v1.BatchSendUserMessageResponse.Result results = 1;
  message Result {
```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06110"></a>
## FND-06110: chesscom.inbox.v1.CheckCanSendUserMessageRequest.recipient_user_uuid = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string recipient_user_uuid = 2;

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 681.

```text
cess = 2;
  }
}

message CheckCanSendUserMessageRequest {
  optional string sender_user_uuid = 1;
  optional string recipient_user_uuid = 2;
}

message CheckCanSendUserMessageResponse {
  optional bool can_send = 1;
  optional .chesscom.inbox.v1.MessageSendNotAllowedReason reason = 2;
}

```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06111"></a>
## FND-06111: message declaration: chesscom.inbox.v1.CheckCanSendUserMessageResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CheckCanSendUserMessageResponse {

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 725.

```text
sageRequest {
  optional string sender_user_uuid = 1;
  optional string recipient_user_uuid = 2;
}

message CheckCanSendUserMessageResponse {
  optional bool can_send = 1;
  optional .chesscom.inbox.v1.MessageSendNotAllowedReason reason = 2;
}

```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06112"></a>
## FND-06112: chesscom.inbox.v1.CheckCanSendUserMessageResponse.can_send = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool can_send = 1;

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 769.

```text
uuid = 1;
  optional string recipient_user_uuid = 2;
}

message CheckCanSendUserMessageResponse {
  optional bool can_send = 1;
  optional .chesscom.inbox.v1.MessageSendNotAllowedReason reason = 2;
}

```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06113"></a>
## FND-06113: chesscom.inbox.v1.CheckCanSendUserMessageResponse.reason = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.inbox.v1.MessageSendNotAllowedReason reason = 2;

### Evidence

- **SRC-0476** `research/proto/chesscom/inbox/v1/user_message_service.proto` — [preserved redacted evidence](../evidence/text/3beabb931d7c1461108a4282e6976d813c4507281f6ac6c8e42474985fb92608.proto)
  Character offset 799.

```text
cipient_user_uuid = 2;
}

message CheckCanSendUserMessageResponse {
  optional bool can_send = 1;
  optional .chesscom.inbox.v1.MessageSendNotAllowedReason reason = 2;
}

```

**Source references:** SRC-0476, SRC-1447  
**URL references:** None independently associated  
**Related findings:** FND-06096, FND-06097, FND-06098

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06114"></a>
## FND-06114: message declaration: chesscom.interactions.v1.Click

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Click {

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 110.

```text
 chesscom/interactions/v1/user_activity.proto
// syntax: proto3

package chesscom.interactions.v1;

message Click {
  oneof _tag {
  string tag = 4;
  }
  oneof _selection_index {
  int32 selection_index = 5;
  }
  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional st
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06115, FND-06116

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06115"></a>
## FND-06115: oneof declaration: chesscom.interactions.v1.Click._tag

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tag {

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 128.

```text
ions/v1/user_activity.proto
// syntax: proto3

package chesscom.interactions.v1;

message Click {
  oneof _tag {
  string tag = 4;
  }
  oneof _selection_index {
  int32 selection_index = 5;
  }
  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;

```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06116

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06116"></a>
## FND-06116: chesscom.interactions.v1.Click.tag = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string tag = 4;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 143.

```text
tivity.proto
// syntax: proto3

package chesscom.interactions.v1;

message Click {
  oneof _tag {
  string tag = 4;
  }
  oneof _selection_index {
  int32 selection_index = 5;
  }
  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated stri
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06117"></a>
## FND-06117: oneof declaration: chesscom.interactions.v1.Click._selection_index

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _selection_index {

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 165.

```text
: proto3

package chesscom.interactions.v1;

message Click {
  oneof _tag {
  string tag = 4;
  }
  oneof _selection_index {
  int32 selection_index = 5;
  }
  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

messag
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06118"></a>
## FND-06118: chesscom.interactions.v1.Click.selection_index = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 selection_index = 5;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 192.

```text
interactions.v1;

message Click {
  oneof _tag {
  string tag = 4;
  }
  oneof _selection_index {
  int32 selection_index = 5;
  }
  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06119"></a>
## FND-06119: oneof declaration: chesscom.interactions.v1.Click._selected_item

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _selected_item {

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 225.

```text

  oneof _tag {
  string tag = 4;
  }
  oneof _selection_index {
  int32 selection_index = 5;
  }
  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof 
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06120"></a>
## FND-06120: chesscom.interactions.v1.Click.selected_item = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string selected_item = 6;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 250.

```text
tag = 4;
  }
  oneof _selection_index {
  int32 selection_index = 5;
  }
  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int3
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06121"></a>
## FND-06121: oneof declaration: chesscom.interactions.v1.Click._count

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _count {

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 282.

```text
index {
  int32 selection_index = 5;
  }
  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  opt
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06122"></a>
## FND-06122: chesscom.interactions.v1.Click.count = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 count = 7;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 299.

```text
election_index = 5;
  }
  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.p
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06123"></a>
## FND-06123: chesscom.interactions.v1.Click.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 322.

```text

  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06124"></a>
## FND-06124: chesscom.interactions.v1.Click.interface = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string interface = 2;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 386.

```text
f _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated s
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06125"></a>
## FND-06125: chesscom.interactions.v1.Click.element = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string element = 3;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 419.

```text

  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated string tags = 5;
  repeated string
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06126"></a>
## FND-06126: chesscom.interactions.v1.Click.tags = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string tags = 8;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 450.

```text
ions.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated string tags = 5;
  repeated string elements = 6;
}

message Input
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06127"></a>
## FND-06127: message declaration: chesscom.interactions.v1.Impression

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Impression {

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 479.

```text
= 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated string tags = 5;
  repeated string elements = 6;
}

message Input {
  oneof _input_text {
  st
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06128"></a>
## FND-06128: oneof declaration: chesscom.interactions.v1.Impression._tag

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _tag {

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 128.

```text
ions/v1/user_activity.proto
// syntax: proto3

package chesscom.interactions.v1;

message Click {
  oneof _tag {
  string tag = 4;
  }
  oneof _selection_index {
  int32 selection_index = 5;
  }
  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;

```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06129"></a>
## FND-06129: chesscom.interactions.v1.Impression.tag = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string tag = 3;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 517.

```text
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated string tags = 5;
  repeated string elements = 6;
}

message Input {
  oneof _input_text {
  string input_text = 4;
  }
  optional .c
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06130"></a>
## FND-06130: oneof declaration: chesscom.interactions.v1.Impression._selection_index

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _selection_index {

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 165.

```text
: proto3

package chesscom.interactions.v1;

message Click {
  oneof _tag {
  string tag = 4;
  }
  oneof _selection_index {
  int32 selection_index = 5;
  }
  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

messag
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06131"></a>
## FND-06131: chesscom.interactions.v1.Impression.selection_index = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

int32 selection_index = 4;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 566.

```text
tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated string tags = 5;
  repeated string elements = 6;
}

message Input {
  oneof _input_text {
  string input_text = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06132"></a>
## FND-06132: chesscom.interactions.v1.Impression.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 322.

```text

  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06133"></a>
## FND-06133: chesscom.interactions.v1.Impression.interface = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string interface = 2;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 386.

```text
f _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated s
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06134"></a>
## FND-06134: chesscom.interactions.v1.Impression.tags = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string tags = 5;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 696.

```text

  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated string tags = 5;
  repeated string elements = 6;
}

message Input {
  oneof _input_text {
  string input_text = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 5;
}

message SharedBoardGifCreated {
 
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06135"></a>
## FND-06135: chesscom.interactions.v1.Impression.elements = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string elements = 6;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 724.

```text
options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated string tags = 5;
  repeated string elements = 6;
}

message Input {
  oneof _input_text {
  string input_text = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 5;
}

message SharedBoardGifCreated {
  optional .chesscom.proto_op
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06136"></a>
## FND-06136: message declaration: chesscom.interactions.v1.Input

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Input {

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 757.

```text
 1;
  optional string interface = 2;
  repeated string tags = 5;
  repeated string elements = 6;
}

message Input {
  oneof _input_text {
  string input_text = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 5;
}

message SharedBoardGifCreated {
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06137"></a>
## FND-06137: oneof declaration: chesscom.interactions.v1.Input._input_text

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _input_text {

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 775.

```text
ing interface = 2;
  repeated string tags = 5;
  repeated string elements = 6;
}

message Input {
  oneof _input_text {
  string input_text = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 5;
}

message SharedBoardGifCreated {
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional strin
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06138"></a>
## FND-06138: chesscom.interactions.v1.Input.input_text = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string input_text = 4;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 797.

```text
epeated string tags = 5;
  repeated string elements = 6;
}

message Input {
  oneof _input_text {
  string input_text = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 5;
}

message SharedBoardGifCreated {
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  opt
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06139"></a>
## FND-06139: chesscom.interactions.v1.Input.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 322.

```text

  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06140"></a>
## FND-06140: chesscom.interactions.v1.Input.interface = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string interface = 2;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 386.

```text
f _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated s
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06141"></a>
## FND-06141: chesscom.interactions.v1.Input.element = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string element = 3;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 419.

```text

  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated string tags = 5;
  repeated string
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06142"></a>
## FND-06142: chesscom.interactions.v1.Input.tags = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string tags = 5;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 696.

```text

  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated string tags = 5;
  repeated string elements = 6;
}

message Input {
  oneof _input_text {
  string input_text = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 5;
}

message SharedBoardGifCreated {
 
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06143"></a>
## FND-06143: message declaration: chesscom.interactions.v1.SharedBoardGifCreated

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SharedBoardGifCreated {

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 983.

```text
= 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 5;
}

message SharedBoardGifCreated {
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 4;
  optional string content = 5;
  optional string website = 6;
  optional int32 size = 7;
  optional string board = 8;
  optional str
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06144"></a>
## FND-06144: chesscom.interactions.v1.SharedBoardGifCreated.funnel = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.proto_options.events.v1.Funnel funnel = 1;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 322.

```text

  oneof _selected_item {
  string selected_item = 6;
  }
  oneof _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06145"></a>
## FND-06145: chesscom.interactions.v1.SharedBoardGifCreated.interface = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string interface = 2;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 386.

```text
f _count {
  int32 count = 7;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated s
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06146"></a>
## FND-06146: chesscom.interactions.v1.SharedBoardGifCreated.element = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string element = 3;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 419.

```text

  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 8;
}

message Impression {
  oneof _tag {
  string tag = 3;
  }
  oneof _selection_index {
  int32 selection_index = 4;
  }
  optional .chesscom.proto_options.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  repeated string tags = 5;
  repeated string
```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06147"></a>
## FND-06147: chesscom.interactions.v1.SharedBoardGifCreated.tags = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string tags = 4;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 1145.

```text
ions.events.v1.Funnel funnel = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 4;
  optional string content = 5;
  optional string website = 6;
  optional int32 size = 7;
  optional string board = 8;
  optional string pieces = 9;
  optional bool has_coordinates = 10;
  optional bool board_is_flipped = 11;
}

```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06148"></a>
## FND-06148: chesscom.interactions.v1.SharedBoardGifCreated.content = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string content = 5;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 1173.

```text
 = 1;
  optional string interface = 2;
  optional string element = 3;
  repeated string tags = 4;
  optional string content = 5;
  optional string website = 6;
  optional int32 size = 7;
  optional string board = 8;
  optional string pieces = 9;
  optional bool has_coordinates = 10;
  optional bool board_is_flipped = 11;
}

```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06149"></a>
## FND-06149: chesscom.interactions.v1.SharedBoardGifCreated.website = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string website = 6;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 1204.

```text
ce = 2;
  optional string element = 3;
  repeated string tags = 4;
  optional string content = 5;
  optional string website = 6;
  optional int32 size = 7;
  optional string board = 8;
  optional string pieces = 9;
  optional bool has_coordinates = 10;
  optional bool board_is_flipped = 11;
}

```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06150"></a>
## FND-06150: chesscom.interactions.v1.SharedBoardGifCreated.size = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 size = 7;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 1235.

```text
nt = 3;
  repeated string tags = 4;
  optional string content = 5;
  optional string website = 6;
  optional int32 size = 7;
  optional string board = 8;
  optional string pieces = 9;
  optional bool has_coordinates = 10;
  optional bool board_is_flipped = 11;
}

```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06151"></a>
## FND-06151: chesscom.interactions.v1.SharedBoardGifCreated.board = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string board = 8;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 1262.

```text
ags = 4;
  optional string content = 5;
  optional string website = 6;
  optional int32 size = 7;
  optional string board = 8;
  optional string pieces = 9;
  optional bool has_coordinates = 10;
  optional bool board_is_flipped = 11;
}

```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06152"></a>
## FND-06152: chesscom.interactions.v1.SharedBoardGifCreated.pieces = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string pieces = 9;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 1291.

```text
ntent = 5;
  optional string website = 6;
  optional int32 size = 7;
  optional string board = 8;
  optional string pieces = 9;
  optional bool has_coordinates = 10;
  optional bool board_is_flipped = 11;
}

```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06153"></a>
## FND-06153: chesscom.interactions.v1.SharedBoardGifCreated.has_coordinates = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool has_coordinates = 10;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 1321.

```text
ebsite = 6;
  optional int32 size = 7;
  optional string board = 8;
  optional string pieces = 9;
  optional bool has_coordinates = 10;
  optional bool board_is_flipped = 11;
}

```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06154"></a>
## FND-06154: chesscom.interactions.v1.SharedBoardGifCreated.board_is_flipped = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool board_is_flipped = 11;

### Evidence

- **SRC-0477** `research/proto/chesscom/interactions/v1/user_activity.proto` — [preserved redacted evidence](../evidence/text/75f44aef2e8cdc224e4df8e558eb4021080b94b9cbfa5aec0757ff8e37cf50bb.proto)
  Character offset 1359.

```text

  optional string board = 8;
  optional string pieces = 9;
  optional bool has_coordinates = 10;
  optional bool board_is_flipped = 11;
}

```

**Source references:** SRC-0477, SRC-1448  
**URL references:** None independently associated  
**Related findings:** FND-06114, FND-06115, FND-06116

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06155"></a>
## FND-06155: enum declaration: chesscom.navigation.v1.ScreenEntityType

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum ScreenEntityType {

### Evidence

- **SRC-0478** `research/proto/chesscom/navigation/v1/screen_entity.proto` — [preserved redacted evidence](../evidence/text/b67b99797a2071ff469cfd65f1a77002e9734adbe66c138e42300784476bc97c.proto)
  Character offset 106.

```text
rce: chesscom/navigation/v1/screen_entity.proto
// syntax: proto3

package chesscom.navigation.v1;

enum ScreenEntityType {
  SCREEN_ENTITY_TYPE_UNSPECIFIED = 0;
  SCREEN_ENTITY_TYPE_FORUM_TOPIC = 1;
  SCREEN_ENTITY_TYPE_ARTICLE = 2;
  SCREEN_ENTITY_TYPE_NEWS_ARTICLE = 3;
  SCREEN_ENTITY_TYPE_EVENT = 4;
  SCREEN_ENTITY_TYPE_PLAYER = 5;
  SCREEN_ENTITY_TYPE_MEMBER = 6;
}

message ScreenEntity {
  oneof _name {
  strin
```

**Source references:** SRC-0478, SRC-1449  
**URL references:** None independently associated  
**Related findings:** FND-06156, FND-06157

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06156"></a>
## FND-06156: chesscom.navigation.v1.ScreenEntityType.SCREEN_ENTITY_TYPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCREEN_ENTITY_TYPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0478** `research/proto/chesscom/navigation/v1/screen_entity.proto` — [preserved redacted evidence](../evidence/text/b67b99797a2071ff469cfd65f1a77002e9734adbe66c138e42300784476bc97c.proto)
  Character offset 132.

```text
1/screen_entity.proto
// syntax: proto3

package chesscom.navigation.v1;

enum ScreenEntityType {
  SCREEN_ENTITY_TYPE_UNSPECIFIED = 0;
  SCREEN_ENTITY_TYPE_FORUM_TOPIC = 1;
  SCREEN_ENTITY_TYPE_ARTICLE = 2;
  SCREEN_ENTITY_TYPE_NEWS_ARTICLE = 3;
  SCREEN_ENTITY_TYPE_EVENT = 4;
  SCREEN_ENTITY_TYPE_PLAYER = 5;
  SCREEN_ENTITY_TYPE_MEMBER = 6;
}

message ScreenEntity {
  oneof _name {
  string name = 3;
  }
  optional
```

**Source references:** SRC-0478, SRC-1449  
**URL references:** None independently associated  
**Related findings:** FND-06155, FND-06157

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06157"></a>
## FND-06157: chesscom.navigation.v1.ScreenEntityType.SCREEN_ENTITY_TYPE_FORUM_TOPIC = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCREEN_ENTITY_TYPE_FORUM_TOPIC = 1;

### Evidence

- **SRC-0478** `research/proto/chesscom/navigation/v1/screen_entity.proto` — [preserved redacted evidence](../evidence/text/b67b99797a2071ff469cfd65f1a77002e9734adbe66c138e42300784476bc97c.proto)
  Character offset 170.

```text
3

package chesscom.navigation.v1;

enum ScreenEntityType {
  SCREEN_ENTITY_TYPE_UNSPECIFIED = 0;
  SCREEN_ENTITY_TYPE_FORUM_TOPIC = 1;
  SCREEN_ENTITY_TYPE_ARTICLE = 2;
  SCREEN_ENTITY_TYPE_NEWS_ARTICLE = 3;
  SCREEN_ENTITY_TYPE_EVENT = 4;
  SCREEN_ENTITY_TYPE_PLAYER = 5;
  SCREEN_ENTITY_TYPE_MEMBER = 6;
}

message ScreenEntity {
  oneof _name {
  string name = 3;
  }
  optional string id = 1;
  optional .chesscom.n
```

**Source references:** SRC-0478, SRC-1449  
**URL references:** None independently associated  
**Related findings:** FND-06155, FND-06156

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06158"></a>
## FND-06158: chesscom.navigation.v1.ScreenEntityType.SCREEN_ENTITY_TYPE_ARTICLE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCREEN_ENTITY_TYPE_ARTICLE = 2;

### Evidence

- **SRC-0478** `research/proto/chesscom/navigation/v1/screen_entity.proto` — [preserved redacted evidence](../evidence/text/b67b99797a2071ff469cfd65f1a77002e9734adbe66c138e42300784476bc97c.proto)
  Character offset 208.

```text
um ScreenEntityType {
  SCREEN_ENTITY_TYPE_UNSPECIFIED = 0;
  SCREEN_ENTITY_TYPE_FORUM_TOPIC = 1;
  SCREEN_ENTITY_TYPE_ARTICLE = 2;
  SCREEN_ENTITY_TYPE_NEWS_ARTICLE = 3;
  SCREEN_ENTITY_TYPE_EVENT = 4;
  SCREEN_ENTITY_TYPE_PLAYER = 5;
  SCREEN_ENTITY_TYPE_MEMBER = 6;
}

message ScreenEntity {
  oneof _name {
  string name = 3;
  }
  optional string id = 1;
  optional .chesscom.navigation.v1.ScreenEntityType type = 2
```

**Source references:** SRC-0478, SRC-1449  
**URL references:** None independently associated  
**Related findings:** FND-06155, FND-06156, FND-06157

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06159"></a>
## FND-06159: chesscom.navigation.v1.ScreenEntityType.SCREEN_ENTITY_TYPE_NEWS_ARTICLE = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCREEN_ENTITY_TYPE_NEWS_ARTICLE = 3;

### Evidence

- **SRC-0478** `research/proto/chesscom/navigation/v1/screen_entity.proto` — [preserved redacted evidence](../evidence/text/b67b99797a2071ff469cfd65f1a77002e9734adbe66c138e42300784476bc97c.proto)
  Character offset 242.

```text
ITY_TYPE_UNSPECIFIED = 0;
  SCREEN_ENTITY_TYPE_FORUM_TOPIC = 1;
  SCREEN_ENTITY_TYPE_ARTICLE = 2;
  SCREEN_ENTITY_TYPE_NEWS_ARTICLE = 3;
  SCREEN_ENTITY_TYPE_EVENT = 4;
  SCREEN_ENTITY_TYPE_PLAYER = 5;
  SCREEN_ENTITY_TYPE_MEMBER = 6;
}

message ScreenEntity {
  oneof _name {
  string name = 3;
  }
  optional string id = 1;
  optional .chesscom.navigation.v1.ScreenEntityType type = 2;
}

```

**Source references:** SRC-0478, SRC-1449  
**URL references:** None independently associated  
**Related findings:** FND-06155, FND-06156, FND-06157

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06160"></a>
## FND-06160: chesscom.navigation.v1.ScreenEntityType.SCREEN_ENTITY_TYPE_EVENT = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCREEN_ENTITY_TYPE_EVENT = 4;

### Evidence

- **SRC-0478** `research/proto/chesscom/navigation/v1/screen_entity.proto` — [preserved redacted evidence](../evidence/text/b67b99797a2071ff469cfd65f1a77002e9734adbe66c138e42300784476bc97c.proto)
  Character offset 281.

```text
TY_TYPE_FORUM_TOPIC = 1;
  SCREEN_ENTITY_TYPE_ARTICLE = 2;
  SCREEN_ENTITY_TYPE_NEWS_ARTICLE = 3;
  SCREEN_ENTITY_TYPE_EVENT = 4;
  SCREEN_ENTITY_TYPE_PLAYER = 5;
  SCREEN_ENTITY_TYPE_MEMBER = 6;
}

message ScreenEntity {
  oneof _name {
  string name = 3;
  }
  optional string id = 1;
  optional .chesscom.navigation.v1.ScreenEntityType type = 2;
}

```

**Source references:** SRC-0478, SRC-1449  
**URL references:** None independently associated  
**Related findings:** FND-06155, FND-06156, FND-06157

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06161"></a>
## FND-06161: chesscom.navigation.v1.ScreenEntityType.SCREEN_ENTITY_TYPE_PLAYER = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCREEN_ENTITY_TYPE_PLAYER = 5;

### Evidence

- **SRC-0478** `research/proto/chesscom/navigation/v1/screen_entity.proto` — [preserved redacted evidence](../evidence/text/b67b99797a2071ff469cfd65f1a77002e9734adbe66c138e42300784476bc97c.proto)
  Character offset 313.

```text
N_ENTITY_TYPE_ARTICLE = 2;
  SCREEN_ENTITY_TYPE_NEWS_ARTICLE = 3;
  SCREEN_ENTITY_TYPE_EVENT = 4;
  SCREEN_ENTITY_TYPE_PLAYER = 5;
  SCREEN_ENTITY_TYPE_MEMBER = 6;
}

message ScreenEntity {
  oneof _name {
  string name = 3;
  }
  optional string id = 1;
  optional .chesscom.navigation.v1.ScreenEntityType type = 2;
}

```

**Source references:** SRC-0478, SRC-1449  
**URL references:** None independently associated  
**Related findings:** FND-06155, FND-06156, FND-06157

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06162"></a>
## FND-06162: chesscom.navigation.v1.ScreenEntityType.SCREEN_ENTITY_TYPE_MEMBER = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCREEN_ENTITY_TYPE_MEMBER = 6;

### Evidence

- **SRC-0478** `research/proto/chesscom/navigation/v1/screen_entity.proto` — [preserved redacted evidence](../evidence/text/b67b99797a2071ff469cfd65f1a77002e9734adbe66c138e42300784476bc97c.proto)
  Character offset 346.

```text
EN_ENTITY_TYPE_NEWS_ARTICLE = 3;
  SCREEN_ENTITY_TYPE_EVENT = 4;
  SCREEN_ENTITY_TYPE_PLAYER = 5;
  SCREEN_ENTITY_TYPE_MEMBER = 6;
}

message ScreenEntity {
  oneof _name {
  string name = 3;
  }
  optional string id = 1;
  optional .chesscom.navigation.v1.ScreenEntityType type = 2;
}

```

**Source references:** SRC-0478, SRC-1449  
**URL references:** None independently associated  
**Related findings:** FND-06155, FND-06156, FND-06157

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06163"></a>
## FND-06163: message declaration: chesscom.navigation.v1.ScreenEntity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ScreenEntity {

### Evidence

- **SRC-0478** `research/proto/chesscom/navigation/v1/screen_entity.proto` — [preserved redacted evidence](../evidence/text/b67b99797a2071ff469cfd65f1a77002e9734adbe66c138e42300784476bc97c.proto)
  Character offset 380.

```text
 SCREEN_ENTITY_TYPE_EVENT = 4;
  SCREEN_ENTITY_TYPE_PLAYER = 5;
  SCREEN_ENTITY_TYPE_MEMBER = 6;
}

message ScreenEntity {
  oneof _name {
  string name = 3;
  }
  optional string id = 1;
  optional .chesscom.navigation.v1.ScreenEntityType type = 2;
}

```

**Source references:** SRC-0478, SRC-1449  
**URL references:** None independently associated  
**Related findings:** FND-06155, FND-06156, FND-06157

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06164"></a>
## FND-06164: oneof declaration: chesscom.navigation.v1.ScreenEntity._name

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _name {

### Evidence

- **SRC-0478** `research/proto/chesscom/navigation/v1/screen_entity.proto` — [preserved redacted evidence](../evidence/text/b67b99797a2071ff469cfd65f1a77002e9734adbe66c138e42300784476bc97c.proto)
  Character offset 405.

```text
 = 4;
  SCREEN_ENTITY_TYPE_PLAYER = 5;
  SCREEN_ENTITY_TYPE_MEMBER = 6;
}

message ScreenEntity {
  oneof _name {
  string name = 3;
  }
  optional string id = 1;
  optional .chesscom.navigation.v1.ScreenEntityType type = 2;
}

```

**Source references:** SRC-0478, SRC-1449  
**URL references:** None independently associated  
**Related findings:** FND-06155, FND-06156, FND-06157

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06165"></a>
## FND-06165: chesscom.navigation.v1.ScreenEntity.name = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string name = 3;

### Evidence

- **SRC-0478** `research/proto/chesscom/navigation/v1/screen_entity.proto` — [preserved redacted evidence](../evidence/text/b67b99797a2071ff469cfd65f1a77002e9734adbe66c138e42300784476bc97c.proto)
  Character offset 421.

```text
NTITY_TYPE_PLAYER = 5;
  SCREEN_ENTITY_TYPE_MEMBER = 6;
}

message ScreenEntity {
  oneof _name {
  string name = 3;
  }
  optional string id = 1;
  optional .chesscom.navigation.v1.ScreenEntityType type = 2;
}

```

**Source references:** SRC-0478, SRC-1449  
**URL references:** None independently associated  
**Related findings:** FND-06155, FND-06156, FND-06157

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06166"></a>
## FND-06166: chesscom.navigation.v1.ScreenEntity.id = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string id = 1;

### Evidence

- **SRC-0478** `research/proto/chesscom/navigation/v1/screen_entity.proto` — [preserved redacted evidence](../evidence/text/b67b99797a2071ff469cfd65f1a77002e9734adbe66c138e42300784476bc97c.proto)
  Character offset 444.

```text
  SCREEN_ENTITY_TYPE_MEMBER = 6;
}

message ScreenEntity {
  oneof _name {
  string name = 3;
  }
  optional string id = 1;
  optional .chesscom.navigation.v1.ScreenEntityType type = 2;
}

```

**Source references:** SRC-0478, SRC-1449  
**URL references:** None independently associated  
**Related findings:** FND-06155, FND-06156, FND-06157

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06167"></a>
## FND-06167: chesscom.navigation.v1.ScreenEntity.type = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.navigation.v1.ScreenEntityType type = 2;

### Evidence

- **SRC-0478** `research/proto/chesscom/navigation/v1/screen_entity.proto` — [preserved redacted evidence](../evidence/text/b67b99797a2071ff469cfd65f1a77002e9734adbe66c138e42300784476bc97c.proto)
  Character offset 470.

```text
R = 6;
}

message ScreenEntity {
  oneof _name {
  string name = 3;
  }
  optional string id = 1;
  optional .chesscom.navigation.v1.ScreenEntityType type = 2;
}

```

**Source references:** SRC-0478, SRC-1449  
**URL references:** None independently associated  
**Related findings:** FND-06155, FND-06156, FND-06157

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-06168"></a>
## FND-06168: enum declaration: chesscom.oauth.v1.Scope

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum Scope {

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 88.

```text
// source: chesscom/oauth/v1/scope.proto
// syntax: proto3

package chesscom.oauth.v1;

enum Scope {
  SCOPE_UNSPECIFIED = 0;
  SCOPE_PUBLIC = 1;
  SCOPE_NONE = 2;
  SCOPE_CHESS = 100;
  SCOPE_ADDRESS = 200;
  SCOPE_EMAIL = 201;
  SCOPE_OPENID = 202;
  SCOPE_PROFILE = 203;
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06169"></a>
## FND-06169: chesscom.oauth.v1.Scope.SCOPE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_UNSPECIFIED = 0;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 103.

```text
source: chesscom/oauth/v1/scope.proto
// syntax: proto3

package chesscom.oauth.v1;

enum Scope {
  SCOPE_UNSPECIFIED = 0;
  SCOPE_PUBLIC = 1;
  SCOPE_NONE = 2;
  SCOPE_CHESS = 100;
  SCOPE_ADDRESS = 200;
  SCOPE_EMAIL = 201;
  SCOPE_OPENID = 202;
  SCOPE_PROFILE = 203;
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WR
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06170"></a>
## FND-06170: chesscom.oauth.v1.Scope.SCOPE_PUBLIC = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_PUBLIC = 1;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 128.

```text
/scope.proto
// syntax: proto3

package chesscom.oauth.v1;

enum Scope {
  SCOPE_UNSPECIFIED = 0;
  SCOPE_PUBLIC = 1;
  SCOPE_NONE = 2;
  SCOPE_CHESS = 100;
  SCOPE_ADDRESS = 200;
  SCOPE_EMAIL = 201;
  SCOPE_OPENID = 202;
  SCOPE_PROFILE = 203;
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMEN
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06171"></a>
## FND-06171: chesscom.oauth.v1.Scope.SCOPE_NONE = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_NONE = 2;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 148.

```text
ax: proto3

package chesscom.oauth.v1;

enum Scope {
  SCOPE_UNSPECIFIED = 0;
  SCOPE_PUBLIC = 1;
  SCOPE_NONE = 2;
  SCOPE_CHESS = 100;
  SCOPE_ADDRESS = 200;
  SCOPE_EMAIL = 201;
  SCOPE_OPENID = 202;
  SCOPE_PROFILE = 203;
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SC
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06172"></a>
## FND-06172: chesscom.oauth.v1.Scope.SCOPE_CHESS = 100

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_CHESS = 100;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 166.

```text
e chesscom.oauth.v1;

enum Scope {
  SCOPE_UNSPECIFIED = 0;
  SCOPE_PUBLIC = 1;
  SCOPE_NONE = 2;
  SCOPE_CHESS = 100;
  SCOPE_ADDRESS = 200;
  SCOPE_EMAIL = 201;
  SCOPE_OPENID = 202;
  SCOPE_PROFILE = 203;
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06173"></a>
## FND-06173: chesscom.oauth.v1.Scope.SCOPE_ADDRESS = 200

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_ADDRESS = 200;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 187.

```text

enum Scope {
  SCOPE_UNSPECIFIED = 0;
  SCOPE_PUBLIC = 1;
  SCOPE_NONE = 2;
  SCOPE_CHESS = 100;
  SCOPE_ADDRESS = 200;
  SCOPE_EMAIL = 201;
  SCOPE_OPENID = 202;
  SCOPE_PROFILE = 203;
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOP
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-06174"></a>
## FND-06174: chesscom.oauth.v1.Scope.SCOPE_EMAIL = 201

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SCOPE_EMAIL = 201;

### Evidence

- **SRC-0479** `research/proto/chesscom/oauth/v1/scope.proto` — [preserved redacted evidence](../evidence/text/caab7a41d67369a89fdc21062831223c0bfb464a27858e1a4385a50285ffbaea.proto)
  Character offset 210.

```text
NSPECIFIED = 0;
  SCOPE_PUBLIC = 1;
  SCOPE_NONE = 2;
  SCOPE_CHESS = 100;
  SCOPE_ADDRESS = 200;
  SCOPE_EMAIL = 201;
  SCOPE_OPENID = 202;
  SCOPE_PROFILE = 203;
  SCOPE_EBOARD = 204;
  SCOPE_NOADS = 205;
  SCOPE_PROLONGED_TOKEN = 206;
  SCOPE_ANALYSIS = 300;
  SCOPE_ARTICLES_READ = 301;
  SCOPE_ATTRIBUTION_WRITE = 302;
  SCOPE_COMMENTS_WRITE = 303;
  SCOPE_COMPUTER_GAMES_MANAGE = 304;
  SCOPE_COMPUTER_GAMES_PLAY =
```

**Source references:** SRC-0479, SRC-1450  
**URL references:** None independently associated  
**Related findings:** FND-06168, FND-06169, FND-06170

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
