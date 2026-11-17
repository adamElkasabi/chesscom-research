# data_models — findings 9201–9300

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-09475"></a>
## FND-09475: message declaration: chesscom.user_gateway.v1.RemoveFriendResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RemoveFriendResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 3882.

```text
e RemoveFriendRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message RemoveFriendResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.RemoveFriendFailure failure = 2;
  }
}

message BlockUserRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message BlockUserResponse {
  oneof
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09476"></a>
## FND-09476: oneof declaration: chesscom.user_gateway.v1.RemoveFriendResponse.result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof result {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2692.

```text
esscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message SendFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.SendFriendRequestFailure failure = 2;
  }
}

message AcceptFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message AcceptFriendRequestResponse {
  oneof result 
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09477"></a>
## FND-09477: chesscom.user_gateway.v1.RemoveFriendResponse.success = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2709.

```text
ay.v1.UserIdentifier user_identifier = 1;
}

message SendFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.SendFriendRequestFailure failure = 2;
  }
}

message AcceptFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message AcceptFriendRequestResponse {
  oneof result {
  .chesscom.use
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09478"></a>
## FND-09478: chesscom.user_gateway.v1.RemoveFriendResponse.failure = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.RemoveFriendFailure failure = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 3998.

```text
iendResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.RemoveFriendFailure failure = 2;
  }
}

message BlockUserRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message BlockUserResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.BlockUserFai
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09479"></a>
## FND-09479: message declaration: chesscom.user_gateway.v1.BlockUserRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BlockUserRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 4064.

```text
onshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.RemoveFriendFailure failure = 2;
  }
}

message BlockUserRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message BlockUserResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.BlockUserFailure failure = 2;
  }
}

message UnblockUserRequest {
  optional .
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09480"></a>
## FND-09480: chesscom.user_gateway.v1.BlockUserRequest.user_identifier = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2580.

```text
stRequest {
  oneof _source {
  string source = 2;
  }
  oneof _method {
  string method = 3;
  }
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message SendFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.SendFriendRequestFailure failure = 2;
  }
}

message AcceptFriendRequestRequest {
  optional .chess
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09481"></a>
## FND-09481: message declaration: chesscom.user_gateway.v1.BlockUserResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BlockUserResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 4167.

```text
sage BlockUserRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message BlockUserResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.BlockUserFailure failure = 2;
  }
}

message UnblockUserRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message UnblockUserResponse {
  oneof r
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09482"></a>
## FND-09482: oneof declaration: chesscom.user_gateway.v1.BlockUserResponse.result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof result {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2692.

```text
esscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message SendFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.SendFriendRequestFailure failure = 2;
  }
}

message AcceptFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message AcceptFriendRequestResponse {
  oneof result 
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09483"></a>
## FND-09483: chesscom.user_gateway.v1.BlockUserResponse.success = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2709.

```text
ay.v1.UserIdentifier user_identifier = 1;
}

message SendFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.SendFriendRequestFailure failure = 2;
  }
}

message AcceptFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message AcceptFriendRequestResponse {
  oneof result {
  .chesscom.use
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09484"></a>
## FND-09484: chesscom.user_gateway.v1.BlockUserResponse.failure = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.BlockUserFailure failure = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 4280.

```text
UserResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.BlockUserFailure failure = 2;
  }
}

message UnblockUserRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message UnblockUserResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.UnblockUser
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09485"></a>
## FND-09485: message declaration: chesscom.user_gateway.v1.UnblockUserRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UnblockUserRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 4343.

```text
ationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.BlockUserFailure failure = 2;
  }
}

message UnblockUserRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message UnblockUserResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.UnblockUserFailure failure = 2;
  }
}

message AcceptFriendLinkRequest {
 
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09486"></a>
## FND-09486: chesscom.user_gateway.v1.UnblockUserRequest.user_identifier = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2580.

```text
stRequest {
  oneof _source {
  string source = 2;
  }
  oneof _method {
  string method = 3;
  }
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message SendFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.SendFriendRequestFailure failure = 2;
  }
}

message AcceptFriendRequestRequest {
  optional .chess
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09487"></a>
## FND-09487: message declaration: chesscom.user_gateway.v1.UnblockUserResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UnblockUserResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 4448.

```text
ge UnblockUserRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message UnblockUserResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.UnblockUserFailure failure = 2;
  }
}

message AcceptFriendLinkRequest {
  optional string friend_link_hash = 1;
}

message AcceptFriendLinkResponse {
  oneof result {
  .chesscom
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09488"></a>
## FND-09488: oneof declaration: chesscom.user_gateway.v1.UnblockUserResponse.result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof result {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2692.

```text
esscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message SendFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.SendFriendRequestFailure failure = 2;
  }
}

message AcceptFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message AcceptFriendRequestResponse {
  oneof result 
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09489"></a>
## FND-09489: chesscom.user_gateway.v1.UnblockUserResponse.success = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2709.

```text
ay.v1.UserIdentifier user_identifier = 1;
}

message SendFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.SendFriendRequestFailure failure = 2;
  }
}

message AcceptFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message AcceptFriendRequestResponse {
  oneof result {
  .chesscom.use
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09490"></a>
## FND-09490: chesscom.user_gateway.v1.UnblockUserResponse.failure = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.UnblockUserFailure failure = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 4563.

```text
UserResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.UnblockUserFailure failure = 2;
  }
}

message AcceptFriendLinkRequest {
  optional string friend_link_hash = 1;
}

