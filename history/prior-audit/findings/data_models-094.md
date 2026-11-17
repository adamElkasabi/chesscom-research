# data_models — findings 9301–9400

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-09575"></a>
## FND-09575: message declaration: chesscom.user_gateway.v1.UserBlocked

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserBlocked {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4336.

```text
sage FriendLinkInvalid {
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

message InvalidRequest {
  oneof _message {
  string me
```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09576"></a>
## FND-09576: message declaration: chesscom.user_gateway.v1.TargetImmune

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message TargetImmune {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4361.

```text
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

message InvalidRequest {
  oneof _message {
  string message = 1;
  }
}

```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09577"></a>
## FND-09577: message declaration: chesscom.user_gateway.v1.BlockLimitReached

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message BlockLimitReached {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4387.

```text
und {
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

message InvalidRequest {
  oneof _message {
  string message = 1;
  }
}

```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09578"></a>
## FND-09578: chesscom.user_gateway.v1.BlockLimitReached.max_blocked_users = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 max_blocked_users = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4417.

```text
hipNotAllowed {
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

message InvalidRequest {
  oneof _message {
  string message = 1;
  }
}

```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09579"></a>
## FND-09579: message declaration: chesscom.user_gateway.v1.FriendshipLimitReached

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FriendshipLimitReached {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4458.

```text
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

message InvalidRequest {
  oneof _message {
  string message = 1;
  }
}

```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09580"></a>
## FND-09580: chesscom.user_gateway.v1.FriendshipLimitReached.max_friends = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 max_friends = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4493.

```text
e BlockLimitReached {
  optional int32 max_blocked_users = 1;
}

message FriendshipLimitReached {
  optional int32 max_friends = 1;
}

message RateLimitExceeded {
  optional int32 retry_after_seconds = 1;
}

message InvalidRequest {
  oneof _message {
  string message = 1;
  }
}

```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09581"></a>
## FND-09581: message declaration: chesscom.user_gateway.v1.RateLimitExceeded

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message RateLimitExceeded {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4528.

```text
t32 max_blocked_users = 1;
}

message FriendshipLimitReached {
  optional int32 max_friends = 1;
}

message RateLimitExceeded {
  optional int32 retry_after_seconds = 1;
}

message InvalidRequest {
  oneof _message {
  string message = 1;
  }
}

```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09582"></a>
## FND-09582: chesscom.user_gateway.v1.RateLimitExceeded.retry_after_seconds = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional int32 retry_after_seconds = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4558.

```text
message FriendshipLimitReached {
  optional int32 max_friends = 1;
}

message RateLimitExceeded {
  optional int32 retry_after_seconds = 1;
}

message InvalidRequest {
  oneof _message {
  string message = 1;
  }
}

```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09583"></a>
## FND-09583: message declaration: chesscom.user_gateway.v1.InvalidRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message InvalidRequest {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4601.

```text
 int32 max_friends = 1;
}

message RateLimitExceeded {
  optional int32 retry_after_seconds = 1;
}

message InvalidRequest {
  oneof _message {
  string message = 1;
  }
}

```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09584"></a>
## FND-09584: oneof declaration: chesscom.user_gateway.v1.InvalidRequest._message

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _message {

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4628.

```text
message RateLimitExceeded {
  optional int32 retry_after_seconds = 1;
}

message InvalidRequest {
  oneof _message {
  string message = 1;
  }
}

```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09585"></a>
## FND-09585: chesscom.user_gateway.v1.InvalidRequest.message = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string message = 1;

### Evidence

- **SRC-0595** `research/proto/chesscom/user_gateway/v1/user_gateway_service_envelopes.proto` — [preserved redacted evidence](../evidence/text/ddc8d658347b9e5399e25f8d42467b2ed3d1389eacdec849ddd05bb6e6c6babf.proto)
  Character offset 4647.

```text
ceeded {
  optional int32 retry_after_seconds = 1;
}

message InvalidRequest {
  oneof _message {
  string message = 1;
  }
}

```

**Source references:** SRC-0595, SRC-1566  
**URL references:** None independently associated  
**Related findings:** FND-09497, FND-09498, FND-09499

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09586"></a>
## FND-09586: message declaration: chesscom.user_gateway.v1.UserIdentifier

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message UserIdentifier {

### Evidence

- **SRC-0596** `research/proto/chesscom/user_gateway/v1/user_identifier.proto` — [preserved redacted evidence](../evidence/text/b6e8359c79dc73bfd5ffdb987248cdbef52a15d62a97fca4362a13ee6965469d.proto)
  Character offset 112.

```text
hesscom/user_gateway/v1/user_identifier.proto
// syntax: proto3

package chesscom.user_gateway.v1;

message UserIdentifier {
  oneof id {
  string user_uuid = 1;
  string username = 2;
  }
}

```

**Source references:** SRC-0596, SRC-1567  
**URL references:** None independently associated  
**Related findings:** FND-09587, FND-09588

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09587"></a>
## FND-09587: oneof declaration: chesscom.user_gateway.v1.UserIdentifier.id

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof id {

### Evidence

- **SRC-0596** `research/proto/chesscom/user_gateway/v1/user_identifier.proto` — [preserved redacted evidence](../evidence/text/b6e8359c79dc73bfd5ffdb987248cdbef52a15d62a97fca4362a13ee6965469d.proto)
  Character offset 139.

```text
r_identifier.proto
// syntax: proto3

package chesscom.user_gateway.v1;

message UserIdentifier {
  oneof id {
  string user_uuid = 1;
  string username = 2;
  }
}

```

**Source references:** SRC-0596, SRC-1567  
**URL references:** None independently associated  
**Related findings:** FND-09586, FND-09588

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09588"></a>
## FND-09588: chesscom.user_gateway.v1.UserIdentifier.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_uuid = 1;

### Evidence

- **SRC-0596** `research/proto/chesscom/user_gateway/v1/user_identifier.proto` — [preserved redacted evidence](../evidence/text/b6e8359c79dc73bfd5ffdb987248cdbef52a15d62a97fca4362a13ee6965469d.proto)
  Character offset 152.

```text
proto
// syntax: proto3

package chesscom.user_gateway.v1;

message UserIdentifier {
  oneof id {
  string user_uuid = 1;
  string username = 2;
  }
}

```

**Source references:** SRC-0596, SRC-1567  
**URL references:** None independently associated  
**Related findings:** FND-09586, FND-09587

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09589"></a>
## FND-09589: chesscom.user_gateway.v1.UserIdentifier.username = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string username = 2;

### Evidence

- **SRC-0596** `research/proto/chesscom/user_gateway/v1/user_identifier.proto` — [preserved redacted evidence](../evidence/text/b6e8359c79dc73bfd5ffdb987248cdbef52a15d62a97fca4362a13ee6965469d.proto)
  Character offset 176.

```text

package chesscom.user_gateway.v1;

message UserIdentifier {
  oneof id {
  string user_uuid = 1;
  string username = 2;
  }
}

```

**Source references:** SRC-0596, SRC-1567  
**URL references:** None independently associated  
**Related findings:** FND-09586, FND-09587, FND-09588

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09590"></a>
## FND-09590: message declaration: chesscom.user_profile.v1.FollowedUser

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FollowedUser {

### Evidence

- **SRC-0597** `research/proto/chesscom/user_profile/v1/social.proto` — [preserved redacted evidence](../evidence/text/b7575860652daf6a882da63e440032cba1fe6b1e8c69cbf8d8c5701127216194.proto)
  Character offset 103.

```text
source: chesscom/user_profile/v1/social.proto
// syntax: proto3

package chesscom.user_profile.v1;

message FollowedUser {
  optional string uuid = 1;
  optional string username = 2;
  optional string avatar = 3;
  optional string country_code = 4;
}

```

**Source references:** SRC-0597, SRC-1568  
**URL references:** None independently associated  
**Related findings:** FND-09591, FND-09592

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09591"></a>
## FND-09591: chesscom.user_profile.v1.FollowedUser.uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string uuid = 1;

### Evidence

- **SRC-0597** `research/proto/chesscom/user_profile/v1/social.proto` — [preserved redacted evidence](../evidence/text/b7575860652daf6a882da63e440032cba1fe6b1e8c69cbf8d8c5701127216194.proto)
  Character offset 128.

```text
file/v1/social.proto
// syntax: proto3

package chesscom.user_profile.v1;

message FollowedUser {
  optional string uuid = 1;
  optional string username = 2;
  optional string avatar = 3;
  optional string country_code = 4;
}

```

**Source references:** SRC-0597, SRC-1568  
**URL references:** None independently associated  
**Related findings:** FND-09590, FND-09592

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09592"></a>
## FND-09592: chesscom.user_profile.v1.FollowedUser.username = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string username = 2;

### Evidence

- **SRC-0597** `research/proto/chesscom/user_profile/v1/social.proto` — [preserved redacted evidence](../evidence/text/b7575860652daf6a882da63e440032cba1fe6b1e8c69cbf8d8c5701127216194.proto)
  Character offset 156.

```text
ax: proto3

package chesscom.user_profile.v1;

message FollowedUser {
  optional string uuid = 1;
  optional string username = 2;
  optional string avatar = 3;
  optional string country_code = 4;
}

```

**Source references:** SRC-0597, SRC-1568  
**URL references:** None independently associated  
**Related findings:** FND-09590, FND-09591

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09593"></a>
## FND-09593: chesscom.user_profile.v1.FollowedUser.avatar = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string avatar = 3;

### Evidence

- **SRC-0597** `research/proto/chesscom/user_profile/v1/social.proto` — [preserved redacted evidence](../evidence/text/b7575860652daf6a882da63e440032cba1fe6b1e8c69cbf8d8c5701127216194.proto)
  Character offset 188.

```text
r_profile.v1;

message FollowedUser {
  optional string uuid = 1;
  optional string username = 2;
  optional string avatar = 3;
  optional string country_code = 4;
}

```

**Source references:** SRC-0597, SRC-1568  
**URL references:** None independently associated  
**Related findings:** FND-09590, FND-09591, FND-09592

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09594"></a>
## FND-09594: chesscom.user_profile.v1.FollowedUser.country_code = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string country_code = 4;

### Evidence

- **SRC-0597** `research/proto/chesscom/user_profile/v1/social.proto` — [preserved redacted evidence](../evidence/text/b7575860652daf6a882da63e440032cba1fe6b1e8c69cbf8d8c5701127216194.proto)
  Character offset 218.

```text
dUser {
  optional string uuid = 1;
  optional string username = 2;
  optional string avatar = 3;
  optional string country_code = 4;
}

```

**Source references:** SRC-0597, SRC-1568  
**URL references:** None independently associated  
**Related findings:** FND-09590, FND-09591, FND-09592

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09595"></a>
## FND-09595: message declaration: chesscom.user_profile.v1.ListFollowedUsersRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFollowedUsersRequest {

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 111.

```text
chesscom/user_profile/v1/social_service.proto
// syntax: proto3

package chesscom.user_profile.v1;

message ListFollowedUsersRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _requester_uuid {
  string requester_uuid = 2;
  }
}

message ListFollowedUsersResponse {
  repeated .chesscom.user_profile.v1.FollowedUser followed_users = 1;
  optional .chesscom.api.v1.ResponsePa
```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09596, FND-09597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09596"></a>
## FND-09596: oneof declaration: chesscom.user_profile.v1.ListFollowedUsersRequest._pagination

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pagination {

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 148.

```text
ce.proto
// syntax: proto3

package chesscom.user_profile.v1;

message ListFollowedUsersRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _requester_uuid {
  string requester_uuid = 2;
  }
}

message ListFollowedUsersResponse {
  repeated .chesscom.user_profile.v1.FollowedUser followed_users = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message D
```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09597"></a>
## FND-09597: chesscom.user_profile.v1.ListFollowedUsersRequest.pagination = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.api.v1.RequestPagination pagination = 1;

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 170.

```text
oto3

package chesscom.user_profile.v1;

message ListFollowedUsersRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _requester_uuid {
  string requester_uuid = 2;
  }
}

message ListFollowedUsersResponse {
  repeated .chesscom.user_profile.v1.FollowedUser followed_users = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message DoesUserFollowOtherUser
```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09598"></a>
## FND-09598: oneof declaration: chesscom.user_profile.v1.ListFollowedUsersRequest._requester_uuid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _requester_uuid {

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 227.

```text
owedUsersRequest {
  oneof _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _requester_uuid {
  string requester_uuid = 2;
  }
}

message ListFollowedUsersResponse {
  repeated .chesscom.user_profile.v1.FollowedUser followed_users = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message DoesUserFollowOtherUsersRequest {
  oneof _user_uuid {
  string user_uuid = 1;
 
```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09599"></a>
## FND-09599: chesscom.user_profile.v1.ListFollowedUsersRequest.requester_uuid = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string requester_uuid = 2;

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 253.

```text
 _pagination {
  .chesscom.api.v1.RequestPagination pagination = 1;
  }
  oneof _requester_uuid {
  string requester_uuid = 2;
  }
}

message ListFollowedUsersResponse {
  repeated .chesscom.user_profile.v1.FollowedUser followed_users = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message DoesUserFollowOtherUsersRequest {
  oneof _user_uuid {
  string user_uuid = 1;
  }
  repeated string targe
```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09600"></a>
## FND-09600: message declaration: chesscom.user_profile.v1.ListFollowedUsersResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ListFollowedUsersResponse {

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 287.

```text
RequestPagination pagination = 1;
  }
  oneof _requester_uuid {
  string requester_uuid = 2;
  }
}

message ListFollowedUsersResponse {
  repeated .chesscom.user_profile.v1.FollowedUser followed_users = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message DoesUserFollowOtherUsersRequest {
  oneof _user_uuid {
  string user_uuid = 1;
  }
  repeated string target_user_uuids = 2;
}

message DoesU
```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09601"></a>
## FND-09601: chesscom.user_profile.v1.ListFollowedUsersResponse.followed_users = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_profile.v1.FollowedUser followed_users = 1;

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 325.

```text
  oneof _requester_uuid {
  string requester_uuid = 2;
  }
}

message ListFollowedUsersResponse {
  repeated .chesscom.user_profile.v1.FollowedUser followed_users = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message DoesUserFollowOtherUsersRequest {
  oneof _user_uuid {
  string user_uuid = 1;
  }
  repeated string target_user_uuids = 2;
}

message DoesUserFollowOtherUsersResponse {
  repeat
```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09602"></a>
## FND-09602: chesscom.user_profile.v1.ListFollowedUsersResponse.pagination = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.ResponsePagination pagination = 2;

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 395.

```text
ListFollowedUsersResponse {
  repeated .chesscom.user_profile.v1.FollowedUser followed_users = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message DoesUserFollowOtherUsersRequest {
  oneof _user_uuid {
  string user_uuid = 1;
  }
  repeated string target_user_uuids = 2;
}

message DoesUserFollowOtherUsersResponse {
  repeated .chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.FollowSt
```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09603"></a>
## FND-09603: message declaration: chesscom.user_profile.v1.DoesUserFollowOtherUsersRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DoesUserFollowOtherUsersRequest {

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 459.

```text
.FollowedUser followed_users = 1;
  optional .chesscom.api.v1.ResponsePagination pagination = 2;
}

message DoesUserFollowOtherUsersRequest {
  oneof _user_uuid {
  string user_uuid = 1;
  }
  repeated string target_user_uuids = 2;
}

message DoesUserFollowOtherUsersResponse {
  repeated .chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.FollowStatusEntry follow_status = 1;
  message FollowStatusEntry {
  opt
```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09604"></a>
## FND-09604: oneof declaration: chesscom.user_profile.v1.DoesUserFollowOtherUsersRequest._user_uuid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_uuid {

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 503.

```text
 .chesscom.api.v1.ResponsePagination pagination = 2;
}

message DoesUserFollowOtherUsersRequest {
  oneof _user_uuid {
  string user_uuid = 1;
  }
  repeated string target_user_uuids = 2;
}

message DoesUserFollowOtherUsersResponse {
  repeated .chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.FollowStatusEntry follow_status = 1;
  message FollowStatusEntry {
  optional string key = 1;
  optional bool value 
```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09605"></a>
## FND-09605: chesscom.user_profile.v1.DoesUserFollowOtherUsersRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

string user_uuid = 1;

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 524.

```text
ponsePagination pagination = 2;
}

message DoesUserFollowOtherUsersRequest {
  oneof _user_uuid {
  string user_uuid = 1;
  }
  repeated string target_user_uuids = 2;
}

message DoesUserFollowOtherUsersResponse {
  repeated .chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.FollowStatusEntry follow_status = 1;
  message FollowStatusEntry {
  optional string key = 1;
  optional bool value = 2;
  }
}

```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09606"></a>
## FND-09606: chesscom.user_profile.v1.DoesUserFollowOtherUsersRequest.target_user_uuids = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated string target_user_uuids = 2;

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 552.

```text
 2;
}

message DoesUserFollowOtherUsersRequest {
  oneof _user_uuid {
  string user_uuid = 1;
  }
  repeated string target_user_uuids = 2;
}

message DoesUserFollowOtherUsersResponse {
  repeated .chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.FollowStatusEntry follow_status = 1;
  message FollowStatusEntry {
  optional string key = 1;
  optional bool value = 2;
  }
}

```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09607"></a>
## FND-09607: message declaration: chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message DoesUserFollowOtherUsersResponse {

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 594.

```text
uest {
  oneof _user_uuid {
  string user_uuid = 1;
  }
  repeated string target_user_uuids = 2;
}

message DoesUserFollowOtherUsersResponse {
  repeated .chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.FollowStatusEntry follow_status = 1;
  message FollowStatusEntry {
  optional string key = 1;
  optional bool value = 2;
  }
}

```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09608"></a>
## FND-09608: chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.follow_status = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.FollowStatusEntry follow_status = 1;

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 639.

```text
d = 1;
  }
  repeated string target_user_uuids = 2;
}

message DoesUserFollowOtherUsersResponse {
  repeated .chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.FollowStatusEntry follow_status = 1;
  message FollowStatusEntry {
  optional string key = 1;
  optional bool value = 2;
  }
}

```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09609"></a>
## FND-09609: message declaration: chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.FollowStatusEntry

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message FollowStatusEntry {

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 746.

```text
d .chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.FollowStatusEntry follow_status = 1;
  message FollowStatusEntry {
  optional string key = 1;
  optional bool value = 2;
  }
}

```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09610"></a>
## FND-09610: chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.FollowStatusEntry.key = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string key = 1;

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 776.

```text
esUserFollowOtherUsersResponse.FollowStatusEntry follow_status = 1;
  message FollowStatusEntry {
  optional string key = 1;
  optional bool value = 2;
  }
}

```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09611"></a>
## FND-09611: chesscom.user_profile.v1.DoesUserFollowOtherUsersResponse.FollowStatusEntry.value = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool value = 2;

### Evidence

- **SRC-0598** `research/proto/chesscom/user_profile/v1/social_service.proto` — [preserved redacted evidence](../evidence/text/96833b1a9f0de356f1dfd4ae36c274cf690d06ba181f01c58ba1fbadd891bef2.proto)
  Character offset 803.

```text
nse.FollowStatusEntry follow_status = 1;
  message FollowStatusEntry {
  optional string key = 1;
  optional bool value = 2;
  }
}

```

**Source references:** SRC-0598, SRC-1569  
**URL references:** None independently associated  
**Related findings:** FND-09595, FND-09596, FND-09597

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09612"></a>
## FND-09612: message declaration: chesscom.user_properties.v1.GetPropertiesForAuthenticatedUserRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetPropertiesForAuthenticatedUserRequest {

### Evidence

- **SRC-0599** `research/proto/chesscom/user_properties/v1/authenticated_properties_service.proto` — [preserved redacted evidence](../evidence/text/f8a30c6383c94996adbf5602c11cb9fbf020f372321146ed945de3140047ce4f.proto)
  Character offset 135.

```text
/v1/authenticated_properties_service.proto
// syntax: proto3

package chesscom.user_properties.v1;

message GetPropertiesForAuthenticatedUserRequest {
  repeated .chesscom.user_properties.v1.Definitions properties = 1;
}

message GetPropertiesForAuthenticatedUserResponse {
  optional .chesscom.user_properties.v1.PropertiesByUser user_properties = 1;
}

```

**Source references:** SRC-0599, SRC-1570  
**URL references:** None independently associated  
**Related findings:** FND-09613, FND-09614

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09613"></a>
## FND-09613: chesscom.user_properties.v1.GetPropertiesForAuthenticatedUserRequest.properties = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.user_properties.v1.Definitions properties = 1;

### Evidence

- **SRC-0599** `research/proto/chesscom/user_properties/v1/authenticated_properties_service.proto` — [preserved redacted evidence](../evidence/text/f8a30c6383c94996adbf5602c11cb9fbf020f372321146ed945de3140047ce4f.proto)
  Character offset 188.

```text
 proto3

package chesscom.user_properties.v1;

message GetPropertiesForAuthenticatedUserRequest {
  repeated .chesscom.user_properties.v1.Definitions properties = 1;
}

message GetPropertiesForAuthenticatedUserResponse {
  optional .chesscom.user_properties.v1.PropertiesByUser user_properties = 1;
}

```

**Source references:** SRC-0599, SRC-1570  
**URL references:** None independently associated  
**Related findings:** FND-09612, FND-09614

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09614"></a>
## FND-09614: message declaration: chesscom.user_properties.v1.GetPropertiesForAuthenticatedUserResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message GetPropertiesForAuthenticatedUserResponse {

### Evidence

- **SRC-0599** `research/proto/chesscom/user_properties/v1/authenticated_properties_service.proto` — [preserved redacted evidence](../evidence/text/f8a30c6383c94996adbf5602c11cb9fbf020f372321146ed945de3140047ce4f.proto)
  Character offset 257.

```text
orAuthenticatedUserRequest {
  repeated .chesscom.user_properties.v1.Definitions properties = 1;
}

message GetPropertiesForAuthenticatedUserResponse {
  optional .chesscom.user_properties.v1.PropertiesByUser user_properties = 1;
}

```

**Source references:** SRC-0599, SRC-1570  
**URL references:** None independently associated  
**Related findings:** FND-09612, FND-09613

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09615"></a>
## FND-09615: chesscom.user_properties.v1.GetPropertiesForAuthenticatedUserResponse.user_properties = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_properties.v1.PropertiesByUser user_properties = 1;

### Evidence

- **SRC-0599** `research/proto/chesscom/user_properties/v1/authenticated_properties_service.proto` — [preserved redacted evidence](../evidence/text/f8a30c6383c94996adbf5602c11cb9fbf020f372321146ed945de3140047ce4f.proto)
  Character offset 311.

```text
_properties.v1.Definitions properties = 1;
}

message GetPropertiesForAuthenticatedUserResponse {
  optional .chesscom.user_properties.v1.PropertiesByUser user_properties = 1;
}

```

**Source references:** SRC-0599, SRC-1570  
**URL references:** None independently associated  
**Related findings:** FND-09612, FND-09613, FND-09614

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09616"></a>
## FND-09616: message declaration: chesscom.user_properties.v1.PropertiesByUser

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message PropertiesByUser {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 113.

```text
esscom/user_properties/v1/properties.proto
// syntax: proto3

package chesscom.user_properties.v1;

message PropertiesByUser {
  oneof _time_windows_properties {
  .chesscom.user_properties.v1.TimeWindowsPropertiesData time_windows_properties = 3;
  }
  optional string user = 1;
  optional .chesscom.user_properties.v1.Properties properties = 2;
}

message Properties {
  oneof _core {
  .chesscom.user_properties.v1.Co
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09617"></a>
## FND-09617: oneof declaration: chesscom.user_properties.v1.PropertiesByUser._time_windows_properties

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _time_windows_properties {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 142.

```text
perties.proto
// syntax: proto3

package chesscom.user_properties.v1;

message PropertiesByUser {
  oneof _time_windows_properties {
  .chesscom.user_properties.v1.TimeWindowsPropertiesData time_windows_properties = 3;
  }
  optional string user = 1;
  optional .chesscom.user_properties.v1.Properties properties = 2;
}

message Properties {
  oneof _core {
  .chesscom.user_properties.v1.CoreProperty core = 1;
  }
  on
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09618"></a>
## FND-09618: chesscom.user_properties.v1.PropertiesByUser.time_windows_properties = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.TimeWindowsPropertiesData time_windows_properties = 3;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 177.

```text
ckage chesscom.user_properties.v1;

message PropertiesByUser {
  oneof _time_windows_properties {
  .chesscom.user_properties.v1.TimeWindowsPropertiesData time_windows_properties = 3;
  }
  optional string user = 1;
  optional .chesscom.user_properties.v1.Properties properties = 2;
}

message Properties {
  oneof _core {
  .chesscom.user_properties.v1.CoreProperty core = 1;
  }
  oneof _pii {
  .chesscom.user_propert
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09619"></a>
## FND-09619: chesscom.user_properties.v1.PropertiesByUser.user = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user = 1;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 267.

```text
rties {
  .chesscom.user_properties.v1.TimeWindowsPropertiesData time_windows_properties = 3;
  }
  optional string user = 1;
  optional .chesscom.user_properties.v1.Properties properties = 2;
}

message Properties {
  oneof _core {
  .chesscom.user_properties.v1.CoreProperty core = 1;
  }
  oneof _pii {
  .chesscom.user_properties.v1.PIIProperty pii = 2;
  }
  oneof _user_details {
  .chesscom.user_properties.v1.Use
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09620"></a>
## FND-09620: chesscom.user_properties.v1.PropertiesByUser.properties = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.user_properties.v1.Properties properties = 2;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 295.

```text
perties.v1.TimeWindowsPropertiesData time_windows_properties = 3;
  }
  optional string user = 1;
  optional .chesscom.user_properties.v1.Properties properties = 2;
}

message Properties {
  oneof _core {
  .chesscom.user_properties.v1.CoreProperty core = 1;
  }
  oneof _pii {
  .chesscom.user_properties.v1.PIIProperty pii = 2;
  }
  oneof _user_details {
  .chesscom.user_properties.v1.UserDetailsProperty user_detail
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09621"></a>
## FND-09621: message declaration: chesscom.user_properties.v1.Properties

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message Properties {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 363.

```text
}
  optional string user = 1;
  optional .chesscom.user_properties.v1.Properties properties = 2;
}

message Properties {
  oneof _core {
  .chesscom.user_properties.v1.CoreProperty core = 1;
  }
  oneof _pii {
  .chesscom.user_properties.v1.PIIProperty pii = 2;
  }
  oneof _user_details {
  .chesscom.user_properties.v1.UserDetailsProperty user_details = 3;
  }
  oneof _roles {
  .chesscom.user_properties.v1.RolesProp
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09622"></a>
## FND-09622: oneof declaration: chesscom.user_properties.v1.Properties._core

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _core {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 386.

```text
r = 1;
  optional .chesscom.user_properties.v1.Properties properties = 2;
}

message Properties {
  oneof _core {
  .chesscom.user_properties.v1.CoreProperty core = 1;
  }
  oneof _pii {
  .chesscom.user_properties.v1.PIIProperty pii = 2;
  }
  oneof _user_details {
  .chesscom.user_properties.v1.UserDetailsProperty user_details = 3;
  }
  oneof _roles {
  .chesscom.user_properties.v1.RolesProperty roles = 4;
  }
  o
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09623"></a>
## FND-09623: chesscom.user_properties.v1.Properties.core = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.CoreProperty core = 1;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 402.

```text
l .chesscom.user_properties.v1.Properties properties = 2;
}

message Properties {
  oneof _core {
  .chesscom.user_properties.v1.CoreProperty core = 1;
  }
  oneof _pii {
  .chesscom.user_properties.v1.PIIProperty pii = 2;
  }
  oneof _user_details {
  .chesscom.user_properties.v1.UserDetailsProperty user_details = 3;
  }
  oneof _roles {
  .chesscom.user_properties.v1.RolesProperty roles = 4;
  }
  oneof _activity {
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09624"></a>
## FND-09624: oneof declaration: chesscom.user_properties.v1.Properties._pii

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _pii {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 460.

```text
}

message Properties {
  oneof _core {
  .chesscom.user_properties.v1.CoreProperty core = 1;
  }
  oneof _pii {
  .chesscom.user_properties.v1.PIIProperty pii = 2;
  }
  oneof _user_details {
  .chesscom.user_properties.v1.UserDetailsProperty user_details = 3;
  }
  oneof _roles {
  .chesscom.user_properties.v1.RolesProperty roles = 4;
  }
  oneof _activity {
  .chesscom.user_properties.v1.ActivityProperty activity 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09625"></a>
## FND-09625: chesscom.user_properties.v1.Properties.pii = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PIIProperty pii = 2;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 475.

```text
erties {
  oneof _core {
  .chesscom.user_properties.v1.CoreProperty core = 1;
  }
  oneof _pii {
  .chesscom.user_properties.v1.PIIProperty pii = 2;
  }
  oneof _user_details {
  .chesscom.user_properties.v1.UserDetailsProperty user_details = 3;
  }
  oneof _roles {
  .chesscom.user_properties.v1.RolesProperty roles = 4;
  }
  oneof _activity {
  .chesscom.user_properties.v1.ActivityProperty activity = 5;
  }
  oneo
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09626"></a>
## FND-09626: oneof declaration: chesscom.user_properties.v1.Properties._user_details

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_details {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 531.

```text
CoreProperty core = 1;
  }
  oneof _pii {
  .chesscom.user_properties.v1.PIIProperty pii = 2;
  }
  oneof _user_details {
  .chesscom.user_properties.v1.UserDetailsProperty user_details = 3;
  }
  oneof _roles {
  .chesscom.user_properties.v1.RolesProperty roles = 4;
  }
  oneof _activity {
  .chesscom.user_properties.v1.ActivityProperty activity = 5;
  }
  oneof _subscription {
  .chesscom.user_properties.v1.Subscri
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09627"></a>
## FND-09627: chesscom.user_properties.v1.Properties.user_details = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.UserDetailsProperty user_details = 3;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 555.

```text
 }
  oneof _pii {
  .chesscom.user_properties.v1.PIIProperty pii = 2;
  }
  oneof _user_details {
  .chesscom.user_properties.v1.UserDetailsProperty user_details = 3;
  }
  oneof _roles {
  .chesscom.user_properties.v1.RolesProperty roles = 4;
  }
  oneof _activity {
  .chesscom.user_properties.v1.ActivityProperty activity = 5;
  }
  oneof _subscription {
  .chesscom.user_properties.v1.SubscriptionProperty subscripti
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09628"></a>
## FND-09628: oneof declaration: chesscom.user_properties.v1.Properties._roles

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _roles {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 628.

```text

  oneof _user_details {
  .chesscom.user_properties.v1.UserDetailsProperty user_details = 3;
  }
  oneof _roles {
  .chesscom.user_properties.v1.RolesProperty roles = 4;
  }
  oneof _activity {
  .chesscom.user_properties.v1.ActivityProperty activity = 5;
  }
  oneof _subscription {
  .chesscom.user_properties.v1.SubscriptionProperty subscription = 6;
  }
  oneof _attribution_signup_initial {
  .chesscom.user_proper
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09629"></a>
## FND-09629: chesscom.user_properties.v1.Properties.roles = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.RolesProperty roles = 4;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 645.

```text
tails {
  .chesscom.user_properties.v1.UserDetailsProperty user_details = 3;
  }
  oneof _roles {
  .chesscom.user_properties.v1.RolesProperty roles = 4;
  }
  oneof _activity {
  .chesscom.user_properties.v1.ActivityProperty activity = 5;
  }
  oneof _subscription {
  .chesscom.user_properties.v1.SubscriptionProperty subscription = 6;
  }
  oneof _attribution_signup_initial {
  .chesscom.user_properties.v1.Attributi
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09630"></a>
## FND-09630: oneof declaration: chesscom.user_properties.v1.Properties._activity

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _activity {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 705.

```text
ser_details = 3;
  }
  oneof _roles {
  .chesscom.user_properties.v1.RolesProperty roles = 4;
  }
  oneof _activity {
  .chesscom.user_properties.v1.ActivityProperty activity = 5;
  }
  oneof _subscription {
  .chesscom.user_properties.v1.SubscriptionProperty subscription = 6;
  }
  oneof _attribution_signup_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_signup_initial = 7;
  }
  oneof _attr
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09631"></a>
## FND-09631: chesscom.user_properties.v1.Properties.activity = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.ActivityProperty activity = 5;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 725.

```text

  oneof _roles {
  .chesscom.user_properties.v1.RolesProperty roles = 4;
  }
  oneof _activity {
  .chesscom.user_properties.v1.ActivityProperty activity = 5;
  }
  oneof _subscription {
  .chesscom.user_properties.v1.SubscriptionProperty subscription = 6;
  }
  oneof _attribution_signup_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_signup_initial = 7;
  }
  oneof _attribution_signup_last 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09632"></a>
## FND-09632: oneof declaration: chesscom.user_properties.v1.Properties._subscription

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _subscription {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 791.

```text
es = 4;
  }
  oneof _activity {
  .chesscom.user_properties.v1.ActivityProperty activity = 5;
  }
  oneof _subscription {
  .chesscom.user_properties.v1.SubscriptionProperty subscription = 6;
  }
  oneof _attribution_signup_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_signup_initial = 7;
  }
  oneof _attribution_signup_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_s
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09633"></a>
## FND-09633: chesscom.user_properties.v1.Properties.subscription = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.SubscriptionProperty subscription = 6;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 815.

```text
ivity {
  .chesscom.user_properties.v1.ActivityProperty activity = 5;
  }
  oneof _subscription {
  .chesscom.user_properties.v1.SubscriptionProperty subscription = 6;
  }
  oneof _attribution_signup_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_signup_initial = 7;
  }
  oneof _attribution_signup_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_signup_last = 8;
  }
  on
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09634"></a>
## FND-09634: oneof declaration: chesscom.user_properties.v1.Properties._attribution_signup_initial

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _attribution_signup_initial {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 889.

```text
  oneof _subscription {
  .chesscom.user_properties.v1.SubscriptionProperty subscription = 6;
  }
  oneof _attribution_signup_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_signup_initial = 7;
  }
  oneof _attribution_signup_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_signup_last = 8;
  }
  oneof _attribution_trial_initial {
  .chesscom.user_properties.v1.Attributio
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09635"></a>
## FND-09635: chesscom.user_properties.v1.Properties.attribution_signup_initial = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AttributionProperty attribution_signup_initial = 7;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 927.

```text
er_properties.v1.SubscriptionProperty subscription = 6;
  }
  oneof _attribution_signup_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_signup_initial = 7;
  }
  oneof _attribution_signup_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_signup_last = 8;
  }
  oneof _attribution_trial_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_trial_initial = 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09636"></a>
## FND-09636: oneof declaration: chesscom.user_properties.v1.Properties._attribution_signup_last

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _attribution_signup_last {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1014.

```text
_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_signup_initial = 7;
  }
  oneof _attribution_signup_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_signup_last = 8;
  }
  oneof _attribution_trial_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_trial_initial = 9;
  }
  oneof _attribution_trial_last {
  .chesscom.user_properties.v1.AttributionProp
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09637"></a>
## FND-09637: chesscom.user_properties.v1.Properties.attribution_signup_last = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AttributionProperty attribution_signup_last = 8;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1049.

```text
ies.v1.AttributionProperty attribution_signup_initial = 7;
  }
  oneof _attribution_signup_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_signup_last = 8;
  }
  oneof _attribution_trial_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_trial_initial = 9;
  }
  oneof _attribution_trial_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_trial_last = 10;
 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09638"></a>
## FND-09638: oneof declaration: chesscom.user_properties.v1.Properties._attribution_trial_initial

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _attribution_trial_initial {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1133.

```text
signup_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_signup_last = 8;
  }
  oneof _attribution_trial_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_trial_initial = 9;
  }
  oneof _attribution_trial_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_trial_last = 10;
  }
  oneof _ratings {
  .chesscom.user_properties.v1.RatingsProperty ratings = 11;
 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09639"></a>
## FND-09639: chesscom.user_properties.v1.Properties.attribution_trial_initial = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AttributionProperty attribution_trial_initial = 9;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1170.

```text
ties.v1.AttributionProperty attribution_signup_last = 8;
  }
  oneof _attribution_trial_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_trial_initial = 9;
  }
  oneof _attribution_trial_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_trial_last = 10;
  }
  oneof _ratings {
  .chesscom.user_properties.v1.RatingsProperty ratings = 11;
  }
  oneof _wdl {
  .chesscom.user_pr
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09640"></a>
## FND-09640: oneof declaration: chesscom.user_properties.v1.Properties._attribution_trial_last

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _attribution_trial_last {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1256.

```text
l_initial {
  .chesscom.user_properties.v1.AttributionProperty attribution_trial_initial = 9;
  }
  oneof _attribution_trial_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_trial_last = 10;
  }
  oneof _ratings {
  .chesscom.user_properties.v1.RatingsProperty ratings = 11;
  }
  oneof _wdl {
  .chesscom.user_properties.v1.WDLProperty wdl = 12;
  }
  oneof _analysis {
  .chesscom.user_properties.
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09641"></a>
## FND-09641: chesscom.user_properties.v1.Properties.attribution_trial_last = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AttributionProperty attribution_trial_last = 10;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1290.

```text
rties.v1.AttributionProperty attribution_trial_initial = 9;
  }
  oneof _attribution_trial_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_trial_last = 10;
  }
  oneof _ratings {
  .chesscom.user_properties.v1.RatingsProperty ratings = 11;
  }
  oneof _wdl {
  .chesscom.user_properties.v1.WDLProperty wdl = 12;
  }
  oneof _analysis {
  .chesscom.user_properties.v1.AnalysisProperty analysis = 13;
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09642"></a>
## FND-09642: oneof declaration: chesscom.user_properties.v1.Properties._ratings

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _ratings {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1374.

```text
_trial_last {
  .chesscom.user_properties.v1.AttributionProperty attribution_trial_last = 10;
  }
  oneof _ratings {
  .chesscom.user_properties.v1.RatingsProperty ratings = 11;
  }
  oneof _wdl {
  .chesscom.user_properties.v1.WDLProperty wdl = 12;
  }
  oneof _analysis {
  .chesscom.user_properties.v1.AnalysisProperty analysis = 13;
  }
  oneof _settings_daily_chess {
  .chesscom.user_properties.v1.SettingsDailyChe
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09643"></a>
## FND-09643: chesscom.user_properties.v1.Properties.ratings = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.RatingsProperty ratings = 11;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1393.

```text
esscom.user_properties.v1.AttributionProperty attribution_trial_last = 10;
  }
  oneof _ratings {
  .chesscom.user_properties.v1.RatingsProperty ratings = 11;
  }
  oneof _wdl {
  .chesscom.user_properties.v1.WDLProperty wdl = 12;
  }
  oneof _analysis {
  .chesscom.user_properties.v1.AnalysisProperty analysis = 13;
  }
  oneof _settings_daily_chess {
  .chesscom.user_properties.v1.SettingsDailyChessProperty settings
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09644"></a>
## FND-09644: oneof declaration: chesscom.user_properties.v1.Properties._wdl

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _wdl {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1458.

```text
ast = 10;
  }
  oneof _ratings {
  .chesscom.user_properties.v1.RatingsProperty ratings = 11;
  }
  oneof _wdl {
  .chesscom.user_properties.v1.WDLProperty wdl = 12;
  }
  oneof _analysis {
  .chesscom.user_properties.v1.AnalysisProperty analysis = 13;
  }
  oneof _settings_daily_chess {
  .chesscom.user_properties.v1.SettingsDailyChessProperty settings_daily_chess = 14;
  }
  oneof _settings_live_chess {
  .chesscom
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09645"></a>
## FND-09645: chesscom.user_properties.v1.Properties.wdl = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.WDLProperty wdl = 12;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1473.

```text
 oneof _ratings {
  .chesscom.user_properties.v1.RatingsProperty ratings = 11;
  }
  oneof _wdl {
  .chesscom.user_properties.v1.WDLProperty wdl = 12;
  }
  oneof _analysis {
  .chesscom.user_properties.v1.AnalysisProperty analysis = 13;
  }
  oneof _settings_daily_chess {
  .chesscom.user_properties.v1.SettingsDailyChessProperty settings_daily_chess = 14;
  }
  oneof _settings_live_chess {
  .chesscom.user_propertie
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09646"></a>
## FND-09646: oneof declaration: chesscom.user_properties.v1.Properties._analysis

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _analysis {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1530.

```text
roperty ratings = 11;
  }
  oneof _wdl {
  .chesscom.user_properties.v1.WDLProperty wdl = 12;
  }
  oneof _analysis {
  .chesscom.user_properties.v1.AnalysisProperty analysis = 13;
  }
  oneof _settings_daily_chess {
  .chesscom.user_properties.v1.SettingsDailyChessProperty settings_daily_chess = 14;
  }
  oneof _settings_live_chess {
  .chesscom.user_properties.v1.SettingsLiveChessProperty settings_live_chess = 15;

```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09647"></a>
## FND-09647: chesscom.user_properties.v1.Properties.analysis = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.AnalysisProperty analysis = 13;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1550.

```text
;
  }
  oneof _wdl {
  .chesscom.user_properties.v1.WDLProperty wdl = 12;
  }
  oneof _analysis {
  .chesscom.user_properties.v1.AnalysisProperty analysis = 13;
  }
  oneof _settings_daily_chess {
  .chesscom.user_properties.v1.SettingsDailyChessProperty settings_daily_chess = 14;
  }
  oneof _settings_live_chess {
  .chesscom.user_properties.v1.SettingsLiveChessProperty settings_live_chess = 15;
  }
  oneof _stats_d
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09648"></a>
## FND-09648: oneof declaration: chesscom.user_properties.v1.Properties._settings_daily_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _settings_daily_chess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1617.

```text
 = 12;
  }
  oneof _analysis {
  .chesscom.user_properties.v1.AnalysisProperty analysis = 13;
  }
  oneof _settings_daily_chess {
  .chesscom.user_properties.v1.SettingsDailyChessProperty settings_daily_chess = 14;
  }
  oneof _settings_live_chess {
  .chesscom.user_properties.v1.SettingsLiveChessProperty settings_live_chess = 15;
  }
  oneof _stats_daily_chess {
  .chesscom.user_properties.v1.StatsDailyProperty stat
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09649"></a>
## FND-09649: chesscom.user_properties.v1.Properties.settings_daily_chess = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.SettingsDailyChessProperty settings_daily_chess = 14;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1649.

```text
 .chesscom.user_properties.v1.AnalysisProperty analysis = 13;
  }
  oneof _settings_daily_chess {
  .chesscom.user_properties.v1.SettingsDailyChessProperty settings_daily_chess = 14;
  }
  oneof _settings_live_chess {
  .chesscom.user_properties.v1.SettingsLiveChessProperty settings_live_chess = 15;
  }
  oneof _stats_daily_chess {
  .chesscom.user_properties.v1.StatsDailyProperty stats_daily_chess = 16;
  }
  oneof 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09650"></a>
## FND-09650: oneof declaration: chesscom.user_properties.v1.Properties._settings_live_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _settings_live_chess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1738.

```text
_chess {
  .chesscom.user_properties.v1.SettingsDailyChessProperty settings_daily_chess = 14;
  }
  oneof _settings_live_chess {
  .chesscom.user_properties.v1.SettingsLiveChessProperty settings_live_chess = 15;
  }
  oneof _stats_daily_chess {
  .chesscom.user_properties.v1.StatsDailyProperty stats_daily_chess = 16;
  }
  oneof _stats_daily_chess960 {
  .chesscom.user_properties.v1.StatsDailyChess960Property stats_d
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09651"></a>
## FND-09651: chesscom.user_properties.v1.Properties.settings_live_chess = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.SettingsLiveChessProperty settings_live_chess = 15;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1769.

```text
rties.v1.SettingsDailyChessProperty settings_daily_chess = 14;
  }
  oneof _settings_live_chess {
  .chesscom.user_properties.v1.SettingsLiveChessProperty settings_live_chess = 15;
  }
  oneof _stats_daily_chess {
  .chesscom.user_properties.v1.StatsDailyProperty stats_daily_chess = 16;
  }
  oneof _stats_daily_chess960 {
  .chesscom.user_properties.v1.StatsDailyChess960Property stats_daily_chess960 = 17;
  }
  oneof
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09652"></a>
## FND-09652: oneof declaration: chesscom.user_properties.v1.Properties._stats_daily_chess

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _stats_daily_chess {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1856.

```text
ve_chess {
  .chesscom.user_properties.v1.SettingsLiveChessProperty settings_live_chess = 15;
  }
  oneof _stats_daily_chess {
  .chesscom.user_properties.v1.StatsDailyProperty stats_daily_chess = 16;
  }
  oneof _stats_daily_chess960 {
  .chesscom.user_properties.v1.StatsDailyChess960Property stats_daily_chess960 = 17;
  }
  oneof _stats_live_chess_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09653"></a>
## FND-09653: chesscom.user_properties.v1.Properties.stats_daily_chess = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsDailyProperty stats_daily_chess = 16;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1885.

```text
roperties.v1.SettingsLiveChessProperty settings_live_chess = 15;
  }
  oneof _stats_daily_chess {
  .chesscom.user_properties.v1.StatsDailyProperty stats_daily_chess = 16;
  }
  oneof _stats_daily_chess960 {
  .chesscom.user_properties.v1.StatsDailyChess960Property stats_daily_chess960 = 17;
  }
  oneof _stats_live_chess_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_bullet = 18;
  }
  one
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09654"></a>
## FND-09654: oneof declaration: chesscom.user_properties.v1.Properties._stats_daily_chess960

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _stats_daily_chess960 {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1963.

```text
stats_daily_chess {
  .chesscom.user_properties.v1.StatsDailyProperty stats_daily_chess = 16;
  }
  oneof _stats_daily_chess960 {
  .chesscom.user_properties.v1.StatsDailyChess960Property stats_daily_chess960 = 17;
  }
  oneof _stats_live_chess_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_bullet = 18;
  }
  oneof _stats_live_chess_blitz {
  .chesscom.user_properties.v1.StatsLiveProperty 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09655"></a>
## FND-09655: chesscom.user_properties.v1.Properties.stats_daily_chess960 = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsDailyChess960Property stats_daily_chess960 = 17;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 1995.

```text
user_properties.v1.StatsDailyProperty stats_daily_chess = 16;
  }
  oneof _stats_daily_chess960 {
  .chesscom.user_properties.v1.StatsDailyChess960Property stats_daily_chess960 = 17;
  }
  oneof _stats_live_chess_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_bullet = 18;
  }
  oneof _stats_live_chess_blitz {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_blitz = 19;
  }
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09656"></a>
## FND-09656: oneof declaration: chesscom.user_properties.v1.Properties._stats_live_chess_bullet

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _stats_live_chess_bullet {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2084.

```text
ess960 {
  .chesscom.user_properties.v1.StatsDailyChess960Property stats_daily_chess960 = 17;
  }
  oneof _stats_live_chess_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_bullet = 18;
  }
  oneof _stats_live_chess_blitz {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_blitz = 19;
  }
  oneof _stats_live_chess_rapid {
  .chesscom.user_properties.v1.StatsLiveProperty stats
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09657"></a>
## FND-09657: chesscom.user_properties.v1.Properties.stats_live_chess_bullet = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_bullet = 18;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2119.

```text
s.v1.StatsDailyChess960Property stats_daily_chess960 = 17;
  }
  oneof _stats_live_chess_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_bullet = 18;
  }
  oneof _stats_live_chess_blitz {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_blitz = 19;
  }
  oneof _stats_live_chess_rapid {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_rapid = 20;
  }
  oneof
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09658"></a>
## FND-09658: oneof declaration: chesscom.user_properties.v1.Properties._stats_live_chess_blitz

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _stats_live_chess_blitz {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2202.

```text
chess_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_bullet = 18;
  }
  oneof _stats_live_chess_blitz {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_blitz = 19;
  }
  oneof _stats_live_chess_rapid {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_rapid = 20;
  }
  oneof _stats_live_chess960_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty sta
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09659"></a>
## FND-09659: chesscom.user_properties.v1.Properties.stats_live_chess_blitz = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_blitz = 19;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2236.

```text
operties.v1.StatsLiveProperty stats_live_chess_bullet = 18;
  }
  oneof _stats_live_chess_blitz {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_blitz = 19;
  }
  oneof _stats_live_chess_rapid {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_rapid = 20;
  }
  oneof _stats_live_chess960_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_bullet = 21;
  }

```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09660"></a>
## FND-09660: oneof declaration: chesscom.user_properties.v1.Properties._stats_live_chess_rapid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _stats_live_chess_rapid {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2318.

```text
e_chess_blitz {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_blitz = 19;
  }
  oneof _stats_live_chess_rapid {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_rapid = 20;
  }
  oneof _stats_live_chess960_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_bullet = 21;
  }
  oneof _stats_live_chess960_blitz {
  .chesscom.user_properties.v1.StatsLivePrope
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09661"></a>
## FND-09661: chesscom.user_properties.v1.Properties.stats_live_chess_rapid = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_rapid = 20;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2352.

```text
roperties.v1.StatsLiveProperty stats_live_chess_blitz = 19;
  }
  oneof _stats_live_chess_rapid {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_rapid = 20;
  }
  oneof _stats_live_chess960_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_bullet = 21;
  }
  oneof _stats_live_chess960_blitz {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_blitz = 22
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09662"></a>
## FND-09662: oneof declaration: chesscom.user_properties.v1.Properties._stats_live_chess960_bullet

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _stats_live_chess960_bullet {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2434.

```text
e_chess_rapid {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess_rapid = 20;
  }
  oneof _stats_live_chess960_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_bullet = 21;
  }
  oneof _stats_live_chess960_blitz {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_blitz = 22;
  }
  oneof _stats_live_chess960_rapid {
  .chesscom.user_properties.v1.StatsLiv
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09663"></a>
## FND-09663: chesscom.user_properties.v1.Properties.stats_live_chess960_bullet = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_bullet = 21;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2472.

```text
rties.v1.StatsLiveProperty stats_live_chess_rapid = 20;
  }
  oneof _stats_live_chess960_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_bullet = 21;
  }
  oneof _stats_live_chess960_blitz {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_blitz = 22;
  }
  oneof _stats_live_chess960_rapid {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_rapid = 
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09664"></a>
## FND-09664: oneof declaration: chesscom.user_properties.v1.Properties._stats_live_chess960_blitz

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _stats_live_chess960_blitz {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2558.

```text
60_bullet {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_bullet = 21;
  }
  oneof _stats_live_chess960_blitz {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_blitz = 22;
  }
  oneof _stats_live_chess960_rapid {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_rapid = 23;
  }
  oneof _stats_live_bughouse {
  .chesscom.user_properties.v1.StatsLivePropert
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09665"></a>
## FND-09665: chesscom.user_properties.v1.Properties.stats_live_chess960_blitz = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_blitz = 22;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2595.

```text
es.v1.StatsLiveProperty stats_live_chess960_bullet = 21;
  }
  oneof _stats_live_chess960_blitz {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_blitz = 22;
  }
  oneof _stats_live_chess960_rapid {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_rapid = 23;
  }
  oneof _stats_live_bughouse {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_bughouse = 24;
  }
  one
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09666"></a>
## FND-09666: oneof declaration: chesscom.user_properties.v1.Properties._stats_live_chess960_rapid

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _stats_live_chess960_rapid {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2680.

```text
s960_blitz {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_blitz = 22;
  }
  oneof _stats_live_chess960_rapid {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_rapid = 23;
  }
  oneof _stats_live_bughouse {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_bughouse = 24;
  }
  oneof _user_settings {
  .chesscom.user_properties.v1.UserSettingsProperty user_settings
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09667"></a>
## FND-09667: chesscom.user_properties.v1.Properties.stats_live_chess960_rapid = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_rapid = 23;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2717.

```text
ies.v1.StatsLiveProperty stats_live_chess960_blitz = 22;
  }
  oneof _stats_live_chess960_rapid {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_rapid = 23;
  }
  oneof _stats_live_bughouse {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_bughouse = 24;
  }
  oneof _user_settings {
  .chesscom.user_properties.v1.UserSettingsProperty user_settings = 25;
  }
  oneof _puzzles_attempted
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09668"></a>
## FND-09668: oneof declaration: chesscom.user_properties.v1.Properties._stats_live_bughouse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _stats_live_bughouse {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2802.

```text
s960_rapid {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_chess960_rapid = 23;
  }
  oneof _stats_live_bughouse {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_bughouse = 24;
  }
  oneof _user_settings {
  .chesscom.user_properties.v1.UserSettingsProperty user_settings = 25;
  }
  oneof _puzzles_attempted {
  .chesscom.user_properties.v1.PuzzlesAttemptedProperty puzzles_attempted = 26;
  
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09669"></a>
## FND-09669: chesscom.user_properties.v1.Properties.stats_live_bughouse = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.StatsLiveProperty stats_live_bughouse = 24;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2833.

```text
roperties.v1.StatsLiveProperty stats_live_chess960_rapid = 23;
  }
  oneof _stats_live_bughouse {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_bughouse = 24;
  }
  oneof _user_settings {
  .chesscom.user_properties.v1.UserSettingsProperty user_settings = 25;
  }
  oneof _puzzles_attempted {
  .chesscom.user_properties.v1.PuzzlesAttemptedProperty puzzles_attempted = 26;
  }
  oneof _clubs {
  .chesscom.
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09670"></a>
## FND-09670: oneof declaration: chesscom.user_properties.v1.Properties._user_settings

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _user_settings {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2912.

```text
ts_live_bughouse {
  .chesscom.user_properties.v1.StatsLiveProperty stats_live_bughouse = 24;
  }
  oneof _user_settings {
  .chesscom.user_properties.v1.UserSettingsProperty user_settings = 25;
  }
  oneof _puzzles_attempted {
  .chesscom.user_properties.v1.PuzzlesAttemptedProperty puzzles_attempted = 26;
  }
  oneof _clubs {
  .chesscom.user_properties.v1.ClubsProperty clubs = 27;
  }
  oneof _puzzle_battle {
  .ch
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09671"></a>
## FND-09671: chesscom.user_properties.v1.Properties.user_settings = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.UserSettingsProperty user_settings = 25;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 2937.

```text
sscom.user_properties.v1.StatsLiveProperty stats_live_bughouse = 24;
  }
  oneof _user_settings {
  .chesscom.user_properties.v1.UserSettingsProperty user_settings = 25;
  }
  oneof _puzzles_attempted {
  .chesscom.user_properties.v1.PuzzlesAttemptedProperty puzzles_attempted = 26;
  }
  oneof _clubs {
  .chesscom.user_properties.v1.ClubsProperty clubs = 27;
  }
  oneof _puzzle_battle {
  .chesscom.user_properties.v1
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09672"></a>
## FND-09672: oneof declaration: chesscom.user_properties.v1.Properties._puzzles_attempted

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _puzzles_attempted {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3013.

```text
neof _user_settings {
  .chesscom.user_properties.v1.UserSettingsProperty user_settings = 25;
  }
  oneof _puzzles_attempted {
  .chesscom.user_properties.v1.PuzzlesAttemptedProperty puzzles_attempted = 26;
  }
  oneof _clubs {
  .chesscom.user_properties.v1.ClubsProperty clubs = 27;
  }
  oneof _puzzle_battle {
  .chesscom.user_properties.v1.PuzzleBattleProperty puzzle_battle = 28;
  }
  oneof _audiences {
  .chessc
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-09673"></a>
## FND-09673: chesscom.user_properties.v1.Properties.puzzles_attempted = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

.chesscom.user_properties.v1.PuzzlesAttemptedProperty puzzles_attempted = 26;

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3042.

```text
scom.user_properties.v1.UserSettingsProperty user_settings = 25;
  }
  oneof _puzzles_attempted {
  .chesscom.user_properties.v1.PuzzlesAttemptedProperty puzzles_attempted = 26;
  }
  oneof _clubs {
  .chesscom.user_properties.v1.ClubsProperty clubs = 27;
  }
  oneof _puzzle_battle {
  .chesscom.user_properties.v1.PuzzleBattleProperty puzzle_battle = 28;
  }
  oneof _audiences {
  .chesscom.user_properties.v1.Audienc
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-09674"></a>
## FND-09674: oneof declaration: chesscom.user_properties.v1.Properties._clubs

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

oneof _clubs {

### Evidence

- **SRC-0600** `research/proto/chesscom/user_properties/v1/properties.proto` — [preserved redacted evidence](../evidence/text/6c6769fbba872d6a61a8bdb2dc0a15cf4f5e94518a33ae6db530d4fdd7134222.proto)
  Character offset 3126.

```text
s_attempted {
  .chesscom.user_properties.v1.PuzzlesAttemptedProperty puzzles_attempted = 26;
  }
  oneof _clubs {
  .chesscom.user_properties.v1.ClubsProperty clubs = 27;
  }
  oneof _puzzle_battle {
  .chesscom.user_properties.v1.PuzzleBattleProperty puzzle_battle = 28;
  }
  oneof _audiences {
  .chesscom.user_properties.v1.AudiencesProperty audiences = 29;
  }
  oneof _user_abuse {
  .chesscom.user_properties.v1.
```

**Source references:** SRC-0600, SRC-1571  
**URL references:** None independently associated  
**Related findings:** FND-09616, FND-09617, FND-09618

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
