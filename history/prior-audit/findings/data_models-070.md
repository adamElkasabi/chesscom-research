# data_models — findings 6901–7000

[Master index](../00_MASTER_INDEX.md) · [All findings](FINDINGS_INDEX.md)

<a id="FND-07175"></a>
## FND-07175: chesscom.payments.v1.ClearFamilyPlanTrialCooldownRequest.verification_id = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string verification_id = 3;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 4724.

```text
anInvitationsRequest {
  optional string user_uuid = 1;
  repeated string invitee_user_uuids = 2;
  optional string verification_id = 3;
}

message GetFamilyPlanInvitationsResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanState plan_state = 1;
  optional int32 secondary_member_count = 2;
  optional int32 max_secondary_members = 3;
  repeated .chesscom.payments.v1.SupportFamilyPlanInvitation invitations = 4
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07176"></a>
## FND-07176: chesscom.payments.v1.ClearFamilyPlanTrialCooldownRequest.context = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionContext context = 4;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 5288.

```text
tring user_uuid = 1;
  optional string invitation_ref = 2;
  optional string verification_id = 3;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message RevokeFamilyPlanInvitationResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanRevokeResult result = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
}

message ClearFamilyPlanTrialCooldownRequest {
  optional st
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07177"></a>
## FND-07177: message declaration: chesscom.payments.v1.ClearFamilyPlanTrialCooldownResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message ClearFamilyPlanTrialCooldownResponse {

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 5777.

```text
al string verification_id = 3;
  optional .chesscom.support.v1.SupportActionContext context = 4;
}

message ClearFamilyPlanTrialCooldownResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanCooldownResult result = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
}

```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07178"></a>
## FND-07178: chesscom.payments.v1.ClearFamilyPlanTrialCooldownResponse.result = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SupportFamilyPlanCooldownResult result = 1;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 5826.

```text
om.support.v1.SupportActionContext context = 4;
}

message ClearFamilyPlanTrialCooldownResponse {
  optional .chesscom.payments.v1.SupportFamilyPlanCooldownResult result = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
}

```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07179"></a>
## FND-07179: chesscom.payments.v1.ClearFamilyPlanTrialCooldownResponse.action_result = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionResult action_result = 2;

### Evidence

- **SRC-0512** `research/proto/chesscom/payments/v1/subscription_admin_service.proto` — [preserved redacted evidence](../evidence/text/258cf675e8f2f39dbee2890bb0ca0dbe9bb7681ab939fe957b61e916235bdf71.proto)
  Character offset 1434.

```text
ing subscription_id = 4;
}

message ExtendSubscriptionResponse {
  optional int32 days_added = 1;
  optional .chesscom.support.v1.SupportActionResult action_result = 2;
  optional .google.protobuf.Timestamp current_period_ends_at = 3;
  optional .chesscom.payments.v1.SubscriptionAdminRefusalReason refusal_reason = 4;
}

message GrantGoodwillDiamondRequest {
  optional string user_uuid = 1;
  optional .chesscom.suppor
```

**Source references:** SRC-0512, SRC-1483  
**URL references:** None independently associated  
**Related findings:** FND-07066, FND-07067, FND-07068

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07180"></a>
## FND-07180: enum declaration: chesscom.payments.v1.SupportFamilyPlanState

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SupportFamilyPlanState {

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 108.

```text
e: chesscom/payments/v1/support_family_plan.proto
// syntax: proto3

package chesscom.payments.v1;

enum SupportFamilyPlanState {
  SUPPORT_FAMILY_PLAN_STATE_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_STATE_NONE = 1;
  SUPPORT_FAMILY_PLAN_STATE_TRIAL = 2;
  SUPPORT_FAMILY_PLAN_STATE_PAID = 3;
}

enum SupportFamilyPlanJoinStatus {
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_CAN_JOI
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07181"></a>
## FND-07181: chesscom.payments.v1.SupportFamilyPlanState.SUPPORT_FAMILY_PLAN_STATE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_STATE_UNSPECIFIED = 0;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 140.

```text
family_plan.proto
// syntax: proto3

package chesscom.payments.v1;

enum SupportFamilyPlanState {
  SUPPORT_FAMILY_PLAN_STATE_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_STATE_NONE = 1;
  SUPPORT_FAMILY_PLAN_STATE_TRIAL = 2;
  SUPPORT_FAMILY_PLAN_STATE_PAID = 3;
}

enum SupportFamilyPlanJoinStatus {
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_CAN_JOIN = 1;
  SUPPORT_FAMILY_PLAN_JOI
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07182"></a>
## FND-07182: chesscom.payments.v1.SupportFamilyPlanState.SUPPORT_FAMILY_PLAN_STATE_NONE = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_STATE_NONE = 1;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 185.

```text
chesscom.payments.v1;

enum SupportFamilyPlanState {
  SUPPORT_FAMILY_PLAN_STATE_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_STATE_NONE = 1;
  SUPPORT_FAMILY_PLAN_STATE_TRIAL = 2;
  SUPPORT_FAMILY_PLAN_STATE_PAID = 3;
}

enum SupportFamilyPlanJoinStatus {
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_CAN_JOIN = 1;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_TRIAL_COOLDOWN = 2;
  SUPPORT_FAMILY
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07183"></a>
## FND-07183: chesscom.payments.v1.SupportFamilyPlanState.SUPPORT_FAMILY_PLAN_STATE_TRIAL = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_STATE_TRIAL = 2;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 223.

```text
ilyPlanState {
  SUPPORT_FAMILY_PLAN_STATE_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_STATE_NONE = 1;
  SUPPORT_FAMILY_PLAN_STATE_TRIAL = 2;
  SUPPORT_FAMILY_PLAN_STATE_PAID = 3;
}

enum SupportFamilyPlanJoinStatus {
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_CAN_JOIN = 1;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_TRIAL_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_REMOVED_BY_OWNER = 3
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07184"></a>
## FND-07184: chesscom.payments.v1.SupportFamilyPlanState.SUPPORT_FAMILY_PLAN_STATE_PAID = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_STATE_PAID = 3;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 262.

```text
ATE_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_STATE_NONE = 1;
  SUPPORT_FAMILY_PLAN_STATE_TRIAL = 2;
  SUPPORT_FAMILY_PLAN_STATE_PAID = 3;
}

enum SupportFamilyPlanJoinStatus {
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_CAN_JOIN = 1;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_TRIAL_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_REMOVED_BY_OWNER = 3;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALR
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07185"></a>
## FND-07185: enum declaration: chesscom.payments.v1.SupportFamilyPlanJoinStatus

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SupportFamilyPlanJoinStatus {

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 301.

```text
LAN_STATE_NONE = 1;
  SUPPORT_FAMILY_PLAN_STATE_TRIAL = 2;
  SUPPORT_FAMILY_PLAN_STATE_PAID = 3;
}

enum SupportFamilyPlanJoinStatus {
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_CAN_JOIN = 1;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_TRIAL_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_REMOVED_BY_OWNER = 3;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_PREMIUM = 4;
  SUPPORT_FAMILY_PLAN
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07186"></a>
## FND-07186: chesscom.payments.v1.SupportFamilyPlanJoinStatus.SUPPORT_FAMILY_PLAN_JOIN_STATUS_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_JOIN_STATUS_UNSPECIFIED = 0;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 338.

```text
PLAN_STATE_TRIAL = 2;
  SUPPORT_FAMILY_PLAN_STATE_PAID = 3;
}

enum SupportFamilyPlanJoinStatus {
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_CAN_JOIN = 1;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_TRIAL_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_REMOVED_BY_OWNER = 3;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_PREMIUM = 4;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_OTHER_COUNTRY = 5;
  SUP
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07187"></a>
## FND-07187: chesscom.payments.v1.SupportFamilyPlanJoinStatus.SUPPORT_FAMILY_PLAN_JOIN_STATUS_CAN_JOIN = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_JOIN_STATUS_CAN_JOIN = 1;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 389.

```text
AID = 3;
}

enum SupportFamilyPlanJoinStatus {
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_CAN_JOIN = 1;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_TRIAL_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_REMOVED_BY_OWNER = 3;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_PREMIUM = 4;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_OTHER_COUNTRY = 5;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_PLAN_FULL = 6;
  SUPPO
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07188"></a>
## FND-07188: chesscom.payments.v1.SupportFamilyPlanJoinStatus.SUPPORT_FAMILY_PLAN_JOIN_STATUS_TRIAL_COOLDOWN = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_JOIN_STATUS_TRIAL_COOLDOWN = 2;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 437.

```text
 SUPPORT_FAMILY_PLAN_JOIN_STATUS_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_CAN_JOIN = 1;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_TRIAL_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_REMOVED_BY_OWNER = 3;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_PREMIUM = 4;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_OTHER_COUNTRY = 5;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_PLAN_FULL = 6;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_MEMBER = 7;
}
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07189"></a>
## FND-07189: chesscom.payments.v1.SupportFamilyPlanJoinStatus.SUPPORT_FAMILY_PLAN_JOIN_STATUS_REMOVED_BY_OWNER = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_JOIN_STATUS_REMOVED_BY_OWNER = 3;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 491.

```text
PPORT_FAMILY_PLAN_JOIN_STATUS_CAN_JOIN = 1;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_TRIAL_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_REMOVED_BY_OWNER = 3;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_PREMIUM = 4;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_OTHER_COUNTRY = 5;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_PLAN_FULL = 6;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_MEMBER = 7;
}

enum SupportFamilyPlanRevokeResult {
  SUPPORT_FAMIL
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07190"></a>
## FND-07190: chesscom.payments.v1.SupportFamilyPlanJoinStatus.SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_PREMIUM = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_PREMIUM = 4;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 547.

```text
MILY_PLAN_JOIN_STATUS_TRIAL_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_REMOVED_BY_OWNER = 3;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_PREMIUM = 4;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_OTHER_COUNTRY = 5;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_PLAN_FULL = 6;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_MEMBER = 7;
}

enum SupportFamilyPlanRevokeResult {
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_P
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07191"></a>
## FND-07191: chesscom.payments.v1.SupportFamilyPlanJoinStatus.SUPPORT_FAMILY_PLAN_JOIN_STATUS_OTHER_COUNTRY = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_JOIN_STATUS_OTHER_COUNTRY = 5;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 602.

```text
ILY_PLAN_JOIN_STATUS_REMOVED_BY_OWNER = 3;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_PREMIUM = 4;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_OTHER_COUNTRY = 5;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_PLAN_FULL = 6;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_MEMBER = 7;
}

enum SupportFamilyPlanRevokeResult {
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_REVOKED = 1;
  SUPPORT_FAMILY_PLAN_RE
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07192"></a>
## FND-07192: chesscom.payments.v1.SupportFamilyPlanJoinStatus.SUPPORT_FAMILY_PLAN_JOIN_STATUS_PLAN_FULL = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_JOIN_STATUS_PLAN_FULL = 6;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 655.

```text
FAMILY_PLAN_JOIN_STATUS_ALREADY_PREMIUM = 4;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_OTHER_COUNTRY = 5;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_PLAN_FULL = 6;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_MEMBER = 7;
}

enum SupportFamilyPlanRevokeResult {
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_REVOKED = 1;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_NOT_FOUND = 2;
}

enum SupportFamilyPlanC
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07193"></a>
## FND-07193: chesscom.payments.v1.SupportFamilyPlanJoinStatus.SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_MEMBER = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_MEMBER = 7;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 704.

```text
PPORT_FAMILY_PLAN_JOIN_STATUS_OTHER_COUNTRY = 5;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_PLAN_FULL = 6;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_MEMBER = 7;
}

enum SupportFamilyPlanRevokeResult {
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_REVOKED = 1;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_NOT_FOUND = 2;
}

enum SupportFamilyPlanCooldownResult {
  SUPPORT_FAMILY_PLAN_COOLDOWN_RE
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07194"></a>
## FND-07194: enum declaration: chesscom.payments.v1.SupportFamilyPlanRevokeResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SupportFamilyPlanRevokeResult {

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 759.

```text
ORT_FAMILY_PLAN_JOIN_STATUS_PLAN_FULL = 6;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_MEMBER = 7;
}

enum SupportFamilyPlanRevokeResult {
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_REVOKED = 1;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_NOT_FOUND = 2;
}

enum SupportFamilyPlanCooldownResult {
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RE
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07195"></a>
## FND-07195: chesscom.payments.v1.SupportFamilyPlanRevokeResult.SUPPORT_FAMILY_PLAN_REVOKE_RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_REVOKE_RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 798.

```text
 6;
  SUPPORT_FAMILY_PLAN_JOIN_STATUS_ALREADY_MEMBER = 7;
}

enum SupportFamilyPlanRevokeResult {
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_REVOKED = 1;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_NOT_FOUND = 2;
}

enum SupportFamilyPlanCooldownResult {
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_CLEARED = 1;
  SUPPORT_FAMILY_PLAN
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07196"></a>
## FND-07196: chesscom.payments.v1.SupportFamilyPlanRevokeResult.SUPPORT_FAMILY_PLAN_REVOKE_RESULT_REVOKED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_REVOKE_RESULT_REVOKED = 1;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 851.

```text
= 7;
}

enum SupportFamilyPlanRevokeResult {
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_REVOKED = 1;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_NOT_FOUND = 2;
}

enum SupportFamilyPlanCooldownResult {
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_CLEARED = 1;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NOT_IN_COOLDOWN = 2;
  SUPPORT_FAMIL
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07197"></a>
## FND-07197: chesscom.payments.v1.SupportFamilyPlanRevokeResult.SUPPORT_FAMILY_PLAN_REVOKE_RESULT_NOT_FOUND = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_REVOKE_RESULT_NOT_FOUND = 2;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 900.

```text
PPORT_FAMILY_PLAN_REVOKE_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_REVOKED = 1;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_NOT_FOUND = 2;
}

enum SupportFamilyPlanCooldownResult {
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_CLEARED = 1;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NOT_IN_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NO_PLAN = 3;
  SUPPORT_FAM
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07198"></a>
## FND-07198: enum declaration: chesscom.payments.v1.SupportFamilyPlanCooldownResult

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum SupportFamilyPlanCooldownResult {

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 952.

```text
UPPORT_FAMILY_PLAN_REVOKE_RESULT_REVOKED = 1;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_NOT_FOUND = 2;
}

enum SupportFamilyPlanCooldownResult {
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_CLEARED = 1;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NOT_IN_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NO_PLAN = 3;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_PLAN_NOT_TRIAL = 4;
  SUPPO
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07199"></a>
## FND-07199: chesscom.payments.v1.SupportFamilyPlanCooldownResult.SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_UNSPECIFIED = 0;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 993.

```text
= 1;
  SUPPORT_FAMILY_PLAN_REVOKE_RESULT_NOT_FOUND = 2;
}

enum SupportFamilyPlanCooldownResult {
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_CLEARED = 1;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NOT_IN_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NO_PLAN = 3;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_PLAN_NOT_TRIAL = 4;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_FRIEND_NOT
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07200"></a>
## FND-07200: chesscom.payments.v1.SupportFamilyPlanCooldownResult.SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_CLEARED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_CLEARED = 1;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1048.

```text

}

enum SupportFamilyPlanCooldownResult {
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_CLEARED = 1;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NOT_IN_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NO_PLAN = 3;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_PLAN_NOT_TRIAL = 4;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_FRIEND_NOT_FROM_THIS_OWNER = 5;
}

message SupportFamilyPlanInvit
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07201"></a>
## FND-07201: chesscom.payments.v1.SupportFamilyPlanCooldownResult.SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NOT_IN_COOLDOWN = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NOT_IN_COOLDOWN = 2;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1099.

```text
T_FAMILY_PLAN_COOLDOWN_RESULT_UNSPECIFIED = 0;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_CLEARED = 1;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NOT_IN_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NO_PLAN = 3;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_PLAN_NOT_TRIAL = 4;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_FRIEND_NOT_FROM_THIS_OWNER = 5;
}

message SupportFamilyPlanInvitation {
  optional string invitation_ref = 1;
  opt
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07202"></a>
## FND-07202: chesscom.payments.v1.SupportFamilyPlanCooldownResult.SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NO_PLAN = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NO_PLAN = 3;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1158.

```text
MILY_PLAN_COOLDOWN_RESULT_CLEARED = 1;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NOT_IN_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NO_PLAN = 3;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_PLAN_NOT_TRIAL = 4;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_FRIEND_NOT_FROM_THIS_OWNER = 5;
}

message SupportFamilyPlanInvitation {
  optional string invitation_ref = 1;
  optional string invitee_user_uuid = 2;
  optional string invit
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07203"></a>
## FND-07203: chesscom.payments.v1.SupportFamilyPlanCooldownResult.SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_PLAN_NOT_TRIAL = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_PLAN_NOT_TRIAL = 4;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1209.

```text
MILY_PLAN_COOLDOWN_RESULT_NOT_IN_COOLDOWN = 2;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_NO_PLAN = 3;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_PLAN_NOT_TRIAL = 4;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_FRIEND_NOT_FROM_THIS_OWNER = 5;
}

message SupportFamilyPlanInvitation {
  optional string invitation_ref = 1;
  optional string invitee_user_uuid = 2;
  optional string invitee_username = 3;
  optional string masked_email = 4
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07204"></a>
## FND-07204: chesscom.payments.v1.SupportFamilyPlanCooldownResult.SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_FRIEND_NOT_FROM_THIS_OWNER = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_FRIEND_NOT_FROM_THIS_OWNER = 5;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1267.

```text
AMILY_PLAN_COOLDOWN_RESULT_NO_PLAN = 3;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_PLAN_NOT_TRIAL = 4;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_FRIEND_NOT_FROM_THIS_OWNER = 5;
}

message SupportFamilyPlanInvitation {
  optional string invitation_ref = 1;
  optional string invitee_user_uuid = 2;
  optional string invitee_username = 3;
  optional string masked_email = 4;
  optional .google.protobuf.Timestamp expires_at = 5;
}

```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07205"></a>
## FND-07205: message declaration: chesscom.payments.v1.SupportFamilyPlanInvitation

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SupportFamilyPlanInvitation {

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1338.

```text
RESULT_PLAN_NOT_TRIAL = 4;
  SUPPORT_FAMILY_PLAN_COOLDOWN_RESULT_FRIEND_NOT_FROM_THIS_OWNER = 5;
}

message SupportFamilyPlanInvitation {
  optional string invitation_ref = 1;
  optional string invitee_user_uuid = 2;
  optional string invitee_username = 3;
  optional string masked_email = 4;
  optional .google.protobuf.Timestamp expires_at = 5;
}

message SupportFamilyPlanInviteeCheck {
  optional string user_uuid = 
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07206"></a>
## FND-07206: chesscom.payments.v1.SupportFamilyPlanInvitation.invitation_ref = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string invitation_ref = 1;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1378.

```text
ILY_PLAN_COOLDOWN_RESULT_FRIEND_NOT_FROM_THIS_OWNER = 5;
}

message SupportFamilyPlanInvitation {
  optional string invitation_ref = 1;
  optional string invitee_user_uuid = 2;
  optional string invitee_username = 3;
  optional string masked_email = 4;
  optional .google.protobuf.Timestamp expires_at = 5;
}

message SupportFamilyPlanInviteeCheck {
  optional string user_uuid = 1;
  optional .chesscom.payments.v1.Supp
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07207"></a>
## FND-07207: chesscom.payments.v1.SupportFamilyPlanInvitation.invitee_user_uuid = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string invitee_user_uuid = 2;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1416.

```text
OM_THIS_OWNER = 5;
}

message SupportFamilyPlanInvitation {
  optional string invitation_ref = 1;
  optional string invitee_user_uuid = 2;
  optional string invitee_username = 3;
  optional string masked_email = 4;
  optional .google.protobuf.Timestamp expires_at = 5;
}

message SupportFamilyPlanInviteeCheck {
  optional string user_uuid = 1;
  optional .chesscom.payments.v1.SupportFamilyPlanJoinStatus status = 2;
  
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07208"></a>
## FND-07208: chesscom.payments.v1.SupportFamilyPlanInvitation.invitee_username = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string invitee_username = 3;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1457.

```text
lyPlanInvitation {
  optional string invitation_ref = 1;
  optional string invitee_user_uuid = 2;
  optional string invitee_username = 3;
  optional string masked_email = 4;
  optional .google.protobuf.Timestamp expires_at = 5;
}

message SupportFamilyPlanInviteeCheck {
  optional string user_uuid = 1;
  optional .chesscom.payments.v1.SupportFamilyPlanJoinStatus status = 2;
  optional .google.protobuf.Timestamp trial
```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07209"></a>
## FND-07209: chesscom.payments.v1.SupportFamilyPlanInvitation.masked_email = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string masked_email = 4;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1497.

```text
itation_ref = 1;
  optional string invitee_user_uuid = 2;
  optional string invitee_username = 3;
  optional string masked_email = 4;
  optional .google.protobuf.Timestamp expires_at = 5;
}

message SupportFamilyPlanInviteeCheck {
  optional string user_uuid = 1;
  optional .chesscom.payments.v1.SupportFamilyPlanJoinStatus status = 2;
  optional .google.protobuf.Timestamp trial_cooldown_ends_at = 3;
}

```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07210"></a>
## FND-07210: chesscom.payments.v1.SupportFamilyPlanInvitation.expires_at = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp expires_at = 5;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1533.

```text
nvitee_user_uuid = 2;
  optional string invitee_username = 3;
  optional string masked_email = 4;
  optional .google.protobuf.Timestamp expires_at = 5;
}

message SupportFamilyPlanInviteeCheck {
  optional string user_uuid = 1;
  optional .chesscom.payments.v1.SupportFamilyPlanJoinStatus status = 2;
  optional .google.protobuf.Timestamp trial_cooldown_ends_at = 3;
}

```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07211"></a>
## FND-07211: message declaration: chesscom.payments.v1.SupportFamilyPlanInviteeCheck

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message SupportFamilyPlanInviteeCheck {

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1588.

```text
e = 3;
  optional string masked_email = 4;
  optional .google.protobuf.Timestamp expires_at = 5;
}

message SupportFamilyPlanInviteeCheck {
  optional string user_uuid = 1;
  optional .chesscom.payments.v1.SupportFamilyPlanJoinStatus status = 2;
  optional .google.protobuf.Timestamp trial_cooldown_ends_at = 3;
}

```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07212"></a>
## FND-07212: chesscom.payments.v1.SupportFamilyPlanInviteeCheck.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1630.

```text

  optional .google.protobuf.Timestamp expires_at = 5;
}

message SupportFamilyPlanInviteeCheck {
  optional string user_uuid = 1;
  optional .chesscom.payments.v1.SupportFamilyPlanJoinStatus status = 2;
  optional .google.protobuf.Timestamp trial_cooldown_ends_at = 3;
}

```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07213"></a>
## FND-07213: chesscom.payments.v1.SupportFamilyPlanInviteeCheck.status = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.payments.v1.SupportFamilyPlanJoinStatus status = 2;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1663.

```text
stamp expires_at = 5;
}

message SupportFamilyPlanInviteeCheck {
  optional string user_uuid = 1;
  optional .chesscom.payments.v1.SupportFamilyPlanJoinStatus status = 2;
  optional .google.protobuf.Timestamp trial_cooldown_ends_at = 3;
}

```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07214"></a>
## FND-07214: chesscom.payments.v1.SupportFamilyPlanInviteeCheck.trial_cooldown_ends_at = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .google.protobuf.Timestamp trial_cooldown_ends_at = 3;

### Evidence

- **SRC-0513** `research/proto/chesscom/payments/v1/support_family_plan.proto` — [preserved redacted evidence](../evidence/text/120f60e23364aa50983b7dd41efcdf5e78c7d1375ac8cf06bcb3f8c444390a60.proto)
  Character offset 1736.

```text
al string user_uuid = 1;
  optional .chesscom.payments.v1.SupportFamilyPlanJoinStatus status = 2;
  optional .google.protobuf.Timestamp trial_cooldown_ends_at = 3;
}

```

**Source references:** SRC-0513, SRC-1484  
**URL references:** None independently associated  
**Related findings:** FND-07180, FND-07181, FND-07182

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07215"></a>
## FND-07215: message declaration: chesscom.payments.v1.CheckMemberPromotionsRequest

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CheckMemberPromotionsRequest {

### Evidence

- **SRC-0514** `research/proto/chesscom/payments/v1/support_promotion_service.proto` — [preserved redacted evidence](../evidence/text/c30f22bb7053b56581028f275b5b134b44fb2d771dd5cbda07019934c06d95b2.proto)
  Character offset 114.

```text
sscom/payments/v1/support_promotion_service.proto
// syntax: proto3

package chesscom.payments.v1;

message CheckMemberPromotionsRequest {
  optional string user_uuid = 1;
  optional string code = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string verification_id = 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

message CheckMemberPromotionsResponse {
  repeated .chesscom.
```

**Source references:** SRC-0514, SRC-1485  
**URL references:** None independently associated  
**Related findings:** FND-07216, FND-07217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07216"></a>
## FND-07216: chesscom.payments.v1.CheckMemberPromotionsRequest.user_uuid = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string user_uuid = 1;

### Evidence

- **SRC-0514** `research/proto/chesscom/payments/v1/support_promotion_service.proto` — [preserved redacted evidence](../evidence/text/c30f22bb7053b56581028f275b5b134b44fb2d771dd5cbda07019934c06d95b2.proto)
  Character offset 155.

```text
ce.proto
// syntax: proto3

package chesscom.payments.v1;

message CheckMemberPromotionsRequest {
  optional string user_uuid = 1;
  optional string code = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string verification_id = 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

message CheckMemberPromotionsResponse {
  repeated .chesscom.payments.v1.MemberPromotion offers = 1;
 
```

**Source references:** SRC-0514, SRC-1485  
**URL references:** None independently associated  
**Related findings:** FND-07215, FND-07217

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07217"></a>
## FND-07217: chesscom.payments.v1.CheckMemberPromotionsRequest.code = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string code = 2;

### Evidence

- **SRC-0514** `research/proto/chesscom/payments/v1/support_promotion_service.proto` — [preserved redacted evidence](../evidence/text/c30f22bb7053b56581028f275b5b134b44fb2d771dd5cbda07019934c06d95b2.proto)
  Character offset 188.

```text
ge chesscom.payments.v1;

message CheckMemberPromotionsRequest {
  optional string user_uuid = 1;
  optional string code = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string verification_id = 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

message CheckMemberPromotionsResponse {
  repeated .chesscom.payments.v1.MemberPromotion offers = 1;
  repeated .chesscom.payments.v1.P
```

**Source references:** SRC-0514, SRC-1485  
**URL references:** None independently associated  
**Related findings:** FND-07215, FND-07216

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07218"></a>
## FND-07218: chesscom.payments.v1.CheckMemberPromotionsRequest.context = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionContext context = 3;

### Evidence

- **SRC-0514** `research/proto/chesscom/payments/v1/support_promotion_service.proto` — [preserved redacted evidence](../evidence/text/c30f22bb7053b56581028f275b5b134b44fb2d771dd5cbda07019934c06d95b2.proto)
  Character offset 216.

```text
ssage CheckMemberPromotionsRequest {
  optional string user_uuid = 1;
  optional string code = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string verification_id = 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

message CheckMemberPromotionsResponse {
  repeated .chesscom.payments.v1.MemberPromotion offers = 1;
  repeated .chesscom.payments.v1.PromotionOnCharge applied = 2
```

**Source references:** SRC-0514, SRC-1485  
**URL references:** None independently associated  
**Related findings:** FND-07215, FND-07216, FND-07217

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07219"></a>
## FND-07219: chesscom.payments.v1.CheckMemberPromotionsRequest.verification_id = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional string verification_id = 4;

### Evidence

- **SRC-0514** `research/proto/chesscom/payments/v1/support_promotion_service.proto` — [preserved redacted evidence](../evidence/text/c30f22bb7053b56581028f275b5b134b44fb2d771dd5cbda07019934c06d95b2.proto)
  Character offset 282.

```text
 1;
  optional string code = 2;
  optional .chesscom.support.v1.SupportActionContext context = 3;
  optional string verification_id = 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

message CheckMemberPromotionsResponse {
  repeated .chesscom.payments.v1.MemberPromotion offers = 1;
  repeated .chesscom.payments.v1.PromotionOnCharge applied = 2;
  optional bool code_applied = 3;
  optional .chesscom.support.v
```

**Source references:** SRC-0514, SRC-1485  
**URL references:** None independently associated  
**Related findings:** FND-07215, FND-07216, FND-07217

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07220"></a>
## FND-07220: chesscom.payments.v1.CheckMemberPromotionsRequest.platform = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.api.v1.Platform platform = 5;

### Evidence

- **SRC-0514** `research/proto/chesscom/payments/v1/support_promotion_service.proto` — [preserved redacted evidence](../evidence/text/c30f22bb7053b56581028f275b5b134b44fb2d771dd5cbda07019934c06d95b2.proto)
  Character offset 321.

```text
nal .chesscom.support.v1.SupportActionContext context = 3;
  optional string verification_id = 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

message CheckMemberPromotionsResponse {
  repeated .chesscom.payments.v1.MemberPromotion offers = 1;
  repeated .chesscom.payments.v1.PromotionOnCharge applied = 2;
  optional bool code_applied = 3;
  optional .chesscom.support.v1.SupportActionResult action_result = 4
```

**Source references:** SRC-0514, SRC-1485  
**URL references:** None independently associated  
**Related findings:** FND-07215, FND-07216, FND-07217

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07221"></a>
## FND-07221: message declaration: chesscom.payments.v1.CheckMemberPromotionsResponse

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

message CheckMemberPromotionsResponse {

### Evidence

- **SRC-0514** `research/proto/chesscom/payments/v1/support_promotion_service.proto` — [preserved redacted evidence](../evidence/text/c30f22bb7053b56581028f275b5b134b44fb2d771dd5cbda07019934c06d95b2.proto)
  Character offset 373.

```text
t = 3;
  optional string verification_id = 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

message CheckMemberPromotionsResponse {
  repeated .chesscom.payments.v1.MemberPromotion offers = 1;
  repeated .chesscom.payments.v1.PromotionOnCharge applied = 2;
  optional bool code_applied = 3;
  optional .chesscom.support.v1.SupportActionResult action_result = 4;
}

```

**Source references:** SRC-0514, SRC-1485  
**URL references:** None independently associated  
**Related findings:** FND-07215, FND-07216, FND-07217

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07222"></a>
## FND-07222: chesscom.payments.v1.CheckMemberPromotionsResponse.offers = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.MemberPromotion offers = 1;

### Evidence

- **SRC-0514** `research/proto/chesscom/payments/v1/support_promotion_service.proto` — [preserved redacted evidence](../evidence/text/c30f22bb7053b56581028f275b5b134b44fb2d771dd5cbda07019934c06d95b2.proto)
  Character offset 415.

```text
 4;
  optional .chesscom.api.v1.Platform platform = 5;
}

message CheckMemberPromotionsResponse {
  repeated .chesscom.payments.v1.MemberPromotion offers = 1;
  repeated .chesscom.payments.v1.PromotionOnCharge applied = 2;
  optional bool code_applied = 3;
  optional .chesscom.support.v1.SupportActionResult action_result = 4;
}

```

**Source references:** SRC-0514, SRC-1485  
**URL references:** None independently associated  
**Related findings:** FND-07215, FND-07216, FND-07217

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07223"></a>
## FND-07223: chesscom.payments.v1.CheckMemberPromotionsResponse.applied = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

repeated .chesscom.payments.v1.PromotionOnCharge applied = 2;

### Evidence

- **SRC-0514** `research/proto/chesscom/payments/v1/support_promotion_service.proto` — [preserved redacted evidence](../evidence/text/c30f22bb7053b56581028f275b5b134b44fb2d771dd5cbda07019934c06d95b2.proto)
  Character offset 476.

```text
sage CheckMemberPromotionsResponse {
  repeated .chesscom.payments.v1.MemberPromotion offers = 1;
  repeated .chesscom.payments.v1.PromotionOnCharge applied = 2;
  optional bool code_applied = 3;
  optional .chesscom.support.v1.SupportActionResult action_result = 4;
}

```

**Source references:** SRC-0514, SRC-1485  
**URL references:** None independently associated  
**Related findings:** FND-07215, FND-07216, FND-07217

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07224"></a>
## FND-07224: chesscom.payments.v1.CheckMemberPromotionsResponse.code_applied = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional bool code_applied = 3;

### Evidence

- **SRC-0514** `research/proto/chesscom/payments/v1/support_promotion_service.proto` — [preserved redacted evidence](../evidence/text/c30f22bb7053b56581028f275b5b134b44fb2d771dd5cbda07019934c06d95b2.proto)
  Character offset 540.

```text
ts.v1.MemberPromotion offers = 1;
  repeated .chesscom.payments.v1.PromotionOnCharge applied = 2;
  optional bool code_applied = 3;
  optional .chesscom.support.v1.SupportActionResult action_result = 4;
}

```

**Source references:** SRC-0514, SRC-1485  
**URL references:** None independently associated  
**Related findings:** FND-07215, FND-07216, FND-07217

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07225"></a>
## FND-07225: chesscom.payments.v1.CheckMemberPromotionsResponse.action_result = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

optional .chesscom.support.v1.SupportActionResult action_result = 4;

### Evidence

- **SRC-0514** `research/proto/chesscom/payments/v1/support_promotion_service.proto` — [preserved redacted evidence](../evidence/text/c30f22bb7053b56581028f275b5b134b44fb2d771dd5cbda07019934c06d95b2.proto)
  Character offset 574.

```text
  repeated .chesscom.payments.v1.PromotionOnCharge applied = 2;
  optional bool code_applied = 3;
  optional .chesscom.support.v1.SupportActionResult action_result = 4;
}

```

**Source references:** SRC-0514, SRC-1485  
**URL references:** None independently associated  
**Related findings:** FND-07215, FND-07216, FND-07217

**Additional notes:** Schema declaration only; does not prove a deployed API endpoint or a populated runtime field.

<a id="FND-07226"></a>
## FND-07226: enum declaration: chesscom.permissions.v1.PremiumFeature

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PremiumFeature {

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 111.

```text
chesscom/permissions/v1/premium_features.proto
// syntax: proto3

package chesscom.permissions.v1;

enum PremiumFeature {
  PREMIUM_FEATURE_UNSPECIFIED = 0;
  PREMIUM_FEATURE_PUZZLES_RATED = 1;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UN
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07227"></a>
## FND-07227: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_UNSPECIFIED = 0;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 135.

```text
premium_features.proto
// syntax: proto3

package chesscom.permissions.v1;

enum PremiumFeature {
  PREMIUM_FEATURE_UNSPECIFIED = 0;
  PREMIUM_FEATURE_PUZZLES_RATED = 1;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEA
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07228"></a>
## FND-07228: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_PUZZLES_RATED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_PUZZLES_RATED = 1;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 170.

```text
roto3

package chesscom.permissions.v1;

enum PremiumFeature {
  PREMIUM_FEATURE_UNSPECIFIED = 0;
  PREMIUM_FEATURE_PUZZLES_RATED = 1;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_F
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07229"></a>
## FND-07229: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_NO_ADS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_NO_ADS = 2;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 207.

```text
1;

enum PremiumFeature {
  PREMIUM_FEATURE_UNSPECIFIED = 0;
  PREMIUM_FEATURE_PUZZLES_RATED = 1;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATU
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07230"></a>
## FND-07230: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_PUZZLE_RUSH = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_PUZZLE_RUSH = 3;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 237.

```text
EMIUM_FEATURE_UNSPECIFIED = 0;
  PREMIUM_FEATURE_PUZZLES_RATED = 1;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FE
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07231"></a>
## FND-07231: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_LESSONS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_LESSONS = 4;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 272.

```text
EMIUM_FEATURE_PUZZLES_RATED = 1;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_FLAIR_PREMIUM = 12;
  PREMIUM
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07232"></a>
## FND-07232: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_ANALYSIS = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_ANALYSIS = 5;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 303.

```text
;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_FLAIR_PREMIUM = 12;
  PREMIUM_FEATURE_FLAIR_STAR = 13;
  PRE
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07233"></a>
## FND-07233: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_VIDEOS = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_VIDEOS = 6;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 335.

```text
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_FLAIR_PREMIUM = 12;
  PREMIUM_FEATURE_FLAIR_STAR = 13;
  PREMIUM_FEATURE_FLAIR_CROWN = 14;
 
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07234"></a>
## FND-07234: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_ENDGAMES_TRAINER = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 365.

```text
= 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_FLAIR_PREMIUM = 12;
  PREMIUM_FEATURE_FLAIR_STAR = 13;
  PREMIUM_FEATURE_FLAIR_CROWN = 14;
  PREMIUM_FEATURE_FLAIR_DIAMOND
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07235"></a>
## FND-07235: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_PUZZLES_UNRATED = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_PUZZLES_UNRATED = 8;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 405.

```text
EMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_FLAIR_PREMIUM = 12;
  PREMIUM_FEATURE_FLAIR_STAR = 13;
  PREMIUM_FEATURE_FLAIR_CROWN = 14;
  PREMIUM_FEATURE_FLAIR_DIAMOND = 15;
  PREMIUM_FEATURE_BOTS = 16;
  PR
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07236"></a>
## FND-07236: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_PUZZLE_BATTLE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_PUZZLE_BATTLE = 9;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 444.

```text
EATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_FLAIR_PREMIUM = 12;
  PREMIUM_FEATURE_FLAIR_STAR = 13;
  PREMIUM_FEATURE_FLAIR_CROWN = 14;
  PREMIUM_FEATURE_FLAIR_DIAMOND = 15;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PRE
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07237"></a>
## FND-07237: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_INSIGHTS = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_INSIGHTS = 10;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 481.

```text
ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_FLAIR_PREMIUM = 12;
  PREMIUM_FEATURE_FLAIR_STAR = 13;
  PREMIUM_FEATURE_FLAIR_CROWN = 14;
  PREMIUM_FEATURE_FLAIR_DIAMOND = 15;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07238"></a>
## FND-07238: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_EXPLORER = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_EXPLORER = 11;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 514.

```text
EATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_FLAIR_PREMIUM = 12;
  PREMIUM_FEATURE_FLAIR_STAR = 13;
  PREMIUM_FEATURE_FLAIR_CROWN = 14;
  PREMIUM_FEATURE_FLAIR_DIAMOND = 15;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_C
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07239"></a>
## FND-07239: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_FLAIR_PREMIUM = 12

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_FLAIR_PREMIUM = 12;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 547.

```text
MIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_FLAIR_PREMIUM = 12;
  PREMIUM_FEATURE_FLAIR_STAR = 13;
  PREMIUM_FEATURE_FLAIR_CROWN = 14;
  PREMIUM_FEATURE_FLAIR_DIAMOND = 15;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COU
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07240"></a>
## FND-07240: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_FLAIR_STAR = 13

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_FLAIR_STAR = 13;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 585.

```text
IUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_FLAIR_PREMIUM = 12;
  PREMIUM_FEATURE_FLAIR_STAR = 13;
  PREMIUM_FEATURE_FLAIR_CROWN = 14;
  PREMIUM_FEATURE_FLAIR_DIAMOND = 15;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIU
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07241"></a>
## FND-07241: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_FLAIR_CROWN = 14

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_FLAIR_CROWN = 14;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 620.

```text
M_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_FLAIR_PREMIUM = 12;
  PREMIUM_FEATURE_FLAIR_STAR = 13;
  PREMIUM_FEATURE_FLAIR_CROWN = 14;
  PREMIUM_FEATURE_FLAIR_DIAMOND = 15;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;
 
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07242"></a>
## FND-07242: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_FLAIR_DIAMOND = 15

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_FLAIR_DIAMOND = 15;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 656.

```text
EATURE_FLAIR_PREMIUM = 12;
  PREMIUM_FEATURE_FLAIR_STAR = 13;
  PREMIUM_FEATURE_FLAIR_CROWN = 14;
  PREMIUM_FEATURE_FLAIR_DIAMOND = 15;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;
  PREMIUM_FEATURE_ADVANCED_STATS = 22
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07243"></a>
## FND-07243: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_BOTS = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_BOTS = 16;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 694.

```text
EATURE_FLAIR_STAR = 13;
  PREMIUM_FEATURE_FLAIR_CROWN = 14;
  PREMIUM_FEATURE_FLAIR_DIAMOND = 15;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;
  PREMIUM_FEATURE_ADVANCED_STATS = 22;
  PREMIUM_FEATURE_DAILY_PUZZLE_EXPLA
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07244"></a>
## FND-07244: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_PLAY_VS_COACH = 17

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_PLAY_VS_COACH = 17;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 723.

```text
MIUM_FEATURE_FLAIR_CROWN = 14;
  PREMIUM_FEATURE_FLAIR_DIAMOND = 15;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;
  PREMIUM_FEATURE_ADVANCED_STATS = 22;
  PREMIUM_FEATURE_DAILY_PUZZLE_EXPLANATIONS = 23;
  PREMIUM_FEATU
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07245"></a>
## FND-07245: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 761.

```text
UM_FEATURE_FLAIR_DIAMOND = 15;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;
  PREMIUM_FEATURE_ADVANCED_STATS = 22;
  PREMIUM_FEATURE_DAILY_PUZZLE_EXPLANATIONS = 23;
  PREMIUM_FEATURE_DRILLS = 24;
  PREMIUM_FEATURE_TIME
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07246"></a>
## FND-07246: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 807.

```text
RE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;
  PREMIUM_FEATURE_ADVANCED_STATS = 22;
  PREMIUM_FEATURE_DAILY_PUZZLE_EXPLANATIONS = 23;
  PREMIUM_FEATURE_DRILLS = 24;
  PREMIUM_FEATURE_TIME_OUT_PROTECTION = 25;
  PREMIUM_FEATURE_PREMIU
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07247"></a>
## FND-07247: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 848.

```text
OACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;
  PREMIUM_FEATURE_ADVANCED_STATS = 22;
  PREMIUM_FEATURE_DAILY_PUZZLE_EXPLANATIONS = 23;
  PREMIUM_FEATURE_DRILLS = 24;
  PREMIUM_FEATURE_TIME_OUT_PROTECTION = 25;
  PREMIUM_FEATURE_PREMIUM_TOURNAMENTS = 26;
  PREMIUM_FEATURE_PLA
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07248"></a>
## FND-07248: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 899.

```text
= 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;
  PREMIUM_FEATURE_ADVANCED_STATS = 22;
  PREMIUM_FEATURE_DAILY_PUZZLE_EXPLANATIONS = 23;
  PREMIUM_FEATURE_DRILLS = 24;
  PREMIUM_FEATURE_TIME_OUT_PROTECTION = 25;
  PREMIUM_FEATURE_PREMIUM_TOURNAMENTS = 26;
  PREMIUM_FEATURE_PLAY_MULTIPLE_GAMES = 27;
  PREMIUM_FEATURE_PREMIUM_MA
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07249"></a>
## FND-07249: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_ADVANCED_STATS = 22

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_ADVANCED_STATS = 22;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 941.

```text
 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;
  PREMIUM_FEATURE_ADVANCED_STATS = 22;
  PREMIUM_FEATURE_DAILY_PUZZLE_EXPLANATIONS = 23;
  PREMIUM_FEATURE_DRILLS = 24;
  PREMIUM_FEATURE_TIME_OUT_PROTECTION = 25;
  PREMIUM_FEATURE_PREMIUM_TOURNAMENTS = 26;
  PREMIUM_FEATURE_PLAY_MULTIPLE_GAMES = 27;
  PREMIUM_FEATURE_PREMIUM_MATCHMAKING = 28;
  PREMIUM_FEATURE_DAILY_PU
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07250"></a>
## FND-07250: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_DAILY_PUZZLE_EXPLANATIONS = 23

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_DAILY_PUZZLE_EXPLANATIONS = 23;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 980.

```text
D_PREVIEWS = 20;
  PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;
  PREMIUM_FEATURE_ADVANCED_STATS = 22;
  PREMIUM_FEATURE_DAILY_PUZZLE_EXPLANATIONS = 23;
  PREMIUM_FEATURE_DRILLS = 24;
  PREMIUM_FEATURE_TIME_OUT_PROTECTION = 25;
  PREMIUM_FEATURE_PREMIUM_TOURNAMENTS = 26;
  PREMIUM_FEATURE_PLAY_MULTIPLE_GAMES = 27;
  PREMIUM_FEATURE_PREMIUM_MATCHMAKING = 28;
  PREMIUM_FEATURE_DAILY_PUZZLES_HISTORY = 29;
  PREMIUM_FEATURE_H
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07251"></a>
## FND-07251: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_DRILLS = 24

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_DRILLS = 24;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 1030.

```text
NS = 21;
  PREMIUM_FEATURE_ADVANCED_STATS = 22;
  PREMIUM_FEATURE_DAILY_PUZZLE_EXPLANATIONS = 23;
  PREMIUM_FEATURE_DRILLS = 24;
  PREMIUM_FEATURE_TIME_OUT_PROTECTION = 25;
  PREMIUM_FEATURE_PREMIUM_TOURNAMENTS = 26;
  PREMIUM_FEATURE_PLAY_MULTIPLE_GAMES = 27;
  PREMIUM_FEATURE_PREMIUM_MATCHMAKING = 28;
  PREMIUM_FEATURE_DAILY_PUZZLES_HISTORY = 29;
  PREMIUM_FEATURE_HIDE_INTERNAL_ADS_SETTING = 33;
  PREMIUM_FEATURE_B
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07252"></a>
## FND-07252: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_TIME_OUT_PROTECTION = 25

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_TIME_OUT_PROTECTION = 25;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 1061.

```text
NCED_STATS = 22;
  PREMIUM_FEATURE_DAILY_PUZZLE_EXPLANATIONS = 23;
  PREMIUM_FEATURE_DRILLS = 24;
  PREMIUM_FEATURE_TIME_OUT_PROTECTION = 25;
  PREMIUM_FEATURE_PREMIUM_TOURNAMENTS = 26;
  PREMIUM_FEATURE_PLAY_MULTIPLE_GAMES = 27;
  PREMIUM_FEATURE_PREMIUM_MATCHMAKING = 28;
  PREMIUM_FEATURE_DAILY_PUZZLES_HISTORY = 29;
  PREMIUM_FEATURE_HIDE_INTERNAL_ADS_SETTING = 33;
  PREMIUM_FEATURE_BRILLIANT_MOVES = 34;
  PREMIUM_
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07253"></a>
## FND-07253: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_PREMIUM_TOURNAMENTS = 26

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_PREMIUM_TOURNAMENTS = 26;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 1105.

```text
ZLE_EXPLANATIONS = 23;
  PREMIUM_FEATURE_DRILLS = 24;
  PREMIUM_FEATURE_TIME_OUT_PROTECTION = 25;
  PREMIUM_FEATURE_PREMIUM_TOURNAMENTS = 26;
  PREMIUM_FEATURE_PLAY_MULTIPLE_GAMES = 27;
  PREMIUM_FEATURE_PREMIUM_MATCHMAKING = 28;
  PREMIUM_FEATURE_DAILY_PUZZLES_HISTORY = 29;
  PREMIUM_FEATURE_HIDE_INTERNAL_ADS_SETTING = 33;
  PREMIUM_FEATURE_BRILLIANT_MOVES = 34;
  PREMIUM_FEATURE_BOT_EVENT_MONETIZATION = 35;
  PREMI
```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07254"></a>
## FND-07254: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_PLAY_MULTIPLE_GAMES = 27

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_PLAY_MULTIPLE_GAMES = 27;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 1149.

```text
LLS = 24;
  PREMIUM_FEATURE_TIME_OUT_PROTECTION = 25;
  PREMIUM_FEATURE_PREMIUM_TOURNAMENTS = 26;
  PREMIUM_FEATURE_PLAY_MULTIPLE_GAMES = 27;
  PREMIUM_FEATURE_PREMIUM_MATCHMAKING = 28;
  PREMIUM_FEATURE_DAILY_PUZZLES_HISTORY = 29;
  PREMIUM_FEATURE_HIDE_INTERNAL_ADS_SETTING = 33;
  PREMIUM_FEATURE_BRILLIANT_MOVES = 34;
  PREMIUM_FEATURE_BOT_EVENT_MONETIZATION = 35;
  PREMIUM_FEATURE_OPENING_COURSES = 36;
}

```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07255"></a>
## FND-07255: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_PREMIUM_MATCHMAKING = 28

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_PREMIUM_MATCHMAKING = 28;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 1193.

```text
ION = 25;
  PREMIUM_FEATURE_PREMIUM_TOURNAMENTS = 26;
  PREMIUM_FEATURE_PLAY_MULTIPLE_GAMES = 27;
  PREMIUM_FEATURE_PREMIUM_MATCHMAKING = 28;
  PREMIUM_FEATURE_DAILY_PUZZLES_HISTORY = 29;
  PREMIUM_FEATURE_HIDE_INTERNAL_ADS_SETTING = 33;
  PREMIUM_FEATURE_BRILLIANT_MOVES = 34;
  PREMIUM_FEATURE_BOT_EVENT_MONETIZATION = 35;
  PREMIUM_FEATURE_OPENING_COURSES = 36;
}

```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07256"></a>
## FND-07256: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_DAILY_PUZZLES_HISTORY = 29

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_DAILY_PUZZLES_HISTORY = 29;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 1237.

```text
NTS = 26;
  PREMIUM_FEATURE_PLAY_MULTIPLE_GAMES = 27;
  PREMIUM_FEATURE_PREMIUM_MATCHMAKING = 28;
  PREMIUM_FEATURE_DAILY_PUZZLES_HISTORY = 29;
  PREMIUM_FEATURE_HIDE_INTERNAL_ADS_SETTING = 33;
  PREMIUM_FEATURE_BRILLIANT_MOVES = 34;
  PREMIUM_FEATURE_BOT_EVENT_MONETIZATION = 35;
  PREMIUM_FEATURE_OPENING_COURSES = 36;
}

```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07257"></a>
## FND-07257: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_HIDE_INTERNAL_ADS_SETTING = 33

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_HIDE_INTERNAL_ADS_SETTING = 33;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 1283.

```text
S = 27;
  PREMIUM_FEATURE_PREMIUM_MATCHMAKING = 28;
  PREMIUM_FEATURE_DAILY_PUZZLES_HISTORY = 29;
  PREMIUM_FEATURE_HIDE_INTERNAL_ADS_SETTING = 33;
  PREMIUM_FEATURE_BRILLIANT_MOVES = 34;
  PREMIUM_FEATURE_BOT_EVENT_MONETIZATION = 35;
  PREMIUM_FEATURE_OPENING_COURSES = 36;
}

```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07258"></a>
## FND-07258: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_BRILLIANT_MOVES = 34

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_BRILLIANT_MOVES = 34;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 1333.

```text
;
  PREMIUM_FEATURE_DAILY_PUZZLES_HISTORY = 29;
  PREMIUM_FEATURE_HIDE_INTERNAL_ADS_SETTING = 33;
  PREMIUM_FEATURE_BRILLIANT_MOVES = 34;
  PREMIUM_FEATURE_BOT_EVENT_MONETIZATION = 35;
  PREMIUM_FEATURE_OPENING_COURSES = 36;
}

```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07259"></a>
## FND-07259: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_BOT_EVENT_MONETIZATION = 35

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_BOT_EVENT_MONETIZATION = 35;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 1373.

```text
Y = 29;
  PREMIUM_FEATURE_HIDE_INTERNAL_ADS_SETTING = 33;
  PREMIUM_FEATURE_BRILLIANT_MOVES = 34;
  PREMIUM_FEATURE_BOT_EVENT_MONETIZATION = 35;
  PREMIUM_FEATURE_OPENING_COURSES = 36;
}

```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07260"></a>
## FND-07260: chesscom.permissions.v1.PremiumFeature.PREMIUM_FEATURE_OPENING_COURSES = 36

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_OPENING_COURSES = 36;

### Evidence

- **SRC-0515** `research/proto/chesscom/permissions/v1/premium_features.proto` — [preserved redacted evidence](../evidence/text/b29ddb197e15bfd4fdcf9495527dde4cfe28587571f4cec2f9c432d7c748dc38.proto)
  Character offset 1420.

```text
TING = 33;
  PREMIUM_FEATURE_BRILLIANT_MOVES = 34;
  PREMIUM_FEATURE_BOT_EVENT_MONETIZATION = 35;
  PREMIUM_FEATURE_OPENING_COURSES = 36;
}

```

**Source references:** SRC-0515, SRC-1486  
**URL references:** None independently associated  
**Related findings:** FND-07226, FND-07227, FND-07228

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07261"></a>
## FND-07261: enum declaration: chesscom.premium_access.v1.PremiumFeature

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

enum PremiumFeature {

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 106.

```text
rce: chesscom/premium_access/v1/enums.proto
// syntax: proto3

package chesscom.premium_access.v1;

enum PremiumFeature {
  PREMIUM_FEATURE_UNSPECIFIED = 0;
  PREMIUM_FEATURE_PUZZLES_RATED = 1;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UN
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07262, FND-07263

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07262"></a>
## FND-07262: chesscom.premium_access.v1.PremiumFeature.PREMIUM_FEATURE_UNSPECIFIED = 0

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_UNSPECIFIED = 0;

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 130.

```text
cess/v1/enums.proto
// syntax: proto3

package chesscom.premium_access.v1;

enum PremiumFeature {
  PREMIUM_FEATURE_UNSPECIFIED = 0;
  PREMIUM_FEATURE_PUZZLES_RATED = 1;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEA
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07261, FND-07263

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07263"></a>
## FND-07263: chesscom.premium_access.v1.PremiumFeature.PREMIUM_FEATURE_PUZZLES_RATED = 1

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_PUZZLES_RATED = 1;

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 165.

```text
o3

package chesscom.premium_access.v1;

enum PremiumFeature {
  PREMIUM_FEATURE_UNSPECIFIED = 0;
  PREMIUM_FEATURE_PUZZLES_RATED = 1;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_F
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07261, FND-07262

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07264"></a>
## FND-07264: chesscom.premium_access.v1.PremiumFeature.PREMIUM_FEATURE_NO_ADS = 2

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_NO_ADS = 2;

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 202.

```text
1;

enum PremiumFeature {
  PREMIUM_FEATURE_UNSPECIFIED = 0;
  PREMIUM_FEATURE_PUZZLES_RATED = 1;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATU
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07261, FND-07262, FND-07263

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07265"></a>
## FND-07265: chesscom.premium_access.v1.PremiumFeature.PREMIUM_FEATURE_PUZZLE_RUSH = 3

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_PUZZLE_RUSH = 3;

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 232.

```text
EMIUM_FEATURE_UNSPECIFIED = 0;
  PREMIUM_FEATURE_PUZZLES_RATED = 1;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FE
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07261, FND-07262, FND-07263

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07266"></a>
## FND-07266: chesscom.premium_access.v1.PremiumFeature.PREMIUM_FEATURE_LESSONS = 4

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_LESSONS = 4;

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 267.

```text
EMIUM_FEATURE_PUZZLES_RATED = 1;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07261, FND-07262, FND-07263

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07267"></a>
## FND-07267: chesscom.premium_access.v1.PremiumFeature.PREMIUM_FEATURE_ANALYSIS = 5

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_ANALYSIS = 5;

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 298.

```text
;
  PREMIUM_FEATURE_NO_ADS = 2;
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_F
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07261, FND-07262, FND-07263

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07268"></a>
## FND-07268: chesscom.premium_access.v1.PremiumFeature.PREMIUM_FEATURE_VIDEOS = 6

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_VIDEOS = 6;

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 330.

```text
  PREMIUM_FEATURE_PUZZLE_RUSH = 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 1
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07261, FND-07262, FND-07263

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07269"></a>
## FND-07269: chesscom.premium_access.v1.PremiumFeature.PREMIUM_FEATURE_ENDGAMES_TRAINER = 7

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 360.

```text
= 3;
  PREMIUM_FEATURE_LESSONS = 4;
  PREMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07261, FND-07262, FND-07263

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07270"></a>
## FND-07270: chesscom.premium_access.v1.PremiumFeature.PREMIUM_FEATURE_PUZZLES_UNRATED = 8

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_PUZZLES_UNRATED = 8;

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 400.

```text
EMIUM_FEATURE_ANALYSIS = 5;
  PREMIUM_FEATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07261, FND-07262, FND-07263

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07271"></a>
## FND-07271: chesscom.premium_access.v1.PremiumFeature.PREMIUM_FEATURE_PUZZLE_BATTLE = 9

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_PUZZLE_BATTLE = 9;

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 439.

```text
EATURE_VIDEOS = 6;
  PREMIUM_FEATURE_ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIUM_FEAT
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07261, FND-07262, FND-07263

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07272"></a>
## FND-07272: chesscom.premium_access.v1.PremiumFeature.PREMIUM_FEATURE_INSIGHTS = 10

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_INSIGHTS = 10;

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 476.

```text
ENDGAMES_TRAINER = 7;
  PREMIUM_FEATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;
  PREMIUM
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07261, FND-07262, FND-07263

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07273"></a>
## FND-07273: chesscom.premium_access.v1.PremiumFeature.PREMIUM_FEATURE_EXPLORER = 11

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_EXPLORER = 11;

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 509.

```text
EATURE_PUZZLES_UNRATED = 8;
  PREMIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;
  PREMIUM_FEATURE_ADVANCED_STATS = 22;
  P
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07261, FND-07262, FND-07263

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.

<a id="FND-07274"></a>
## FND-07274: chesscom.premium_access.v1.PremiumFeature.PREMIUM_FEATURE_BOTS = 16

**Category:** data_models  
**Classification:** verified observation  
**Verification:** verified  
**Confidence:** high — Exact content of the cited stored artifact; not a claim of current live deployment.

PREMIUM_FEATURE_BOTS = 16;

### Evidence

- **SRC-0516** `research/proto/chesscom/premium_access/v1/enums.proto` — [preserved redacted evidence](../evidence/text/9e67a90c11122ce2657c2140c20858942e9b4644b40bd1160422b267f4d5a2f0.proto)
  Character offset 542.

```text
MIUM_FEATURE_PUZZLE_BATTLE = 9;
  PREMIUM_FEATURE_INSIGHTS = 10;
  PREMIUM_FEATURE_EXPLORER = 11;
  PREMIUM_FEATURE_BOTS = 16;
  PREMIUM_FEATURE_PLAY_VS_COACH = 17;
  PREMIUM_FEATURE_COURSES_SPECIAL_PRICE = 18;
  PREMIUM_FEATURE_EXCLUSIVE_COURSE = 19;
  PREMIUM_FEATURE_COURSES_UNLIMITED_PREVIEWS = 20;
  PREMIUM_FEATURE_MOVE_EXPLANATIONS = 21;
  PREMIUM_FEATURE_ADVANCED_STATS = 22;
  PREMIUM_FEATURE_OFFLINE_PUZZLES = 
```

**Source references:** SRC-0516, SRC-1487  
**URL references:** None independently associated  
**Related findings:** FND-07261, FND-07262, FND-07263

**Additional notes:** No additional caveat recorded beyond the source scope and confidence above.