message AcceptFriendLinkResponse {
  oneof result {
  .chesscom.user_gateway.v1.AcceptFriendLinkSuccess success = 1;
  .chesscom.user_gateway.v1.AcceptFriendLinkFailure failure =
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09491"></a>
## FND-09491: message declaration: chesscom.user_gateway.v1.AcceptFriendLinkRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AcceptFriendLinkRequest {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 4628.

```text
ionshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.UnblockUserFailure failure = 2;
  }
}

message AcceptFriendLinkRequest {
  optional string friend_link_hash = 1;
}

message AcceptFriendLinkResponse {
  oneof result {
  .chesscom.user_gateway.v1.AcceptFriendLinkSuccess success = 1;
  .chesscom.user_gateway.v1.AcceptFriendLinkFailure failure = 2;
  }
}

```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09492"></a>
## FND-09492: chesscom.user_gateway.v1.AcceptFriendLinkRequest.friend_link_hash = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string friend_link_hash = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 4664.

```text
chesscom.user_gateway.v1.UnblockUserFailure failure = 2;
  }
}

message AcceptFriendLinkRequest {
  optional string friend_link_hash = 1;
}

message AcceptFriendLinkResponse {
  oneof result {
  .chesscom.user_gateway.v1.AcceptFriendLinkSuccess success = 1;
  .chesscom.user_gateway.v1.AcceptFriendLinkFailure failure = 2;
  }
}

```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09493"></a>
## FND-09493: message declaration: chesscom.user_gateway.v1.AcceptFriendLinkResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AcceptFriendLinkResponse {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 4705.

```text
re failure = 2;
  }
}

message AcceptFriendLinkRequest {
  optional string friend_link_hash = 1;
}

message AcceptFriendLinkResponse {
  oneof result {
  .chesscom.user_gateway.v1.AcceptFriendLinkSuccess success = 1;
  .chesscom.user_gateway.v1.AcceptFriendLinkFailure failure = 2;
  }
}

```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09494"></a>
## FND-09494: oneof declaration: chesscom.user_gateway.v1.AcceptFriendLinkResponse.result

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof result {

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 2692.

```text
esscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message SendFriendRequestResponse {
  oneof result {
  .chesscom.user_gateway.v1.RelationshipWriteSuccess success = 1;
  .chesscom.user_gateway.v1.SendFriendRequestFailure failure = 2;
  }
}

message AcceptFriendRequestRequest {
  optional .chesscom.user_gateway.v1.UserIdentifier user_identifier = 1;
}

message AcceptFriendRequestResponse {
  oneof result 
```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09495"></a>
## FND-09495: chesscom.user_gateway.v1.AcceptFriendLinkResponse.success = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.AcceptFriendLinkSuccess success = 1;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 4759.

```text
 {
  optional string friend_link_hash = 1;
}

message AcceptFriendLinkResponse {
  oneof result {
  .chesscom.user_gateway.v1.AcceptFriendLinkSuccess success = 1;
  .chesscom.user_gateway.v1.AcceptFriendLinkFailure failure = 2;
  }
}

```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09496"></a>
## FND-09496: chesscom.user_gateway.v1.AcceptFriendLinkResponse.failure = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.AcceptFriendLinkFailure failure = 2;

### Evidence

- **SRC-0594** `research/proto/chesscom/user_gateway/v1/user_gateway_service.proto` — [preserved redacted evidence](../evidence/text/fa9e5dadadd23a3f9c90669f0c0abcafea85203521fbebd6a4b6e4df6c4c3331.proto)
  Character offset 4824.

```text
dLinkResponse {
  oneof result {
  .chesscom.user_gateway.v1.AcceptFriendLinkSuccess success = 1;
  .chesscom.user_gateway.v1.AcceptFriendLinkFailure failure = 2;
  }
}

```

**Source references:** SRC-0594, SRC-1565  
**URL references:** None independently associated  
**Related findings:** FND-09400, FND-09401, FND-09402

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09497"></a>
## FND-09497: message declaration: chesscom.user_gateway.v1.RelationshipWriteSuccess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RelationshipWriteSuccess {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 127.

```text
teway/v1/user_gateway_service_envelopes.proto
// syntax: proto3

package chesscom.user_gateway.v1;

message RelationshipWriteSuccess {
  optional .google.protobuf.Timestamp completed_at = 1;
}

message SendFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowe
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09498"></a>
## FND-09498: chesscom.user_gateway.v1.RelationshipWriteSuccess.completed_at = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp completed_at = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 164.

```text
es.proto
// syntax: proto3

package chesscom.user_gateway.v1;

message RelationshipWriteSuccess {
  optional .google.protobuf.Timestamp completed_at = 1;
}

message SendFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;

```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09499"></a>
## FND-09499: message declaration: chesscom.user_gateway.v1.SendFriendRequestFailure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SendFriendRequestFailure {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 221.

```text
.v1;

message RelationshipWriteSuccess {
  optional .google.protobuf.Timestamp completed_at = 1;
}

message SendFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friend
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09500"></a>
## FND-09500: oneof declaration: chesscom.user_gateway.v1.SendFriendRequestFailure.error

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof error {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 258.

```text
s {
  optional .google.protobuf.Timestamp completed_at = 1;
}

message SendFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.u
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09501"></a>
## FND-09501: chesscom.user_gateway.v1.SendFriendRequestFailure.already_friends = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 274.

```text
google.protobuf.Timestamp completed_at = 1;
}

message SendFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.user_gateway.v1.T
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09502"></a>
## FND-09502: chesscom.user_gateway.v1.SendFriendRequestFailure.user_blocked = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.UserBlocked user_blocked = 2;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 338.

```text
dRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.user_gateway.v1.TargetFriendCapReached target_friend_cap_reached = 5;
  .chesscom
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09503"></a>
## FND-09503: chesscom.user_gateway.v1.SendFriendRequestFailure.self_relationship_not_allowed = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 396.

```text
.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.user_gateway.v1.TargetFriendCapReached target_friend_cap_reached = 5;
  .chesscom.user_gateway.v1.OutgoingFriendRequestCapReached outgoing_
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09504"></a>
## FND-09504: chesscom.user_gateway.v1.SendFriendRequestFailure.friendship_limit_reached = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 486.

```text
ed = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.user_gateway.v1.TargetFriendCapReached target_friend_cap_reached = 5;
  .chesscom.user_gateway.v1.OutgoingFriendRequestCapReached outgoing_friend_request_cap_reached = 6;
  .chesscom.user_gateway.v1.TrustLevelDenied trust_level_d
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09505"></a>
## FND-09505: chesscom.user_gateway.v1.SendFriendRequestFailure.target_friend_cap_reached = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.TargetFriendCapReached target_friend_cap_reached = 5;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 567.

```text
not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.user_gateway.v1.TargetFriendCapReached target_friend_cap_reached = 5;
  .chesscom.user_gateway.v1.OutgoingFriendRequestCapReached outgoing_friend_request_cap_reached = 6;
  .chesscom.user_gateway.v1.TrustLevelDenied trust_level_denied = 7;
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 8;
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09506"></a>
## FND-09506: chesscom.user_gateway.v1.SendFriendRequestFailure.outgoing_friend_request_cap_reached = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.OutgoingFriendRequestCapReached outgoing_friend_request_cap_reached = 6;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 649.

```text
it_reached = 4;
  .chesscom.user_gateway.v1.TargetFriendCapReached target_friend_cap_reached = 5;
  .chesscom.user_gateway.v1.OutgoingFriendRequestCapReached outgoing_friend_request_cap_reached = 6;
  .chesscom.user_gateway.v1.TrustLevelDenied trust_level_denied = 7;
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 8;
  .chesscom.user_gateway.v1.TargetNotAcceptingFriendRequests target_not_accepting
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09507"></a>
## FND-09507: chesscom.user_gateway.v1.SendFriendRequestFailure.trust_level_denied = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.TrustLevelDenied trust_level_denied = 7;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 750.

```text
chesscom.user_gateway.v1.OutgoingFriendRequestCapReached outgoing_friend_request_cap_reached = 6;
  .chesscom.user_gateway.v1.TrustLevelDenied trust_level_denied = 7;
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 8;
  .chesscom.user_gateway.v1.TargetNotAcceptingFriendRequests target_not_accepting_friend_requests = 9;
  .chesscom.user_gateway.v1.TargetUnavailable target_unavailable = 10;
  .chess
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09508"></a>
## FND-09508: chesscom.user_gateway.v1.SendFriendRequestFailure.rate_limit_exceeded = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 8;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 819.

```text
end_request_cap_reached = 6;
  .chesscom.user_gateway.v1.TrustLevelDenied trust_level_denied = 7;
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 8;
  .chesscom.user_gateway.v1.TargetNotAcceptingFriendRequests target_not_accepting_friend_requests = 9;
  .chesscom.user_gateway.v1.TargetUnavailable target_unavailable = 10;
  .chesscom.user_gateway.v1.SenderNotAllowed sender_not_allowed = 11;
  .ches
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09509"></a>
## FND-09509: chesscom.user_gateway.v1.SendFriendRequestFailure.target_not_accepting_friend_requests = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.TargetNotAcceptingFriendRequests target_not_accepting_friend_requests = 9;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 890.

```text
ed trust_level_denied = 7;
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 8;
  .chesscom.user_gateway.v1.TargetNotAcceptingFriendRequests target_not_accepting_friend_requests = 9;
  .chesscom.user_gateway.v1.TargetUnavailable target_unavailable = 10;
  .chesscom.user_gateway.v1.SenderNotAllowed sender_not_allowed = 11;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 12;
  .chesscom.u
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09510"></a>
## FND-09510: chesscom.user_gateway.v1.SendFriendRequestFailure.target_unavailable = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.TargetUnavailable target_unavailable = 10;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 993.

```text
esscom.user_gateway.v1.TargetNotAcceptingFriendRequests target_not_accepting_friend_requests = 9;
  .chesscom.user_gateway.v1.TargetUnavailable target_unavailable = 10;
  .chesscom.user_gateway.v1.SenderNotAllowed sender_not_allowed = 11;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 12;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 13;
  }
}

message AcceptFriendRequestFailure
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09511"></a>
## FND-09511: chesscom.user_gateway.v1.SendFriendRequestFailure.sender_not_allowed = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.SenderNotAllowed sender_not_allowed = 11;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1064.

```text
pting_friend_requests = 9;
  .chesscom.user_gateway.v1.TargetUnavailable target_unavailable = 10;
  .chesscom.user_gateway.v1.SenderNotAllowed sender_not_allowed = 11;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 12;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 13;
  }
}

message AcceptFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RelationshipNotFound not
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09512"></a>
## FND-09512: chesscom.user_gateway.v1.SendFriendRequestFailure.invalid_request = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.InvalidRequest invalid_request = 12;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1134.

```text
le target_unavailable = 10;
  .chesscom.user_gateway.v1.SenderNotAllowed sender_not_allowed = 11;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 12;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 13;
  }
}

message AcceptFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RelationshipNotFound not_found = 1;
  .chesscom.user_gateway.v1.FriendRequestNotPending friend
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09513"></a>
## FND-09513: chesscom.user_gateway.v1.SendFriendRequestFailure.target_user_not_found = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 13;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1199.

```text
Allowed sender_not_allowed = 11;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 12;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 13;
  }
}

message AcceptFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RelationshipNotFound not_found = 1;
  .chesscom.user_gateway.v1.FriendRequestNotPending friend_request_not_pending = 2;
  .chesscom.user_gateway.v1.FriendshipL
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09514"></a>
## FND-09514: message declaration: chesscom.user_gateway.v1.AcceptFriendRequestFailure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AcceptFriendRequestFailure {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1279.

```text
lid_request = 12;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 13;
  }
}

message AcceptFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RelationshipNotFound not_found = 1;
  .chesscom.user_gateway.v1.FriendRequestNotPending friend_request_not_pending = 2;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 3;
  .chesscom.user_gateway.v1.UserBlocke
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09515"></a>
## FND-09515: oneof declaration: chesscom.user_gateway.v1.AcceptFriendRequestFailure.error

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof error {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 258.

```text
s {
  optional .google.protobuf.Timestamp completed_at = 1;
}

message SendFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.u
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09516"></a>
## FND-09516: chesscom.user_gateway.v1.AcceptFriendRequestFailure.not_found = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.RelationshipNotFound not_found = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1334.

```text
rNotFound target_user_not_found = 13;
  }
}

message AcceptFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RelationshipNotFound not_found = 1;
  .chesscom.user_gateway.v1.FriendRequestNotPending friend_request_not_pending = 2;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 3;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 4;
  .chesscom.user_gateway.v1.RateLim
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09517"></a>
## FND-09517: chesscom.user_gateway.v1.AcceptFriendRequestFailure.friend_request_not_pending = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.FriendRequestNotPending friend_request_not_pending = 2;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1398.

```text
dRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RelationshipNotFound not_found = 1;
  .chesscom.user_gateway.v1.FriendRequestNotPending friend_request_not_pending = 2;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 3;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 4;
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 5;
  .chesscom.user_gateway.v1.
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09518"></a>
## FND-09518: chesscom.user_gateway.v1.AcceptFriendRequestFailure.friendship_limit_reached = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 3;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1482.

```text
ot_found = 1;
  .chesscom.user_gateway.v1.FriendRequestNotPending friend_request_not_pending = 2;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 3;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 4;
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 5;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 6;
  .chesscom.user_gateway.v1.InvalidReq
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09519"></a>
## FND-09519: chesscom.user_gateway.v1.AcceptFriendRequestFailure.user_blocked = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.UserBlocked user_blocked = 4;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1563.

```text
not_pending = 2;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 3;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 4;
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 5;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 6;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 7;
  }
}

message DeclineFriendRequestFailure {
  oneof er
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09520"></a>
## FND-09520: chesscom.user_gateway.v1.AcceptFriendRequestFailure.rate_limit_exceeded = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 5;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1621.

```text
itReached friendship_limit_reached = 3;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 4;
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 5;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 6;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 7;
  }
}

message DeclineFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_l
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09521"></a>
## FND-09521: chesscom.user_gateway.v1.AcceptFriendRequestFailure.target_user_not_found = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 6;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1692.

```text
rBlocked user_blocked = 4;
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 5;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 6;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 7;
  }
}

message DeclineFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound targe
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09522"></a>
## FND-09522: chesscom.user_gateway.v1.AcceptFriendRequestFailure.invalid_request = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.InvalidRequest invalid_request = 7;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1766.

```text
ate_limit_exceeded = 5;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 6;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 7;
  }
}

message DeclineFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_r
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09523"></a>
## FND-09523: message declaration: chesscom.user_gateway.v1.DeclineFriendRequestFailure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DeclineFriendRequestFailure {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1835.

```text
d target_user_not_found = 6;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 7;
  }
}

message DeclineFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 3;
  }
}

message CancelFriendRequestFailure {
  oneof error
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09524"></a>
## FND-09524: oneof declaration: chesscom.user_gateway.v1.DeclineFriendRequestFailure.error

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof error {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 258.

```text
s {
  optional .google.protobuf.Timestamp completed_at = 1;
}

message SendFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.u
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09525"></a>
## FND-09525: chesscom.user_gateway.v1.DeclineFriendRequestFailure.rate_limit_exceeded = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1891.

```text
.InvalidRequest invalid_request = 7;
  }
}

message DeclineFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 3;
  }
}

message CancelFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_li
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09526"></a>
## FND-09526: chesscom.user_gateway.v1.DeclineFriendRequestFailure.target_user_not_found = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1962.

```text
tFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 3;
  }
}

message CancelFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09527"></a>
## FND-09527: chesscom.user_gateway.v1.DeclineFriendRequestFailure.invalid_request = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.InvalidRequest invalid_request = 3;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2036.

```text
ate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 3;
  }
}

message CancelFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_re
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09528"></a>
## FND-09528: message declaration: chesscom.user_gateway.v1.CancelFriendRequestFailure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CancelFriendRequestFailure {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2105.

```text
d target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 3;
  }
}

message CancelFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 3;
  }
}

message RemoveFriendFailure {
  oneof error {
  .ch
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09529"></a>
## FND-09529: oneof declaration: chesscom.user_gateway.v1.CancelFriendRequestFailure.error

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof error {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 258.

```text
s {
  optional .google.protobuf.Timestamp completed_at = 1;
}

message SendFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.u
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09530"></a>
## FND-09530: chesscom.user_gateway.v1.CancelFriendRequestFailure.rate_limit_exceeded = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1891.

```text
.InvalidRequest invalid_request = 7;
  }
}

message DeclineFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 3;
  }
}

message CancelFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_li
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09531"></a>
## FND-09531: chesscom.user_gateway.v1.CancelFriendRequestFailure.target_user_not_found = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1962.

```text
tFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 3;
  }
}

message CancelFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09532"></a>
## FND-09532: chesscom.user_gateway.v1.CancelFriendRequestFailure.invalid_request = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.InvalidRequest invalid_request = 3;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2036.

```text
ate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 3;
  }
}

message CancelFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_re
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09533"></a>
## FND-09533: message declaration: chesscom.user_gateway.v1.RemoveFriendFailure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RemoveFriendFailure {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2374.

```text
d target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 3;
  }
}

message RemoveFriendFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 1;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 2;
  }
}

message BlockUserFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetImmune target_immune = 1;
  .chesscom.user_gateway.v
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09534"></a>
## FND-09534: oneof declaration: chesscom.user_gateway.v1.RemoveFriendFailure.error

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof error {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 258.

```text
s {
  optional .google.protobuf.Timestamp completed_at = 1;
}

message SendFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.u
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09535"></a>
## FND-09535: chesscom.user_gateway.v1.RemoveFriendFailure.target_user_not_found = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2422.

```text
teway.v1.InvalidRequest invalid_request = 3;
  }
}

message RemoveFriendFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 1;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 2;
  }
}

message BlockUserFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetImmune target_immune = 1;
  .chesscom.user_gateway.v1.BlockLimitReached block_limit_reached = 2;
  .
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09536"></a>
## FND-09536: chesscom.user_gateway.v1.RemoveFriendFailure.invalid_request = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.InvalidRequest invalid_request = 2;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2496.

```text
ilure {
  oneof error {
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 1;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 2;
  }
}

message BlockUserFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetImmune target_immune = 1;
  .chesscom.user_gateway.v1.BlockLimitReached block_limit_reached = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09537"></a>
## FND-09537: message declaration: chesscom.user_gateway.v1.BlockUserFailure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BlockUserFailure {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2565.

```text
d target_user_not_found = 1;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 2;
  }
}

message BlockUserFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetImmune target_immune = 1;
  .chesscom.user_gateway.v1.BlockLimitReached block_limit_reached = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.TargetUserNotFound target_us
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09538"></a>
## FND-09538: oneof declaration: chesscom.user_gateway.v1.BlockUserFailure.error

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof error {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 258.

```text
s {
  optional .google.protobuf.Timestamp completed_at = 1;
}

message SendFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.u
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09539"></a>
## FND-09539: chesscom.user_gateway.v1.BlockUserFailure.target_immune = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.TargetImmune target_immune = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2610.

```text
_gateway.v1.InvalidRequest invalid_request = 2;
  }
}

message BlockUserFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetImmune target_immune = 1;
  .chesscom.user_gateway.v1.BlockLimitReached block_limit_reached = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 4;
  .chesscom.user_gateway.v1
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09540"></a>
## FND-09540: chesscom.user_gateway.v1.BlockUserFailure.block_limit_reached = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.BlockLimitReached block_limit_reached = 2;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2670.

```text
ge BlockUserFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetImmune target_immune = 1;
  .chesscom.user_gateway.v1.BlockLimitReached block_limit_reached = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 4;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 5;
  }
}

message UnblockU
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09541"></a>
## FND-09541: chesscom.user_gateway.v1.BlockUserFailure.self_relationship_not_allowed = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 396.

```text
.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.user_gateway.v1.TargetFriendCapReached target_friend_cap_reached = 5;
  .chesscom.user_gateway.v1.OutgoingFriendRequestCapReached outgoing_
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09542"></a>
## FND-09542: chesscom.user_gateway.v1.BlockUserFailure.target_user_not_found = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 4;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2831.

```text
ed = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 4;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 5;
  }
}

message UnblockUserFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 1;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09543"></a>
## FND-09543: chesscom.user_gateway.v1.BlockUserFailure.invalid_request = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.InvalidRequest invalid_request = 5;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2905.

```text
onship_not_allowed = 3;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 4;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 5;
  }
}

message UnblockUserFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 1;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 2;
  }
}

message AcceptFriendLinkSuccess {
  optional string friend_uu
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09544"></a>
## FND-09544: message declaration: chesscom.user_gateway.v1.UnblockUserFailure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UnblockUserFailure {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2974.

```text
d target_user_not_found = 4;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 5;
  }
}

message UnblockUserFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 1;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 2;
  }
}

message AcceptFriendLinkSuccess {
  optional string friend_uuid = 1;
  optional string friend_username = 2;
}

message AcceptFrien
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09545"></a>
## FND-09545: oneof declaration: chesscom.user_gateway.v1.UnblockUserFailure.error

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof error {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 258.

```text
s {
  optional .google.protobuf.Timestamp completed_at = 1;
}

message SendFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.u
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09546"></a>
## FND-09546: chesscom.user_gateway.v1.UnblockUserFailure.target_user_not_found = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2422.

```text
teway.v1.InvalidRequest invalid_request = 3;
  }
}

message RemoveFriendFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 1;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 2;
  }
}

message BlockUserFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetImmune target_immune = 1;
  .chesscom.user_gateway.v1.BlockLimitReached block_limit_reached = 2;
  .
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09547"></a>
## FND-09547: chesscom.user_gateway.v1.UnblockUserFailure.invalid_request = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.InvalidRequest invalid_request = 2;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 2496.

```text
ilure {
  oneof error {
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 1;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 2;
  }
}

message BlockUserFailure {
  oneof error {
  .chesscom.user_gateway.v1.TargetImmune target_immune = 1;
  .chesscom.user_gateway.v1.BlockLimitReached block_limit_reached = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09548"></a>
## FND-09548: message declaration: chesscom.user_gateway.v1.AcceptFriendLinkSuccess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AcceptFriendLinkSuccess {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3164.

```text
d target_user_not_found = 1;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 2;
  }
}

message AcceptFriendLinkSuccess {
  optional string friend_uuid = 1;
  optional string friend_username = 2;
}

message AcceptFriendLinkFailure {
  oneof error {
  .chesscom.user_gateway.v1.FriendLinkInvalid friend_link_invalid = 1;
  .chesscom.user_gateway.v1.FriendLinkNotFound friend_link_not_found = 2;
  .chesscom.us
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09549"></a>
## FND-09549: chesscom.user_gateway.v1.AcceptFriendLinkSuccess.friend_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string friend_uuid = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3200.

```text
scom.user_gateway.v1.InvalidRequest invalid_request = 2;
  }
}

message AcceptFriendLinkSuccess {
  optional string friend_uuid = 1;
  optional string friend_username = 2;
}

message AcceptFriendLinkFailure {
  oneof error {
  .chesscom.user_gateway.v1.FriendLinkInvalid friend_link_invalid = 1;
  .chesscom.user_gateway.v1.FriendLinkNotFound friend_link_not_found = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAll
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09550"></a>
## FND-09550: chesscom.user_gateway.v1.AcceptFriendLinkSuccess.friend_username = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string friend_username = 2;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3235.

```text
 invalid_request = 2;
  }
}

message AcceptFriendLinkSuccess {
  optional string friend_uuid = 1;
  optional string friend_username = 2;
}

message AcceptFriendLinkFailure {
  oneof error {
  .chesscom.user_gateway.v1.FriendLinkInvalid friend_link_invalid = 1;
  .chesscom.user_gateway.v1.FriendLinkNotFound friend_link_not_found = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed 
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09551"></a>
## FND-09551: message declaration: chesscom.user_gateway.v1.AcceptFriendLinkFailure

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AcceptFriendLinkFailure {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3275.

```text
eptFriendLinkSuccess {
  optional string friend_uuid = 1;
  optional string friend_username = 2;
}

message AcceptFriendLinkFailure {
  oneof error {
  .chesscom.user_gateway.v1.FriendLinkInvalid friend_link_invalid = 1;
  .chesscom.user_gateway.v1.FriendLinkNotFound friend_link_not_found = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.UserBlo
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09552"></a>
## FND-09552: oneof declaration: chesscom.user_gateway.v1.AcceptFriendLinkFailure.error

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof error {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 258.

```text
s {
  optional .google.protobuf.Timestamp completed_at = 1;
}

message SendFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.u
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09553"></a>
## FND-09553: chesscom.user_gateway.v1.AcceptFriendLinkFailure.friend_link_invalid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.FriendLinkInvalid friend_link_invalid = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3327.

```text
 = 1;
  optional string friend_username = 2;
}

message AcceptFriendLinkFailure {
  oneof error {
  .chesscom.user_gateway.v1.FriendLinkInvalid friend_link_invalid = 1;
  .chesscom.user_gateway.v1.FriendLinkNotFound friend_link_not_found = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 4;
  .chesscom.user_gateway.v1.F
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09554"></a>
## FND-09554: chesscom.user_gateway.v1.AcceptFriendLinkFailure.friend_link_not_found = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.FriendLinkNotFound friend_link_not_found = 2;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3398.

```text
kFailure {
  oneof error {
  .chesscom.user_gateway.v1.FriendLinkInvalid friend_link_invalid = 1;
  .chesscom.user_gateway.v1.FriendLinkNotFound friend_link_not_found = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 4;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 5;
  .chesscom.user_ga
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09555"></a>
## FND-09555: chesscom.user_gateway.v1.AcceptFriendLinkFailure.self_relationship_not_allowed = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 396.

```text
.v1.AlreadyFriends already_friends = 1;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 2;
  .chesscom.user_gateway.v1.SelfRelationshipNotAllowed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 4;
  .chesscom.user_gateway.v1.TargetFriendCapReached target_friend_cap_reached = 5;
  .chesscom.user_gateway.v1.OutgoingFriendRequestCapReached outgoing_
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09556"></a>
## FND-09556: chesscom.user_gateway.v1.AcceptFriendLinkFailure.user_blocked = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.UserBlocked user_blocked = 4;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1563.

```text
not_pending = 2;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 3;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 4;
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 5;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 6;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 7;
  }
}

message DeclineFriendRequestFailure {
  oneof er
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09557"></a>
## FND-09557: chesscom.user_gateway.v1.AcceptFriendLinkFailure.friendship_limit_reached = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 5;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3620.

```text
owed self_relationship_not_allowed = 3;
  .chesscom.user_gateway.v1.UserBlocked user_blocked = 4;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 5;
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 6;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 7;
  }
}

message AlreadyFriends {
}

message TargetFriendCapReached {
}

message OutgoingFriendRequestCapRea
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09558"></a>
## FND-09558: chesscom.user_gateway.v1.AcceptFriendLinkFailure.rate_limit_exceeded = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 6;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3701.

```text
ser_blocked = 4;
  .chesscom.user_gateway.v1.FriendshipLimitReached friendship_limit_reached = 5;
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 6;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 7;
  }
}

message AlreadyFriends {
}

message TargetFriendCapReached {
}

message OutgoingFriendRequestCapReached {
}

message TrustLevelDenied {
  oneof _reason {
  string reason = 1;
  }
}
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09559"></a>
## FND-09559: chesscom.user_gateway.v1.AcceptFriendLinkFailure.invalid_request = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_gateway.v1.InvalidRequest invalid_request = 7;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 1766.

```text
ate_limit_exceeded = 5;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 6;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 7;
  }
}

message DeclineFriendRequestFailure {
  oneof error {
  .chesscom.user_gateway.v1.RateLimitExceeded rate_limit_exceeded = 1;
  .chesscom.user_gateway.v1.TargetUserNotFound target_user_not_found = 2;
  .chesscom.user_gateway.v1.InvalidRequest invalid_r
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09560"></a>
## FND-09560: message declaration: chesscom.user_gateway.v1.AlreadyFriends

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message AlreadyFriends {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3841.

```text
ded rate_limit_exceeded = 6;
  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 7;
  }
}

message AlreadyFriends {
}

message TargetFriendCapReached {
}

message OutgoingFriendRequestCapReached {
}

message TrustLevelDenied {
  oneof _reason {
  string reason = 1;
  }
}

message TargetNotAcceptingFriendRequests {
}

message TargetUnavailable {
}

message SenderNotAllowed {
}

message TargetUserNotFound {
}

```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09561"></a>
## FND-09561: message declaration: chesscom.user_gateway.v1.TargetFriendCapReached

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TargetFriendCapReached {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3869.

```text

  .chesscom.user_gateway.v1.InvalidRequest invalid_request = 7;
  }
}

message AlreadyFriends {
}

message TargetFriendCapReached {
}

message OutgoingFriendRequestCapReached {
}

message TrustLevelDenied {
  oneof _reason {
  string reason = 1;
  }
}

message TargetNotAcceptingFriendRequests {
}

message TargetUnavailable {
}

message SenderNotAllowed {
}

message TargetUserNotFound {
}

message RelationshipNotFoun
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09562"></a>
## FND-09562: message declaration: chesscom.user_gateway.v1.OutgoingFriendRequestCapReached

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message OutgoingFriendRequestCapReached {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3905.

```text
Request invalid_request = 7;
  }
}

message AlreadyFriends {
}

message TargetFriendCapReached {
}

message OutgoingFriendRequestCapReached {
}

message TrustLevelDenied {
  oneof _reason {
  string reason = 1;
  }
}

message TargetNotAcceptingFriendRequests {
}

message TargetUnavailable {
}

message SenderNotAllowed {
}

message TargetUserNotFound {
}

message RelationshipNotFound {
}

message FriendRequestNotPendi
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09563"></a>
## FND-09563: message declaration: chesscom.user_gateway.v1.TrustLevelDenied

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TrustLevelDenied {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3950.

```text
lreadyFriends {
}

message TargetFriendCapReached {
}

message OutgoingFriendRequestCapReached {
}

message TrustLevelDenied {
  oneof _reason {
  string reason = 1;
  }
}

message TargetNotAcceptingFriendRequests {
}

message TargetUnavailable {
}

message SenderNotAllowed {
}

message TargetUserNotFound {
}

message RelationshipNotFound {
}

message FriendRequestNotPending {
}

message FriendLinkInvalid {
}

messag
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09564"></a>
## FND-09564: oneof declaration: chesscom.user_gateway.v1.TrustLevelDenied._reason

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _reason {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3979.

```text
rgetFriendCapReached {
}

message OutgoingFriendRequestCapReached {
}

message TrustLevelDenied {
  oneof _reason {
  string reason = 1;
  }
}

message TargetNotAcceptingFriendRequests {
}

message TargetUnavailable {
}

message SenderNotAllowed {
}

message TargetUserNotFound {
}

message RelationshipNotFound {
}

message FriendRequestNotPending {
}

message FriendLinkInvalid {
}

message FriendLinkNotFound {
}

mes
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09565"></a>
## FND-09565: chesscom.user_gateway.v1.TrustLevelDenied.reason = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string reason = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 3997.

```text
ed {
}

message OutgoingFriendRequestCapReached {
}

message TrustLevelDenied {
  oneof _reason {
  string reason = 1;
  }
}

message TargetNotAcceptingFriendRequests {
}

message TargetUnavailable {
}

message SenderNotAllowed {
}

message TargetUserNotFound {
}

message RelationshipNotFound {
}

message FriendRequestNotPending {
}

message FriendLinkInvalid {
}

message FriendLinkNotFound {
}

message SelfRelations
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09566"></a>
## FND-09566: message declaration: chesscom.user_gateway.v1.TargetNotAcceptingFriendRequests

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TargetNotAcceptingFriendRequests {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4023.

```text
iendRequestCapReached {
}

message TrustLevelDenied {
  oneof _reason {
  string reason = 1;
  }
}

message TargetNotAcceptingFriendRequests {
}

message TargetUnavailable {
}

message SenderNotAllowed {
}

message TargetUserNotFound {
}

message RelationshipNotFound {
}

message FriendRequestNotPending {
}

message FriendLinkInvalid {
}

message FriendLinkNotFound {
}

message SelfRelationshipNotAllowed {
}

message
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09567"></a>
## FND-09567: message declaration: chesscom.user_gateway.v1.TargetUnavailable

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TargetUnavailable {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4069.

```text
enied {
  oneof _reason {
  string reason = 1;
  }
}

message TargetNotAcceptingFriendRequests {
}

message TargetUnavailable {
}

message SenderNotAllowed {
}

message TargetUserNotFound {
}

message RelationshipNotFound {
}

message FriendRequestNotPending {
}

message FriendLinkInvalid {
}

message FriendLinkNotFound {
}

message SelfRelationshipNotAllowed {
}

message UserBlocked {
}

message TargetImmune {
}

me
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09568"></a>
## FND-09568: message declaration: chesscom.user_gateway.v1.SenderNotAllowed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SenderNotAllowed {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4100.

```text
ing reason = 1;
  }
}

message TargetNotAcceptingFriendRequests {
}

message TargetUnavailable {
}

message SenderNotAllowed {
}

message TargetUserNotFound {
}

message RelationshipNotFound {
}

message FriendRequestNotPending {
}

message FriendLinkInvalid {
}

message FriendLinkNotFound {
}

message SelfRelationshipNotAllowed {
}

message UserBlocked {
}

message TargetImmune {
}

message BlockLimitReached {
  opt
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09569"></a>
## FND-09569: message declaration: chesscom.user_gateway.v1.TargetUserNotFound

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TargetUserNotFound {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4130.

```text
 TargetNotAcceptingFriendRequests {
}

message TargetUnavailable {
}

message SenderNotAllowed {
}

message TargetUserNotFound {
}

message RelationshipNotFound {
}

message FriendRequestNotPending {
}

message FriendLinkInvalid {
}

message FriendLinkNotFound {
}

message SelfRelationshipNotAllowed {
}

message UserBlocked {
}

message TargetImmune {
}

message BlockLimitReached {
  optional int32 max_blocked_users 
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09570"></a>
## FND-09570: message declaration: chesscom.user_gateway.v1.RelationshipNotFound

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RelationshipNotFound {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4162.

```text
s {
}

message TargetUnavailable {
}

message SenderNotAllowed {
}

message TargetUserNotFound {
}

message RelationshipNotFound {
}

message FriendRequestNotPending {
}

message FriendLinkInvalid {
}

message FriendLinkNotFound {
}

message SelfRelationshipNotAllowed {
}

message UserBlocked {
}

message TargetImmune {
}

message BlockLimitReached {
  optional int32 max_blocked_users = 1;
}

message FriendshipLimitR
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09571"></a>
## FND-09571: message declaration: chesscom.user_gateway.v1.FriendRequestNotPending

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FriendRequestNotPending {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4196.

```text

}

message SenderNotAllowed {
}

message TargetUserNotFound {
}

message RelationshipNotFound {
}

message FriendRequestNotPending {
}

message FriendLinkInvalid {
}

message FriendLinkNotFound {
}

message SelfRelationshipNotAllowed {
}

message UserBlocked {
}

message TargetImmune {
}

message BlockLimitReached {
  optional int32 max_blocked_users = 1;
}

message FriendshipLimitReached {
  optional int32 max_frie
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09572"></a>
## FND-09572: message declaration: chesscom.user_gateway.v1.FriendLinkInvalid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FriendLinkInvalid {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4233.

```text
sage TargetUserNotFound {
}

message RelationshipNotFound {
}

message FriendRequestNotPending {
}

message FriendLinkInvalid {
}

message FriendLinkNotFound {
}

message SelfRelationshipNotAllowed {
}

message UserBlocked {
}

message TargetImmune {
}

message BlockLimitReached {
  optional int32 max_blocked_users = 1;
}

message FriendshipLimitReached {
  optional int32 max_friends = 1;
}

message RateLimitExceeded
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09573"></a>
## FND-09573: message declaration: chesscom.user_gateway.v1.FriendLinkNotFound

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FriendLinkNotFound {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4264.

```text
ssage RelationshipNotFound {
}

message FriendRequestNotPending {
}

message FriendLinkInvalid {
}

message FriendLinkNotFound {
}

message SelfRelationshipNotAllowed {
}

message UserBlocked {
}

message TargetImmune {
}

message BlockLimitReached {
  optional int32 max_blocked_users = 1;
}

message FriendshipLimitReached {
  optional int32 max_friends = 1;
}

message RateLimitExceeded {
  optional int32 retry_after
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09574"></a>
## FND-09574: message declaration: chesscom.user_gateway.v1.SelfRelationshipNotAllowed

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SelfRelationshipNotAllowed {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4296.

```text
message FriendRequestNotPending {
}

message FriendLinkInvalid {
}

message FriendLinkNotFound {
}

message SelfRelationshipNotAllowed {
}

message UserBlocked {
}

message TargetImmune {
}

message BlockLimitReached {
  optional int32 max_blocked_users = 1;
}

message FriendshipLimitReached {
  optional int32 max_friends = 1;
}

message RateLimitExceeded {
  optional int32 retry_after_seconds = 1;
}

message Invalid
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
